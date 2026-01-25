# 🎯 Guía de Uso: Selector de Avatares en el Visualizador

## ✨ Nueva Funcionalidad Implementada

El visualizador ahora tiene **2 selectores independientes**:

### 👤 Selector de Avatar
- **Ubicación**: Panel superior derecho
- **Función**: Cambiar entre diferentes avatares de Mixamo
- **Avatares disponibles**:
  - Remy
  - JH

### 🤟 Selector de Seña
- **Ubicación**: Panel superior derecho (debajo del selector de avatar)
- **Función**: Seleccionar la seña que quieres visualizar
- **Señas disponibles**:
  - Letra B

---

## 🚀 Cómo Usar

### Opción 1: Cambiar Avatar con la Misma Seña
```
1. Abre el visualizador en: http://localhost:8000/test/viewer_senas_v2.html
2. Selecciona un avatar del selector "👤 Avatar"
3. La animación se cargará automáticamente
4. Presiona ▶️ para reproducir
```

**Ejemplo:**
- Avatar: Remy → Seña: Letra B
- Avatar: JH → Seña: Letra B
- **Resultado**: Ambos hacen la misma seña pero con diferentes apariencias

---

### Opción 2: Cambiar Seña con el Mismo Avatar
```
1. Mantén seleccionado tu avatar favorito
2. Selecciona una seña diferente del selector "🤟 Seña"
3. La nueva animación se cargará automáticamente
```

**Ejemplo:**
- Avatar: Remy → Seña: Letra B
- Avatar: Remy → Seña: Letra C (cuando esté disponible)
- **Resultado**: El mismo avatar haciendo diferentes señas

---

## 🎨 Características del Selector

### Diseño Visual:
- **Avatar selector**: Borde azul (`#4fc3f7`)
- **Seña selector**: Borde rosa (`#f093fb`)
- **Hover effect**: Escala 1.02x con sombra brillante
- **Focus effect**: Sombra más intensa al hacer clic

### Información Mostrada:
- **Panel Info**: Muestra "Avatar - Seña" (ej: "Remy - Letra B")
- **Carga automática**: Al cambiar selector, se carga inmediatamente
- **Estado visual**: Indicador de carga mientras procesa

---

## 📂 Estructura de Archivos

El sistema busca archivos con el formato:
```
output/{Avatar}_{Seña}.fbx
```

**Ejemplos:**
- `output/Remy_b_deepmotion.fbx` ✅
- `output/JH_b_deepmotion.fbx` ✅
- `output/Remy_resultado_b.fbx` ✅ (archivo legacy)

---

## ➕ Agregar Más Avatares

### Paso 1: Descargar Avatar de Mixamo
```
1. Ir a https://www.mixamo.com
2. Seleccionar avatar (ej: Amy, Josh, Malcolm)
3. Download → FBX for Unity
4. Guardar en: avatars/Amy.fbx
```

### Paso 2: Procesar con la Animación
```powershell
blender --background --python scripts\apply_animation_to_avatars.py -- "animations_library\alphabet\b_deepmotion.fbx"
```

### Paso 3: Actualizar HTML
```html
<!-- En viewer_senas_v2.html, agregar opción: -->
<select id="avatar-select">
    <option value="Remy">Remy</option>
    <option value="JH">JH</option>
    <option value="Amy">Amy</option>  <!-- NUEVO -->
</select>
```

### Paso 4: Recargar Navegador
```
F5 o Ctrl+R
```

---

## ➕ Agregar Más Señas

### Paso 1: Generar en DeepMotion (1 crédito)
```
1. Subir video de la seña
2. Procesar en DeepMotion
3. Descargar: resultado_c.fbx (por ejemplo)
```

### Paso 2: Guardar en Biblioteca
```powershell
Copy-Item "Downloads\resultado_c.fbx" "animations_library\alphabet\c_deepmotion.fbx"
```

### Paso 3: Procesar con Todos los Avatares
```powershell
blender --background --python scripts\apply_animation_to_avatars.py -- "animations_library\alphabet\c_deepmotion.fbx"
```

### Paso 4: Actualizar HTML
```html
<!-- En viewer_senas_v2.html, agregar opción: -->
<select id="sign-select">
    <option value="b_deepmotion">Letra B</option>
    <option value="c_deepmotion">Letra C</option>  <!-- NUEVO -->
</select>
```

---

## 🎯 Ejemplo Completo: Sistema con 3 Avatares y 3 Señas

### Configuración:
```
Avatares: Remy, JH, Amy
Señas: B, C, D
```

