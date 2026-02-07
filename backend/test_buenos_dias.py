"""Test rápido para verificar detección de "buenos días" """
from api_optimizer import LSVOptimizer

opt = LSVOptimizer()

# Probar con y sin acento
frases = [
    "buenos dias",
    "buenos días",
    "hola buenos días"
]

for frase in frases:
    print(f"\n{'='*60}")
    print(f"Probando: '{frase}'")
    print('='*60)
    
    resultado = opt.translate_to_animations(
        frase,
        deletrear_desconocidas=True,
        corregir_ortografia=True
    )
    
    # Mostrar animaciones
    print(f"\n📋 Animaciones generadas:")
    for i, anim in enumerate(resultado['animaciones'], 1):
        if not anim.get('es_deletreo', False):
            print(f"  {i}. {anim['nombre'].upper()}")
    
    print(f"\n📊 Total: {resultado['total_animaciones']} animaciones")
    
    if resultado.get('palabras_deletreadas'):
        print(f"🔡 Deletreadas: {', '.join(resultado['palabras_deletreadas'])}")
