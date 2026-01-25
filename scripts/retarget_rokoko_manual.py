import bpy
from pathlib import Path

print("="*80)
print("RETARGETING MANUAL CON ROKOKO STUDIO LIVE")
print("="*80)

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "saludos" / "Nina_resultado_hola.glb"
NANCY_OUTPUT_BLEND = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_ROKOKO.blend"
NANCY_OUTPUT_GLB = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_ROKOKO.glb"

print(f"\n📂 Archivos:")
print(f"   Nancy: {NANCY_BASE}")
print(f"   Nina: {NINA_FILE}")
print(f"   Salida BLEND: {NANCY_OUTPUT_BLEND}")
print(f"   Salida GLB: {NANCY_OUTPUT_GLB}")

try:
    # 1. Limpiar escena
    print(f"\n🧹 Paso 1: Limpiando escena...")
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # 2. Importar Nina con animación PRIMERO (será el source)
    print(f"\n🎬 Paso 2: Importando Nina (source con animación)...")
    bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
    
    nina_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            nina_armature = obj
            nina_armature.name = "Nina_Armature"
            break
    
    if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
        raise Exception("Nina sin animación")
    
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    
    print(f"   ✅ Nina Armature: {nina_armature.name}")
    print(f"   ✅ Huesos: {len(nina_armature.data.bones)}")
    print(f"   ✅ Animación: {nina_action.name}")
    print(f"   ✅ Frames: {frame_start}-{frame_end}")
    print(f"   ✅ FCurves: {len(nina_action.fcurves)}")
    
    # 3. Importar Nancy (target)
    print(f"\n📦 Paso 3: Importando Nancy (target)...")
    bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
    
    nancy_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != nina_armature:
            nancy_armature = obj
            nancy_armature.name = "Nancy_Armature"
            break
    
    if not nancy_armature:
        raise Exception("No se encontró Nancy armature")
    
    print(f"   ✅ Nancy Armature: {nancy_armature.name}")
    print(f"   ✅ Huesos: {len(nancy_armature.data.bones)}")
    
    # Limpiar animación de Nancy si existe
    if nancy_armature.animation_data:
        nancy_armature.animation_data_clear()
    
    # 4. Verificar que los huesos coincidan
    print(f"\n🦴 Paso 4: Verificando huesos...")
    nancy_bones = set(nancy_armature.data.bones.keys())
    nina_bones = set(nina_armature.data.bones.keys())
    bones_comunes = nancy_bones & nina_bones
    
    print(f"   Nancy: {len(nancy_bones)} huesos")
    print(f"   Nina: {len(nina_bones)} huesos")
    print(f"   Coinciden: {len(bones_comunes)} huesos")
    
    if len(bones_comunes) != len(nancy_bones) or len(bones_comunes) != len(nina_bones):
        print(f"   ⚠️ ADVERTENCIA: No todos los huesos coinciden")
    else:
        print(f"   ✅ Todos los huesos coinciden perfectamente")
    
    # 5. Configurar Rokoko Studio
    print(f"\n🔧 Paso 5: Configurando Rokoko Studio...")
    
    scene = bpy.context.scene
    
    # Configurar source y target para Rokoko
    if hasattr(scene, 'rsl_retargeting_armature_source'):
        scene.rsl_retargeting_armature_source = nina_armature
        print(f"   ✅ Source armature: {nina_armature.name}")
    
    if hasattr(scene, 'rsl_retargeting_armature_target'):
        scene.rsl_retargeting_armature_target = nancy_armature
        print(f"   ✅ Target armature: {nancy_armature.name}")
    
    # Configurar frame range
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    
    # 6. Intentar usar Rokoko para retargeting
    print(f"\n🎯 Paso 6: Aplicando retargeting de Rokoko...")
    
    # Seleccionar target (Nancy) como activo
    bpy.ops.object.select_all(action='DESELECT')
    nancy_armature.select_set(True)
    bpy.context.view_layer.objects.active = nancy_armature
    
    rokoko_success = False
    
    if hasattr(bpy.ops, 'rsl') and hasattr(bpy.ops.rsl, 'retarget_animation'):
        try:
            # Intentar auto-detectar huesos
            print(f"   🔍 Detectando huesos...")
            bpy.ops.rsl.detect_actor_bones()
            
            # Intentar build bone list
            if hasattr(bpy.ops.rsl, 'build_bone_list'):
                print(f"   🔨 Construyendo lista de huesos...")
                bpy.ops.rsl.build_bone_list()
            
            # Ejecutar retargeting
            print(f"   🎬 Ejecutando retargeting...")
            result = bpy.ops.rsl.retarget_animation()
            
            if result == {'FINISHED'}:
                rokoko_success = True
                print(f"   ✅ Retargeting de Rokoko exitoso")
            else:
                print(f"   ⚠️ Rokoko retornó: {result}")
                
        except Exception as e:
            print(f"   ⚠️ Error en Rokoko: {e}")
    
    # 7. Si Rokoko falló, usar método manual
    if not rokoko_success:
        print(f"\n🔄 Paso 6b: Usando método manual (constraints + bake)...")
        
        # Crear constraints
        constraints_count = 0
        for nancy_bone in nancy_armature.pose.bones:
            if nancy_bone.name in nina_armature.pose.bones:
                constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = nina_armature
                constraint.subtarget = nancy_bone.name
                constraints_count += 1
        
        print(f"   ✅ {constraints_count} constraints creados")
        
        # Bake
        print(f"   🔥 Baking animación...")
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
            use_current_action=False,
            clean_curves=False,
            bake_types={'POSE'}
        )
        
        print(f"   ✅ Bake completado")
    
    # 8. Verificar que Nancy tiene animación
    print(f"\n✅ Paso 7: Verificando animación en Nancy...")
    
    if not nancy_armature.animation_data or not nancy_armature.animation_data.action:
        raise Exception("Nancy no recibió la animación")
    
    nancy_action = nancy_armature.animation_data.action
    print(f"   ✅ Action: {nancy_action.name}")
    print(f"   ✅ FCurves: {len(nancy_action.fcurves)}")
    
    # Verificar movimiento real
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
    
    print(f"   Hips movimiento:")
    print(f"     Posición: {pos_diff:.4f}")
    print(f"     Rotación: {rot_diff:.4f}")
    
    if pos_diff < 0.001 and rot_diff < 0.001:
        raise Exception("No hay movimiento en los huesos")
    
    print(f"   ✅ Animación verificada - hay movimiento")
    
    # 9. Eliminar objetos de Nina
    print(f"\n🗑️ Paso 8: Eliminando objetos de Nina...")
    
    objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
    objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
    
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    print(f"   ✅ {len(objetos_eliminar)} objetos eliminados")
    print(f"   ✅ {len(objetos_nancy)} objetos de Nancy mantenidos")
    
    # 10. Guardar como .blend
    print(f"\n💾 Paso 9: Guardando como .blend...")
    NANCY_OUTPUT_BLEND.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.wm.save_as_mainfile(filepath=str(NANCY_OUTPUT_BLEND))
    
    blend_size = NANCY_OUTPUT_BLEND.stat().st_size / (1024*1024)
    print(f"   ✅ BLEND guardado: {blend_size:.1f} MB")
    
    # 11. Exportar usando método FBX → GLB (preserva animación)
    print(f"\n💾 Paso 10: Exportando con método FBX → GLB...")
    
    fbx_temp = NANCY_OUTPUT_GLB.with_suffix('.fbx')
    
    # Exportar a FBX
    print(f"   📦 Exportando a FBX temporal...")
    bpy.ops.export_scene.fbx(
        filepath=str(fbx_temp),
        use_selection=False,
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_step=1.0,
        add_leaf_bones=False,
        path_mode='COPY',
        embed_textures=True
    )
    
    print(f"   📦 Reimportando FBX...")
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.fbx(filepath=str(fbx_temp))
    
    # Exportar a GLB desde FBX
    print(f"   💾 Exportando FBX a GLB...")
    bpy.ops.export_scene.gltf(
        filepath=str(NANCY_OUTPUT_GLB),
        export_format='GLB',
        export_animations=True,
        export_frame_range=True,
        export_force_sampling=True,
        export_def_bones=False,
        export_optimize_animation_size=False,
        export_materials='EXPORT',
        export_image_format='AUTO',
        export_texcoords=True,
        export_normals=True
    )
    
    # Limpiar FBX temporal
    if fbx_temp.exists():
        fbx_temp.unlink()
        print(f"   🗑️ FBX temporal eliminado")
    
    glb_size = NANCY_OUTPUT_GLB.stat().st_size / (1024*1024)
    print(f"   ✅ GLB exportado: {glb_size:.1f} MB")
    
    # 12. VERIFICACIÓN FINAL: Reimportar GLB
    print(f"\n🔍 Paso 11: VERIFICACIÓN FINAL - Reimportando GLB...")
    
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT_GLB))
    
    test_arm = None
    test_materials = []
    test_textures = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            test_arm = obj
        elif obj.type == 'MESH' and obj.data.materials:
            for mat in obj.data.materials:
                if mat and mat not in test_materials:
                    test_materials.append(mat)
                    if mat.use_nodes:
                        for node in mat.node_tree.nodes:
                            if node.type == 'TEX_IMAGE' and node.image:
                                test_textures.append({
                                    'nombre': node.image.name,
                                    'size': node.image.size[:]
                                })
    
    print(f"\n📦 Contenido del GLB final:")
    print(f"   Materiales: {len(test_materials)}")
    print(f"   Texturas: {len(test_textures)}")
    
    # Contar texturas HD
    hd_textures = sum(1 for t in test_textures if t['size'][0] >= 512 or t['size'][1] >= 512)
    print(f"   Texturas HD (>=512px): {hd_textures}")
    
    # Verificar animación
    if not test_arm:
        raise Exception("GLB no tiene armature")
    
    if not test_arm.animation_data or not test_arm.animation_data.action:
        raise Exception("GLB no tiene animación")
    
    test_action = test_arm.animation_data.action
    print(f"\n🎬 Animación en GLB:")
    print(f"   Nombre: {test_action.name}")
    print(f"   FCurves: {len(test_action.fcurves)}")
    print(f"   Frame range: {test_action.frame_range}")
    
    # Verificar movimiento en GLB
    bpy.context.scene.frame_set(int(test_action.frame_range[0]))
    bpy.context.view_layer.update()
    
    if 'Hips' not in test_arm.pose.bones:
        raise Exception("GLB no tiene hueso Hips")
    
    test_bone = test_arm.pose.bones['Hips']
    test_pos_start = test_bone.matrix.translation.copy()
    
    bpy.context.scene.frame_set(int(test_action.frame_range[1]))
    bpy.context.view_layer.update()
    
    test_pos_end = test_bone.matrix.translation.copy()
    test_diff = (test_pos_end - test_pos_start).length
    
    print(f"\n🎯 Movimiento en GLB:")
    print(f"   Hips diff: {test_diff:.4f}")
    
    # EVALUACIÓN FINAL
    print(f"\n{'='*80}")
    
    if test_diff > 0.001 and hd_textures > 0:
        print("✅ ✅ ✅ ÉXITO TOTAL ✅ ✅ ✅")
        print(f"GLB con {len(test_textures)} texturas ({hd_textures} HD) Y animación funcional")
        print(f"Movimiento verificado: {test_diff:.4f}")
    elif test_diff > 0.001:
        print("⚠️ ÉXITO PARCIAL")
        print("Animación funciona pero texturas en baja resolución")
    elif hd_textures > 0:
        print("❌ PROBLEMA")
        print("Texturas OK pero animación NO funciona")
    else:
        print("❌ FALLÓ")
        print("Ni texturas ni animación funcionan correctamente")
    
    print(f"{'='*80}")
    
    print(f"\n📁 Archivos generados:")
    print(f"   BLEND: {NANCY_OUTPUT_BLEND}")
    print(f"   GLB: {NANCY_OUTPUT_GLB}")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
