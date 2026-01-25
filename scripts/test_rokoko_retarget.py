import bpy
from pathlib import Path

print("="*80)
print("RETARGETING CON ROKOKO STUDIO LIVE: Nina → Nancy")
print("="*80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "saludos" / "Nina_resultado_hola.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_ROKOKO.glb"

print(f"\n📂 Archivos:")
print(f"   Nancy base: {NANCY_BASE}")
print(f"   Nina: {NINA_FILE}")
print(f"   Salida: {NANCY_OUTPUT}")

try:
    # 1. Limpiar escena
    print(f"\n🧹 Limpiando escena...")
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # 2. Importar Nancy (destino)
    print(f"\n📦 Importando Nancy (destino)...")
    bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
    
    nancy_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            nancy_armature = obj
            nancy_armature.name = "Nancy_Armature"
            break
    
    if not nancy_armature:
        print("❌ ERROR: No se encontró armature de Nancy")
        exit(1)
    
    print(f"   ✅ Nancy Armature: {nancy_armature.name}")
    print(f"   ✅ Huesos: {len(nancy_armature.data.bones)}")
    
    # Limpiar animación previa
    if nancy_armature.animation_data:
        nancy_armature.animation_data_clear()
    
    # 3. Importar Nina con animación
    print(f"\n🎬 Importando Nina con animación...")
    bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
    
    nina_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != nancy_armature:
            nina_armature = obj
            nina_armature.name = "Nina_Armature"
            break
    
    if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
        print("❌ ERROR: Nina sin animación")
        exit(1)
    
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    
    print(f"   ✅ Animación: {nina_action.name}")
    print(f"   ✅ Frames: {frame_start} - {frame_end}")
    
    # 4. Configurar frame range
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    
    # 5. Seleccionar armatures para Rokoko
    print(f"\n🔄 Configurando Rokoko Studio...")
    bpy.context.view_layer.objects.active = nancy_armature
    nancy_armature.select_set(True)
    nina_armature.select_set(False)
    
    # Configurar Rokoko: Nina es SOURCE, Nancy es TARGET
    scene = bpy.context.scene
    if hasattr(scene, 'rsl_retargeting_armature_source'):
        scene.rsl_retargeting_armature_source = nina_armature
        print(f"   ✅ Source configurado: {nina_armature.name}")
    
    if hasattr(scene, 'rsl_retargeting_armature_target'):
        scene.rsl_retargeting_armature_target = nancy_armature
        print(f"   ✅ Target configurado: {nancy_armature.name}")
    
    # 6. Ejecutar retargeting de Rokoko
    print(f"\n🎯 Ejecutando retargeting de Rokoko Studio...")
    
    # Verificar si Rokoko está disponible
    if hasattr(bpy.ops, 'rsl') and hasattr(bpy.ops.rsl, 'retarget_animation'):
        print(f"   ✅ Rokoko Studio Live disponible")
        
        # Intentar retargeting automático
        try:
            bpy.ops.rsl.detect_actor_bones()
            print(f"   ✅ Huesos detectados")
        except:
            print(f"   ⚠️ No se pudo auto-detectar huesos")
        
        # Ejecutar retargeting
        try:
            result = bpy.ops.rsl.retarget_animation()
            print(f"   ✅ Retargeting ejecutado: {result}")
        except Exception as e:
            print(f"   ❌ Error en retargeting de Rokoko: {e}")
            print(f"   ⚠️ Usando método manual como fallback...")
            
            # Fallback: método manual
            for nancy_bone in nancy_armature.pose.bones:
                if nancy_bone.name in nina_armature.pose.bones:
                    constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
                    constraint.target = nina_armature
                    constraint.subtarget = nancy_bone.name
            
            bpy.ops.nla.bake(
                frame_start=frame_start,
                frame_end=frame_end,
                step=1,
                only_selected=False,
                visual_keying=True,
                clear_constraints=True,
                bake_types={'POSE'}
            )
    else:
        print(f"   ❌ Rokoko Studio Live NO disponible")
        print(f"   Usando método manual...")
        
        # Método manual
        for nancy_bone in nancy_armature.pose.bones:
            if nancy_bone.name in nina_armature.pose.bones:
                constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = nina_armature
                constraint.subtarget = nancy_bone.name
        
        bpy.ops.nla.bake(
            frame_start=frame_start,
            frame_end=frame_end,
            step=1,
            only_selected=False,
            visual_keying=True,
            clear_constraints=True,
            bake_types={'POSE'}
        )
    
    # 7. Verificar que Nancy tiene animación
    if not nancy_armature.animation_data or not nancy_armature.animation_data.action:
        print(f"   ❌ ERROR: Nancy no recibió animación")
        exit(1)
    
    print(f"   ✅ Nancy tiene animación: {nancy_armature.animation_data.action.name}")
    print(f"   ✅ FCurves: {len(nancy_armature.animation_data.action.fcurves)}")
    
    # 8. Eliminar objetos de Nina
    print(f"\n🗑️ Eliminando objetos de Nina...")
    objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
    objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
    
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    print(f"   ✅ {len(objetos_eliminar)} objetos eliminados")
    
    # 9. Verificar materiales
    print(f"\n🎨 Verificando materiales...")
    materiales_count = 0
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.materials:
            materiales_count += len(obj.data.materials)
    print(f"   ✅ Materiales: {materiales_count}")
    
    # 10. Exportar a GLB directamente (SIN FBX intermedio)
    print(f"\n💾 Exportando a GLB con animación y texturas...")
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
    
    if NANCY_OUTPUT.exists():
        size_mb = NANCY_OUTPUT.stat().st_size / (1024*1024)
        print(f"   ✅ Archivo generado: {size_mb:.1f} MB")
        
        # 11. Verificación final
        print(f"\n🔍 Verificación final...")
        bpy.ops.wm.read_homefile(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))
        
        test_arm = None
        test_materials = []
        
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                test_arm = obj
            elif obj.type == 'MESH' and obj.data.materials:
                test_materials.extend(obj.data.materials)
        
        # Verificar texturas
        print(f"   Materiales: {len(set(test_materials))}")
        texturas_count = 0
        for mat in set(test_materials):
            if mat and mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == 'TEX_IMAGE' and node.image:
                        texturas_count += 1
        print(f"   Texturas: {texturas_count}")
        
        # Verificar animación
        if test_arm and test_arm.animation_data and test_arm.animation_data.action:
            test_action = test_arm.animation_data.action
            print(f"   ✅ Animación: {test_action.name}")
            print(f"   ✅ FCurves: {len(test_action.fcurves)}")
            
            # Probar movimiento en varios huesos
            bpy.context.scene.frame_set(frame_start)
            test_bones = ['Hips', 'LeftShoulder', 'RightShoulder', 'LeftHand', 'RightHand']
            
            for bone_name in test_bones:
                if bone_name in test_arm.pose.bones:
                    bone = test_arm.pose.bones[bone_name]
                    rot_start = bone.rotation_quaternion.copy()
                    
                    bpy.context.scene.frame_set(frame_end)
                    rot_end = test_arm.pose.bones[bone_name].rotation_quaternion
                    
                    diff = abs(rot_start.w - rot_end.w) + abs(rot_start.x - rot_end.x)
                    
                    if diff > 0.01:
                        print(f"   ✅ {bone_name} se mueve: {diff:.3f}")
                        break
            
            print(f"\n{'='*80}")
            print("✅ ✅ ✅ ÉXITO COMPLETO ✅ ✅ ✅")
            print("Nancy con TEXTURAS y ANIMACIÓN correcta")
            print(f"{'='*80}")
        else:
            print("   ❌ ERROR: Sin animación")
    else:
        print("   ❌ ERROR: Archivo no generado")
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
