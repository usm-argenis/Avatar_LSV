"""
Agregar palabras comunes faltantes al diccionario LSV
"""

import json
from pathlib import Path

# Leer diccionario actual
data_path = Path(__file__).parent / 'scripts' / 'data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print(f"📚 Diccionario actual: {len(diccionario)} palabras")

# Palabras faltantes comunes
palabras_nuevas = {
    # Verbos comunes
    'usar': {'categoria': 'verbos', 'archivo': 'usar'},  # Ya debería existir
    'buscar': {'categoria': 'verbos', 'archivo': 'buscar'},
    'buscamos': {'categoria': 'verbos', 'archivo': 'buscar'},  # Variante
    'crear': {'categoria': 'verbos', 'archivo': 'crear'},  # Ya debería existir
    'mejorar': {'categoria': 'verbos', 'archivo': 'mejorar'},
    'mejora': {'categoria': 'verbos', 'archivo': 'mejorar'},  # Variante
    
    # Tecnología
    'computadora': {'categoria': 'tecnologia', 'archivo': 'computadora'},
    'computadoras': {'categoria': 'tecnologia', 'archivo': 'computadora'},
    
    # Adjetivos/estados
    'mejor': {'categoria': 'expresiones', 'archivo': 'mejor'},
    
    # Plurales que deberían normalizar
    'sordas': {'categoria': 'personas', 'archivo': 'sordo'},  # Normalizar a sordo
    'sordos': {'categoria': 'personas', 'archivo': 'sordo'},  # Normalizar a sordo
}

# Agregar palabras que faltan
palabras_agregadas = []
for palabra, info in palabras_nuevas.items():
    if palabra not in diccionario:
        diccionario[palabra] = info
        palabras_agregadas.append(palabra)
        print(f"✅ Agregada: {palabra} → {info['archivo']}")
    else:
        print(f"⚠️  Ya existe: {palabra}")

# Guardar
with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, ensure_ascii=False, indent=2)

print(f"\n📊 RESUMEN:")
print(f"   Total palabras: {len(diccionario)}")
print(f"   Nuevas agregadas: {len(palabras_agregadas)}")
print(f"   Guardado en: {data_path}")

if palabras_agregadas:
    print(f"\n🆕 PALABRAS AGREGADAS:")
    for p in sorted(palabras_agregadas):
        print(f"   • {p}")
