"""Test rápido para verificar traducción de 'maestro e ingeniera'"""

from api_optimizer import LSVOptimizer

optimizer = LSVOptimizer()

texto = "maestro e ingeniera"
resultado = optimizer.translate_to_animations(
    texto=texto,
    deletrear_desconocidas=True,
    corregir_ortografia=True
)

print("\n" + "="*60)
print(f"📝 TEXTO: '{texto}'")
print("="*60)
print(f"\n✅ Texto corregido: '{resultado['texto_corregido']}'")
print(f"📊 Total animaciones: {resultado['total_animaciones']}")

if resultado['correcciones']:
    print("\n🔧 Correcciones:")
    for corr in resultado['correcciones']:
        print(f"   • {corr['original']} → {corr['corregida']} ({corr['tipo']}, {corr['confianza']}%)")

print("\n🎬 Secuencia de animaciones:")
for i, anim in enumerate(resultado['animaciones'], 1):
    icono = "🔤" if anim['es_deletreo'] else "✋"
    print(f"   {i}. {icono} {anim['nombre'].upper()} ({anim['categoria']})")

if resultado['palabras_deletreadas']:
    print(f"\n📝 Palabras deletreadas: {', '.join(resultado['palabras_deletreadas'])}")

print("\n" + "="*60 + "\n")
