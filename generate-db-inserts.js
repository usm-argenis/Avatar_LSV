#!/usr/bin/env node

/**
 * Genera SQL con URLs reales desde GitHub Releases
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const REPO = 'usm-argenis/Avatar_LSV';
const RELEASE_TAG = 'models-v1';
const GH_PATH = 'C:\\Program Files\\GitHub CLI\\gh.exe';

console.log('🔍 Obteniendo assets desde GitHub Releases...\n');

// Obtener lista de assets
const assetsJson = execSync(`"${GH_PATH}" release view ${RELEASE_TAG} --repo ${REPO} --json assets`).toString();
const release = JSON.parse(assetsJson);
const assets = release.assets;

console.log(`✅ Encontrados ${assets.length} archivos en el release\n`);

// Generar SQL
let sql = '';
sql += '-- Inserción automática desde GitHub Releases\n';
sql += `-- Release: ${RELEASE_TAG}\n`;
sql += `-- Assets: ${assets.length}\n`;
sql += `-- Generado: ${new Date().toISOString()}\n\n`;
sql += 'BEGIN;\n\n';

let count = 0;
const errors = [];

for (const asset of assets) {
    const fileName = asset.name;
    const url = asset.url;
    const sizeMB = (asset.size / (1024 * 1024)).toFixed(2);
    
    // Extraer información del nombre del archivo
    // Formato esperado: Avatar_resultado_palabra.glb o Avatar.glb
    const match = fileName.match(/^([A-Za-z]+)(?:_resultado)?_?(.+)?\.glb$/);
    
    if (!match) {
        errors.push(`Nombre de archivo no reconocido: ${fileName}`);
        continue;
    }
    
    const avatar = match[1];
    let palabra = match[2] || 'base';
    
    // Determinar categoría (por ahora, dejarla vacía y actualizarla manualmente)
    // O inferirla desde la estructura de carpetas local
    const categoria = 'sin_categoria'; // Placeholder
    
    const esDeletreo = palabra.length === 1 && /^[a-zñ]$/.test(palabra);
    
    sql += `-- ${fileName}\n`;
    sql += `INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)\n`;
    sql += `VALUES ('${avatar}', '${categoria}', '${palabra}', '${fileName}', '${url}', ${sizeMB}, ${esDeletreo})\n`;
    sql += `ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET\n`;
    sql += `  url_github = EXCLUDED.url_github,\n`;
    sql += `  peso_mb = EXCLUDED.peso_mb,\n`;
    sql += `  updated_at = CURRENT_TIMESTAMP;\n\n`;
    
    count++;
}

sql += 'COMMIT;\n';

// Guardar SQL
const outputPath = path.join(__dirname, 'database', 'insert_from_github.sql');
fs.writeFileSync(outputPath, sql);

console.log(`✅ SQL generado: ${outputPath}`);
console.log(`📊 Registros: ${count}`);

if (errors.length > 0) {
    console.log(`\n⚠️  Archivos no procesados: ${errors.length}`);
    errors.forEach(err => console.log(`  - ${err}`));
}

console.log('\n🎯 Próximo paso:');
console.log(`   psql -U postgres -d VeneSeñas -f "${outputPath}"`);
