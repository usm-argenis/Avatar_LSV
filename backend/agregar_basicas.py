"""
Agregar palabras básicas que faltan en el diccionario LSV
"""
import json
from pathlib import Path

DICT_PATH = Path(__file__).parent / 'scripts' / 'data.json'

with open(DICT_PATH, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print(f"📚 Diccionario actual: {len(diccionario)} palabras\n")

# Palabras básicas que DEBEN estar
palabras_basicas = {
    'año': {'categoria': 'tiempo', 'archivo': 'año'},
    'años': {'categoria': 'tiempo', 'archivo': 'año'},
    'tener': {'categoria': 'verbos', 'archivo': 'tener'},
    'tengo': {'categoria': 'verbos', 'archivo': 'tener'},
    'tienes': {'categoria': 'verbos', 'archivo': 'tener'},
    'tiene': {'categoria': 'verbos', 'archivo': 'tener'},
    'nombre': {'categoria': 'general', 'archivo': 'nombre'},
    'llamar': {'categoria': 'verbos', 'archivo': 'llamar'},
    'llamo': {'categoria': 'verbos', 'archivo': 'llamar'},
    'edad': {'categoria': 'general', 'archivo': 'edad'},
}

agregadas = 0
for palabra, info in palabras_basicas.items():
    if palabra not in diccionario:
        diccionario[palabra] = info
        print(f"✅ Agregada: {palabra} → {info['archivo']}")
        agregadas += 1
    else:
        print(f"⏭️  Ya existe: {palabra}")

print(f"\n{'='*80}")
print(f"📊 Total agregadas: {agregadas}")
print(f"📚 Total en diccionario: {len(diccionario)} palabras")
print(f"{'='*80}\n")

with open(DICT_PATH, 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, ensure_ascii=False, indent=2)

print(f"💾 Guardado en: {DICT_PATH}")
