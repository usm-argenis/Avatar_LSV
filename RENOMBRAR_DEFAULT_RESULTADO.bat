@echo off
REM ====================================================================
REM RENOMBRAR ARCHIVOS *_default.glb a Duvall_resultado_*.glb
REM Uso: RENOMBRAR_DEFAULT_RESULTADO.bat [carpeta]
REM ====================================================================

setlocal enabledelayedexpansion

REM Si no se proporciona carpeta, usar Downloads
if "%~1"=="" (
    set "CARPETA=C:\Users\andre\Downloads"
    echo ⚠️  No se especificó carpeta, usando:
    echo    %CARPETA%
) else (
    set "CARPETA=%~1"
)

echo.
echo ====================================================================
echo   RENOMBRAR ARCHIVOS: *_default.glb ^→ Duvall_resultado_*.glb
echo ====================================================================
echo.
echo 📁 Carpeta: %CARPETA%
echo.

REM Verificar que la carpeta existe
if not exist "%CARPETA%" (
    echo ❌ ERROR: La carpeta no existe
    echo    %CARPETA%
    pause
    exit /b 1
)

REM Ejecutar script Python
python renombrar_default_a_resultado.py "%CARPETA%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ PROCESO COMPLETADO
) else (
    echo.
    echo ❌ ERROR EN EL PROCESO
)

echo.
pause
