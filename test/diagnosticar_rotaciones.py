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

# Analizar algunos frames clave
frames_to_check = [1, 10, 20, 30, 40, 50, 60, 70]

print("\n" + "="*80)
print("DIAGNÓSTICO DE ROTACIONES")
print("="*80)

for frame in frames_to_check:
    bpy.context.scene.frame_set(frame)
    print(f"\n--- FRAME {frame} ---")
    
    # Solo verificar un hueso para simplificar: LeftArm
    fbx_bone_name = 'Bip001 L UpperArm'
    glb_bone_name = 'LeftArm'
    
    if fbx_bone_name in fbx_armature.pose.bones and glb_bone_name in glb_armature.pose.bones:
        fbx_pose_bone = fbx_armature.pose.bones[fbx_bone_name]
        glb_pose_bone = glb_armature.pose.bones[glb_bone_name]
        
        print(f"\n{fbx_bone_name} (FBX):")
        print(f"  Rotation mode: {fbx_pose_bone.rotation_mode}")
        
        if fbx_pose_bone.rotation_mode == 'QUATERNION':
            print(f"  Rotation (quat): {fbx_pose_bone.rotation_quaternion}")
        else:
            print(f"  Rotation (euler): {fbx_pose_bone.rotation_euler}")
        
        # Matriz en pose bone space (local)
        print(f"  Matrix (local):")
        for row in fbx_pose_bone.matrix:
            print(f"    {row}")
        
        # Matriz en armature space  
        print(f"  Matrix (armature space):")
        armature_matrix = fbx_armature.matrix_world @ fbx_pose_bone.matrix
        for row in armature_matrix:
            print(f"    {row}")
        
        print(f"\n{glb_bone_name} (GLB):")
        print(f"  Rotation mode: {glb_pose_bone.rotation_mode}")
        if glb_pose_bone.rotation_mode == 'QUATERNION':
            print(f"  Rotation (quat): {glb_pose_bone.rotation_quaternion}")
        else:
            print(f"  Rotation (euler): {glb_pose_bone.rotation_euler}")
        
        print(f"  Matrix (local):")
        for row in glb_pose_bone.matrix:
            print(f"    {row}")

# Verificar jerarquías
print("\n" + "="*80)
print("JERARQUÍA DE HUESOS")
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

print("\n" + "="*80)
print("DIAGNÓSTICO COMPLETADO")
print("="*80)
