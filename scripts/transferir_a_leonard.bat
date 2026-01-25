@echo off
echo ========================================
echo  TRANSFERIR ANIMACION A LEONARD
echo ========================================
echo.
echo Avatar: Leonard.fbx
echo Animacion: Remy_resultado_b.fbx
echo Salida: output/Leonard_con_animacion_b.fbx
echo.
echo ========================================
echo.

REM Buscar Blender en ubicaciones comunes
set BLENDER_PATH=

if exist "C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" (
    set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.5\blender.exe
) else if exist "C:\Program Files\Blender Foundation\Blender 4.4\blender.exe" (
    set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.4\blender.exe
) else if exist "C:\Program Files\Blender Foundation\Blender 4.3\blender.exe" (
    set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.3\blender.exe
) else if exist "C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" (
    set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.2\blender.exe
) else if exist "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe" (
    set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.1\blender.exe
) else if exist "C:\Program Files\Blender Foundation\Blender 4.0\blender.exe" (
    set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.0\blender.exe
) else if exist "C:\Program Files\Blender Foundation\Blender 3.6\blender.exe" (
    set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 3.6\blender.exe
) else if exist "C:\Program Files\Blender Foundation\Blender 3.3\blender.exe" (
    set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 3.3\blender.exe
) else (
    echo ERROR: No se encontro Blender instalado
    echo.
    echo Por favor instala Blender desde: https://www.blender.org/download/
    echo O edita este script y establece la ruta manualmente en BLENDER_PATH
    echo.
    pause
    exit /b 1
)

echo Usando Blender: %BLENDER_PATH%
echo.

REM Ejecutar script
"%BLENDER_PATH%" --background --python "%~dp0transferir_con_keyframes_directos.py"

echo.
echo ========================================
if %ERRORLEVEL% EQU 0 (
    echo  COMPLETADO!
    echo ========================================
    echo.
    echo El archivo se guardo en: output\Leonard_con_animacion_b.fbx
) else (
    echo  ERROR
    echo ========================================
    echo.
    echo Ocurrio un error durante la transferencia
)
echo.
pause
