"""
Test rápido: yo tengo 18 años
"""
from api_optimizer import LSVOptimizer

optimizer = LSVOptimizer()

# Probar "yo tengo 18 años"
resultado = optimizer.translate_to_animations("yo tengo 18 años")

print("="*80)
print("PRUEBA: 'yo tengo 18 años'")
print("="*80)
print(f"\n🎯 GLOSA LSV: {resultado['glosa_lsv']}")
print(f"\n📋 Secuencia detallada:")
for i, anim in enumerate(resultado['animaciones'], 1):
    print(f"  {i}. {anim['nombre'].upper()} (archivo: {anim['archivo']})")

print("\n" + "="*80)
