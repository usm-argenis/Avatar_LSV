@echo off
cd /d "%~dp0"

echo ========================================
echo PROCESAMIENTO BATCH DE CARPETAS
echo ========================================
echo.

echo [1/2] Procesando carpeta Duvall...
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python aplicar_modificaciones_batch.py -- datos_duvall_batch.json

if errorlevel 1 (
    echo ERROR: Fallo al procesar Duvall
    pause
    exit /b 1
)

echo.
echo [2/2] Procesando carpeta Carla...
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python aplicar_modificaciones_batch.py -- datos_carla_batch.json

if errorlevel 1 (
    echo ERROR: Fallo al procesar Carla
    pause
    exit /b 1
)

echo.
echo ========================================
echo PROCESO COMPLETADO EXITOSAMENTE
echo ========================================
echo.
echo Archivos generados:
echo - output\glb\Duvall\alfabeto_modificado\
echo - output\glb\Carla\alfabeto_modificado\
echo.
pause
