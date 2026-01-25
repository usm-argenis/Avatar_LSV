@echo off
REM ====================================================================
REM RETARGET: Duvall -> Argenis (Sin congelamiento)
REM Uso: RETARGET_DUVALL_ARGENIS.bat [categoria]
REM Ejemplo: RETARGET_DUVALL_ARGENIS.bat alfabeto
REM ====================================================================

if "%1"=="" (
    echo ❌ ERROR: Debes especificar una categoria
    echo Uso: RETARGET_DUVALL_ARGENIS.bat [categoria]
    echo Ejemplo: RETARGET_DUVALL_ARGENIS.bat alfabeto
    exit /b 1
)

set CATEGORIA=%1

echo ====================================================================
echo 🚀 RETARGET: Duvall → Argenis
echo 📁 Categoría: %CATEGORIA%
echo ====================================================================

REM Ruta a Blender (ajusta si es necesario)
set BLENDER="C:\Program Files\Blender Foundation\Blender 4.5\blender.exe"

REM Ejecutar script de Python en Blender
%BLENDER% --background --python scripts\retarget_duvall_argenis.py -- %CATEGORIA%

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ RETARGET COMPLETADO EXITOSAMENTE
    echo 📂 Archivos generados en: test\output\glb\Argenis\%CATEGORIA%
) else (
    echo.
    echo ❌ ERROR EN EL PROCESO
    exit /b 1
)

pause
