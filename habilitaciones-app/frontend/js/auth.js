import { buildApiUrl } from './api.js';

/**
 * auth.js - Gestion de estado y sesion de usuario.
 */
const auth = {
    async login(username, password) {
        try {
            const formData = new URLSearchParams();
            formData.append('username', username);
            formData.append('password', password);

            const response = await fetch(buildApiUrl('/auth/login'), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Credenciales invalidas');
            }

            const data = await response.json();
            localStorage.setItem('token', data.access_token);
            localStorage.setItem('last_username', username);
            return data;
        } catch (error) {
            console.error('Login Error:', error);
            throw error;
        }
    },

    logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        window.location.href = '/login.html';
    },

    isAuthenticated() {
        return !!localStorage.getItem('token');
    },

    parseTokenPayload() {
        const token = localStorage.getItem('token');
        if (!token) return null;
        try {
            const base64Url = token.split('.')[1];
            const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
            const jsonPayload = decodeURIComponent(
                window
                    .atob(base64)
                    .split('')
                    .map((c) => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
                    .join('')
            );
            return JSON.parse(jsonPayload);
        } catch {
            return null;
        }
    },

    getUserRole() {
        const payload = this.parseTokenPayload();
        return payload?.role || null;
    },

    getRoleLabel() {
        const role = this.getUserRole();
        const labels = {
            ADMIN_CONSULTORA: 'Admin',
            RESPONSABLE_HABILITACIONES: 'Admin',
            OPERADOR_CONSULTORA: 'DataEntry',
            EMPRESA: 'Empresa',
            AUDITOR: 'Visita',
        };
        return labels[role] || 'Sin Rol';
    },

    applyUIPermissions() {
        const role = this.getUserRole();
        if (!role) return;

        const roleBadge = document.getElementById('roleBadge');
        if (roleBadge) {
            roleBadge.textContent = this.getRoleLabel();
        }

        const userNameDisplay = document.getElementById('userNameDisplay');
        if (userNameDisplay) {
            userNameDisplay.textContent = localStorage.getItem('last_username') || 'Usuario';
        }

        const roleAwareItems = document.querySelectorAll('[data-roles]');
        roleAwareItems.forEach((item) => {
            const allowed = (item.getAttribute('data-roles') || '')
                .split(',')
                .map((r) => r.trim())
                .filter(Boolean);
            if (allowed.length && !allowed.includes(role)) {
                item.style.display = 'none';
            }
        });
    },
};

export default auth;
