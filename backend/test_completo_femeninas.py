"""Test completo de palabras femeninas vs carreras"""

from api_optimizer import LSVOptimizer

optimizer = LSVOptimizer()

print("\n" + "="*70)
print("PRUEBAS: PERSONAS FEMENINAS vs CARRERAS")
print("="*70)

casos = [
    # Profesiones (personas)
    ("maestro", "MAESTRO"),
    ("maestra", "MAESTRO + MUJER"),
    ("ingeniero", "INGENIERO"),
    ("ingeniera", "INGENIERO + MUJER"),
    
    # Carreras (NO agregan MUJER)
    ("ingenieria", "INGENIERO"),
    ("enfermeria", "ENFERMERIA"),
    ("informatica", "INFORMATICA"),
    
    # Familia
    ("hermano", "HERMANO"),
    ("hermana", "HERMANO + MUJER"),
    ("padre", "PADRE"),
    ("madre", "PADRE + MUJER"),
    
    # Personas
    ("anciano", "ANCIANO"),
    ("anciana", "ANCIANO + MUJER"),
    ("niño", "NIÑO"),
    ("niña", "NIÑO + MUJER"),
    
    # Frases completas
    ("yo estudio ingenieria", "YO → ESTUDIAR → INGENIERO"),
    ("mi hermana es ingeniera", "MIO → HERMANO → MUJER → SER → INGENIERO → MUJER"),
]

for texto, esperado in casos:
    resultado = optimizer.translate_to_animations(
        texto=texto,
        deletrear_desconocidas=False,
        corregir_ortografia=True
    )
    
    secuencia = ' → '.join([a['nombre'].upper() for a in resultado['animaciones']])
    
    correcto = "✅" if secuencia == esperado else "❌"
    
    print(f"\n{correcto} '{texto}'")
    print(f"   Esperado: {esperado}")
    print(f"   Obtenido: {secuencia}")

print("\n" + "="*70 + "\n")
