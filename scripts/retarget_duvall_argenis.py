"""
Script Optimizado: Retargetear animaciones de Duvall a Argenis
Proceso completo sin congelamiento

USO:
blender --background --python scripts/retarget_duvall_argenis.py -- profesion
"""

import bpy
from pathlib import Path
import time
import sys
import shutil

print("="*80)
print("🚀 RETARGET OPTIMIZADO: Duvall → Argenis → GLB")
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
ARGENIS_MODEL = BASE_DIR / "Argenis" / "Argenis.glb"
DUVALL_DIR = BASE_DIR / "Duvall" / CATEGORIA
ARGENIS_OUTPUT_DIR = BASE_DIR / "Argenis" / CATEGORIA

# Verificar carpeta
if not DUVALL_DIR.exists():
    print(f"❌ ERROR: No existe {DUVALL_DIR}")
    sys.exit(1)

# Verificar modelo Argenis
if not ARGENIS_MODEL.exists():
    print(f"❌ ERROR: No existe el modelo Argenis en {ARGENIS_MODEL}")
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
    # Huesos clave a revisar (en orden de prioridad)
    bones_to_check = ['Hips', 'LeftHand', 'RightHand', 'LeftArm', 'RightArm', 'Spine', 'Spine1']
    
    for action in actions:
        if not armature.animation_data:
            armature.animation_data_create()
        
        armature.animation_data.action = action
        armature.animation_data.use_nla = False
        
        frame_start, frame_end = action.frame_range
        
        # Intentar con varios huesos
        for bone_name in bones_to_check:
            if bone_name in armature.pose.bones:
                bpy.context.scene.frame_set(int(frame_start))
                bpy.context.view_layer.update()
                pos_start = armature.pose.bones[bone_name].matrix.translation.copy()
                rot_start = armature.pose.bones[bone_name].matrix.to_quaternion()
                
                bpy.context.scene.frame_set(int(frame_end))
                bpy.context.view_layer.update()
                pos_end = armature.pose.bones[bone_name].matrix.translation.copy()
                rot_end = armature.pose.bones[bone_name].matrix.to_quaternion()
                
                # Verificar movimiento en posición O rotación
                pos_diff = (pos_start - pos_end).length
                rot_diff = (rot_start.rotation_difference(rot_end)).angle
                
                if pos_diff > 0.001 or rot_diff > 0.01:
                    print(f"   ✓ Movimiento detectado en {bone_name}: pos={pos_diff:.4f}, rot={rot_diff:.4f}")
                    return action
    
    print(f"   ⚠️ No se detectó movimiento en {len(actions)} acciones")
    return None

