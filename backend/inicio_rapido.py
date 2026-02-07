"""
🚀 INICIO RÁPIDO - Sistema de Traducción LSV
===============================================

Guía de 5 minutos para empezar a usar tu nuevo sistema
"""

print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║  🤟 SISTEMA DE TRADUCCIÓN CONCEPTUAL LSV - INICIO RÁPIDO            ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

✅ IMPLEMENTACIÓN COMPLETADA

Tu API ahora traduce por CONCEPTO, no palabra por palabra.
Todas las reglas anteriores (deletreo, números, género) siguen funcionando.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 OPCIÓN 1: PRUEBA INTERACTIVA (RECOMENDADO)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Ejecuta:
   
   python traductor_interactivo.py
   
   Luego escribe frases como:
   • "Hoy presento mi trabajo de grado"
   • "La integración de la comunidad sorda es importante"
   • "Ayer la ingeniera trabajó en su proyecto"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 OPCIÓN 2: INICIAR API (PARA FRONTEND/APP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Ejecuta:
   
   python main.py
   
   La API estará en: http://localhost:5000
   Documentación en: http://localhost:5000/docs
   
   Endpoint: POST /api/translate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 OPCIÓN 3: EJECUTAR PRUEBAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Ver todos los casos de prueba:
   
   python test_traduccion_conceptual.py
   
   Prueba con frase real de defensa:
   
   python prueba_defensa_final.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 OPCIÓN 4: USAR DESDE TU CÓDIGO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Python:
   
   from api_optimizer import LSVOptimizer
   
   optimizer = LSVOptimizer()
   resultado = optimizer.translate_to_animations("Tu frase aquí")
   
   glosas = [a['nombre'].upper() for a in resultado['animaciones']]
   print(' '.join(glosas))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 DOCUMENTACIÓN COMPLETA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   📄 README_SISTEMA_LISTO.md      → Resumen ejecutivo
   📄 TRADUCCION_CONCEPTUAL_LSV.md → Guía completa
   📄 IMPLEMENTACION_COMPLETADA.md → Detalles técnicos

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 EJEMPLO RÁPIDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Entrada:
   "Hoy presento la defensa de mi trabajo de grado"
   
   Salida LSV:
   HOY PRESENTAR DEFENSA MIO TRABAJAR GRADO
   
   ✅ TIEMPO al inicio (HOY)
   ✅ Verbos a infinitivo (presento → PRESENTAR)
   ✅ Omisión de artículos (la, de, mi → MIO)
   ✅ Sin deletreo innecesario

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 NUEVAS CAPACIDADES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   ✅ Reformulación conceptual (85+ mapeos)
   ✅ Verbos base para construcción
   ✅ Orden LSV: TIEMPO → LUGAR → SUJETO → VERBO
   ✅ Deletreo solo como último recurso
   ✅ Todas las reglas anteriores intactas

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎓 LISTO PARA TU DEFENSA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Tu sistema puede traducir frases académicas complejas manteniendo
   la estructura natural de la Lengua de Señas Venezolana.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

¿Qué quieres hacer primero?

[1] 🎮 Probar traducción interactiva
[2] 🚀 Iniciar API
[3] 🧪 Ver pruebas
[4] 📚 Leer documentación

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

import sys

try:
    opcion = input("Elige opción (1-4) o 'q' para salir: ").strip()
    
    if opcion == '1':
        print("\n🎮 Iniciando traductor interactivo...\n")
        import traductor_interactivo
        traductor_interactivo.main()
    
    elif opcion == '2':
        print("\n🚀 Iniciando API...\n")
        import os
        os.system("python main.py")
    
    elif opcion == '3':
        print("\n🧪 Ejecutando pruebas...\n")
        import os
        os.system("python test_traduccion_conceptual.py")
    
    elif opcion == '4':
        print("""
📚 DOCUMENTACIÓN DISPONIBLE:

1. README_SISTEMA_LISTO.md
   → Resumen ejecutivo y ejemplos

2. TRADUCCION_CONCEPTUAL_LSV.md
   → Guía completa de todas las reglas

3. IMPLEMENTACION_COMPLETADA.md
   → Detalles técnicos de la implementación

Abre cualquiera de estos archivos en tu editor.
        """)
    
    elif opcion.lower() in ['q', 'quit', 'salir']:
        print("\n👋 ¡Hasta luego!\n")
        sys.exit(0)
    
    else:
        print("\n⚠️ Opción no válida. Por favor elige 1, 2, 3, 4 o 'q'\n")

except KeyboardInterrupt:
    print("\n\n👋 ¡Hasta luego!\n")
    sys.exit(0)
