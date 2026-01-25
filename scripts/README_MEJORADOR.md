# 🔧 Mejorador de Animaciones DeepMotion

## 🎯 Problema que Resuelve

Cuando exportas animaciones desde DeepMotion, a veces:
- ❌ Los dedos quedan ocultos dentro del pecho del personaje
- ❌ Los brazos están demasiado pegados al torso
- ❌ Las manos atraviesan el cuerpo
- ❌ La animación se ve poco natural

Este script **automáticamente ajusta** las poses para separar los brazos del cuerpo y evitar estas colisiones.

---

## 🚀 Uso Rápido

### Opción 1: Ejecutar el Batch (MÁS FÁCIL)

```bash
scripts\mejorar_animaciones.bat
```

**Menú interactivo con 4 opciones:**
1. Mejorar UN archivo específico
2. Mejorar TODOS los archivos en `test/output/glb`
3. Mejorar TODOS los archivos en directorio personalizado
4. Configuración avanzada (ajustar grados de separación)

### Opción 2: Comando Directo de Blender

```bash
# Mejorar un archivo
blender --background --python scripts\mejorar_animaciones_deepmotion.py -- --input "test\output\glb\Remy_resultado_c.glb"

# Mejorar todo un directorio
blender --background --python scripts\mejorar_animaciones_deepmotion.py -- --directorio "test\output\glb"

# Con ajustes personalizados
blender --background --python scripts\mejorar_animaciones_deepmotion.py -- --input "archivo.glb" --separacion 20 --elevacion 15
```

---

## ⚙️ Parámetros Ajustables

### `--separacion` (default: 15)
Grados de separación lateral de los brazos.
- **Valores bajos (5-10):** Separación sutil
- **Valores medios (10-20):** Separación natural ✅ **Recomendado**
- **Valores altos (20-30):** Brazos muy abiertos

### `--elevacion` (default: 10)
Grados de elevación frontal de los brazos.
- **Valores bajos (5-10):** Elevación sutil ✅ **Recomendado**
- **Valores medios (10-15):** Brazos más adelante
- **Valores altos (15-20):** Brazos muy elevados

---

## 📊 ¿Qué Hace el Script?

### Proceso Automático

```
1. 📂 Carga el archivo GLB/FBX
2. 🔍 Identifica automáticamente los huesos del rig
   - Shoulders (hombros)
   - Upper arms (brazos superiores)
   - Forearms (antebrazos)
   - Hands (manos)
3. 🎬 Procesa TODOS los frames de la animación
4. 🔧 Aplica transformaciones:
   - Separa brazos lateralmente del cuerpo
   - Eleva brazos ligeramente hacia adelante
   - Inserta keyframes para mantener los cambios
5. 💾 Exporta archivo mejorado con sufijo _mejorado
```

### Transformaciones Aplicadas

**Brazo Izquierdo:**
- Shoulder: Rotación Z + `separacion`° (lateral)
- Upper Arm: Rotación X + `elevacion`° (frontal)
- Upper Arm: Rotación Z + `separacion * 0.5`° (lateral)

**Brazo Derecho:**
- Shoulder: Rotación Z - `separacion`° (lateral invertido)
- Upper Arm: Rotación X + `elevacion`° (frontal)
- Upper Arm: Rotación Z - `separacion * 0.5`° (lateral invertido)

---

## 📁 Salidas Generadas

### Archivo Individual

```
Input:  test/output/glb/Remy_resultado_c.glb
Output: test/output/glb/Remy_resultado_c_mejorado.glb
```

### Directorio Completo

```
Input:  test/output/glb/*.glb
Output: test/output/glb/mejorados/*_mejorado.glb
```

---

## 💡 Ejemplos Prácticos

### Ejemplo 1: Mejorar la letra C

```bash
blender --background --python scripts\mejorar_animaciones_deepmotion.py -- --input "test\output\glb\Remy_resultado_c.glb"
```

