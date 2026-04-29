# Etapa 2.4 - Matriz de Contrato API (Plan vs Implementado)

Fecha: 2026-04-29
Base path: `/api/v1`
Fuente funcional: `Documento Maestro`

## 1) Modulos esperados vs estado (actualizado)

| Modulo | Esperado (Documento Maestro) | Estado actual | Brecha |
|---|---|---|---|
| `/auth` | Login + me + logout | `POST /auth/login`, `GET /auth/me`, `POST /auth/logout` | Cubierto |
| `/personas` | CRUD + PATCH | GET/POST/GET by id/PUT/PATCH/DELETE | Cubierto |
| `/empresas` | CRUD + `/empresas/{id}/personas` | CRUD + personas por empresa | Cubierto |
| `/documentos` | alta + aprobar/rechazar | alta (`/` y `/upload`), aprobar/rechazar, estado, descarga | Cubierto |
| `/estados` | modulo dedicado | listado/alta/get/patch | Cubierto minimo |
| `/habilitaciones` | alta + consulta | list/create/get by id | Cubierto |
| `/alertas` | listado + emision | listado/alta/emitir | Cubierto minimo |
| `/dashboard` | vistas/kpis de tablero | `GET /dashboard/summary` | Parcial (pendiente desagregado) |
| `/reportes` | reportes operativos/regulatorios | `GET /reportes/{tipo}`, `POST /reportes/{tipo}/pdf` | Cubierto minimo |
| `/empresa/*` | acceso externo dedicado | `GET /empresa/personas`, `POST /empresa/documentos` | Cubierto |

## 2) Endpoints criticos (Documento Maestro)

| Endpoint esperado | Estado actual |
|---|---|
| `GET /personas` | Implementado |
| `POST /personas` | Implementado |
| `GET /personas/{id}` | Implementado |
| `PATCH /personas/{id}` | No implementado (existe `PUT`) |
| `POST /documentos` | Parcialmente implementado como `POST /documentos/upload` (multipart) |
| `POST /documentos/{id}/aprobar` | No implementado (se usa `PUT /documentos/{id}/status?nuevo_estado=APROBADO`) |
| `POST /documentos/{id}/rechazar` | No implementado (se usa `PUT /documentos/{id}/status?nuevo_estado=RECHAZADO`) |
| `GET /empresa/personas` | No implementado |
| `POST /empresa/documentos` | No implementado |

## 3) Cobertura estimada de contrato critico

- Cobertura estimada: **~90%** de endpoints/modulos criticos definidos.
- Ambiguedades activas:
  - `/dashboard` continua consolidado en `summary` (faltan vistas especializadas por KPI).
  - `/reportes` y `/estados` implementados en modo minimo contractual (pendiente logica de negocio avanzada).

## 4) Prioridad de cierre (siguiente etapa técnica)

1. Completar lógica funcional de `reportes` (datos reales + exportación).
2. Completar lógica de `estados/recalcular` según flujo documental.
3. Expandir `dashboard` en endpoints desagregados por vista/KPI.
4. Agregar tests de integración por endpoint crítico.

## 5) Estado de cierre de la Etapa 2.4

- Contrato mínimo de `auth`: implementado (`POST /auth/login`, `GET /auth/me`, `POST /auth/logout`).
- Contrato mínimo de `personas`: implementado (`GET /personas`, `POST /personas`, `GET /personas/{id}`, `PUT/PATCH /personas/{id}`, `DELETE /personas/{id}`).
- Contrato mínimo de `empresas`: implementado para administradores con CRUD y lista de personas por empresa (`GET /empresas/{empresa_id}/personas`).
- Contrato mínimo de `documentos`: implementado con alias contractual `POST /documentos` y flujo de file upload, estado, descarga y aprobación/rechazo.
- Contrato mínimo de `estados`: implementado con CRUD básico en `/estados`.
- Contrato mínimo de `habilitaciones`: implementado con list/create/get básico.
- Contrato mínimo de `alertas`: implementado con endpoints básicos.
- Contrato mínimo de `dashboard`: actualizado con resumen y constructor `dashboard-builder`.
- Contrato mínimo de `empresa/*`: implementado con `GET /empresa/personas` y `POST /empresa/documentos`.

## 6) Observaciones de cobertura

- La API de `dashboard` ahora incluye el constructor V1 de tableros y el catálogo de visualizaciones.
- La implementación de `reportes` y `estados` sigue en modo mínimo contractual; falta completar la generación de datos reales y exportación avanzada.
- El contrato está completo para la mayoría de endpoints críticos; la principal deuda es funcionalidad interna, no presencia de rutas.

## 7) Riesgos abiertos

- Validación de reglas de negocio en `reportes` y `estados` aún no está suficientemente cubierta.
- Faltan tests E2E que verifiquen el aislamiento de empresa y las transiciones de estado documental.
- El módulo de `dashboard-builder` todavía depende de una consulta placeholder en el backend.

## 8) Recomendación

Avanzar con la Etapa 2.5 sobre multi-tenant y reglas de acceso antes de invertir en la capa analítica completa de dashboard. La API básica ya está normalizada, y los siguientes pasos deben enfocarse en seguridad funcional y pruebas de flujo.
