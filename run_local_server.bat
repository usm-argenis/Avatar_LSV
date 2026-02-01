@echo off
REM Script para iniciar el servidor local LSV
REM Para Windows

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════╗
echo ║   🌐 Servidor LSV - GitHub Pages Local   ║
echo ║           (Windows Batch Script)          ║
echo ╚════════════════════════════════════════════╝
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no está instalado
    echo.
    echo Instálalo desde: https://www.python.org/
    echo Asegúrate de marcar "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

REM Obtener la ruta del script
cd /d "%~dp0"

echo ✅ Python detectado
echo 📁 Directorio: %cd%
echo 🔗 URL: http://localhost:8000/
echo.
echo ⏳ Iniciando servidor...
echo.

REM Ejecutar servidor Python
python run_local_server.py

REM Mostrar mensaje si el usuario cierra la ventana
echo.
echo 🛑 Servidor detenido
echo ✅ ¡Hasta luego!
pause
