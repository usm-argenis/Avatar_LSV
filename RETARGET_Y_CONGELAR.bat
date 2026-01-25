@echo off
REM ====================================================================
REM RETARGET + CONGELAMIENTO: Duvall -> Luis (Con congelamiento de piernas)
REM Uso: RETARGET_Y_CONGELAR.bat [categoria]
REM Ejemplo: RETARGET_Y_CONGELAR.bat profesion
REM ====================================================================

if "%1"=="" (
    echo ❌ ERROR: Debes especificar una categoria
    echo Uso: RETARGET_Y_CONGELAR.bat [categoria]
    echo Ejemplo: RETARGET_Y_CONGELAR.bat profesion
    exit /b 1
)

set CATEGORIA=%1

echo ====================================================================
echo 🚀 RETARGET + CONGELAMIENTO: Duvall → Luis
echo 📁 Categoría: %CATEGORIA%
echo 🧊 Congelando piernas automáticamente
echo ====================================================================

REM Ruta a Blender (ajusta si es necesario)
set BLENDER="C:\Program Files\Blender Foundation\Blender 4.1\blender.exe"

REM Ejecutar script de Python en Blender
%BLENDER% --background --python scripts\retarget_y_congelar_optimizado.py -- %CATEGORIA%

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ RETARGET Y CONGELAMIENTO COMPLETADO EXITOSAMENTE
    echo 📂 Archivos generados en: test\output\glb\Luis\%CATEGORIA%
) else (
    echo.
    echo ❌ ERROR EN EL PROCESO
    exit /b 1
)

pause
