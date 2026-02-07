# Script de configuración inicial
# Refresca PATH y autentica con GitHub

Write-Host "🔄 Refrescando PATH..." -ForegroundColor Cyan
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

Write-Host "✅ PATH actualizado" -ForegroundColor Green
Write-Host ""

Write-Host "📋 Verificando GitHub CLI..." -ForegroundColor Cyan
gh --version

Write-Host ""
Write-Host "🔐 Iniciando autenticación con GitHub..." -ForegroundColor Cyan
Write-Host "Sigue las instrucciones en pantalla" -ForegroundColor Yellow
Write-Host ""

gh auth login
