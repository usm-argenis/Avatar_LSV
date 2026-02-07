const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Configuración
const REPO = 'usm-argenis/Avatar_LSV';
const RELEASE_TAG = 'models-v1';
const OUTPUT_DIR = path.join(__dirname, 'assets', 'models', 'animaciones');

// Asegurar que existe el directorio
if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

console.log('📥 Descargando archivos de GitHub Release...');
console.log(`Release: ${RELEASE_TAG}`);
console.log(`Destino: ${OUTPUT_DIR}\n`);

try {
    // Descargar todos los archivos del release (excepto los base que ya están)
    const command = `gh release download ${RELEASE_TAG} --repo ${REPO} --pattern "*_resultado_*.glb" --dir "${OUTPUT_DIR}" --skip-existing`;
    
    console.log('🔄 Ejecutando descarga...');
    execSync(command, { 
        stdio: 'inherit',
        env: { 
            ...process.env,
            PATH: process.env.PATH + ';C:\\Program Files\\GitHub CLI'
        }
    });
    
    console.log('\n✅ Descarga completada');
    
    // Contar archivos descargados
    const files = fs.readdirSync(OUTPUT_DIR).filter(f => f.endsWith('.glb'));
    console.log(`📊 Total de archivos: ${files.length}`);
    
} catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
}
