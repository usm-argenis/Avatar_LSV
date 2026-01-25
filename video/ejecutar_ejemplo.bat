@echo off
REM Script para ejecutar el ejemplo de segmentación de video
REM Usa el entorno virtual automáticamente

echo ================================================
echo   SEGMENTADOR DE VIDEOS - Lengua de Senas
echo ================================================
echo.

REM Activar el entorno virtual
call C:\Users\andre\OneDrive\Documentos\tesis\.venv\Scripts\activate.bat

REM Ejecutar el script
python ejemplo.py

echo.
echo Presiona cualquier tecla para salir...
pause > nul
