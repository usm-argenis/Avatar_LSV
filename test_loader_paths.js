/**
 * Script de prueba para validar que el loader construye rutas correctamente
 */

const fs = require('fs');
const path = require('path');

// Configuración local (simulando loader.js)
const AVATAR_PATHS = {
    Carla: {
        animations: {
            frase: 'test/output/glb/Carla/frase/',
            expresiones: 'test/output/glb/Carla/expresiones/',
            saludos: 'test/output/glb/Carla/saludos/',
        }
    },
    Luis: {
        animations: {
            frase: 'test/output/glb/Luis/frase/',
            expresiones: 'test/output/glb/Luis/expresiones/',
            saludos: 'test/output/glb/Luis/saludos/',
        }
    }
};

const ANIMATION_CATEGORIES = {
    'miembro': 'frase',
    'miembros': 'frase',
    'traduccion': 'frase',
    'hola': 'saludos',
    'gracias': 'expresiones'
};

/**
 * Simula _buildAnimationPath
 */
function buildAnimationPath(avatarName, animName) {
    const config = AVATAR_PATHS[avatarName];
    if (!config) {
        console.error(`❌ Avatar "${avatarName}" no existe`);
        return null;
    }

    const fileName = animName.toLowerCase();
    const category = ANIMATION_CATEGORIES[fileName];
    
    if (category && config.animations[category]) {
        const fileNameWithSpaces = fileName.replace(/_/g, ' ');
        const categoryPath = config.animations[category];
        const fullPath = `${categoryPath}${avatarName}_resultado_${fileNameWithSpaces}.glb`;
        return fullPath;
    }
    
    // Fallback
    console.warn(`⚠️ "${animName}" no está en mapeo, usando fallback`);
    const fileNameWithSpaces = fileName.replace(/_/g, ' ');
    
    for (const categoryName of ['frase', 'expresiones', 'saludos']) {
        const categoryPath = config.animations[categoryName];
        if (categoryPath) {
            const fullPath = `${categoryPath}${avatarName}_resultado_${fileNameWithSpaces}.glb`;
            return fullPath;
        }
    }
    
    return null;
}

/**
 * Verificar si un archivo existe
 */
function fileExists(filePath) {
    try {
        return fs.existsSync(filePath);
    } catch (e) {
        return false;
    }
}

/**
 * Ejecutar pruebas
 */
console.log('🧪 PRUEBAS DE CONSTRUCCIÓN DE RUTAS\n');
console.log('=' .repeat(60));

const testCases = [
    { avatar: 'Carla', word: 'miembros', expected: 'test/output/glb/Carla/frase/Carla_resultado_miembros.glb' },
    { avatar: 'Carla', word: 'miembro', expected: 'test/output/glb/Carla/frase/Carla_resultado_miembros.glb' },
    { avatar: 'Carla', word: 'traduccion', expected: 'test/output/glb/Carla/frase/Carla_resultado_traduccion.glb' },
    { avatar: 'Luis', word: 'miembros', expected: 'test/output/glb/Luis/frase/Luis_resultado_miembros.glb' },
    { avatar: 'Luis', word: 'traduccion', expected: 'test/output/glb/Luis/frase/Luis_resultado_traduccion.glb' },
];

let passed = 0;
let failed = 0;

testCases.forEach((test, index) => {
    console.log(`\nTest ${index + 1}: ${test.avatar} - "${test.word}"`);
    
    const result = buildAnimationPath(test.avatar, test.word);
    const exists = result ? fileExists(result) : false;
    
    console.log(`  Ruta generada: ${result}`);
    console.log(`  Ruta esperada: ${test.expected}`);
    console.log(`  ¿Coincide?: ${result === test.expected ? '✅ SÍ' : '❌ NO'}`);
    console.log(`  ¿Archivo existe?: ${exists ? '✅ SÍ' : '❌ NO'}`);
    
    if (result === test.expected && exists) {
        console.log(`  ✅ PASS`);
        passed++;
    } else {
        console.log(`  ❌ FAIL`);
        failed++;
    }
});

console.log('\n' + '='.repeat(60));
console.log(`\n📊 RESULTADOS: ${passed} passed, ${failed} failed`);

if (failed === 0) {
    console.log('\n🎉 ¡Todas las pruebas pasaron!');
    process.exit(0);
} else {
    console.log('\n⚠️ Algunas pruebas fallaron');
    process.exit(1);
}
