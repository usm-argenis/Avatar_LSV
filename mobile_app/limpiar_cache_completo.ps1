# LIMPIEZA COMPLETA DE CACHE - React Native
# Ejecutar si los cambios aún no se ven

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "LIMPIEZA COMPLETA DE CACHE" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Navegar a la carpeta
cd mobile_app\lengua-de-senas

Write-Host "🧹 [1/5] Limpiando cache de npm..." -ForegroundColor Yellow
npm cache clean --force

Write-Host ""
Write-Host "🧹 [2/5] Eliminando node_modules..." -ForegroundColor Yellow
Remove-Item -Recurse -Force node_modules -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "🧹 [3/5] Eliminando cache de Metro..." -ForegroundColor Yellow
Remove-Item -Recurse -Force $env:LOCALAPPDATA\Temp\metro-* -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force $env:LOCALAPPDATA\Temp\haste-* -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "📦 [4/5] Reinstalando dependencias..." -ForegroundColor Yellow
npm install

Write-Host ""
Write-Host "🚀 [5/5] Iniciando con cache limpio..." -ForegroundColor Yellow
Write-Host ""
Write-Host "✅ Ahora ejecuta: npm start" -ForegroundColor Green
Write-Host ""
Write-Host "Los nuevos avatares deberían aparecer ahora!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
