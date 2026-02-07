@echo off
REM ====================================================================
REM RETARGET DEEPMOTION -> DUVALL
REM Convierte animaciones de Deepmotion a avatar Duvall
REM Uso: RETARGET_DEEPMOTION_DUVALL.bat <archivo_glb> [nombre_salida]
REM Ejemplo: RETARGET_DEEPMOTION_DUVALL.bat "verbo_default (1).glb" verbo_hola
REM ====================================================================

if "%~1"=="" (
    echo ❌ ERROR: Debes especificar el archivo GLB de Deepmotion
    echo.
    echo Uso: RETARGET_DEEPMOTION_DUVALL.bat ^<archivo_glb^> [nombre_salida]
    echo.
    echo Ejemplos:
    echo   RETARGET_DEEPMOTION_DUVALL.bat "verbo_default (1).glb" verbo_hola
    echo   RETARGET_DEEPMOTION_DUVALL.bat verbo_default.glb verbo_adios
    echo.
    exit /b 1
)

set ARCHIVO_GLB=%~1
set NOMBRE_SALIDA=%~2

REM Si no se especifica nombre de salida, usar el nombre del archivo sin extensión
if "%NOMBRE_SALIDA%"=="" (
    set NOMBRE_SALIDA=%~n1
)

echo ====================================================================
echo 🚀 RETARGET DEEPMOTION -^> DUVALL
echo 📁 Archivo fuente: %ARCHIVO_GLB%
echo 📝 Nombre salida: %NOMBRE_SALIDA%
echo ====================================================================

REM Ruta a Blender
set BLENDER="C:\Program Files\Blender Foundation\Blender 4.5\blender.exe"

REM Ejecutar script de retargeting
%BLENDER% --background --python scripts\retarget_deepmotion_duvall.py -- "%ARCHIVO_GLB%" "%NOMBRE_SALIDA%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ RETARGETING COMPLETADO EXITOSAMENTE
    echo 📂 Archivo generado: test\output\glb\Duvall\deepmotion\%NOMBRE_SALIDA%.glb
    echo.
) else (
    echo.
    echo ❌ ERROR EN EL RETARGETING
    exit /b 1
)

pause
