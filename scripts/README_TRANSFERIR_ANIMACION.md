# 🎬 Transferencia de Animaciones entre Avatares FBX

Scripts para transferir animaciones de un modelo FBX a otro, con ajuste automático de escala y mapeo de huesos.

## 📋 Requisitos

- **Blender 3.0+** instalado en tu sistema
  - Descarga: https://www.blender.org/download/
  - El script buscará automáticamente Blender en las rutas comunes de instalación

## 🚀 Uso Rápido

### Opción 1: Script BAT (más fácil)

Simplemente ejecuta el archivo `.bat`:

```bash
scripts\transferir_a_leonard.bat
```

Este script transferirá automáticamente la animación de `Remy_resultado_b.fbx` a `Leonard.fbx`.

**Salida:** `output/Leonard_con_animacion_b.fbx`

---

### Opción 2: Script Genérico (más flexible)

Para transferir cualquier animación a cualquier avatar:

```bash
python scripts/transferir_animacion_generica.py <avatar.fbx> <animacion.fbx> [salida.fbx]
```

**Ejemplos:**

```bash
# Leonard con animación B
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_b.fbx output/Leonard_b.fbx

# Leonard con animación C
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_c.fbx output/Leonard_c.fbx

# JH con animación B
python scripts/transferir_animacion_generica.py avatars/JH.fbx deploy-viewer-temp/output/Remy_resultado_b.fbx output/JH_b.fbx

# Remy con animación de JH
python scripts/transferir_animacion_generica.py avatars/Remy.fbx deploy-viewer-temp/output/JH_resultado_b.fbx output/Remy_from_JH_b.fbx
```

Si omites el tercer parámetro (salida), se genera automáticamente un nombre basado en el avatar y la animación.

---

### Opción 3: Script de Blender Directo

Si prefieres ejecutar el script directamente en Blender:

```bash
blender --background --python scripts/transferir_animacion_a_leonard.py
```

---

## 🎯 ¿Qué hace el script?

1. **Carga el avatar destino** (ej: Leonard.fbx)
   - Conserva el mesh (piel) del avatar
   - Conserva el esqueleto (armature)

2. **Carga la animación fuente** (ej: Remy_resultado_b.fbx)
   - Lee los keyframes de la animación
   - Detecta el esqueleto animado

3. **Calcula la escala automáticamente**
   - Compara la altura de ambos avatares
   - Ajusta el factor de escala para evitar deformaciones

4. **Mapea los huesos**
   - Intenta encontrar correspondencias entre los huesos de ambos esqueletos
   - Soporta nombres exactos o similares
   - Mapeo inteligente por nombre (ej: "hand_r" → "righthand")

5. **Copia los keyframes**
   - Transfiere rotaciones, posiciones y escalas
   - Aplica el factor de escala a las posiciones
   - Preserva los tiempos exactos de los keyframes

6. **Exporta el resultado**
   - Guarda un nuevo FBX con el avatar destino + la animación aplicada
   - Incluye texturas embebidas
   - Optimiza los keyframes (bake_anim)

---

## 📊 Estructura de Archivos

```
tesis/
├── avatars/               # Avatares base (con piel y esqueleto)
│   ├── Leonard.fbx       ← Avatar destino
│   ├── JH.fbx
│   └── Remy.fbx
│
├── deploy-viewer-temp/
│   └── output/           # Animaciones de entrada
│       ├── Remy_resultado_b.fbx  ← Animación fuente
│       ├── Remy_resultado_c.fbx
│       └── ...
│
├── scripts/              # Scripts de transferencia
│   ├── transferir_a_leonard.bat              # BAT para Leonard + B
│   ├── transferir_animacion_a_leonard.py     # Script Blender específico
│   └── transferir_animacion_generica.py      # Script genérico
│
└── output/               # Resultados (se crean aquí)
    ├── Leonard_con_animacion_b.fbx  ← Resultado
    ├── Leonard_c.fbx
    └── ...
```

---

## ⚙️ Parámetros Técnicos

### Ajuste de Escala

El script calcula automáticamente la escala comparando la **altura** de ambos avatares:

```
Escala = Altura_Avatar_Destino / Altura_Avatar_Origen
```

Este factor se aplica solo a las transformaciones de **posición (location)**, mientras que las **rotaciones** se copian sin modificar.

### Mapeo de Huesos

El script intenta mapear huesos usando estos criterios (en orden):

1. **Nombres exactos** (ej: "Spine" → "Spine")
2. **Nombres similares** (ej: "hand_r" contiene "hand")
3. **Mapeo genérico por índice** (como último recurso)

Huesos comunes que se mapean:

