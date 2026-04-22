# SGH-V1 - Sistema Integral de Habilitaciones

## Arquitectura Técnica (Sprint 1)

### Stack Tecnológico
- **Backend**: FastAPI (Python 3.11) + SQLAlchemy 2.0 (Async) + Pydantic v2.
- **Frontend**: Vite + React 19 + Tailwind CSS v4 + Bootstrap 5.
- **Base de Datos**: PostgreSQL 15.
- **Orquestación**: Docker Compose.

### Estructura del Repositorio
- `/habilitaciones-app/backend`: Capa de servicios y lógica de negocio.
- `/habilitaciones-app/frontend`: Interfaz de usuario SPA.
- `/habilitaciones-app/docker`: Configuraciones de contenedores.
- `/habilitaciones-app/docs`: Documentación técnica y funcional.

### Despliegue en Desarrollo
1. `/habilitaciones-app$ docker-compose -f docker/docker-compose.yml up --build`

### Modelo de Datos (Sprint 2)
- **Motor ORM**: SQLAlchemy 2.0 (Estilo Mapped/mapped_column).
- **Entidades**: Empresa, Persona, Documento, Estado, Habilitación, Alerta, Usuario, Auditoría.
- **Relaciones**: 
  - Empresa (1) -> Persona (N)
  - Persona (1) -> [Documento, Estado, Habilitación, Alerta] (N)
  - Usuario (1) -> Auditoría (N)
- **Migraciones**: Gestionadas por Alembic (`alembic upgrade head`).

### Seguridad (Sprint 3)
- **Autenticación**: JWT (JSON Web Tokens) con algoritmo HS256.
- **Hashing**: BCrypt para contraseñas.
- **Autorización**: RBAC (Role-Based Access Control) con dependencias de FastAPI.
- **Multi-tenancy**: Filtrado de datos basado en `empresa_id` incorporado en el token.

### Variables de Entorno (.env)
- `POSTGRES_USER`: Usuario DB.
- `POSTGRES_PASSWORD`: Password DB.
- `POSTGRES_DB`: Nombre DB.
- `SECRET_KEY`: Llave para JWT.
