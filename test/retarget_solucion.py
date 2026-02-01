import bpy
import mathutils
from pathlib import Path
import math

# Rutas de archivos
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_SOLUCION.blend")

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

print("Importando GLB...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))
glb_armature = bpy.context.selected_objects[0]
glb_armature.name = "GLB_Armature"
print(f"GLB importado: {glb_armature.name}")

print("\nImportando FBX...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_objects = [obj for obj in bpy.context.selected_objects if obj != glb_armature]
fbx_armature = next((obj for obj in fbx_objects if obj.type == 'ARMATURE'), None)
fbx_armature.name = "FBX_Armature"
print(f"FBX importado: {fbx_armature.name}")

# Mapeo de huesos
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

# Asegurar acción
if not glb_armature.animation_data:
    glb_armature.animation_data_create()
if not glb_armature.animation_data.action:
    action = bpy.data.actions.new(name="CombinedAction")
    glb_armature.animation_data.action = action

# Obtener rango de frames
if fbx_armature.animation_data and fbx_armature.animation_data.action:
    frame_start = int(fbx_armature.animation_data.action.frame_range[0])
    frame_end = int(fbx_armature.animation_data.action.frame_range[1])
else:
    frame_start = 1
    frame_end = 73

print(f"Procesando frames {frame_start} a {frame_end}")

print("\nRetargeting con transformación swing-twist...")
keyframes_inserted = 0

# Procesar cada frame
for frame in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame)
    
    for fbx_bone_name, glb_bone_name in bone_mapping.items():
        fbx_pose_bone = fbx_armature.pose.bones[fbx_bone_name]
        glb_pose_bone = glb_armature.pose.bones[glb_bone_name]
        fbx_bone = fbx_armature.data.bones[fbx_bone_name]
        glb_bone = glb_armature.data.bones[glb_bone_name]
        
        # Obtener la matriz de pose del FBX en world space
        fbx_world_matrix = fbx_armature.matrix_world @ fbx_pose_bone.matrix
        
        # Obtener la matriz rest del FBX en world space
        fbx_rest_world = fbx_armature.matrix_world @ fbx_bone.matrix_local
        
        # Calcular la rotación relativa: rest -> posed
        # posed = rest @ rotation_offset
        # rotation_offset = rest.inverted() @ posed
        fbx_rotation_offset_matrix = fbx_rest_world.inverted() @ fbx_world_matrix
        
        # Ahora aplicar la misma rotación relativa al GLB
        # Obtener rest del GLB en world space
        glb_rest_world = glb_armature.matrix_world @ glb_bone.matrix_local
        
        # Aplicar el offset de rotación
        glb_target_world = glb_rest_world @ fbx_rotation_offset_matrix
        
        # Convertir a local space del hueso GLB
        if glb_pose_bone.parent:
            # Obtener la matriz del parent en world space
            glb_parent_world = glb_armature.matrix_world @ glb_pose_bone.parent.matrix
            glb_local_matrix = glb_parent_world.inverted() @ glb_target_world
        else:
            # Sin parent, convertir desde world a armature space
            glb_local_matrix = glb_armature.matrix_world.inverted() @ glb_target_world
        
        # Descomponer y aplicar
        loc, rot, scale = glb_local_matrix.decompose()
        
        glb_pose_bone.rotation_mode = 'QUATERNION'
        glb_pose_bone.rotation_quaternion = rot
        glb_pose_bone.location = loc
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

# Limpiar FBX
print("\nLimpiando objetos FBX...")
bpy.ops.object.select_all(action='DESELECT')
for obj in fbx_objects:
    obj.select_set(True)
bpy.ops.object.delete()
print(f"✓ Objetos FBX eliminados")

# Guardar
output_path.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(output_path))
print(f"\n✓ Archivo guardado: {output_path}")

# VERIFICACIÓN
print("\n" + "="*80)
print("VERIFICACIÓN INTEGRADA")
print("="*80)

# Reimportar FBX para verificar
print("\nReimportando FBX para verificar...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_objects_verify = [obj for obj in bpy.context.selected_objects]
fbx_armature_verify = next((obj for obj in fbx_objects_verify if obj.type == 'ARMATURE'), None)

test_frames = [1, 20, 40, 60]
bones_to_test = list(bone_mapping.items())[:2]

for frame in test_frames:
    bpy.context.scene.frame_set(frame)
    print(f"\nFrame {frame}:")
    
    for fbx_bone_name, glb_bone_name in bones_to_test:
        fbx_pose = fbx_armature_verify.pose.bones[fbx_bone_name]
        glb_pose = glb_armature.pose.bones[glb_bone_name]
        
        fbx_world = fbx_armature_verify.matrix_world @ fbx_pose.matrix
        glb_world = glb_armature.matrix_world @ glb_pose.matrix
        
        fbx_rot = fbx_world.to_quaternion()
        glb_rot = glb_world.to_quaternion()
        
        dot = abs(fbx_rot.dot(glb_rot))
        dot = min(1.0, max(-1.0, dot))
        angle_diff = math.acos(dot) * 2 * 57.2958
        
        status = "✓" if angle_diff < 15 else "✗"
        print(f"  {status} {glb_bone_name}: {angle_diff:.1f}°")

print("\n" + "="*80)
print("¡COMPLETADO!")
print("="*80)
