@echo off
REM ====================================================================
REM Script para renombrar archivos GLB/FBX
REM Elimina espacios, acentos y caracteres especiales
REM ====================================================================

setlocal enabledelayedexpansion

echo.
echo ======================================================================
echo   RENOMBRADOR DE ARCHIVOS GLB/FBX
echo ======================================================================
echo.

REM Activar entorno virtual si existe
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

echo Este script renombrara archivos eliminando:
echo   - Espacios (convertidos a guiones bajos)
echo   - Acentos (a, e, i, o, u, n)
echo   - Caracteres especiales
echo.
echo Ejemplos:
echo   "Remy_resultado_buenos dias.glb" -^> "remy_resultado_buenos_dias.glb"
echo   "Remy_resultado_nino.glb" -^> "remy_resultado_nino.glb"
echo   "Remy_resultado_adios.glb" -^> "remy_resultado_adios.glb"
echo.
echo ======================================================================
echo.

echo Selecciona una opcion:
echo.
echo   1. PREVIEW - Ver que archivos se renombrarian (sin cambios)
echo   2. RENOMBRAR archivos en test/output/glb
echo   3. RENOMBRAR archivos en directorio personalizado
echo   4. Ver EJEMPLOS de transformaciones
echo.
set /p OPCION="Ingresa el numero de opcion (1-4): "

if "%OPCION%"=="1" goto :preview
if "%OPCION%"=="2" goto :renombrar_default
if "%OPCION%"=="3" goto :renombrar_custom
if "%OPCION%"=="4" goto :ejemplos

echo Opcion invalida
pause
exit /b 1

:preview
echo.
echo ======================================================================
echo   MODO PREVIEW
echo ======================================================================
echo.
python scripts\renombrar_archivos_glb.py --dry-run
goto :fin

:renombrar_default
echo.
echo ======================================================================
echo   RENOMBRAR ARCHIVOS EN test/output/glb
echo ======================================================================
echo.
python scripts\renombrar_archivos_glb.py
goto :fin

:renombrar_custom
echo.
echo ======================================================================
echo   RENOMBRAR ARCHIVOS EN DIRECTORIO PERSONALIZADO
echo ======================================================================
echo.
set /p DIR="Ingresa la ruta del directorio: "

if not exist "%DIR%" (
    echo.
    echo ERROR: El directorio no existe: %DIR%
    pause
    exit /b 1
)

echo.
python scripts\renombrar_archivos_glb.py --directorio "%DIR%"
goto :fin

:ejemplos
echo.
python scripts\renombrar_archivos_glb.py --ejemplos
goto :fin

:fin
echo.
echo ======================================================================
echo   PROCESO COMPLETADO
echo ======================================================================
echo.
pause
