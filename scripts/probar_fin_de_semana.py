"""
Script de Prueba - Refinamiento LSV: Fin de Semana
Analiza el video "fin de semana.mp4" y lo compara con su animación GLB
"""

import cv2
import mediapipe as mp
import json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def analizar_video_fin_de_semana(video_path):
    """Análisis del video fin de semana con MediaPipe"""
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
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(f"   📊 FPS: {fps}, Frames: {frame_count}, Resolución: {width}x{height}")
    
    # Preparar video de salida con landmarks
    output_dir = Path(video_path).parent.parent / "comparisons"
    output_dir.mkdir(exist_ok=True, parents=True)
    
    output_video_path = output_dir / "analyzed_fin_de_semana.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(str(output_video_path), fourcc, fps, (width, height))
    
    frames_con_manos = 0
    frames_procesados = 0
    
    # Datos para análisis
    resultados = {
        'video': str(video_path),
        'fps': fps,
        'total_frames': frame_count,
        'frames_con_deteccion': 0,
        'keypoints_por_frame': []
    }
    
    print(f"   🔄 Procesando frames...")
    
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
                # Dibujar landmarks en el frame
                mp_drawing.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
                )
                
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
        
        # Agregar texto de progreso al frame
        cv2.putText(frame, f"Frame: {frames_procesados}/{frame_count}", 
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        if results.multi_hand_landmarks:
            cv2.putText(frame, "MANO DETECTADA", 
                        (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Sin deteccion", 
                        (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        out.write(frame)
        frames_procesados += 1
        
        # Mostrar progreso cada 30 frames
        if frames_procesados % 30 == 0:
            print(f"      {frames_procesados}/{frame_count} frames...")
    
    cap.release()
    out.release()
    hands.close()
    
    resultados['frames_con_deteccion'] = frames_con_manos
    porcentaje = (frames_con_manos / frame_count * 100) if frame_count > 0 else 0
    
    print(f"\n   ✅ Análisis completado!")
    print(f"   📊 Frames con manos: {frames_con_manos}/{frame_count} ({porcentaje:.1f}%)")
    print(f"   🎥 Video con landmarks: {output_video_path.name}")
    
    return resultados


def generar_reporte(resultados, output_path):
    """Genera reporte detallado en JSON"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=2)
    
    print(f"   💾 Reporte JSON: {Path(output_path).name}")


def visualizar_resultados(resultados, output_path):
    """Genera visualización completa de los resultados"""
    frames_con_deteccion = [frame['frame'] for frame in resultados['keypoints_por_frame']]
    total_frames = resultados['total_frames']
    
    if not frames_con_deteccion:
        print("   ⚠️ No hay frames con detección para visualizar")
        return
    
    fig, axes = plt.subplots(2, 1, figsize=(14, 8))
    
    # Gráfico 1: Detección por frame
    deteccion = [1 if i in frames_con_deteccion else 0 for i in range(total_frames)]
    
    axes[0].plot(range(total_frames), deteccion, linewidth=2, color='#4ECDC4')
    axes[0].fill_between(range(total_frames), deteccion, alpha=0.3, color='#4ECDC4')
    axes[0].set_title('Detección de Manos - Fin de Semana', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Frame')
    axes[0].set_ylabel('Detección (1=Sí, 0=No)')
    axes[0].set_ylim(-0.1, 1.1)
    axes[0].grid(True, alpha=0.3)
    
    # Estadísticas
    porcentaje = resultados['frames_con_deteccion'] / total_frames * 100
    axes[0].text(0.02, 0.95, f"Detección: {porcentaje:.1f}%\nFrames: {resultados['frames_con_deteccion']}/{total_frames}", 
                transform=axes[0].transAxes, fontsize=12,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Gráfico 2: Movimiento de mano en profundidad (eje Z)
    if frames_con_deteccion:
        z_values = []
        frame_nums = []
        
        for frame_data in resultados['keypoints_por_frame']:
            # Usar la muñeca (keypoint 0) como referencia
            if frame_data['keypoints']:
                wrist = frame_data['keypoints'][0]
                z_values.append(wrist['z'])
                frame_nums.append(frame_data['frame'])
        
        if z_values:
            axes[1].plot(frame_nums, z_values, linewidth=2, color='#FF6B6B', marker='o', markersize=3)
            axes[1].set_title('Movimiento en Profundidad (Eje Z) - Muñeca', fontsize=14, fontweight='bold')
            axes[1].set_xlabel('Frame')
            axes[1].set_ylabel('Profundidad Z')
            axes[1].grid(True, alpha=0.3)
            
            # Estadísticas de movimiento
            z_range = max(z_values) - min(z_values)
            axes[1].text(0.02, 0.95, f"Rango Z: {z_range:.3f}\nMin: {min(z_values):.3f}\nMax: {max(z_values):.3f}", 
                        transform=axes[1].transAxes, fontsize=10,
                        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"   📊 Visualización: {Path(output_path).name}")


def main():
    """Función principal"""
    print("\n" + "="*70)
    print("🔬 REFINAMIENTO LSV - ANÁLISIS: FIN DE SEMANA")
    print("="*70)
    
    # Configuración
    BASE_DIR = Path(__file__).parent.parent
    VIDEO_PATH = BASE_DIR / "test" / "output" / "videos" / "fin de semana.mp4"
    GLB_PATH = BASE_DIR / "test" / "output" / "glb" / "Nancy" / "tiempo" / "Nancy_resultado_fin de semana.glb"
    OUTPUT_DIR = BASE_DIR / "test" / "output" / "comparisons"
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    
    # Verificar archivos
    if not VIDEO_PATH.exists():
        print(f"\n❌ Video no encontrado: {VIDEO_PATH}")
        return
    
    if not GLB_PATH.exists():
        print(f"\n⚠️ GLB no encontrado: {GLB_PATH}")
        print("   (Continuando solo con análisis de video)")
    else:
        print(f"\n✅ Archivos encontrados:")
        print(f"   📹 Video: {VIDEO_PATH.name}")
        print(f"   🎭 GLB: {GLB_PATH.name}")
    
    # Paso 1: Analizar video
    print(f"\n{'='*70}")
    print("PASO 1: ANÁLISIS DE VIDEO CON MEDIAPIPE")
    print("="*70)
    
    resultados = analizar_video_fin_de_semana(str(VIDEO_PATH))
    
    # Paso 2: Generar reporte
    print(f"\n{'='*70}")
    print("PASO 2: GENERACIÓN DE REPORTES")
    print("="*70)
    
    report_path = OUTPUT_DIR / "fin_de_semana_analisis.json"
    generar_reporte(resultados, str(report_path))
    
    # Paso 3: Generar visualización
    viz_path = OUTPUT_DIR / "fin_de_semana_visualizacion.png"
    visualizar_resultados(resultados, str(viz_path))
    
    # Resumen final
    print(f"\n{'='*70}")
    print("✅ ANÁLISIS COMPLETADO")
    print("="*70)
    
    print(f"\n📁 Archivos generados en: {OUTPUT_DIR}")
    print(f"   1. 📄 {report_path.name} - Datos completos JSON")
    print(f"   2. 📊 {viz_path.name} - Gráficos de análisis")
    print(f"   3. 🎥 analyzed_fin_de_semana.mp4 - Video con landmarks")
    
    # Evaluación
    porcentaje = resultados['frames_con_deteccion'] / resultados['total_frames'] * 100
    
    print(f"\n📊 EVALUACIÓN:")
    if porcentaje >= 80:
        print(f"   ✅ EXCELENTE: {porcentaje:.1f}% de detección")
        print(f"   ✅ El video es ideal para refinamiento")
    elif porcentaje >= 60:
        print(f"   ⚠️ BUENO: {porcentaje:.1f}% de detección")
        print(f"   ⚠️ Se puede refinar, algunos frames sin mano")
    else:
        print(f"   🔴 BAJO: {porcentaje:.1f}% de detección")
        print(f"   🔴 Considerar re-grabar el video")
    
    print(f"\n💡 PRÓXIMOS PASOS:")
    print(f"   1. Revisar: {viz_path.name}")
    print(f"   2. Ver: analyzed_fin_de_semana.mp4")
    print(f"   3. Si detección > 80%, ejecutar comparador completo:")
    print(f"      python scripts/video_to_glb_comparator.py")
    print(f"   4. Aplicar correcciones en Blender")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Proceso interrumpido por el usuario")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
