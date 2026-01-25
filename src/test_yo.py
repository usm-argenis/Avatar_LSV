"""
Prueba específica para generar animación de "YO"
"""

from ai.motion_generator import MotionGenerator
from api.translator import SignTranslator

print("=" * 60)
print("PRUEBA: Generación de animación para 'YO'")
print("=" * 60)

# Inicializar
generator = MotionGenerator(keypoints_dir="data/keypoints")
translator = SignTranslator()

# Verificar que "yo" existe
print(f"\n1. Verificando base de datos...")
print(f"   Señas disponibles: {list(generator.sign_database.keys())}")

yo_data = generator.sign_database.get('yo')
if yo_data:
    print(f"   ✓ 'yo' encontrado")
    print(f"   Keyframes: {len(yo_data.get('keyframes', []))}")
else:
    print(f"   ✗ 'yo' NO encontrado")

# Probar traducción
print(f"\n2. Traduciendo texto...")
signs = translator.translate("yo")
print(f"   Señas traducidas: {[s['sign'] for s in signs]}")

# Generar keyframes
print(f"\n3. Generando keyframes...")
keyframes = generator.sequence_to_keyframes(["yo"])
print(f"   Frames generados: {len(keyframes.get('frames', []))}")
print(f"   Duración: {keyframes.get('duration', 0):.2f}s")

if len(keyframes.get('frames', [])) > 0:
    print(f"\n4. Generando animación...")
    animation = generator.generate_animation(keyframes, smooth=False)
    
    print(f"\n5. Exportando...")
    success = generator.export_glb(animation, "test_yo.json")
    
    if success:
        print(f"\n✅ ÉXITO: Animación de 'yo' generada en test_yo.json")
    else:
        print(f"\n❌ ERROR: No se pudo exportar")
else:
    print(f"\n❌ ERROR: No se generaron keyframes")

print("\n" + "=" * 60)
