import bpy
from pathlib import Path

# Abrir el archivo que creamos
result_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_CONSTRAINTS.blend")
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")

print("="*80)
print("DIAGNÓSTICO VISUAL DEL RESULTADO")
print("="*80)

bpy.ops.wm.open_mainfile(filepath=str(result_path))

# Encontrar el armature
glb_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        glb_armature = obj
        break

print(f"\nArmature encontrado: {glb_armature.name}")
print(f"Número de huesos: {len(glb_armature.data.bones)}")

# Verificar si tiene animación
if glb_armature.animation_data and glb_armature.animation_data.action:
    action = glb_armature.animation_data.action
    print(f"\nAcción: {action.name}")
    print(f"Frame range: {action.frame_range[0]} - {action.frame_range[1]}")
    print(f"FCurves: {len(action.fcurves)}")
    
    # Listar las FCurves
    arm_fcurves = [fc for fc in action.fcurves if 'Arm' in fc.data_path or 'Shoulder' in fc.data_path]
    print(f"\nFCurves de brazos: {len(arm_fcurves)}")
    for fc in arm_fcurves[:10]:  # Mostrar primeras 10
        print(f"  - {fc.data_path} [{fc.array_index}]")
else:
    print("\n✗ NO HAY ANIMACIÓN")

# Ahora importar el FBX original lado a lado
print("\n" + "="*80)
print("IMPORTANDO FBX PARA COMPARACIÓN VISUAL")
print("="*80)

bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_armature = None
for obj in bpy.context.selected_objects:
    if obj.type == 'ARMATURE':
        fbx_armature = obj
        break

# Mover el FBX a un lado
fbx_armature.location.x = 2.0  # 2 unidades a la derecha

print(f"\nFBX importado: {fbx_armature.name}")
print(f"Posición FBX: {fbx_armature.location}")

# Comparar en frame 30 (mitad de la animación)
frame_test = 30
bpy.context.scene.frame_set(frame_test)
bpy.context.view_layer.update()

print(f"\n" + "="*80)
print(f"COMPARACIÓN EN FRAME {frame_test}")
print("="*80)

bones_to_check = ['LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand']
fbx_bones_to_check = ['Bip001 L Clavicle', 'Bip001 L UpperArm', 'Bip001 L Forearm', 'Bip001 L Hand']

for i, (glb_bone, fbx_bone) in enumerate(zip(bones_to_check, fbx_bones_to_check)):
    if glb_bone in glb_armature.pose.bones and fbx_bone in fbx_armature.pose.bones:
        glb_pose = glb_armature.pose.bones[glb_bone]
        fbx_pose = fbx_armature.pose.bones[fbx_bone]
        
        # Posiciones en world space
        glb_world_pos = glb_armature.matrix_world @ glb_pose.matrix @ glb_pose.bone.head_local
        fbx_world_pos = fbx_armature.matrix_world @ fbx_pose.matrix @ fbx_pose.bone.head_local
        
        # Rotaciones
        glb_rot = glb_pose.rotation_quaternion if glb_pose.rotation_mode == 'QUATERNION' else glb_pose.rotation_euler
        fbx_rot = fbx_pose.rotation_quaternion if fbx_pose.rotation_mode == 'QUATERNION' else fbx_pose.rotation_euler
        
        print(f"\n{glb_bone} / {fbx_bone}:")
        print(f"  GLB pos: {glb_world_pos}")
        print(f"  FBX pos: {fbx_world_pos}")
        print(f"  GLB rot: {glb_rot}")
        print(f"  FBX rot: {fbx_rot}")

# Guardar este archivo de comparación
comparison_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\COMPARACION_VISUAL.blend")
bpy.ops.wm.save_as_mainfile(filepath=str(comparison_path))

print("\n" + "="*80)
print("ARCHIVO DE COMPARACIÓN GUARDADO")
print("="*80)
print(f"Ubicación: {comparison_path}")
print("\nAbre este archivo en Blender para ver:")
print("- GLB a la izquierda (origen)")
print("- FBX a la derecha (2 unidades en X)")
print("- Reproduce la animación para comparar visualmente")
print("="*80)
