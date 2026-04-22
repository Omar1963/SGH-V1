/**
 * api.js - Wrapper modular para fetch()
 * Centraliza las peticiones al backend y maneja la inyección de JWT.
 */

const BASE_URL = 'http://localhost:8000/api/v1';

const api = {
    /**
     * Realiza una petición genérica
     */
    async request(endpoint, options = {}) {
        const token = localStorage.getItem('token');
        const headers = {
            'Content-Type': 'application/json',
            ...options.headers,
        };

        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        const config = {
            ...options,
            headers,
        };

        try {
            const response = await fetch(`${BASE_URL}${endpoint}`, config);

            // Manejo de expiración de token (401 Unauthorized)
            if (response.status === 401) {
                console.error('Sesión expirada o no autorizada');
                localStorage.removeItem('token');
                if (!window.location.pathname.includes('login.html')) {
                    window.location.href = '/login.html';
                }
            }

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error en la petición');
            }

            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    },

    get(endpoint) {
        return this.request(endpoint, { method: 'GET' });
    },

    post(endpoint, data) {
        return this.request(endpoint, {
            method: 'POST',
            body: JSON.stringify(data),
        });
    },

    put(endpoint, data) {
        return this.request(endpoint, {
            method: 'PUT',
            body: JSON.stringify(data),
        });
    },

    delete(endpoint) {
        return this.request(endpoint, { method: 'DELETE' });
    }
};

export default api;
