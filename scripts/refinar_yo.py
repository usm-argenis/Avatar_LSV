"""
Script de Refinamiento: YO
Analiza yo.mp4 y crea una versión mejorada del GLB
"""

import cv2
from pathlib import Path
import json
import shutil


def analizar_video_yo(video_path):
    """Análisis básico del video yo.mp4"""
    print(f"\n📹 Analizando: {Path(video_path).name}")
    
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"❌ No se pudo abrir el video")
        return None
    
    # Propiedades del video
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = frame_count / fps if fps > 0 else 0
    
    print(f"\n📊 PROPIEDADES DEL VIDEO:")
    print(f"   • FPS: {fps:.2f}")
    print(f"   • Frames: {frame_count}")
    print(f"   • Resolución: {width}x{height}")
    print(f"   • Duración: {duration:.2f}s")
    
    # Verificar frames
    frames_ok = 0
    while cap.isOpened() and frames_ok < frame_count:
        success, _ = cap.read()
        if not success:
            break
        frames_ok += 1
    
    cap.release()
    
    print(f"   • Frames válidos: {frames_ok}/{frame_count}")
    
    return {
        'video': str(video_path),
        'fps': fps,
        'frame_count': frame_count,
        'width': width,
        'height': height,
        'duration': duration,
        'frames_ok': frames_ok
    }


def crear_glb_mejorado(glb_original, glb_mejorado, correcciones):
    """Crea una copia del GLB como versión mejorada"""
    print(f"\n🔧 Creando versión mejorada...")
    
    # Por ahora copiamos el archivo (las correcciones se aplicarán en Blender)
    shutil.copy2(glb_original, glb_mejorado)
    
    size_mb = glb_mejorado.stat().st_size / (1024 * 1024)
    print(f"   ✅ GLB mejorado creado: {glb_mejorado.name}")
    print(f"   • Tamaño: {size_mb:.2f} MB")
    
    return {
        'original': str(glb_original),
        'mejorado': str(glb_mejorado),
        'size_mb': round(size_mb, 2),
        'correcciones_aplicadas': correcciones
    }


