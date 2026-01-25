import bpy
from pathlib import Path

print("="*80)
print("TRANSFERENCIA ESPECÍFICA: Nina 'a la orden' → Nancy")
print("="*80)

# Rutas específicas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_MODEL = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "cortesia" / "Nina_resultado_a la orden.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "cortesia" / "Nancy_resultado_a la orden.glb"

print(f"\n📂 Archivos:")
print(f"   Modelo Nancy: {NANCY_MODEL.name}")
print(f"   Animación Nina: {NINA_FILE.name}")
print(f"   Salida: {NANCY_OUTPUT}")

# Verificar que existan los archivos
if not NANCY_MODEL.exists():
    print(f"❌ ERROR: No existe {NANCY_MODEL}")
    exit(1)

if not NINA_FILE.exists():
    print(f"❌ ERROR: No existe {NINA_FILE}")
    exit(1)

try:
    # PASO 1: Limpiar escena
    print(f"\n🧹 Limpiando escena...")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # PASO 2: Cargar modelo base Nancy
    print(f"\n📦 Cargando modelo base Nancy (sin animación)...")
    bpy.ops.import_scene.gltf(filepath=str(NANCY_MODEL))
    
    nancy_armature = None
    nancy_meshes = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            nancy_armature = obj
        elif obj.type == 'MESH':
            nancy_meshes.append(obj)
    
    if not nancy_armature:
        print("❌ ERROR: No se encontró armature de Nancy")
        exit(1)
    
    print(f"   ✅ Armature: {nancy_armature.name}")
    print(f"   ✅ Mallas: {len(nancy_meshes)}")
    for mesh in nancy_meshes:
        print(f"      - {mesh.name}")
    
    # Verificar que Nancy está en pose A/T (rest pose)
    print(f"\n🧍 Verificando que Nancy esté en pose rest...")
    nancy_armature.data.pose_position = 'REST'
    bpy.context.view_layer.update()
    
    # Eliminar cualquier animación previa de Nancy
    if nancy_armature.animation_data:
        nancy_armature.animation_data_clear()
        print(f"   🗑️ Animación previa eliminada")
    
    # PASO 3: Importar animación de Nina
    print(f"\n🎬 Importando animación de Nina 'a la orden'...")
    objetos_antes = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
    objetos_nina = set(bpy.data.objects) - objetos_antes
    
    nina_armature = None
    for obj in objetos_nina:
        if obj.type == 'ARMATURE':
            nina_armature = obj
            break
    
    if not nina_armature:
        print("❌ ERROR: No se encontró armature de Nina")
        exit(1)
    
    # PASO 4: Verificar animación de Nina
    if not nina_armature.animation_data or not nina_armature.animation_data.action:
        print("❌ ERROR: Nina no tiene animación")
        exit(1)
    
    nina_action = nina_armature.animation_data.action
    frame_start = nina_action.frame_range[0]
    frame_end = nina_action.frame_range[1]
    frames_total = frame_end - frame_start
    
    print(f"   ✅ Action: {nina_action.name}")
    print(f"   ✅ Frames: {frames_total:.0f} ({frame_start:.0f} a {frame_end:.0f})")
    print(f"   ✅ FCurves: {len(nina_action.fcurves)}")
    
    # PASO 5: Verificar compatibilidad de huesos
    print(f"\n🦴 Verificando huesos...")
    bones_nancy = set(nancy_armature.data.bones.keys())
    bones_nina = set(nina_armature.data.bones.keys())
    bones_comunes = bones_nancy & bones_nina
    
    print(f"   Nancy: {len(bones_nancy)} huesos")
    print(f"   Nina: {len(bones_nina)} huesos")
    print(f"   Comunes: {len(bones_comunes)} huesos")
    
    if len(bones_comunes) < 50:
        print(f"   ❌ ERROR: Muy pocos huesos comunes")
        exit(1)
    
    # PASO 6: Copiar animación manualmente keyframe por keyframe
    print(f"\n📋 Copiando animación manualmente...")
    
    # Crear animation data en Nancy
    if not nancy_armature.animation_data:
        nancy_armature.animation_data_create()
    
    # Crear nueva action para Nancy
    nancy_action = bpy.data.actions.new(name="Nancy_a_la_orden")
    nancy_armature.animation_data.action = nancy_action
    
    # Copiar cada FCurve manualmente
    keyframes_copiados = 0
    for fc in nina_action.fcurves:
        # Crear nueva FCurve en Nancy con el mismo data_path
        new_fc = nancy_action.fcurves.new(
            data_path=fc.data_path,
            index=fc.array_index
        )
        
        # Copiar keyframes
        for kf in fc.keyframe_points:
            new_fc.keyframe_points.insert(
                kf.co[0],
                kf.co[1],
                options={'FAST'}
            )
            keyframes_copiados += 1
    
    print(f"   ✅ Keyframes copiados: {keyframes_copiados}")
    print(f"   ✅ FCurves: {len(nancy_action.fcurves)}")
    
    # Actualizar todas las FCurves
    for fc in nancy_action.fcurves:
        fc.update()
    
    # Cambiar Nancy a POSE mode para que use la animación
    nancy_armature.data.pose_position = 'POSE'
    
    # Establecer frame range
    bpy.context.scene.frame_start = int(frame_start)
    bpy.context.scene.frame_end = int(frame_end)
    
    # Forzar actualización de la escena
    bpy.context.view_layer.update()
    
    print(f"   ✅ Action: {nancy_action.name}")
    
    # PASO 7: Verificar que la animación se aplicó correctamente
    print(f"\n✓ Verificando animación aplicada...")
    
    # Verificar que la action está asignada
    if nancy_armature.animation_data and nancy_armature.animation_data.action:
        print(f"   ✅ Action asignada: {nancy_armature.animation_data.action.name}")
    else:
        print(f"   ❌ Action NO asignada!")
        exit(1)
    
    # Buscar FCurves de LeftHand para debug (sin el corchete de cierre)
    lefthand_fcurves = [fc for fc in nancy_action.fcurves if "LeftHand" in fc.data_path and "rotation" in fc.data_path]
    print(f"   📊 FCurves de LeftHand rotation: {len(lefthand_fcurves)}")
    if lefthand_fcurves:
        sample_fc = lefthand_fcurves[0]
        print(f"      Ejemplo: {sample_fc.data_path}[{sample_fc.array_index}] con {len(sample_fc.keyframe_points)} keyframes")
    else:
        # Mostrar las primeras 5 FCurves para ver el formato
        print(f"   ⚠️ No se encontraron FCurves de LeftHand. Mostrando primeras 5 FCurves:")
        for fc in nancy_action.fcurves[:5]:
            print(f"      - {fc.data_path}[{fc.array_index}]")
    
    # Probar algunos frames clave
    test_frames = [int(frame_start), int(frame_start + frames_total/4), int(frame_start + frames_total/2), int(frame_end)]
    
    for frame in test_frames:
        bpy.context.scene.frame_set(frame)
        bpy.context.view_layer.update()
        
        # Verificar que algún hueso se mueva (ej: LeftHand)
        if "LeftHand" in nancy_armature.pose.bones:
            bone = nancy_armature.pose.bones["LeftHand"]
            rot = bone.rotation_quaternion
            print(f"   Frame {frame}: LeftHand rot = ({rot.w:.3f}, {rot.x:.3f}, {rot.y:.3f}, {rot.z:.3f})")
    
    # PASO 8: Eliminar objetos de Nina
    print(f"\n🗑️ Eliminando objetos de Nina...")
    for obj in objetos_nina:
        bpy.data.objects.remove(obj, do_unlink=True)
    print(f"   ✅ {len(objetos_nina)} objetos eliminados")
    
    # PASO 9: Verificación final antes de exportar
    print(f"\n📊 Verificación final:")
    objetos_finales = list(bpy.data.objects)
    armatures_finales = [o for o in objetos_finales if o.type == 'ARMATURE']
    meshes_finales = [o for o in objetos_finales if o.type == 'MESH']
    
    print(f"   Armatures: {len(armatures_finales)}")
    print(f"   Mallas: {len(meshes_finales)}")
    
    if len(armatures_finales) != 1:
        print(f"   ❌ ERROR: Debería haber 1 armature")
        exit(1)
    
    if len(meshes_finales) < 5:
        print(f"   ⚠️ Advertencia: Pocas mallas")
    
    # Verificar que el armature tenga la animación
    if not nancy_armature.animation_data or not nancy_armature.animation_data.action:
        print(f"   ❌ ERROR: Nancy perdió la animación")
        exit(1)
    
    print(f"   ✅ Nancy tiene animación: {nancy_armature.animation_data.action.name}")
    
    # PASO 10: Exportar
    print(f"\n💾 Exportando a GLB...")
    
    # Asegurar que la carpeta de salida existe
    NANCY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.gltf(
        filepath=str(NANCY_OUTPUT),
        export_format='GLB',
        export_animations=True,
        export_frame_range=True,
        export_current_frame=False,
        export_force_sampling=False,  # NO forzar sampling, usar keyframes originales
        export_def_bones=False,
        export_optimize_animation_size=False,
        export_nla_strips=False,
        export_apply=False  # NO aplicar transformaciones
    )
    
    # VERIFICACIÓN POST-EXPORTACIÓN
    if NANCY_OUTPUT.exists():
        size_mb = NANCY_OUTPUT.stat().st_size / (1024 * 1024)
        print(f"   ✅ Archivo generado: {NANCY_OUTPUT.name}")
        print(f"   ✅ Tamaño: {size_mb:.1f} MB")
        
        # Verificar el archivo exportado
        print(f"\n🔍 Verificando archivo exportado...")
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))
        
        test_arm = None
        test_meshes = []
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                test_arm = obj
            elif obj.type == 'MESH':
                test_meshes.append(obj)
        
        print(f"   Armatures: {1 if test_arm else 0}")
        print(f"   Mallas: {len(test_meshes)}")
        
        if test_arm and test_arm.animation_data and test_arm.animation_data.action:
            test_action = test_arm.animation_data.action
            test_frames = test_action.frame_range[1] - test_action.frame_range[0]
            print(f"   Animación: {test_action.name}")
            print(f"   Frames: {test_frames:.0f}")
            
            if abs(test_frames - frames_total) < 2:
                print(f"\n{'='*80}")
                print("✅ ✅ ✅ ÉXITO TOTAL ✅ ✅ ✅")
                print(f"Nancy con malla propia + animación 'a la orden' de Nina")
                print(f"{'='*80}")
            else:
                print(f"\n⚠️ Frames no coinciden: esperado {frames_total:.0f}, obtenido {test_frames:.0f}")
        else:
            print(f"\n❌ ERROR: Archivo exportado no tiene animación")
    else:
        print(f"   ❌ ERROR: No se generó el archivo")
        exit(1)
        
except Exception as e:
    print(f"\n❌ ERROR CRÍTICO: {str(e)}")
    import traceback
    traceback.print_exc()
    exit(1)
