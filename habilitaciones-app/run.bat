@echo off
echo ============================================
echo     Iniciando SGH-V1 - Entorno Local
echo ============================================

echo.
echo [1/4] Iniciando base de datos PostgreSQL...
docker compose up -d db

echo.
echo [2/4] Ejecutando migraciones Alembic...
cd backend
alembic upgrade head
cd ..

echo.
echo [3/4] Iniciando backend FastAPI...
start cmd /k "cd backend && uvicorn app.main:app --reload --port 8000"

echo.
echo [4/4] Iniciando servidor frontend...
start cmd /k "cd frontend && python -m http.server 8080"

echo.
echo ============================================
echo SGH-V1 iniciado correctamente
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:8080
echo ============================================
pause
