# 📋 Archivos Importantes del Proyecto LSV

## 🎯 Scripts Principales

### `scripts/transfer_animation_to_jh.py`
**Función**: Transferir animación entre avatares diferentes (Remy → JH)
- Mapea automáticamente huesos entre esqueletos
- Ajusta escala entre avatares
- Preserva materiales y texturas
- **Uso**: Transfiere señas de un avatar a otro

### `scripts/update_fbx_from_json.py`
**Función**: Actualizar animación de manos en FBX usando datos de JSON
- Lee landmarks de MediaPipe desde JSONs SignAvatar
- Aplica animación híbrida optimizada (pulgar libre, dedos Z-curl)
- Preserva materiales y escala original
- **Uso**: Mejora animaciones de manos en FBX existentes

### `scripts/convertir_sena.py`, `convert_skeletons.py`, `convert_with_hands.py`
**Función**: Scripts de conversión y procesamiento de señas
- Conversión entre formatos
- Procesamiento de esqueletos
- Integración de datos de manos

---

## 🌐 Visualizadores HTML

### `test/viewer_senas_v3.html` ⭐ **PRINCIPAL**
- Visualizador actualizado con todas las señas
- Incluye versiones "Actualizada" con manos mejoradas
- Soporte para FBX de ambos avatares (Remy y JH)

### Otros visualizadores:
- `test/viewer_senas_v2.html` - Versión anterior
- `test/visualizador_senas.html` - Versión simple
- `test/editor_senas.html` - Editor de señas
- `test/index.html` - Procesador con MediaPipe

---

## 📊 Datos JSON

### `data/coordenates/` (6 archivos)
Coordenadas MediaPipe raw de videos procesados:
- `b.json`, `c.json`, `d.json`, `e.json` - Nuevas señas
- `estacion.json`, `hola.json` - Señas originales

### `data/skeletons/` (6 archivos)
Esqueletos procesados con jerarquía:
- `b_skel.json`, `c_skel.json`, `d_skel.json`, `e_skel.json`
- `estacion_skel.json`, `hola_skel.json`

### `test/output/` (6 archivos SignAvatar)
Formato SignAvatar v2.0 con 58 puntos (16 skeleton + 42 manos):
- `b_signavatar.json`, `c_signavatar.json`, `d_signavatar.json`, `e_signavatar.json`
- `estacion_signavatar.json`, `hola_signavatar.json`

---

## 🎬 Archivos FBX Finales

### Avatar Remy (4 archivos, ~27 MB cada uno)
`output/Remy_resultado_*.fbx`
- Señas B, C, D, E con animación de manos MEJORADA
- Algoritmo híbrido: pulgar libre, dedos Z-curl optimizado
- Materiales y texturas preservados

### Avatar JH (4 archivos, ~52 MB cada uno)
`output/JH_resultado_*.fbx`
- Señas B, C, D, E transferidas desde Remy
- 65/67 huesos mapeados (97%)
- Factor de escala: 0.447x
- Texturas empacadas correctamente

---

## 🔧 Workflow Completo

1. **Video → JSON**
   - `test/index.html` procesa video con MediaPipe
   - Genera `data/coordenates/*.json`

2. **JSON → Skeleton**
   - `scripts/convert_skeletons.py` procesa coordenadas
   - Genera `data/skeletons/*_skel.json`

3. **Skeleton → SignAvatar**
   - Convierte a formato v2.0 con 58 puntos
   - Genera `test/output/*_signavatar.json`

4. **SignAvatar → FBX (Remy)**
   - `scripts/update_fbx_from_json.py` actualiza manos
   - Genera `output/Remy_resultado_*.fbx`

5. **Remy → JH**
   - `scripts/transfer_animation_to_jh.py` transfiere animación
   - Genera `output/JH_resultado_*.fbx`

6. **Visualización**
   - `test/viewer_senas_v3.html` muestra resultados

---

## 📌 Notas Importantes

### Algoritmo de Animación de Manos (Híbrido)
- **Pulgar**: Rotación completa (quaternion) con límite de twist (0.3x)
- **Dedos**: Solo Z-curl con factor 0.75x
- **Límites**: 110° flexión, -20° hiperextensión
- **Resultado**: Balance entre precisión y calidad de skinning

### Transferencia entre Avatares
- Mapeo automático por nombre de huesos
- Calcula factor de escala entre esqueletos
- Preserva materiales y texturas del avatar target
- Copia rotaciones y location del root

### Formato SignAvatar v2.0
```json
{
  "version": "2.0",
  "bones": [58 huesos con jerarquía],
  "bone_groups": {
    "skeleton": [0-15],
    "left_hand": [16-36],
    "right_hand": [37-57]
  },
  "frames": [{"time": 0.0, "positions": [[x,y,z], ...]}]
}
```

---

## ✅ Archivos Eliminados (Limpieza)

- ❌ Scripts experimentales: `apply_animation_to_avatars.py`, `check_*.py`, etc.
- ❌ Carpeta `comparisons/` (análisis temporales)
- ❌ Scripts de test temporales: `build_eskeleton.py`, `temp_check.py`, etc.
- ❌ `test/scripts/` (contenía solo `check_frames.py`)

---

**Fecha de limpieza**: 22/10/2025
**Archivos conservados**: ~35 archivos esenciales
**Espacio liberado**: Scripts y análisis temporales eliminados
