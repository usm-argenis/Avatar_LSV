"""
Agregar más palabras básicas que faltan
"""
import json
from pathlib import Path

DICT_PATH = Path(__file__).parent / 'scripts' / 'data.json'

with open(DICT_PATH, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print(f"📚 Diccionario actual: {len(diccionario)} palabras\n")

# Más palabras básicas
palabras_nuevas = {
    'ir': {'categoria': 'verbos', 'archivo': 'ir'},
    'voy': {'categoria': 'verbos', 'archivo': 'ir'},
    'vas': {'categoria': 'verbos', 'archivo': 'ir'},
    'va': {'categoria': 'verbos', 'archivo': 'ir'},
    'vamos': {'categoria': 'verbos', 'archivo': 'ir'},
    'van': {'categoria': 'verbos', 'archivo': 'ir'},
    
    'entender': {'categoria': 'verbos', 'archivo': 'entender'},
    'entiendo': {'categoria': 'verbos', 'archivo': 'entender'},
    'entiendes': {'categoria': 'verbos', 'archivo': 'entender'},
    'entiende': {'categoria': 'verbos', 'archivo': 'entender'},
    
    'ser': {'categoria': 'verbos', 'archivo': 'ser'},
    'soy': {'categoria': 'verbos', 'archivo': 'ser'},
    'eres': {'categoria': 'verbos', 'archivo': 'ser'},
}

agregadas = 0
for palabra, info in palabras_nuevas.items():
    if palabra not in diccionario:
        diccionario[palabra] = info
        print(f"✅ Agregada: {palabra} → {info['archivo']}")
        agregadas += 1
    else:
        print(f"⏭️  Ya existe: {palabra}")

print(f"\n📊 Total agregadas: {agregadas}")
print(f"📚 Total en diccionario: {len(diccionario)} palabras\n")

with open(DICT_PATH, 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, ensure_ascii=False, indent=2)

print(f"💾 Guardado")
