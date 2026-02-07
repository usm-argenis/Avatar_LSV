"""Ver todas las palabras del diccionario por categoría"""
from api_optimizer import LSVOptimizer
import json

opt = LSVOptimizer()

# Agrupar por categoría
categorias = {}
for palabra, info in opt.diccionario.items():
    cat = info.get('categoria', 'sin_categoria')
    if cat not in categorias:
        categorias[cat] = []
    categorias[cat].append(palabra)

print("=" * 70)
print("DICCIONARIO LSV COMPLETO POR CATEGORÍAS")
print("=" * 70)

for cat in sorted(categorias.keys()):
    print(f"\n📂 {cat.upper()} ({len(categorias[cat])} palabras)")
    print("   " + ", ".join(sorted(categorias[cat])))

# Buscar verbos que puedan servir como base
print("\n" + "=" * 70)
print("🔍 VERBOS DISPONIBLES:")
print("=" * 70)
if 'verbos' in categorias:
    for v in sorted(categorias['verbos']):
        print(f"   ✅ {v}")
