#!/usr/bin/env node

/**
 * Script optimizado para subir SOLO Duvall y Carla a GitHub Releases
 */

const fs = require('fs');
const path = require('path');

const GLB_DIR = path.join(__dirname, 'test', 'output', 'glb');
const REPO = 'usm-argenis/Avatar_LSV';
const AVATARES_SELECCIONADOS = ['Duvall', 'Carla'];

function getFilesForAvatars(avatares) {
    const groups = {};
    
    avatares.forEach(avatar => {
        const avatarPath = path.join(GLB_DIR, avatar);
        
        if (!fs.existsSync(avatarPath)) {
            console.log(`⚠️  Avatar ${avatar} no encontrado`);
            return;
        }
        
        const items = fs.readdirSync(avatarPath);
        
        items.forEach(item => {
            const itemPath = path.join(avatarPath, item);
            const stat = fs.statSync(itemPath);
            
            if (stat.isDirectory()) {
                const categoria = item;
                const key = `${avatar}-${categoria}`;
                
                if (!groups[key]) {
                    groups[key] = {
                        avatar,
                        categoria,
                        files: []
                    };
                }
                
                const glbFiles = fs.readdirSync(itemPath)
                    .filter(f => f.endsWith('.glb'))
                    .map(f => path.join(itemPath, f));
                
                groups[key].files.push(...glbFiles);
            } else if (item.endsWith('.glb')) {
                const key = `${avatar}-base`;
                
                if (!groups[key]) {
                    groups[key] = {
                        avatar,
                        categoria: 'base',
                        files: []
                    };
                }
                
                groups[key].files.push(itemPath);
            }
        });
    });
    
    return groups;
}

function generateSQL(groups) {
    let sql = '-- Inserción de modelos GLB para Duvall y Carla\n';
    sql += '-- Generado: ' + new Date().toISOString() + '\n\n';
    sql += 'BEGIN;\n\n';
    
    Object.keys(groups).forEach(key => {
        const { avatar, categoria, files } = groups[key];
        
        sql += `-- ${avatar} - ${categoria} (${files.length} archivos)\n`;
        
        files.forEach(filePath => {
            const fileName = path.basename(filePath);
            const stats = fs.statSync(filePath);
            const pesoMB = (stats.size / (1024 * 1024)).toFixed(2);
            
            let nombrePalabra = fileName
                .replace(/^[A-Za-z]+_resultado_/, '')
                .replace(/^[A-Za-z]+_/, '')
                .replace('.glb', '');
            
            if (fileName === `${avatar}.glb`) {
                nombrePalabra = 'base';
            }
            
            const esDeletreo = categoria === 'alfabeto' && nombrePalabra.length === 1;
            const releaseTag = `models-v1`;
            const url = `https://github.com/${REPO}/releases/download/${releaseTag}/${avatar}/${categoria}/${encodeURIComponent(fileName)}`;
            
            sql += `INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)\n`;
            sql += `VALUES ('${avatar}', '${categoria}', '${nombrePalabra}', '${fileName}', '${url}', ${pesoMB}, ${esDeletreo})\n`;
            sql += `ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET\n`;
            sql += `  url_github = EXCLUDED.url_github,\n`;
            sql += `  peso_mb = EXCLUDED.peso_mb,\n`;
            sql += `  updated_at = CURRENT_TIMESTAMP;\n\n`;
        });
    });
    
    sql += 'COMMIT;\n';
    
    return sql;
}

