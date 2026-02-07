@echo off
REM ====================================================================
REM VERIFICAR Y HABILITAR GITHUB PAGES
REM ====================================================================

echo.
echo ======================================================================
echo   VERIFICACION GITHUB PAGES - Avatar LSV
echo ======================================================================
echo.

echo [1/5] Verificando repositorio...
git remote -v | findstr "origin"
echo.

echo [2/5] Verificando archivos necesarios...
if exist "index.html" (
    echo   ^✅ index.html encontrado
) else (
    echo   ^❌ index.html NO encontrado
)

if exist ".nojekyll" (
    echo   ^✅ .nojekyll encontrado
) else (
    echo   ^❌ .nojekyll NO encontrado
)

if exist "README.md" (
    echo   ^✅ README.md encontrado
) else (
    echo   ^⚠️  README.md NO encontrado
)
echo.

echo [3/5] Verificando estado de Git...
git status --short
echo.

echo [4/5] Ultimos commits...
git log --oneline -3
echo.

echo ======================================================================
echo   INSTRUCCIONES PARA HABILITAR GITHUB PAGES
echo ======================================================================
echo.
echo 1. Abre tu navegador en:
echo    https://github.com/usm-argenis/Avatar_LSV/settings/pages
echo.
echo 2. En "Source" selecciona:
echo    - Branch: main
echo    - Folder: / (root)
echo.
echo 3. Presiona "Save"
echo.
echo 4. Espera 2-3 minutos y tu sitio estara disponible en:
echo    https://usm-argenis.github.io/Avatar_LSV/
echo.
echo ======================================================================
echo.

echo [5/5] ^¿Deseas abrir la configuracion de GitHub Pages ahora? (S/N)
set /p RESPUESTA="> "

if /i "%RESPUESTA%"=="S" (
    start https://github.com/usm-argenis/Avatar_LSV/settings/pages
    echo.
    echo   ^✅ Abriendo configuracion en el navegador...
    timeout /t 3 >nul
    echo.
    echo   Despues de habilitar, espera 2-3 minutos y abre:
    start https://usm-argenis.github.io/Avatar_LSV/
)

echo.
pause
