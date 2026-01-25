"""
Script combinado: Genera todos los .blend y los convierte a GLB en un solo paso
Luego elimina los .blend dejando solo los GLB funcionales

Uso:
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python scripts\generar_y_convertir_todos.py
"""

import bpy
from pathlib import Path
import time
import shutil

print("="*80)
print("PIPELINE COMPLETO: BLEND → GLB → LIMPIEZA")
print("="*80)

# Rutas base
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_MODEL = BASE_DIR / "Luis" / "Luis.glb"
BLEND_OUTPUT_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\blend1")

# Todas las animaciones organizadas por categoría
ANIMACIONES = {
    "cortesia": [
        "a la orden",
    ]
}

# ============================================================================
# PASO 1: GENERAR TODOS LOS .BLEND
# ============================================================================

def retarget_animacion(categoria, animacion_nombre):
    """Retargetear una animación de Duvall a Luis usando Rokoko"""
    
    print(f"\n{'='*80}")
    print(f"📝 BLEND: {categoria.upper()} → {animacion_nombre}")
    print(f"{'='*80}")
    
    # Archivos
    duvall_file = BASE_DIR / "Duvall" / categoria / f"Duvall_resultado_{animacion_nombre}.glb"
    blend_output = BLEND_OUTPUT_DIR / categoria / f"Luis_{animacion_nombre}.blend"
    
    if not duvall_file.exists():
        print(f"❌ ERROR: No existe {duvall_file}")
        return False
    
    try:
        # Limpiar escena
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar Luis (destino)
        print(f"📦 Importando Luis...")
        bpy.ops.import_scene.gltf(filepath=str(NANCY_MODEL))
        
        luis_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                luis_armature = obj
                luis_armature.name = "Luis_Armature"
                break
        
        if not luis_armature:
            print("❌ ERROR: No armature de Luis")
            return False
        
        # Limpiar animación previa
        if luis_armature.animation_data:
            luis_armature.animation_data_clear()
        
        # Importar Duvall (source con animación)
        print(f"🎬 Importando Duvall con animación...")
        bpy.ops.import_scene.gltf(filepath=str(duvall_file))
        
        duvall_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != luis_armature:
                duvall_armature = obj
                duvall_armature.name = "Duvall_Armature"
                break
        
        if not duvall_armature:
            print("❌ ERROR: No armature de Duvall")
            return False
        
        if not duvall_armature.animation_data or not duvall_armature.animation_data.action:
            print("❌ ERROR: Duvall no tiene animación")
            return False
        
        duvall_action = duvall_armature.animation_data.action
        frame_start = int(duvall_action.frame_range[0])
        frame_end = int(duvall_action.frame_range[1])
        
        print(f"   Frames: {frame_start} → {frame_end}")
        
        # Aplicar retargeting manual con baking
        print(f"🔄 Aplicando retargeting...")
        
        # Configurar frame range
        bpy.context.scene.frame_start = frame_start
        bpy.context.scene.frame_end = frame_end
        
        # Crear constraints Copy Transforms
        bpy.context.view_layer.objects.active = luis_armature
        luis_armature.select_set(True)
        
        constraints_creados = 0
        for luis_bone in luis_armature.pose.bones:
            if luis_bone.name in duvall_armature.pose.bones:
                constraint = luis_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = duvall_armature
                constraint.subtarget = luis_bone.name
                constraints_creados += 1
        
        print(f"   ✅ {constraints_creados} constraints creados")
        
        # Bake la animación
        print(f"   🔥 Baking animación...")
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
            use_current_action=False,
            clean_curves=False,
            bake_types={'POSE'}
        )
        
        # Verificar animación en Luis
        if not luis_armature.animation_data or not luis_armature.animation_data.action:
            print(f"❌ ERROR: Luis no recibió animación")
            return False
        
        # Eliminar objetos de Duvall
        objetos_luis = []
        for obj in bpy.data.objects:
            if obj == luis_armature or obj.parent == luis_armature:
                objetos_luis.append(obj)
        
        objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_luis]
        for obj in objetos_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # Guardar .blend
        blend_output.parent.mkdir(parents=True, exist_ok=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_output))
        
        if blend_output.exists():
            print(f"   ✅ BLEND guardado")
            return True
        else:
            print(f"   ❌ ERROR: No se guardó el archivo")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False

