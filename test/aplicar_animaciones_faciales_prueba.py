"""
Script para aplicar animaciones faciales JSON a archivos GLB - VERSIÓN CORRECTA
Crea actions separadas para cada objeto con morph targets
"""

import bpy
import os
import json
from pathlib import Path

# Lista de palabras de prueba
test_words = ["hola", "adios", "amar", "bienvenido", "buenos_dias"]

print("="*70)
print("APLICANDO ANIMACIONES FACIALES A GLB - PRUEBA")
print("="*70)

for word in test_words:
    # Construir rutas
    categoria = None
    if word in ["hola", "adios"]:
        categoria = "saludos"
    elif word in ["amar"]:
        categoria = "sentimientos"
    elif word in ["bienvenido", "buenos_dias"]:
        categoria = "expresiones_comunes"
    
    if not categoria:
        print(f"\n❌ No se encontró categoría para '{word}'")
        continue
    
    glb_file = Path(f"output/glb/Duvall/{categoria}/Duvall_resultado_{word}.glb")
    
    if not glb_file.exists():
        print(f"\n❌ No existe: {glb_file}")
        continue
    
    print(f"\n{'='*70}")
    print(f"Procesando: {word}")
    print(f"Archivo: {glb_file.name}")
    
    # Limpiar escena
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # Importar GLB
    print(f"📦 Importando GLB...")
    bpy.ops.import_scene.gltf(filepath=str(glb_file))
    
    # Encontrar TODOS los objetos con morph targets (facial meshes)
    morph_objects = []
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.shape_keys:
            if any(name in obj.name for name in ['Wolf3D_Head', 'EyeLeft', 'EyeRight', 'Wolf3D_Teeth']):
                morph_objects.append(obj)
    
    if not morph_objects:
        print(f"❌ No se encontraron objetos con morph targets")
        continue
    
    print(f"✅ Encontrados {len(morph_objects)} objetos con morph targets:")
    for obj in morph_objects:
        print(f"   - {obj.name}: {len(obj.data.shape_keys.key_blocks)} shape keys")
    
    # Cargar datos faciales
    json_path = Path(f"output/glb/Rostro/{word}.json")
    if not json_path.exists():
        print(f"❌ No se encontró {json_path}")
        continue
    
    with open(json_path, 'r', encoding='utf-8') as f:
        facial_data = json.load(f)
    
    if not facial_data.get('shapeKeys'):
        print(f"⚠️ JSON tiene 0 shape keys para {word}")
        continue
    
    print(f"📝 JSON contiene {len(facial_data['shapeKeys'])} shape keys animados")
    for sk_name in facial_data['shapeKeys'].keys():
        print(f"   - {sk_name}")
    
    # Para cada objeto con morph targets, crear su PROPIA action
    total_applied = 0
    for obj in morph_objects:
        # Crear animation_data si no existe
        if not obj.animation_data:
            obj.animation_data_create()
        
        # Crear una action ÚNICA para este objeto
        # Usar nombre base (sin sufijo .001 etc)
        import re
        base_name = re.sub(r'\.\d+$', '', obj.name)
        action_name = f"{base_name}_{word}_facial"
        
        if action_name in bpy.data.actions:
            action = bpy.data.actions[action_name]
        else:
            action = bpy.data.actions.new(name=action_name)
        
        obj.animation_data.action = action
        action.use_fake_user = True
        
        # Obtener shape key names de este objeto
        shape_key_names = [sk.name for sk in obj.data.shape_keys.key_blocks]
        
        # Aplicar shape keys del JSON a esta action
        applied_to_obj = 0
        for shape_key_name, frames_data in facial_data['shapeKeys'].items():
            if shape_key_name in shape_key_names:
                # Data path relativo a ESTE objeto
                data_path = f'data.shape_keys.key_blocks["{shape_key_name}"].value'
                
                # Buscar o crear F-Curve
                fcurve = action.fcurves.find(data_path)
                if fcurve:
                    # Limpiar keyframes existentes
                    while len(fcurve.keyframe_points) > 0:
                        fcurve.keyframe_points.remove(fcurve.keyframe_points[0])
                else:
                    fcurve = action.fcurves.new(data_path)
                
                # Añadir keyframes
                for frame_data in frames_data:
                    frame = frame_data['frame']
                    value = frame_data['value']
                    fcurve.keyframe_points.insert(frame, value)
                
                # Interpolación lineal
                for kf in fcurve.keyframe_points:
                    kf.interpolation = 'LINEAR'
                
                applied_to_obj += 1
        
        if applied_to_obj > 0:
            print(f"   ✅ {obj.name}: {applied_to_obj} shape keys animados")
            total_applied += applied_to_obj
    
    print(f"\n✅ Total de F-Curves creados: {total_applied}")
    
    # Exportar GLB con animaciones faciales
    print(f"💾 Exportando GLB...")
    bpy.ops.export_scene.gltf(
        filepath=str(glb_file),
        export_format='GLB',
        export_animations=True,
        export_morph=True,
        export_morph_normal=True,
        export_morph_tangent=True
    )
    
    print(f"✅ Exportado: {glb_file.name}")

print("\n" + "="*70)
print("✅ PROCESAMIENTO COMPLETADO")
print("="*70)
