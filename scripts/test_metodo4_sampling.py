"""
TEST FINAL - Método 4: Sample toda la animación explícitamente
"""

import bpy
import sys
from pathlib import Path

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output")
BLEND_DIR = BASE_DIR / "blend" / "cortesia"
TEST_BLEND = BLEND_DIR / "Nancy_a la orden.blend"

print("\n" + "="*80)
print("TEST FINAL - MÉTODO 4: SAMPLING EXPLÍCITO")
print("="*80)

# Cargar
bpy.ops.wm.open_mainfile(filepath=str(TEST_BLEND))

armature = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE'][0]
print(f"✅ Armature: {armature.name}")

if not armature.animation_data or not armature.animation_data.action:
    print("❌ No hay action")
    sys.exit(1)

original_action = armature.animation_data.action
frame_start, frame_end = original_action.frame_range
print(f"✅ Action: {original_action.name}")
print(f"   Frames: {frame_start:.0f} - {frame_end:.0f}")

# Configurar escena para exportación con sample
bpy.context.scene.frame_start = int(frame_start)
bpy.context.scene.frame_end = int(frame_end)
bpy.context.scene.frame_set(int(frame_start))

# Desactivar NLA
if armature.animation_data.use_nla:
    armature.animation_data.use_nla = False

# CRUCIAL: Exportar con force_sampling
print(f"\n📤 Exportando con FORCE SAMPLING...")

output_file = BLEND_DIR / "TEST_metodo4_sampling.glb"

bpy.ops.object.select_all(action='SELECT')

bpy.ops.export_scene.gltf(
    filepath=str(output_file),
    export_format='GLB',
    export_image_format='AUTO',
    export_texcoords=True,
    export_normals=True,
    export_draco_mesh_compression_enable=False,
    export_materials='EXPORT',
    export_cameras=False,
    use_selection=False,
    use_visible=True,
    use_renderable=True,
    use_active_collection=False,
    export_yup=True,
    export_apply=False,
    export_animations=True,
    export_frame_range=True,
    export_frame_step=1,
    export_force_sampling=True,  # CRUCIAL
    export_nla_strips=False,
    export_def_bones=True,
    export_skins=True,
    export_morph=True,
    export_lights=False
)

if output_file.exists():
    size_kb = output_file.stat().st_size / 1024
    print(f"✅ Exportado: {size_kb:.1f} KB")
else:
    print("❌ No se generó")
    sys.exit(1)

# Verificar GLB
print(f"\n🔍 VERIFICACIÓN EXHAUSTIVA...")

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(output_file))

armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
if not armatures:
    print("❌ No hay armature")
    sys.exit(1)

armature = armatures[0]
print(f"✅ Armature importado: {armature.name}")

if not armature.animation_data or not armature.animation_data.action:
    print("❌ No hay animación")
    sys.exit(1)

action = armature.animation_data.action
print(f"✅ Action: {action.name}")
print(f"   FCurves: {len(action.fcurves)}")

frame_start, frame_end = action.frame_range
print(f"   Frames: {frame_start:.0f} - {frame_end:.0f}")

# Verificar movimiento en MÚLTIPLES huesos
print(f"\n🔍 Verificando movimiento en múltiples huesos...")

bones_to_test = ['Hips', 'Spine', 'Head', 'LeftArm', 'RightArm']
has_movement = False

for bone_name in bones_to_test:
    if bone_name in armature.pose.bones:
        bone = armature.pose.bones[bone_name]
        
        bpy.context.scene.frame_set(int(frame_start))
        bpy.context.view_layer.update()
        pos_start = bone.matrix.translation.copy()
        rot_start = bone.matrix.to_quaternion().copy()
        
        bpy.context.scene.frame_set(int(frame_end))
        bpy.context.view_layer.update()
        pos_end = bone.matrix.translation.copy()
        rot_end = bone.matrix.to_quaternion().copy()
        
        pos_movement = (pos_start - pos_end).length
        rot_diff = abs(rot_start.w - rot_end.w) + abs(rot_start.x - rot_end.x) + \
                  abs(rot_start.y - rot_end.y) + abs(rot_start.z - rot_end.z)
        
        print(f"   {bone_name}: pos={pos_movement:.4f}, rot={rot_diff:.4f}")
        
        if pos_movement > 0.001 or rot_diff > 0.001:
            has_movement = True

if has_movement:
    print("\n" + "🎉"*40)
    print("✅✅✅ MOVIMIENTO DETECTADO - FUNCIONA ✅✅✅")
    print("🎉"*40)
else:
    print("\n❌ NO SE DETECTÓ MOVIMIENTO")
    
    # Verificar si hay keyframes
    print("\n🔍 Verificando keyframes...")
    for fcurve in action.fcurves:
        if 'Hips' in fcurve.data_path:
            print(f"   {fcurve.data_path}: {len(fcurve.keyframe_points)} keyframes")

# Verificar texturas
meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
materials = list(bpy.data.materials)
total_textures = 0

for mesh in meshes:
    for mat in mesh.data.materials:
        if mat and mat.use_nodes:
            for node in mat.node_tree.nodes:
                if node.type == 'TEX_IMAGE':
                    total_textures += 1

print(f"\n✅ Mallas: {len(meshes)}")
print(f"✅ Materiales: {len(materials)}")
print(f"✅ Texturas: {total_textures}")

if has_movement and total_textures > 0:
    print("\n" + "="*80)
    print("🎯 SOLUCIÓN ENCONTRADA - MÉTODO 4 FUNCIONA AL 100%")
    print("="*80)
    print(f"Archivo: {output_file}")
    print("✅ Animación funcional")
    print("✅ Texturas preservadas")
    print("="*80)
