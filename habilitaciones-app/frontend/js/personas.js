/* global bootstrap */
import api from './api.js';

/**
 * personas.js - Lógica para la gestión de personas (Personal).
 */

const personas = {
    /**
     * Inicializa la vista de personas
     */
    async init() {
        await this.loadPersonas();
        this.setupEventListeners();
    },

    /**
     * Carga el listado de personas desde la API
     */
    async loadPersonas() {
        const tableBody = document.getElementById('personasTableBody');
        if (!tableBody) return;

        tableBody.innerHTML = '<tr><td colspan="5" class="text-center">Cargando...</td></tr>';

        try {
            const data = await api.get('/personas/');
            tableBody.innerHTML = '';

            data.forEach(persona => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${persona.id}</td>
                    <td><strong>${persona.nombre} ${persona.apellido}</strong></td>
                    <td>${persona.dni}</td>
                    <td><span class="badge bg-secondary">${persona.cuil || '-'}</span></td>
                    <td class="text-end">
                        <button class="btn btn-sm btn-outline-primary info-btn" data-id="${persona.id}">
                            <i class="fas fa-eye"></i>
                        </button>
                    </td>
                `;
                tableBody.appendChild(tr);
            });
        } catch (error) {
            tableBody.innerHTML = `<tr><td colspan="5" class="text-center text-danger">Error: ${error.message}</td></tr>`;
        }
    },

    /**
     * Setea los listeners
     */
    setupEventListeners() {
        const form = document.getElementById('personaForm');
        if (form) {
            form.addEventListener('submit', async (e) => {
                e.preventDefault();
                await this.handleCreatePersona();
            });
        }
    },

    /**
     * Procesa la creación de una nueva persona
     */
    async handleCreatePersona() {
        const data = {
            nombre: document.getElementById('nombre').value,
            apellido: document.getElementById('apellido').value,
            dni: document.getElementById('dni').value,
            cuil: document.getElementById('cuil').value,
            empresa_id: parseInt(document.getElementById('empresa_id').value)
        };

        try {
            await api.post('/personas/', data);

            const modalEl = document.getElementById('personaModal');
            const modal = bootstrap.Modal.getInstance(modalEl);
            modal.hide();

            document.getElementById('personaForm').reset();
            await this.loadPersonas();

        } catch (error) {
            alert('Error al crear persona: ' + error.message);
        }
    }
};

// Auto-inicialización
if (document.getElementById('personasTableBody')) {
    personas.init();
}

export default personas;
