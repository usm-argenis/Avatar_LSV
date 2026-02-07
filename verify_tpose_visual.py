import bpy
from pathlib import Path

# Archivo a verificar
VERIFY_FILE = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\Duvall_TPose.glb")

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Cargar el archivo
print(f"Cargando {VERIFY_FILE}")
bpy.ops.import_scene.gltf(filepath=str(VERIFY_FILE))

# Buscar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if armature:
    # Activar el armature
    bpy.context.view_layer.objects.active = armature
    
    # Entrar en modo pose para ver la pose actual
    bpy.ops.object.mode_set(mode='POSE')
    
    print("\n=== POSE ACTUAL (debería estar en rest pose/neutral) ===")
    for bone_name in ['LeftArm', 'RightArm', 'LeftForeArm', 'RightForeArm']:
        if bone_name in armature.pose.bones:
            bone = armature.pose.bones[bone_name]
            print(f"{bone_name}:")
            print(f"  Rotation (Quat): {bone.rotation_quaternion}")
            print(f"  Location: {bone.location}")
    
    # Entrar en modo edit para ver la rest pose (posición real de los huesos)
    bpy.ops.object.mode_set(mode='EDIT')
    
    print("\n=== REST POSE (posición física de los huesos) ===")
    for bone_name in ['LeftArm', 'RightArm']:
        if bone_name in armature.data.edit_bones:
            bone = armature.data.edit_bones[bone_name]
            direction = (bone.tail - bone.head).normalized()
            print(f"{bone_name}:")
            print(f"  Head: {bone.head}")
            print(f"  Tail: {bone.tail}")
            print(f"  Direction: {direction}")
            print(f"  Length: {bone.length:.3f}")

print("\n¡Archivo cargado! Revisa visualmente en Blender.")
