@echo off
cd /d "%~dp0"

echo ========================================
echo GENERANDO MODIFICACIONES - DUVALL Y CARLA
echo ========================================
echo.

echo [1/2] Procesando DUVALL...
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python aplicar_modificaciones_blender.py -- datos_duvall.json
if errorlevel 1 (
    echo ERROR: Fallo al procesar Duvall
    pause
    exit /b 1
)

echo.
echo [2/2] Procesando CARLA...
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python aplicar_modificaciones_blender.py -- datos_carla.json
if errorlevel 1 (
    echo ERROR: Fallo al procesar Carla
    pause
    exit /b 1
)

echo.
echo ========================================
echo PROCESO COMPLETADO - AMBOS AVATARES
echo ========================================
echo.
echo Archivos generados para DUVALL y CARLA con sus dimensiones especificas
echo Verificacion de quaternions aplicada en frames correctos
echo.
pause
