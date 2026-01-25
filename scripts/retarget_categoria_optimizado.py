"""
Script Optimizado: Retargetear una categoría completa de Carla a Nancy
Proceso completo en un solo paso sin archivos intermedios

USO:
blender --background --python scripts/retarget_categoria_optimizado.py -- profesion
blender --background --python scripts/retarget_categoria_optimizado.py -- verbos
"""

import bpy
from pathlib import Path
import time
import sys
import shutil

print("="*80)
print("🚀 RETARGET OPTIMIZADO: Carla → Nancy → GLB → Copiar")
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
    print(f"📁 Categoría seleccionada: {CATEGORIA}")
except (ValueError, IndexError):
    print("❌ ERROR: Debes especificar una categoría")
    print("   Uso: blender --background --python script.py -- profesion")
    sys.exit(1)

# Rutas base
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_MODEL = BASE_DIR / "Nancy" / "Nancy.glb"
CARLA_DIR = BASE_DIR / "Carla" / CATEGORIA
NANCY_OUTPUT_DIR = BASE_DIR / "Nancy" / CATEGORIA

# Verificar que existe la carpeta
if not CARLA_DIR.exists():
    print(f"❌ ERROR: No existe la carpeta {CARLA_DIR}")
    sys.exit(1)

# Obtener todas las animaciones de la carpeta
animaciones = []
for glb_file in CARLA_DIR.glob("Carla_resultado_*.glb"):
    nombre = glb_file.stem.replace("Carla_resultado_", "")
    animaciones.append(nombre)

if not animaciones:
    print(f"❌ No se encontraron animaciones en {CARLA_DIR}")
    sys.exit(1)

print(f"✅ Encontradas {len(animaciones)} animaciones")
for i, anim in enumerate(animaciones, 1):
    print(f"   {i}. {anim}")

def encontrar_accion_con_movimiento(armature, actions):
    """Encuentra la acción que tiene movimiento real"""
    for action in actions:
        if not armature.animation_data:
            armature.animation_data_create()
        
        armature.animation_data.action = action
        armature.animation_data.use_nla = False
        
        frame_start, frame_end = action.frame_range
        
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

