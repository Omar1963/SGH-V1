# SGH-V1: Documentación Técnica

Bienvenido a la documentación del **Sistema Integral de Habilitaciones (SGH-V1)**.

## Estructura del Proyecto

- `/backend`: API construida con FastAPI, SQLAlchemy 2.0 y PostgreSQL.
- `/frontend`: Aplicación SPA con React, Vite, Tailwind CSS y Bootstrap 5.
- `/docker`: Archivos de configuración para contenedores Docker.
- `/docs`: Guías de usuario y especificaciones técnicas.

## Guía de Inicio Rápido (Docker)

1. Asegúrate de tener Docker y Docker Compose instalados.
2. Desde la raíz del proyecto ejecutiva:
   ```bash
   docker-compose -f docker/docker-compose.yml up --build
   ```
3. Accede a:
   - Frontend: `http://localhost:5173`
   - Backend Docs: `http://localhost:8000/docs`

## Contacto e Instrucciones para Agentes
Para cualquier modificación, referirse siempre al **Documento Maestro** en la raíz del repositorio original.
