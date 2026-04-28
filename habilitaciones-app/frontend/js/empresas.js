/* global bootstrap */
import api from './api.js';


/**
 * empresas.js - Lógica para la gestión de empresas.
 */

const empresas = {
    /**
     * Inicializa la vista de empresas
     */
    async init() {
        await this.loadEmpresas();
        this.setupEventListeners();
    },

    /**
     * Carga el listado de empresas desde la API
     */
    async loadEmpresas() {
        const tableBody = document.getElementById('empresasTableBody');
        if (!tableBody) return;

        tableBody.innerHTML = '<tr><td colspan="4" class="text-center">Cargando...</td></tr>';

        try {
            const data = await api.get('/empresas/');
            tableBody.innerHTML = '';

            data.forEach(empresa => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${empresa.id}</td>
                    <td><strong>${empresa.razon_social}</strong></td>
                    <td>${empresa.cuit}</td>
                    <td class="text-end">
                        <button class="btn btn-sm btn-outline-primary edit-btn" data-id="${empresa.id}">
                            <i class="fas fa-edit"></i>
                        </button>
                    </td>
                `;
                tableBody.appendChild(tr);
            });
        } catch (error) {
            tableBody.innerHTML = `<tr><td colspan="4" class="text-center text-danger">Error: ${error.message}</td></tr>`;
        }
    },

    /**
     * Setea los listeners de la página
     */
    setupEventListeners() {
        const form = document.getElementById('empresaForm');
        if (form) {
            form.addEventListener('submit', async (e) => {
                e.preventDefault();
                await this.handleCreateEmpresa();
            });
        }
    },

    /**
     * Procesa la creación de una nueva empresa
     */
    async handleCreateEmpresa() {
        const data = {
            razon_social: document.getElementById('razon_social').value,
            cuit: document.getElementById('cuit').value,
            direccion: document.getElementById('direccion').value
        };

        try {
            await api.post('/empresas/', data);

            // Cerrar modal (Bootstrap 5 way)
            const modalEl = document.getElementById('empresaModal');
            const modal = bootstrap.Modal.getInstance(modalEl);
            modal.hide();

            // Limpiar y recargar
            document.getElementById('empresaForm').reset();
            await this.loadEmpresas();

        } catch (error) {
            alert('Error al crear empresa: ' + error.message);
        }
    }
};

// Auto-inicialización si el elemento existe
if (document.getElementById('empresasTableBody')) {
    empresas.init();
}

export default empresas;
