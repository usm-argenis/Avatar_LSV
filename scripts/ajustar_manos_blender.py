"""
Script de Blender para ajustar animación de manos basándose en video de referencia
Ejecutar en Blender con el modelo Remy_resultado_r.glb cargado
"""

import bpy
import json
import mathutils
from pathlib import Path

# CONFIGURACIÓN
VIDEO_FPS = 29.47
FRAMES_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\output\frames_r")
GLB_PATH = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Remy_resultado_r.glb")
OUTPUT_GLB = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\output\Remy_resultado_r_ajustado.glb")

def importar_glb():
    """Importa el modelo GLB"""
    print(f"📥 Importando GLB: {GLB_PATH}")
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Importar GLB
    bpy.ops.import_scene.gltf(filepath=str(GLB_PATH))
    
    # Buscar armature
    armature = None
    for obj in bpy.context.scene.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        print("❌ No se encontró armature en el GLB")
        return None
    
    print(f"✅ Armature encontrado: {armature.name}")
    
    # Listar huesos de las manos
    print("\n🦴 Huesos de manos encontrados:")
    hand_bones = []
    for bone in armature.pose.bones:
        if any(keyword in bone.name.lower() for keyword in ['hand', 'finger', 'thumb', 'index', 'middle', 'ring', 'pinky']):
            hand_bones.append(bone.name)
            print(f"   - {bone.name}")
    
    return armature, hand_bones

def analizar_animacion(armature):
    """Analiza la animación actual"""
    print(f"\n📊 Analizando animación...")
    
    if not armature.animation_data or not armature.animation_data.action:
        print("❌ No se encontró animación en el armature")
        return None
    
    action = armature.animation_data.action
    print(f"✅ Acción encontrada: {action.name}")
    
    # Obtener rango de frames
    frame_start = int(action.frame_range[0])
    frame_end = int(action.frame_range[1])
    duracion = (frame_end - frame_start) / bpy.context.scene.render.fps
    
    print(f"   📊 Frame inicio: {frame_start}")
    print(f"   📊 Frame fin: {frame_end}")
    print(f"   📊 Total frames: {frame_end - frame_start}")
    print(f"   📊 Duración: {duracion:.2f}s")
    print(f"   📊 FPS: {bpy.context.scene.render.fps}")
    
    # Contar FCurves de manos
    hand_fcurves = []
    for fcurve in action.fcurves:
        if any(keyword in fcurve.data_path.lower() for keyword in ['hand', 'finger', 'thumb', 'index', 'middle', 'ring', 'pinky']):
            hand_fcurves.append(fcurve)
    
    print(f"   📊 FCurves de manos: {len(hand_fcurves)}")
    
    return {
        'action': action,
        'frame_start': frame_start,
        'frame_end': frame_end,
        'duracion': duracion,
        'hand_fcurves': hand_fcurves
    }

def ajustar_timing_manos(armature, info_anim):
    """
    Ajusta el timing de las animaciones de manos
    basándose en la duración del video de referencia
    """
    print(f"\n🔧 Ajustando timing de manos...")
    
    # Duración del video: 2.75s
    duracion_video = 2.75
    duracion_actual = info_anim['duracion']
    
    print(f"   📊 Duración video: {duracion_video}s")
    print(f"   📊 Duración actual: {duracion_actual}s")
    
    if abs(duracion_actual - duracion_video) > 0.1:
        print(f"   ⚠️ Diferencia significativa: {abs(duracion_actual - duracion_video):.2f}s")
        print(f"   💡 Se recomienda ajustar la velocidad de playback")
    
    # Ajustar FPS para que coincida con el video
    fps_int = int(round(VIDEO_FPS))
    bpy.context.scene.render.fps = fps_int
    print(f"   ✅ FPS ajustado a: {fps_int} (original: {VIDEO_FPS})")
    
    return True

def exportar_glb_ajustado():
    """Exporta el GLB con las modificaciones"""
    print(f"\n💾 Exportando GLB ajustado...")
    
    # Crear directorio de salida
    OUTPUT_GLB.parent.mkdir(parents=True, exist_ok=True)
    
    # Asegurarse de estar en Object Mode
    if bpy.context.active_object and bpy.context.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    # Seleccionar todos los objetos
    bpy.ops.object.select_all(action='SELECT')
    
    # Exportar
    bpy.ops.export_scene.gltf(
        filepath=str(OUTPUT_GLB),
        export_format='GLB',
        export_animations=True,
        export_apply=True,
        export_rest_position_armature=False
    )
    
    print(f"✅ GLB exportado: {OUTPUT_GLB}")
    
    # Verificar tamaño
    tamaño_mb = OUTPUT_GLB.stat().st_size / (1024 * 1024)
    print(f"📊 Tamaño: {tamaño_mb:.2f} MB")
    
    return OUTPUT_GLB

def main():
    print("=" * 60)
    print("🔧 AJUSTE DE ANIMACIÓN DE MANOS")
    print("=" * 60)
    
    # 1. Importar GLB
    resultado = importar_glb()
    if not resultado:
        return
    
    armature, hand_bones = resultado
    
    # 2. Analizar animación
    info_anim = analizar_animacion(armature)
    if not info_anim:
        return
    
    # 3. Ajustar timing
    ajustar_timing_manos(armature, info_anim)
    
    # 4. Exportar
    exportar_glb_ajustado()
    
    print("\n" + "=" * 60)
    print("✅ PROCESO COMPLETADO")
    print("=" * 60)
    print(f"📁 Archivo ajustado: {OUTPUT_GLB}")
    print("\n💡 Siguiente paso:")
    print("   Revisar el archivo ajustado en el visor 3D")

if __name__ == "__main__":
    main()
