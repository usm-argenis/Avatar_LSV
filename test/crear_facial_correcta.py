"""
Script para crear UNA animación facial correcta desde cero y verificar que funciona
"""
import bpy
from pathlib import Path
import json

# Limpiar
bpy.ops.wm.read_homefile(use_empty=True)

# Importar un GLB de Duvall (el procesado)
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\saludos\Duvall_resultado_hola.glb")
print(f"Importando: {glb_path}")
bpy.ops.import_scene.gltf(filepath=str(glb_path))

# Buscar objetos con morph targets
morph_objects = []
for obj in bpy.data.objects:
    if obj.type == 'MESH' and obj.data.shape_keys:
        if any(name in obj.name for name in ['Wolf3D_Head', 'EyeLeft', 'EyeRight', 'Wolf3D_Teeth']):
            morph_objects.append(obj)
            print(f"\n✅ Objeto con morphs: {obj.name}")
            print(f"   Shape keys: {len(obj.data.shape_keys.key_blocks)}")

# Cargar datos faciales de hola
json_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Rostro\hola.json")
with open(json_path, 'r', encoding='utf-8') as f:
    facial_data = json.load(f)

print(f"\n📝 Datos faciales: {len(facial_data['shapeKeys'])} shape keys")
for sk_name in facial_data['shapeKeys'].keys():
    print(f"   - {sk_name}")

# CLAVE: Para cada objeto con morphs, crear su PROPIA action separada
for obj in morph_objects:
    print(f"\n🎬 Configurando animación para: {obj.name}")
    
    # Crear animation_data si no existe
    if not obj.animation_data:
        obj.animation_data_create()
        print(f"   ✅ Animation data creado")
    
    # Crear action ÚNICA para este objeto (no compartir)
    # Usar nombre base del objeto (sin sufijo .001)
    base_name = obj.name.split('.')[0]
    action_name = f"{base_name}_hola_facial"
    
    if action_name in bpy.data.actions:
        action = bpy.data.actions[action_name]
        print(f"   ✅ Usando action existente: {action.name}")
    else:
        action = bpy.data.actions.new(name=action_name)
        print(f"   ✅ Action nueva creada: {action.name}")
    
    obj.animation_data.action = action
    action.use_fake_user = True
    
    # Agregar F-Curves para los shape keys
    shape_key_names = [sk.name for sk in obj.data.shape_keys.key_blocks]
    added = 0
    
    for sk_name, frames_data in facial_data['shapeKeys'].items():
        if sk_name in shape_key_names:
            # Data path para este shape key
            data_path = f'data.shape_keys.key_blocks["{sk_name}"].value'
            
            # Buscar si ya existe el F-Curve
            existing_fcurve = action.fcurves.find(data_path)
            if existing_fcurve:
                # Eliminar keyframes existentes
                while len(existing_fcurve.keyframe_points) > 0:
                    existing_fcurve.keyframe_points.remove(existing_fcurve.keyframe_points[0])
                fcurve = existing_fcurve
            else:
                # Crear nuevo F-Curve
                fcurve = action.fcurves.new(data_path)
            
            # Agregar keyframes
            for frame_data in frames_data:
                frame = frame_data['frame']
                value = frame_data['value']
                fcurve.keyframe_points.insert(frame, value)
            
            # Interpolación lineal
            for kf in fcurve.keyframe_points:
                kf.interpolation = 'LINEAR'
            
            added += 1
    
    print(f"   ✅ Agregados {added} F-Curves")

# Mostrar resumen de la acción final
print(f"\n📊 RESUMEN DE ANIMACIONES:")
for action in bpy.data.actions:
    print(f"\nAction: {action.name}")
    print(f"  Total F-Curves: {len(action.fcurves)}")
    
    # Contar por tipo
    bone_curves = sum(1 for fc in action.fcurves if 'pose.bones' in fc.data_path)
    shape_curves = sum(1 for fc in action.fcurves if 'shape_keys' in fc.data_path)
    
    print(f"  F-Curves de huesos: {bone_curves}")
    print(f"  F-Curves de shape keys: {shape_curves}")

# EXPORTAR
output_glb = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\test_hola_corregido.glb")
print(f"\n💾 Exportando a: {output_glb}")

bpy.ops.export_scene.gltf(
    filepath=str(output_glb),
    export_format='GLB',
    export_animations=True,
    export_morph=True,
    export_morph_normal=True,
    export_morph_tangent=True
)

print(f"✅ Exportado exitosamente")

# VERIFICAR reimportando
print(f"\n🔍 VERIFICACIÓN: Reimportando para comprobar...")
bpy.ops.wm.read_homefile(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(output_glb))

print(f"\nObjetos importados:")
for obj in bpy.data.objects:
    if obj.type == 'MESH' and obj.data.shape_keys:
        if any(name in obj.name for name in ['Wolf3D_Head', 'EyeLeft', 'EyeRight', 'Wolf3D_Teeth']):
            print(f"\n  {obj.name}:")
            if obj.animation_data and obj.animation_data.action:
                action = obj.animation_data.action
                shape_fcurves = [fc for fc in action.fcurves if 'shape_keys' in fc.data_path]
                print(f"    ✅ Tiene action: {action.name}")
                print(f"    ✅ F-Curves de shape keys: {len(shape_fcurves)}")
                if shape_fcurves:
                    print(f"    Primeros shape keys animados:")
                    for fc in shape_fcurves[:3]:
                        # Extraer nombre del shape key
                        import re
                        match = re.search(r'key_blocks\["([^"]+)"\]', fc.data_path)
                        if match:
                            sk_name = match.group(1)
                            num_kf = len(fc.keyframe_points)
                            print(f"      - {sk_name}: {num_kf} keyframes")
            else:
                print(f"    ❌ NO tiene animation_data/action")

print(f"\n✅ VERIFICACIÓN COMPLETADA")
