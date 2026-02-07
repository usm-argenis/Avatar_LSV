"""
Script para probar optimización de género MUJER
Verifica que:
- "policia" → POLICIA (SIN mujer, porque ya existe)
- "profesora" → PROFESOR MUJER (CON mujer, porque no existe "profesora")
"""
import sys
import os

# Agregar el directorio backend al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from api_optimizer import LSVOptimizer

print("="*80)
print("PRUEBA: Optimización de Género MUJER")
print("="*80)

optimizer = LSVOptimizer()

# Casos de prueba
casos = [
    {
        'texto': 'policia',
        'esperado': 'Solo POLICIA (sin MUJER porque ya existe en diccionario)',
        'debe_tener_mujer': False
    },
    {
        'texto': 'profesora',
        'esperado': 'PROFESOR + MUJER (con MUJER porque no existe "profesora")',
        'debe_tener_mujer': True
    },
    {
        'texto': 'ingeniera',
        'esperado': 'INGENIERO + MUJER (con MUJER porque no existe "ingeniera")',
        'debe_tener_mujer': True
    },
    {
        'texto': 'doctor',
        'esperado': 'DOCTOR (sin MUJER porque es masculino)',
        'debe_tener_mujer': False
    }
]

for i, caso in enumerate(casos, 1):
    print(f"\n{'='*80}")
    print(f"CASO {i}: '{caso['texto']}'")
    print(f"Esperado: {caso['esperado']}")
    print(f"{'='*80}")
    
    resultado = optimizer.translate_to_animations(
        caso['texto'],
        deletrear_desconocidas=False,
        corregir_ortografia=False
    )
    
    # Verificar animaciones
    animaciones = resultado['animaciones']
    nombres_animaciones = [anim['nombre'] for anim in animaciones]
    tiene_mujer = 'mujer' in nombres_animaciones
    
    print(f"Animaciones generadas: {' → '.join([n.upper() for n in nombres_animaciones])}")
    print(f"¿Tiene MUJER?: {tiene_mujer}")
    
    # Verificar si cumple expectativa
    if tiene_mujer == caso['debe_tener_mujer']:
        print("✅ CORRECTO")
    else:
        print("❌ INCORRECTO")
        if caso['debe_tener_mujer']:
            print("   Debería tener MUJER pero no lo tiene")
        else:
            print("   NO debería tener MUJER pero lo tiene")

print(f"\n{'='*80}")
print("Prueba completada")
print(f"{'='*80}")