def procesar_animacion(animacion_nombre):
    """Proceso completo optimizado: retarget + limpieza + export + copia"""
    
    print(f"\n{'='*80}")
    print(f"📝 Procesando: {animacion_nombre}")
    print(f"{'='*80}")
    
    carla_file = CARLA_DIR / f"Carla_resultado_{animacion_nombre}.glb"
    nancy_glb_temp = Path(f"/tmp/nancy_temp_{animacion_nombre}.glb")
    nancy_glb_final = NANCY_OUTPUT_DIR / f"Nancy_resultado_{animacion_nombre}.glb"
    
    if not carla_file.exists():
        print(f"❌ No existe: {carla_file}")
        return False
    
    inicio = time.time()
    
    try:
        # === PASO 1: RETARGET ===
        print(f"🔄 PASO 1/4: Retargeting...")
        
        # Limpiar escena
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar Nancy
        bpy.ops.import_scene.gltf(filepath=str(NANCY_MODEL))
        nancy_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                nancy_armature = obj
                nancy_armature.name = "Nancy_Armature"
                break
        
        if not nancy_armature:
            print("❌ No se encontró armature de Nancy")
            return False
        
        if nancy_armature.animation_data:
            nancy_armature.animation_data_clear()
        
        # Importar Carla con animación
        bpy.ops.import_scene.gltf(filepath=str(carla_file))
        carla_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != nancy_armature:
                carla_armature = obj
                carla_armature.name = "Carla_Armature"
                break
        
        if not carla_armature or not carla_armature.animation_data or not carla_armature.animation_data.action:
            print("❌ Carla no tiene animación")
            return False
        
        carla_action = carla_armature.animation_data.action
        frame_start = int(carla_action.frame_range[0])
        frame_end = int(carla_action.frame_range[1])
        
        bpy.context.scene.frame_start = frame_start
        bpy.context.scene.frame_end = frame_end
        
        # Crear constraints
        bpy.context.view_layer.objects.active = nancy_armature
        nancy_armature.select_set(True)
        
        constraints_count = 0
        for nancy_bone in nancy_armature.pose.bones:
            if nancy_bone.name in carla_armature.pose.bones:
                constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = carla_armature
                constraint.subtarget = nancy_bone.name
                constraints_count += 1
        
        print(f"   ✅ {constraints_count} constraints creados")
        
        # Bake animación
        print(f"   🔥 Baking...")
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
        
        if not nancy_armature.animation_data or not nancy_armature.animation_data.action:
            print("❌ Nancy no recibió animación")
            return False
        
        print(f"   ✅ Retarget completado")
        
        # === PASO 2: LIMPIAR ACCIONES ===
        print(f"🧹 PASO 2/4: Limpiando acciones...")
        
        all_actions = list(bpy.data.actions)
        good_action = encontrar_accion_con_movimiento(nancy_armature, all_actions)
        
        if not good_action:
            print("❌ No se encontró acción con movimiento")
            return False
        
        # Eliminar acciones inservibles
        removed = 0
        for action in bpy.data.actions:
            if action != good_action:
                bpy.data.actions.remove(action)
                removed += 1
        
        print(f"   🗑️ {removed} acciones eliminadas")
        
        # Asignar la acción correcta
        nancy_armature.animation_data.action = good_action
        nancy_armature.animation_data.use_nla = False
        
        # === PASO 3: ELIMINAR OBJETOS DE CARLA ===
        print(f"🗑️ PASO 3/4: Eliminando objetos temporales...")
        
        objetos_nancy = []
        for obj in bpy.data.objects:
            if obj == nancy_armature or obj.parent == nancy_armature:
                objetos_nancy.append(obj)
        
        objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
        for obj in objetos_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        print(f"   ✅ {len(objetos_eliminar)} objetos eliminados")
        
        # === PASO 4: EXPORTAR GLB ===
        print(f"📤 PASO 4/4: Exportando GLB...")
        
        bpy.ops.object.select_all(action='SELECT')
        
        bpy.ops.export_scene.gltf(
            filepath=str(nancy_glb_temp),
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
        
        if not nancy_glb_temp.exists():
            print("❌ No se generó el GLB temporal")
            return False
        
        # === PASO 5: COPIAR A DESTINO FINAL ===
        print(f"📋 PASO 5/5: Copiando a destino final...")
        
        nancy_glb_final.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(nancy_glb_temp, nancy_glb_final)
        
        # Eliminar temporal
        nancy_glb_temp.unlink()
        
        if nancy_glb_final.exists():
            size_kb = nancy_glb_final.stat().st_size / 1024
            tiempo = time.time() - inicio
            print(f"   ✅ ÉXITO: {size_kb:.1f} KB en {tiempo:.1f}s")
            print(f"   📁 {nancy_glb_final}")
            return True
        else:
            print("❌ No se pudo copiar al destino final")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

# === PROCESAR TODAS LAS ANIMACIONES ===
print(f"\n{'#'*80}")
print(f"🚀 INICIANDO PROCESO OPTIMIZADO")
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

# === RESUMEN FINAL ===
print(f"\n{'='*80}")
print(f"📊 RESUMEN FINAL - {CATEGORIA.upper()}")
print(f"{'='*80}")
print(f"⏱️  Tiempo total: {tiempo_total/60:.1f} minutos")
print(f"⚡ Promedio: {tiempo_total/len(animaciones):.1f}s por animación")
print(f"✅ Exitosos: {len(resultados['exitosos'])}/{len(animaciones)}")
print(f"❌ Fallidos: {len(resultados['fallidos'])}/{len(animaciones)}")

if resultados["fallidos"]:
    print(f"\n❌ Animaciones fallidas:")
    for item in resultados["fallidos"]:
        print(f"   - {item}")

if resultados["exitosos"]:
    print(f"\n✅ Archivos generados en:")
    print(f"   {NANCY_OUTPUT_DIR}")
    print(f"\n🎉 PROCESO COMPLETADO")

print(f"{'='*80}")
