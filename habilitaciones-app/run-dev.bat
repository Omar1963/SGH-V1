@echo off
title SGH-V1 - Desarrollo
color 0A

rem Ensure relative paths work even if launched from another directory.
pushd "%~dp0"

echo ============================================
echo      SGH-V1 - ENTORNO DE DESARROLLO
echo ============================================

echo.
echo [1/5] Activando entorno virtual...
if not exist "backend\.venv\Scripts\activate.bat" (
  echo ERROR: No se encontro el entorno virtual en backend\.venv
  echo Ejecuta primero: py -m venv backend\.venv  ^(y luego instala dependencias^)
  popd
  pause
  exit /b 1
)
call "backend\.venv\Scripts\activate.bat"

echo.
echo [2/5] Iniciando Base de Datos (Docker)...
docker info >nul 2>nul
if errorlevel 1 (
  echo WARNING: Docker no esta disponible para este usuario/sesion.
  echo          Inicia Docker Desktop y/o verifica permisos ^(grupo docker-users^).
  echo          Continuando sin levantar la DB...
) else (
  docker compose -f docker\docker-compose.yml up -d db
)

echo.
echo [3/5] Ejecutando migraciones Alembic...
cd backend
python -m alembic upgrade head
cd ..

echo.
echo [4/5] Iniciando Backend FastAPI...
start cmd /k "cd backend && call .venv\\Scripts\\activate.bat && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

echo.
echo [5/5] Iniciando Frontend en puerto 8081...
start cmd /k "cd frontend && py -m http.server 8081"

echo.
echo ============================================
echo SGH-V1 (DEV) iniciado correctamente
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:8081
echo ============================================
popd
pause
