@echo off
chcp 65001 > nul
cls
echo ========================================
echo    PRUEBA DEL SISTEMA DE ANIMACIONES
echo ========================================
echo.
echo Selecciona una opcion:
echo.
echo 1. Prueba automatica (hola, gracias)
echo 2. Modo interactivo (escribe tu texto)
echo 3. Ver archivos generados
echo 4. Salir
echo.
set /p opcion="Opcion (1-4): "

if "%opcion%"=="1" goto prueba
if "%opcion%"=="2" goto interactivo
if "%opcion%"=="3" goto archivos
if "%opcion%"=="4" goto fin

:prueba
cls
echo Ejecutando prueba automatica...
echo.
python main.py
goto menu

:interactivo
cls
echo Modo interactivo activado
echo Escribe tu texto y presiona Enter
echo.
python main.py --mode interactive
goto menu

:archivos
cls
echo Archivos JSON generados:
echo.
dir /b *.json
echo.
pause
goto menu

:menu
echo.
echo ========================================
pause
goto inicio

:inicio
cls
goto :eof

:fin
echo Adios!
