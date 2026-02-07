import json

with open('scripts/data.json', encoding='utf-8') as f:
    data = json.load(f)

palabras = ['año', 'ano', 'mañana', 'manana', 'niño', 'nino']

print("Verificando palabras en diccionario:")
for p in palabras:
    existe = p in data
    print(f"  '{p}': {existe}")
