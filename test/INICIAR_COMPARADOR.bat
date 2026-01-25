@echo off
REM ========================================
REM  COMPARADOR: Original vs Mejorado
REM ========================================

echo.
echo ============================================
echo  COMPARADOR DE ANIMACIONES LSV
echo ============================================
echo.
echo Archivos creados:
echo   - Nancy_resultado_yo_MEJORADO.glb
echo   - yo_analisis_refinamiento.json
echo   - comparador.html
echo.
echo ============================================
echo  INICIANDO SERVIDOR
echo ============================================
echo.

cd /d "c:\Users\andre\OneDrive\Documentos\tesis\test"

echo Abriendo comparador en navegador...
start http://localhost:8000/comparador.html

echo.
echo ============================================
echo  INSTRUCCIONES:
echo ============================================
echo.
echo 1. En el navegador, verás dos paneles lado a lado:
echo    - Izquierda: ORIGINAL
echo    - Derecha: MEJORADO
echo.
echo 2. Selecciona "YO" en el dropdown
echo.
echo 3. Presiona "Animar Ambas"
echo.
echo 4. IMPORTANTE: Por ahora ambas versiones son IGUALES
echo    porque el archivo MEJORADO es una copia.
echo.
echo 5. Para aplicar las correcciones REALES:
echo    a) Abrir Blender
echo    b) Cargar Nancy_resultado_yo_MEJORADO.glb
echo    c) Aplicar las correcciones de dedos:
echo       - Indice: -15 grados (mas extendido)
echo       - Medio: +10 grados (mas cerrado)
echo       - Anular: +10 grados (mas cerrado)
echo       - Meñique: +10 grados (mas cerrado)
echo       - Pulgar: +5 grados (ajuste ligero)
echo    d) Exportar como Nancy_resultado_yo_MEJORADO.glb
echo    e) Recargar esta pagina para ver la diferencia
echo.
echo ============================================
echo  Presiona Ctrl+C para detener el servidor
echo ============================================
echo.

python -m http.server 8000
