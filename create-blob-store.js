#!/usr/bin/env node

/**
 * Script para crear Blob Store desde CLI
 */

const { execSync } = require('child_process');

console.log('🔧 Creando Blob Store en Vercel...\n');

try {
  // Crear blob store usando la API de Vercel
  console.log('Ejecutando: vercel env pull');
  execSync('vercel env pull', { stdio: 'inherit' });
  
  console.log('\n✅ Configuración lista');
  console.log('\nAhora ve a: https://vercel.com/dashboard');
  console.log('Y busca tu proyecto "tesis" para crear el Blob Store');
  
} catch (error) {
  console.error('❌ Error:', error.message);
  console.log('\n📝 Instrucciones manuales:');
  console.log('1. Ve a https://vercel.com/dashboard');
  console.log('2. Click en tu proyecto "tesis"');
  console.log('3. Busca la pestaña "Storage" en el menú superior');
  console.log('4. Click "Create" → Selecciona "Blob"');
}
