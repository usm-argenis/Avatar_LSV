@echo off
cd /d "%~dp0.."
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python scripts\verificar_tamanos_fbx.py
pause
