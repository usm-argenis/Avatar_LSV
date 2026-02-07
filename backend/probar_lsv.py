"""
Probador interactivo de LSV
Escribe cualquier frase y verás la traducción exacta a LSV
"""

from api_optimizer import LSVOptimizer

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║  🎯 PROBADOR DE TRADUCCIÓN LSV                                              ║
║  Escribe tus frases y ve la traducción exacta a Lengua de Señas Venezolana ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")

optimizer = LSVOptimizer()
print(f"✅ Sistema cargado: {len(optimizer.diccionario)} palabras en diccionario\n")

print("💡 EJEMPLOS PARA PROBAR:")
print("   • yo tengo 18 años")
print("   • mi nombre es José")
print("   • hola buenos días")
print("   • mañana voy a la universidad")
print("   • no entiendo")
print("\n" + "="*80 + "\n")

while True:
    try:
        # Leer entrada
        texto = input("📝 Escribe tu frase (o 'salir' para terminar): ").strip()
        
        if texto.lower() in ['salir', 'exit', 'quit', 'q']:
            print("\n👋 ¡Hasta luego!")
            break
        
        if not texto:
            continue
        
        # Traducir
        print(f"\n{'─'*80}")
        resultado = optimizer.translate_to_animations(
            texto,
            deletrear_desconocidas=True,
            velocidad_deletreo=1.2,
            corregir_ortografia=True
        )
        
        # Mostrar resultado principal
        print(f"🎯 GLOSA LSV: {resultado['glosa_lsv']}")
        
        # Mostrar correcciones si las hay
        if resultado['correcciones']:
            print(f"\n✏️  Correcciones:")
            for corr in resultado['correcciones']:
                print(f"   • '{corr['original']}' → '{corr['corregida']}'")
        
        # Mostrar observaciones
        if resultado['observaciones_linguisticas']:
            print(f"\n📚 Observaciones:")
            for obs in resultado['observaciones_linguisticas']:
                print(f"   • {obs}")
        
        # Mostrar deletreos
        if resultado['palabras_deletreadas']:
            print(f"\n🔤 Palabras deletreadas: {', '.join(resultado['palabras_deletreadas'])}")
        
        # Mostrar secuencia detallada
        print(f"\n📋 Secuencia de señas ({resultado['total_animaciones']} total):")
        secuencia = []
        for anim in resultado['animaciones']:
            if anim.get('es_deletreo'):
                secuencia.append(f"[{anim['nombre'].upper()}]")
            else:
                secuencia.append(anim['nombre'].upper())
        print(f"   {' → '.join(secuencia)}")
        
        print(f"{'─'*80}\n")
        
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
        break
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        continue
