@echo off
REM ====================================================================
REM Script para mejorar animaciones de DeepMotion
REM Soluciona: dedos ocultos en pecho, brazos muy pegados
REM ====================================================================

setlocal enabledelayedexpansion

echo.
echo ======================================================================
echo   MEJORADOR DE ANIMACIONES DEEPMOTION
echo ======================================================================
echo.

REM Buscar instalación de Blender
set "BLENDER_PATH="

REM Rutas comunes de instalación
if exist "C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" (
    set "BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.5\blender.exe"
)
if exist "C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" (
    set "BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.2\blender.exe"
)
if exist "C:\Program Files\Blender Foundation\Blender 4.0\blender.exe" (
    set "BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.0\blender.exe"
)
if exist "C:\Program Files\Blender Foundation\Blender 3.6\blender.exe" (
    set "BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 3.6\blender.exe"
)

if "%BLENDER_PATH%"=="" (
    echo ERROR: No se encontro Blender instalado
    echo.
    echo Por favor instala Blender 4.0+ desde:
    echo https://www.blender.org/download/
    pause
    exit /b 1
)

echo Blender encontrado: %BLENDER_PATH%
echo.

REM Menú de opciones
echo Selecciona una opcion:
echo.
echo   1. Mejorar UN archivo especifico
echo   2. Mejorar TODOS los archivos en test/output/glb
echo   3. Mejorar TODOS los archivos en un directorio personalizado
echo   4. Configuracion avanzada
echo.
set /p OPCION="Ingresa el numero de opcion (1-4): "

if "%OPCION%"=="1" goto :opcion_archivo
if "%OPCION%"=="2" goto :opcion_directorio_default
if "%OPCION%"=="3" goto :opcion_directorio_custom
if "%OPCION%"=="4" goto :opcion_avanzada

echo Opcion invalida
pause
exit /b 1

:opcion_archivo
echo.
echo ======================================================================
echo   MEJORAR ARCHIVO INDIVIDUAL
echo ======================================================================
echo.
set /p INPUT_FILE="Ingresa la ruta del archivo GLB/FBX: "

if not exist "%INPUT_FILE%" (
    echo.
    echo ERROR: El archivo no existe: %INPUT_FILE%
    pause
    exit /b 1
)

echo.
echo Procesando: %INPUT_FILE%
echo.

"%BLENDER_PATH%" --background --python scripts\mejorar_animaciones_deepmotion.py -- --input "%INPUT_FILE%"

goto :fin

:opcion_directorio_default
echo.
echo ======================================================================
echo   MEJORAR TODOS LOS ARCHIVOS EN test/output/glb
echo ======================================================================
echo.

if not exist "test\output\glb" (
    echo ERROR: No existe el directorio test\output\glb
    pause
    exit /b 1
)

echo Procesando todos los archivos en: test\output\glb
echo Los archivos mejorados se guardaran en: test\output\glb\mejorados
echo.
pause

"%BLENDER_PATH%" --background --python scripts\mejorar_animaciones_deepmotion.py -- --directorio "test\output\glb"

goto :fin

:opcion_directorio_custom
echo.
echo ======================================================================
echo   MEJORAR TODOS LOS ARCHIVOS EN DIRECTORIO PERSONALIZADO
echo ======================================================================
echo.
set /p INPUT_DIR="Ingresa la ruta del directorio: "

if not exist "%INPUT_DIR%" (
    echo.
    echo ERROR: El directorio no existe: %INPUT_DIR%
    pause
    exit /b 1
)

echo.
echo Procesando todos los archivos en: %INPUT_DIR%
echo.

"%BLENDER_PATH%" --background --python scripts\mejorar_animaciones_deepmotion.py -- --directorio "%INPUT_DIR%"

goto :fin

:opcion_avanzada
echo.
echo ======================================================================
echo   CONFIGURACION AVANZADA
echo ======================================================================
echo.
set /p INPUT_FILE="Archivo de entrada: "

if not exist "%INPUT_FILE%" (
    echo ERROR: El archivo no existe
    pause
    exit /b 1
)

echo.
echo Ajustes de mejora:
echo   - Separacion: Cuanto se separan los brazos del cuerpo (0-30 grados)
echo   - Elevacion: Cuanto se elevan los brazos hacia adelante (0-20 grados)
echo.
echo Valores por defecto: Separacion=15, Elevacion=10
echo.

set /p SEPARACION="Separacion (Enter para default 15): "
set /p ELEVACION="Elevacion (Enter para default 10): "

if "%SEPARACION%"=="" set SEPARACION=15
if "%ELEVACION%"=="" set ELEVACION=10

echo.
echo Procesando con: Separacion=%SEPARACION% Elevacion=%ELEVACION%
echo.

"%BLENDER_PATH%" --background --python scripts\mejorar_animaciones_deepmotion.py -- --input "%INPUT_FILE%" --separacion %SEPARACION% --elevacion %ELEVACION%

goto :fin

:fin
echo.
echo ======================================================================
echo   PROCESO COMPLETADO
echo ======================================================================
echo.
echo Revisa los archivos generados con el sufijo _mejorado
echo.
pause
