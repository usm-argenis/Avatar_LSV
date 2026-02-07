const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Configuración
const ANIMACIONES_DIR = path.join(__dirname, 'assets', 'models', 'animaciones');
const BATCH_SIZE = 50; // Subir 50 archivos a la vez

console.log('📦 Preparando carga de archivos GLB al repositorio...\n');

// Obtener lista de archivos
const files = fs.readdirSync(ANIMACIONES_DIR)
    .filter(f => f.endsWith('.glb'))
    .sort();

console.log(`📊 Total de archivos encontrados: ${files.length}`);
console.log(`🔢 Tamaño de lote: ${BATCH_SIZE} archivos\n`);

const totalBatches = Math.ceil(files.length / BATCH_SIZE);

for (let i = 0; i < files.length; i += BATCH_SIZE) {
    const batch = files.slice(i, i + BATCH_SIZE);
    const batchNumber = Math.floor(i / BATCH_SIZE) + 1;
    
    console.log(`\n📤 Lote ${batchNumber}/${totalBatches} (${batch.length} archivos)...`);
    
    try {
        // Agregar archivos de este lote
        const filePaths = batch.map(f => 
            `"assets/models/animaciones/${f}"`
        ).join(' ');
        
        execSync(`git add -f ${filePaths}`, { stdio: 'inherit' });
        
        // Commit
        const firstFile = batch[0].replace('_resultado_', ' - ').replace('.glb', '');
        const lastFile = batch[batch.length - 1].replace('_resultado_', ' - ').replace('.glb', '');
        
        const commitMsg = `feat: Agregar lote ${batchNumber}/${totalBatches} de animaciones GLB

Archivos: ${batch.length}
Rango: ${firstFile} ... ${lastFile}`;
        
        execSync(`git commit -m "${commitMsg.replace(/\n/g, ' ')}"`, { stdio: 'inherit' });
        
        // Push
        console.log(`⬆️ Subiendo lote ${batchNumber} a GitHub...`);
        execSync('git push', { stdio: 'inherit' });
        
        console.log(`✅ Lote ${batchNumber}/${totalBatches} completado`);
        
    } catch (error) {
        console.error(`❌ Error en lote ${batchNumber}:`, error.message);
        process.exit(1);
    }
}

console.log('\n✅ Todos los lotes han sido subidos exitosamente');
console.log(`📊 Total de archivos subidos: ${files.length}`);
