from api_optimizer import LSVOptimizer

opt = LSVOptimizer()

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("🧪 TEST: Normalización de acentos")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

# Casos de prueba con acentos
tests = [
    "hola cómo estás",
    "buenos días",
    "buenas tardes mucho gusto",
    "año mañana niño",
    "médico ingeniero",
    "vídeo canción"
]

for texto in tests:
    print(f"📝 Entrada: '{texto}'")
    resultado = opt.translate_to_animations(texto, corregir_ortografia=True)
    
    print(f"   → Corregido: '{resultado['texto_corregido']}'")
    print(f"   → Animaciones: {len(resultado['animaciones'])}")
    
    # Mostrar secuencia
    secuencia = ' → '.join([anim['nombre'].upper() for anim in resultado['animaciones']])
    print(f"   → Secuencia: {secuencia}")
    
    # Mostrar correcciones
    if resultado['correcciones']:
        for corr in resultado['correcciones']:
            print(f"   ✏️ '{corr['original']}' → '{corr['corregida']}'")
    
    print()

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("✅ TODAS las frases deben funcionar igual CON o SIN acentos")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
