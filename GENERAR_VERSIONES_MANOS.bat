@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║  🖐️  GENERAR VERSIONES CON DIFERENTES ESCALAS DE ROTACIÓN     ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

set BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.5\blender.exe
set SCRIPT_PATH=%~dp0aplicar_manos_quaternions_escalable.py
set HAND_JSON=%~dp0output\hand_analysis\miercoles_hands.json
set INPUT_GLB=%~dp0test\output\glb\Duvall\dias_semana\Duvall_resultado_miercoles.glb
set OUTPUT_DIR=%~dp0test\output\glb\Duvall\dias_semana

echo 📋 Generando 3 versiones con diferentes escalas:
echo    • v2_escala_030: Escala 0.3 (suave)
echo    • v2_escala_070: Escala 0.7 (media)
echo    • v2_escala_100: Escala 1.0 (completo)
echo.

REM Versión con escala 0.3
echo ════════════════════════════════════════════════════════════════
echo [1/3] Generando con escala 0.3...
echo ════════════════════════════════════════════════════════════════
"%BLENDER_PATH%" --background --python "%SCRIPT_PATH%" -- "%HAND_JSON%" "%INPUT_GLB%" "%OUTPUT_DIR%\Duvall_resultado_miercoles_MANOS_v2_escala_030.glb" 0.3

REM Versión con escala 0.7
echo.
echo ════════════════════════════════════════════════════════════════
echo [2/3] Generando con escala 0.7...
echo ════════════════════════════════════════════════════════════════
"%BLENDER_PATH%" --background --python "%SCRIPT_PATH%" -- "%HAND_JSON%" "%INPUT_GLB%" "%OUTPUT_DIR%\Duvall_resultado_miercoles_MANOS_v2_escala_070.glb" 0.7

REM Versión con escala 1.0
echo.
echo ════════════════════════════════════════════════════════════════
echo [3/3] Generando con escala 1.0...
echo ════════════════════════════════════════════════════════════════
"%BLENDER_PATH%" --background --python "%SCRIPT_PATH%" -- "%HAND_JSON%" "%INPUT_GLB%" "%OUTPUT_DIR%\Duvall_resultado_miercoles_MANOS_v2_escala_100.glb" 1.0

echo.
echo ════════════════════════════════════════════════════════════════
echo ✅ ¡TODAS LAS VERSIONES GENERADAS!
echo ════════════════════════════════════════════════════════════════
echo.
echo 📂 Archivos creados en: %OUTPUT_DIR%
echo    • Duvall_resultado_miercoles_MANOS_v2_escala_030.glb
echo    • Duvall_resultado_miercoles_MANOS_v2_escala_070.glb
echo    • Duvall_resultado_miercoles_MANOS_v2_escala_100.glb
echo.
echo 💡 Prueba cada versión para ver cuál se ve mejor
echo.

pause
