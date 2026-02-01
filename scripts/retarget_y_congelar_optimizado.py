"""
Script Super Optimizado: Retarget + Congelamiento en un solo paso
Duvall → Luis con congelamiento de tren inferior automático

USO:
blender --background --python scripts/retarget_y_congelar_optimizado.py -- profesion
"""

import bpy
from pathlib import Path
import time
import sys
import shutil

print("="*80)
print("🚀 RETARGET + CONGELAMIENTO: Duvall → Luis → Freeze → GLB")
print("="*80)

# Obtener categoría del argumento
try:
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]
    if not argv:
        print("❌ ERROR: Debes especificar una categoría")
        print("   Uso: blender --background --python script.py -- profesion")
        sys.exit(1)
    CATEGORIA = argv[0]
    print(f"📁 Categoría: {CATEGORIA}")
except (ValueError, IndexError):
    print("❌ ERROR: Debes especificar una categoría")
    sys.exit(1)

# Rutas base
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
LUIS_MODEL = BASE_DIR / "Luis" / "Luis.glb"
DUVALL_DIR = BASE_DIR / "Duvall" / CATEGORIA
LUIS_OUTPUT_DIR = BASE_DIR / "Luis" / CATEGORIA

# Huesos del tren inferior a congelar
LOWER_BODY_BONES = [
    'Hips',
    'Spine',
    'Spine1',
    'Spine2',
    'LeftUpLeg',
    'LeftLeg',
    'LeftFoot',
    'LeftToeBase',
    'LeftToe_End',
    'RightUpLeg',
    'RightLeg',
    'RightFoot',
    'RightToeBase',
    'RightToe_End'
]

# Verificar carpeta
if not DUVALL_DIR.exists():
    print(f"❌ ERROR: No existe {DUVALL_DIR}")
    sys.exit(1)

# Obtener animaciones
animaciones = []
for glb_file in DUVALL_DIR.glob("Duvall_resultado_*.glb"):
    nombre = glb_file.stem.replace("Duvall_resultado_", "")
    animaciones.append(nombre)

if not animaciones:
    print(f"❌ No hay animaciones en {DUVALL_DIR}")
    sys.exit(1)

print(f"✅ {len(animaciones)} animaciones encontradas")

def encontrar_accion_con_movimiento(armature, actions):
    """Encuentra la acción con movimiento real"""
    # Buscar la acción más larga con fcurves
    best_action = None
    max_frames = 0
    
    for action in actions:
        if not action.fcurves:
            continue
        
        frame_start, frame_end = action.frame_range
        num_frames = frame_end - frame_start
        
        if num_frames > max_frames:
            max_frames = num_frames
            best_action = action
    
    return best_action

def congelar_tren_inferior(armature, action, frame_start, frame_end):
    """Congela completamente el tren inferior"""
    print(f"   🔒 Congelando tren inferior...")
    
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    
    frozen_count = 0
    
    for bone_name in LOWER_BODY_BONES:
        if bone_name not in armature.pose.bones:
            continue
        
        pose_bone = armature.pose.bones[bone_name]
        
        # Guardar pose inicial
        bpy.context.scene.frame_set(frame_start)
        bpy.context.view_layer.update()
        
        initial_location = pose_bone.location.copy()
        initial_rotation_quat = pose_bone.rotation_quaternion.copy() if pose_bone.rotation_mode == 'QUATERNION' else None
        initial_rotation_euler = pose_bone.rotation_euler.copy() if pose_bone.rotation_mode != 'QUATERNION' else None
        initial_scale = pose_bone.scale.copy()
        
        # Eliminar keyframes existentes
        fcurves_to_remove = []
        for fcurve in action.fcurves:
            if f'pose.bones["{bone_name}"]' in fcurve.data_path:
                fcurves_to_remove.append(fcurve)
        
        for fcurve in fcurves_to_remove:
            action.fcurves.remove(fcurve)
        
        # Aplicar pose congelada en todos los frames
        for frame in range(frame_start, frame_end + 1):
            bpy.context.scene.frame_set(frame)
            
            pose_bone.location = initial_location
            if initial_rotation_quat is not None:
                pose_bone.rotation_quaternion = initial_rotation_quat
            if initial_rotation_euler is not None:
                pose_bone.rotation_euler = initial_rotation_euler
            pose_bone.scale = initial_scale
            
            pose_bone.keyframe_insert(data_path="location", frame=frame)
            if pose_bone.rotation_mode == 'QUATERNION':
                pose_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
            else:
                pose_bone.keyframe_insert(data_path="rotation_euler", frame=frame)
            pose_bone.keyframe_insert(data_path="scale", frame=frame)
        
        frozen_count += 1
    
    bpy.ops.object.mode_set(mode='OBJECT')
    print(f"   ✅ {frozen_count} huesos congelados")

