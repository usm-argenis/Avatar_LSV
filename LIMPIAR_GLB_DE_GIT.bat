@echo off
echo ========================================
echo LIMPIAR ARCHIVOS GLB DEL REPOSITORIO
echo ========================================
echo.
echo ADVERTENCIA: Esto eliminara archivos GLB del historial de git
echo pero NO los borrara de tu disco.
echo.
echo Los archivos seguiran en tu carpeta local.
echo.
pause

cd /d C:\Users\andre\OneDrive\Documentos\tesis

echo.
echo Paso 1: Removiendo archivos GLB del index de git...
git rm -r --cached test/output/glb

echo.
echo Paso 2: Verificando .gitignore...
findstr /C:"*.glb" .gitignore
if errorlevel 1 (
    echo ERROR: .gitignore no tiene *.glb
    pause
    exit /b 1
)

echo.
echo Paso 3: Creando commit...
git add .gitignore
git commit -m "chore: Remover archivos GLB del repositorio (mantener solo localmente)"

echo.
echo Paso 4: Subiendo cambios...
git push origin main

echo.
echo ========================================
echo COMPLETADO
echo ========================================
echo.
echo Los archivos GLB han sido removidos del repositorio.
echo GitHub Pages ahora deberia construir mucho mas rapido.
echo.
echo Los archivos GLB siguen en tu carpeta local:
echo   test/output/glb/
echo.
pause
