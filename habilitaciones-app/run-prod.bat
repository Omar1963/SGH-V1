@echo off
title SGH-V1 - Produccion
color 0C
setlocal
pushd "%~dp0"

echo ============================================
echo      SGH-V1 - ENTORNO DE PRODUCCION
echo ============================================

echo.
echo [1/4] Verificando Docker...
docker info >nul 2>nul
if errorlevel 1 (
  echo ERROR: Docker no esta disponible para este usuario/sesion.
  echo        Inicia Docker Desktop y verifica permisos ^(grupo docker-users^).
  popd
  pause
  exit /b 1
)

if not exist "docker\docker-compose.yml" (
  echo ERROR: No se encontro docker\docker-compose.yml
  popd
  pause
  exit /b 1
)

echo.
echo [2/4] Iniciando servicios con Docker Compose...
docker compose -f docker\docker-compose.yml up -d --build
if errorlevel 1 (
  echo ERROR: Fallo el arranque de servicios.
  popd
  pause
  exit /b 1
)

echo.
echo [3/4] Estado de contenedores...
docker compose -f docker\docker-compose.yml ps

echo.
echo [4/4] Diagnostico rapido...
powershell -ExecutionPolicy Bypass -File diagnose.ps1

echo.
echo ============================================
echo SGH-V1 (PROD) iniciado correctamente
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:8080
echo DB:       localhost:5432
echo ============================================
popd
pause

