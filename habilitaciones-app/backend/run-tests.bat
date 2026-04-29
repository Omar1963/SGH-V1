@echo off
setlocal
pushd "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo ERROR: No se encontro backend\.venv\Scripts\python.exe
  echo Crea el entorno: py -m venv backend\.venv
  popd
  exit /b 1
)

set PYTHONPATH=%CD%
.\.venv\Scripts\python.exe -m pytest -q tests
set _exit=%ERRORLEVEL%
popd
exit /b %_exit%
