"""
Sistema Integrado de Generación de Animaciones 3D
Prueba completa del pipeline: Texto -> Señas -> Keyframes -> Animación
"""

import sys
from pathlib import Path

# Agregar src al path
src_path = Path(__file__).parent
sys.path.insert(0, str(src_path))

from ai.motion_generator import MotionGenerator
from api.translator import SignTranslator


def test_complete_pipeline():
    """
    Prueba completa del sistema de generación de animaciones
    """
    print("=" * 80)
    print("🚀 SISTEMA DE GENERACIÓN DE ANIMACIONES 3D - LENGUA DE SEÑAS VENEZOLANA")
    print("=" * 80)
    print()
    
    # Inicializar componentes
    print("📦 Inicializando componentes...")
    translator = SignTranslator()
    generator = MotionGenerator(
        keypoints_dir=str(src_path / "data" / "keypoints")
    )
    print()
    
    # Frases de prueba
    test_phrases = [
        "hola",
        "gracias",
        "hola gracias"
    ]
    
    for phrase in test_phrases:
        print("\n" + "=" * 80)
        print(f"📝 PROCESANDO: '{phrase}'")
        print("=" * 80)
        
        # Paso 1: Traducir texto a señas
        print("\n🔤 Paso 1: Traduciendo texto a señas...")
        signs = translator.translate(phrase)
        sign_names = [s['sign'] for s in signs]
        print(f"   Señas detectadas: {' -> '.join(sign_names)}")
        
        # Paso 2: Convertir a secuencia de keyframes
        print("\n🎯 Paso 2: Generando keyframes...")
        keyframes = generator.sequence_to_keyframes(sign_names)
        print(f"   Total de frames: {len(keyframes.get('frames', []))}")
        print(f"   Duración: {keyframes.get('duration', 0):.2f} segundos")
        
        # Paso 3: Generar animación con suavizado
        print("\n✨ Paso 3: Generando animación suavizada...")
        animation = generator.generate_animation(keyframes, smooth=True)
        
        # Paso 4: Exportar
        output_file = f"output_{phrase.replace(' ', '_')}.json"
        print(f"\n💾 Paso 4: Exportando animación...")
        success = generator.export_glb(animation, output_file)
        
        if success:
            print(f"\n✅ ÉXITO: Animación generada para '{phrase}'")
        else:
            print(f"\n❌ ERROR: No se pudo generar animación para '{phrase}'")
    
    print("\n" + "=" * 80)
    print("🎉 PRUEBA COMPLETA FINALIZADA")
    print("=" * 80)


def interactive_mode():
    """
    Modo interactivo para probar el sistema
    """
    print("=" * 80)
    print("🎮 MODO INTERACTIVO - GENERADOR DE ANIMACIONES")
    print("=" * 80)
    print()
    print("Escribe una frase en español y se generará la animación correspondiente.")
    print("Escribe 'salir' para terminar.")
    print()
    
    # Inicializar
    translator = SignTranslator()
    generator = MotionGenerator(
        keypoints_dir=str(Path(__file__).parent / "data" / "keypoints")
    )
    
    while True:
        print("\n" + "-" * 80)
        text = input("📝 Ingresa texto (o 'salir'): ").strip()
        
        if text.lower() in ['salir', 'exit', 'quit']:
            print("\n👋 ¡Hasta luego!")
            break
        
        if not text:
            print("⚠️  Por favor ingresa un texto válido")
            continue
        
        try:
            # Generar animación
            animation = generator.generate_from_text(
                text,
                output_path=f"interactive_{text.replace(' ', '_')}.json"
            )
            
            print(f"\n✅ Animación generada exitosamente!")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Sistema de Generación de Animaciones 3D para Lengua de Señas"
    )
    parser.add_argument(
        "--mode",
        choices=["test", "interactive"],
        default="test",
        help="Modo de ejecución: test (pruebas automáticas) o interactive (modo interactivo)"
    )
    
    args = parser.parse_args()
    
    if args.mode == "interactive":
        interactive_mode()
    else:
        test_complete_pipeline()