### Archivos Generados (9 combinaciones):
```
output/
├── Remy_b_deepmotion.fbx
├── Remy_c_deepmotion.fbx
├── Remy_d_deepmotion.fbx
├── JH_b_deepmotion.fbx
├── JH_c_deepmotion.fbx
├── JH_d_deepmotion.fbx
├── Amy_b_deepmotion.fbx
├── Amy_c_deepmotion.fbx
└── Amy_d_deepmotion.fbx
```

### Créditos Gastados:
- **Sin optimización**: 9 créditos (1 por cada combinación)
- **Con optimización**: 3 créditos (1 por seña)
- **AHORRO**: 6 créditos (66%)

---

## 🎨 Personalización del Selector

### Cambiar Colores:
```css
/* Avatar selector - Azul */
#avatar-select {
    border: 2px solid #4fc3f7; /* Cambiar este color */
}

/* Seña selector - Rosa */
#sign-select {
    border: 2px solid #f093fb; /* Cambiar este color */
}
```

### Agregar Iconos:
```html
<option value="Remy">👨 Remy</option>
<option value="JH">🧑 JH</option>
<option value="b_deepmotion">🅱️ Letra B</option>
```

---

## 🐛 Solución de Problemas

### Error: "No se puede cargar FBX"

**Causa**: Archivo no existe con la combinación avatar + seña

**Solución**:
```powershell
# Verificar archivos disponibles
Get-ChildItem output\*.fbx

# Si falta, procesar:
blender --background --python scripts\apply_animation_to_avatars.py -- "animations_library\alphabet\[letra]_deepmotion.fbx"
```

### El selector no muestra opciones

**Causa**: HTML no actualizado

**Solución**:
```html
<!-- Verificar que los <option> existan en el HTML -->
<select id="avatar-select">
    <option value="Remy">Remy</option>
    <option value="JH">JH</option>
</select>
```

### Cambio de selector no carga nueva animación

**Causa**: Error en la ruta del archivo

**Solución**:
```javascript
// Abrir consola del navegador (F12)
// Ver si hay errores de carga
// Verificar formato: output/{Avatar}_{Seña}.fbx
```

---

## 📊 Estado Actual del Sistema

```
🚀 LSV SYSTEM - QUICK STATUS
============================================================
📚 Animaciones en biblioteca: 1/50 (2%)
👤 Avatares disponibles:      2 (Remy, JH)
📤 Archivos procesados:       3
💰 Créditos gastados:         ~1
💸 Créditos necesarios:       ~49
🎯 Combinaciones posibles:    2 avatares × 1 seña = 2
📊 Eficiencia:                150% (3/2 archivos)
============================================================
✅ Sistema operativo
```

---

## 🎓 Mejores Prácticas

### ✅ HACER:
1. Generar animación UNA vez en DeepMotion
2. Procesar con TODOS los avatares localmente
3. Agregar opciones al HTML para cada nueva combinación
4. Verificar archivos antes de actualizar selectores
5. Usar nomenclatura consistente: `{Avatar}_{Seña}.fbx`

### ❌ EVITAR:
1. Generar misma seña múltiples veces en DeepMotion
2. Olvidar procesar nuevos avatares con señas existentes
3. Usar nombres de archivo inconsistentes
4. No verificar rutas en buildFBXPath()

---

## 🚀 Próximos Pasos Recomendados

1. **Descargar más avatares**:
   - Amy, Josh, Malcolm, Claire de Mixamo
   - Procesar con letra B existente

2. **Generar más señas**:
   - Letras frecuentes: E, A, O, S, R
   - Procesar con todos los avatares

3. **Actualizar selectores HTML**:
   - Agregar nuevos avatares al `#avatar-select`
   - Agregar nuevas señas al `#sign-select`

4. **Automatizar actualización**:
   - Crear script que genere opciones automáticamente
   - Escanear carpeta `output/` y crear HTML dinámico

---

## 💡 Comando Rápido de Referencia

```powershell
# Ver estado
python scripts\quick_status.py

# Procesar avatar con seña
blender --background --python scripts\apply_animation_to_avatars.py -- "animations_library\alphabet\b_deepmotion.fbx"

# Ver archivos generados
Get-ChildItem output\*.fbx

# Iniciar visualizador
python -m http.server 8000
# → http://localhost:8000/test/viewer_senas_v2.html
```

---

**Última actualización**: Octubre 22, 2025
**Versión**: 3.0 - Selector de Avatares Múltiples
