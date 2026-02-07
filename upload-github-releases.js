#!/usr/bin/env node

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const REPO = 'usm-argenis/Avatar_LSV';
const RELEASE_TAG = 'models-v1';
const BASE_DIR = path.join(__dirname, 'test', 'output', 'glb');
const AVATARES = ['Duvall', 'Carla'];
const BATCH_SIZE = 15;
const GH_PATH = 'C:\\Program Files\\GitHub CLI\\gh.exe';
const LOG_FILE = path.join(__dirname, 'upload-progress.log');

// Función para log
function log(message) {
    const timestamp = new Date().toISOString();
    const logMessage = `[${timestamp}] ${message}\n`;
    console.log(message);
    fs.appendFileSync(LOG_FILE, logMessage);
}

// Limpiar log anterior
if (fs.existsSync(LOG_FILE)) {
    fs.unlinkSync(LOG_FILE);
}

log('========================================');
log(' Subida de Modelos GLB a GitHub');
log('  Avatares: Duvall y Carla');
log('========================================\n');

// Verificar autenticación
try {
    execSync(`"${GH_PATH}" auth status`, { stdio: 'pipe' });
    log('✅ Autenticado correctamente\n');
} catch (error) {
    log('❌ No autenticado. Ejecuta: gh auth login');
    process.exit(1);
}

// Crear release
log(`📦 Creando release '${RELEASE_TAG}'...`);
try {
    execSync(`"${GH_PATH}" release create ${RELEASE_TAG} --repo ${REPO} --title "Modelos GLB - Duvall y Carla" --notes "Archivos GLB para avatares Duvall y Carla"`, { stdio: 'pipe' });
    log('✅ Release creado\n');
} catch (error) {
    log('⚠️  Release ya existe. Continuando...\n');
}

let totalUploaded = 0;
let totalErrors = 0;

// Procesar cada avatar
for (const avatar of AVATARES) {
    const avatarPath = path.join(BASE_DIR, avatar);
    
    if (!fs.existsSync(avatarPath)) {
        console.log(`⚠️  No se encontró: ${avatar}`);
        continue;
    }
    
    console.log(`👤 Procesando avatar: ${avatar}`);
    
    // Obtener categorías
    const items = fs.readdirSync(avatarPath);
    const categorias = items.filter(item => {
        const itemPath = path.join(avatarPath, item);
        return fs.statSync(itemPath).isDirectory();
    });
    
    const totalCategorias = categorias.length;
    let currentCategoria = 0;
    
    for (const categoria of categorias) {
        currentCategoria++;
        const categoriaPath = path.join(avatarPath, categoria);
        
        // Obtener archivos GLB
        const glbFiles = fs.readdirSync(categoriaPath)
            .filter(f => f.endsWith('.glb'))
            .map(f => path.join(categoriaPath, f));
        
        const fileCount = glbFiles.length;
        
        if (fileCount === 0) {
            console.log(`  [${currentCategoria}/${totalCategorias}] ${categoria} - Sin archivos`);
            continue;
        }
        
        console.log(`  [${currentCategoria}/${totalCategorias}] ${categoria} (${fileCount} archivos)`);
        
        // Dividir en lotes
        const totalBatches = Math.ceil(fileCount / BATCH_SIZE);
        
        for (let i = 0; i < fileCount; i += BATCH_SIZE) {
            const batchNum = Math.floor(i / BATCH_SIZE) + 1;
            const batch = glbFiles.slice(i, i + BATCH_SIZE);
            
            console.log(`    Lote ${batchNum}/${totalBatches} (${batch.length} archivos)...`);
            
            // Construir comando con rutas escapadas
            const filesArgs = batch.map(f => `"${f}"`).join(' ');
            const command = `"${GH_PATH}" release upload ${RELEASE_TAG} ${filesArgs} --repo ${REPO} --clobber`;
            
            try {
                execSync(command, { stdio: 'pipe', maxBuffer: 50 * 1024 * 1024 });
                console.log(`      ✅ Lote ${batchNum} subido`);
                totalUploaded += batch.length;
            } catch (error) {
                console.error(`      ❌ Error en lote ${batchNum}`);
                totalErrors += batch.length;
            }
        }
        
        console.log('');
    }
    
    // Archivo base del avatar
    const avatarBase = path.join(avatarPath, `${avatar}.glb`);
    if (fs.existsSync(avatarBase)) {
        console.log(`  Subiendo archivo base: ${avatar}.glb`);
        try {
            execSync(`"${GH_PATH}" release upload ${RELEASE_TAG} "${avatarBase}" --repo ${REPO} --clobber`, { stdio: 'pipe' });
            console.log('  ✅ Archivo base subido');
            totalUploaded++;
        } catch (error) {
            console.error('  ❌ Error subiendo archivo base');
            totalErrors++;
        }
    }
    
    console.log('');
}

// Resumen
console.log('========================================');
console.log('  RESUMEN DE SUBIDA');
console.log('========================================');
console.log(`✅ Archivos subidos: ${totalUploaded}`);
console.log(`❌ Errores: ${totalErrors}`);
console.log('');
console.log('🔗 Ver release:');
console.log(`   https://github.com/${REPO}/releases/tag/${RELEASE_TAG}`);
console.log('');

if (totalErrors === 0) {
    console.log('🎉 ¡Subida completada exitosamente!');
} else {
    console.log('⚠️  Subida completada con algunos errores');
}
