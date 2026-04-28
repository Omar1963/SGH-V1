@echo off
title SGH-V1 - Produccion
color 0C

echo ============================================
echo      SGH-V1 - ENTORNO DE PRODUCCION
echo ============================================

echo.
echo Iniciando servicios con Docker Compose...
docker compose -f docker/docker-compose.yml up -d --build

echo.
echo ============================================
echo SGH-V1 (PROD) iniciado correctamente
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:8080
echo ============================================
pause

