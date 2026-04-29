/* global bootstrap */

import api from './api.js';
import auth from './auth.js';
import { buildApiUrl } from './api.js';

/**
 * documentos.js - Lógica para la gestión documental.
 */

const documentos = {
    /**
     * Inicializa la vista de documentos
     */
    async init() {
        await this.loadDocumentos();
        this.setupEventListeners();
    },

    /**
     * Carga el listado de documentos desde la API
     */
    async loadDocumentos() {
        const tableBody = document.getElementById('documentosTableBody');
        if (!tableBody) return;

        tableBody.innerHTML = '<tr><td colspan="6" class="text-center">Cargando...</td></tr>';

        try {
            const data = await api.get('/documentos/');
            tableBody.innerHTML = '';

            data.forEach(doc => {
                const role = auth.getUserRole();
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${doc.id}</td>
                    <td><strong>${doc.tipo}</strong></td>
                    <td><sup>ID:</sup> ${doc.persona_id || doc.empresa_id || 'N/A'}</td>
                    <td><span class="badge ${this.getStatusBadgeClass(doc.estado)}">${doc.estado}</span></td>
                    <td>${doc.fecha_vencimiento ? new Date(doc.fecha_vencimiento).toLocaleDateString() : '-'}</td>
                    <td class="text-end">
                        <div class="btn-group">
                            <button class="btn btn-sm btn-outline-success download-btn" data-id="${doc.id}" title="Descargar">
                                <i class="fas fa-download"></i>
                            </button>
                            ${(role === 'ADMIN_CONSULTORA' || role === 'RESPONSABLE_HABILITACIONES') && doc.estado === 'PENDIENTE_REVISION' ? `
                                <button class="btn btn-sm btn-success approve-btn" data-id="${doc.id}" title="Aprobar">
                                    <i class="fas fa-check"></i>
                                </button>
                                <button class="btn btn-sm btn-danger reject-btn" data-id="${doc.id}" title="Rechazar">
                                    <i class="fas fa-times"></i>
                                </button>
                            ` : ''}
                        </div>
                    </td>
                `;
                tableBody.appendChild(tr);
            });

            this.setupActionButtons();

        } catch (error) {
            tableBody.innerHTML = `<tr><td colspan="6" class="text-center text-danger">Error: ${error.message}</td></tr>`;
        }
    },

    /**
     * Retorna la clase de CSS para el badge según el estado
     */
    getStatusBadgeClass(estado) {
        const classes = {
            'PENDIENTE_EMPRESA': 'bg-secondary',
            'PENDIENTE_REVISION': 'bg-primary',
            'APROBADO': 'bg-success',
            'RECHAZADO': 'bg-danger',
            'VENCIDO': 'bg-dark'
        };
        return classes[estado] || 'bg-light';
    },

    /**
     * Setea los listeners
     */
    setupEventListeners() {
        const form = document.getElementById('uploadForm');
        if (form) {
            form.addEventListener('submit', async (e) => {
                e.preventDefault();
                await this.handleUpload();
            });
        }
    },

    /**
     * Setea los botones de la tabla (descargas y auditoría)
     */
    setupActionButtons() {
        document.querySelectorAll('.download-btn').forEach(btn => {
            btn.addEventListener('click', async (e) => {
                const id = e.currentTarget.dataset.id;
                await this.handleDownload(id);
            });
        });

        document.querySelectorAll('.approve-btn').forEach(btn => {
            btn.addEventListener('click', async (e) => {
                const id = e.currentTarget.dataset.id;
                if (confirm('¿Confirmar aprobación de este documento?')) {
                    await this.handleUpdateStatus(id, 'APROBADO');
                }
            });
        });

        document.querySelectorAll('.reject-btn').forEach(btn => {
            btn.addEventListener('click', async (e) => {
                const id = e.currentTarget.dataset.id;
                if (confirm('¿Confirmar rechazo de este documento?')) {
                    await this.handleUpdateStatus(id, 'RECHAZADO');
                }
            });
        });
    },

    /**
     * Actualiza el estado de un documento
     */
    async handleUpdateStatus(id, nuevoEstado) {
        try {
            await api.request(`/documentos/${id}/status?nuevo_estado=${nuevoEstado}`, {
                method: 'PUT'
            });
            await this.loadDocumentos();
        } catch (error) {
            alert('Error al actualizar estado: ' + error.message);
        }
    },

    /**
     * Procesa la subida de un archivo
     */
    async handleUpload() {
        const fileInput = document.getElementById('fileInput');
        if (!fileInput.files[0]) return alert('Seleccione un archivo');

        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        formData.append('tipo', document.getElementById('tipo_documento').value);
        formData.append('jurisdiccion', 'CABA');
        formData.append('fecha_presentacion', new Date().toISOString().slice(0, 10));

        const personaId = document.getElementById('persona_id_link').value;
        if (personaId) formData.append('persona_id', personaId);

        try {
            // Nota: api.post usa JSON.stringify. Para FormData usamos fetch directo con el token.
            const token = localStorage.getItem('token');
            const response = await fetch(buildApiUrl('/documentos/upload'), {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`
                },
                body: formData
            });

            if (!response.ok) throw new Error('Error al subir archivo');

            const modalEl = document.getElementById('uploadModal');
            const modal = bootstrap.Modal.getInstance(modalEl);
            modal.hide();

            document.getElementById('uploadForm').reset();
            await this.loadDocumentos();

        } catch (error) {
            alert('Error: ' + error.message);
        }
    },

    /**
     * Maneja la descarga de archivos
     */
    async handleDownload(id) {
        try {
            const token = localStorage.getItem('token');
            const response = await fetch(buildApiUrl(`/documentos/${id}/download`), {
                headers: { 'Authorization': `Bearer ${token}` }
            });

            if (!response.ok) throw new Error('No se pudo descargar el archivo');

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `documento_${id}`; // Deberíamos obtener el nombre original del backend preferiblemente
            document.body.appendChild(a);
            a.click();
            a.remove();
        } catch (error) {
            alert('Error en descarga: ' + error.message);
        }
    }
};

// Auto-inicialización
if (document.getElementById('documentosTableBody')) {
    documentos.init();
}

export default documentos;
