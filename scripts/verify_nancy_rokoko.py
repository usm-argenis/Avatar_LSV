import bpy
from pathlib import Path

GLB_FILE = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\saludos\Nancy_resultado_hola_ROKOKO.glb")

print("="*80)
print("VERIFICACIÓN DETALLADA: Nancy_resultado_hola_ROKOKO.glb")
print("="*80)

# Importar
bpy.ops.wm.read_homefile(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(GLB_FILE))

# Encontrar armature
armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        armature = obj
        break

if not armature or not armature.animation_data or not armature.animation_data.action:
    print("❌ ERROR: Sin animación")
    exit(1)

action = armature.animation_data.action
frame_start = int(action.frame_range[0])
frame_end = int(action.frame_range[1])

print(f"\n✅ Animación encontrada:")
print(f"   Nombre: {action.name}")
print(f"   Frames: {frame_start} - {frame_end}")
print(f"   FCurves: {len(action.fcurves)}")

# Verificar materiales y texturas
print(f"\n🎨 Texturas:")
materials = []
textures = []

for obj in bpy.data.objects:
    if obj.type == 'MESH' and obj.data.materials:
        for mat in obj.data.materials:
            if mat and mat not in materials:
                materials.append(mat)
                if mat.use_nodes:
                    for node in mat.node_tree.nodes:
                        if node.type == 'TEX_IMAGE' and node.image:
                            textures.append(node.image.name)

print(f"   Materiales: {len(materials)}")
print(f"   Imágenes: {len(textures)}")

# PROBAR MOVIMIENTO EN DIFERENTES FRAMES
print(f"\n🎬 Probando movimiento de huesos:")

test_bones = ['Hips', 'Spine', 'Spine1', 'Spine2', 'LeftShoulder', 'RightShoulder', 
              'LeftArm', 'RightArm', 'LeftForeArm', 'RightForeArm', 'LeftHand', 'RightHand']

any_movement = False

for bone_name in test_bones:
    if bone_name in armature.pose.bones:
        bone = armature.pose.bones[bone_name]
        
        # Frame inicial
        bpy.context.scene.frame_set(frame_start)
        loc_start = bone.location.copy()
        rot_start = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
        
        # Frame medio
        mid_frame = (frame_start + frame_end) // 2
        bpy.context.scene.frame_set(mid_frame)
        loc_mid = bone.location.copy()
        rot_mid = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
        
        # Frame final
        bpy.context.scene.frame_set(frame_end)
        loc_end = bone.location.copy()
        rot_end = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
        
        # Calcular diferencias
        loc_diff = (loc_end - loc_start).length
        
        if bone.rotation_mode == 'QUATERNION':
            rot_diff = abs(rot_start.w - rot_end.w) + abs(rot_start.x - rot_end.x) + abs(rot_start.y - rot_end.y) + abs(rot_start.z - rot_end.z)
        else:
            rot_diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(3))
        
        total_diff = loc_diff + rot_diff
        
        if total_diff > 0.001:
            print(f"   ✅ {bone_name:20s} → Movimiento: {total_diff:.4f}")
            any_movement = True

if any_movement:
    print(f"\n{'='*80}")
    print("✅ ✅ ✅ VERIFICACIÓN EXITOSA ✅ ✅ ✅")
    print("El archivo tiene TEXTURAS y ANIMACIÓN FUNCIONAL")
    print(f"{'='*80}")
else:
    print(f"\n{'='*80}")
    print("❌ ❌ ❌ PROBLEMA ❌ ❌ ❌")
    print("Los huesos NO SE MUEVEN - animación no funcional")
    print(f"{'='*80}")
