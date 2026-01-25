@echo off
echo ========================================
echo REINICIAR APP REACT NATIVE
echo ========================================
echo.
echo Este script reiniciara la app con cache limpio
echo para que veas los nuevos avatares.
echo.
echo Pasos:
echo 1. Detener servidor actual (Ctrl+C si esta corriendo)
echo 2. Limpiar cache de Metro bundler
echo 3. Reiniciar la app
echo.
pause

cd mobile_app\lengua-de-senas

echo.
echo [1/3] Limpiando cache de Metro...
call npm start -- --clear

pause
