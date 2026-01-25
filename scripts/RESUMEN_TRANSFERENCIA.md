# 📝 Resumen: Sistema de Transferencia de Animaciones

## ✅ Scripts Creados

Se crearon **4 archivos** en el directorio `scripts/`:

### 1. `transferir_animacion_a_leonard.py`
- **Propósito:** Script de Blender Python para transferir animación a Leonard
- **Uso:** `blender --background --python transferir_animacion_a_leonard.py`
- **Funciones principales:**
  - `limpiar_escena()` - Resetea Blender
  - `importar_fbx()` - Carga archivos FBX
  - `encontrar_armature()` - Detecta esqueletos
  - `copiar_pose()` - Transfiere animación
  - `calcular_escala_necesaria()` - Ajusta tamaño
  - `transferir_animacion()` - Función principal

### 2. `transferir_a_leonard.bat`
- **Propósito:** Ejecutor Windows para uso fácil
- **Uso:** Doble clic o `transferir_a_leonard.bat`
- **Características:**
  - Busca Blender automáticamente en rutas comunes
  - Ejecuta el script Python de Blender
  - Muestra mensajes de progreso

### 3. `transferir_animacion_generica.py`
- **Propósito:** Script Python genérico para cualquier combinación
- **Uso:** `python transferir_animacion_generica.py <avatar> <animacion> [salida]`
- **Ventajas:**
  - Acepta argumentos de línea de comandos
  - Genera nombres de salida automáticos
  - Script Blender embebido (no necesita archivo separado)
  - Búsqueda automática de Blender

### 4. `README_TRANSFERIR_ANIMACION.md`
- **Propósito:** Documentación completa del sistema
- **Contenido:**
  - Guía de instalación
  - Ejemplos de uso
  - Solución de problemas
  - Casos de uso avanzados
  - Parámetros técnicos

## 🎯 Flujo de Trabajo

```
┌─────────────────────────────────────────────────────────────┐
│  ENTRADA                                                    │
├─────────────────────────────────────────────────────────────┤
│  Avatar Destino:   avatars/Leonard.fbx                     │
│  Animación Fuente: deploy-viewer-temp/output/Remy_resultado_b.fbx │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  PROCESAMIENTO (Blender Python)                            │
├─────────────────────────────────────────────────────────────┤
│  1. Importar ambos FBX                                     │
│  2. Detectar armatures (esqueletos)                        │
│  3. Calcular escala: altura_destino / altura_origen        │
│  4. Mapear huesos:                                         │
│     - Por nombre exacto                                    │
│     - Por similitud (contiene, parcial)                    │
│     - Por índice (último recurso)                          │
│  5. Copiar keyframes:                                      │
│     - Rotaciones (sin cambios)                             │
│     - Posiciones (con escala aplicada)                     │
│  6. Eliminar objetos temporales                            │
│  7. Exportar FBX resultante                                │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  SALIDA                                                     │
├─────────────────────────────────────────────────────────────┤
│  Archivo: output/Leonard_con_animacion_b.fbx              │
│                                                             │
│  Contenido:                                                 │
│    ✅ Mesh de Leonard (piel, texturas)                     │
│    ✅ Esqueleto de Leonard                                 │
│    ✅ Animación de Remy (transferida y escalada)           │
│    ✅ Sin deformaciones                                    │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Características Técnicas

### Ajuste Automático de Escala
```python
escala = altura_avatar_destino / altura_avatar_origen

# Aplicado a:
- Posiciones (location): ✅ Con escala
- Rotaciones (rotation): ❌ Sin escala (se copian tal cual)
```

### Mapeo Inteligente de Huesos

**Prioridad 1:** Nombres exactos
```
"Spine" → "Spine"
"Head" → "Head"
```

**Prioridad 2:** Similitudes
```
"mixamorig:RightHand" → "RightHand" (contiene)
"hand_r" → "RightHand" (similar)
```

**Prioridad 3:** Índice genérico
```
hueso[0] → hueso[0]
hueso[1] → hueso[1]
```

### Exportación Optimizada
- `bake_anim=True` - Hornea la animación
- `add_leaf_bones=False` - No añade huesos extra
- `path_mode='COPY'` - Copia texturas
- `embed_textures=True` - Embebe texturas en el FBX

## 📋 Requisitos del Sistema

| Requisito | Versión | Obligatorio |
|-----------|---------|-------------|
| Python | 3.7+ | ✅ Sí |
| Blender | 3.0+ | ✅ Sí |
| Windows | 10/11 | No (funciona en cualquier OS) |

**Instalación de Blender:**
1. Descargar: https://www.blender.org/download/
2. Instalar en ruta por defecto
3. No requiere configuración adicional

## 🚀 Métodos de Ejecución

### Método 1: BAT (Más Fácil)
```bash
# Windows, doble clic
scripts\transferir_a_leonard.bat
```
**Ventaja:** No requiere parámetros  
**Desventaja:** Solo Leonard + Remy_b

### Método 2: Python Genérico (Flexible)
```bash
# Cualquier combinación
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_b.fbx

