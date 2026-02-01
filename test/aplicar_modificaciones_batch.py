import bpy
import json
import math
from pathlib import Path
from mathutils import Quaternion, Euler
import glob
import os

def aplicar_modificaciones_a_archivo(glb_path, modifications, output_path):
    """Aplicar modificaciones a un solo archivo GLB"""
    
    print(f"\n{'='*80}")
    print(f"📁 Procesando: {Path(glb_path).name}")
    print(f"{'='*80}")
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Importar GLB
    print(f"📥 Importando GLB...")
    bpy.ops.import_scene.gltf(filepath=str(glb_path))
    
    # Buscar armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        print(f"❌ No se encontró armature, saltando...")
        return False
    
    print(f"✅ Armature: {armature.name}")
    
    # Verificar animación
    if not armature.animation_data or not armature.animation_data.action:
        print(f"❌ Sin animación, saltando...")
        return False
    
    action = armature.animation_data.action
    print(f"✅ Animación: {action.name}")
    
    # Extraer configuración de alcance
    alcance = modifications['alcance']
    frame_min = alcance['min']
    frame_max_config = alcance['max']
    frame_retencion_config = alcance['retencion']
    
    # Si frame_max es "fin", usar el último frame de la animación
    if isinstance(frame_max_config, str) and frame_max_config.lower() == "fin":
        frame_max = int(action.frame_range[1])
        print(f"🔍 'fin' detectado en max → usando último frame de la animación: {frame_max}")
    else:
        frame_max = int(frame_max_config)
    
    # Calcular rangos
    total_frames = frame_max - frame_min
    
    # Si frame_retencion es "fin", usar todo el rango disponible
    if isinstance(frame_retencion_config, str) and frame_retencion_config.lower() == "fin":
        frame_retencion = total_frames
        print(f"🔍 'fin' detectado en retencion → usando rango completo: {frame_retencion}")
    else:
        frame_retencion = int(frame_retencion_config)
    
    repeat_start = frame_min + (total_frames - frame_retencion) // 2
    repeat_end = repeat_start + frame_retencion
    
    print(f"⚙️  Rango: {frame_min} → {frame_max}")
    print(f"📊 Repetición: frames {repeat_start}-{repeat_end}")
    
    # Procesar cada hueso
    bones_modified = []
    
    for bone_name in modifications:
        if bone_name in ['alcance', 'carpeta_entrada', 'carpeta_salida', 'patron', 'excluir', 'sufijo_salida']:
            continue
        
        target_values = modifications[bone_name]
        
        # Verificar hueso
        if bone_name not in armature.pose.bones:
            continue
        
        # Crear quaternion objetivo
        target_quat = Quaternion((
            target_values['w'],
            target_values['x'],
            target_values['y'],
            target_values['z']
        ))
        
        # Buscar fcurves
        data_path = f'pose.bones["{bone_name}"].rotation_quaternion'
        fcurves = [fc for fc in action.fcurves if fc.data_path == data_path]
        
        if len(fcurves) != 4:
            continue
        
        # Obtener valor original en repeat_start
        original_quat = Quaternion()
        for i, fc in enumerate(fcurves):
            original_quat[i] = fc.evaluate(repeat_start)
        
        # Aplicar modificaciones
        for frame in range(repeat_start, repeat_end + 1):
            for i, fc in enumerate(fcurves):
                fc.keyframe_points.insert(frame, target_quat[i])
        
        # Transición entrada
        for frame in range(frame_min, repeat_start):
            progress = (frame - frame_min) / (repeat_start - frame_min)
            progress = progress * progress * (3 - 2 * progress)  # Smoothstep
            
            for i, fc in enumerate(fcurves):
                original_val = fc.evaluate(frame)
                blended_val = original_val + (target_quat[i] - original_quat[i]) * progress
                fc.keyframe_points.insert(frame, blended_val)
        
        # Transición salida
        for frame in range(repeat_end + 1, frame_max + 1):
            progress = (frame - repeat_end) / (frame_max - repeat_end)
            progress = progress * progress * (3 - 2 * progress)  # Smoothstep
            
            for i, fc in enumerate(fcurves):
                final_val = fc.evaluate(frame_max)
                blended_val = target_quat[i] + (final_val - target_quat[i]) * progress
                fc.keyframe_points.insert(frame, blended_val)
        
        bones_modified.append(bone_name)
    
    print(f"\n✅ Huesos modificados: {len(bones_modified)}")
    
    # Exportar
    print(f"\n💾 Exportando a: {Path(output_path).name}")
    
    # Crear directorio de salida si no existe
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.gltf(
        filepath=str(output_path),
        export_format='GLB',
        export_animations=True,
        export_force_sampling=True
    )
    
    print(f"✅ Exportado exitosamente!")
    
    # IMPORTANTE: Limpiar TODO después de exportar para evitar contaminación entre archivos
    print(f"🧹 Limpiando datos de Blender...")
    
    # Eliminar todos los objetos
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Limpiar datos huérfanos (meshes, armatures, actions, etc.)
    for mesh in bpy.data.meshes:
        bpy.data.meshes.remove(mesh)
    
    for armature_data in bpy.data.armatures:
        bpy.data.armatures.remove(armature_data)
    
    for action in bpy.data.actions:
        bpy.data.actions.remove(action)
    
    for material in bpy.data.materials:
        bpy.data.materials.remove(material)
    
    for image in bpy.data.images:
        bpy.data.images.remove(image)
    
    print(f"✅ Limpieza completada")
    
    return True


