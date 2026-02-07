"""
Test específico de frase proporcionada por el usuario
"""
from api_optimizer import LSVOptimizer

optimizer = LSVOptimizer()

frase = "Este proyecto busca crear un sistema de traducción de lengua de señas venezolana que facilite la comunicación entre personas sordas y oyentes en la universidad."

print("="*80)
print("TRADUCCIÓN A LSV")
print("="*80)
print(f"\n📥 FRASE ORIGINAL:")
print(f"   \"{frase}\"")
print("\n" + "-"*80 + "\n")

resultado = optimizer.translate_to_animations(frase)

print(f"🎯 GLOSA LSV:")
print(f"   {resultado['glosa_lsv']}")

if resultado['correcciones']:
    print(f"\n✏️  Correcciones ortográficas:")
    for corr in resultado['correcciones']:
        print(f"   • '{corr['original']}' → '{corr['corregida']}'")

if resultado['observaciones_linguisticas']:
    print(f"\n📚 Observaciones LSV:")
    for obs in resultado['observaciones_linguisticas']:
        print(f"   • {obs}")

if resultado['palabras_deletreadas']:
    print(f"\n🔤 Deletreadas (sin seña): {', '.join(resultado['palabras_deletreadas'])}")

print(f"\n📋 Secuencia completa ({resultado['total_animaciones']} señas):")
secuencia = []
for anim in resultado['animaciones']:
    if anim.get('es_deletreo'):
        if anim['nombre'] == 'deletrear':
            continue  # no mostrar el marcador
        secuencia.append(f"[{anim['nombre'].upper()}]")
    else:
        secuencia.append(anim['nombre'].upper())

print(f"   {' → '.join(secuencia)}")

print("\n" + "="*80)
