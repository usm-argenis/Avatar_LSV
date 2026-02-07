"""
Prueba final con frase real de defensa
"""

from api_optimizer import LSVOptimizer

optimizer = LSVOptimizer()

# Frase típica de defensa de tesis
texto = "Hoy presento la defensa de mi trabajo de grado sobre un aporte tecnológico para la integración de la comunidad sorda venezolana"

print("=" * 80)
print("🎓 PRUEBA FINAL: FRASE REAL DE DEFENSA DE TESIS")
print("=" * 80)
print()
print(f"📝 Español:")
print(f'   "{texto}"')
print()

resultado = optimizer.translate_to_animations(
    texto,
    deletrear_desconocidas=True,
    corregir_ortografia=True
)

# Extraer glosas
glosas = [anim['nombre'].upper() for anim in resultado['animaciones'] if not anim.get('es_deletreo', False)]

print(f"🤟 LSV (Glosas):")
print(f"   {' '.join(glosas)}")
print()

# Análisis
print("📊 ANÁLISIS DEL RESULTADO:")
print()

# Tiempo
tiempo_palabras = ['HOY']
tiempo_encontradas = [g for g in glosas if g in tiempo_palabras]
if tiempo_encontradas:
    print(f"✅ TIEMPO al inicio: {' '.join(tiempo_encontradas)}")

# Lugar
lugar_palabras = ['UNIVERSIDAD', 'VENEZUELA', 'CERCA', 'LEJOS', 'CASA']
lugar_encontradas = [g for g in glosas if g in lugar_palabras]
if lugar_encontradas:
    print(f"✅ LUGAR después de tiempo: {' '.join(lugar_encontradas)}")

# Verbos
verbos = ['PRESENTAR', 'TRABAJAR', 'INTEGRAR', 'PRESENTAR']
verbos_encontrados = [g for g in glosas if g in verbos]
if verbos_encontrados:
    print(f"✅ VERBOS: {', '.join(set(verbos_encontrados))}")

# Reformulaciones
if resultado.get('correcciones'):
    print(f"\n📝 Correcciones aplicadas: {len(resultado['correcciones'])}")

# Deletreadas
if resultado.get('palabras_deletreadas'):
    print(f"\n🔡 Palabras deletreadas: {', '.join(resultado['palabras_deletreadas'])}")
else:
    print(f"\n✅ No se necesitó deletrear ninguna palabra")

print()
print(f"📈 Total de animaciones: {resultado['total_animaciones']}")
print()
print("=" * 80)
print("✅ SISTEMA LISTO PARA DEFENSA DE TESIS")
print("=" * 80)
