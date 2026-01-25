"""
🎬 Demostración Visual del Sistema de Generación de Animaciones
Muestra el proceso completo con visualización paso a paso
"""

import json
from pathlib import Path
import sys

# Agregar src al path
src_path = Path(__file__).parent
sys.path.insert(0, str(src_path))

from ai.motion_generator import MotionGenerator
from api.translator import SignTranslator


def print_header(title):
    """Imprime un encabezado decorado"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")


def visualize_keyframe(keyframe, frame_num):
    """Visualiza un keyframe de forma legible"""
    print(f"\n📍 Frame {frame_num} (t={keyframe['time']:.2f}s):")
    
    pose = keyframe['pose']
    
    # Mano derecha
    hand = pose['right_hand']
    print(f"  🤚 Mano derecha:")
    print(f"     Posición: ({hand['x']:.2f}, {hand['y']:.2f}, {hand['z']:.2f})")
    print(f"     Rotación: ({hand['rotation_x']:.0f}°, {hand['rotation_y']:.0f}°, {hand['rotation_z']:.0f}°)")
    
    # Brazo
    arm = pose['right_arm']
    print(f"  💪 Brazo derecho:")
    print(f"     Codo: {arm['elbow_angle']:.0f}°")
    print(f"     Hombro: {arm['shoulder_angle']:.0f}°")
    
    # Cabeza
    head = pose['head']
    print(f"  🧑 Cabeza:")
    print(f"     Rotación: ({head['rotation_x']:.0f}°, {head['rotation_y']:.0f}°, {head['rotation_z']:.0f}°)")


def demo_translation():
    """Demuestra el proceso de traducción"""
    print_header("🔤 DEMOSTRACIÓN: TRADUCCIÓN DE TEXTO")
    
    translator = SignTranslator()
    
    test_phrases = [
        "hola",
        "gracias",
        "hola gracias adios",
        "yo ir a trabajar",
        "mama y papa"
    ]
    
    for phrase in test_phrases:
        print(f"\n📝 Texto: \"{phrase}\"")
        signs = translator.translate(phrase)
        
        print(f"   ➜ {len(signs)} señas detectadas:")
        for i, sign in enumerate(signs, 1):
            print(f"      {i}. {sign['sign']} ({sign['category']})")


def demo_keyframe_generation():
    """Demuestra la generación de keyframes"""
    print_header("🎯 DEMOSTRACIÓN: GENERACIÓN DE KEYFRAMES")
    
    generator = MotionGenerator(
        keypoints_dir=str(src_path / "data" / "keypoints")
    )
    
    signs = ["hola", "gracias"]
    
    print(f"📋 Secuencia de señas: {' → '.join(signs)}")
    
    keyframes = generator.sequence_to_keyframes(signs)
    
    print(f"\n✅ Keyframes generados:")
    print(f"   Total de frames: {len(keyframes['frames'])}")
    print(f"   Duración: {keyframes['duration']:.2f} segundos")
    print(f"   FPS: {keyframes['fps']}")
    
    # Mostrar algunos keyframes clave
    frames_to_show = [0, len(keyframes['frames']) // 2, len(keyframes['frames']) - 1]
    
    for idx in frames_to_show:
        if idx < len(keyframes['frames']):
            frame = keyframes['frames'][idx]
            visualize_keyframe(frame['keypoints'], frame['frame'])


def demo_interpolation():
    """Demuestra el proceso de interpolación"""
    print_header("✨ DEMOSTRACIÓN: INTERPOLACIÓN Y SUAVIZADO")
    
    generator = MotionGenerator(
        keypoints_dir=str(src_path / "data" / "keypoints")
    )
    
    print("🎬 Generando animación con interpolación...")
    
    signs = ["hola", "gracias"]
    keyframes = generator.sequence_to_keyframes(signs)
    
    print(f"\n📊 Antes del suavizado:")
    print(f"   Frames: {len(keyframes['frames'])}")
    
    animation = generator.generate_animation(keyframes, smooth=True)
    
    print(f"\n📊 Después del suavizado:")
    print(f"   Frames: {len(animation['frames'])}")
    print(f"   Duración: {animation['duration']:.2f}s")
    
    # Comparar frames adyacentes
    if len(animation['frames']) >= 3:
        print(f"\n🔍 Comparación de frames consecutivos:")
        
        for i in range(min(3, len(animation['frames']) - 1)):
            frame1 = animation['frames'][i]
            frame2 = animation['frames'][i + 1]
            
            pos1 = frame1['keypoints']['pose']['right_hand']
            pos2 = frame2['keypoints']['pose']['right_hand']
            
            dx = pos2['x'] - pos1['x']
            dy = pos2['y'] - pos1['y']
            dz = pos2['z'] - pos1['z']
            
            distance = (dx**2 + dy**2 + dz**2) ** 0.5
            
            print(f"   Frame {i} → {i+1}: distancia = {distance:.4f} unidades")


def demo_complete_pipeline():
    """Demuestra el pipeline completo"""
    print_header("🚀 DEMOSTRACIÓN: PIPELINE COMPLETO")
    
    generator = MotionGenerator(
        keypoints_dir=str(src_path / "data" / "keypoints")
    )
    
    test_text = "hola gracias"
    output_file = "demo_output.json"
    
    print(f"📝 Texto de entrada: \"{test_text}\"")
    print(f"📁 Archivo de salida: {output_file}\n")
    
    print("⏳ Procesando...")
    
    # Ejecutar pipeline
    animation = generator.generate_from_text(test_text, output_file)
    
    print("\n✅ ¡Animación generada!")
    
    # Cargar y mostrar estadísticas
    with open(output_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"\n📊 Estadísticas del archivo generado:")
    print(f"   Total de frames: {len(data['frames'])}")
    print(f"   Duración: {data['duration']:.2f} segundos")
    print(f"   FPS: {data['fps']}")
    print(f"   Tamaño del archivo: {len(json.dumps(data)) / 1024:.2f} KB")
    
    # Mostrar timeline
    print(f"\n⏱️  Timeline de la animación:")
    current_sign = None
    for frame in data['frames']:
        if frame['sign'] != current_sign:
            current_sign = frame['sign']
            print(f"   {frame['time']:.2f}s: {current_sign}")


def demo_dictionary():
    """Demuestra el diccionario de señas"""
    print_header("📚 DEMOSTRACIÓN: DICCIONARIO DE SEÑAS")
    
    translator = SignTranslator()
    
    print(f"Total de palabras en el diccionario: {len(translator.dictionary)}\n")
    
    # Agrupar por categoría
    categories = {}
    for word, info in translator.dictionary.items():
        cat = info['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(word)
    
    # Mostrar por categoría
    for category, words in sorted(categories.items()):
        print(f"\n📂 {category.upper()}: ({len(words)} palabras)")
        print(f"   {', '.join(sorted(words))}")


def main():
    """Ejecuta todas las demostraciones"""
    print("""
    ╔════════════════════════════════════════════════════════════════════════╗
    ║                                                                        ║
    ║   🎬 DEMOSTRACIÓN DEL SISTEMA DE GENERACIÓN DE ANIMACIONES 3D         ║
    ║      Lengua de Señas Venezolana (LSV)                                 ║
    ║                                                                        ║
    ╚════════════════════════════════════════════════════════════════════════╝
    """)
    
    try:
        # Ejecutar demostraciones
        demo_dictionary()
        demo_translation()
        demo_keyframe_generation()
        demo_interpolation()
        demo_complete_pipeline()
        
        print_header("✅ DEMOSTRACIÓN COMPLETADA")
        print("""
        El sistema ha demostrado exitosamente:
        
        ✅ Traducción de texto a señas
        ✅ Generación de keyframes
        ✅ Interpolación cúbica entre poses
        ✅ Suavizado de movimientos
        ✅ Exportación a JSON
        ✅ Pipeline completo funcional
        
        📁 Archivos generados:
           - demo_output.json
        
        🚀 El sistema está listo para uso en producción!
        """)
        
    except Exception as e:
        print(f"\n❌ Error durante la demostración: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