**Resultado:**
- ✅ Dedos separados del pecho
- ✅ Mano visible durante toda la animación
- ✅ Pose más natural

### Ejemplo 2: Mejorar todas las letras del abecedario

```bash
blender --background --python scripts\mejorar_animaciones_deepmotion.py -- --directorio "test\output\glb"
```

**Resultado:**
- ✅ Procesa automáticamente: a.glb, b.glb, c.glb, ..., z.glb
- ✅ Crea carpeta `mejorados/` con todas las versiones mejoradas

### Ejemplo 3: Ajuste personalizado para señas muy pegadas

```bash
blender --background --python scripts\mejorar_animaciones_deepmotion.py -- --input "señ_pegada.glb" --separacion 25 --elevacion 18
```

**Resultado:**
- ✅ Brazos mucho más separados (25° lateral)
- ✅ Brazos elevados hacia adelante (18° frontal)

---

## 🔍 Identificación Automática de Huesos

El script detecta automáticamente nombres de huesos comunes:

### Patrones Soportados

| Hueso | Patrones Detectados |
|-------|-------------------|
| **Shoulder Left** | `shoulder.l`, `shoulder_l`, `leftshoulder`, `clavicle.l` |
| **Shoulder Right** | `shoulder.r`, `shoulder_r`, `rightshoulder`, `clavicle.r` |
| **Upper Arm Left** | `upperarm.l`, `upper_arm.l`, `arm.l`, `leftarm` |
| **Upper Arm Right** | `upperarm.r`, `upper_arm.r`, `arm.r`, `rightarm` |
| **Forearm Left** | `forearm.l`, `lowerarm.l`, `leftforearm` |
| **Forearm Right** | `forearm.r`, `lowerarm.r`, `rightforearm` |
| **Hand Left** | `hand.l`, `lefthand`, `l_hand`, `wrist.l` |
| **Hand Right** | `hand.r`, `righthand`, `r_hand`, `wrist.r` |

**Compatible con:**
- Mixamo rigs
- DeepMotion exports
- Rigs personalizados con convenciones estándar

---

## ⚠️ Solución de Problemas

### Problema: "No se encontraron huesos críticos"

**Causa:** El rig usa nombres de huesos no estándar.

**Solución:**
1. Abre el archivo en Blender manualmente
2. Ve a Pose Mode
3. Identifica los nombres reales de los huesos
4. Edita `mejorar_animaciones_deepmotion.py` línea 60-80 para agregar tus patrones

### Problema: Los brazos siguen muy pegados

**Solución:** Aumenta `--separacion`
```bash
--separacion 25
```

### Problema: Las manos atraviesan el pecho

**Solución:** Aumenta `--elevacion`
```bash
--elevacion 18
```

### Problema: Los brazos se ven demasiado separados

**Solución:** Reduce `--separacion` y `--elevacion`
```bash
--separacion 8 --elevacion 5
```

---

## 📊 Salida del Script

### Ejemplo de Consola

```
======================================================================
🚀 MEJORADOR DE ANIMACIONES DEEPMOTION
======================================================================
📥 Input:  test/output/glb/Remy_resultado_c.glb
📤 Output: test/output/glb/Remy_resultado_c_mejorado.glb
🎚️  Separación: 15° | Elevación: 10°
======================================================================
✅ Entorno Blender configurado
📂 Cargando: test/output/glb/Remy_resultado_c.glb
✅ Cargado: Armature
🔍 Identificando huesos...
  ✓ shoulder_l: mixamorig:LeftShoulder
  ✓ shoulder_r: mixamorig:RightShoulder
  ✓ upper_arm_l: mixamorig:LeftArm
  ✓ upper_arm_r: mixamorig:RightArm
  ✓ forearm_l: mixamorig:LeftForeArm
  ✓ forearm_r: mixamorig:RightForeArm
  ✓ hand_l: mixamorig:LeftHand
  ✓ hand_r: mixamorig:RightHand

🔧 Aplicando mejoras...
  📐 Separación lateral: 15°
  📐 Elevación frontal: 10°
  🎬 Procesando 148 frames (0 → 147)
  ⏳ Progreso: 50/148 frames
  ⏳ Progreso: 100/148 frames
  ✅ 148 frames procesados

💾 Exportando a: test/output/glb/Remy_resultado_c_mejorado.glb
✅ Exportado: test/output/glb/Remy_resultado_c_mejorado.glb

======================================================================
✅ PROCESO COMPLETADO EXITOSAMENTE
======================================================================
📁 Archivo mejorado guardado en:
   C:\Users\...\test\output\glb\Remy_resultado_c_mejorado.glb

💡 Consejos:
   • Si los brazos siguen muy pegados, aumenta --separacion
   • Si las manos atraviesan el pecho, aumenta --elevacion
   • Valores recomendados: separacion=10-20, elevacion=5-15
```

