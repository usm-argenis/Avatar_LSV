@echo off
echo ========================================
echo   SISTEMA DE GESTOS FACIALES - LSV
echo ========================================
echo.
echo Iniciando servidor web...
echo.
echo URLs disponibles:
echo.
echo [1] Test Gestos Faciales (Luis):
echo     http://localhost:8080/test/test_facial_expressions.html
echo.
echo [2] Animation con Gestos (Luis):
echo     http://localhost:8080/test/animation.html?avatar=Luis^&texto=hola mal gracias
echo.
echo [3] Animation con Gestos (Nancy):
echo     http://localhost:8080/test/animation.html?avatar=Nancy^&texto=buenos dias como estas
echo.
echo [4] Test expresion "molesto" (Luis):
echo     http://localhost:8080/test/animation.html?avatar=Luis^&texto=mal no error
echo.
echo Presiona Ctrl+C para detener el servidor
echo ========================================
echo.
python -m http.server 8080
