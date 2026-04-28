@echo off
title SGH-V1 - Desarrollo
color 0A

echo ============================================
echo      SGH-V1 - ENTORNO DE DESARROLLO
echo ============================================

echo.
echo [1/5] Activando entorno virtual...
call backend\.venv\Scripts\activate

echo.
echo [2/5] Iniciando Base de Datos (Docker)...
docker compose -f docs\docker-compose.yml up -d db

echo.
echo [3/5] Ejecutando migraciones Alembic...
cd backend
py -m alembic upgrade head
cd ..

echo.
echo [4/5] Iniciando Backend FastAPI...
start cmd /k "cd backend && py -m uvicorn app.main:app --reload --port 8000"

echo.
echo [5/5] Iniciando Frontend en puerto 8081...
start cmd /k "cd frontend && py -m http.server 8081"

echo.
echo ============================================
echo SGH-V1 (DEV) iniciado correctamente
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:8081
echo ============================================
pause
