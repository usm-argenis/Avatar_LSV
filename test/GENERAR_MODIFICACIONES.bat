@echo off
cd /d "%~dp0"

echo ========================================
echo GENERANDO ARCHIVOS MODIFICADOS
echo ========================================
echo.

echo [1/2] Procesando Duvall...
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python aplicar_modificaciones_blender.py -- datos_duvall.json
if errorlevel 1 (
    echo ERROR: Fallo al procesar Duvall
    pause
    exit /b 1
)

echo.
echo [2/2] Procesando Carla...
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python aplicar_modificaciones_blender.py -- datos_carla.json
if errorlevel 1 (
    echo ERROR: Fallo al procesar Carla
    pause
    exit /b 1
)

echo.
echo ========================================
echo PROCESO COMPLETADO
echo ========================================
echo.
echo Archivos generados:
echo - output\glb\Duvall\alfabeto\Duvall_resultado_b_modif.glb
echo - output\glb\Carla\alfabeto\Carla_resultado_b_modif.glb
echo.
pause
