#!/usr/bin/env node

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const REPO = 'usm-argenis/Avatar_LSV';
const REL_TAG = 'models-v1';
const BASE = path.join(__dirname, 'test', 'output', 'glb');
const GH = '"C:\\Program Files\\GitHub CLI\\gh.exe"';

console.log('\n┌──────────────────────────────────────┐');
console.log('│  Subida de GLB a GitHub Releases     │');
console.log('│  Avatares: Duvall y Carla            │');
console.log('└──────────────────────────────────────┘\n');

// Función helper para ejecutar comandos
function exec(cmd) {
    return new Promise((resolve, reject) => {
        const proc = spawn('cmd.exe', ['/c', cmd]);
        let output = '';
        
        proc.stdout.on('data', (data) => {
            output += data.toString();
        });
        
        proc.stderr.on('data', (data) => {
            output += data.toString();
        });
        
        proc.on('close', (code) => {
            if (code === 0) resolve(output);
            else reject(new Error(output));
        });
    });
}

async function main() {
    let uploaded = 0;
    let errors = 0;
    
    // Crear release
    console.log('📦 Creando release...');
    try {
        await exec(`${GH} release create ${REL_TAG} --repo ${REPO} --title "Modelos - Duvall y Carla" --notes "GLB files"`);
        console.log('✅ Release creado\n');
    } catch (e) {
        console.log('⚠️  Release existe\n');
    }
    
    // Subir por avatar
    for (const avatar of ['Duvall', 'Carla']) {
        const avatarDir = path.join(BASE, avatar);
        if (!fs.existsSync(avatarDir)) continue;
        
        console.log(`\n👤 ${avatar}`);
        console.log('─'.repeat(40));
        
        // Obtener categorías
        const cats = fs.readdirSync(avatarDir).filter(f => 
            fs.statSync(path.join(avatarDir, f)).isDirectory()
        );
        
        for (let i = 0; i < cats.length; i++) {
            const cat = cats[i];
            const catDir = path.join(avatarDir, cat);
            const files = fs.readdirSync(catDir).filter(f => f.endsWith('.glb'));
            
            if (files.length === 0) continue;
            
            process.stdout.write(`  [${i+1}/${cats.length}] ${cat.padEnd(25)} ${files.length.toString().padStart(3)}  archivos... `);
            
            // Subir en lotes de 10
            for (let j = 0; j < files.length; j += 10) {
                const batch = files.slice(j, j + 10);
                const paths = batch.map(f => `"${path.join(catDir, f)}"`).join(' ');
                
                try {
                    await exec(`${GH} release upload ${REL_TAG} ${paths} --repo ${REPO} --clobber`);
                    uploaded += batch.length;
                } catch (e) {
                    errors += batch.length;
                }
            }
            
            console.log('✅');
        }
        
        // Archivo base
        const base = path.join(avatarDir, `${avatar}.glb`);
        if (fs.existsSync(base)) {
            process.stdout.write(`  Archivo base... `);
            try {
                await exec(`${GH} release upload ${REL_TAG} "${base}" --repo ${REPO} --clobber`);
                uploaded++;
                console.log('✅');
            } catch (e) {
                errors++;
                console.log('❌');
            }
        }
    }
    
    // Resumen
    console.log('\n' + '═'.repeat(40));
    console.log(`✅ Subidos: ${uploaded}`);
    console.log(`❌ Errores: ${errors}`);
    console.log(`🔗 https://github.com/${REPO}/releases/tag/${REL_TAG}`);
    console.log('═'.repeat(40) + '\n');
}

main().catch(err => {
    console.error('\n❌ Error:', err.message);
    process.exit(1);
});
