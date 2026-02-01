import bpy
import mathutils
from pathlib import Path
import math

# Rutas
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_world_space.blend")

# Limpiar
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

print("Importando GLB...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))
glb_armature = bpy.context.selected_objects[0]
glb_armature.name = "GLB_Armature"

print("\nImportando FBX...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_objects = [obj for obj in bpy.context.selected_objects if obj != glb_armature]
fbx_armature = next((obj for obj in fbx_objects if obj.type == 'ARMATURE'), None)
fbx_armature.name = "FBX_Armature"

# Ajustar escala del FBX para que coincida con GLB
# El ratio es 0.0123 (GLB es ~81 veces más pequeño)
scale_factor = 0.0123
fbx_armature.scale = (scale_factor, scale_factor, scale_factor)
bpy.context.view_layer.update()

print(f"FBX escalado por factor: {scale_factor}")

# Mapeo
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

# Configurar acción
if not glb_armature.animation_data:
    glb_armature.animation_data_create()
if not glb_armature.animation_data.action:
    action = bpy.data.actions.new(name="CombinedAction")
    glb_armature.animation_data.action = action

frame_start = 1
frame_end = 73

print(f"Procesando frames {frame_start} a {frame_end}")
print("\nCopiando posiciones WORLD SPACE directas...")

keyframes_inserted = 0

# Procesar cada frame
for frame in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame)
    
    for fbx_bone_name, glb_bone_name in bone_mapping.items():
        fbx_pose_bone = fbx_armature.pose.bones[fbx_bone_name]
        glb_pose_bone = glb_armature.pose.bones[glb_bone_name]
        
        # Obtener matriz en WORLD SPACE del FBX
        fbx_world_matrix = fbx_armature.matrix_world @ fbx_pose_bone.matrix
        
        # Convertir directamente a local space del GLB
        # Primero, necesitamos la matriz en el espacio del armature GLB
        glb_armature_space_matrix = glb_armature.matrix_world.inverted() @ fbx_world_matrix
        
        # Ahora convertir a local space del hueso (considerando el parent)
        if glb_pose_bone.parent:
            glb_parent_armature_space = glb_pose_bone.parent.matrix
            glb_local_matrix = glb_parent_armature_space.inverted() @ glb_armature_space_matrix
        else:
            glb_local_matrix = glb_armature_space_matrix
        
        # Descomponer
        loc, rot, scale = glb_local_matrix.decompose()
        
        # Aplicar
        glb_pose_bone.rotation_mode = 'QUATERNION'
        glb_pose_bone.location = loc
        glb_pose_bone.rotation_quaternion = rot
        glb_pose_bone.scale = scale
        
        # Keyframes
        glb_pose_bone.keyframe_insert(data_path="location", frame=frame)
        glb_pose_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
        glb_pose_bone.keyframe_insert(data_path="scale", frame=frame)
        keyframes_inserted += 3

fcurves_created = len(glb_armature.animation_data.action.fcurves)

print(f"\n✓ Frames procesados: {frame_end - frame_start + 1}")
print(f"✓ Keyframes insertados: {keyframes_inserted}")
print(f"✓ FCurves creadas: {fcurves_created}")

# Limpiar
print("\nLimpiando objetos FBX...")
bpy.ops.object.select_all(action='DESELECT')
for obj in fbx_objects:
    obj.select_set(True)
bpy.ops.object.delete()

# Guardar
output_path.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(output_path))
print(f"\n✓ Archivo guardado: {output_path}")

# VERIFICACIÓN
print("\n" + "="*80)
print("VERIFICACIÓN CON FBX ESCALADO")
print("="*80)

# Reimportar y escalar FBX
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_check = None
for obj in bpy.context.selected_objects:
    if obj.type == 'ARMATURE':
        fbx_check = obj
        break

fbx_check.scale = (scale_factor, scale_factor, scale_factor)
bpy.context.view_layer.update()

test_frames = [1, 20, 40, 60]
test_bones = list(bone_mapping.items())[:2]

for frame in test_frames:
    bpy.context.scene.frame_set(frame)
    print(f"\nFrame {frame}:")
    
    for fbx_bone_name, glb_bone_name in test_bones:
        fbx_pose = fbx_check.pose.bones[fbx_bone_name]
        glb_pose = glb_armature.pose.bones[glb_bone_name]
        
        fbx_world = fbx_check.matrix_world @ fbx_pose.matrix
        glb_world = glb_armature.matrix_world @ glb_pose.matrix
        
        fbx_rot = fbx_world.to_quaternion()
        glb_rot = glb_world.to_quaternion()
        
        dot = abs(fbx_rot.dot(glb_rot))
        dot = min(1.0, max(-1.0, dot))
        angle_diff = math.acos(dot) * 2 * 57.2958
        
        status = "✓" if angle_diff < 15 else ("⚠" if angle_diff < 30 else "✗")
        print(f"  {status} {glb_bone_name}: {angle_diff:.1f}°")

print("\n" + "="*80)
print("¡COMPLETADO!")
print("="*80)