def procesar_animacion(animacion_nombre):
    """Proceso completo: retarget + congelamiento + export + congelar Duvall original"""
    
    print(f"\n{'='*80}")
    print(f"📝 {animacion_nombre}")
    print(f"{'='*80}")
    
    duvall_file = DUVALL_DIR / f"Duvall_resultado_{animacion_nombre}.glb"
    luis_glb_temp = Path(f"/tmp/luis_temp_{animacion_nombre}.glb")
    luis_glb_final = LUIS_OUTPUT_DIR / f"Luis_resultado_{animacion_nombre}.glb"
    
    if not duvall_file.exists():
        print(f"❌ No existe: {duvall_file}")
        return False
    
    inicio = time.time()
    
    try:
        # === PASO 1: RETARGET ===
        print(f"🔄 [1/5] Retargeting...")
        
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar Luis
        bpy.ops.import_scene.gltf(filepath=str(LUIS_MODEL))
        luis_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                luis_armature = obj
                luis_armature.name = "Luis_Armature"
                break
        
        if not luis_armature:
            print("❌ No armature Luis")
            return False
        
        if luis_armature.animation_data:
            luis_armature.animation_data_clear()
        
        # Importar Duvall con animación
        bpy.ops.import_scene.gltf(filepath=str(duvall_file))
        duvall_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != luis_armature:
                duvall_armature = obj
                duvall_armature.name = "Duvall_Armature"
                break
        
        if not duvall_armature or not duvall_armature.animation_data or not duvall_armature.animation_data.action:
            print("❌ Duvall sin animación")
            return False
        
        duvall_action = duvall_armature.animation_data.action
        frame_start = int(duvall_action.frame_range[0])
        frame_end = int(duvall_action.frame_range[1])
        
        bpy.context.scene.frame_start = frame_start
        bpy.context.scene.frame_end = frame_end
        
        # Crear constraints
        bpy.context.view_layer.objects.active = luis_armature
        luis_armature.select_set(True)
        
        constraints_count = 0
        for luis_bone in luis_armature.pose.bones:
            if luis_bone.name in duvall_armature.pose.bones:
                constraint = luis_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = duvall_armature
                constraint.subtarget = luis_bone.name
                constraints_count += 1
        
        print(f"   ✅ {constraints_count} constraints")
        
        # === PASO 2: BAKE ===
        print(f"🔥 [2/5] Baking...")
        bpy.ops.object.select_all(action='DESELECT')
        luis_armature.select_set(True)
        bpy.context.view_layer.objects.active = luis_armature
        
        bpy.ops.nla.bake(
            frame_start=frame_start,
            frame_end=frame_end,
            step=1,
            only_selected=False,
            visual_keying=True,
            clear_constraints=True,
            clear_parents=False,
            use_current_action=True,
            clean_curves=False,
            bake_types={'POSE'}
        )
        
        if not luis_armature.animation_data or not luis_armature.animation_data.action:
            print("❌ Luis sin animación después del bake")
            return False
        
        baked_action = luis_armature.animation_data.action
        num_fcurves = len(baked_action.fcurves) if baked_action.fcurves else 0
        frame_range = baked_action.frame_range if baked_action else (0, 0)
        print(f"   ✅ Bake completado: {num_fcurves} fcurves, frames {frame_range[0]:.0f}-{frame_range[1]:.0f}")
        
        # === PASO 3: LIMPIAR ACCIONES ===
        print(f"🧹 [3/5] Limpiando acciones...")
        
        # Mantener solo la acción bakeada actual
        current_action = luis_armature.animation_data.action
        
        if not current_action or not current_action.fcurves:
            print("❌ Sin acción válida después del bake")
            return False
        
        # Asegurar que la acción está correctamente nombrada y vinculada
        current_action.name = f"Luis_{animacion_nombre}_Action"
        current_action.use_fake_user = True
        
        # Eliminar otras acciones
        removed = 0
        for action in list(bpy.data.actions):
            if action != current_action:
                bpy.data.actions.remove(action)
                removed += 1
        
        print(f"   🗑️ {removed} acciones eliminadas, mantenida: {current_action.name}")
        
        # Verificar que la acción sigue asignada
        luis_armature.animation_data.action = current_action
        luis_armature.animation_data.use_nla = False
        
        print(f"   ✅ Acción asignada: {len(current_action.fcurves)} fcurves")
        
        # === PASO 4: CONGELAR TREN INFERIOR ===
        print(f"❄️ [4/5] Congelando tren inferior...")
        congelar_tren_inferior(luis_armature, current_action, frame_start, frame_end)
        
        # Verificar que la acción sigue válida después del congelamiento
        if not luis_armature.animation_data or not luis_armature.animation_data.action:
            print("❌ Acción perdida después del congelamiento")
            return False
        
        print(f"   ✅ Congelamiento completado, acción intacta")
        
        # === PASO 5: ELIMINAR OBJETOS DE DUVALL ===
        objetos_luis = []
        for obj in bpy.data.objects:
            if obj == luis_armature or obj.parent == luis_armature:
                objetos_luis.append(obj)
        
        objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_luis]
        for obj in objetos_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # === PASO 6: EXPORTAR GLB ===
        print(f"📤 [5/5] Exportando GLB...")
        
        # Verificación final antes de exportar
        if not luis_armature.animation_data or not luis_armature.animation_data.action:
            print("❌ ERROR CRÍTICO: Acción perdida antes de exportar")
            return False
        
        final_action = luis_armature.animation_data.action
        print(f"   📋 Exportando acción: {final_action.name}")
        print(f"   📊 FCurves: {len(final_action.fcurves)}")
        print(f"   🎬 Frames: {final_action.frame_range[0]:.0f} - {final_action.frame_range[1]:.0f}")
        
        # Asegurar que el armature está seleccionado y activo
        bpy.ops.object.select_all(action='DESELECT')
        luis_armature.select_set(True)
        bpy.context.view_layer.objects.active = luis_armature
        
        # Seleccionar todos los objetos relacionados con Luis
        for obj in bpy.data.objects:
            if obj == luis_armature or obj.parent == luis_armature:
                obj.select_set(True)
        
        bpy.ops.export_scene.gltf(
            filepath=str(luis_glb_temp),
            export_format='GLB',
            export_image_format='AUTO',
            export_texcoords=True,
            export_normals=True,
            export_draco_mesh_compression_enable=False,
            export_materials='EXPORT',
            export_cameras=False,
            use_selection=True,
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
        
        if not luis_glb_temp.exists():
            print("❌ No se generó GLB")
            return False
        
        # Copiar a destino final
        luis_glb_final.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(luis_glb_temp, luis_glb_final)
        luis_glb_temp.unlink()
        
        if not luis_glb_final.exists():
            print("❌ Error al copiar")
            return False
        
        size_kb = luis_glb_final.stat().st_size / 1024
        print(f"   ✅ Luis generado: {size_kb:.1f} KB")
        
        # === PASO 7: CONGELAR DUVALL ORIGINAL ===
        print(f"❄️ [EXTRA] Congelando Duvall original...")
        
        # Limpiar y cargar Duvall original
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=str(duvall_file))
        
        duvall_armature_freeze = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                duvall_armature_freeze = obj
                break
        
        if duvall_armature_freeze and duvall_armature_freeze.animation_data and duvall_armature_freeze.animation_data.action:
            duvall_action_freeze = duvall_armature_freeze.animation_data.action
            frame_start_duvall = int(duvall_action_freeze.frame_range[0])
            frame_end_duvall = int(duvall_action_freeze.frame_range[1])
            
            # Congelar tren inferior en Duvall
            congelar_tren_inferior(duvall_armature_freeze, duvall_action_freeze, frame_start_duvall, frame_end_duvall)
            
            # Exportar Duvall congelado
            duvall_temp = Path(f"/tmp/duvall_frozen_{animacion_nombre}.glb")
            bpy.ops.object.select_all(action='SELECT')
            
            bpy.ops.export_scene.gltf(
                filepath=str(duvall_temp),
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
            
            if duvall_temp.exists():
                shutil.copy2(duvall_temp, duvall_file)
                duvall_temp.unlink()
                print(f"   ✅ Duvall congelado")
        
        tiempo = time.time() - inicio
        print(f"\n   🎉 COMPLETADO: {tiempo:.1f}s total")
        return True
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

# === PROCESAR TODAS ===
print(f"\n{'#'*80}")
print(f"🚀 INICIANDO PROCESO COMPLETO")
print(f"{'#'*80}\n")

resultados = {
    "exitosos": [],
    "fallidos": []
}

inicio_total = time.time()

for i, animacion in enumerate(animaciones, 1):
    print(f"\n[{i}/{len(animaciones)}]")
    exito = procesar_animacion(animacion)
    
    if exito:
        resultados["exitosos"].append(animacion)
    else:
        resultados["fallidos"].append(animacion)

tiempo_total = time.time() - inicio_total

# === RESUMEN ===
print(f"\n{'='*80}")
print(f"📊 RESUMEN - {CATEGORIA.upper()}")
print(f"{'='*80}")
print(f"⏱️  Tiempo: {tiempo_total/60:.1f} minutos")
print(f"⚡ Promedio: {tiempo_total/len(animaciones):.1f}s/animación")
print(f"✅ Exitosos: {len(resultados['exitosos'])}/{len(animaciones)}")
print(f"❌ Fallidos: {len(resultados['fallidos'])}/{len(animaciones)}")

if resultados["fallidos"]:
    print(f"\n❌ Fallidas:")
    for item in resultados["fallidos"]:
        print(f"   - {item}")

if resultados["exitosos"]:
    print(f"\n✅ Archivos en: {LUIS_OUTPUT_DIR}")
    print(f"\n🎉 PROCESO COMPLETADO - RETARGET + CONGELAMIENTO")

print(f"{'='*80}")
