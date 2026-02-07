"""Verificar palabras en diccionario"""
from api_optimizer import LSVOptimizer

opt = LSVOptimizer()

palabras_buscar = [
    'tecnologia', 'defender', 'importante', 'inclusion', 
    'acceso', 'facil', 'aporte', 'integracion', 'defensa',
    'incluir', 'ayudar', 'usar', 'dar', 'hacer', 'poder',
    'trabajo', 'grado', 'proyecto', 'universidad', 'estudiante',
    'año'
]

print("=" * 50)
print("VERIFICACIÓN DE PALABRAS EN DICCIONARIO")
print("=" * 50)

for p in palabras_buscar:
    existe = "✅" if p in opt.diccionario else "❌"
    print(f"{existe} {p}")

print("\n" + "=" * 50)
print(f"Total palabras en diccionario: {len(opt.diccionario)}")
print("=" * 50)
