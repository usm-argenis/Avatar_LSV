"""
SOLUCIÓN FINAL - Exportar GLB con la acción correcta "Action"
"""

import bpy
import sys
from pathlib import Path

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output")
BLEND_DIR = BASE_DIR / "blend" / "cortesia"
TEST_BLEND = BLEND_DIR / "Nancy_a la orden.blend"

print("\n" + "="*80)
print("SOLUCIÓN FINAL - EXPORTANDO CON ACCIÓN CORRECTA")
print("="*80)

# Cargar
bpy.ops.wm.open_mainfile(filepath=str(TEST_BLEND))

armature = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE'][0]
print(f"\n✅ Armature: {armature.name}")

# Buscar la acción "Action" que es la que tiene movimiento
target_action = None
for action in bpy.data.actions:
    if action.name == "Action":
        target_action = action
        break

if not target_action:
    print("❌ No se encontró la acción 'Action'")
    sys.exit(1)

print(f"✅ Acción encontrada: {target_action.name}")
print(f"   FCurves: {len(target_action.fcurves)}")

frame_start, frame_end = target_action.frame_range
print(f"   Frames: {frame_start:.0f} - {frame_end:.0f}")

# ASIGNAR la acción correcta
if not armature.animation_data:
    armature.animation_data_create()

armature.animation_data.action = target_action
armature.animation_data.use_nla = False

print(f"✅ Acción asignada al armature")

# Configurar escena
bpy.context.scene.frame_start = int(frame_start)
bpy.context.scene.frame_end = int(frame_end)
bpy.context.scene.frame_set(int(frame_start))

# Verificar movimiento antes de exportar
print(f"\n🔍 Verificando movimiento antes de exportar...")
bpy.context.scene.frame_set(int(frame_start))
bpy.context.view_layer.update()

test_bone = armature.pose.bones['Hips']
pos_start = test_bone.matrix.translation.copy()

bpy.context.scene.frame_set(int(frame_end))
bpy.context.view_layer.update()

pos_end = test_bone.matrix.translation.copy()
movement = (pos_start - pos_end).length

print(f"   Movimiento Hips: {movement:.4f}")

if movement < 0.001:
    print("❌ No hay movimiento - algo está mal")
    sys.exit(1)

print("✅ Movimiento verificado")

# Exportar GLB
print(f"\n📤 Exportando GLB...")

output_file = BLEND_DIR / "Nancy_a la orden.glb"

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
    export_force_sampling=True,
    export_nla_strips=False,
    export_def_bones=True,
    export_skins=True,
    export_morph=True,
    export_lights=False
)

if not output_file.exists():
    print("❌ No se generó el archivo")
    sys.exit(1)

size_kb = output_file.stat().st_size / 1024
print(f"✅ Exportado: {size_kb:.1f} KB")
print(f"   Archivo: {output_file}")

# VERIFICACIÓN COMPLETA
print(f"\n🔍 VERIFICACIÓN COMPLETA DEL GLB...")

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(output_file))

armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
if not armatures:
    print("❌ No hay armature en GLB")
    sys.exit(1)

armature = armatures[0]
print(f"✅ Armature importado: {armature.name}")

if not armature.animation_data or not armature.animation_data.action:
    print("❌ No hay animación en GLB")
    sys.exit(1)

action = armature.animation_data.action
print(f"✅ Action: {action.name}")
print(f"   FCurves: {len(action.fcurves)}")

frame_start, frame_end = action.frame_range
print(f"   Frames: {frame_start:.0f} - {frame_end:.0f}")

# Verificar movimiento en múltiples huesos
print(f"\n🔍 Verificando movimiento en GLB...")

test_bones = ['Hips', 'Spine', 'Head', 'LeftArm', 'RightArm', 'LeftHand', 'RightHand']
has_movement = False
movement_details = []

for bone_name in test_bones:
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
        
        pos_diff = (pos_start - pos_end).length
        rot_diff = abs(rot_start.w - rot_end.w) + abs(rot_start.x - rot_end.x) + \
                  abs(rot_start.y - rot_end.y) + abs(rot_start.z - rot_end.z)
        
        movement_details.append(f"   {bone_name}: pos={pos_diff:.4f}, rot={rot_diff:.4f}")
        
        if pos_diff > 0.001 or rot_diff > 0.001:
            has_movement = True

for detail in movement_details:
    print(detail)

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

print(f"\n📊 Contenido del GLB:")
print(f"   Mallas: {len(meshes)}")
print(f"   Materiales: {len(materials)}")
print(f"   Texturas: {total_textures}")

# Resultado final
print(f"\n" + "="*80)

if has_movement and total_textures > 0:
    print("🎉🎉🎉 ÉXITO TOTAL 🎉🎉🎉")
    print("="*80)
    print(f"✅ GLB FUNCIONA AL 100%")
    print(f"✅ Animación: FUNCIONAL con movimiento real")
    print(f"✅ Texturas: {total_textures} texturas preservadas")
    print(f"✅ Geometría: {len(meshes)} mallas completas")
    print(f"\n📁 Archivo: {output_file}")
    print(f"📊 Tamaño: {size_kb:.1f} KB")
    print("="*80)
else:
    print("❌ FALLO")
    print("="*80)
    if not has_movement:
        print("❌ No hay movimiento en la animación")
    if total_textures == 0:
        print("❌ No hay texturas")
    sys.exit(1)
