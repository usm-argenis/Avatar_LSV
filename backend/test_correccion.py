from api_optimizer import LSVOptimizer

opt = LSVOptimizer()

# Prueba 1: Corrección simple
print("=" * 60)
print("PRUEBA 1: Corrección ortográfica")
print("=" * 60)
texto, corr = opt.corregir_texto('ola cmo estas')
print(f"Original:  'ola cmo estas'")
print(f"Corregido: '{texto}'")
print(f"\nCorrecciones:")
for c in corr:
    print(f"  ✓ {c['original']} → {c['corregida']} ({c['tipo']}, {c['confianza']}%)")

# Prueba 2: Corrección compleja
print("\n" + "=" * 60)
print("PRUEBA 2: Frase compleja con errores")
print("=" * 60)
texto2, corr2 = opt.corregir_texto('yo traajo en gogle mi ermana estuida')
print(f"Original:  'yo traajo en gogle mi ermana estuida'")
print(f"Corregido: '{texto2}'")
print(f"\nCorrecciones:")
for c in corr2:
    print(f"  ✓ {c['original']} → {c['corregida']} ({c['tipo']}, {c['confianza']}%)")

# Prueba 3: Traducción completa
print("\n" + "=" * 60)
print("PRUEBA 3: Traducción con corrección automática")
print("=" * 60)
resultado = opt.translate_to_animations('ola yo traajo en la univercidad', corregir_ortografia=True)
print(f"\nTexto original:  '{resultado['texto_original']}'")
print(f"Texto corregido: '{resultado['texto_corregido']}'")
print(f"\nAnimaciones generadas: {resultado['total_animaciones']}")
print(f"Palabras deletreadas: {resultado['palabras_deletreadas']}")
print(f"\nSecuencia de animaciones:")
for i, anim in enumerate(resultado['animaciones'][:10], 1):
    print(f"  {i}. {anim['nombre'].upper()}")
if len(resultado['animaciones']) > 10:
    print(f"  ... y {len(resultado['animaciones']) - 10} más")
