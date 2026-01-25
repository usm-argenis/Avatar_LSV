# Script para organizar archivos de Duvall en la estructura correcta
$origen = "C:\Users\andre\Downloads\Duvall_2"
$destino = "test\output\glb\Duvall"

Write-Host "`n=== ORGANIZANDO ARCHIVOS DE DUVALL ===" -ForegroundColor Cyan

# Crear estructura de carpetas
$categorias = @(
    "cortesia",
    "dias_semana", 
    "expresiones",
    "preguntas",
    "pronombres",
    "saludos",
    "tiempo",
    "alfabeto",
    "otros"
)

Write-Host "`nCreando estructura de carpetas..." -ForegroundColor Yellow
foreach ($cat in $categorias) {
    $ruta = Join-Path $destino $cat
    if (!(Test-Path $ruta)) {
        New-Item -ItemType Directory -Path $ruta -Force | Out-Null
        Write-Host "   OK Creada: $cat" -ForegroundColor Green
    }
}

# Mapeo de archivos a categorías
$mapeo = @{
    # Cortesía
    "a la orden" = "cortesia"
    "buen provecho" = "cortesia"
    "cortesia" = "cortesia"
    "gracias" = "cortesia"
    "muchas gracias" = "cortesia"
    "mucho gusto" = "cortesia"
    "permiso" = "cortesia"
    "de nada" = "cortesia"
    
    # Días de la semana
    "domingo" = "dias_semana"
    "jueves" = "dias_semana"
    "lunes" = "dias_semana"
    "martes" = "dias_semana"
    "miercoles" = "dias_semana"
    "sabado" = "dias_semana"
    "viernes" = "dias_semana"
    
    # Expresiones
    "expresiones" = "expresiones"
    "saludas a" = "expresiones"
    "mal" = "expresiones"
    "no" = "expresiones"
    "regular" = "expresiones"
    "si" = "expresiones"
    
    # Preguntas
    "como estas" = "preguntas"
    "cual es tu nombre" = "preguntas"
    "cual es tu sena" = "preguntas"
    "que tal" = "preguntas"
    
    # Pronombres
    "el" = "pronombres"
    "ella" = "pronombres"
    "ellas" = "pronombres"
    "ellos" = "pronombres"
    "nosotros" = "pronombres"
    "tu" = "pronombres"
    "ustedes" = "pronombres"
    "yo" = "pronombres"
    
    # Saludos
    "adios" = "saludos"
    "bienvenido" = "saludos"
    "bien" = "saludos"
    "buenas noches" = "saludos"
    "buenas tardes" = "saludos"
    "buenos dias" = "saludos"
    "chao" = "saludos"
    "hola" = "saludos"
    
    # Tiempo
    "anteayer" = "tiempo"
    "ayer" = "tiempo"
    "calendario" = "tiempo"
    "fin de semana" = "tiempo"
    "hoy" = "tiempo"
    "manana" = "tiempo"
    "mes" = "tiempo"
    "pasado manana" = "tiempo"
    "semana" = "tiempo"
    
    # Otros
    "r" = "otros"
}

# Obtener todos los archivos GLB
$archivos = Get-ChildItem -Path $origen -Filter "*.glb"

Write-Host "`nProcesando $($archivos.Count) archivos..." -ForegroundColor Yellow

$copiados = 0
$errores = 0

foreach ($archivo in $archivos) {
    # Extraer nombre base (quitar _default y extensión)
    $nombreBase = $archivo.BaseName -replace '_default.*$', ''
    
    # Buscar categoría
    $categoria = $mapeo[$nombreBase]
    
    if ($categoria) {
        # Crear nombre de destino: Duvall_resultado_nombreBase.glb
        $nombreDestino = "Duvall_resultado_$nombreBase.glb"
        $rutaDestino = Join-Path -Path $destino -ChildPath $categoria | Join-Path -ChildPath $nombreDestino
        
        try {
            Copy-Item -Path $archivo.FullName -Destination $rutaDestino -Force
            Write-Host "   OK $nombreBase -> $categoria" -ForegroundColor Green
            $copiados++
        }
        catch {
            Write-Host "   ERROR con $nombreBase : $_" -ForegroundColor Red
            $errores++
        }
    }
    else {
        Write-Host "   SIN CATEGORIA: $nombreBase" -ForegroundColor Yellow
    }
}

# Resumen
Write-Host "`n=== RESUMEN ===" -ForegroundColor Cyan
Write-Host "Archivos copiados: $copiados" -ForegroundColor Green
Write-Host "Errores: $errores" -ForegroundColor Red
Write-Host "`nArchivos organizados en: $destino" -ForegroundColor Cyan
Write-Host ""
