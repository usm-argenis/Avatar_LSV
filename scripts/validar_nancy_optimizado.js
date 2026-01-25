/**
 * Script de Validación para Nancy Optimizado
 * Uso: node scripts/validar_nancy_optimizado.js
 * 
 * Verifica:
 * - Estructura del GLB
 * - Animaciones disponibles
 * - Tamaño del archivo
 * - Compatibilidad con Three.js
 */

const fs = require('fs');
const path = require('path');

// ====================================
// CONFIGURACIÓN
// ====================================

const NANCY_OPTIMIZADO_PATH = path.join(__dirname, '..', 'test', 'output', 'glb', 'Nancy_optimizado.glb');
const MAX_FILE_SIZE_MB = 20; // Tamaño máximo recomendado
const EXPECTED_ANIMATIONS = [
    // Saludos
    'saludos_hola',
    'saludos_chao',
    'saludos_buenos_dias',
    'saludos_buenas_tardes',
    'saludos_buenas_noches',
    'saludos_bienvenido',
    'saludos_adios',
    
    // Tiempo
    'tiempo_ayer',
    'tiempo_hoy',
    'tiempo_manana',
    'tiempo_semana',
    'tiempo_mes',
    
    // Días de la semana
    'dias_semana_lunes',
    'dias_semana_martes',
    'dias_semana_miercoles',
    
    // Pronombres
    'pronombres_yo',
    'pronombres_tu',
    'pronombres_el',
    
    // Expresiones
    'expresiones_gracias',
    'expresiones_por_favor',
    
    // Cortesía
    'cortesia_a_la_orden',
];

// ====================================
// FUNCIONES DE VALIDACIÓN
// ====================================

function validarExistenciaArchivo() {
    console.log('📁 Verificando existencia del archivo...');
    
    if (!fs.existsSync(NANCY_OPTIMIZADO_PATH)) {
        console.error(`❌ ERROR: No se encuentra el archivo: ${NANCY_OPTIMIZADO_PATH}`);
        console.log('   Ejecuta primero el script de Blender para generar Nancy_optimizado.glb');
        return false;
    }
    
    console.log('✅ Archivo encontrado');
    return true;
}

function validarTamanoArchivo() {
    console.log('\n📊 Verificando tamaño del archivo...');
    
    const stats = fs.statSync(NANCY_OPTIMIZADO_PATH);
    const fileSizeMB = stats.size / (1024 * 1024);
    
    console.log(`   Tamaño: ${fileSizeMB.toFixed(2)} MB`);
    
    if (fileSizeMB > MAX_FILE_SIZE_MB) {
        console.warn(`⚠️  ADVERTENCIA: Archivo muy grande (> ${MAX_FILE_SIZE_MB} MB)`);
        console.log('   Considera optimizar texturas o comprimir animaciones');
        return false;
    }
    
    console.log(`✅ Tamaño óptimo (< ${MAX_FILE_SIZE_MB} MB)`);
    return true;
}

function validarEstructuraGLB() {
    console.log('\n🔍 Verificando estructura GLB...');
    
    try {
        const buffer = fs.readFileSync(NANCY_OPTIMIZADO_PATH);
        
        // Verificar magic number de GLB (0x46546C67 = "glTF")
        const magic = buffer.readUInt32LE(0);
        if (magic !== 0x46546C67) {
            console.error('❌ ERROR: No es un archivo GLB válido (magic number incorrecto)');
            return false;
        }
        
        // Verificar versión
        const version = buffer.readUInt32LE(4);
        console.log(`   Versión GLB: ${version}`);
        
        if (version !== 2) {
            console.warn('⚠️  ADVERTENCIA: Versión GLB diferente a 2.0');
        }
        
        // Tamaño total
        const length = buffer.readUInt32LE(8);
        console.log(`   Tamaño declarado: ${(length / 1024 / 1024).toFixed(2)} MB`);
        
        console.log('✅ Estructura GLB válida');
        return true;
        
    } catch (error) {
        console.error(`❌ ERROR al leer archivo: ${error.message}`);
        return false;
    }
}

function generarReporteDetallado() {
    console.log('\n' + '='.repeat(60));
    console.log('📋 REPORTE DETALLADO DE VALIDACIÓN');
    console.log('='.repeat(60));
    
    console.log('\n📦 Información del Archivo:');
    console.log(`   Ruta: ${NANCY_OPTIMIZADO_PATH}`);
    
    const stats = fs.statSync(NANCY_OPTIMIZADO_PATH);
    console.log(`   Tamaño: ${(stats.size / 1024 / 1024).toFixed(2)} MB`);
    console.log(`   Fecha: ${stats.mtime.toLocaleString()}`);
    
    console.log('\n📋 Animaciones Esperadas:');
    console.log(`   Total: ${EXPECTED_ANIMATIONS.length} animaciones`);
    
    const categorias = {};
    EXPECTED_ANIMATIONS.forEach(anim => {
        const categoria = anim.split('_')[0];
        if (!categorias[categoria]) {
            categorias[categoria] = [];
        }
        categorias[categoria].push(anim);
    });
    
    for (const [cat, anims] of Object.entries(categorias)) {
        console.log(`\n   📁 ${cat.toUpperCase()}: ${anims.length} animaciones`);
        anims.forEach(a => console.log(`      - ${a}`));
    }
    
    console.log('\n💡 Próximos Pasos:');
    console.log('   1. Abrir Nancy_optimizado.glb en Blender');
    console.log('   2. Verificar animaciones en Action Editor');
    console.log('   3. Probar en prueba.html');
    console.log('   4. Integrar en React Native');
    
    console.log('\n' + '='.repeat(60));
}

