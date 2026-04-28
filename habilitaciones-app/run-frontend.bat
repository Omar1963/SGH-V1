@echo off
title SGH-V1 - Frontend (Vite)
color 0B

echo ============================================
echo        SGH-V1 - FRONTEND (VITE)
echo ============================================

echo.
echo [1/4] Navegando a la carpeta del frontend...
cd /d "%~dp0frontend"

echo.
echo [2/4] Verificando Node.js...
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js no esta instalado.
    echo Descargalo desde: https://nodejs.org/
    pause
    exit /b
)

echo.
echo [3/4] Instalando dependencias (npm install)...
npm install

echo.
echo [4/4] Iniciando Vite en modo desarrollo...
start http://localhost:5173
npm run dev

echo.
echo ============================================
echo Frontend iniciado correctamente con Vite
echo URL: http://localhost:5173
echo ============================================
pause
