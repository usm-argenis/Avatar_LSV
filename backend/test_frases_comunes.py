"""
Más pruebas de frases comunes en LSV
"""
from api_optimizer import LSVOptimizer

optimizer = LSVOptimizer()

ejemplos = [
    "yo tengo 18 años",
    "mi nombre es José",
    "hola buenos días",
    "mañana voy a la universidad",
    "no entiendo",
    "yo soy sordo",
    "tú cómo estás",
]

print("="*80)
print("PRUEBAS DE FRASES COMUNES EN LSV")
print("="*80 + "\n")

for i, frase in enumerate(ejemplos, 1):
    resultado = optimizer.translate_to_animations(frase)
    print(f"{i}. '{frase}'")
    print(f"   → {resultado['glosa_lsv']}")
    if resultado['palabras_deletreadas']:
        print(f"   (deletreadas: {', '.join(resultado['palabras_deletreadas'])})")
    print()