function mostrarInstruccionesBlender() {
    console.log('\n📘 Instrucciones para Verificar en Blender:');
    console.log('   1. Abrir Blender');
    console.log('   2. File > Import > glTF 2.0 (.glb/.gltf)');
    console.log(`   3. Seleccionar: ${path.basename(NANCY_OPTIMIZADO_PATH)}`);
    console.log('   4. Seleccionar el Armature');
    console.log('   5. Cambiar editor a "Action Editor"');
    console.log('   6. En el dropdown ver lista de animaciones');
    console.log('   7. Presionar ESPACIO para probar cada animación\n');
}

function mostrarInstruccionesThreeJS() {
    console.log('📘 Código de Ejemplo para Three.js:');
    console.log(`
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import * as THREE from 'three';

// Cargar Nancy optimizado
const loader = new GLTFLoader();
loader.load('${path.basename(NANCY_OPTIMIZADO_PATH)}', (gltf) => {
    const nancy = gltf.scene;
    const animations = gltf.animations;
    
    console.log('✅ Nancy cargada');
    console.log('📋 Animaciones disponibles:', animations.length);
    
    animations.forEach((clip, index) => {
        console.log(\`   \${index + 1}. \${clip.name} - \${clip.duration.toFixed(2)}s\`);
    });
    
    // Crear mixer para reproducir animaciones
    const mixer = new THREE.AnimationMixer(nancy);
    
    // Reproducir animación específica
    const hola = animations.find(a => a.name === 'saludos_hola');
    if (hola) {
        const action = mixer.clipAction(hola);
        action.play();
    }
    
    // Actualizar en el loop de animación
    function animate() {
        requestAnimationFrame(animate);
        mixer.update(clock.getDelta());
        renderer.render(scene, camera);
    }
});
`);
}

function mostrarInstruccionesReactNative() {
    console.log('📘 Código de Ejemplo para React Native (Expo):');
    console.log(`
import { Asset } from 'expo-asset';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';

// En tu componente
const loadNancy = async () => {
    const asset = Asset.fromModule(require('./assets/Nancy_optimizado.glb'));
    await asset.downloadAsync();
    
    const loader = new GLTFLoader();
    loader.load(asset.localUri, (gltf) => {
        const nancy = gltf.scene;
        const animations = gltf.animations;
        
        console.log('✅ Nancy cargada:', animations.length, 'animaciones');
        
        // Configurar mixer
        const mixer = new THREE.AnimationMixer(nancy);
        setAnimationMixer(mixer);
        setAvailableAnimations(animations);
        
        // Añadir a la escena
        scene.add(nancy);
    });
};

// Cambiar animación
const playAnimation = (animationName) => {
    const clip = availableAnimations.find(a => a.name === animationName);
    if (clip && animationMixer) {
        // Detener animación actual
        animationMixer.stopAllAction();
        
        // Reproducir nueva animación
        const action = animationMixer.clipAction(clip);
        action.reset();
        action.play();
    }
};

// Uso
playAnimation('saludos_hola');
playAnimation('expresiones_gracias');
`);
}

// ====================================
// EJECUCIÓN PRINCIPAL
// ====================================

function main() {
    console.log('\n' + '='.repeat(60));
    console.log('🔍 VALIDADOR DE NANCY OPTIMIZADO');
    console.log('='.repeat(60) + '\n');
    
    let todoBien = true;
    
    // Validación 1: Existencia
    if (!validarExistenciaArchivo()) {
        console.log('\n❌ Validación fallida: Archivo no existe\n');
        return;
    }
    
    // Validación 2: Tamaño
    if (!validarTamanoArchivo()) {
        todoBien = false;
    }
    
    // Validación 3: Estructura
    if (!validarEstructuraGLB()) {
        todoBien = false;
    }
    
    // Reporte
    generarReporteDetallado();
    
    // Instrucciones
    mostrarInstruccionesBlender();
    mostrarInstruccionesThreeJS();
    mostrarInstruccionesReactNative();
    
    // Resultado final
    if (todoBien) {
        console.log('\n✅ VALIDACIÓN EXITOSA - Nancy_optimizado.glb está listo para usar\n');
    } else {
        console.log('\n⚠️  VALIDACIÓN CON ADVERTENCIAS - Revisar mensajes arriba\n');
    }
}

// Ejecutar
if (require.main === module) {
    main();
}

module.exports = {
    validarExistenciaArchivo,
    validarTamanoArchivo,
    validarEstructuraGLB
};
