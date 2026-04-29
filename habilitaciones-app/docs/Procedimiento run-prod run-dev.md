# Procedimiento run-prod / run-dev

Fecha: 2026-04-29

## Objetivo
Ejecutar verificaciones de funcionamiento de SGH-V1 en dos modos:
- `run-dev.bat`: desarrollo iterativo.
- `run-prod.bat`: validacion de stack containerizado.

## Prerrequisitos comunes
1. Docker Desktop iniciado.
2. Proyecto ubicado en `C:\Users\Admin\GitHub\SGH-V1\habilitaciones-app`.
3. PowerShell/CMD con permisos para ejecutar Docker.

## A) Verificacion con run-dev.bat (modo desarrollo)

### Que hace
1. Valida `backend\.venv\Scripts\python.exe`.
2. Levanta solo DB en Docker.
3. Espera a que Postgres responda (`pg_isready`).
4. Ejecuta migraciones Alembic.
5. Levanta backend FastAPI en recarga (`--reload`) en `:8000`.
6. Levanta frontend Vite en `:5173`.

### Pasos
1. Abrir CMD en `habilitaciones-app`.
2. Ejecutar:
   - `run-dev.bat`
3. Esperar apertura de 2 ventanas nuevas (backend y frontend).
4. Verificar:
   - Backend: `http://localhost:8000/`
   - Frontend: `http://localhost:5173/`
   - DB: `localhost:5432`

### Criterio de exito
- Migraciones corren sin error.
- Backend responde HTTP 200 en `/`.
- Frontend carga en navegador.

## B) Verificacion con run-prod.bat (modo compose completo)

### Que hace
1. Valida Docker disponible.
2. Levanta `db + backend + frontend` con `docker compose up -d --build`.
3. Muestra estado de contenedores (`docker compose ps`).
4. Ejecuta diagnostico (`diagnose.ps1`) con chequeo de puertos, HTTP y DB.

### Pasos
1. Abrir CMD en `habilitaciones-app`.
2. Ejecutar:
   - `run-prod.bat`
3. Esperar finalizacion de build/arranque.
4. Verificar:
   - Backend: `http://localhost:8000/`
   - Frontend: `http://localhost:8080/`
   - DB: `localhost:5432`
5. Confirmar que `diagnose.ps1` no reporte fallas.

### Criterio de exito
- Contenedores `sgh-db`, `sgh-backend`, `sgh-frontend` en estado `Up`.
- Healthchecks sin error.
- Backend y frontend responden HTTP 200.

## Diferencias clave entre run-dev y run-prod
- Alcance:
  - `run-dev`: DB en Docker + backend/frontend locales.
  - `run-prod`: todo en Docker.
- Velocidad de iteracion:
  - `run-dev`: mas rapido para desarrollar.
  - `run-prod`: mas lento por build, mas representativo de despliegue.
- Puertos frontend:
  - `run-dev`: `5173` (Vite).
  - `run-prod`: `8080` (Nginx).
- Diagnostico:
  - `run-dev`: foco en flujo de desarrollo y migraciones.
  - `run-prod`: foco en consistencia del stack containerizado.

## Comandos de apoyo
- Ver estado compose:
  - `docker compose -f docker\docker-compose.yml ps`
- Ver logs:
  - `docker compose -f docker\docker-compose.yml logs -f`
- Detener stack prod:
  - `docker compose -f docker\docker-compose.yml down`

## Verificacion de tests backend (Etapa 2.3)
1. Abrir CMD en `C:\Users\Admin\GitHub\SGH-V1\habilitaciones-app\backend`.
2. Ejecutar:
   - `run-tests.bat`
3. Resultado esperado:
   - Suite estable (smoke tests API en verde).
   - Tests legacy marcados como `skipped` hasta su reescritura contractual.
