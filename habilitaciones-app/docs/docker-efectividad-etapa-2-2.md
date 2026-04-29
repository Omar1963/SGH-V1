# Etapa 2.2 - Efectividad de Docker y estandar de ejecucion

Fecha: 2026-04-29

## Resultado ejecutivo
Docker es efectivo para SGH-V1 en integracion, QA y demos, con estrategia hibrida recomendada:
- `docker-first` para stack completo reproducible.
- `venv + vite` para desarrollo diario rapido.

## Hallazgos tecnicos (estado previo)
- `depends_on` sin `healthchecks`: arranque no determinista entre `db -> backend -> frontend`.
- Sin volumen de datos para PostgreSQL: riesgo de perdida de datos al recrear contenedores.
- Diagnostico acoplado a nombre fijo de red (`habilitaciones-app_default`) no consistente con el compose actual.

## Ajustes implementados
- `docker-compose.yml`:
  - `db` con `healthcheck` (`pg_isready`) y volumen persistente `postgres_data`.
  - `backend` con `depends_on: db: service_healthy` y `healthcheck` HTTP.
  - `frontend` con `depends_on: backend: service_healthy` y `healthcheck` HTTP.
- `diagnose.ps1`:
  - Resolucion dinamica del nombre de red desde `docker compose config`.

## Decision operativa
1. Dev rapido: backend local + frontend local, con `db` por Docker.
2. Integracion: stack completo por Docker Compose.
3. Demo/QA: stack completo por Docker Compose con healthchecks.

## Riesgos abiertos
- Warning de permisos en `C:\Users\Admin\.docker\config.json` (acceso denegado).
- Falta medir tiempos reales de `up --build` en ejecucion limpia.

## Criterios de salida de la etapa (pendientes de medicion)
- `docker compose up --build` <= 8 minutos.
- 3 arranques consecutivos sin falla >= 95%.
- 0 errores por dependencia de servicios.