function generatePowerShellScript(groups) {
    let script = '# Script PowerShell para subir Duvall y Carla a GitHub Releases\n';
    script += '# Requiere GitHub CLI instalado y autenticado\n\n';
    script += '$ErrorActionPreference = "Continue"\n\n';
    script += `$REPO = "${REPO}"\n`;
    script += `$RELEASE_TAG = "models-v1"\n\n`;
    
    script += '# Crear release único para todos los modelos\n';
    script += 'Write-Host "📦 Creando release models-v1..."\n';
    script += 'gh release create $RELEASE_TAG --repo $REPO --title "Modelos GLB - Duvall y Carla" --notes "Archivos GLB para avatares Duvall y Carla con todas las categorías"\n\n';
    
    script += 'Write-Host "📤 Subiendo archivos en lotes..."\n';
    script += '$totalGroups = ' + Object.keys(groups).length + '\n';
    script += '$currentGroup = 0\n\n';
    
    Object.keys(groups).forEach(key => {
        const { avatar, categoria, files } = groups[key];
        
        script += `\n# ${avatar} - ${categoria} (${files.length} archivos)\n`;
        script += '$currentGroup++\n';
        script += `Write-Host "[$currentGroup/$totalGroups] Subiendo ${avatar} - ${categoria}..."\n\n`;
        
        // Dividir en lotes de 20 archivos (más conservador)
        for (let i = 0; i < files.length; i += 20) {
            const batch = files.slice(i, i + 20);
            const batchNum = Math.floor(i / 20) + 1;
            const totalBatches = Math.ceil(files.length / 20);
            
            script += `Write-Host "  Lote ${batchNum}/${totalBatches}..."\n`;
            script += 'gh release upload $RELEASE_TAG `\n';
            
            batch.forEach((file, idx) => {
                const relativePath = path.relative(process.cwd(), file);
                script += `  "${relativePath.replace(/\\/g, '/')}"`;
                if (idx < batch.length - 1) script += ' `\n';
                else script += ' `\n';
            });
            
            script += '  --repo $REPO --clobber\n\n';
        }
    });
    
    script += 'Write-Host ""\n';
    script += 'Write-Host "✅ Subida completa!" -ForegroundColor Green\n';
    script += 'Write-Host "🔗 Ver release: https://github.com/$REPO/releases/tag/$RELEASE_TAG"\n';
    
    return script;
}

function main() {
    console.log('🎯 Preparando subida de Duvall y Carla...\n');
    
    const groups = getFilesForAvatars(AVATARES_SELECCIONADOS);
    const totalGroups = Object.keys(groups).length;
    let totalFiles = 0;
    let totalSize = 0;
    
    console.log(`Grupos encontrados:\n`);
    
    Object.keys(groups).forEach(key => {
        const { avatar, categoria, files } = groups[key];
        const groupSize = files.reduce((sum, f) => sum + fs.statSync(f).size, 0);
        totalFiles += files.length;
        totalSize += groupSize;
        
        const sizeMB = (groupSize / (1024 * 1024)).toFixed(1);
        console.log(`  ${avatar.padEnd(10)} | ${categoria.padEnd(20)} | ${files.length.toString().padStart(4)} archivos | ${sizeMB.padStart(7)} MB`);
    });
    
    const totalSizeGB = (totalSize / (1024 * 1024 * 1024)).toFixed(2);
    console.log(`\n📊 Total: ${totalFiles} archivos en ${totalGroups} grupos (${totalSizeGB} GB)\n`);
    
    // Generar SQL
    console.log('💾 Generando SQL...');
    const sql = generateSQL(groups);
    fs.writeFileSync('database/insert_duvall_carla.sql', sql);
    console.log('✅ SQL generado: database/insert_duvall_carla.sql\n');
    
    // Generar script PowerShell
    console.log('📝 Generando script de subida...');
    const script = generatePowerShellScript(groups);
    fs.writeFileSync('upload-duvall-carla.ps1', script);
    console.log('✅ Script generado: upload-duvall-carla.ps1\n');
    
    console.log('🎯 SIGUIENTES PASOS:\n');
    console.log('1. Autenticar GitHub CLI:');
    console.log('   gh auth login\n');
    console.log('2. Subir archivos (tarda ~20-30 min):');
    console.log('   powershell -ExecutionPolicy Bypass -File upload-duvall-carla.ps1\n');
    console.log('3. Ejecutar SQL en PostgreSQL:');
    console.log('   psql -U postgres -d VeneSeñas -f database/insert_duvall_carla.sql\n');
}

main();
