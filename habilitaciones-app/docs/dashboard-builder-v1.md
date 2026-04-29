# Especificación Dashboard Builder v1

## 1. Modelo de datos v1 (mínimo)
- dashboard_templates: plantillas base del sistema (globales, versionadas)
- dashboards: tablero creado por usuario (owner, nombre, descripción, visibilidad, timestamps)
- dashboard_widgets: widgets del tablero (tipo gráfico, dataset_key, métrica, dimensión, agregación, orden)
- dashboard_filters: filtros persistentes por tablero/widget (campo, operador, valor, scope)
- dashboard_shares: permisos de acceso por rol/usuario/empresa

## 2. Endpoints v1 (mínimos)
- GET /dashboard/catalog (datasets, métricas, dimensiones, tipos de gráfico permitidos)
- POST /dashboard-builder (crear tablero)
- GET /dashboard-builder/{id} (obtener tablero con widgets/filtros)
- PATCH /dashboard-builder/{id} (editar metadatos/tablero)
- POST /dashboard-builder/{id}/widgets (agregar widget)
- PATCH /dashboard-builder/{id}/widgets/{widget_id} (editar widget)
- DELETE /dashboard-builder/{id}/widgets/{widget_id} (eliminar widget)
- POST /dashboard-builder/{id}/query (ejecutar tablero con filtros runtime)
- POST /dashboard-builder/{id}/share (compartir por rol/usuario/empresa con reglas de acceso)

### Contrato API concreto
- GET /dashboard/catalog
  - Respuesta: `{datasets:[...], metrics:[...], dimensions:[...], chart_types:[...]}`
- POST /dashboard-builder
  - Request: `{nombre, descripcion?, visibilidad?, widgets?, filters?}`
  - Respuesta: dashboard con `id`, `owner_id`, `empresa_id`, `widgets[]`, `filters[]`, `shares[]`
- GET /dashboard-builder/{id}
  - Respuesta: dashboard completo con widgets, filtros y shares
- PATCH /dashboard-builder/{id}
  - Request: `{nombre?, descripcion?, visibilidad?}`
  - Respuesta: dashboard actualizado
- POST /dashboard-builder/{id}/widgets
  - Request: `{tipo, dataset_key, metric, dimension?, agregacion?, orden?, config?}`
  - Respuesta: widget creado
- PATCH /dashboard-builder/{id}/widgets/{widget_id}
  - Request: campos de widget opcionales
  - Respuesta: widget actualizado
- DELETE /dashboard-builder/{id}/widgets/{widget_id}
  - Respuesta: `204 No Content`
- POST /dashboard-builder/{id}/query
  - Respuesta: `{dashboard_id, results:[...], message?}`
- POST /dashboard-builder/{id}/share
  - Request: `{target_user_id?, target_role?, target_empresa_id?, permisos?}`
  - Respuesta: registro de compartido

## 3. UX mínima v1
- Constructor en 3 pasos: Datos -> Visualización -> Guardar
- Interacciones clave: agregar widget, duplicar widget, reordenar, guardar como borrador/publicado
- Biblioteca de visualizaciones inicial: KPI, línea, barras, torta/donut, tabla analítica
- Estados de UI: loading, vacío, error de consulta, sin permisos

## 4. Matriz de reglas de acceso por rol
| Rol        | Crear | Editar | Ver | Compartir |
|------------|-------|--------|-----|-----------|
| Admin      |  X    |   X    |  X  |     X     |
| Empresa    |  X    |   X    |  X  |     X     |
| DataEntry  |       |        |  X  |           |
| Visita     |       |        |  X  |           |

## 5. Criterios de aceptación E2E
- Ambigüedad de especificación: 0 campos/endpoint sin definición
- Tasa de cambios de alcance post-aprobación: <= 10%
- Éxito: backend, frontend y QA validan la misma especificación sin conflictos
