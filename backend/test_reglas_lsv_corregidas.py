"""
Test de reglas LSV corregidas según el prompt del usuario
"""

from api_optimizer import LSVOptimizer

# Inicializar optimizador
optimizer = LSVOptimizer()

print("=" * 80)
print("🧪 TEST: REGLAS LSV CORREGIDAS")
print("=" * 80)
print()

# Frase principal del usuario
frase_principal = "Bienvenidos a la defensa de nuestro TEG: Un aporte tecnológico para la integración de la comunidad sorda venezolana"

print("📝 FRASE A TRADUCIR:")
print(f"   {frase_principal}")
print()

# Traducir
resultado = optimizer.translate_to_animations(
    frase_principal,
    deletrear_desconocidas=True,
    corregir_ortografia=False
)

print("✅ GLOSA LSV:")
print(f"   {resultado['glosa_lsv']}")
print()

print("🎬 SECUENCIA DE ANIMACIONES:")
for i, anim in enumerate(resultado['animaciones'], 1):
    prefijo = "🔤" if anim.get('es_deletreo') else "✋"
    print(f"   {i}. {prefijo} {anim['nombre'].upper():20s} [{anim['categoria']}]")
print()

if resultado['observaciones_linguisticas']:
    print("📋 OBSERVACIONES LINGÜÍSTICAS:")
    for obs in resultado['observaciones_linguisticas']:
        print(f"   • {obs}")
    print()

if resultado['palabras_deletreadas']:
    print("🔤 PALABRAS DELETREADAS:")
    for palabra in resultado['palabras_deletreadas']:
        print(f"   • {palabra}")
    print()

print(f"📊 Total de animaciones: {resultado['total_animaciones']}")
print()

# Tests adicionales
print("=" * 80)
print("🧪 TESTS ADICIONALES")
print("=" * 80)
print()

frases_test = [
    "mañana mi hermano va a trabajar en la universidad",
    "yo tengo 18 años",
    "la ingeniera trabaja en el sistema",
    "no existe accesibilidad para personas sordas"
]

for frase in frases_test:
    print(f"📝 Frase: {frase}")
    resultado = optimizer.translate_to_animations(frase, deletrear_desconocidas=True)
    print(f"✅ Glosa: {resultado['glosa_lsv']}")
    print()

print("=" * 80)
print("✅ TEST COMPLETADO")
print("=" * 80)
