"""
Script de Prueba Rápida - Sistema de Refinamiento LSV
Analiza un video y compara con su animación GLB correspondiente

Uso:
    python ejemplo_refinamiento_gracias.py
"""

import cv2
import mediapipe as mp
import json
from pathlib import Path
import matplotlib.pyplot as plt


def analizar_video_simple(video_path):
    """Análisis simplificado con MediaPipe"""
    print(f"\n📹 Analizando: {Path(video_path).name}")
    
    # Inicializar MediaPipe Hands
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    )
    
    # Abrir video
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"   FPS: {fps}, Frames totales: {frame_count}")
    
    frames_con_manos = 0
    frames_procesados = 0
    
    # Datos de ejemplo para análisis
    resultados = {
        'video': str(video_path),
        'fps': fps,
        'total_frames': frame_count,
        'frames_con_deteccion': 0,
        'keypoints_por_frame': []
    }
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        # Convertir a RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            frames_con_manos += 1
            
            for hand_landmarks in results.multi_hand_landmarks:
                # Extraer coordenadas
                keypoints = []
                for landmark in hand_landmarks.landmark:
                    keypoints.append({
                        'x': landmark.x,
                        'y': landmark.y,
                        'z': landmark.z
                    })
                
                resultados['keypoints_por_frame'].append({
                    'frame': frames_procesados,
                    'keypoints': keypoints
                })
        
        frames_procesados += 1
        
        # Mostrar progreso cada 30 frames
        if frames_procesados % 30 == 0:
            print(f"   Procesados {frames_procesados}/{frame_count} frames...")
    
    cap.release()
    hands.close()
    
    resultados['frames_con_deteccion'] = frames_con_manos
    
    print(f"\n✅ Análisis completado!")
    print(f"   Frames con manos detectadas: {frames_con_manos}/{frame_count} ({frames_con_manos/frame_count*100:.1f}%)")
    
    return resultados


def generar_reporte(resultados, output_path):
    """Genera reporte simple en JSON"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=2)
    
    print(f"\n💾 Reporte guardado: {output_path}")


def visualizar_deteccion(resultados, output_path):
    """Genera gráfico de detección por frame"""
    frames_con_deteccion = [frame['frame'] for frame in resultados['keypoints_por_frame']]
    
    if not frames_con_deteccion:
        print("⚠️ No hay frames con detección para visualizar")
        return
    
    fig, ax = plt.subplots(figsize=(12, 4))
    
    # Gráfico de barras de detección
    total_frames = resultados['total_frames']
    deteccion = [1 if i in frames_con_deteccion else 0 for i in range(total_frames)]
    
    ax.plot(range(total_frames), deteccion, linewidth=2, color='#4ECDC4')
    ax.fill_between(range(total_frames), deteccion, alpha=0.3, color='#4ECDC4')
    ax.set_title(f'Detección de Manos - {Path(resultados["video"]).name}', fontsize=14, fontweight='bold')
    ax.set_xlabel('Frame')
    ax.set_ylabel('Detección (1=Sí, 0=No)')
    ax.set_ylim(-0.1, 1.1)
    ax.grid(True, alpha=0.3)
    
    # Estadísticas
    porcentaje = resultados['frames_con_deteccion'] / total_frames * 100
    ax.text(0.02, 0.95, f"Detección: {porcentaje:.1f}%", 
            transform=ax.transAxes, fontsize=12,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    print(f"📊 Visualización guardada: {output_path}")


def main():
    """Función principal"""
    print("="*60)
    print("🔬 PRUEBA RÁPIDA - SISTEMA DE REFINAMIENTO LSV")
    print("="*60)
    
    # Configuración
    BASE_DIR = Path(__file__).parent.parent
    VIDEO_PATH = BASE_DIR / "test" / "output" / "videos" / "gracias.mp4"
    OUTPUT_DIR = BASE_DIR / "test" / "output" / "comparisons"
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    
    # Verificar que existe el video
    if not VIDEO_PATH.exists():
        print(f"\n❌ Video no encontrado: {VIDEO_PATH}")
        print("\n📁 Videos disponibles:")
        video_dir = BASE_DIR / "test" / "output" / "videos"
        for video in sorted(video_dir.glob("*.mp4"))[:10]:
            print(f"   - {video.name}")
        return
    
    # Analizar video
    print(f"\n[1/3] Analizando video...")
    resultados = analizar_video_simple(str(VIDEO_PATH))
    
    # Generar reporte
    print(f"\n[2/3] Generando reporte...")
    report_path = OUTPUT_DIR / "gracias_analisis_simple.json"
    generar_reporte(resultados, str(report_path))
    
    # Generar visualización
    print(f"\n[3/3] Generando visualización...")
    viz_path = OUTPUT_DIR / "gracias_deteccion.png"
    visualizar_deteccion(resultados, str(viz_path))
    
    print("\n" + "="*60)
    print("✅ ANÁLISIS COMPLETADO")
    print("="*60)
    print(f"\nArchivos generados:")
    print(f"  📄 Reporte: {report_path}")
    print(f"  📊 Gráfico: {viz_path}")
    print(f"\nPróximos pasos:")
    print(f"  1. Revisar {viz_path.name}")
    print(f"  2. Si la detección es buena (>80%), ejecutar comparador completo")
    print(f"  3. Usar: python scripts/video_to_glb_comparator.py")
    print("="*60)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