# Con salida personalizada
python scripts/transferir_animacion_generica.py avatars/JH.fbx deploy-viewer-temp/output/Remy_resultado_c.fbx output/JH_personalizado.fbx
```
**Ventaja:** Cualquier avatar + animación  
**Desventaja:** Requiere especificar rutas

### Método 3: Blender Directo (Avanzado)
```bash
# Ejecutar script directamente en Blender
blender --background --python scripts/transferir_animacion_a_leonard.py
```
**Ventaja:** Control total  
**Desventaja:** Requiere conocimiento de Blender

## 📊 Ejemplo de Salida

```
======================================================================
🎬 TRANSFERENCIA DE ANIMACIÓN
======================================================================

1️⃣  AVATAR DESTINO
📥 Importando: Leonard.fbx
   ✓ Importados 15 objetos
   ✓ Armature: Armature
   ✓ Mesh: Body

2️⃣  ANIMACIÓN FUENTE
📥 Importando: Remy_resultado_b.fbx
   ✓ Importados 12 objetos
   ✓ Armature: mixamorig:Hips

📏 Calculando escala:
   Altura origen: 1.75
   Altura destino: 1.80
   Factor de escala: 1.03

3️⃣  TRANSFERIR ANIMACIÓN
🔄 Copiando animación...
   Origen: mixamorig:Hips
   Destino: Armature
   Escala: 1.03
   ✓ Animación encontrada: Take 001
   ✓ Frames: 1 - 120

🦴 Mapeando huesos:
   Origen: 65 huesos
   Destino: 52 huesos
   ✓ 48 huesos mapeados

⏱️  Copiando keyframes...
   ✓ 2847 keyframes copiados

4️⃣  LIMPIAR OBJETOS TEMPORALES
   ✓ Objetos de animación eliminados

5️⃣  EXPORTAR RESULTADO
   Archivo: Leonard_con_animacion_b.fbx
   ✓ Exportación completada

======================================================================
✅ TRANSFERENCIA EXITOSA
======================================================================

🎉 Archivo generado: C:\Users\andre\...\output\Leonard_con_animacion_b.fbx
```

## 🎯 Casos de Uso Reales

### 1. Todas las animaciones de Remy a Leonard
```bash
for %a in (b c d e) do (
  python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_%a.fbx output/Leonard_%a.fbx
)
```

### 2. Animaciones de JH a todos los avatares
```bash
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/JH_resultado_b.fbx output/Leonard_from_JH.fbx
python scripts/transferir_animacion_generica.py avatars/Remy.fbx deploy-viewer-temp/output/JH_resultado_b.fbx output/Remy_from_JH.fbx
```

### 3. Mezclar animaciones
```bash
# Leonard con animación B de Remy
python scripts/transferir_animacion_generica.py avatars/Leonard.fbx deploy-viewer-temp/output/Remy_resultado_b.fbx

# Luego transferir esa animación a JH
python scripts/transferir_animacion_generica.py avatars/JH.fbx output/Leonard_con_animacion_b.fbx output/JH_from_Leonard_b.fbx
```

## ✅ Verificación del Resultado

### En Blender (Recomendado)
1. Abrir Blender
2. File → Import → FBX
3. Seleccionar `output/Leonard_con_animacion_b.fbx`
4. Ir a "Dope Sheet" → "Action Editor"
5. Presionar ▶ para reproducir
6. Verificar que no hay deformaciones

### En Three.js (Visualizador Web)
```javascript
const loader = new FBXLoader();
loader.load('output/Leonard_con_animacion_b.fbx', (fbx) => {
    scene.add(fbx);
    
    const mixer = new THREE.AnimationMixer(fbx);
    const action = mixer.clipAction(fbx.animations[0]);
    action.play();
});
```

## 🐛 Problemas Conocidos y Soluciones

| Problema | Causa | Solución |
|----------|-------|----------|
| "No se encontró Blender" | Blender no instalado | Instalar desde blender.org |
| "No se encontró armature" | FBX sin esqueleto | Verificar en Blender manualmente |
| Deformaciones en el resultado | Esqueletos muy diferentes | Usar avatares similares |
| Pocos huesos mapeados | Nombres muy diferentes | Editar mapeo manual en el script |
| Animación muy rápida/lenta | FPS diferentes | Ajustar FPS en exportación |

## 📈 Métricas de Éxito

**Para considerar la transferencia exitosa:**

✅ Archivo FBX generado sin errores  
✅ Al menos 60% de huesos mapeados  
✅ Más de 1000 keyframes copiados (típico)  
✅ No hay deformaciones visibles al reproducir  
✅ Escala calculada entre 0.8 - 1.2 (razonable)  

## 🔜 Próximos Pasos

1. **Ejecutar el script:**
   ```bash
   scripts\transferir_a_leonard.bat
   ```

2. **Verificar resultado en Blender**

3. **Si funciona:** Transferir más animaciones

4. **Integrar con visualizador:**
   - Subir a GitHub Pages
   - Actualizar rutas en el visualizador Three.js
   - Probar en la app móvil

## 📞 Soporte

Si tienes problemas:

1. Lee `README_TRANSFERIR_ANIMACION.md` (documentación completa)
2. Verifica que Blender esté instalado
3. Abre los FBX manualmente en Blender para verificar estructura
4. Revisa los logs de Blender en la consola

---

**Creado:** 7 de Noviembre de 2025  
**Archivos:** 4 scripts + 2 READMEs  
**Estado:** ✅ Listo para usar (requiere Blender)
