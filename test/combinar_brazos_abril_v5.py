import bpy
import mathutils
from pathlib import Path

# Rutas de archivos
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_combinado_v5.blend")

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

# Primero, analizar las orientaciones de rest pose
print("\nAnalizando orientaciones de rest pose...")
for fbx_bone_name, glb_bone_name in bone_mapping.items():
    if fbx_bone_name in fbx_armature.data.bones and glb_bone_name in glb_armature.data.bones:
        fbx_bone = fbx_armature.data.bones[fbx_bone_name]
        glb_bone = glb_armature.data.bones[glb_bone_name]
        
        # Obtener las direcciones de los huesos en rest pose
        fbx_head = fbx_bone.head_local
        fbx_tail = fbx_bone.tail_local
        fbx_dir = (fbx_tail - fbx_head).normalized()
        
        glb_head = glb_bone.head_local
        glb_tail = glb_bone.tail_local
        glb_dir = (glb_tail - glb_head).normalized()
        
        print(f"{fbx_bone_name} -> {glb_bone_name}")
        print(f"  FBX dir: {fbx_dir}")
        print(f"  GLB dir: {glb_dir}")

print("\nCopiando animación de brazos con retargeting...")
keyframes_inserted = 0

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
        
        # Obtener la matriz de pose completa en world space
        fbx_world_matrix = fbx_armature.matrix_world @ fbx_pose_bone.matrix
        
        # Obtener solo la rotación del FBX
        fbx_world_rot = fbx_world_matrix.to_quaternion()
        
        # Convertir a espacio local del GLB
        if glb_pose_bone.parent:
            # Obtener matriz del padre en world space
            parent_world_matrix = glb_armature.matrix_world @ glb_pose_bone.parent.matrix
            parent_world_rot = parent_world_matrix.to_quaternion()
            
            # Rotar desde world space al parent space
            local_rot = parent_world_rot.inverted() @ fbx_world_rot
        else:
            # Sin padre, convertir desde world space a armature space
            armature_rot = glb_armature.matrix_world.to_quaternion()
            local_rot = armature_rot.inverted() @ fbx_world_rot
        
        # Aplicar solo la rotación
        glb_pose_bone.rotation_mode = 'QUATERNION'
        glb_pose_bone.rotation_quaternion = local_rot
        
        # Insertar keyframe solo para rotación
        glb_pose_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
        keyframes_inserted += 1

# Contar FCurves creadas
fcurves_created = 0
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
