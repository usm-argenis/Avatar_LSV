$Base = "C:\Users\andre\OneDrive\Documentos\tesis"
$Backup = Join-Path $Base "__backup__\unused"
New-Item -ItemType Directory -Path $Backup -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $Backup 'glb') -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $Backup 'output') -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $Backup 'bat_files') -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $Backup 'videos') -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $Backup 'animations') -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $Backup 'deploy_temp') -Force | Out-Null

Write-Host "Moving test\output\glb files..."
$glbDir = Join-Path $Base 'test\output\glb'
if (Test-Path $glbDir) {
    Get-ChildItem -Path $glbDir -Force | Where-Object { -not $_.PSIsContainer } | ForEach-Object {
        Move-Item -LiteralPath $_.FullName -Destination (Join-Path $Backup 'glb') -Force -ErrorAction SilentlyContinue
    }
} else { Write-Host "  no test\output\glb found" }

Write-Host "Moving root output folder..."
$rootOutput = Join-Path $Base 'output'
if (Test-Path $rootOutput) { Move-Item -LiteralPath $rootOutput -Destination (Join-Path $Backup 'output') -Force -ErrorAction SilentlyContinue } else { Write-Host "  no output folder" }

Write-Host "Moving deploy-viewer-temp..."
$deployTemp = Join-Path $Base 'deploy-viewer-temp'
if (Test-Path $deployTemp) { Move-Item -LiteralPath $deployTemp -Destination (Join-Path $Backup 'deploy_temp') -Force -ErrorAction SilentlyContinue } else { Write-Host "  no deploy-viewer-temp" }

Write-Host "Moving .bat files from repo root..."
Get-ChildItem -Path $Base -Filter '*.bat' -File -ErrorAction SilentlyContinue | ForEach-Object { Move-Item -LiteralPath $_.FullName -Destination (Join-Path $Backup 'bat_files') -Force -ErrorAction SilentlyContinue }

Write-Host "Moving .bat files under convertidor_abeceda and convertidor..."
foreach($d in @('convertidor_abeceda','convertidor')){
    $p = Join-Path $Base $d
    if (Test-Path $p) {
        Get-ChildItem -Path $p -Filter '*.bat' -File -Recurse -ErrorAction SilentlyContinue | ForEach-Object { Move-Item -LiteralPath $_.FullName -Destination (Join-Path $Backup 'bat_files') -Force -ErrorAction SilentlyContinue }
    }
}

Write-Host "Moving animations directories..."
foreach($anim in @('animaciones_remy','animaciones_lsv_final')){
    $path = Join-Path $Base $anim
    if (Test-Path $path) { Move-Item -LiteralPath $path -Destination (Join-Path $Backup 'animations') -Force -ErrorAction SilentlyContinue }
}

Write-Host "Moving large video files (root and data) to backup/videos..."
Get-ChildItem -Path $Base -Include *.mp4 -File -Recurse -ErrorAction SilentlyContinue | ForEach-Object {
    if ($_.FullName -notlike "*$Backup*") { Move-Item -LiteralPath $_.FullName -Destination (Join-Path $Backup 'videos') -Force -ErrorAction SilentlyContinue }
}

Write-Host "Moving deploy_github_pages.bat if present..."
$dg = Join-Path $Base 'deploy_github_pages.bat'
if (Test-Path $dg) { Move-Item -LiteralPath $dg -Destination (Join-Path $Backup 'bat_files') -Force -ErrorAction SilentlyContinue }

Write-Host "Finished moves. Listing backup contents:"
Get-ChildItem -Path $Backup -Recurse | Select-Object FullName | ForEach-Object { Write-Host $_.FullName }
