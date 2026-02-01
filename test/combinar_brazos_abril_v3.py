"""
Script corregido V3 - Conversión correcta de transformaciones de huesos
Convierte las matrices de transformación del FBX al espacio del GLB
"""

import bpy
import os
from mathutils import Matrix

# Rutas
fbx_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx"
glb_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb"
output_blend = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_combinado_v3.blend"

print("="*80)
print("COMBINACIÓN DE ANIMACIONES - VERSIÓN 3 (Conversión de Matrices)")
print("="*80)

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 1. Importar GLB
print("\n1. Importando GLB base...")
bpy.ops.import_scene.gltf(filepath=glb_path)

glb_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        glb_armature = obj
        break

print(f"   ✓ Armature GLB: {glb_armature.name}")
original_action = glb_armature.animation_data.action if glb_armature.animation_data else None

# 2. Importar FBX
print("\n2. Importando FBX...")
bpy.ops.import_scene.fbx(filepath=fbx_path)

fbx_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != glb_armature:
        fbx_armature = obj
        break

print(f"   ✓ Armature FBX: {fbx_armature.name}")
fbx_action = fbx_armature.animation_data.action if fbx_armature.animation_data else None

# 3. Mapeo de huesos
bone_mapping = {
    'Bip001 L Clavicle': 'LeftShoulder',
    'Bip001 L UpperArm': 'LeftArm',
    'Bip001 L Forearm': 'LeftForeArm',
    'Bip001 L Hand': 'LeftHand',
    'Bip001 R Clavicle': 'RightShoulder',
    'Bip001 R UpperArm': 'RightArm',
    'Bip001 R Forearm': 'RightForeArm',
    'Bip001 R Hand': 'RightHand',
}

print("\n3. Mapeando huesos...")
for fbx_b, glb_b in bone_mapping.items():
    print(f"   {fbx_b} -> {glb_b}")

# 4. Copiar animación con conversión de espacio
print("\n4. Copiando animación con conversión de matrices...")

start_frame = 1
end_frame = int(fbx_action.frame_range[1]) if fbx_action else 73
bpy.context.scene.frame_start = start_frame
bpy.context.scene.frame_end = end_frame

print(f"   Frames: {start_frame} - {end_frame}")

# Seleccionar armature GLB
bpy.context.view_layer.objects.active = glb_armature
glb_armature.select_set(True)
bpy.ops.object.mode_set(mode='POSE')

# Para cada frame
keyframes_insertados = 0
for frame in range(start_frame, end_frame + 1):
    bpy.context.scene.frame_set(frame)
    
    for fbx_bone_name, glb_bone_name in bone_mapping.items():
        if fbx_bone_name not in fbx_armature.pose.bones:
            continue
        if glb_bone_name not in glb_armature.pose.bones:
            continue
            
        fbx_pose_bone = fbx_armature.pose.bones[fbx_bone_name]
        glb_pose_bone = glb_armature.pose.bones[glb_bone_name]
        
        # Obtener matriz mundial del FBX
        fbx_world_matrix = fbx_armature.matrix_world @ fbx_pose_bone.matrix
        
        # Convertir a matriz local del GLB
        # Primero obtener la matriz mundial del padre en GLB
        if glb_pose_bone.parent:
            parent_world_matrix = glb_armature.matrix_world @ glb_pose_bone.parent.matrix
            # Matriz local = inversa(matriz_padre) @ matriz_mundial
            glb_local_matrix = parent_world_matrix.inverted() @ fbx_world_matrix
        else:
            # Si no tiene padre, convertir directamente
            glb_local_matrix = glb_armature.matrix_world.inverted() @ fbx_world_matrix
        
        # Extraer componentes de la matriz
        loc, rot, scale = glb_local_matrix.decompose()
        
        # Aplicar al hueso del GLB
        glb_pose_bone.location = loc
        glb_pose_bone.rotation_quaternion = rot
        glb_pose_bone.scale = scale
        
        # Insertar keyframes
        glb_pose_bone.keyframe_insert(data_path="location", frame=frame)
        glb_pose_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
        glb_pose_bone.keyframe_insert(data_path="scale", frame=frame)
        keyframes_insertados += 3
    
    if frame % 10 == 0:
        print(f"   Frame {frame}/{end_frame}...")

print(f"   ✓ {keyframes_insertados} keyframes insertados")

bpy.ops.object.mode_set(mode='OBJECT')

# 5. Limpiar FBX
print("\n5. Eliminando objetos del FBX...")
objects_to_delete = []
for obj in bpy.data.objects:
    if obj == fbx_armature or (obj.parent == fbx_armature if obj.parent else False):
        objects_to_delete.append(obj)

for obj in objects_to_delete:
    bpy.data.objects.remove(obj, do_unlink=True)

print(f"   ✓ {len(objects_to_delete)} objetos eliminados")

# 6. Verificar
print("\n6. Verificación...")
if glb_armature.animation_data and glb_armature.animation_data.action:
    action = glb_armature.animation_data.action
    arm_fcurves = 0
    for fcurve in action.fcurves:
        if 'pose.bones' in fcurve.data_path:
            bone_name = fcurve.data_path.split('"')[1]
            if bone_name in bone_mapping.values():
                arm_fcurves += 1
    
    print(f"   ✓ FCurves de brazos: {arm_fcurves}")
    print(f"   ✓ Animación: {action.name}")

# 7. Guardar
print("\n7. Guardando...")
os.makedirs(os.path.dirname(output_blend), exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=output_blend)

print("\n" + "="*80)
print("✅ COMPLETADO")
print("="*80)
print(f"Archivo: {output_blend}")
print("\nVerifica que los brazos repliquen el movimiento del FBX")
print("="*80)
