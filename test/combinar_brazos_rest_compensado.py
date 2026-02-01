"""
SOLUCIÓN: Compensar diferencias de rest pose al copiar rotaciones de brazos
"""

import bpy
from pathlib import Path
from mathutils import Quaternion, Matrix

print("="*80)
print("SOLUCIÓN: Copiar brazos compensando rest pose")
print("="*80)

fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_BRAZOS_COMPENSADO.glb")

# Limpiar escena
bpy.ops.wm.read_homefile(use_empty=True)

# Importar GLB target
print(f"📦 Importando GLB target...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))
glb_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        glb_armature = obj
        glb_armature.name = "GLB_Target"
        break

# Importar FBX source
print(f"📦 Importando FBX source...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != glb_armature:
        fbx_armature = obj
        fbx_armature.name = "FBX_Source"
        break

# Escalar FBX
SCALE_FACTOR = 0.0123
fbx_armature.scale = (SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR)
bpy.context.view_layer.update()

# Mapeo de huesos
ARM_BONES_MAPPING = {
    'Bip001 L Clavicle': 'LeftShoulder',
    'Bip001 L UpperArm': 'LeftArm',
    'Bip001 L Forearm': 'LeftForeArm',
    'Bip001 L Hand': 'LeftHand',
    'Bip001 R Clavicle': 'RightShoulder',
    'Bip001 R UpperArm': 'RightArm',
    'Bip001 R Forearm': 'RightForeArm',
    'Bip001 R Hand': 'RightHand',
}

print(f"\n📐 Calculando diferencias de rest pose...")

# Calcular matrices de conversión para cada par de huesos
rest_conversions = {}

for fbx_bone_name, glb_bone_name in ARM_BONES_MAPPING.items():
    if fbx_bone_name not in fbx_armature.data.bones or glb_bone_name not in glb_armature.data.bones:
        print(f"  ⚠️ Hueso no encontrado: {fbx_bone_name} o {glb_bone_name}")
        continue
    
    fbx_bone = fbx_armature.data.bones[fbx_bone_name]
    glb_bone = glb_armature.data.bones[glb_bone_name]
    
    # Rest pose en espacio local
    fbx_rest_local = fbx_bone.matrix_local.copy()
    glb_rest_local = glb_bone.matrix_local.copy()
    
    # Calcular matriz de conversión: de FBX rest a GLB rest
    # conversion = glb_rest @ fbx_rest^-1
    conversion_matrix = glb_rest_local @ fbx_rest_local.inverted()
    
    rest_conversions[glb_bone_name] = conversion_matrix
    
    print(f"  ✓ {glb_bone_name}: Conversión calculada")

print(f"\n🎬 Copiando animación de brazos con compensación...")

# Obtener rango de frames del FBX
fbx_action = fbx_armature.animation_data.action if fbx_armature.animation_data else None
if fbx_action:
    frame_start = int(fbx_action.frame_range[0])
    frame_end = int(fbx_action.frame_range[1])
else:
    frame_start = 1
    frame_end = 73

print(f"  📊 Frames: {frame_start} - {frame_end}")

# Asegurar que GLB tiene animation_data
if not glb_armature.animation_data:
    glb_armature.animation_data_create()
if not glb_armature.animation_data.action:
    glb_armature.animation_data.action = bpy.data.actions.new(name="GLB_Animation")

# Procesar cada frame
for frame in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame)
    bpy.context.view_layer.update()
    
    for fbx_bone_name, glb_bone_name in ARM_BONES_MAPPING.items():
        if fbx_bone_name not in fbx_armature.pose.bones or glb_bone_name not in glb_armature.pose.bones:
            continue
        
        if glb_bone_name not in rest_conversions:
            continue
        
        fbx_pb = fbx_armature.pose.bones[fbx_bone_name]
        glb_pb = glb_armature.pose.bones[glb_bone_name]
        
        # Obtener matriz de pose del FBX en espacio local
        fbx_pose_local = fbx_pb.matrix_basis.copy()
        
        # Aplicar conversión de rest pose
        conversion = rest_conversions[glb_bone_name]
        
        # La rotación compensada es: conversion @ fbx_pose @ conversion^-1
        # Pero queremos solo la rotación, así que:
        fbx_rot = fbx_pose_local.to_quaternion()
        conversion_rot = conversion.to_quaternion()
        
        # Convertir rotación del espacio FBX al espacio GLB
        # glb_rot = conversion_rot @ fbx_rot @ conversion_rot.conjugated()
        glb_rot_compensated = conversion_rot @ fbx_rot @ conversion_rot.conjugated()
        
        # Aplicar al GLB
        glb_pb.rotation_quaternion = glb_rot_compensated
        
        # Insertar keyframe
        glb_pb.keyframe_insert(data_path="rotation_quaternion", frame=frame)
    
    if frame % 10 == 0:
        print(f"  📍 Frame {frame}/{frame_end}")

print(f"\n💾 Exportando resultado...")
output_path.parent.mkdir(exist_ok=True, parents=True)

bpy.ops.export_scene.gltf(
    filepath=str(output_path),
    export_format='GLB',
    use_selection=False,
    export_animations=True,
    export_frame_range=True,
    export_frame_step=1,
    export_nla_strips=False,
    export_def_bones=True,
    export_optimize_animation_size=False
)

file_size = output_path.stat().st_size / 1024
print(f"\n{'='*80}")
print(f"✅ PROCESO COMPLETADO")
print(f"{'='*80}")
print(f"📁 Archivo: {output_path.name}")
print(f"📊 Tamaño: {file_size:.1f} KB")
print(f"🎯 Frames: {frame_start}-{frame_end}")
print(f"✨ Rotaciones compensadas por diferencias de rest pose")
