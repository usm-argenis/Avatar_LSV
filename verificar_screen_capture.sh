#!/bin/bash
# Script de verificación: Pantalla Negra en Expo Go
# Verificar que no hay restricciones de seguridad que bloqueen screen capture

echo "🔍 VERIFICACIÓN DE CONFIGURACIÓN - EXPO GO SCREEN CAPTURE"
echo "=============================================================="
echo ""

# Verificar si hay preventScreenCaptureAsync
echo "✓ Buscando preventScreenCaptureAsync()..."
if grep -r "preventScreenCaptureAsync" mobile_app/lengua-de-senas/screens/ 2>/dev/null; then
    echo "❌ ENCONTRADO: preventScreenCaptureAsync() está activo"
    echo "   Solución: Reemplazar con allowScreenCaptureAsync()"
else
    echo "✅ OK: No hay preventScreenCaptureAsync()"
fi
echo ""

# Verificar si expo-screen-capture está instalada
echo "✓ Buscando expo-screen-capture en package.json..."
if grep -q "expo-screen-capture" mobile_app/lengua-de-senas/package.json; then
    echo "⚠️  ADVERTENCIA: expo-screen-capture está instalada"
    echo "   Si no la usas, considera desinstalarla"
else
    echo "✅ OK: expo-screen-capture no está instalada"
fi
echo ""

# Verificar que los WebViews tengan useWebKit={true}
echo "✓ Verificando propiedades de WebView..."
WEBVIEW_COUNT=$(grep -r "useWebKit={true}" mobile_app/lengua-de-senas/screens/ 2>/dev/null | wc -l)
echo "   Encontrados $WEBVIEW_COUNT WebViews con useWebKit={true}"
if [ $WEBVIEW_COUNT -ge 3 ]; then
    echo "✅ OK: Todos los WebViews principales tienen configuración correcta"
else
    echo "⚠️  ADVERTENCIA: Algunos WebViews podrían no estar configurados"
fi
echo ""

# Verificar app.json
echo "✓ Buscando restricciones en app.json..."
if grep -q "FLAG_SECURE\|secure\|preventScreenCapture" mobile_app/lengua-de-senas/app.json; then
    echo "❌ ENCONTRADO: Restricciones de seguridad en app.json"
else
    echo "✅ OK: No hay restricciones en app.json"
fi
echo ""

# Resumen
echo "=============================================================="
echo "📊 RESUMEN"
echo "=============================================================="
echo ""
echo "Si todos están marcados con ✅, la configuración es correcta."
echo "Si ves ⚠️  o ❌, requiere acción."
echo ""
echo "🚀 PRÓXIMOS PASOS:"
echo "1. Ejecuta: npx expo start --clear"
echo "2. Recarga la app en Expo Go"
echo "3. Intenta compartir pantalla nuevamente"
echo ""
