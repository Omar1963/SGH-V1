@echo off
title SGH-V1 - Desarrollo
color 0A
setlocal

rem Ensure relative paths work even if launched from another directory.
pushd "%~dp0"

echo ============================================
echo      SGH-V1 - ENTORNO DE DESARROLLO
echo ============================================

echo.
echo [1/7] Validando entorno backend...
if not exist "backend\.venv\Scripts\python.exe" (
  echo ERROR: No se encontro Python del entorno virtual en backend\.venv
  echo Ejecuta primero: py -m venv backend\.venv  ^(y luego instala dependencias^)
  popd
  pause
  exit /b 1
)

echo.
echo [2/7] Verificando Docker...
docker info >nul 2>nul
if errorlevel 1 (
  echo ERROR: Docker no esta disponible para este usuario/sesion.
  echo        Inicia Docker Desktop y verifica permisos ^(grupo docker-users^).
  popd
  pause
  exit /b 1
)

echo.
echo [3/7] Iniciando Base de Datos (Docker)...
docker compose -f docker\docker-compose.yml up -d db
if errorlevel 1 (
  echo ERROR: No se pudo iniciar el contenedor de DB.
  popd
  pause
  exit /b 1
)

echo.
echo [4/7] Esperando disponibilidad de DB...
set /a _attempt=0
:wait_db
set /a _attempt+=1
docker exec sgh-db pg_isready -U sgh_user -d sgh_db >nul 2>nul
if not errorlevel 1 goto db_ready
if %_attempt% GEQ 30 (
  echo ERROR: DB no quedo disponible a tiempo.
  popd
  pause
  exit /b 1
)
timeout /t 2 /nobreak >nul
goto wait_db

:db_ready
echo DB lista.

echo.
echo [5/7] Ejecutando migraciones Alembic...
pushd backend
.\.venv\Scripts\python.exe -m alembic upgrade head
if errorlevel 1 (
  echo ERROR: Fallaron las migraciones Alembic.
  popd
  popd
  pause
  exit /b 1
)
popd

echo.
echo [6/7] Iniciando Backend FastAPI...
start "SGH-BACKEND-DEV" cmd /k "cd backend && .venv\\Scripts\\python.exe -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

echo.
echo [7/7] Iniciando Frontend Vite en puerto 5173...
start "SGH-FRONTEND-DEV" cmd /k "cd frontend && npm run dev -- --host 0.0.0.0 --port 5173"

echo.
echo ============================================
echo SGH-V1 (DEV) iniciado correctamente
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:5173
echo DB:       localhost:5432
echo ============================================
popd
pause
