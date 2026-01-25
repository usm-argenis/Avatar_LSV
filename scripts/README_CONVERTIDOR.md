# 🎭 Convertidor de Señas - Guía de Uso

## 📋 Descripción

Este script automatiza completamente el proceso de transferir cualquier animación FBX al avatar Standing Torch, realizando retargeting automático de huesos.

---

## 🚀 Uso Rápido

### Opción 1: Modo Interactivo (Recomendado)

```bash
python scripts/convertir_sena.py
```

El script te guiará paso a paso:
1. Te pedirá la ruta del FBX con la animación
2. Te sugerirá un nombre para el archivo de salida
3. Ejecutará la conversión automáticamente

### Opción 2: Editar el Script Directamente

Si quieres procesar múltiples archivos, puedes editar `simple_transfer.py` directamente:

```python
# Editar estas 3 líneas en scripts/simple_transfer.py:

PIEL_FBX = r"C:\Users\andre\Downloads\Standing Torch Light Torch.fbx"
ANIMACION_FBX = r"C:\Users\andre\Downloads\abecedario\tu_archivo.fbx"  # ← CAMBIAR AQUÍ
OUTPUT_FBX = r"C:\Users\andre\Downloads\abecedario\resultado.fbx"      # ← CAMBIAR AQUÍ
```

Luego ejecuta:

```bash
blender --background --python scripts/simple_transfer.py
```

---

## 📁 Estructura de Archivos

```
scripts/
├── convertir_sena.py       # Script interactivo (USAR ESTE)
└── simple_transfer.py      # Script base de Blender

downloads/
├── Standing Torch Light Torch.fbx  # Avatar (piel)
└── abecedario/
    ├── a_xyz123.fbx         # Animación letra A
    ├── b_xyz456.fbx         # Animación letra B
    ├── resultado_a.fbx      # ← Salida generada
    └── resultado_b.fbx      # ← Salida generada
```

---

## ⚙️ Configuración

### Rutas por Defecto

El script usa estas rutas por defecto. Edítalas en `convertir_sena.py` si tus archivos están en otro lugar:

```python
# Ruta de Blender
BLENDER_PATH = r"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe"

# Ruta del avatar
AVATAR_PATH = r"C:\Users\andre\Downloads\Standing Torch Light Torch.fbx"

# Directorio de salida
DEFAULT_OUTPUT_DIR = r"C:\Users\andre\Downloads\abecedario"
```

---

## 🎯 Ejemplo Completo

### Paso 1: Ejecutar el script

```bash
cd C:\Users\andre\OneDrive\Documentos\tesis
python scripts/convertir_sena.py
```

### Paso 2: Seguir las instrucciones

```
======================================================================
              🎭 CONVERTIDOR DE SEÑAS - LSV
======================================================================

ℹ️  Verificando requisitos...
✅ Blender encontrado
✅ Avatar encontrado
✅ Script de Blender encontrado

======================================================================
                        CONFIGURACIÓN
======================================================================

ℹ️  Ingresa la ruta completa del archivo FBX con la animación de la seña:
ℹ️  Ejemplo: C:\Users\andre\Downloads\abecedario\b_hXBrhdpmbtpo6dwf3zVGyw.fbx

Ruta del FBX: C:\Users\andre\Downloads\abecedario\c_xyz789.fbx

✅ Archivo de animación: c_xyz789.fbx

ℹ️  Nombre sugerido para el archivo de salida: resultado_c_xyz789.fbx
ℹ️  Presiona ENTER para usar el nombre sugerido, o escribe uno nuevo:
Nombre: resultado_c.fbx

✅ Archivo de salida: resultado_c.fbx

⚠️  ¿Proceder con la conversión?
(s/n): s
```

### Paso 3: Esperar resultado

```
======================================================================
                   EJECUTANDO CONVERSIÓN
======================================================================

ℹ️  Preparando script de Blender...
ℹ️  Ejecutando Blender...
ℹ️  (Esto puede tomar unos segundos...)

PASO 1: Importar FBX con animación
  ✓ Armature: Armature (52 huesos)
  ✓ Animación: 85 frames

PASO 2: Importar mesh de piel
  ✓ Mesh: Ch06

PASO 3: Retargeting de vertex groups
  ✅ Renombrados: 52 vertex groups

PASO 4: Enlazar piel con esqueleto animado
  ✓ Parented al armature

PASO 5: Exportar resultado

✅ ¡Conversión completada exitosamente!
ℹ️  Archivo generado: C:\Users\andre\Downloads\abecedario\resultado_c.fbx
ℹ️  Tamaño: 2.34 MB
```

