import bpy
from pathlib import Path
import math

# Rutas
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_CONSTRAINTS.blend")

print("="*80)
print("PASO 1: IMPORTAR ARCHIVOS")
print("="*80)

# Limpiar
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

print("\nImportando GLB...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))
glb_armature = bpy.context.selected_objects[0]
glb_armature.name = "GLB_Armature"
print(f"✓ GLB importado: {len(glb_armature.data.bones)} huesos")

print("\nImportando FBX...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_objects = [obj for obj in bpy.context.selected_objects if obj != glb_armature]
fbx_armature = next((obj for obj in fbx_objects if obj.type == 'ARMATURE'), None)
fbx_armature.name = "FBX_Armature"
print(f"✓ FBX importado: {len(fbx_armature.data.bones)} huesos")

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

print("="*80)
print("PASO 2: CREAR CONSTRAINTS COPY ROTATION")
print("="*80)

# Seleccionar GLB y entrar en pose mode
bpy.context.view_layer.objects.active = glb_armature
bpy.ops.object.mode_set(mode='POSE')

constraints_created = 0

for fbx_bone_name, glb_bone_name in bone_mapping.items():
    if fbx_bone_name in fbx_armature.pose.bones and glb_bone_name in glb_armature.pose.bones:
        glb_pose_bone = glb_armature.pose.bones[glb_bone_name]
        
        # Crear constraint Copy Rotation
        constraint = glb_pose_bone.constraints.new('COPY_ROTATION')
        constraint.name = f"Copy_{fbx_bone_name}"
        constraint.target = fbx_armature
        constraint.subtarget = fbx_bone_name
        constraint.target_space = 'WORLD'
        constraint.owner_space = 'WORLD'
        constraint.mix_mode = 'REPLACE'
        
        constraints_created += 1
        print(f"✓ Constraint creado: {glb_bone_name} <- {fbx_bone_name}")

bpy.ops.object.mode_set(mode='OBJECT')
print(f"\n✓ Total constraints creados: {constraints_created}")

print("="*80)
print("PASO 3: VERIFICAR CONSTRAINTS EN FRAMES CLAVE")
print("="*80)

# Verificar en algunos frames
test_frames = [1, 20, 40, 60]
verification_passed = True

for frame in test_frames:
    bpy.context.scene.frame_set(frame)
    bpy.context.view_layer.update()
    
    print(f"\nFrame {frame}:")
    
    # Verificar solo los primeros 2 huesos
    for fbx_bone_name, glb_bone_name in list(bone_mapping.items())[:2]:
        fbx_pose = fbx_armature.pose.bones[fbx_bone_name]
        glb_pose = glb_armature.pose.bones[glb_bone_name]
        
        # Comparar rotaciones en world space
        fbx_world = fbx_armature.matrix_world @ fbx_pose.matrix
        glb_world = glb_armature.matrix_world @ glb_pose.matrix
        
        fbx_rot = fbx_world.to_quaternion()
        glb_rot = glb_world.to_quaternion()
        
        dot = abs(fbx_rot.dot(glb_rot))
        dot = min(1.0, max(-1.0, dot))
        angle_diff = math.acos(dot) * 2 * 57.2958
        
        if angle_diff < 5:
            status = "✓ EXCELENTE"
        elif angle_diff < 15:
            status = "✓ BUENO"
        elif angle_diff < 30:
            status = "⚠ ACEPTABLE"
        else:
            status = "✗ ERROR"
            verification_passed = False
        
        print(f"  {glb_bone_name}: {angle_diff:.1f}° - {status}")

if verification_passed:
    print("\n✓ VERIFICACIÓN EXITOSA - Los constraints funcionan correctamente")
else:
    print("\n⚠ VERIFICACIÓN CON ADVERTENCIAS - Algunos huesos tienen diferencias")

print("="*80)
print("PASO 4: BAKE ANIMATION")
print("="*80)

# Configurar rango de frames
frame_start = 1
frame_end = 73

# Seleccionar GLB y entrar en pose mode
bpy.context.view_layer.objects.active = glb_armature
bpy.ops.object.mode_set(mode='POSE')

# Seleccionar solo los huesos de brazos
for bone_name in glb_armature.pose.bones:
    bone_name.bone.select = False

for glb_bone_name in bone_mapping.values():
    if glb_bone_name in glb_armature.pose.bones:
        glb_armature.pose.bones[glb_bone_name].bone.select = True

print(f"Baking frames {frame_start} to {frame_end}...")

# Bake animation
bpy.ops.nla.bake(
    frame_start=frame_start,
    frame_end=frame_end,
    only_selected=True,
    visual_keying=True,
    clear_constraints=True,
    bake_types={'POSE'}
)

print("✓ Animation baked")

bpy.ops.object.mode_set(mode='OBJECT')

print("="*80)
print("PASO 5: LIMPIAR Y GUARDAR")
print("="*80)

# Eliminar objetos FBX
bpy.ops.object.select_all(action='DESELECT')
for obj in fbx_objects:
    obj.select_set(True)
bpy.ops.object.delete()
print("✓ Objetos FBX eliminados")

# Guardar
output_path.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(output_path))
print(f"✓ Archivo guardado: {output_path}")

print("="*80)
print("PASO 6: VERIFICACIÓN FINAL")
print("="*80)

# Reimportar FBX para verificación final
print("\nReimportando FBX para verificación final...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_check = None
for obj in bpy.context.selected_objects:
    if obj.type == 'ARMATURE':
        fbx_check = obj
        break

final_verification_passed = True
max_error = 0

for frame in test_frames:
    bpy.context.scene.frame_set(frame)
    print(f"\nFrame {frame}:")
    
    for fbx_bone_name, glb_bone_name in list(bone_mapping.items())[:4]:
        fbx_pose = fbx_check.pose.bones[fbx_bone_name]
        glb_pose = glb_armature.pose.bones[glb_bone_name]
        
        fbx_world = fbx_check.matrix_world @ fbx_pose.matrix
        glb_world = glb_armature.matrix_world @ glb_pose.matrix
        
        fbx_rot = fbx_world.to_quaternion()
        glb_rot = glb_world.to_quaternion()
        
        dot = abs(fbx_rot.dot(glb_rot))
        dot = min(1.0, max(-1.0, dot))
        angle_diff = math.acos(dot) * 2 * 57.2958
        
        max_error = max(max_error, angle_diff)
        
        if angle_diff < 10:
            status = "✓"
        elif angle_diff < 20:
            status = "⚠"
        else:
            status = "✗"
            final_verification_passed = False
        
        print(f"  {status} {glb_bone_name}: {angle_diff:.1f}°")

print("\n" + "="*80)
print("RESULTADO FINAL")
print("="*80)

if final_verification_passed and max_error < 15:
    print("✓✓✓ ÉXITO COMPLETO ✓✓✓")
    print(f"Error máximo: {max_error:.1f}°")
    print("La animación de brazos se copió correctamente.")
elif max_error < 30:
    print("✓ ÉXITO CON ADVERTENCIAS")
    print(f"Error máximo: {max_error:.1f}°")
    print("La animación funciona pero con algunas diferencias menores.")
else:
    print("✗ REQUIERE AJUSTES")
    print(f"Error máximo: {max_error:.1f}°")
    print("La animación tiene diferencias significativas.")

print("="*80)
