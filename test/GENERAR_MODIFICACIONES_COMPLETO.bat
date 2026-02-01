@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║       🚀 PROCESAMIENTO PARALELO - DUVALL Y CARLA              ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

set BLENDER="C:\Program Files\Blender Foundation\Blender 4.5\blender.exe"
set PYTHON_SCRIPT=aplicar_modificaciones_maestro.py

echo 📋 Sistema maestro con 2 JSON:
echo    • Duvall.json
echo    • Carla.json
echo.

REM Verificar archivos
if not exist "Duvall.json" (
    echo ❌ Error: No se encuentra Duvall.json
    pause
    exit /b 1
)

if not exist "Carla.json" (
    echo ❌ Error: No se encuentra Carla.json
    pause
    exit /b 1
)

if not exist "%PYTHON_SCRIPT%" (
    echo ❌ Error: No se encuentra %PYTHON_SCRIPT%
    pause
    exit /b 1
)

echo ⚡ INICIANDO PROCESAMIENTO PARALELO...
echo.

REM PROCESAMIENTO PARALELO - Ambos personajes a la vez
start /B "Duvall" %BLENDER% --background --python %PYTHON_SCRIPT% -- Duvall.json > log_duvall.txt 2>&1
start /B "Carla" %BLENDER% --background --python %PYTHON_SCRIPT% -- Carla.json > log_carla.txt 2>&1

echo 🔄 Duvall y Carla procesándose simultáneamente...
echo 📊 Logs: log_duvall.txt y log_carla.txt
echo.

REM Esperar a que ambos procesos terminen
:WAIT_LOOP
timeout /t 5 /nobreak > nul
tasklist /FI "IMAGENAME eq blender.exe" 2>NUL | find /I /N "blender.exe">NUL
if "%ERRORLEVEL%"=="0" goto WAIT_LOOP

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                    ✅ PROCESO COMPLETADO                       ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo 📁 Archivos en: output\glb\{Duvall^|Carla}\Modif\
echo 📝 Logs: log_duvall.txt ^| log_carla.txt
echo.
pause