---

## 🔧 Solución de Problemas

### Error: "No se encontró Blender"

**Solución:** Edita la variable `BLENDER_PATH` en `convertir_sena.py`:

```python
BLENDER_PATH = r"C:\Ruta\A\Tu\Blender\blender.exe"
```

### Error: "No se encontró el avatar"

**Solución:** Descarga o mueve el archivo `Standing Torch Light Torch.fbx` a la ubicación correcta, o edita `AVATAR_PATH`.

### Error: "El archivo no tiene animación"

**Causa:** El FBX que seleccionaste no contiene animación, solo geometría.

**Solución:** Asegúrate de usar el archivo correcto que tenga la animación de la seña.

### El mesh no se deforma en Blender

**Causa:** Los nombres de huesos no coinciden exactamente.

**Solución:** El script intenta hacer retargeting automático de estos formatos:
- `mixamorig9:*` → `*_JNT`
- Si tu FBX usa otra nomenclatura, tendrás que editar el mapeo `BONE_MAP` en `simple_transfer.py`

---

## 📊 ¿Qué hace el script exactamente?

1. **Importa la animación** del FBX que seleccionaste
2. **Elimina el mesh temporal** (solo necesitamos el esqueleto)
3. **Importa el avatar Standing Torch** (el mesh/piel)
4. **Elimina el esqueleto del avatar** (no lo necesitamos)
5. **Renombra los vertex groups** para que coincidan con el esqueleto de animación
   - `mixamorig9:LeftArm` → `l_arm_JNT`
   - `mixamorig9:RightHand` → `r_hand_JNT`
   - etc. (52 huesos mapeados)
6. **Conecta el mesh con el esqueleto** usando Armature Modifier
7. **Exporta el resultado** como un nuevo FBX

---

## 🎨 Resultado Final

El archivo FBX generado contiene:
- ✅ 1 esqueleto con animación (52 huesos)
- ✅ 1 mesh del avatar Standing Torch
- ✅ Vertex groups correctamente mapeados
- ✅ Animación funcional

**Listo para:**
- Importar en Blender y ver la animación
- Usar en Unity/Unreal Engine
- Visualizar en el navegador con Three.js

---

## 📚 Scripts Relacionados

- `simple_transfer.py` - Script base que hace el retargeting
- `transfer_animation.py` - Script anterior (con eliminación de tren inferior)
- `list_bones.py` - Para ver nombres de huesos de un FBX
- `fix_fbx_animation.py` - Para reparar FBX con animación perdida

---

## 💡 Tips

1. **Nombra tus archivos de forma descriptiva:**
   - ❌ `b_hXBrhdpmbtpo6dwf3zVGyw.fbx`
   - ✅ `letra_b.fbx` o `b_seña.fbx`

2. **Organiza por carpetas:**
   ```
   abecedario/
   ├── letra_a.fbx
   ├── letra_b.fbx
   ├── letra_c.fbx
   └── resultados/
       ├── resultado_a.fbx
       ├── resultado_b.fbx
       └── resultado_c.fbx
   ```

3. **Verifica siempre en Blender antes de usar:**
   - Importa el FBX
   - Presiona ESPACIO
   - Asegúrate que la animación se ve bien

4. **Usa el visualizador web:**
   - Abre `test/visualizador_senas.html`
   - Carga tu FBX
   - Verifica que todo funciona

---

## 🆘 Ayuda

Si tienes problemas, verifica:

1. ✅ Blender 4.5+ instalado
2. ✅ Standing Torch avatar descargado
3. ✅ Archivo FBX de animación tiene esqueleto con nomenclatura `*_JNT`
4. ✅ Python 3.8+ instalado

**¿Necesitas más ayuda?** Revisa los mensajes de error del script, suelen indicar exactamente qué falta.
