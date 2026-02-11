/**
 * Test completo End-to-End: Translator + Loader + HTTP Server
 * 
 * Simula el flujo completo de la app móvil para verificar que:
 * 1. El Translator convierte palabras correctamente (ej: "miembro" → "miembros")
 * 2. El Loader construye las rutas correctas
 * 3. El servidor HTTP sirve los archivos GLB correctamente
 */

const https = require('https');
const http = require('http');

// ========== CONFIGURACIÓN ==========
const SERVER_URL = 'http://10.171.95.217:8000';

// ========== SIMULACIÓN DEL TRANSLATOR ==========
const translatorDictionary = new Map([
    ['miembro', 'miembros'],
    ['miembros', 'miembros'],
    ['traduccion', 'traduccion'],
    ['hola', 'hola'],
    ['gracias', 'gracias']
]);

function translate(word) {
    const normalized = word.toLowerCase().trim();
    return translatorDictionary.get(normalized) || normalized;
}

// ========== SIMULACIÓN DEL LOADER ==========
const ANIMATION_CATEGORIES = {
    'miembros': 'frase',
    'traduccion': 'frase',
    'hola': 'saludos',
    'gracias': 'expresiones'
};

const AVATAR_PATHS = {
    'Carla': {
        animations: {
            frase: 'output/glb/Carla/frase/',
            expresiones: 'output/glb/Carla/expresiones/',
            saludos: 'output/glb/Carla/saludos/'
        }
    },
    'Luis': {
        animations: {
            frase: 'output/glb/Luis/frase/',
            expresiones: 'output/glb/Luis/expresiones/',
            saludos: 'output/glb/Luis/saludos/'
        }
    }
};

function buildAnimationPath(avatarName, animName) {
    const config = AVATAR_PATHS[avatarName];
    if (!config) return null;

    const fileName = animName.toLowerCase();
    const category = ANIMATION_CATEGORIES[fileName];
    
    if (category && config.animations[category]) {
        const categoryPath = config.animations[category];
        const fullPath = `${SERVER_URL}/${categoryPath}${avatarName}_resultado_${fileName}.glb`;
        return fullPath;
    }
    
    return null;
}

// ========== TEST DE ACCESO HTTP ==========
function checkHTTP(url) {
    return new Promise((resolve) => {
        const urlObj = new URL(url);
        const client = urlObj.protocol === 'https:' ? https : http;
        
        const req = client.get(url, (res) => {
            resolve(res.statusCode);
        });
        
        req.on('error', () => {
            resolve(0);
        });
        
        req.setTimeout(3000, () => {
            req.destroy();
            resolve(0);
        });
    });
}

// ========== EJECUTAR TESTS ==========
async function runTests() {
    console.log('🧪 TEST END-TO-END: Translator → Loader → HTTP\n');
    console.log('='.repeat(70));
    
    const testCases = [
        { avatar: 'Carla', userInput: 'miembro', description: 'Carla - palabra singular "miembro"' },
        { avatar: 'Carla', userInput: 'miembros', description: 'Carla - palabra plural "miembros"' },
        { avatar: 'Carla', userInput: 'traduccion', description: 'Carla - palabra "traduccion"' },
        { avatar: 'Luis', userInput: 'miembro', description: 'Luis - palabra singular "miembro"' },
        { avatar: 'Luis', userInput: 'miembros', description: 'Luis - palabra plural "miembros"' },
        { avatar: 'Luis', userInput: 'traduccion', description: 'Luis - palabra "traduccion"' }
    ];
    
    let passed = 0;
    let failed = 0;
    
    for (let i = 0; i < testCases.length; i++) {
        const test = testCases[i];
        console.log(`\n📝 Test ${i + 1}/${testCases.length}: ${test.description}`);
        console.log('-'.repeat(70));
        
        // PASO 1: Translator
        const translatedWord = translate(test.userInput);
        console.log(`  1️⃣  Usuario escribe: "${test.userInput}"`);
        console.log(`      Translator convierte a: "${translatedWord}"`);
        
        // PASO 2: Loader
        const glbPath = buildAnimationPath(test.avatar, translatedWord);
        console.log(`  2️⃣  Loader construye ruta:`);
        console.log(`      ${glbPath}`);
        
        // PASO 3: HTTP
        if (glbPath) {
            console.log(`  3️⃣  Verificando acceso HTTP...`);
            const statusCode = await checkHTTP(glbPath);
            console.log(`      HTTP Status: ${statusCode}`);
            
            if (statusCode === 200) {
                console.log(`  ✅ PASS - Todo funciona correctamente`);
                passed++;
            } else {
                console.log(`  ❌ FAIL - Archivo no accesible (HTTP ${statusCode})`);
                failed++;
            }
        } else {
            console.log(`  ❌ FAIL - No se pudo construir ruta`);
            failed++;
        }
    }
    
    console.log('\n' + '='.repeat(70));
    console.log(`\n📊 RESULTADOS FINALES:`);
    console.log(`   ✅ Pasados: ${passed}/${testCases.length}`);
    console.log(`   ❌ Fallidos: ${failed}/${testCases.length}`);
    
    if (failed === 0) {
        console.log('\n🎉 ¡ÉXITO! Todos los tests pasaron.');
        console.log('✨ La aplicación React Native debería funcionar correctamente.\n');
        process.exit(0);
    } else {
        console.log('\n⚠️  ATENCIÓN: Algunos tests fallaron.');
        console.log('🔍 Revisa los errores arriba para más detalles.\n');
        process.exit(1);
    }
}

// Ejecutar
runTests().catch(error => {
    console.error('❌ Error ejecutando tests:', error);
    process.exit(1);
});
