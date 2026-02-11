# VERIFICADOR DE SERVIDORES - Sistema Multi-IP
# Este script verifica qué servidores están corriendo

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   VERIFICADOR DE SERVIDORES" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Obtener IPs
Write-Host "📡 TUS IPS ACTUALES:" -ForegroundColor Yellow
$ips = ipconfig | Select-String "IPv4" | ForEach-Object { ($_ -split ':')[1].Trim() }
foreach ($ip in $ips) {
    Write-Host "   • $ip" -ForegroundColor White
}
Write-Host ""

# IPs a probar
$testIPs = @("10.2.0.2", "192.168.10.93", "10.171.95.217", "127.0.0.1")
$ports = @{
    "8000" = "Servidor HTTP (GLB)"
    "3000" = "API Node.js (Auth)"
    "5000" = "Backend Flask (IA)"
}

Write-Host "🔍 VERIFICANDO SERVIDORES..." -ForegroundColor Yellow
Write-Host ""

$serversFound = 0

foreach ($ip in $testIPs) {
    Write-Host "Probando IP: $ip" -ForegroundColor Cyan
    
    foreach ($port in $ports.Keys) {
        $service = $ports[$port]
        
        try {
            $test = Test-NetConnection -ComputerName $ip -Port $port -WarningAction SilentlyContinue -InformationLevel Quiet -ErrorAction Stop
            
            if ($test) {
                Write-Host "   ✅ Puerto $port - $service" -ForegroundColor Green
                $serversFound++
                
                # Mostrar URL
                $url = "http://${ip}:${port}"
                if ($port -eq "8000") {
                    $url += "/avatar_static.html?avatar=Luis"
                }
                Write-Host "      URL: $url" -ForegroundColor Gray
            } else {
                Write-Host "   ❌ Puerto $port - $service (no responde)" -ForegroundColor Red
            }
        } catch {
            Write-Host "   ❌ Puerto $port - $service (no responde)" -ForegroundColor Red
        }
    }
    Write-Host ""
}

Write-Host "========================================" -ForegroundColor Cyan
if ($serversFound -gt 0) {
    Write-Host "✅ $serversFound servidor(es) encontrado(s)" -ForegroundColor Green
    Write-Host ""
    Write-Host "Tu app móvil debería funcionar correctamente" -ForegroundColor Green
} else {
    Write-Host "⚠️  NO SE ENCONTRARON SERVIDORES" -ForegroundColor Red
    Write-Host ""
    Write-Host "Necesitas iniciar al menos el servidor HTTP:" -ForegroundColor Yellow
    Write-Host "   1. Ejecuta: INICIAR_SERVIDOR_TEST.bat" -ForegroundColor White
    Write-Host "   O manualmente: python -m http.server 8000" -ForegroundColor White
}
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Instrucciones adicionales
Write-Host "📋 COMANDOS ÚTILES:" -ForegroundColor Yellow
Write-Host "   Servidor HTTP:  python -m http.server 8000" -ForegroundColor White
Write-Host "   Backend Node:   npm start (en rn-postgres-example/backend)" -ForegroundColor White
Write-Host "   Backend Flask:  python main.py (en backend)" -ForegroundColor White
Write-Host ""

Read-Host "Presiona Enter para salir"
