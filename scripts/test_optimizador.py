"""
Script de prueba rápida del optimizador LSV
"""

import sys
from pathlib import Path

# Agregar backend al path
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from lsv_optimizer import LSVTextOptimizer

# Crear optimizador
optimizer = LSVTextOptimizer()

# Casos de prueba
casos = [
    "¿cual es tu nombre?",
    "ola como estas",
    "k haces mañana",
    "buenos dias",
    "cual es tu edad",
]

print("=" * 70)
print("PRUEBA DEL OPTIMIZADOR LSV")
print("=" * 70)

for caso in casos:
    print(f"\n📝 Texto Original:")
    print(f"   {caso}")
    
    resultado = optimizer.procesar_texto(caso)
    
    print(f"✅ Texto Corregido:")
    print(f"   {resultado['texto_corregido']}")
    
    print(f"🔄 Orden LSV:")
    print(f"   {resultado['texto_lsv']}")
    
    print(f"📊 Cobertura: {resultado['porcentaje_cobertura']:.1f}%")

print("\n" + "=" * 70)
