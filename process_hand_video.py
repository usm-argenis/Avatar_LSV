"""
USO RÁPIDO: Análisis de orientación de manos

Script simplificado para procesar un video y obtener cuaterniones.
"""

from hand_quaternion_analyzer import HandQuaternionAnalyzer
from pathlib import Path


def process_hand_video(video_path: str, 
                       output_name: str = None,
                       show_video: bool = True):
    """
    Procesa un video de manos y genera archivos JSON y CSV con cuaterniones.
    
    Args:
        video_path: Ruta al video (relativa o absoluta)
        output_name: Nombre base para archivos de salida (sin extensión)
        show_video: Si mostrar el video durante procesamiento
    """
    video_file = Path(video_path)
    
    if not video_file.exists():
        print(f"❌ Error: Video no encontrado en {video_path}")
        return
    
    # Generar nombre de salida automático si no se proporciona
    if output_name is None:
        output_name = video_file.stem + "_hand_analysis"
    
    # Directorio de salida
    output_dir = Path("output/hand_analysis")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("="*80)
    print("🖐️  ANÁLISIS DE ORIENTACIÓN DE MANOS CON CUATERNIONES")
    print("="*80)
    print(f"Video: {video_file.name}")
    print(f"Salida: {output_name}.json / .csv")
    print("="*80)
    print()
    
    # Crear analizador y procesar
    analyzer = HandQuaternionAnalyzer(str(video_file))
    
    results = analyzer.process_video(
        output_json=str(output_dir / f"{output_name}.json"),
        output_csv=str(output_dir / f"{output_name}.csv"),
        visualize=show_video
    )
    
    print("\n" + "="*80)
    print("✅ PROCESO COMPLETADO")
    print("="*80)
    
    return results


if __name__ == "__main__":
    # CONFIGURACIÓN: Cambiar ruta del video aquí
    VIDEO_PATH = r"test\output\videos\miercoles.mp4"
    
    # Procesar
    results = process_hand_video(
        video_path=VIDEO_PATH,
        output_name="miercoles_hands",
        show_video=True  # Cambiar a False para procesamiento sin visualización
    )
    
    # Mostrar resumen
    if results:
        frames_con_manos = sum(1 for f in results if f['hands'])
        print(f"\n📈 Resumen:")
        print(f"   Frames procesados: {len(results)}")
        print(f"   Frames con manos detectadas: {frames_con_manos}")
        print(f"   Tasa de detección: {(frames_con_manos/len(results)*100):.1f}%")