# ============================================================================
# PASO 2: CONVERTIR TODOS LOS .BLEND A GLB
# ============================================================================

def encontrar_accion_con_movimiento(armature, actions):
    """Encuentra la acción que tiene movimiento real"""
    
    for action in actions:
        if not armature.animation_data:
            armature.animation_data_create()
        
        armature.animation_data.action = action
        armature.animation_data.use_nla = False
        
        frame_start, frame_end = action.frame_range
        
        # Verificar movimiento en Hips
        if 'Hips' in armature.pose.bones:
            bpy.context.scene.frame_set(int(frame_start))
            bpy.context.view_layer.update()
            
            pos_start = armature.pose.bones['Hips'].matrix.translation.copy()
            
            bpy.context.scene.frame_set(int(frame_end))
            bpy.context.view_layer.update()
            
            pos_end = armature.pose.bones['Hips'].matrix.translation.copy()
            movement = (pos_start - pos_end).length
            
            if movement > 0.001:
                return action
    
    return None

def convertir_blend_a_glb(categoria, animacion_nombre):
    """Convierte un archivo .blend a GLB funcional"""
    
    print(f"\n{'='*80}")
    print(f"📤 GLB: {categoria.upper()} → {animacion_nombre}")
    print(f"{'='*80}")
    
    blend_file = BLEND_OUTPUT_DIR / categoria / f"Luis_{animacion_nombre}.blend"
    glb_output = BASE_DIR / "Luis" / categoria / f"Luis_resultado_{animacion_nombre}.glb"
    glb_output.parent.mkdir(parents=True, exist_ok=True)
    
    if not blend_file.exists():
        print(f"❌ No existe: {blend_file}")
        return False
    
    try:
        # Cargar .blend
        bpy.ops.wm.open_mainfile(filepath=str(blend_file))
        
        # Obtener armature
        armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
        if not armatures:
            print("❌ No hay armature")
            return False
        
        armature = armatures[0]
        
        # Obtener todas las acciones
        actions = list(bpy.data.actions)
        if not actions:
            print("❌ No hay acciones")
            return False
        
        # Encontrar la acción con movimiento real
        good_action = encontrar_accion_con_movimiento(armature, actions)
        
        if not good_action:
            print("❌ No se encontró acción con movimiento")
            return False
        
        # ELIMINAR todas las acciones inservibles
        actions_to_remove = []
        for action in bpy.data.actions:
            if action != good_action:
                actions_to_remove.append(action)
        
        for action in actions_to_remove:
            bpy.data.actions.remove(action)
        
        # Asignar la acción correcta
        if not armature.animation_data:
            armature.animation_data_create()
        
        armature.animation_data.action = good_action
        armature.animation_data.use_nla = False
        
        # Configurar escena
        frame_start, frame_end = good_action.frame_range
        bpy.context.scene.frame_start = int(frame_start)
        bpy.context.scene.frame_end = int(frame_end)
        bpy.context.scene.frame_set(int(frame_start))
        
        # Exportar GLB
        bpy.ops.object.select_all(action='SELECT')
        
        bpy.ops.export_scene.gltf(
            filepath=str(glb_output),
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
        
        if glb_output.exists():
            size_kb = glb_output.stat().st_size / 1024
            print(f"   ✅ GLB: {size_kb:.1f} KB")
            return True
        else:
            print(f"   ❌ No se generó el archivo")
            return False
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
        return False

# ============================================================================
# MAIN: EJECUTAR TODO EL PIPELINE
# ============================================================================

print(f"\n📊 Total de animaciones a procesar:")
total = 0
for categoria, animaciones in ANIMACIONES.items():
    print(f"   {categoria}: {len(animaciones)} animaciones")
    total += len(animaciones)
print(f"   TOTAL: {total} animaciones")

resultados = {
    "blend_exitosos": [],
    "blend_fallidos": [],
    "glb_exitosos": [],
    "glb_fallidos": []
}

inicio_total = time.time()

# ============================================================================
# PASO 1: GENERAR TODOS LOS .BLEND
# ============================================================================
print(f"\n{'#'*80}")
print(f"PASO 1: GENERANDO ARCHIVOS .BLEND")
print(f"{'#'*80}")

for categoria, animaciones in ANIMACIONES.items():
    for animacion in animaciones:
        exito = retarget_animacion(categoria, animacion)
        
        if exito:
            resultados["blend_exitosos"].append(f"{categoria}/{animacion}")
        else:
            resultados["blend_fallidos"].append(f"{categoria}/{animacion}")

print(f"\n✅ PASO 1 COMPLETADO: {len(resultados['blend_exitosos'])}/{total} .blend generados")

# ============================================================================
# PASO 2: CONVERTIR TODOS LOS .BLEND A GLB
# ============================================================================
print(f"\n{'#'*80}")
print(f"PASO 2: CONVIRTIENDO .BLEND A GLB")
print(f"{'#'*80}")

for categoria, animaciones in ANIMACIONES.items():
    for animacion in animaciones:
        exito = convertir_blend_a_glb(categoria, animacion)
        
        if exito:
            resultados["glb_exitosos"].append(f"{categoria}/{animacion}")
        else:
            resultados["glb_fallidos"].append(f"{categoria}/{animacion}")

print(f"\n✅ PASO 2 COMPLETADO: {len(resultados['glb_exitosos'])}/{total} .glb generados")

# ============================================================================
# PASO 3: ELIMINAR ARCHIVOS .BLEND
# ============================================================================
print(f"\n{'#'*80}")
print(f"PASO 3: LIMPIANDO ARCHIVOS .BLEND")
print(f"{'#'*80}")

archivos_eliminados = 0
for categoria, animaciones in ANIMACIONES.items():
    for animacion in animaciones:
        blend_file = BLEND_OUTPUT_DIR / categoria / f"Luis_{animacion}.blend"
        if blend_file.exists():
            try:
                blend_file.unlink()
                archivos_eliminados += 1
                print(f"   🗑️ Eliminado: {categoria}/{animacion}.blend")
            except Exception as e:
                print(f"   ⚠️ No se pudo eliminar: {categoria}/{animacion}.blend - {e}")

print(f"\n✅ PASO 3 COMPLETADO: {archivos_eliminados} archivos .blend eliminados")

# ============================================================================
# RESUMEN FINAL
# ============================================================================
tiempo_total = time.time() - inicio_total

print(f"\n{'='*80}")
print(f"RESUMEN FINAL DEL PIPELINE")
print(f"{'='*80}")
print(f"⏱️ Tiempo total: {tiempo_total/60:.1f} minutos")
print(f"\n📊 PASO 1 - Generación .blend:")
print(f"   ✅ Exitosos: {len(resultados['blend_exitosos'])}/{total}")
print(f"   ❌ Fallidos: {len(resultados['blend_fallidos'])}")
print(f"\n📊 PASO 2 - Conversión a GLB:")
print(f"   ✅ Exitosos: {len(resultados['glb_exitosos'])}/{total}")
print(f"   ❌ Fallidos: {len(resultados['glb_fallidos'])}")
print(f"\n🗑️ PASO 3 - Limpieza:")
print(f"   ✅ {archivos_eliminados} archivos .blend eliminados")

if resultados["glb_fallidos"]:
    print(f"\n❌ Animaciones fallidas en conversión GLB:")
    for item in resultados["glb_fallidos"]:
        print(f"   - {item}")

print(f"\n📁 Archivos GLB funcionales guardados en:")
print(f"   {BLEND_OUTPUT_DIR}")
print(f"\n{'='*80}")
print(f"🎉 PIPELINE COMPLETADO")
print(f"{'='*80}")
