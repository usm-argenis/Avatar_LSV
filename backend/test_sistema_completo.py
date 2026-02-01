"""Test del sistema completo con palabras variadas"""

from api_optimizer import LSVOptimizer

optimizer = LSVOptimizer()

print("\n" + "="*70)
print("🧪 TEST COMPLETO DEL SISTEMA LSV")
print("="*70)

casos_prueba = [
    "carrera",
    "carreras",
    "ingeniero",
    "ingeniera",
    "ingenieria",
    "maestros",
    "maestras",
    "hermanos",
    "padres",
    "madres",
    "niños",
    "ancianas",
    "casas",
    "coches",
    "hospitales",
    "yo estudio ingenieria en sistemas",
    "mi hermana es maestra",
    "los niños juegan",
    "las maestras enseñan",
]

for texto in casos_prueba:
    resultado = optimizer.translate_to_animations(
        texto=texto,
        deletrear_desconocidas=False,
        corregir_ortografia=True
    )
    
    secuencia = ' → '.join([a['nombre'].upper() for a in resultado['animaciones']])
    
    print(f"\n📝 '{texto}'")
    if resultado['correcciones']:
        for corr in resultado['correcciones']:
            print(f"   🔧 {corr['original']} → {corr['corregida']} ({corr['tipo']})")
    print(f"   ✅ {secuencia}")

print("\n" + "="*70 + "\n")
