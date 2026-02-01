# Sistema de Modificaciones Batch para GLB

Este sistema permite aplicar modificaciones de huesos a múltiples archivos GLB de forma automática.

## 📁 Archivos Creados

### Scripts Python
- `aplicar_modificaciones_batch.py` - Script que procesa carpetas completas de archivos GLB
- `aplicar_modificaciones_blender.py` - Script original que procesa un solo archivo

### Scripts Batch
- `GENERAR_MODIFICACIONES_BATCH.bat` - Procesa carpeta completa
- `GENERAR_MODIFICACIONES.bat` - Procesa archivos individuales (original)

### Archivos de Configuración JSON

#### Para Carpetas Completas:
- `datos_carpeta_batch.json` - Configuración genérica para batch
- `datos_carla_batch.json` - Configuración para carpeta de Carla
- `datos_duvall_batch.json` - Configuración para carpeta de Duvall (por crear)

#### Para Archivos Individuales (originales):
- `datos_carla.json` - Configuración para un archivo de Carla
- `datos_duvall.json` - Configuración para un archivo de Duvall

## 🚀 Uso

### Procesamiento Batch (Carpeta Completa)

1. **Edita el archivo JSON de configuración** (ejemplo: `datos_carpeta_batch.json`):

```json
{
  "carpeta_entrada": "C:/ruta/a/carpeta/entrada",
  "carpeta_salida": "C:/ruta/a/carpeta/salida",
  "patron": "*.glb",
  "excluir": ["*_modif.glb", "*_modificado.glb"],
  "sufijo_salida": "_modif",
  
  "alcance": {
    "min": 24,
    "max": 42,
    "retencion": 13
  },
  
  "RightHandIndex1": {
    "w": 0.962,
    "x": 0.213,
    "y": 0.046,
    "z": 0.166
  }
  // ... más huesos
}
```

2. **Ejecuta el script batch**:
```bash
GENERAR_MODIFICACIONES_BATCH.bat
```

O ejecuta directamente con Blender:
```bash
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python aplicar_modificaciones_batch.py -- datos_carpeta_batch.json
```

### Procesamiento Individual (Original)

Ejecuta el script original:
```bash
GENERAR_MODIFICACIONES.bat
```

## 📋 Configuración JSON

### Parámetros para Batch

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `carpeta_entrada` | Carpeta con archivos GLB originales | `"C:/input/folder"` |
| `carpeta_salida` | Carpeta donde se guardarán los modificados | `"C:/output/folder"` |
| `patron` | Patrón de búsqueda de archivos | `"*.glb"` o `"Carla_*.glb"` |
| `excluir` | Patrones de archivos a excluir | `["*_modif.glb"]` |
| `sufijo_salida` | Sufijo para archivos de salida | `"_modif"` |
| `alcance` | Rango de frames para modificar | Ver abajo |
| `RightHand*` | Valores de rotación de huesos | Ver abajo |

### Alcance de Frames

```json
"alcance": {
  "min": 24,        // Frame inicial del rango
  "max": 42,        // Frame final del rango
  "retencion": 13   // Frames a mantener en pose objetivo
}
```

### Valores de Huesos

```json
"RightHandIndex1": {
  "w": 0.962,  // Componente W del quaternion
  "x": 0.213,  // Componente X del quaternion
  "y": 0.046,  // Componente Y del quaternion
  "z": 0.166   // Componente Z del quaternion
}
```

## 📊 Salida

El script mostrará:
- Número de archivos encontrados
- Número de archivos a procesar
- Progreso para cada archivo
- Número de huesos modificados por archivo
- Resumen final con éxitos y fallos

### Ejemplo de Salida:

```
========================================
PROCESAMIENTO BATCH DE CARPETA
========================================

📂 Carpeta entrada: C:/input/alfabeto
📂 Carpeta salida: C:/output/alfabeto_modificado
🔍 Patrón: *.glb
🚫 Excluir: ['*_modif.glb']
📝 Sufijo: _modif

📊 Archivos encontrados: 27
📊 Archivos a procesar: 27

========================================
[1/27] Carla_a.glb
========================================
📥 Importando GLB...
✅ Armature: Armature
✅ Animación: ArmatureAction
✅ Huesos modificados: 15
💾 Exportando a: Carla_a_modif.glb
✅ Exportado exitosamente!

[...]

========================================
📊 RESUMEN FINAL
========================================
✅ Procesados exitosamente: 27
❌ Fallidos: 0
📁 Archivos en: C:/output/alfabeto_modificado
========================================
```

## 🔍 Diferencias entre Sistemas

### Sistema Original (Individual)
- Procesa 1 archivo a la vez
- Usa `datos_duvall.json` o `datos_carla.json`
- Ejecuta `aplicar_modificaciones_blender.py`
- Ruta de entrada/salida en el JSON como clave del diccionario

### Sistema Batch (Carpeta)
- Procesa múltiples archivos automáticamente
- Usa `datos_*_batch.json`
- Ejecuta `aplicar_modificaciones_batch.py`
- Carpetas de entrada/salida como parámetros separados
- Permite filtrar archivos con patrones
- Genera nombres de salida automáticamente

## 💡 Ejemplos de Uso

### Procesar todos los archivos del alfabeto de Carla:

1. Edita `datos_carla_batch.json`:
```json
{
  "carpeta_entrada": "C:/tesis/test/output/glb/Carla/alfabeto",
  "carpeta_salida": "C:/tesis/test/output/glb/Carla/alfabeto_modificado",
  "patron": "*.glb",
  "excluir": ["*_modif.glb"],
  "sufijo_salida": "_modif",
  // ... resto de configuración
}
```

2. Ejecuta: `GENERAR_MODIFICACIONES_BATCH.bat`

### Procesar solo archivos que empiezan con "Carla_a":

```json
{
  "patron": "Carla_a*.glb",
  // ... resto igual
}
```

## ⚠️ Notas Importantes

1. **No procesar archivos ya modificados**: Usa `"excluir": ["*_modif.glb"]` para evitar reprocesar
2. **Verificar rutas**: Usa `/` en lugar de `\` en las rutas
3. **Backup**: Haz respaldo antes de procesar carpetas completas
4. **Carpeta de salida**: Se crea automáticamente si no existe
5. **Mismo sufijo**: Todos los archivos tendrán el mismo sufijo

## 🐛 Solución de Problemas

### Error: "Carpeta de entrada no existe"
- Verifica que la ruta en `carpeta_entrada` existe
- Asegúrate de usar `/` en lugar de `\`

### Error: "No hay archivos para procesar"
- Verifica el patrón de búsqueda
- Revisa que los archivos no estén excluidos
- Confirma que hay archivos `.glb` en la carpeta

### Archivos sin procesar
- Revisa los logs para ver si tienen animación
- Verifica que tienen Armature
- Confirma que los nombres de huesos coinciden
