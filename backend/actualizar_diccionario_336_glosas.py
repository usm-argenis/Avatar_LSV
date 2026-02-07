"""
Actualizar data.json con las 336 glosas de glosas_duvall_completas.txt
"""

import json
from pathlib import Path

# Leer diccionario actual
data_path = Path(__file__).parent / 'scripts' / 'data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print(f"📚 Diccionario actual: {len(diccionario)} palabras")

# Palabras de las 336 glosas que faltan en el diccionario
palabras_faltantes = {
    # NUEVO (33 glosas) - categoría 'familia'
    'hermano': {'categoria': 'familia', 'archivo': 'hermano'},
    'hijo': {'categoria': 'familia', 'archivo': 'hijo'},
    'madre': {'categoria': 'familia', 'archivo': 'madre'},
    'madrina': {'categoria': 'familia', 'archivo': 'madrina'},
    'mama': {'categoria': 'familia', 'archivo': 'mama'},
    'nieto': {'categoria': 'familia', 'archivo': 'nieto'},
    'padre': {'categoria': 'familia', 'archivo': 'padre'},
    'padrino': {'categoria': 'familia', 'archivo': 'padrino'},
    'papa': {'categoria': 'familia', 'archivo': 'papa'},
    'primo': {'categoria': 'familia', 'archivo': 'primo'},
    'sobrino': {'categoria': 'familia', 'archivo': 'sobrino'},
    'suegro': {'categoria': 'familia', 'archivo': 'suegro'},
    'tio': {'categoria': 'familia', 'archivo': 'tio'},
    'abuelo': {'categoria': 'familia', 'archivo': 'abuelo'},
    'cuñado': {'categoria': 'familia', 'archivo': 'cunado'},  # sin tilde para archivo
    
    # Otras de NUEVO
    'familia': {'categoria': 'familia', 'archivo': 'familia'},
    'nombre': {'categoria': 'general', 'archivo': 'nombre'},
    'seña': {'categoria': 'general', 'archivo': 'sena'},  # sin tilde
    
    # Verbos que pueden faltar
    'correr': {'categoria': 'verbos', 'archivo': 'correr'},
    'dividir': {'categoria': 'verbos', 'archivo': 'dividir'},
    'entrar': {'categoria': 'verbos', 'archivo': 'entrar'},
    'fumar': {'categoria': 'verbos', 'archivo': 'fumar'},
    'multiplicar': {'categoria': 'verbos', 'archivo': 'multiplicar'},
    'permitir': {'categoria': 'verbos', 'archivo': 'permitir'},
    'prohibir': {'categoria': 'verbos', 'archivo': 'prohibir'},
    'respetar': {'categoria': 'verbos', 'archivo': 'respetar'},
    'restar': {'categoria': 'verbos', 'archivo': 'restar'},
    'sumar': {'categoria': 'verbos', 'archivo': 'sumar'},
    'viajar': {'categoria': 'verbos', 'archivo': 'viajar'},
    'crear': {'categoria': 'verbos', 'archivo': 'crear'},
    'evaluar': {'categoria': 'verbos', 'archivo': 'evaluar'},
    
    # Expresiones temporales
    'antes': {'categoria': 'tiempo', 'archivo': 'antes'},
    'hace rato': {'categoria': 'tiempo', 'archivo': 'hace_rato'},
}

# Agregar palabras faltantes
palabras_agregadas = []
for palabra, info in palabras_faltantes.items():
    if palabra not in diccionario:
        diccionario[palabra] = info
        palabras_agregadas.append(palabra)
        print(f"✅ Agregada: {palabra}")

# Guardar diccionario actualizado
with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, ensure_ascii=False, indent=2)

print(f"\n📊 RESUMEN:")
print(f"   Total en diccionario: {len(diccionario)} palabras")
print(f"   Palabras agregadas: {len(palabras_agregadas)}")
print(f"   Guardado en: {data_path}")

if palabras_agregadas:
    print(f"\n🆕 NUEVAS PALABRAS:")
    for p in sorted(palabras_agregadas):
        print(f"   • {p}")
