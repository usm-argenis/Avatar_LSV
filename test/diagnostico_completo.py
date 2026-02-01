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
}

print("\n" + "="*80)
print("COMPARACIÓN DETALLADA DE ORIENTACIONES EN REST POSE")
print("="*80)

for fbx_bone_name, glb_bone_name in bone_mapping.items():
    fbx_bone = fbx_armature.data.bones[fbx_bone_name]
    glb_bone = glb_armature.data.bones[glb_bone_name]
    
    print(f"\n{fbx_bone_name} -> {glb_bone_name}")
    print(f"  FBX matrix_local:")
    for i, row in enumerate(fbx_bone.matrix_local):
        print(f"    [{i}] {row}")
    
    print(f"  GLB matrix_local:")
    for i, row in enumerate(glb_bone.matrix_local):
        print(f"    [{i}] {row}")
    
    # Extraer rotación del rest pose
    fbx_rest_rot = fbx_bone.matrix_local.to_quaternion()
    glb_rest_rot = glb_bone.matrix_local.to_quaternion()
    
    print(f"  FBX rest rotation: {fbx_rest_rot}")
    print(f"  GLB rest rotation: {glb_rest_rot}")

print("\n" + "="*80)
print("COMPARACIÓN FRAME POR FRAME (Frames 1, 20, 40)")
print("="*80)

for frame in [1, 20, 40]:
    bpy.context.scene.frame_set(frame)
    print(f"\n{'='*80}")
    print(f"FRAME {frame}")
    print(f"{'='*80}")
    
    for fbx_bone_name, glb_bone_name in bone_mapping.items():
        fbx_pose_bone = fbx_armature.pose.bones[fbx_bone_name]
        glb_pose_bone = glb_armature.pose.bones[fbx_bone_name]
        
        print(f"\n{fbx_bone_name}:")
        print(f"  FBX rotation_quaternion: {fbx_pose_bone.rotation_quaternion}")
        print(f"  FBX location: {fbx_pose_bone.location}")
        print(f"  FBX scale: {fbx_pose_bone.scale}")
        
        # Matriz pose en bone space local
        print(f"  FBX pose matrix (local):")
        for i, row in enumerate(fbx_pose_bone.matrix):
            print(f"    [{i}] {row}")
        
        # Calcular la matriz en world space
        fbx_world = fbx_armature.matrix_world @ fbx_pose_bone.matrix
        print(f"  FBX world position: {fbx_world.translation}")
        print(f"  FBX world rotation: {fbx_world.to_quaternion()}")
        print(f"  FBX world scale: {fbx_world.to_scale()}")

print("\n" + "="*80)
print("VERIFICAR SI HAY CONSTRAINTS O DRIVERS")
print("="*80)

for fbx_bone_name in bone_mapping.keys():
    fbx_pose_bone = fbx_armature.pose.bones[fbx_bone_name]
    
    if len(fbx_pose_bone.constraints) > 0:
        print(f"\n{fbx_bone_name} tiene {len(fbx_pose_bone.constraints)} constraints:")
        for const in fbx_pose_bone.constraints:
            print(f"  - {const.name} ({const.type})")
    
    # Verificar si hay drivers
    if fbx_armature.animation_data:
        for driver in fbx_armature.animation_data.drivers:
            if fbx_bone_name in driver.data_path:
                print(f"  - Driver en: {driver.data_path}")

print("\n" + "="*80)
print("ANÁLISIS COMPLETADO")
print("="*80)
