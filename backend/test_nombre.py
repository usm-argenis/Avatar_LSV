from api_optimizer import LSVOptimizer

opt = LSVOptimizer()

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("🧪 TEST: 'mi nombre es argenis'")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

texto = "mi nombre es argenis"
resultado = opt.translate_to_animations(texto)

print(f"📝 Texto original: {resultado['texto_original']}")
print(f"📝 Texto corregido: {resultado['texto_corregido']}")
print(f"\n✏️ Correcciones: {len(resultado['correcciones'])}")
for corr in resultado['correcciones']:
    print(f"  - '{corr['original']}' → '{corr['corregida']}' ({corr['tipo']}, {corr['confianza']}% confianza)")

print(f"\n🎬 Animaciones ({len(resultado['animaciones'])}):")
for i, anim in enumerate(resultado['animaciones'], 1):
    print(f"  {i}. {anim}")

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("✅ ESPERADO: MIO + deletreado de ARGENIS (sin corregir 'nombre' a 'hombre')")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

# Test adicional
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("🧪 TEST 2: 'cual es tu nombre'")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

texto2 = "cual es tu nombre"
resultado2 = opt.translate_to_animations(texto2)

print(f"📝 Texto original: {resultado2['texto_original']}")
print(f"📝 Texto corregido: {resultado2['texto_corregido']}")
print(f"\n🎬 Animaciones ({len(resultado2['animaciones'])}):")
for i, anim in enumerate(resultado2['animaciones'], 1):
    print(f"  {i}. {anim}")

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("✅ ESPERADO: 1 sola animación 'CUAL ES TU NOMBRE'")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
