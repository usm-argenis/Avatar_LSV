import bpy
from pathlib import Path

print("="*80)
print("SOLUCIÓN HÍBRIDA: Bake con constraints + Export directo GLB")
print("="*80)

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "saludos" / "Nina_resultado_hola.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_HIBRIDO.glb"

try:
    # 1. Limpiar
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # 2. Importar Nancy
    print(f"\n📦 Importando Nancy...")
    bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
    
    nancy_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            nancy_armature = obj
            break
    
    if nancy_armature.animation_data:
        nancy_armature.animation_data_clear()
    
    # 3. Importar Nina
    print(f"🎬 Importando Nina...")
    bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
    
    nina_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != nancy_armature:
            nina_armature = obj
            break
    
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    
    print(f"   Frames: {frame_start}-{frame_end}")
    
    # 4. MÉTODO CONSTRAINTS + BAKE
    print(f"\n🔄 Aplicando constraints...")
    
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    
    # Crear constraints
    constraints_count = 0
    for nancy_bone in nancy_armature.pose.bones:
        if nancy_bone.name in nina_armature.pose.bones:
            constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
            constraint.target = nina_armature
            constraint.subtarget = nancy_bone.name
            constraints_count += 1
    
    print(f"   ✅ {constraints_count} constraints creados")
    
    # 5. BAKE con visual keying
    print(f"\n🔥 Baking animación...")
    
    bpy.ops.object.select_all(action='DESELECT')
    nancy_armature.select_set(True)
    bpy.context.view_layer.objects.active = nancy_armature
    
    bpy.ops.nla.bake(
        frame_start=frame_start,
        frame_end=frame_end,
        step=1,
        only_selected=False,
        visual_keying=True,
        clear_constraints=True,
        clear_parents=False,
        use_current_action=True,  # Usar acción actual
        clean_curves=True,
        bake_types={'POSE'}
    )
    
    print(f"   ✅ Bake completado")
    
    # 6. Verificar que hay animación
    if nancy_armature.animation_data and nancy_armature.animation_data.action:
        action = nancy_armature.animation_data.action
        print(f"   ✅ Action: {action.name} ({len(action.fcurves)} FCurves)")
    else:
        raise Exception("Bake falló - no hay action")
    
    # 7. Verificar movimiento REAL en la escena
    print(f"\n🔍 Verificando movimiento...")
    
    bpy.context.scene.frame_set(frame_start)
    bpy.context.view_layer.update()
    
    test_bone = nancy_armature.pose.bones['Hips']
    pos_start = test_bone.matrix.translation.copy()
    rot_start = test_bone.matrix.to_quaternion()
    
    bpy.context.scene.frame_set(frame_end)
    bpy.context.view_layer.update()
    
    pos_end = test_bone.matrix.translation.copy()
    rot_end = test_bone.matrix.to_quaternion()
    
    pos_diff = (pos_end - pos_start).length
    rot_diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(4))
    
    print(f"   Hips pos diff: {pos_diff:.4f}")
    print(f"   Hips rot diff: {rot_diff:.4f}")
    
    if pos_diff < 0.001 and rot_diff < 0.001:
        raise Exception("No hay movimiento después del bake")
    
    # 8. Eliminar Nina
    print(f"\n🗑️ Eliminando Nina...")
    objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
    objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
    
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    # 9. Exportar GLB directo
    print(f"\n💾 Exportando a GLB...")
    NANCY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.gltf(
        filepath=str(NANCY_OUTPUT),
        export_format='GLB',
        export_animations=True,
        export_frame_range=True,
        export_force_sampling=True,
        export_def_bones=False,
        export_optimize_animation_size=False,
        export_materials='EXPORT',
        export_image_format='AUTO',
        export_texcoords=True,
        export_normals=True,
        export_attributes=True
    )
    
    glb_size = NANCY_OUTPUT.stat().st_size / (1024*1024)
    print(f"   ✅ {glb_size:.1f} MB")
    
    # 10. Verificación
    print(f"\n🔍 VERIFICACIÓN FINAL...")
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))
    
    test_arm = None
    test_texs = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            test_arm = obj
        elif obj.type == 'MESH' and obj.data.materials:
            for mat in obj.data.materials:
                if mat and mat.use_nodes:
                    for node in mat.node_tree.nodes:
                        if node.type == 'TEX_IMAGE' and node.image:
                            test_texs.append({
                                'nombre': node.image.name,
                                'size': node.image.size[:]
                            })
    
    print(f"   Texturas: {len(test_texs)}")
    
    texturas_alta_res = sum(1 for t in test_texs if t['size'][0] >= 512)
    print(f"   Alta resolución: {texturas_alta_res}/{len(test_texs)}")
    
    if test_arm and test_arm.animation_data and test_arm.animation_data.action:
        action = test_arm.animation_data.action
        print(f"   ✅ Animación: {action.name} ({len(action.fcurves)} FCurves)")
        
        # Probar movimiento
        bpy.context.scene.frame_set(0)
        bpy.context.view_layer.update()
        
        bone = test_arm.pose.bones['Hips']
        pos_start = bone.matrix.translation.copy()
        
        bpy.context.scene.frame_set(71)
        bpy.context.view_layer.update()
        
        pos_end = bone.matrix.translation.copy()
        diff = (pos_end - pos_start).length
        
        print(f"   Movimiento Hips: {diff:.4f}")
        
        if diff > 0.001 and texturas_alta_res >= 6:
            print(f"\n{'='*80}")
            print("✅ ✅ ✅ ÉXITO TOTAL ✅ ✅ ✅")
            print("Nancy con texturas HD Y animación funcional")
            print(f"{'='*80}")
        elif diff > 0.001:
            print(f"\n⚠️ Animación OK pero texturas en baja resolución")
        elif texturas_alta_res >= 6:
            print(f"\n⚠️ Texturas OK pero animación no funciona")
        else:
            print(f"\n❌ Ambos problemas persisten")
    else:
        print(f"   ❌ Sin animación")
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
