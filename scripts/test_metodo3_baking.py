"""
Diagnóstico TEST 7 - Baking animación antes de exportar
"""

import bpy
from pathlib import Path

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output")
BLEND_DIR = BASE_DIR / "blend" / "cortesia"
TEST_BLEND = BLEND_DIR / "Nancy_a la orden.blend"

print("\n" + "="*80)
print("TEST 7: BAKING ANIMACIÓN ANTES DE EXPORTAR")
print("="*80)

# Cargar blend
bpy.ops.wm.open_mainfile(filepath=str(TEST_BLEND))

# Obtener armature
armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
if not armatures:
    print("❌ No hay armature")
    sys.exit(1)

armature = armatures[0]
print(f"✅ Armature: {armature.name}")

# Verificar action actual
if not armature.animation_data or not armature.animation_data.action:
    print("❌ No hay action")
    sys.exit(1)

original_action = armature.animation_data.action
print(f"✅ Action original: {original_action.name}")
print(f"   FCurves: {len(original_action.fcurves)}")

frame_start, frame_end = original_action.frame_range
print(f"   Frames: {frame_start:.0f} - {frame_end:.0f}")

# Configurar escena
bpy.context.scene.frame_start = int(frame_start)
bpy.context.scene.frame_end = int(frame_end)

# CRUCIAL: Seleccionar armature y hacer bake
print(f"\n🔥 BAKING animación...")
bpy.ops.object.select_all(action='DESELECT')
armature.select_set(True)
bpy.context.view_layer.objects.active = armature

# Desactivar NLA si está activo
if armature.animation_data.use_nla:
    armature.animation_data.use_nla = False
    print("   NLA desactivado")

try:
    # Bake con visual keying
    bpy.ops.nla.bake(
        frame_start=int(frame_start),
        frame_end=int(frame_end),
        step=1,
        only_selected=False,
        visual_keying=True,
        clear_constraints=False,
        clear_parents=False,
        use_current_action=True,
        clean_curves=False,
        bake_types={'POSE'}
    )
    
    print("✅ Baking completado")
    
    # Verificar que la action tiene keyframes
    baked_action = armature.animation_data.action
    print(f"   Action bakeada: {baked_action.name}")
    print(f"   FCurves: {len(baked_action.fcurves)}")
    
    # Verificar keyframes
    total_keyframes = 0
    for fcurve in baked_action.fcurves:
        total_keyframes += len(fcurve.keyframe_points)
    
    print(f"   Total keyframes: {total_keyframes}")
    
    if total_keyframes == 0:
        print("❌ No se generaron keyframes")
        sys.exit(1)
    
except Exception as e:
    print(f"❌ Error en baking: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Exportar GLB con la animación bakeada
print(f"\n📤 Exportando GLB con animación bakeada...")

output_file = BLEND_DIR / "TEST_metodo3_baked.glb"

try:
    bpy.ops.object.select_all(action='SELECT')
    
    bpy.ops.export_scene.gltf(
        filepath=str(output_file),
        export_format='GLB',
        export_animations=True,
        export_frame_range=True,
        export_frame_step=1,
        export_force_sampling=True,
        export_animation_mode='ACTIONS',
        export_nla_strips=False,
        export_def_bones=True,
        export_skins=True,
        export_morph=True,
        export_materials='EXPORT',
        export_image_format='AUTO',
        export_texcoords=True,
        export_normals=True,
        export_draco_mesh_compression_enable=False,
        use_selection=False
    )
    
    if output_file.exists():
        size_kb = output_file.stat().st_size / 1024
        print(f"✅ Exportado: {size_kb:.1f} KB")
    else:
        print("❌ No se generó archivo")
        sys.exit(1)
        
except Exception as e:
    print(f"❌ Error exportando: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Verificar GLB
print(f"\n🔍 Verificando GLB...")

bpy.ops.wm.read_factory_settings(use_empty=True)

try:
    bpy.ops.import_scene.gltf(filepath=str(output_file))
    
    armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
    if not armatures:
        print("❌ No hay armature en GLB")
        sys.exit(1)
    
    armature = armatures[0]
    print(f"✅ Armature: {armature.name}")
    
    if not armature.animation_data or not armature.animation_data.action:
        print("❌ No hay animación en GLB")
        sys.exit(1)
    
    action = armature.animation_data.action
    print(f"✅ Action: {action.name}")
    print(f"   FCurves: {len(action.fcurves)}")
    
    # Verificar keyframes
    total_keyframes = 0
    for fcurve in action.fcurves:
        total_keyframes += len(fcurve.keyframe_points)
    
    print(f"   Total keyframes: {total_keyframes}")
    
    # Verificar movimiento REAL
    if armature.pose.bones:
        frame_start, frame_end = action.frame_range
        
        bpy.context.scene.frame_set(int(frame_start))
        bpy.context.view_layer.update()
        
        test_bone = armature.pose.bones[0]
        pos_start = test_bone.matrix.translation.copy()
        rot_start = test_bone.matrix.to_quaternion().copy()
        
        bpy.context.scene.frame_set(int(frame_end))
        bpy.context.view_layer.update()
        
        pos_end = test_bone.matrix.translation.copy()
        rot_end = test_bone.matrix.to_quaternion().copy()
        
        pos_movement = (pos_start - pos_end).length
        rot_movement = abs(rot_start.w - rot_end.w) + abs(rot_start.x - rot_end.x) + \
                      abs(rot_start.y - rot_end.y) + abs(rot_start.z - rot_end.z)
        
        print(f"\n   Movimiento {test_bone.name}:")
        print(f"      Posición: {pos_movement:.4f}")
        print(f"      Rotación: {rot_movement:.4f}")
        
        if pos_movement > 0.001 or rot_movement > 0.001:
            print("\n" + "🎉"*40)
            print("✅✅✅ GLB TIENE ANIMACIÓN FUNCIONAL AL 100% ✅✅✅")
            print("🎉"*40)
            print(f"\nArchivo funcional: {output_file}")
        else:
            print("\n❌ GLB no tiene movimiento real")
            sys.exit(1)
    
    # Verificar materiales
    materials = list(bpy.data.materials)
    meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
    
    print(f"\n✅ Materiales: {len(materials)}")
    print(f"✅ Mallas: {len(meshes)}")
    
    total_textures = 0
    for mesh in meshes:
        for mat in mesh.data.materials:
            if mat and mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == 'TEX_IMAGE':
                        total_textures += 1
    
    print(f"✅ Texturas: {total_textures}")
    
    if total_textures > 0:
        print("\n✅✅✅ TEXTURAS PRESERVADAS")
    
except Exception as e:
    print(f"❌ Error verificando: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "="*80)
print("MÉTODO 3 (BAKING) - COMPLETADO")
print("="*80)
