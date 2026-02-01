"""Test de corrección de typos específicos"""

from api_optimizer import LSVOptimizer

optimizer = LSVOptimizer()

# Casos de prueba
casos = [
    "ingenieria",  # Debe corregir a "ingeniera"
    "ingeniero de sistemas",
    "maestro e ingeniera"
]

for texto in casos:
    print(f"\n{'='*60}")
    print(f"📝 TEXTO: '{texto}'")
    print('='*60)
    
    resultado = optimizer.translate_to_animations(
        texto=texto,
        deletrear_desconocidas=True,
        corregir_ortografia=True
    )
    
    print(f"✅ Corregido: '{resultado['texto_corregido']}'")
    
    if resultado['correcciones']:
        print("\n🔧 Correcciones:")
        for corr in resultado['correcciones']:
            print(f"   • {corr['original']} → {corr['corregida']} ({corr['confianza']}%)")
    
    print(f"\n🎬 Secuencia ({resultado['total_animaciones']} animaciones):")
    secuencia = ' → '.join([a['nombre'].upper() for a in resultado['animaciones']])
    print(f"   {secuencia}")
    
    if resultado['palabras_deletreadas']:
        print(f"\n⚠️ Deletreadas: {', '.join(resultado['palabras_deletreadas'])}")

print(f"\n{'='*60}\n")
