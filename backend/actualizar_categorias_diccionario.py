"""
Actualizar categorías del diccionario para que coincidan con las carpetas reales
"""
import json
from pathlib import Path

# Cargar diccionario
data_path = Path('C:/Users/andre/OneDrive/Documentos/tesis/backend/scripts/data.json')
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print("🔄 Actualizando categorías del diccionario...")

# Días de la semana: tiempo → dias_semana
dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
for dia in dias_semana:
    if dia in diccionario and diccionario[dia]['categoria'] == 'tiempo':
        diccionario[dia]['categoria'] = 'dias_semana'
        print(f"  ✅ {dia}: tiempo → dias_semana")

# Guardar diccionario actualizado
with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, ensure_ascii=False, indent=2)

print("\n✅ Diccionario actualizado correctamente")
