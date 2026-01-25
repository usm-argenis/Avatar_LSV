# 🔧 Guía de Debugging - Sistema de Gestos Faciales

## 🚨 Problema Reportado

"Las expresiones no se están aplicando cuando ejecuto el test"

## 🔍 Archivos de Diagnóstico Creados

### 1. **test_rapido_gestos.html** (RECOMENDADO)
Test completo con console output visible en la página.

**Cómo usar:**
```
http://localhost:8080/test_rapido_gestos.html
```

1. Click en "▶️ INICIAR TEST COMPLETO"
2. Observa la consola en la página
3. Verifica si aparecen errores

**Qué verificar:**
- ✅ "Modelo cargado" aparece
- ✅ "Sistema de gestos inicializado"  
- ✅ "X morph targets activos" (debe ser > 0)
- ❌ Si dice "NINGÚN morph target está activado" → HAY UN PROBLEMA

### 2. **diagnostico_gestos.html**
Diagnóstico paso a paso.

**Cómo usar:**
```
http://localhost:8080/diagnostico_gestos.html
```

Ejecuta cada paso en orden:
1. Cargar Config JSON
2. Cargar Modelo Luis
3. Inicializar Sistema
4. Aplicar Expresión
5. Verificar Morph Targets

### 3. **test_facial_expressions.html** (MEJORADO)
Test interactivo con mejor logging.

**Cómo usar:**
```
http://localhost:8080/test_facial_expressions.html
```

Abre la consola del navegador (F12) y click en cualquier botón de expresión.

## 🐛 Problemas Comunes y Soluciones

### Problema 1: "Config no cargado"

**Síntomas:**
```
⚠️ Config no cargado
```

**Causa:** Archivo `facial_expressions_config.json` no se encuentra

**Solución:**
1. Verifica que el servidor esté corriendo en el directorio correcto
2. Verifica que el archivo exista:
   ```bash
   ls facial_expressions_config.json
   ```

### Problema 2: "No hay meshes con morph targets"

**Síntomas:**
```
⚠️ No hay meshes con morph targets
Inicializado con 0 meshes
```

**Causa:** El modelo no se cargó correctamente o no tiene shape keys

**Solución:**
1. Verifica que Luis.glb existe en `output/glb/Luis/Luis.glb`
2. Ejecuta el script de análisis:
   ```bash
   python analyze_glb_shapekeys.py
   ```
3. Verifica que el análisis muestre 69 shape keys

### Problema 3: "Shape key no encontrado"

**Síntomas:**
```
✗ Shape key no encontrado: browDownLeft
```

**Causa:** Nombre del shape key en config no coincide con el del modelo

**Solución:**
1. Verifica nombres exactos en `Luis_shapekeys_analysis.json`
2. Corrige nombres en `facial_expressions_config.json`

### Problema 4: "Ningún morph target tiene valor > 0"

**Síntomas:**
```
❌ NINGÚN morph target está activado
Las expresiones NO se están aplicando!
```

**Posibles causas:**

#### A. Los índices no se están mapeando correctamente

**Verificar:**
```javascript
// En consola del navegador después de cargar:
facialSystem.morphTargetIndices
// Debe mostrar objeto con ~69 propiedades
```

**Si está vacío:** El morphTargetDictionary no se está leyendo bien

**Solución:** Verificar que Three.js esté cargando correctamente el GLB

#### B. La expresión "neutral" se está aplicando sobre las otras

**Verificar en código:**
```javascript
// En facial_expression_system.js línea ~63
// Comentar temporalmente:
// this.setExpression('neutral', 0);
```

#### C. Los meshes no se están agregando al array

**Verificar:**
```javascript
// En consola:
facialSystem.meshesWithMorphTargets.length
// Debe ser 4
```

### Problema 5: Rutas incorrectas

**Síntomas:**
```
404 Not Found
```

**Causa:** Servidor corriendo en directorio incorrecto

**Solución:**
```bash
# Debe estar EN la carpeta test:
cd test
python -m http.server 8080

# O usar el batch:
INICIAR_TEST_GESTOS.bat
```

## 📋 Checklist de Verificación

Usa esta lista para diagnosticar:

```
□ Servidor corriendo en directorio test/
□ facial_expressions_config.json existe y carga
□ Luis.glb existe en output/glb/Luis/Luis.glb
□ Luis.glb tiene 69 shape keys (verificar con Python script)
□ Sistema encuentra 4 meshes con morph targets
□ morphTargetIndices tiene ~69 entradas
□ No hay errores en consola del navegador
□ Al aplicar expresión, algunos morph targets tienen valor > 0
```

## 🔬 Tests de Verificación

