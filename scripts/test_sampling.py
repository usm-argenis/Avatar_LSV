import bpy
from pathlib import Path

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "saludos" / "Nina_resultado_hola.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_REAL.glb"

print("=" * 80)
print("SOLUCIÓN REAL: Bake + sampling correcto")
print("=" * 80)

try:
    # 1-3. Importar Nancy y Nina
    bpy.ops.wm.read_homefile(use_empty=True)
    
    print("\n📦 Importando Nancy...")
    bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
    
    nancy_armature = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE'][0]
    if nancy_armature.animation_data:
        nancy_armature.animation_data_clear()
    
    print("🎬 Importando Nina...")
    bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
    
    nina_armature = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE' and obj != nancy_armature][0]
    
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    
    print(f"   Frames: {frame_start}-{frame_end}")
    
    # 4. Constraints
    print("\n🔄 Aplicando constraints...")
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    
    for nancy_bone in nancy_armature.pose.bones:
        if nancy_bone.name in nina_armature.pose.bones:
            constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
            constraint.target = nina_armature
            constraint.subtarget = nancy_bone.name
    
    # 5. Bake con TODOS los frames
    print("🔥 Baking...")
    
    bpy.ops.object.select_all(action='DESELECT')
    nancy_armature.select_set(True)
    bpy.context.view_layer.objects.active = nancy_armature
    
    bpy.ops.nla.bake(
        frame_start=frame_start,
        frame_end=frame_end,
        step=1,  # CADA frame
        only_selected=False,
        visual_keying=True,
        clear_constraints=True,
        clear_parents=False,
        use_current_action=False,  # Crear nueva acción
        clean_curves=False,  # NO limpiar curvas
        bake_types={'POSE'}
    )
    
    # 6. Elminar Nina
    objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
    for obj in bpy.data.objects:
        if obj not in objetos_nancy:
            bpy.data.objects.remove(obj, do_unlink=True)
    
    # 7. Asegurar action está correcta
    if nancy_armature.animation_data and nancy_armature.animation_data.action:
        action = nancy_armature.animation_data.action
        print(f"   ✅ Action: {len(action.fcurves)} FCurves")
        action.frame_range = (frame_start, frame_end)
    
    # 8. Exportar con sampling MANUAL
    print("\n💾 Exportando...")
    NANCY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.gltf(
        filepath=str(NANCY_OUTPUT),
        export_format='GLB',
        export_animations=True,
        export_frame_range=True,
        export_force_sampling=False,  # NO forzar re-sampling
        export_def_bones=False,
        export_optimize_animation_size=False,  # NO optimizar
        export_materials='EXPORT',
        export_image_format='AUTO',
        export_texcoords=True,
        export_normals=True
    )
    
    print(f"   ✅ {NANCY_OUTPUT.stat().st_size / (1024*1024):.1f} MB")
    
    # 9. Verificar
    print("\n🔍 Verificación...")
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))
    
    test_arm = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE'][0]
    
    texs = []
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.materials:
            for mat in obj.data.materials:
                if mat and mat.use_nodes:
                    for node in mat.node_tree.nodes:
                        if node.type == 'TEX_IMAGE' and node.image:
                            texs.append(node.image.size[:])
    
    print(f"   Texturas: {len(texs)}")
    hd_texs = sum(1 for t in texs if t[0] >= 512)
    print(f"   HD (>=512px): {hd_texs}")
    
    if test_arm.animation_data and test_arm.animation_data.action:
        action = test_arm.animation_data.action
        print(f"   ✅ Animación: {len(action.fcurves)} FCurves")
        
        # Test movimiento con matrix
        bpy.context.scene.frame_set(frame_start)
        bpy.context.view_layer.update()
        
        hips = test_arm.pose.bones['Hips']
        pos1 = hips.matrix.translation.copy()
        
        bpy.context.scene.frame_set(frame_start + 10)
        bpy.context.view_layer.update()
        
        pos2 = hips.matrix.translation.copy()
        diff = (pos2 - pos1).length
        
        print(f"   Movimiento: {diff:.4f}")
        
        if diff > 0.001 and hd_texs >= 6:
            print("\n✅ ✅ ✅ ÉXITO TOTAL ✅ ✅ ✅")
            print(f"Texturas HD Y animación funcional")
        elif diff > 0.001:
            print("\n✅ Animación OK, texturas bajas")
        elif hd_texs >= 6:
            print("\n⚠️ Texturas OK, animación falla")
        else:
            print("\n❌ Ambos fallan")
    else:
        print("❌ Sin animación")
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