- `Hips`, `Spine`, `Chest`, `Neck`, `Head`
- `LeftShoulder`, `LeftArm`, `LeftForeArm`, `LeftHand`
- `RightShoulder`, `RightArm`, `RightForeArm`, `RightHand`
- Variantes: `mixamorig:*`, `*_r`, `*_l`, etc.

---

## 🐛 Solución de Problemas

### Error: "No se encontró Blender instalado"

**Solución 1:** Instala Blender desde https://www.blender.org/download/

**Solución 2:** Edita el archivo `.bat` o `.py` y añade manualmente la ruta:

```python
BLENDER_PATH = r"C:\Ruta\Personalizada\blender.exe"
```

---

### Error: "No se encontró el armature"

Esto significa que el FBX no tiene un esqueleto (armature).

**Verifica:**
- Abre el FBX en Blender manualmente
- Comprueba que tiene un objeto tipo "Armature"

---

### Error: "No hay animación en el origen"

El FBX de animación no contiene keyframes.

**Verifica:**
- Abre el FBX de animación en Blender
- Ve a "Dope Sheet" → "Action Editor"
- Comprueba que hay una "Action" con keyframes

---

### La animación se ve deformada

Esto puede pasar si los esqueletos son muy diferentes.

**Soluciones:**

1. **Ajusta la escala manualmente:**
   ```python
   # En transferir_animacion_generica.py, línea ~80
   auto_escala = False  # Desactiva escala automática
   ```

2. **Usa avatares con esqueletos similares:**
   - Leonard y Remy tienen estructuras similares ✅
   - JH puede tener esqueleto diferente ⚠️

---

### Huesos no se mapean correctamente

**Solución:** Edita el mapeo manual en `transferir_animacion_a_leonard.py`:

```python
# Línea ~120 aprox
mapeo_huesos = {
    "mixamorig:Hips": "Hips",
    "mixamorig:Spine": "Spine",
    "mixamorig:RightArm": "RightUpperArm",
    # ... añade más mapeos manuales
}
```

---

## 🎨 Casos de Uso

### 1. Transferir todas las animaciones de Remy a Leonard

```bash
# Animación B
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_b.fbx output/Leonard_b.fbx

# Animación C
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_c.fbx output/Leonard_c.fbx

# Animación D
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_d.fbx output/Leonard_d.fbx

# Animación E
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_e.fbx output/Leonard_e.fbx
```

### 2. Transferir animaciones de JH a otros avatares

```bash
# JH → Leonard
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/JH_resultado_b.fbx output/Leonard_from_JH_b.fbx

# JH → Remy
python scripts/transferir_animacion_generica.py avatars/Remy.fbx deploy-viewer-temp/output/JH_resultado_b.fbx output/Remy_from_JH_b.fbx
```

### 3. Batch: Transferir múltiples animaciones

Crea un script `.bat`:

```batch
@echo off
echo Transfiriendo todas las animaciones a Leonard...

python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_b.fbx output/Leonard_b.fbx
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_c.fbx output/Leonard_c.fbx
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_d.fbx output/Leonard_d.fbx
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_e.fbx output/Leonard_e.fbx

echo Completado!
pause
```

---

## 📚 Referencias

- [Blender Python API](https://docs.blender.org/api/current/)
- [FBX SDK Documentation](https://help.autodesk.com/view/FBX/2020/ENU/)
- [Retargeting Animations in Blender](https://www.youtube.com/results?search_query=blender+retarget+animation)

---

## ✅ Checklist de Verificación

Antes de ejecutar el script:

- [ ] Blender instalado (versión 3.0 o superior)
- [ ] Avatar destino existe en `avatars/`
- [ ] Animación fuente existe en `deploy-viewer-temp/output/`
- [ ] Ambos FBX tienen armatures (esqueletos)
- [ ] La animación fuente tiene keyframes

Después de ejecutar:

- [ ] Archivo de salida creado en `output/`
- [ ] Abrir en Blender y verificar la animación
- [ ] Comprobar que no hay deformaciones
- [ ] Probar en el visualizador 3D

---

## 🎉 Resultado Esperado

Al ejecutar el script correctamente, obtendrás:

**Archivo:** `output/Leonard_con_animacion_b.fbx`

**Contenido:**
- ✅ Mesh (piel) de Leonard
- ✅ Esqueleto de Leonard
- ✅ Animación de Remy_resultado_b transferida
- ✅ Escala ajustada automáticamente
- ✅ Sin deformaciones

**Puedes usar este archivo en:**
- Three.js (visualizador web)
- Unity
- Unreal Engine
- Cualquier software que soporte FBX

---

**¿Problemas o preguntas?** Revisa la sección de "Solución de Problemas" o abre el archivo en Blender para inspección manual.
