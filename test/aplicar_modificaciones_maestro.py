import bpy
import json
import sys
from pathlib import Path
from mathutils import Quaternion
import glob
import gc

# OPTIMIZACIÓN GLOBAL: Deshabilitar sistemas innecesarios
bpy.context.preferences.view.show_splash = False
bpy.context.preferences.filepaths.use_auto_save_temporary_files = False

def limpiar_memoria():
    """Limpieza agresiva de memoria"""
    # Purgar datos huérfanos (múltiples pasadas)
    for _ in range(3):
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    # Forzar garbage collection de Python
    gc.collect()

def procesar_archivo(archivo_entrada, archivo_salida, modificaciones):
    """Procesa UN archivo GLB - ULTRA optimizado"""
    
    # Limpiar escena (método directo, más rápido que bpy.ops)
    for obj in bpy.data.objects[:]:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    # Importar GLB
    bpy.ops.import_scene.gltf(filepath=str(archivo_entrada))
    
    # Buscar armature (comprehension más rápida)
    armature = next((obj for obj in bpy.data.objects if obj.type == 'ARMATURE'), None)
    
    if not armature or not armature.animation_data or not armature.animation_data.action:
        return False
    
    action = armature.animation_data.action
    
    # Extraer alcance
    alcance = modificaciones['alcance']
    frame_min = alcance['min']
    frame_max_config = alcance['max']
    frame_retencion_config = alcance['retencion']
    
    # Calcular frames (optimizado sin if anidados)
    frame_max = int(action.frame_range[1]) if isinstance(frame_max_config, str) and frame_max_config.lower() == "fin" else int(frame_max_config)
    total_frames = frame_max - frame_min
    frame_retencion = total_frames if isinstance(frame_retencion_config, str) and frame_retencion_config.lower() == "fin" else int(frame_retencion_config)
    
    repeat_start = frame_min + (total_frames - frame_retencion) // 2
    repeat_end = repeat_start + frame_retencion
    
    # Función de suavizado (pre-compilada)
    smooth = lambda t: t * t * (3 - 2 * t)
    
    # Procesar huesos (ULTRA optimizado)
    for bone_name, target_values in modificaciones.items():
        if bone_name == 'alcance' or bone_name not in armature.pose.bones:
            continue
        
        target_quat = Quaternion((target_values['w'], target_values['x'], target_values['y'], target_values['z']))
        data_path = f'pose.bones["{bone_name}"].rotation_quaternion'
        fcurves = [fc for fc in action.fcurves if fc.data_path == data_path]
        
        if len(fcurves) != 4:
            continue
        
        # Obtener quaternion original (una sola vez)
        original_quat = Quaternion([fc.evaluate(repeat_start) for fc in fcurves])
        
        # BATCH INSERT: Preparar todos los keyframes de una vez
        for i, fc in enumerate(fcurves):
            # Repetición (valor constante) - más rápido con co_insert
            keyframes = [(frame, target_quat[i]) for frame in range(repeat_start, repeat_end + 1)]
            fc.keyframe_points.add(len(keyframes))
            for idx, (frame, value) in enumerate(keyframes):
                kf = fc.keyframe_points[-(len(keyframes) - idx)]
                kf.co = (frame, value)
                kf.interpolation = 'LINEAR'
        
        # Transiciones (pre-calculadas)
        if repeat_start > frame_min:
            entrada_range = repeat_start - frame_min
            for i, fc in enumerate(fcurves):
                original_val = fc.evaluate(frame_min)
                diff = target_quat[i] - original_quat[i]
                for frame in range(frame_min, repeat_start):
                    progress = smooth((frame - frame_min) / entrada_range)
                    fc.keyframe_points.insert(frame, original_val + diff * progress, options={'FAST'})
        
        if repeat_end < frame_max:
            salida_range = frame_max - repeat_end
            for i, fc in enumerate(fcurves):
                final_val = fc.evaluate(frame_max)
                diff = final_val - target_quat[i]
                for frame in range(repeat_end + 1, frame_max + 1):
                    progress = smooth((frame - repeat_end) / salida_range)
                    fc.keyframe_points.insert(frame, target_quat[i] + diff * progress, options={'FAST'})
    
    # Exportar (sin sampleo forzado, es más rápido)
    bpy.ops.export_scene.gltf(
        filepath=str(archivo_salida),
        export_format='GLB',
        export_animations=True,
        export_force_sampling=False  # OPTIMIZACIÓN: Más rápido
    )
    
    # Limpiar inmediatamente después de exportar
    limpiar_memoria()
    
    return True


def aplicar_modificaciones_a_carpeta(carpeta_entrada, carpeta_salida, modificaciones):
    """Procesa todos los archivos GLB de una carpeta - ULTRA OPTIMIZADO"""
    
    # Buscar archivos GLB
    patron = str(Path(carpeta_entrada) / "*.glb")
    archivos = [f for f in glob.glob(patron) if not any(x in Path(f).name for x in ['_modif', '_modificado', '_MANOS'])]
    
    if not archivos:
        return 0
    
    # Crear carpeta de salida
    Path(carpeta_salida).mkdir(parents=True, exist_ok=True)
    
    procesados = 0
    total = len(archivos)
    
    for idx, archivo_entrada in enumerate(archivos, 1):
        archivo_salida = Path(carpeta_salida) / Path(archivo_entrada).name
        if procesar_archivo(str(archivo_entrada), str(archivo_salida), modificaciones):
            procesados += 1
            # Mostrar progreso cada 5 archivos o al final
            if idx % 5 == 0 or idx == total:
                print(f"✅ {procesados}/{total}")
        
        # Limpieza profunda cada 10 archivos
        if idx % 10 == 0:
            limpiar_memoria()
    
    return procesados


def procesar_personaje(json_path):
    """Procesa todas las carpetas de un personaje - OPTIMIZADO"""
    
    with open(json_path, 'r', encoding='utf-8') as f:
        modificaciones = json.load(f)
    
    personaje = Path(json_path).stem
    carpetas = ["alfabeto", "cortesia", "dias_semana", "estado civil", "expresiones",
                "numero", "numeros ordinales", "personas", "preguntas", "preposicion",
                "profesion", "pronombres", "saludos", "tiempo", "verbos",
                "adverbios lugares", "tipos de vivienda"]
    
    base_path = Path(__file__).parent / "output" / "glb" / personaje
    total = 0
    
    print(f"\n{'='*60}\n🎭 {personaje.upper()}\n{'='*60}")
    
    for carpeta in carpetas:
        entrada = base_path / carpeta
        if not entrada.exists():
            continue
        
        salida = base_path / "Modif" / carpeta
        procesados = aplicar_modificaciones_a_carpeta(str(entrada), str(salida), modificaciones)
        
        if procesados > 0:
            print(f"📁 {carpeta}: {procesados} archivos")
            total += procesados
        
        # Limpieza profunda después de cada carpeta
        limpiar_memoria()
    
    print(f"\n✅ {personaje.upper()}: {total} archivos totales\n")
    return total


if __name__ == "__main__":
    argv = sys.argv
    
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        argv = []
    
    if len(argv) < 1:
        print("❌ Error: Se requiere el archivo JSON maestro")
        print("Uso: blender --background --python script.py -- <Duvall.json|Carla.json>")
        sys.exit(1)
    
    json_path = argv[0]
    
    if not Path(json_path).exists():
        print(f"❌ Error: No se encontró el archivo {json_path}")
        sys.exit(1)
    
    # Limpieza inicial
    limpiar_memoria()
    
    procesar_personaje(json_path)
