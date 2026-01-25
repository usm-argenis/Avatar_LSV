@echo off
echo ========================================
echo Fusion: Leonard Animacion + Texturas
echo ========================================
echo.

cd /d "%~dp0.."

"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python scripts\fusion_leonard_animacion_textura.py

echo.
echo ========================================
echo Proceso completado
echo ========================================
echo.
echo Archivos generados en: deploy-viewer-temp\output\
echo   - Leonard_resultado_b_con_texturas.fbx
echo   - Leonard_resultado_b_con_texturas.blend
echo.
pause
