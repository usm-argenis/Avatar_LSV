Write-Host ""
Write-Host "========================================"
Write-Host "  VERIFICACION DE CONFIGURACION IP"
Write-Host "========================================"
Write-Host ""

Write-Host "IP DEL SISTEMA:" -ForegroundColor Yellow
Get-NetIPAddress | Where-Object {$_.AddressFamily -eq 'IPv4' -and $_.IPAddress -notmatch '^127\.|^169\.254\.'} | Format-Table IPAddress, InterfaceAlias -AutoSize

Write-Host "SERVICIOS ACTIVOS:" -ForegroundColor Yellow
netstat -ano | findstr "LISTENING" | findstr "3000 5000 8000"

Write-Host ""
Write-Host "VERIFICANDO ARCHIVOS CRITICOS:" -ForegroundColor Yellow

$newIP = "10.171.95.159"
$oldIP = "192.168.10.93"
$archivos = @(
    "mobile_app\lengua-de-senas\config\serverConfig.js",
    "mobile_app\lengua-de-senas\services\authService.js",
    "test\animation_mobile.html"
)

foreach ($arch in $archivos) {
    $path = Join-Path $PWD $arch
    if (Test-Path $path) {
        $contenido = Get-Content $path -Raw
        if ($contenido -match $oldIP) {
            Write-Host "  X $arch - TIENE IP ANTIGUA" -ForegroundColor Red
        } elseif ($contenido -match $newIP) {
            Write-Host "  OK $arch" -ForegroundColor Green
        }
    }
}

Write-Host ""
Write-Host "Configuracion lista para IP: $newIP"
Write-Host ""
