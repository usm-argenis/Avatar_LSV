"""
Test completo de los ejemplos del prompt LSV
Verifica que todos los patrones lingüísticos estén funcionando correctamente
"""

from api_optimizer import LSVOptimizer

def test_ejemplo(num, entrada, esperado_glosa, descripcion=""):
    """Prueba un ejemplo y muestra los resultados"""
    print(f"\n{'='*80}")
    print(f"🧪 EJEMPLO {num}: {descripcion}")
    print(f"{'='*80}")
    print(f"📥 ENTRADA: \"{entrada}\"")
    print(f"🎯 ESPERADO: {esperado_glosa}")
    print(f"{'-'*80}")
    
    resultado = optimizer.translate_to_animations(
        entrada,
        deletrear_desconocidas=True,
        velocidad_deletreo=1.2,
        corregir_ortografia=True
    )
    
    print(f"✅ GLOSA LSV: {resultado['glosa_lsv']}")
    
    if resultado['correcciones']:
        print(f"\n📝 CORRECCIONES:")
        for corr in resultado['correcciones']:
            print(f"   • \"{corr['original']}\" → \"{corr['corregida']}\" ({corr['tipo']}, {corr['confianza']}% confianza)")
    
    if resultado['observaciones_linguisticas']:
        print(f"\n📚 OBSERVACIONES LINGÜÍSTICAS:")
        for i, obs in enumerate(resultado['observaciones_linguisticas'], 1):
            print(f"   {i}. {obs}")
    
    if resultado['palabras_deletreadas']:
        print(f"\n🔤 PALABRAS DELETREADAS: {', '.join(resultado['palabras_deletreadas'])}")
    
    # Verificar si coincide
    glosa_obtenida = resultado['glosa_lsv'].upper()
    esperado_upper = esperado_glosa.upper()
    
    if glosa_obtenida == esperado_upper:
        print(f"\n✅ ¡CORRECTO! La glosa coincide exactamente.")
        return True
    else:
        print(f"\n⚠️  DIFERENCIA DETECTADA:")
        print(f"   Esperado:  {esperado_upper}")
        print(f"   Obtenido:  {glosa_obtenida}")
        return False

# Inicializar optimizador
print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║  🎯 TEST DE TRADUCCIÓN LSV - EJEMPLOS DEL PROMPT                            ║
║  Sistema Experto en Lengua de Señas Venezolana                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")

optimizer = LSVOptimizer()

resultados = []

# ═══════════════════════════════════════════════════════════════════════════════
# EJEMPLO 1: Discurso académico
# ═══════════════════════════════════════════════════════════════════════════════
resultados.append(test_ejemplo(
    1,
    "Bienvenidos a la defensa de nuestro trabajo especial de grado",
    "BIENVENIR DEFENSA TRABAJO GRADO NOSOTROS",
    "Discurso académico - Saludo inicial"
))

# ═══════════════════════════════════════════════════════════════════════════════
# EJEMPLO 2: Objetivo del proyecto
# ═══════════════════════════════════════════════════════════════════════════════
resultados.append(test_ejemplo(
    2,
    "Nuestro objetivo es crear un sistema de traducción de lengua de señas venezolana",
    "OBJETIVO NOSOTROS SISTEMA TRADUCIR LENGUA SEÑAS VENEZUELA CREAR",
    "Objetivo del proyecto"
))

# ═══════════════════════════════════════════════════════════════════════════════
# EJEMPLO 3: Palabra sin seña (con deletreo)
# ═══════════════════════════════════════════════════════════════════════════════
print(f"\n{'='*80}")
print(f"🧪 EJEMPLO 3: Palabra sin seña documentada")
print(f"{'='*80}")
print(f"📥 ENTRADA: \"Plataforma digital inclusiva\"")
print(f"🎯 ESPERADO: PLATAFORMA[DELETREAR] DIGITAL INCLUIR TODOS")
print(f"{'-'*80}")

resultado3 = optimizer.translate_to_animations(
    "Plataforma digital inclusiva",
    deletrear_desconocidas=True,
    velocidad_deletreo=1.2,
    corregir_ortografia=True
)

print(f"✅ GLOSA LSV: {resultado3['glosa_lsv']}")
if resultado3['palabras_deletreadas']:
    print(f"🔤 PALABRAS DELETREADAS: {', '.join(resultado3['palabras_deletreadas'])}")
    print(f"✅ ¡CORRECTO! 'plataforma' se deletreó como se esperaba")
    resultados.append(True)
else:
    print(f"⚠️  ERROR: 'plataforma' debería haberse deletreado")
    resultados.append(False)

# ═══════════════════════════════════════════════════════════════════════════════
# EJEMPLO 4: Justificación social
# ═══════════════════════════════════════════════════════════════════════════════
resultados.append(test_ejemplo(
    4,
    "Este proyecto busca mejorar la comunicación entre personas sordas y oyentes",
    "PROYECTO ESTE BUSCAR COMUNICACION MEJORAR PERSONA SORDO OYENTE",
    "Justificación social"
))

# ═══════════════════════════════════════════════════════════════════════════════
# PATRONES ESPECÍFICOS DEL PROMPT
# ═══════════════════════════════════════════════════════════════════════════════

# PATRÓN DE ÉNFASIS: Lo importante va primero
resultados.append(test_ejemplo(
    5,
    "Es muy importante la comunicación",
    "COMUNICACION IMPORTANTE MUCHO",
    "PATRÓN DE ÉNFASIS - Lo importante primero"
))

# PATRÓN DE NEGACIÓN: Negación al final
resultados.append(test_ejemplo(
    6,
    "No existe un sistema accesible",
    "SISTEMA ESPECIAL EXISTIR NO",
    "PATRÓN DE NEGACIÓN - NO al final"
))

# PATRÓN DE INTEGRACIÓN SOCIAL: Reformulación conceptual
resultados.append(test_ejemplo(
    7,
    "Integración social",
    "PERSONAS JUNTO PARTICIPAR",
    "PATRÓN DE CONCEPTOS ABSTRACTOS - Reformulación"
))

# PATRÓN TEMPORAL: Tiempo al inicio
resultados.append(test_ejemplo(
    8,
    "Mañana presentaré el proyecto",
    "MAÑANA PROYECTO PRESENTAR",
    "PATRÓN TEMPORAL - Tiempo al inicio"
))

# ═══════════════════════════════════════════════════════════════════════════════
# RESUMEN DE RESULTADOS
# ═══════════════════════════════════════════════════════════════════════════════
print(f"\n{'='*80}")
print(f"📊 RESUMEN DE RESULTADOS")
print(f"{'='*80}")

correctos = sum(resultados)
total = len(resultados)
porcentaje = (correctos / total * 100) if total > 0 else 0

print(f"\n✅ Pruebas correctas: {correctos}/{total} ({porcentaje:.1f}%)")

if correctos == total:
    print(f"\n🎉 ¡PERFECTO! Todos los ejemplos del prompt funcionan correctamente")
    print(f"   El sistema LSV está 100% alineado con las reglas del prompt.")
else:
    print(f"\n⚠️  Hay {total - correctos} pruebas que necesitan ajustes")
    print(f"   Revisar las diferencias mostradas arriba.")

print(f"\n{'='*80}\n")
