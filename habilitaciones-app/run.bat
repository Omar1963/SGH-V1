@echo off
title SGH-V1 - Menu Interactivo
color 0A

:menu
cls
echo ============================================
echo        SGH-V1 - MENU INTERACTIVO
echo ============================================
echo.
echo  1. Iniciar TODO (DB + Backend + Frontend)
echo  2. Iniciar solo Base de Datos (Docker)
echo  3. Iniciar solo Backend (FastAPI)
echo  4. Iniciar solo Frontend (HTTP Server)
echo  5. Detener contenedores Docker
echo  6. Salir
echo.
set /p opcion=Seleccione una opcion: 

if "%opcion%"=="1" goto all
if "%opcion%"=="2" goto db
if "%opcion%"=="3" goto backend
if "%opcion%"=="4" goto frontend
if "%opcion%"=="5" goto stopdocker
if "%opcion%"=="6" exit
goto menu

:activate_venv
echo Activando entorno virtual...
call backend\.venv\Scripts\activate
goto :eof

:db
cls
echo ============================================
echo     Iniciando Base de Datos PostgreSQL...
echo ============================================
docker compose -f docs\docker-compose.yml up -d db
echo.
pause
goto menu

:backend
cls
echo ============================================
echo     Iniciando Backend FastAPI...
echo ============================================
call :activate_venv
start cmd /k "cd backend && py -m uvicorn app.main:app --reload --port 8000"
echo.
pause
goto menu

:frontend
cls
echo ============================================
echo     Iniciando Frontend en puerto 8081...
echo ============================================
start cmd /k "cd frontend && py -m http.server 8081"
echo.
pause
goto menu

:all
cls
echo ============================================
echo     Iniciando TODO SGH-V1
echo ============================================

echo [1/3] Base de datos...
docker compose -f docs\docker-compose.yml up -d db

echo [2/3] Backend...
call :activate_venv
start cmd /k "cd backend && py -m uvicorn app.main:app --reload --port 8000"

echo [3/3] Frontend...
start cmd /k "cd frontend && py -m http.server 8081"

echo.
echo SGH-V1 iniciado correctamente.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:8081
echo.
pause
goto menu

:stopdocker
cls
echo ============================================
echo     Deteniendo contenedores Docker...
echo ============================================
docker compose -f docs\docker-compose.yml down
echo.
pause
goto menu
