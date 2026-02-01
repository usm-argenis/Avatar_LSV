import bpy
import mathutils
from pathlib import Path

# Rutas de archivos
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")

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

print("\n" + "="*80)
print("ANÁLISIS DE TAMAÑOS DE HUESOS")
print("="*80)

total_length_fbx = 0
total_length_glb = 0

for fbx_bone_name, glb_bone_name in bone_mapping.items():
    if fbx_bone_name in fbx_armature.data.bones and glb_bone_name in glb_armature.data.bones:
        fbx_bone = fbx_armature.data.bones[fbx_bone_name]
        glb_bone = glb_armature.data.bones[glb_bone_name]
        
        fbx_length = fbx_bone.length
        glb_length = glb_bone.length
        
        total_length_fbx += fbx_length
        total_length_glb += glb_length
        
        ratio = glb_length / fbx_length if fbx_length > 0 else 0
        
        print(f"\n{fbx_bone_name} -> {glb_bone_name}")
        print(f"  FBX length: {fbx_length:.4f}")
        print(f"  GLB length: {glb_length:.4f}")
        print(f"  Ratio (GLB/FBX): {ratio:.4f}")

scale_factor = total_length_glb / total_length_fbx if total_length_fbx > 0 else 1.0

print(f"\n" + "="*80)
print(f"TOTAL FBX: {total_length_fbx:.4f}")
print(f"TOTAL GLB: {total_length_glb:.4f}")
print(f"FACTOR DE ESCALA: {scale_factor:.4f}")
print("="*80)

print("\n" + "="*80)
print("ANÁLISIS DE JERARQUÍA")
print("="*80)

for fbx_bone_name, glb_bone_name in bone_mapping.items():
    if fbx_bone_name in fbx_armature.data.bones and glb_bone_name in glb_armature.data.bones:
        fbx_bone = fbx_armature.data.bones[fbx_bone_name]
        glb_bone = glb_armature.data.bones[glb_bone_name]
        
        fbx_parent = fbx_bone.parent.name if fbx_bone.parent else "None"
        glb_parent = glb_bone.parent.name if glb_bone.parent else "None"
        
        print(f"\n{fbx_bone_name} -> {glb_bone_name}")
        print(f"  FBX parent: {fbx_parent}")
        print(f"  GLB parent: {glb_parent}")
        print(f"  FBX head: {fbx_bone.head_local}")
        print(f"  FBX tail: {fbx_bone.tail_local}")
        print(f"  GLB head: {glb_bone.head_local}")
        print(f"  GLB tail: {glb_bone.tail_local}")

print("\n" + "="*80)
print("ANÁLISIS DE TRANSFORMACIONES EN FRAME 30")
print("="*80)

bpy.context.scene.frame_set(30)

for fbx_bone_name, glb_bone_name in list(bone_mapping.items())[:2]:  # Solo primeros 2
    if fbx_bone_name in fbx_armature.pose.bones:
        fbx_pose_bone = fbx_armature.pose.bones[fbx_bone_name]
        
        print(f"\n{fbx_bone_name}:")
        print(f"  Location: {fbx_pose_bone.location}")
        print(f"  Rotation mode: {fbx_pose_bone.rotation_mode}")
        
        if fbx_pose_bone.rotation_mode == 'QUATERNION':
            print(f"  Rotation (quat): {fbx_pose_bone.rotation_quaternion}")
        elif fbx_pose_bone.rotation_mode == 'XYZ':
            print(f"  Rotation (euler): {fbx_pose_bone.rotation_euler}")
        
        print(f"  Scale: {fbx_pose_bone.scale}")
        
        # Matriz en world space
        world_matrix = fbx_armature.matrix_world @ fbx_pose_bone.matrix
        print(f"  World position: {world_matrix.translation}")
        print(f"  World rotation (quat): {world_matrix.to_quaternion()}")

print("\n" + "="*80)
print("ANÁLISIS COMPLETADO")
print("="*80)
