import bpy
import mathutils
from pathlib import Path

# Rutas de archivos
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_combinado_v4.blend")

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

print("Importando GLB...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))
glb_armature = bpy.context.selected_objects[0]
glb_armature.name = "GLB_Armature"
print(f"GLB importado: {glb_armature.name} con {len(glb_armature.data.bones)} huesos")

print("\nImportando FBX...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_objects = [obj for obj in bpy.context.selected_objects if obj != glb_armature]
fbx_armature = next((obj for obj in fbx_objects if obj.type == 'ARMATURE'), None)
if fbx_armature:
    fbx_armature.name = "FBX_Armature"
    print(f"FBX importado: {fbx_armature.name} con {len(fbx_armature.data.bones)} huesos")

# Mapeo de huesos (FBX -> GLB)
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

print(f"\nHuesos a mapear: {len(bone_mapping)}")

# Asegurar que hay una acción
if not glb_armature.animation_data:
    glb_armature.animation_data_create()
if not glb_armature.animation_data.action:
    action = bpy.data.actions.new(name="CombinedAction")
    glb_armature.animation_data.action = action

# Obtener el rango de frames
if fbx_armature.animation_data and fbx_armature.animation_data.action:
    frame_start = int(fbx_armature.animation_data.action.frame_range[0])
    frame_end = int(fbx_armature.animation_data.action.frame_range[1])
else:
    frame_start = 0
    frame_end = 73

print(f"Procesando frames {frame_start} a {frame_end}")

# Almacenar las rest poses
fbx_rest_poses = {}
glb_rest_poses = {}

# Obtener rest poses del FBX (en modo OBJECT, sin pose mode)
for fbx_bone_name in bone_mapping.keys():
    if fbx_bone_name in fbx_armature.data.bones:
        bone = fbx_armature.data.bones[fbx_bone_name]
        # Rest pose en armature space
        fbx_rest_poses[fbx_bone_name] = bone.matrix_local.copy()

# Obtener rest poses del GLB
for glb_bone_name in bone_mapping.values():
    if glb_bone_name in glb_armature.data.bones:
        bone = glb_armature.data.bones[glb_bone_name]
        glb_rest_poses[glb_bone_name] = bone.matrix_local.copy()

print("\nCopiando animación de brazos...")
keyframes_inserted = 0
fcurves_created = 0

# Procesar cada frame
for frame in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame)
    
    for fbx_bone_name, glb_bone_name in bone_mapping.items():
        if fbx_bone_name not in fbx_armature.pose.bones:
            continue
        if glb_bone_name not in glb_armature.pose.bones:
            continue
        
        fbx_pose_bone = fbx_armature.pose.bones[fbx_bone_name]
        glb_pose_bone = glb_armature.pose.bones[glb_bone_name]
        
        # Obtener la matriz de pose del FBX en armature space
        fbx_pose_matrix = fbx_pose_bone.matrix
        
        # Obtener la transformación relativa al rest pose del FBX
        # pose_matrix = rest_matrix @ offset_matrix
        # offset_matrix = rest_matrix^-1 @ pose_matrix
        fbx_rest_matrix = fbx_rest_poses[fbx_bone_name]
        fbx_offset_matrix = fbx_rest_matrix.inverted() @ fbx_pose_matrix
        
        # Aplicar la misma transformación relativa al rest pose del GLB
        glb_rest_matrix = glb_rest_poses[glb_bone_name]
        glb_target_matrix = glb_rest_matrix @ fbx_offset_matrix
        
        # Convertir a espacio local (considerando el parent)
        if glb_pose_bone.parent:
            parent_matrix = glb_pose_bone.parent.matrix
            glb_local_matrix = parent_matrix.inverted() @ glb_target_matrix
        else:
            glb_local_matrix = glb_target_matrix
        
        # Descomponer en loc, rot, scale
        loc, rot, scale = glb_local_matrix.decompose()
        
        # Aplicar transformación
        glb_pose_bone.location = loc
        glb_pose_bone.rotation_quaternion = rot
        glb_pose_bone.scale = scale
        
        # Insertar keyframes
        glb_pose_bone.keyframe_insert(data_path="location", frame=frame)
        glb_pose_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
        glb_pose_bone.keyframe_insert(data_path="scale", frame=frame)
        keyframes_inserted += 3

# Contar FCurves creadas
if glb_armature.animation_data and glb_armature.animation_data.action:
    fcurves_created = len(glb_armature.animation_data.action.fcurves)

print(f"\n✓ Frames procesados: {frame_end - frame_start + 1}")
print(f"✓ Keyframes insertados: {keyframes_inserted}")
print(f"✓ FCurves creadas: {fcurves_created}")

# Limpiar objetos FBX
print("\nLimpiando objetos FBX...")
bpy.ops.object.select_all(action='DESELECT')
objects_to_remove = [obj for obj in fbx_objects]
for obj in objects_to_remove:
    obj.select_set(True)
bpy.ops.object.delete()
print(f"✓ {len(objects_to_remove)} objetos FBX eliminados")

# Guardar archivo
output_path.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(output_path))
print(f"\n✓ Archivo guardado: {output_path}")
print("\n¡COMPLETADO! Abre el archivo en Blender para verificar la animación.")
