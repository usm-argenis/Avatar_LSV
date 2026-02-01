import bpy
from pathlib import Path

# Rutas
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_CORRECTO.blend")

# Limpiar
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

print("Importando archivos...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))
glb_armature = bpy.context.selected_objects[0]
glb_armature.name = "GLB"

bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_objects = [obj for obj in bpy.context.selected_objects if obj != glb_armature]
fbx_armature = next((obj for obj in fbx_objects if obj.type == 'ARMATURE'), None)
fbx_armature.name = "FBX"

# MÉTODO: Copiar directamente los keyframes frame por frame
# pero aplicar en POSE SPACE (bone space local)

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

# Asegurar acción en GLB
if not glb_armature.animation_data:
    glb_armature.animation_data_create()
if not glb_armature.animation_data.action:
    action = bpy.data.actions.new(name="BrazosAction")
    glb_armature.animation_data.action = action

print("\nAnalizando animación FBX...")

# Ver qué tipo de rotación usa el FBX
fbx_sample_bone = fbx_armature.pose.bones['Bip001 L UpperArm']
print(f"FBX rotation mode: {fbx_sample_bone.rotation_mode}")

# Copiar frame por frame
frame_start = 1
frame_end = 73

print(f"\nCopiando {frame_end} frames...")
print("Usando POSE BONE space (copia directa de transformaciones locales)...")

for frame in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame)
    
    for fbx_bone_name, glb_bone_name in bone_mapping.items():
        fbx_bone = fbx_armature.pose.bones[fbx_bone_name]
        glb_bone = glb_armature.pose.bones[glb_bone_name]
        
        # Copiar DIRECTAMENTE las propiedades del pose bone
        # (esto es en bone local space, no world space)
        
        # Asegurar mismo modo de rotación
        glb_bone.rotation_mode = fbx_bone.rotation_mode
        
        # Copiar valores
        if fbx_bone.rotation_mode == 'QUATERNION':
            glb_bone.rotation_quaternion = fbx_bone.rotation_quaternion.copy()
            glb_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
        elif fbx_bone.rotation_mode in ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']:
            glb_bone.rotation_euler = fbx_bone.rotation_euler.copy()
            glb_bone.keyframe_insert(data_path="rotation_euler", frame=frame)
        
        # NO copiar location ni scale - solo rotación
        # glb_bone.location = fbx_bone.location.copy()
        # glb_bone.scale = fbx_bone.scale.copy()

print(f"✓ {frame_end} frames copiados")

# Verificar
print("\nVerificando en frames clave...")
import math

for test_frame in [1, 20, 40, 60]:
    bpy.context.scene.frame_set(test_frame)
    
    # Comparar solo rotaciones en local space
    fbx_bone = fbx_armature.pose.bones['Bip001 L UpperArm']
    glb_bone = glb_armature.pose.bones['LeftArm']
    
    if fbx_bone.rotation_mode == 'QUATERNION':
        fbx_rot = fbx_bone.rotation_quaternion
        glb_rot = glb_bone.rotation_quaternion
        
        # Comparar quaternions
        dot = abs(fbx_rot.dot(glb_rot))
        angle_diff = math.acos(min(1.0, max(-1.0, dot))) * 2 * 57.2958
        
        print(f"Frame {test_frame}: LeftArm diff = {angle_diff:.1f}°")

# Limpiar FBX
bpy.ops.object.select_all(action='DESELECT')
for obj in fbx_objects:
    obj.select_set(True)
bpy.ops.object.delete()

# Guardar
output_path.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(output_path))
print(f"\n✓ Guardado: {output_path}")

print("\nIMPORTANTE: Este método copia las rotaciones en BONE LOCAL SPACE.")
print("Si los rest poses son diferentes, el resultado será incorrecto.")
print("Abriendo archivo para verificación visual...")
