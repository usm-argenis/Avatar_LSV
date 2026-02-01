import bpy
import mathutils
from pathlib import Path

# Rutas
result_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_retarget.blend")
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")

# Cargar el archivo resultante
bpy.ops.wm.open_mainfile(filepath=str(result_path))
result_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        result_armature = obj
        break

print(f"Armature encontrado: {result_armature.name}")

# Ahora importar el FBX para comparar
print("\nImportando FBX original...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_objects = [obj for obj in bpy.context.selected_objects]
fbx_armature = next((obj for obj in fbx_objects if obj.type == 'ARMATURE'), None)

bone_mapping = {
    'Bip001 L Clavicle': 'LeftShoulder',
    'Bip001 L UpperArm': 'LeftArm',
}

print("\n" + "="*80)
print("VERIFICACIÓN DE RESULTADOS - Frames clave")
print("="*80)

for frame in [1, 20, 40, 60]:
    bpy.context.scene.frame_set(frame)
    
    print(f"\n{'='*80}")
    print(f"FRAME {frame}")
    print(f"{'='*80}")
    
    for fbx_bone_name, glb_bone_name in bone_mapping.items():
        fbx_pose = fbx_armature.pose.bones[fbx_bone_name]
        glb_pose = result_armature.pose.bones[glb_bone_name]
        
        # Comparar en world space
        fbx_world_matrix = fbx_armature.matrix_world @ fbx_pose.matrix
        glb_world_matrix = result_armature.matrix_world @ glb_pose.matrix
        
        fbx_world_rot = fbx_world_matrix.to_quaternion()
        glb_world_rot = glb_world_matrix.to_quaternion()
        
        # Calcular diferencia angular
        import math
        dot_product = abs(fbx_world_rot.dot(glb_world_rot))
        dot_product = min(1.0, max(-1.0, dot_product))  # Clamp
        angle_diff = math.acos(dot_product) * 2 * 57.2958  # A grados
        
        print(f"\n{fbx_bone_name} -> {glb_bone_name}:")
        print(f"  FBX world rot: {fbx_world_rot}")
        print(f"  GLB world rot: {glb_world_rot}")
        print(f"  Diferencia angular: {angle_diff:.2f}°")
        
        if angle_diff < 5:
            print(f"  ✓ CORRECTO (< 5°)")
        elif angle_diff < 15:
            print(f"  ⚠ ACEPTABLE (< 15°)")
        else:
            print(f"  ✗ ERROR (> 15°)")

print("\n" + "="*80)
print("VERIFICACIÓN COMPLETADA")
print("="*80)
