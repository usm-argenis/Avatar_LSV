"""
Script para aplicar animaciones faciales JSON a TODOS los archivos GLB de Duvall
Procesa las 256 palabras completas
"""

import bpy
import json
from pathlib import Path
import re

# Mapeo de palabras a categorías (basado en la estructura de carpetas)
WORD_TO_CATEGORY = {}

# Cargar estructura de carpetas
base_path = Path("output/glb/Duvall")
for category_folder in base_path.iterdir():
    if category_folder.is_dir():
        for glb_file in category_folder.glob("Duvall_resultado_*.glb"):
            # Extraer nombre de palabra del archivo
            word = glb_file.stem.replace("Duvall_resultado_", "")
            WORD_TO_CATEGORY[word] = category_folder.name

print(f"📁 Encontradas {len(WORD_TO_CATEGORY)} palabras en {len(set(WORD_TO_CATEGORY.values()))} categorías")

# Estadísticas
total_procesados = 0
total_con_gestos = 0
total_neutral = 0
errores = []

print("\n" + "="*70)
print("PROCESANDO TODOS LOS ARCHIVOS GLB")
print("="*70)

for word, categoria in sorted(WORD_TO_CATEGORY.items()):
    glb_file = base_path / categoria / f"Duvall_resultado_{word}.glb"
    json_file = Path(f"output/glb/Rostro/{word}.json")
    
    if not glb_file.exists():
        print(f"\n⚠️ No existe GLB: {word}")
        errores.append({"word": word, "error": "GLB no encontrado"})
        continue
    
    if not json_file.exists():
        print(f"\n⚠️ No existe JSON: {word}")
        errores.append({"word": word, "error": "JSON no encontrado"})
        continue
    
    # Mostrar progreso cada 10 archivos
    if total_procesados % 10 == 0:
        print(f"\n[{total_procesados}/{len(WORD_TO_CATEGORY)}] Procesando: {word} ({categoria})")
    
    try:
        # Limpiar escena
        bpy.ops.wm.read_homefile(use_empty=True)
        
        # Importar GLB
        bpy.ops.import_scene.gltf(filepath=str(glb_file))
        
        # Encontrar objetos con morph targets
        morph_objects = []
        for obj in bpy.data.objects:
            if obj.type == 'MESH' and obj.data.shape_keys:
                if any(name in obj.name for name in ['Wolf3D_Head', 'EyeLeft', 'EyeRight', 'Wolf3D_Teeth']):
                    morph_objects.append(obj)
        
        if not morph_objects:
            errores.append({"word": word, "error": "No morph objects"})
            continue
        
        # Cargar datos faciales
        with open(json_file, 'r', encoding='utf-8') as f:
            facial_data = json.load(f)
        
        if not facial_data.get('shapeKeys'):
            total_neutral += 1
            total_procesados += 1
            continue
        
        # Para cada objeto con morph targets, crear su PROPIA action
        total_fcurves = 0
        for obj in morph_objects:
            # Crear animation_data si no existe
            if not obj.animation_data:
                obj.animation_data_create()
            
            # Crear action única
            base_name = re.sub(r'\.\d+$', '', obj.name)
            action_name = f"{base_name}_{word}_facial"
            
            if action_name in bpy.data.actions:
                action = bpy.data.actions[action_name]
            else:
                action = bpy.data.actions.new(name=action_name)
            
            obj.animation_data.action = action
            action.use_fake_user = True
            
            # Obtener shape key names
            shape_key_names = [sk.name for sk in obj.data.shape_keys.key_blocks]
            
            # Aplicar shape keys del JSON
            for shape_key_name, frames_data in facial_data['shapeKeys'].items():
                if shape_key_name in shape_key_names:
                    data_path = f'data.shape_keys.key_blocks["{shape_key_name}"].value'
                    
                    fcurve = action.fcurves.find(data_path)
                    if fcurve:
                        while len(fcurve.keyframe_points) > 0:
                            fcurve.keyframe_points.remove(fcurve.keyframe_points[0])
                    else:
                        fcurve = action.fcurves.new(data_path)
                    
                    for frame_data in frames_data:
                        fcurve.keyframe_points.insert(frame_data['frame'], frame_data['value'])
                    
                    for kf in fcurve.keyframe_points:
                        kf.interpolation = 'LINEAR'
                    
                    total_fcurves += 1
        
        # Exportar GLB
        bpy.ops.export_scene.gltf(
            filepath=str(glb_file),
            export_format='GLB',
            export_animations=True,
            export_morph=True,
            export_morph_normal=True,
            export_morph_tangent=True
        )
        
        if total_fcurves > 0:
            total_con_gestos += 1
        
        total_procesados += 1
        
    except Exception as e:
        print(f"\n❌ Error en {word}: {e}")
        errores.append({"word": word, "error": str(e)})

print("\n" + "="*70)
print("RESUMEN FINAL")
print("="*70)
print(f"Total procesados: {total_procesados}/{len(WORD_TO_CATEGORY)}")
print(f"Con gestos faciales: {total_con_gestos}")
print(f"Neutrales: {total_neutral}")
print(f"Errores: {len(errores)}")

if errores:
    print("\nPrimeros errores:")
    for err in errores[:5]:
        print(f"  - {err['word']}: {err['error']}")
