"""
Script Simplificado - Análisis Básico de Video
Verifica el video "fin de semana.mp4" sin MediaPipe
"""

import cv2
from pathlib import Path
import json


def analizar_video_basico(video_path):
    """Análisis básico del video sin MediaPipe"""
    print(f"\n📹 Analizando: {Path(video_path).name}")
    
    # Abrir video
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"❌ No se pudo abrir el video")
        return None
    
    # Obtener propiedades
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = frame_count / fps if fps > 0 else 0
    
    print(f"\n📊 PROPIEDADES DEL VIDEO:")
    print(f"   • FPS: {fps}")
    print(f"   • Frames totales: {frame_count}")
    print(f"   • Resolución: {width}x{height}")
    print(f"   • Duración: {duration:.2f} segundos")
    
    # Leer algunos frames para verificar
    print(f"\n🔍 Verificando frames...")
    frames_leidos = 0
    
    while cap.isOpened() and frames_leidos < frame_count:
        success, frame = cap.read()
        if not success:
            break
        frames_leidos += 1
        
        if frames_leidos % 30 == 0:
            print(f"   Verificados {frames_leidos}/{frame_count} frames...")
    
    cap.release()
    
    print(f"\n✅ Video válido: {frames_leidos} frames leídos correctamente")
    
    return {
        'video': str(video_path),
        'fps': fps,
        'frame_count': frame_count,
        'width': width,
        'height': height,
        'duration': duration,
        'frames_leidos': frames_leidos
    }


def verificar_glb(glb_path):
    """Verifica que el archivo GLB existe y su tamaño"""
    if not glb_path.exists():
        return None
    
    size_mb = glb_path.stat().st_size / (1024 * 1024)
    
    return {
        'path': str(glb_path),
        'size_mb': round(size_mb, 2),
        'exists': True
    }


def main():
    """Función principal"""
    print("\n" + "="*70)
    print("🔬 ANÁLISIS BÁSICO: FIN DE SEMANA")
    print("="*70)
    
    # Configuración
    BASE_DIR = Path(__file__).parent.parent
    VIDEO_PATH = BASE_DIR / "test" / "output" / "videos" / "fin de semana.mp4"
    GLB_PATH = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "tiempo" / "Nancy_resultado_fin de semana.glb"
    OUTPUT_DIR = BASE_DIR / "test" / "output" / "comparisons"
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    
    # Verificar video
    print(f"\n{'='*70}")
    print("PASO 1: VERIFICACIÓN DE VIDEO")
    print("="*70)
    
    if not VIDEO_PATH.exists():
        print(f"\n❌ Video no encontrado: {VIDEO_PATH}")
        return
    
    video_info = analizar_video_basico(str(VIDEO_PATH))
    
    # Verificar GLB
    print(f"\n{'='*70}")
    print("PASO 2: VERIFICACIÓN DE ANIMACIÓN GLB")
    print("="*70)
    
    if not GLB_PATH.exists():
        print(f"\n❌ GLB no encontrado: {GLB_PATH}")
        glb_info = None
    else:
        glb_info = verificar_glb(GLB_PATH)
        print(f"\n✅ GLB encontrado:")
        print(f"   • Archivo: {GLB_PATH.name}")
        print(f"   • Tamaño: {glb_info['size_mb']} MB")
    
    # Guardar reporte
    print(f"\n{'='*70}")
    print("PASO 3: GENERACIÓN DE REPORTE")
    print("="*70)
    
    reporte = {
        'video': video_info,
        'glb': glb_info,
        'fecha_analisis': '2025-12-17'
    }
    
    report_path = OUTPUT_DIR / "fin_de_semana_info.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(reporte, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Reporte guardado: {report_path}")
    
    # Resumen final
    print(f"\n{'='*70}")
    print("✅ VERIFICACIÓN COMPLETADA")
    print("="*70)
    
    print(f"\n📊 RESUMEN:")
    print(f"   • Video: ✅ Válido ({video_info['duration']:.2f}s, {video_info['frame_count']} frames)")
    print(f"   • GLB: {'✅ Encontrado' if glb_info else '❌ No encontrado'}")
    
    print(f"\n💡 SIGUIENTE PASO:")
    print(f"   Para análisis con MediaPipe (detección de manos):")
    print(f"   1. Instalar MediaPipe correctamente:")
    print(f"      pip uninstall mediapipe")
    print(f"      pip install mediapipe==0.10.9")
    print(f"   2. Ejecutar: python scripts/probar_fin_de_semana.py")
    
    print(f"\n   O usar el sistema web para ver la animación:")
    print(f"   1. cd test")
    print(f"   2. python -m http.server 8000")
    print(f"   3. Abrir: http://localhost:8000/animation.html")
    print(f"   4. Escribir: 'fin de semana'")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
