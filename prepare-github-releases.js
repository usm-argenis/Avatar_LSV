#!/usr/bin/env node

/**
 * Script para subir archivos GLB a GitHub Releases
 * Organizado por avatar y categoría
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const GLB_DIR = path.join(__dirname, 'test', 'output', 'glb');
const REPO = 'usm-argenis/Avatar_LSV';
const BASE_VERSION = 'models';

// Función para obtener archivos agrupados por avatar y categoría
function getGroupedFiles() {
    const groups = {};
    
    // Obtener todos los avatares
    const avatares = fs.readdirSync(GLB_DIR).filter(item => {
        const fullPath = path.join(GLB_DIR, item);
        return fs.statSync(fullPath).isDirectory();
    });
    
    avatares.forEach(avatar => {
        const avatarPath = path.join(GLB_DIR, avatar);
        
        // Obtener categorías
        const items = fs.readdirSync(avatarPath);
        
        items.forEach(item => {
            const itemPath = path.join(avatarPath, item);
            const stat = fs.statSync(itemPath);
            
            if (stat.isDirectory()) {
                // Es una categoría
                const categoria = item;
                const key = `${avatar}-${categoria}`;
                
                if (!groups[key]) {
                    groups[key] = {
                        avatar,
                        categoria,
                        files: []
                    };
                }
                
                // Obtener archivos GLB en la categoría
                const glbFiles = fs.readdirSync(itemPath)
                    .filter(f => f.endsWith('.glb'))
                    .map(f => path.join(itemPath, f));
                
                groups[key].files.push(...glbFiles);
            } else if (item.endsWith('.glb')) {
                // Archivo GLB directo (avatar base)
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

// Generar SQL para insertar en base de datos
function generateSQL(groups, baseUrl) {
    let sql = '-- Inserción automática de modelos GLB\n';
    sql += '-- Generado: ' + new Date().toISOString() + '\n\n';
    sql += 'BEGIN;\n\n';
    
    Object.keys(groups).forEach(key => {
        const { avatar, categoria, files } = groups[key];
        
        sql += `-- ${avatar} - ${categoria} (${files.length} archivos)\n`;
        
        files.forEach(filePath => {
            const fileName = path.basename(filePath);
            const relativePath = path.relative(GLB_DIR, filePath).replace(/\\/g, '/');
            const stats = fs.statSync(filePath);
            const pesoMB = (stats.size / (1024 * 1024)).toFixed(2);
            
            // Extraer nombre de palabra del archivo
            // Formato: Avatar_resultado_palabra.glb o Avatar.glb
            let nombrePalabra = fileName
                .replace(/^[A-Za-z]+_resultado_/, '')
                .replace(/^[A-Za-z]+_/, '')
                .replace('.glb', '');
            
            if (fileName === `${avatar}.glb`) {
                nombrePalabra = 'base';
            }
            
            const esDeletreo = categoria === 'alfabeto' && nombrePalabra.length === 1;
            
            // URL en GitHub Release
            const releaseTag = `${BASE_VERSION}-${avatar.toLowerCase()}-${categoria.toLowerCase()}`;
            const url = `https://github.com/${REPO}/releases/download/${releaseTag}/${encodeURIComponent(fileName)}`;
            
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

// Función principal
function main() {
    console.log('📦 Analizando archivos GLB...\n');
    
    const groups = getGroupedFiles();
    const totalGroups = Object.keys(groups).length;
    let totalFiles = 0;
    
    console.log(`Encontrados ${totalGroups} grupos:\n`);
    
    Object.keys(groups).forEach(key => {
        const { avatar, categoria, files } = groups[key];
        totalFiles += files.length;
        console.log(`  ${avatar.padEnd(10)} | ${categoria.padEnd(20)} | ${files.length.toString().padStart(4)} archivos`);
    });
    
    console.log(`\n📊 Total: ${totalFiles} archivos en ${totalGroups} grupos\n`);
    
    // Generar SQL
    console.log('💾 Generando SQL...');
    const sql = generateSQL(groups, REPO);
    fs.writeFileSync('database/insert_glb_models.sql', sql);
    console.log('✅ SQL generado: database/insert_glb_models.sql\n');
    
    // Generar comandos para subir a GitHub
    console.log('📝 Generando comandos de GitHub CLI...\n');
    
    let commands = '';
    commands += '# Comandos para subir archivos a GitHub Releases\n';
    commands += '# Requiere GitHub CLI: https://cli.github.com/\n\n';
    
    Object.keys(groups).forEach(key => {
        const { avatar, categoria, files } = groups[key];
        const releaseTag = `${BASE_VERSION}-${avatar.toLowerCase()}-${categoria.toLowerCase()}`;
        
        commands += `\n# ${avatar} - ${categoria}\n`;
        commands += `gh release create ${releaseTag} --repo ${REPO} --title "${avatar} - ${categoria}" --notes "Modelos GLB para ${avatar} en categoría ${categoria}"\n`;
        
        // Dividir en lotes de 50 archivos (límite recomendado de GitHub)
        for (let i = 0; i < files.length; i += 50) {
            const batch = files.slice(i, i + 50);
            const fileList = batch.map(f => `"${f}"`).join(' ');
            commands += `gh release upload ${releaseTag} ${fileList} --repo ${REPO}\n`;
        }
    });
    
    fs.writeFileSync('upload-to-github-releases.sh', commands);
    console.log('✅ Comandos generados: upload-to-github-releases.sh\n');
    
    console.log('🎯 SIGUIENTES PASOS:\n');
    console.log('1. Instalar GitHub CLI: https://cli.github.com/');
    console.log('2. Autenticar: gh auth login');
    console.log('3. Ejecutar: bash upload-to-github-releases.sh');
    console.log('4. Ejecutar SQL: psql -U postgres -d VeneSeñas -f database/insert_glb_models.sql\n');
}

main();
