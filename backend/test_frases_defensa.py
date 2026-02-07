"""
Test de frases para defensa de TEG con API LSV corregida
"""

from api_optimizer import LSVOptimizer

# Inicializar optimizador
optimizer = LSVOptimizer()

print("=" * 90)
print("🧪 TEST: FRASES DE DEFENSA DE TEG")
print("=" * 90)
print()

# Frases de prueba
frases_prueba = [
    "Bienvenidos a la defensa de nuestro TEG",
    "Este proyecto ayuda a personas sordas",
    "Nuestro sistema usa computadora",
    "La tecnología mejora la comunicación",
    "Buscamos la integración de la comunidad sorda"
]

for i, frase in enumerate(frases_prueba, 1):
    print(f"{'='*90}")
    print(f"FRASE {i}")
    print(f"{'='*90}")
    print(f"📝 Español: {frase}")
    print()
    
    # Traducir
    resultado = optimizer.translate_to_animations(
        frase,
        deletrear_desconocidas=True,
        corregir_ortografia=True
    )
    
    print(f"✅ Glosa LSV: {resultado['glosa_lsv']}")
    print()
    
    # Mostrar animaciones
    print("🎬 Secuencia de animaciones:")
    for j, anim in enumerate(resultado['animaciones'], 1):
        prefijo = "🔤" if anim.get('es_deletreo') else "✋"
        nombre = anim['nombre'].upper()
        categoria = anim['categoria']
        print(f"   {j:2d}. {prefijo} {nombre:20s} [{categoria}]")
    
    print(f"\n📊 Total: {resultado['total_animaciones']} animaciones")
    
    # Mostrar observaciones si las hay
    if resultado['observaciones_linguisticas']:
        print("\n💡 Observaciones:")
        for obs in resultado['observaciones_linguisticas']:
            print(f"   • {obs}")
    
    # Mostrar palabras deletreadas
    if resultado['palabras_deletreadas']:
        print("\n🔤 Palabras deletreadas:")
        for palabra in resultado['palabras_deletreadas']:
            print(f"   • {palabra}")
    
    print()

print("=" * 90)
print("✅ TEST COMPLETADO")
print("=" * 90)
print()

# Resumen
print("📋 RESUMEN DE TRADUCCIONES:")
print("=" * 90)
for i, frase in enumerate(frases_prueba, 1):
    resultado = optimizer.translate_to_animations(frase, deletrear_desconocidas=True)
    print(f"{i}. {frase}")
    print(f"   → {resultado['glosa_lsv']}")
    print()