def procesar_animacion(animacion_nombre):
    """Proceso completo: retarget + limpieza + export"""
    
    print(f"\n{'='*80}")
    print(f"📝 {animacion_nombre}")
    print(f"{'='*80}")
    
    duvall_file = DUVALL_DIR / f"Duvall_resultado_{animacion_nombre}.glb"
    argenis_glb_temp = Path(f"/tmp/argenis_temp_{animacion_nombre}.glb")
    argenis_glb_final = ARGENIS_OUTPUT_DIR / f"Argenis_resultado_{animacion_nombre}.glb"
    
    if not duvall_file.exists():
        print(f"❌ No existe: {duvall_file}")
        return False
    
    inicio = time.time()
    
    try:
        # === PASO 1: RETARGET ===
        print(f"🔄 [1/4] Retargeting...")
        
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar Argenis
        bpy.ops.import_scene.gltf(filepath=str(ARGENIS_MODEL))
        argenis_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                argenis_armature = obj
                argenis_armature.name = "Argenis_Armature"
                break
        
        if not argenis_armature:
            print("❌ No armature Argenis")
            return False
        
        if argenis_armature.animation_data:
            argenis_armature.animation_data_clear()
        
        # Importar Duvall con animación
        bpy.ops.import_scene.gltf(filepath=str(duvall_file))
        duvall_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != argenis_armature:
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
        bpy.context.view_layer.objects.active = argenis_armature
        argenis_armature.select_set(True)
        
        constraints_count = 0
        for argenis_bone in argenis_armature.pose.bones:
            if argenis_bone.name in duvall_armature.pose.bones:
                constraint = argenis_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = duvall_armature
                constraint.subtarget = argenis_bone.name
                constraints_count += 1
        
        print(f"   ✅ {constraints_count} constraints")
        
        # === PASO 2: BAKE ===
        print(f"🔥 [2/4] Baking...")
        bpy.ops.object.select_all(action='DESELECT')
        argenis_armature.select_set(True)
        bpy.context.view_layer.objects.active = argenis_armature
        
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
        
        if not argenis_armature.animation_data or not argenis_armature.animation_data.action:
            print("❌ Argenis sin animación después del bake")
            return False
        
        baked_action = argenis_armature.animation_data.action
        num_fcurves = len(baked_action.fcurves) if baked_action.fcurves else 0
        frame_range = baked_action.frame_range if baked_action else (0, 0)
        print(f"   ✅ Bake completado: {num_fcurves} fcurves, frames {frame_range[0]:.0f}-{frame_range[1]:.0f}")
        
        # === PASO 3: LIMPIAR ACCIONES ===
        print(f"🧹 [3/4] Limpiando acciones...")
        
        # Mantener solo la acción bakeada actual
        current_action = argenis_armature.animation_data.action
        
        if not current_action or not current_action.fcurves:
            print("❌ Sin acción válida después del bake")
            return False
        
        # Asegurar que la acción está correctamente nombrada y vinculada
        current_action.name = f"Argenis_{animacion_nombre}_Action"
        current_action.use_fake_user = True
        
        # Eliminar otras acciones
        removed = 0
        for action in list(bpy.data.actions):
            if action != current_action:
                bpy.data.actions.remove(action)
                removed += 1
        
        print(f"   🗑️ {removed} acciones eliminadas, mantenida: {current_action.name}")
        
        # Verificar que la acción sigue asignada
        argenis_armature.animation_data.action = current_action
        argenis_armature.animation_data.use_nla = False
        
        print(f"   ✅ Acción asignada: {len(current_action.fcurves)} fcurves")
        
        # === PASO 4: ELIMINAR OBJETOS DE DUVALL ===
        objetos_argenis = []
        for obj in bpy.data.objects:
            if obj == argenis_armature or obj.parent == argenis_armature:
                objetos_argenis.append(obj)
        
        objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_argenis]
        for obj in objetos_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # === PASO 5: EXPORTAR GLB ===
        print(f"📤 [4/4] Exportando GLB...")
        
        # Verificación final antes de exportar
        if not argenis_armature.animation_data or not argenis_armature.animation_data.action:
            print("❌ ERROR CRÍTICO: Acción perdida antes de exportar")
            return False
        
        final_action = argenis_armature.animation_data.action
        print(f"   📋 Exportando acción: {final_action.name}")
        print(f"   📊 FCurves: {len(final_action.fcurves)}")
        print(f"   🎬 Frames: {final_action.frame_range[0]:.0f} - {final_action.frame_range[1]:.0f}")
        
        # Asegurar que el armature está seleccionado y activo
        bpy.ops.object.select_all(action='DESELECT')
        argenis_armature.select_set(True)
        bpy.context.view_layer.objects.active = argenis_armature
        
        # Seleccionar todos los objetos relacionados con Argenis
        for obj in bpy.data.objects:
            if obj == argenis_armature or obj.parent == argenis_armature:
                obj.select_set(True)
        
        bpy.ops.export_scene.gltf(
            filepath=str(argenis_glb_temp),
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
        
        if not argenis_glb_temp.exists():
            print("❌ No se generó GLB")
            return False
        
        # Copiar a destino final
        argenis_glb_final.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(argenis_glb_temp, argenis_glb_final)
        argenis_glb_temp.unlink()
        
        if argenis_glb_final.exists():
            size_kb = argenis_glb_final.stat().st_size / 1024
            tiempo = time.time() - inicio
            print(f"   ✅ ÉXITO: {size_kb:.1f} KB en {tiempo:.1f}s")
            return True
        else:
            print("❌ Error al copiar")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

# === PROCESAR TODAS ===
print(f"\n{'#'*80}")
print(f"🚀 INICIANDO RETARGET")
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
    print(f"\n✅ Archivos en: {ARGENIS_OUTPUT_DIR}")
    print(f"\n🎉 PROCESO COMPLETADO")

print(f"{'='*80}")
