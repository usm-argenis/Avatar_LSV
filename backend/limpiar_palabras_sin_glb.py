"""
Eliminar palabras de data.json que NO tienen archivos GLB generados
Esto permite que el sistema las deletree automáticamente
"""

import json
from pathlib import Path

# Palabras que NO tienen archivos GLB y causan error 404
palabras_sin_glb = [
    'tecnologia', 'tecnologico', 'teg', 'defensa', 'proyecto',
    'computadora', 'computadoras', 'objetivo', 'grado', 'jurado',
    'presentacion', 'traduccion', 'traducir', 'lsv', 'universidad',
    'comunidad', 'aporte', 'evaluar', 'miembro', 'miembros',
    'especial', 'importante', 'social', 'junto', 'edad',
    'venezuela', 'venezolano', 'trabajo', 'año', 'años',
    # Verbos extras sin GLB
    'buscar', 'busca', 'buscamos', 'buscan', 'buscas',
    'integrar', 'integracion', 'mejorar', 'mejora', 'mejor',
    'entender', 'entiende', 'entiendes', 'entiendo',
    'facilitar', 'facilita', 'facilitamos', 'facilitan', 'facilitas', 'facilite',
    'crear', 'llamar', 'llamo', 'participar', 'existir'
]

# Leer data.json
data_path = Path(__file__).parent / 'scripts' / 'data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

print(f"Diccionario original: {len(diccionario)} palabras")
print()

# Crear copia de respaldo
backup_path = data_path.parent / 'data_backup_con_palabras_sin_glb.json'
with open(backup_path, 'w', encoding='utf-8') as f:
    json.dump(diccionario, f, indent=2, ensure_ascii=False)
print(f"Respaldo guardado en: {backup_path}")
print()

# Eliminar palabras sin GLB
palabras_eliminadas = []
diccionario_limpio = {}

for palabra, info in diccionario.items():
    if palabra in palabras_sin_glb:
        palabras_eliminadas.append(palabra)
        print(f"Eliminando: {palabra:30s} (categoria: {info['categoria']})")
    else:
        diccionario_limpio[palabra] = info

print()
print(f"Palabras eliminadas: {len(palabras_eliminadas)}")
print(f"Diccionario limpio: {len(diccionario_limpio)} palabras")
print()

# Guardar diccionario limpio
with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(diccionario_limpio, f, indent=2, ensure_ascii=False)

print("data.json actualizado!")
print()
print("RESULTADO:")
print(f"   Antes: {len(diccionario)} palabras")
print(f"   Ahora: {len(diccionario_limpio)} palabras")
print(f"   Eliminadas: {len(palabras_eliminadas)} palabras sin archivos GLB")
print()
print("Ahora estas palabras se deletrearan automáticamente con el alfabeto.")
