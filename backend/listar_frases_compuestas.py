import json

# Cargar diccionario
with open('scripts/data.json', encoding='utf-8') as f:
    data = json.load(f)

# Encontrar todas las frases compuestas (con espacios)
frases = [k for k in data.keys() if ' ' in k]
frases.sort()

print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print(f'📚 FRASES COMPUESTAS EN EL DICCIONARIO LSV')
print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print(f'Total: {len(frases)} frases\n')

# Agrupar por número de palabras
frases_2_palabras = [f for f in frases if len(f.split()) == 2]
frases_3_palabras = [f for f in frases if len(f.split()) == 3]
frases_4_palabras = [f for f in frases if len(f.split()) == 4]

print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print(f'📝 FRASES DE 2 PALABRAS ({len(frases_2_palabras)}):')
print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
for f in frases_2_palabras:
    categoria = data[f]['categoria']
    print(f'  ✓ "{f}" - {categoria}')

if frases_3_palabras:
    print(f'\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'📝 FRASES DE 3 PALABRAS ({len(frases_3_palabras)}):')
    print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    for f in frases_3_palabras:
        categoria = data[f]['categoria']
        print(f'  ✓ "{f}" - {categoria}')

if frases_4_palabras:
    print(f'\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'📝 FRASES DE 4+ PALABRAS ({len(frases_4_palabras)}):')
    print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    for f in frases_4_palabras:
        categoria = data[f]['categoria']
        print(f'  ✓ "{f}" - {categoria}')

print(f'\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print(f'📊 RESUMEN:')
print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print(f'  • 2 palabras: {len(frases_2_palabras)}')
print(f'  • 3 palabras: {len(frases_3_palabras)}')
print(f'  • 4+ palabras: {len(frases_4_palabras)}')
print(f'  • TOTAL: {len(frases)}')
print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
