import bpy
from pathlib import Path

print("="*80)
print("RETARGETING CON ROKOKO STUDIO: Nina → Nancy")
print("="*80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_MODEL = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "cortesia" / "Nina_resultado_a la orden.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "cortesia" / "Nancy_resultado_a la orden.glb"

print(f"\n📂 Archivos:")
print(f"   Modelo Nancy: {NANCY_MODEL.name}")
print(f"   Animación Nina: {NINA_FILE.name}")
print(f"   Salida: {NANCY_OUTPUT}")

try:
    # PASO 1: Limpiar escena
    print(f"\n🧹 Limpiando escena...")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # PASO 2: Importar Nancy (destino - sin animación)
    print(f"\n📦 Importando Nancy (destino)...")
    bpy.ops.import_scene.gltf(filepath=str(NANCY_MODEL))
    
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
    print(f"   ✅ Huesos Nancy: {len(nancy_armature.data.bones)}")
    
    # Eliminar animación previa de Nancy
    if nancy_armature.animation_data:
        nancy_armature.animation_data_clear()
    
    # PASO 3: Importar Nina (source - con animación)
    print(f"\n🎬 Importando Nina (source con animación)...")
    bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
    
    nina_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != nancy_armature:
            nina_armature = obj
            nina_armature.name = "Nina_Armature"
            break
    
    if not nina_armature:
        print("❌ ERROR: No se encontró armature de Nina")
        exit(1)
    
    if not nina_armature.animation_data or not nina_armature.animation_data.action:
        print("❌ ERROR: Nina no tiene animación")
        exit(1)
    
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    
    print(f"   ✅ Nina Armature: {nina_armature.name}")
    print(f"   ✅ Huesos Nina: {len(nina_armature.data.bones)}")
    print(f"   ✅ Animación: {nina_action.name}")
    print(f"   ✅ Frames: {frame_start} a {frame_end}")
    
    # PASO 4: Verificar huesos
    print(f"\n🦴 Verificando compatibilidad de huesos...")
    nancy_bones = set(nancy_armature.data.bones.keys())
    nina_bones = set(nina_armature.data.bones.keys())
    bones_comunes = nancy_bones & nina_bones
    
    print(f"   Nancy: {len(nancy_bones)} huesos")
    print(f"   Nina: {len(nina_bones)} huesos")
    print(f"   Comunes: {len(bones_comunes)} huesos")
    
    if len(bones_comunes) == len(nancy_bones) and len(bones_comunes) == len(nina_bones):
        print(f"   ✅ Todos los huesos coinciden perfectamente")
    
    # PASO 5: Usar Rokoko Studio para retargeting
    print(f"\n🔄 Aplicando retargeting con Rokoko Studio...")
    
    # Verificar si Rokoko está disponible
    if 'rokoko' not in dir(bpy.ops):
        print("   ⚠️ Rokoko Studio no disponible, usando método manual mejorado")
        
        # Método manual mejorado con bake
        bpy.context.scene.frame_start = frame_start
        bpy.context.scene.frame_end = frame_end
        
        # Seleccionar Nina como activo
        bpy.context.view_layer.objects.active = nina_armature
        nina_armature.select_set(True)
        nancy_armature.select_set(True)
        
        # Crear constraint en Nancy que siga a Nina
        print(f"   📌 Creando constraints Copy Transforms...")
        nancy_armature.select_set(True)
        bpy.context.view_layer.objects.active = nancy_armature
        
        constraints_creados = 0
        for nancy_bone in nancy_armature.pose.bones:
            if nancy_bone.name in nina_armature.pose.bones:
                # Crear constraint Copy Transforms
                constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = nina_armature
                constraint.subtarget = nancy_bone.name
                constraints_creados += 1
        
        print(f"   ✅ {constraints_creados} constraints creados")
        
        # Bake la animación
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
        
        print(f"   ✅ Animación bakeada")
        
        # Verificar que Nancy tenga la animación
        if nancy_armature.animation_data and nancy_armature.animation_data.action:
            nancy_new_action = nancy_armature.animation_data.action
            print(f"   ✅ Nancy ahora tiene action: {nancy_new_action.name}")
            print(f"   ✅ FCurves: {len(nancy_new_action.fcurves)}")
        else:
            print(f"   ❌ ERROR: Nancy no recibió la animación")
            exit(1)
    
    # PASO 6: Eliminar TODOS los objetos que no sean de Nancy
    print(f"\n🗑️ Eliminando objetos de Nina...")
    objetos_nancy = []
    
    # Guardar solo objetos de Nancy (los que estaban desde el inicio)
    for obj in bpy.data.objects:
        if obj == nancy_armature or obj.parent == nancy_armature:
            objetos_nancy.append(obj)
    
    # Eliminar todo lo demás
    objetos_eliminar = []
    for obj in bpy.data.objects:
        if obj not in objetos_nancy:
            objetos_eliminar.append(obj)
    
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    print(f"   ✅ {len(objetos_eliminar)} objetos eliminados")
    print(f"   ✅ {len(objetos_nancy)} objetos de Nancy mantenidos")
    
    # PASO 7: Verificar animación en Nancy
    print(f"\n✓ Verificando animación en Nancy...")
    bpy.context.scene.frame_set(frame_start)
    bpy.context.view_layer.update()
    
    # Probar algunos frames
    test_frames = [frame_start, frame_start + 10, frame_start + 20, frame_end]
    
    for frame in test_frames:
        bpy.context.scene.frame_set(frame)
        bpy.context.view_layer.update()
        
        if "LeftHand" in nancy_armature.pose.bones:
            bone = nancy_armature.pose.bones["LeftHand"]
            rot = bone.rotation_quaternion
            print(f"   Frame {frame}: LeftHand rot = ({rot.w:.3f}, {rot.x:.3f}, {rot.y:.3f}, {rot.z:.3f})")
    
    # PASO 8: Asegurar que frame range esté correcto
    print(f"\n📊 Preparando para exportar...")
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    
    # Verificar action una vez más
    if nancy_armature.animation_data and nancy_armature.animation_data.action:
        action = nancy_armature.animation_data.action
        print(f"   Action: {action.name}")
        print(f"   FCurves: {len(action.fcurves)}")
        print(f"   Frame range: {action.frame_range}")
    
    # PASO 9: Guardar blend para inspección
    blend_file = NANCY_OUTPUT.parent / "Nancy_a_la_orden_DEBUG.blend"
    print(f"\n💾 Guardando .blend para debug...")
    bpy.ops.wm.save_as_mainfile(filepath=str(blend_file))
    print(f"   ✅ Guardado: {blend_file.name}")
    
    # PASO 10: Exportar a GLB
    print(f"\n💾 Exportando a GLB...")
    NANCY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    # Probar FBX primero (formato más compatible con animaciones)
    fbx_file = NANCY_OUTPUT.with_suffix('.fbx')
    print(f"💾 Exportando primero a FBX: {fbx_file.name}...")
    bpy.ops.export_scene.fbx(
        filepath=str(fbx_file),
        use_selection=False,
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=False,
        bake_anim_use_all_actions=False,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=0.0,
        add_leaf_bones=False,
        path_mode='AUTO'
    )
    
    # Limpiar escena y re-importar FBX
    print("📦 Re-importando FBX...")
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.fbx(filepath=str(fbx_file))
    
    # Exportar a GLB desde FBX
    print("💾 Exportando FBX a GLB...")
    bpy.ops.export_scene.gltf(
        filepath=str(NANCY_OUTPUT),
        export_format='GLB',
        export_animations=True,
        export_frame_range=True,
        export_force_sampling=True,
        export_def_bones=False,
        export_optimize_animation_size=False
    )
    
    if NANCY_OUTPUT.exists():
        size_mb = NANCY_OUTPUT.stat().st_size / (1024 * 1024)
        print(f"   ✅ Archivo generado: {size_mb:.1f} MB")
        
        # VERIFICACIÓN FINAL
        print(f"\n🔍 Verificación final del archivo exportado...")
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))
        
        test_arm = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                test_arm = obj
                break
        
        if test_arm and test_arm.animation_data and test_arm.animation_data.action:
            test_action = test_arm.animation_data.action
            print(f"   ✅ Animación: {test_action.name}")
            print(f"   ✅ FCurves: {len(test_action.fcurves)}")
            
            # Probar movimiento
            bpy.context.scene.frame_set(frame_start)
            bpy.context.view_layer.update()
            if "LeftHand" in test_arm.pose.bones:
                bone_start = test_arm.pose.bones["LeftHand"]
                rot_start = bone_start.rotation_quaternion.copy()
                
                bpy.context.scene.frame_set(frame_end)
                bpy.context.view_layer.update()
                rot_end = test_arm.pose.bones["LeftHand"].rotation_quaternion
                
                diff = abs(rot_start.w - rot_end.w) + abs(rot_start.x - rot_end.x) + abs(rot_start.y - rot_end.y) + abs(rot_start.z - rot_end.z)
                
                print(f"   Rot inicio: ({rot_start.w:.3f}, {rot_start.x:.3f}, {rot_start.y:.3f}, {rot_start.z:.3f})")
                print(f"   Rot final:  ({rot_end.w:.3f}, {rot_end.x:.3f}, {rot_end.y:.3f}, {rot_end.z:.3f})")
                print(f"   Diferencia: {diff:.3f}")
                
                if diff > 0.01:
                    print(f"\n{'='*80}")
                    print("✅ ✅ ✅ ÉXITO - ANIMACIÓN FUNCIONANDO ✅ ✅ ✅")
                    print(f"Nancy tiene su malla con la animación 'a la orden' de Nina")
                    print(f"{'='*80}")
                else:
                    print(f"\n⚠️ ADVERTENCIA: LeftHand no se mueve")
        else:
            print(f"   ❌ ERROR: Archivo no tiene animación")
    else:
        print(f"   ❌ ERROR: No se generó el archivo")
        
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    exit(1)
