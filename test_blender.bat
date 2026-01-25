@echo off
echo Probando Blender...
echo.

blender --version

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ ERROR: Blender no está instalado o no está en el PATH
    echo.
    echo Para solucionar:
    echo 1. Instala Blender desde https://www.blender.org/download/
    echo 2. O agrega Blender al PATH del sistema
    echo.
) else (
    echo.
    echo ✅ Blender está funcionando correctamente
    echo.
)

pause