def procesar_carpeta_batch(json_config_path):
    """Procesar todos los archivos GLB de una carpeta"""
    
    print(f"\n{'='*80}")
    print(f"🎨 PROCESAMIENTO BATCH DE CARPETA")
    print(f"{'='*80}\n")
    
    # Cargar configuración
    with open(json_config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    carpeta_entrada = Path(config['carpeta_entrada'])
    carpeta_salida = Path(config['carpeta_salida'])
    patron = config.get('patron', '*.glb')
    excluir = config.get('excluir', [])
    sufijo_salida = config.get('sufijo_salida', '')
    
    print(f"📂 Carpeta entrada: {carpeta_entrada}")
    print(f"📂 Carpeta salida: {carpeta_salida}")
    print(f"🔍 Patrón: {patron}")
    print(f"🚫 Excluir: {excluir}")
    print(f"📝 Sufijo: {sufijo_salida}")
    
    # Verificar carpeta entrada
    if not carpeta_entrada.exists():
        raise FileNotFoundError(f"Carpeta de entrada no existe: {carpeta_entrada}")
    
    # Buscar archivos
    archivos = list(carpeta_entrada.glob(patron))
    
    # Filtrar archivos excluidos
    archivos_filtrados = []
    for archivo in archivos:
        excluir_archivo = False
        for patron_excluir in excluir:
            if archivo.match(patron_excluir):
                excluir_archivo = True
                break
        if not excluir_archivo:
            archivos_filtrados.append(archivo)
    
    print(f"\n📊 Archivos encontrados: {len(archivos)}")
    print(f"📊 Archivos a procesar: {len(archivos_filtrados)}")
    
    if not archivos_filtrados:
        print("⚠️  No hay archivos para procesar")
        return
    
    # Procesar cada archivo
    procesados = 0
    fallidos = 0
    
    for i, archivo in enumerate(archivos_filtrados, 1):
        print(f"\n{'='*80}")
        print(f"[{i}/{len(archivos_filtrados)}] {archivo.name}")
        print(f"{'='*80}")
        
        # Crear nombre de salida
        nombre_base = archivo.stem
        nombre_salida = f"{nombre_base}{sufijo_salida}.glb"
        ruta_salida = carpeta_salida / nombre_salida
        
        try:
            exito = aplicar_modificaciones_a_archivo(
                str(archivo),
                config,
                str(ruta_salida)
            )
            
            if exito:
                procesados += 1
            else:
                fallidos += 1
        except Exception as e:
            print(f"\n❌ ERROR: {e}")
            fallidos += 1
    
    # Resumen
    print(f"\n{'='*80}")
    print(f"📊 RESUMEN FINAL")
    print(f"{'='*80}")
    print(f"✅ Procesados exitosamente: {procesados}")
    print(f"❌ Fallidos: {fallidos}")
    print(f"📁 Archivos en: {carpeta_salida}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("❌ Uso: blender --background --python aplicar_modificaciones_batch.py -- config.json")
        sys.exit(1)
    
    # El argumento después de -- es el JSON
    json_path = sys.argv[-1]
    
    if not Path(json_path).exists():
        print(f"❌ Archivo no encontrado: {json_path}")
        sys.exit(1)
    
    try:
        procesar_carpeta_batch(json_path)
        print("\n✅ PROCESO COMPLETADO")
    except Exception as e:
        print(f"\n❌ ERROR FATAL: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
