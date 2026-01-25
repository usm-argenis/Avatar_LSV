@echo off
chcp 65001 > nul
echo ========================================
echo 🎮 GENERADOR DE ANIMACIONES 3D
echo    Modo Interactivo
echo ========================================
echo.
cd /d "%~dp0"
python main.py --mode interactive
pause
