import api from './api.js';

/**
 * auth.js - Gestión de estado y sesión de usuario.
 */

const auth = {
    /**
     * Inicia sesión y almacena el token
     */
    async login(username, password) {
        try {
            const formData = new URLSearchParams();
            formData.append('username', username);
            formData.append('password', password);

            // Nota: OAuth2 Password flow usa x-www-form-urlencoded
            const response = await fetch('http://localhost:8000/api/v1/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData
            });

            if (!response.ok) {
                throw new Error('Credenciales inválidas');
            }

            const data = await response.json();
            localStorage.setItem('token', data.access_token);
            
            // Opcional: Almacenar datos básicos del usuario
            // const user = await api.get('/auth/me');
            // localStorage.setItem('user', JSON.stringify(user));

            return data;
        } catch (error) {
            console.error('Login Error:', error);
            throw error;
        }
    },

    /**
     * Cierra la sesión
     */
    logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        window.location.href = '/login.html';
    },

    /**
     * Verifica si el usuario está autenticado
     */
    isAuthenticated() {
        return !!localStorage.getItem('token');
    },

    /**
     * Obtiene el rol del usuario desde el almacenamiento
     */
    getUserRole() {
        const token = localStorage.getItem('token');
        if (!token) return null;
        
        // Decodificar JWT (parte payload) para obtener datos sin pegarle a la API cada vez
        try {
            const base64Url = token.split('.')[1];
            const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
            const jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            }).join(''));

            const payload = JSON.parse(jsonPayload);
            return payload.role; // Asumimos que el backend incluyó 'role' en el sub o claims
        } catch (e) {
            return null;
        }
    },

    /**
     * Aplica restricciones de UI basadas en el rol
     */
    applyUIPermissions() {
        const role = this.getUserRole();
        if (!role) return;

        // Si es EMPRESA, ocultar gestión de otras empresas
        if (role === 'EMPRESA') {
            const empresaLinks = document.querySelectorAll('.nav-link[href="empresas.html"]');
            empresaLinks.forEach(el => el.parentElement.style.display = 'none');
        }
    }
};

export default auth;
