# Script PowerShell mejorado para subir Duvall y Carla a GitHub Releases
# Maneja correctamente rutas con espacios

$ErrorActionPreference = "Continue"

$REPO = "usm-argenis/Avatar_LSV"
$RELEASE_TAG = "models-v1"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Subida de Modelos GLB a GitHub" -ForegroundColor Cyan
Write-Host "  Avatares: Duvall y Carla" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Refrescar PATH
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Verificar autenticación
Write-Host "🔐 Verificando autenticación..." -ForegroundColor Yellow
$authStatus = gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ No estás autenticado. Ejecuta: gh auth login" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Autenticado correctamente" -ForegroundColor Green
Write-Host ""

# Crear release
Write-Host "📦 Creando release '$RELEASE_TAG'..." -ForegroundColor Yellow
gh release create $RELEASE_TAG --repo $REPO --title "Modelos GLB - Duvall y Carla" --notes "Archivos GLB para avatares Duvall y Carla con todas las categorías" 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Release creado exitosamente" -ForegroundColor Green
} else {
    Write-Host "⚠️  Release ya existe o error al crear. Continuando..." -ForegroundColor Yellow
}
Write-Host ""

# Obtener todos los archivos GLB de Duvall y Carla
$baseDir = "test\output\glb"
$avatares = @("Duvall", "Carla")
$batchSize = 15  # Archivos por lote (conservador para evitar timeouts)
$totalUploaded = 0
$totalErrors = 0

foreach ($avatar in $avatares) {
    $avatarPath = Join-Path $baseDir $avatar
    
    if (-not (Test-Path $avatarPath)) {
        Write-Host "⚠️  No se encontró carpeta para avatar: $avatar" -ForegroundColor Yellow
        continue
    }
    
    Write-Host "👤 Procesando avatar: $avatar" -ForegroundColor Cyan
    Write-Host "   Ruta: $avatarPath" -ForegroundColor Gray
    Write-Host ""
    
    # Obtener todas las categorías
    $categorias = Get-ChildItem -Path $avatarPath -Directory
    $totalCategorias = $categorias.Count
    $currentCategoria = 0
    
    foreach ($categoria in $categorias) {
        $currentCategoria++
        $categoriaName = $categoria.Name
        
        # Obtener archivos GLB en la categoría
        $glbFiles = Get-ChildItem -Path $categoria.FullName -Filter "*.glb"
        $fileCount = $glbFiles.Count
        
        if ($fileCount -eq 0) {
            Write-Host "  [$currentCategoria/$totalCategorias] $categoriaName - Sin archivos" -ForegroundColor Gray
            continue
        }
        
        Write-Host "  [$currentCategoria/$totalCategorias] $categoriaName ($fileCount archivos)" -ForegroundColor Yellow
        
        # Dividir en lotes
        $totalBatches = [Math]::Ceiling($fileCount / $batchSize)
        
        for ($i = 0; $i -lt $fileCount; $i += $batchSize) {
            $batchNum = [Math]::Floor($i / $batchSize) + 1
            $batch = $glbFiles | Select-Object -Skip $i -First $batchSize
            $batchFileCount = $batch.Count
            
            Write-Host "    Lote $batchNum/$totalBatches ($batchFileCount archivos)..." -ForegroundColor Gray
            
            # Construir array de rutas
            $filePaths = @()
            foreach ($file in $batch) {
                $filePaths += $file.FullName
            }
            
            # Subir lote
            try {
                $uploadArgs = @($RELEASE_TAG) + $filePaths + @("--repo", $REPO, "--clobber")
                & gh release upload $uploadArgs 2>&1 | Out-Null
                
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "      ✅ Lote $batchNum subido" -ForegroundColor Green
                    $totalUploaded += $batchFileCount
                } else {
                    Write-Host "      ❌ Error en lote $batchNum" -ForegroundColor Red
                    $totalErrors += $batchFileCount
                }
            } catch {
                Write-Host "      ❌ Excepción en lote $batchNum : $_" -ForegroundColor Red
                $totalErrors += $batchFileCount
            }
            
            # Pequeña pausa entre lotes para no saturar la API
            Start-Sleep -Milliseconds 500
        }
        
        Write-Host ""
    }
    
    # Procesar archivo base del avatar (si existe)
    $avatarBase = Join-Path $avatarPath "$avatar.glb"
    if (Test-Path $avatarBase) {
        Write-Host "  Subiendo archivo base: $avatar.glb" -ForegroundColor Yellow
        try {
            gh release upload $RELEASE_TAG $avatarBase --repo $REPO --clobber 2>&1 | Out-Null
            if ($LASTEXITCODE -eq 0) {
                Write-Host "  ✅ Archivo base subido" -ForegroundColor Green
                $totalUploaded++
            } else {
                Write-Host "  ❌ Error subiendo archivo base" -ForegroundColor Red
                $totalErrors++
            }
        } catch {
            Write-Host "  ❌ Excepción subiendo archivo base: $_" -ForegroundColor Red
            $totalErrors++
        }
    }
    
    Write-Host ""
}

# Resumen final
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  RESUMEN DE SUBIDA" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✅ Archivos subidos: $totalUploaded" -ForegroundColor Green
Write-Host "❌ Errores: $totalErrors" -ForegroundColor $(if ($totalErrors -gt 0) { "Red" } else { "Green" })
Write-Host ""
Write-Host "🔗 Ver release:" -ForegroundColor Cyan
Write-Host "   https://github.com/$REPO/releases/tag/$RELEASE_TAG" -ForegroundColor Blue
Write-Host ""

if ($totalErrors -eq 0) {
    Write-Host "🎉 ¡Subida completada exitosamente!" -ForegroundColor Green
} else {
    Write-Host "⚠️  Subida completada con algunos errores" -ForegroundColor Yellow
}
