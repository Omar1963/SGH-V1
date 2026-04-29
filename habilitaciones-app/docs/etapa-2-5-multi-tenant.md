# Etapa 2.5 - Flujo funcional core y multi-tenant

## 1. Objetivo

Normalizar el comportamiento multi-tenant para que los usuarios `EMPRESA` solo vean y actúen sobre sus propios datos, mientras que los roles internos consultora mantengan acceso global.

## 2. Regla de acceso central

- `EMPRESA`: acceso restringido a `empresa_id` propio.
- `ADMIN_CONSULTORA`, `RESPONSABLE_HABILITACIONES`, `OPERADOR_CONSULTORA`: acceso global a datos de empresas.
- `AUDITOR`: no se ha habilitado un permiso específico en esta etapa; el módulo se reserva para futuros requisitos de solo lectura.

## 3. Módulos validados

### Personas
- `GET /personas`: listagem filtrada por `empresa_id` para usuarios EMPRESA.
- `GET /personas/{id}`: validación de pertenencia por empresa.
- `POST /personas`: EMPRESA fuerza su propio `empresa_id` en la creación.
- `PUT /personas/{id}` y `PATCH /personas/{id}`: solo permite actualización si la persona pertenece a la misma empresa para el rol EMPRESA.
- `DELETE /personas/{id}`: mismo aislamiento por empresa.

### Documentos
- `GET /documentos`: EMPRESA ve solo documentos asociados a personas de su empresa.
- `POST /documentos` y `POST /documentos/upload`: EMPRESA solo puede subir documentos para personas dentro de su empresa.
- `GET /documentos/{id}` y `/download`: acceso validado por empresa.
- `PUT /documentos/{id}/status`, `/aprobar`, `/rechazar`: solo roles consultora, EMPRESA no puede cambiar estado.

### Habilitaciones
- `GET /habilitaciones`: EMPRESA solo ve habilitaciones de sus personas.
- `POST /habilitaciones`: EMPRESA solo puede crear habilitaciones para sus propias personas.
- `GET /habilitaciones/{id}`: acceso validado por empresa.

### Dashboard
- `GET /dashboard/summary`: datos consolidados por empresa cuando el usuario es EMPRESA.
- `GET /dashboard/builder/{id}` y builder CRUD: EMPRESA solo puede acceder a dashboards que pertenezcan a su propia empresa.

## 4. Estado de implementación

- Reglas de aislamiento implementadas en `PersonaService`, `DocumentoService`, `HabilitacionService` y `DashboardService`.
- El contrato API para los flujos de empresa ya está presente y expuesto en OpenAPI.
- La etapa 2.5 queda principalemente pendiente de pruebas E2E de aislamiento y refuerzo de reglas de acceso de roles adicionales.

## 5. Criterios de aceptación

- [x] Usuario EMPRESA solo ve personas, documentos y habilitaciones de su empresa.
- [x] Usuario EMPRESA solo puede subir documentos para su propio `empresa_id`.
- [x] Usuarios consultora mantienen acceso global.
- [ ] Se debe validar con pruebas automatizadas que el aislamiento no se rompe en los endpoints críticos.

## 6. Riesgos y observaciones

- El backend ya implementa el aislamiento, pero falta el coverage de pruebas que verifique casos de uso cruzado de empresa.
- Aún no se definieron roles `DATA_ENTRY` y `VISITA` en el backend; esos perfiles quedan para la etapa 2.6/2.7 si se requiere visibilidad de solo lectura.
- La lógica de consulta analítica del dashboard continúa en placeholder; la validación funcional de dashboard queda limitada a creación/edición de metadatos.
