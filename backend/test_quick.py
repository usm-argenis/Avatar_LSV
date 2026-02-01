from api_optimizer import LSVOptimizer

opt = LSVOptimizer()
r = opt.translate_to_animations('yo estudio ingenieria', corregir_ortografia=True)
print(f"\nSecuencia: {' → '.join([a['nombre'].upper() for a in r['animaciones']])}")
print(f"Total: {r['total_animaciones']} animaciones\n")