---

## 🎓 Conceptos Técnicos

### ¿Por qué Ocurre el Problema?

DeepMotion optimiza las poses para naturalidad, pero a veces:
- Los brazos quedan demasiado pegados al torso
- Las rotaciones de hombros no tienen suficiente separación
- El retargeting desde el skeleton original comprime las poses

### ¿Cómo lo Soluciona el Script?

1. **Separación Lateral:** Rota los shoulders en el eje Z para abrir los brazos
2. **Elevación Frontal:** Rota los upper arms en el eje X para traer los brazos adelante
3. **Keyframe Insertion:** Graba las transformaciones en TODOS los frames para mantener consistencia

### Rotaciones Aplicadas

```python
# Brazo Izquierdo
shoulder_l.rotation_euler[2] += radians(separacion)       # Z: lateral
upper_arm_l.rotation_euler[0] += radians(elevacion)       # X: frontal
upper_arm_l.rotation_euler[2] += radians(separacion * 0.5) # Z: lateral

# Brazo Derecho (invertido)
shoulder_r.rotation_euler[2] -= radians(separacion)       # Z: lateral
upper_arm_r.rotation_euler[0] += radians(elevacion)       # X: frontal
upper_arm_r.rotation_euler[2] -= radians(separacion * 0.5) # Z: lateral
```

---

## 🔄 Workflow Recomendado

### Pipeline Completo

```
1. 📹 Graba video de la seña
2. 🤖 Sube a DeepMotion para retargeting
3. 💾 Descarga el GLB exportado
4. 🔧 Ejecuta mejorar_animaciones.bat
5. 🎬 Prueba en test/prueba.html
6. ✅ Si se ve bien: úsalo
7. 🔄 Si no: ajusta --separacion y --elevacion, repite paso 4
```

---

## 📝 Notas Importantes

- ✅ **Compatible con GLB y FBX**
- ✅ **Preserva todas las animaciones existentes**
- ✅ **No modifica el archivo original** (crea uno nuevo con `_mejorado`)
- ✅ **Procesa batch automáticamente**
- ⚠️ **Requiere Blender 3.6+** instalado

---

## 🛠️ Archivos del Sistema

```
scripts/
├── mejorar_animaciones_deepmotion.py  ← Script principal (Python)
├── mejorar_animaciones.bat            ← Launcher interactivo (Windows)
└── README_MEJORADOR.md                ← Este archivo
```

---

## 🎯 Casos de Uso

### ✅ Ideal Para:
- Animaciones de señas donde las manos quedan ocultas
- Exportaciones de DeepMotion con brazos muy pegados
- Rigs Mixamo que necesitan poses más abiertas
- Procesamiento batch de múltiples animaciones

### ❌ NO Recomendado Para:
- Animaciones donde los brazos DEBEN estar pegados al cuerpo
- Poses estáticas sin movimiento
- Animaciones de cuerpo completo (correr, saltar) donde la separación puede verse antinatural

---

**Fecha:** 30 de noviembre de 2025  
**Versión:** 1.0.0  
**Autor:** Sistema de optimización LSV
