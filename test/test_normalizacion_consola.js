// Test automatizado de normalización de tildes para animation_mobile.html
// Ejecutar este código en la consola del navegador

console.log('🧪 Iniciando tests de normalización...\n');

// Test 1: Función normalizarPalabra
console.log('📝 Test 1: Función normalizarPalabra');
const tests1 = [
    { input: 'buenos días', expected: 'buenos dias' },
    { input: 'adiós', expected: 'adios' },
    { input: 'José', expected: 'jose' },
    { input: 'María', expected: 'maria' },
    { input: 'cómo estás', expected: 'como estas' }
];

let passed1 = 0;
tests1.forEach(test => {
    const result = normalizarPalabra(test.input);
    const ok = result === test.expected;
    console.log(`  ${ok ? '✅' : '❌'} "${test.input}" → "${result}" ${ok ? '' : `(esperado: "${test.expected}")`}`);
    if (ok) passed1++;
});
console.log(`  Resultado: ${passed1}/${tests1.length} tests pasados\n`);

// Test 2: Búsqueda en diccionario
console.log('📚 Test 2: Búsqueda en diccionario');
const tests2 = [
    { input: 'buenos dias', shouldExist: true },
    { input: 'adios', shouldExist: true },
    { input: 'hola', shouldExist: true },
    { input: 'gracias', shouldExist: true }
];

let passed2 = 0;
tests2.forEach(test => {
    const normalized = normalizarPalabra(test.input);
    const exists = DICCIONARIO[normalized] !== undefined;
    const ok = exists === test.shouldExist;
    console.log(`  ${ok ? '✅' : '❌'} "${test.input}" → normalizado: "${normalized}" → ${exists ? 'EXISTE' : 'NO EXISTE'} ${ok ? '' : '(ERROR)'}`);
    if (ok) passed2++;
});
console.log(`  Resultado: ${passed2}/${tests2.length} tests pasados\n`);

// Test 3: Normalización de letras individuales
console.log('🔤 Test 3: Normalización de letras con tildes');
const tests3 = [
    { input: 'á', expected: 'a' },
    { input: 'é', expected: 'e' },
    { input: 'í', expected: 'i' },
    { input: 'ó', expected: 'o' },
    { input: 'ú', expected: 'u' }
];

let passed3 = 0;
tests3.forEach(test => {
    const normalized = test.input.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    const ok = normalized === test.expected;
    const existsInDict = DICCIONARIO[normalized] !== undefined;
    console.log(`  ${ok ? '✅' : '❌'} "${test.input}" → "${normalized}" ${ok ? '' : `(esperado: "${test.expected}")`} - En dict: ${existsInDict ? 'Sí' : 'No'}`);
    if (ok) passed3++;
});
console.log(`  Resultado: ${passed3}/${tests3.length} tests pasados\n`);

// Test 4: Frases completas con tildes
console.log('💬 Test 4: Frases completas con tildes');
const tests4 = [
    'buenos días',
    'adiós',
    'cómo estás',
    'José María'
];

tests4.forEach(frase => {
    const normalized = normalizarPalabra(frase);
    const exists = DICCIONARIO[normalized] !== undefined;
    console.log(`  📝 "${frase}" → "${normalized}" → ${exists ? '✅ EXISTE' : '⚠️ NO EXISTE (se deletreará)'}`);
});

// Resumen final
const totalTests = tests1.length + tests2.length + tests3.length;
const totalPassed = passed1 + passed2 + passed3;
console.log('\n' + '='.repeat(50));
console.log(`📊 RESUMEN FINAL: ${totalPassed}/${totalTests} tests pasados`);
if (totalPassed === totalTests) {
    console.log('✅ TODOS LOS TESTS PASARON CORRECTAMENTE');
    console.log('🎉 La normalización de tildes funciona al 100%');
} else {
    console.log(`❌ ${totalTests - totalPassed} tests fallaron`);
    console.log('⚠️ Revisar la implementación');
}
console.log('='.repeat(50));