### Test 1: Verificar Config
```javascript
// En consola del navegador:
fetch('facial_expressions_config.json')
  .then(r => r.json())
  .then(config => {
    console.log('Expresiones:', Object.keys(config.expressions));
    console.log('Angry shape keys:', Object.keys(config.expressions.angry.morphTargets));
  });
```

**Resultado esperado:**
```
Expresiones: ['neutral', 'angry', 'happy', 'sad', ...]
Angry shape keys: ['browDownLeft', 'browDownRight', ...]
```

### Test 2: Verificar Modelo
```javascript
// Después de cargar Luis:
luisModel.traverse(child => {
  if (child.isMesh && child.morphTargetInfluences) {
    console.log(child.name, ':', child.morphTargetInfluences.length, 'targets');
    console.log('Dictionary:', child.morphTargetDictionary);
  }
});
```

**Resultado esperado:**
```
EyeLeft.001 : 69 targets
Dictionary: {mouthOpen: 0, viseme_sil: 1, ...}
```

### Test 3: Aplicar Manualmente
```javascript
// Después de cargar todo:
// Aplicar directamente a un mesh:
const mesh = facialSystem.meshesWithMorphTargets[0];
const idx = mesh.morphTargetDictionary['mouthSmile'];
mesh.morphTargetInfluences[idx] = 0.9;

// Verificar:
console.log('Valor:', mesh.morphTargetInfluences[idx]);
// Debe mostrar: 0.9
// Y deberías ver cambio visual en Luis
```

## 🎯 Solución Paso a Paso

Si nada funciona, sigue estos pasos:

### 1. Limpiar y Empezar de Nuevo

```bash
cd test

# Verificar archivos
ls facial_*.*
ls output/glb/Luis/Luis.glb

# Si falta algo, regenerar:
python analyze_glb_shapekeys.py
```

### 2. Test Mínimo

Crea `test_minimo.html`:

```html
<!DOCTYPE html>
<html>
<body>
<canvas id="c" width="800" height="600"></canvas>
<script type="module">
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.module.js';
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@0.128.0/examples/jsm/loaders/GLTFLoader.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, 800/600);
camera.position.z = 2;
const renderer = new THREE.WebGLRenderer({canvas: document.getElementById('c')});
scene.add(new THREE.AmbientLight(0xffffff, 1));

const loader = new GLTFLoader();
loader.load('output/glb/Luis/Luis.glb', (gltf) => {
  scene.add(gltf.scene);
  
  // Buscar mesh con morph targets
  gltf.scene.traverse(child => {
    if (child.isMesh && child.morphTargetDictionary) {
      console.log('✅ Mesh:', child.name);
      console.log('   Targets:', Object.keys(child.morphTargetDictionary).length);
      
      // Aplicar sonrisa
      const idx = child.morphTargetDictionary['mouthSmile'];
      if (idx !== undefined) {
        child.morphTargetInfluences[idx] = 1.0;
        console.log('✅ mouthSmile aplicado:', child.morphTargetInfluences[idx]);
      }
    }
  });
  
  function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
  }
  animate();
});
</script>
</body>
</html>
```

Abre y verifica que Luis sonríe.

### 3. Si el Test Mínimo Funciona

El problema está en `facial_expression_system.js`. Verifica:

1. `morphTargetIndices` se está llenando correctamente
2. `applyExpression` está usando los índices correctos
3. No hay código que resetee los valores

### 4. Si el Test Mínimo NO Funciona

El problema está en el modelo GLB:

1. Verifica que el GLB tenga shape keys:
   ```bash
   python analyze_glb_shapekeys.py
   ```
2. Si no hay shape keys, el GLB necesita ser regenerado con shape keys

## 📞 Soporte Adicional

Si después de todos estos pasos aún no funciona:

1. **Captura de pantalla** de la consola con errores
2. **Output** del script Python de análisis
3. **Versión** de Three.js (debería ser r128)
4. **Navegador** y versión

## ✅ Confirmación de Funcionamiento

El sistema está funcionando correctamente cuando:

1. ✅ Console muestra: "✅ Aplicados X shape keys en 4 meshes" (X > 0)
2. ✅ Al verificar: "X morph targets activos"
3. ✅ **Visualmente**: La cara de Luis cambia (cejas, boca, ojos)

## 🎯 Mejoras Implementadas

Para ayudar con el debugging, he agregado:

1. **Logging mejorado**: Ahora muestra exactamente qué shape keys se aplican
2. **Validaciones**: Warns si config no carga o meshes no se encuentran
3. **Tests múltiples**: 3 archivos HTML diferentes para probar
4. **Verificación automática**: Muestra si hay valores activos

## 📝 Próximos Pasos

Una vez que funcione:

1. Probar con animation.html integrado
2. Probar diferentes expresiones
3. Verificar transiciones suaves
4. Probar con otros avatares (Nancy, Duvall, Nina)
