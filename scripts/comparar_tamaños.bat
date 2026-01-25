@echo off
cd /d "%~dp0.."
"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" --background --python scripts\comparar_tamaños.py
pause
