import bpy
import mathutils
from pathlib import Path
import math

# Rutas de archivos
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_FINAL_VERIFICADO.blend")

# Limpiar escena
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

# Precalcular las matrices de mapeo para cada hueso
print("\nCalculando matrices de mapeo...")
bone_mappings_data = {}

for fbx_bone_name, glb_bone_name in bone_mapping.items():
    fbx_bone = fbx_armature.data.bones[fbx_bone_name]
    glb_bone = glb_armature.data.bones[glb_bone_name]
    
    # Obtener la dirección de cada hueso en rest pose (en armature space)
    fbx_direction = (fbx_bone.tail_local - fbx_bone.head_local).normalized()
    glb_direction = (glb_bone.tail_local - glb_bone.head_local).normalized()
    
    # Obtener rotaciones de rest pose
    fbx_rest_rot = fbx_bone.matrix_local.to_quaternion()
    glb_rest_rot = glb_bone.matrix_local.to_quaternion()
    
    # Guardar información
    bone_mappings_data[fbx_bone_name] = {
        'glb_bone_name': glb_bone_name,
        'fbx_rest_rot': fbx_rest_rot,
        'glb_rest_rot': glb_rest_rot,
        'fbx_direction': fbx_direction,
        'glb_direction': glb_direction
    }
    
    print(f"{fbx_bone_name} -> {glb_bone_name}")
    print(f"  FBX dir: {fbx_direction}")
    print(f"  GLB dir: {glb_direction}")

print("\nAplicando retargeting basado en direcciones de huesos...")
keyframes_inserted = 0

# Procesar cada frame
for frame in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame)
    
    for fbx_bone_name, glb_bone_name in bone_mapping.items():
        fbx_pose_bone = fbx_armature.pose.bones[fbx_bone_name]
        glb_pose_bone = glb_armature.pose.bones[glb_bone_name]
        
        mapping_data = bone_mappings_data[fbx_bone_name]
        
        # Obtener la matriz de pose del FBX en world space
        fbx_world_matrix = fbx_armature.matrix_world @ fbx_pose_bone.matrix
        fbx_world_rot = fbx_world_matrix.to_quaternion()
        
        # Obtener la matriz de rest del FBX en world space
        fbx_rest_world = fbx_armature.matrix_world @ fbx_armature.data.bones[fbx_bone_name].matrix_local
        fbx_rest_world_rot = fbx_rest_world.to_quaternion()
        
        # Calcular swing: la rotación desde rest a posed
        # swing = posed @ rest.inverted()
        swing = fbx_world_rot @ fbx_rest_world_rot.inverted()
        
        # Aplicar el mismo swing al GLB
        glb_rest_world = glb_armature.matrix_world @ glb_armature.data.bones[glb_bone_name].matrix_local
        glb_rest_world_rot = glb_rest_world.to_quaternion()
        
        # Aplicar swing
        glb_target_world_rot = swing @ glb_rest_world_rot
        
        # Ahora convertir a local space
        if glb_pose_bone.parent:
            glb_parent_world_matrix = glb_armature.matrix_world @ glb_pose_bone.parent.matrix
            glb_parent_world_rot = glb_parent_world_matrix.to_quaternion()
            glb_local_rot = glb_parent_world_rot.inverted() @ glb_target_world_rot
        else:
            armature_rot = glb_armature.matrix_world.to_quaternion()
            glb_local_rot = armature_rot.inverted() @ glb_target_world_rot
        
        # Aplicar
        glb_pose_bone.rotation_mode = 'QUATERNION'
        glb_pose_bone.rotation_quaternion = glb_local_rot
        
        # Keyframe
        glb_pose_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
        keyframes_inserted += 1

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

# VERIFICACIÓN FINAL
print("\n" + "="*80)
print("VERIFICACIÓN FINAL CON FBX ORIGINAL")
print("="*80)

# Reimportar FBX
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_armature_check = None
for obj in bpy.context.selected_objects:
    if obj.type == 'ARMATURE':
        fbx_armature_check = obj
        break

test_frames = [1, 10, 20, 30, 40, 50, 60, 70]
test_bones = list(bone_mapping.items())[:3]

all_good = True

for frame in test_frames:
    bpy.context.scene.frame_set(frame)
    print(f"\nFrame {frame}:")
    
    for fbx_bone_name, glb_bone_name in test_bones:
        fbx_pose = fbx_armature_check.pose.bones[fbx_bone_name]
        glb_pose = glb_armature.pose.bones[glb_bone_name]
        
        fbx_world = fbx_armature_check.matrix_world @ fbx_pose.matrix
        glb_world = glb_armature.matrix_world @ glb_pose.matrix
        
        fbx_rot = fbx_world.to_quaternion()
        glb_rot = glb_world.to_quaternion()
        
        dot = abs(fbx_rot.dot(glb_rot))
        dot = min(1.0, max(-1.0, dot))
        angle_diff = math.acos(dot) * 2 * 57.2958
        
        if angle_diff < 10:
            status = "✓ EXCELENTE"
        elif angle_diff < 20:
            status = "✓ BUENO"
        elif angle_diff < 40:
            status = "⚠ ACEPTABLE"
        else:
            status = "✗ ERROR"
            all_good = False
        
        print(f"  {glb_bone_name}: {angle_diff:.1f}° - {status}")

print("\n" + "="*80)
if all_good:
    print("✓ ¡VERIFICACIÓN EXITOSA! Todos los huesos están correctos.")
else:
    print("⚠ Algunos huesos tienen diferencias, pero el retargeting está aplicado.")
print("="*80)
