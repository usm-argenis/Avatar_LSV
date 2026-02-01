from api_optimizer import LSVOptimizer

optimizer = LSVOptimizer()

pruebas = [
    "ingenieria",
    "carreras", 
    "sistemas",
    "matematicas"
]

print("\n" + "="*70)
print("🔍 TEST: Verificando que 'nombre' use 'archivo' correcto")
print("="*70)

for texto in pruebas:
    resultado = optimizer.translate_to_animations(
        texto=texto,
        deletrear_desconocidas=False,
        corregir_ortografia=True
    )
    
    if resultado['animaciones']:
        anim = resultado['animaciones'][0]
        print(f"\n📝 '{texto}'")
        print(f"   nombre: {anim['nombre']}")
        print(f"   archivo: {anim['archivo']}")
        print(f"   ✅ {'CORRECTO' if anim['nombre'] == anim['archivo'] else '❌ ERROR'}")

print("\n" + "="*70 + "\n")
