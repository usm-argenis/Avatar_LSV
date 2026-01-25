$Base = "C:\Users\andre\OneDrive\Documentos\tesis"
$src = Join-Path $Base "__backup__\unused\glb"
$dst = Join-Path $Base "test\output\glb"

Write-Host "Backup glb source: $src"
Write-Host "Destination: $dst"

if (-not (Test-Path $src)) {
    Write-Host "No backup glb folder found at $src. Nothing to restore."; exit 0
}

# Ensure destination exists
New-Item -ItemType Directory -Path $dst -Force | Out-Null

# Move files (only files, do not touch subdirectories)
Get-ChildItem -Path $src -Force | Where-Object { -not $_.PSIsContainer } | ForEach-Object {
    $name = $_.Name
    $srcPath = $_.FullName
    $dstPath = Join-Path $dst $name
    try {
        Move-Item -LiteralPath $srcPath -Destination $dstPath -Force
        Write-Host "Restored: $name"
    } catch {
        Write-Host "Failed to restore: $name -> $_"
    }
}

Write-Host "Done. Restored files placed in $dst."