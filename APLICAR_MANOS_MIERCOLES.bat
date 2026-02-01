@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║     🖐️  APLICAR CUATERNIONES DE MANOS A GLB DUVALL            ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Configuración de rutas
set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.5\blender.exe
set SCRIPT_PATH=%~dp0aplicar_manos_quaternions_v2.py
set HAND_JSON=%~dp0output\hand_analysis\miercoles_hands.json
set INPUT_GLB=%~dp0test\output\glb\Duvall\dias_semana\Duvall_resultado_miercoles.glb
set OUTPUT_GLB=%~dp0test\output\glb\Duvall\dias_semana\Duvall_resultado_miercoles_MANOS_v2.glb

echo 📋 Configuración:
echo    • Script: aplicar_manos_quaternions_v2.py (Rotaciones Relativas)
echo    • JSON manos: output\hand_analysis\miercoles_hands.json
echo    • GLB entrada: Duvall_resultado_miercoles.glb
echo    • GLB salida: Duvall_resultado_miercoles_MANOS_v2.glb
echo.

REM Verificar que existen los archivos
if not exist "%BLENDER_PATH%" (
    echo ❌ Error: No se encuentra Blender en: %BLENDER_PATH%
    echo    Por favor, verifica la ruta de instalación de Blender
    pause
    exit /b 1
)

if not exist "%SCRIPT_PATH%" (
    echo ❌ Error: No se encuentra el script: %SCRIPT_PATH%
    pause
    exit /b 1
)

if not exist "%HAND_JSON%" (
    echo ❌ Error: No se encuentra el JSON de manos: %HAND_JSON%
    echo    Por favor, ejecuta primero el análisis de manos con MediaPipe
    pause
    exit /b 1
)

if not exist "%INPUT_GLB%" (
    echo ❌ Error: No se encuentra el GLB de entrada: %INPUT_GLB%
    pause
    exit /b 1
)

echo ✅ Todos los archivos verificados
echo.
echo 🚀 Iniciando procesamiento con Blender...
echo ════════════════════════════════════════════════════════════════
echo.

REM Ejecutar Blender en modo background con el script
"%BLENDER_PATH%" --background --python "%SCRIPT_PATH%" -- "%HAND_JSON%" "%INPUT_GLB%" "%OUTPUT_GLB%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ════════════════════════════════════════════════════════════════
    echo ✅ ¡PROCESO COMPLETADO EXITOSAMENTE!
    echo.
    echo 📂 Archivo generado:
    echo    %OUTPUT_GLB%
    echo.
    
    REM Verificar tamaño del archivo generado
    if exist "%OUTPUT_GLB%" (
        for %%A in ("%OUTPUT_GLB%") do set size=%%~zA
        set /a size_mb=!size! / 1048576
        echo 📊 Tamaño: !size_mb! MB
    )
    echo.
) else (
    echo.
    echo ════════════════════════════════════════════════════════════════
    echo ❌ ERROR: El proceso falló con código: %ERRORLEVEL%
    echo.
    echo 🔍 Revisa los mensajes de error arriba para más detalles
    echo.
)

echo Presiona cualquier tecla para cerrar...
pause >nul