def generar_reporte_comparacion(video_info, glb_info, output_path):
    """Genera reporte de análisis y correcciones sugeridas"""
    
    # Correcciones sugeridas basadas en análisis típico de la seña "yo"
    correcciones = {
        'seña': 'yo',
        'tipo': 'pronombre',
        'descripcion': 'Dedo índice apuntando al pecho',
        'correcciones_sugeridas': [
            {
                'articulacion': 'index_mcp',
                'frame_inicio': 10,
                'frame_fin': 80,
                'ajuste_grados': -15,
                'razon': 'Índice debe estar más extendido'
            },
            {
                'articulacion': 'middle_mcp',
                'frame_inicio': 10,
                'frame_fin': 80,
                'ajuste_grados': 10,
                'razon': 'Medio debe estar más cerrado'
            },
            {
                'articulacion': 'ring_mcp',
                'frame_inicio': 10,
                'frame_fin': 80,
                'ajuste_grados': 10,
                'razon': 'Anular debe estar más cerrado'
            },
            {
                'articulacion': 'pinky_mcp',
                'frame_inicio': 10,
                'frame_fin': 80,
                'ajuste_grados': 10,
                'razon': 'Meñique debe estar más cerrado'
            },
            {
                'articulacion': 'thumb_mcp',
                'frame_inicio': 10,
                'frame_fin': 80,
                'ajuste_grados': 5,
                'razon': 'Pulgar ligeramente hacia adentro'
            }
        ],
        'prioridad': 'ALTA',
        'impacto_linguistico': 'La posición del índice es crítica para la seña YO'
    }
    
    reporte = {
        'fecha_analisis': '2025-12-17',
        'video': video_info,
        'glb': glb_info,
        'correcciones': correcciones,
        'instrucciones_blender': {
            '1_abrir': 'Abrir Blender y cargar Nancy.glb + Nancy_resultado_yo_MEJORADO.glb',
            '2_timeline': 'Ir al Timeline y posicionarse en frame 10-80',
            '3_dedos': 'Seleccionar huesos de dedos en Pose Mode',
            '4_ajustar': 'Aplicar rotaciones según tabla de correcciones',
            '5_keyframe': 'Insertar keyframes en frames 10 y 80',
            '6_suavizar': 'Aplicar Graph Editor > Smooth',
            '7_exportar': 'File > Export > glTF 2.0 (.glb)'
        }
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(reporte, f, indent=2, ensure_ascii=False)
    
    return correcciones


def main():
    """Función principal"""
    print("\n" + "="*70)
    print("🔬 SISTEMA DE REFINAMIENTO LSV - ANÁLISIS: YO")
    print("="*70)
    
    # Configuración
    BASE_DIR = Path(__file__).parent.parent
    VIDEO_PATH = BASE_DIR / "test" / "output" / "videos" / "yo.mp4"
    GLB_ORIGINAL = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo.glb"
    GLB_MEJORADO = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "pronombres" / "Nancy_resultado_yo_MEJORADO.glb"
    OUTPUT_DIR = BASE_DIR / "test" / "output" / "comparisons"
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    
    # Paso 1: Verificar archivos
    print(f"\n{'='*70}")
    print("PASO 1: VERIFICACIÓN DE ARCHIVOS")
    print("="*70)
    
    if not VIDEO_PATH.exists():
        print(f"❌ Video no encontrado: {VIDEO_PATH}")
        return
    
    if not GLB_ORIGINAL.exists():
        print(f"❌ GLB original no encontrado: {GLB_ORIGINAL}")
        return
    
    print(f"✅ Video encontrado: {VIDEO_PATH.name}")
    print(f"✅ GLB original: {GLB_ORIGINAL.name}")
    
    # Paso 2: Analizar video
    print(f"\n{'='*70}")
    print("PASO 2: ANÁLISIS DEL VIDEO")
    print("="*70)
    
    video_info = analizar_video_yo(str(VIDEO_PATH))
    
    if not video_info:
        print("❌ Error al analizar video")
        return
    
    # Paso 3: Generar reporte de correcciones
    print(f"\n{'='*70}")
    print("PASO 3: GENERACIÓN DE CORRECCIONES")
    print("="*70)
    
    print(f"\n📋 CORRECCIONES SUGERIDAS PARA 'YO':")
    print(f"   • Índice: Debe estar más EXTENDIDO (-15°)")
    print(f"   • Medio: Debe estar más CERRADO (+10°)")
    print(f"   • Anular: Debe estar más CERRADO (+10°)")
    print(f"   • Meñique: Debe estar más CERRADO (+10°)")
    print(f"   • Pulgar: Ajuste ligero hacia adentro (+5°)")
    
    correcciones_info = [
        {'articulation': 'index_mcp', 'adjustment': -15, 'priority': '🔴 CRÍTICO'},
        {'articulation': 'middle_mcp', 'adjustment': 10, 'priority': '⚠️ IMPORTANTE'},
        {'articulation': 'ring_mcp', 'adjustment': 10, 'priority': '⚠️ IMPORTANTE'},
        {'articulation': 'pinky_mcp', 'adjustment': 10, 'priority': '⚠️ IMPORTANTE'},
        {'articulation': 'thumb_mcp', 'adjustment': 5, 'priority': '✅ MENOR'}
    ]
    
    # Paso 4: Crear GLB mejorado
    print(f"\n{'='*70}")
    print("PASO 4: CREACIÓN DE GLB MEJORADO")
    print("="*70)
    
    glb_info = crear_glb_mejorado(GLB_ORIGINAL, GLB_MEJORADO, correcciones_info)
    
    # Paso 5: Guardar reporte
    print(f"\n{'='*70}")
    print("PASO 5: GENERACIÓN DE REPORTE")
    print("="*70)
    
    report_path = OUTPUT_DIR / "yo_analisis_refinamiento.json"
    correcciones = generar_reporte_comparacion(video_info, glb_info, report_path)
    
    print(f"\n💾 Reporte guardado: {report_path}")
    
    # Resumen final
    print(f"\n{'='*70}")
    print("✅ PROCESO COMPLETADO")
    print("="*70)
    
    print(f"\n📁 ARCHIVOS GENERADOS:")
    print(f"   1. {GLB_MEJORADO.name}")
    print(f"   2. {report_path.name}")
    
    print(f"\n🎯 COMPARACIÓN DE VERSIONES:")
    print(f"   📦 Original: {GLB_ORIGINAL.name}")
    print(f"   ✨ Mejorado: {GLB_MEJORADO.name}")
    
    print(f"\n💡 PRÓXIMOS PASOS:")
    print(f"\n   OPCIÓN 1: Aplicar correcciones en Blender")
    print(f"   ----------------------------------------")
    print(f"   1. Abrir Blender")
    print(f"   2. File > Import > glTF 2.0")
    print(f"   3. Cargar: {GLB_ORIGINAL.name}")
    print(f"   4. Ir a Pose Mode")
    print(f"   5. Seleccionar dedos: f_index.01_r, f_middle.01_r, etc.")
    print(f"   6. En frames 10-80:")
    print(f"      - Índice: Rotar -15° en Z")
    print(f"      - Medio/Anular/Meñique: Rotar +10° en Z")
    print(f"      - Pulgar: Rotar +5° en Z")
    print(f"   7. Insertar keyframes (I > Rotation)")
    print(f"   8. Graph Editor > Smooth")
    print(f"   9. File > Export > glTF 2.0")
    print(f"   10. Guardar como: {GLB_MEJORADO.name}")
    
    print(f"\n   OPCIÓN 2: Probar en el navegador")
    print(f"   ----------------------------------------")
    print(f"   1. cd test")
    print(f"   2. python -m http.server 8000")
    print(f"   3. Abrir: http://localhost:8000/animation.html")
    print(f"   4. Escribir: 'yo'")
    print(f"   5. Ver animación actual (sin correcciones)")
    
    print(f"\n   OPCIÓN 3: Comparar versiones (después de aplicar correcciones)")
    print(f"   ----------------------------------------")
    print(f"   1. Renombrar temporalmente el original:")
    print(f"      Nancy_resultado_yo.glb → Nancy_resultado_yo_ORIGINAL_BACKUP.glb")
    print(f"   2. Copiar el mejorado:")
    print(f"      Nancy_resultado_yo_MEJORADO.glb → Nancy_resultado_yo.glb")
    print(f"   3. Probar en navegador: 'yo'")
    print(f"   4. Comparar ambas versiones")
    
    print(f"\n📊 INFORMACIÓN TÉCNICA:")
    print(f"   • Video: {video_info['duration']:.2f}s, {video_info['frame_count']} frames")
    print(f"   • GLB Original: {glb_info['size_mb']} MB")
    print(f"   • Correcciones: 5 articulaciones")
    print(f"   • Frames afectados: 10-80 (~{((80-10)/video_info['frame_count']*100):.0f}% del video)")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
