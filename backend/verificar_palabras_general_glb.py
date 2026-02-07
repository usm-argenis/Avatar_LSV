"""
Verificar qué palabras de categoría 'general' tienen archivos GLB y cuáles NO
"""

import json
from pathlib import Path

# Leer data.json
data_path = Path(__file__).parent / 'scripts' / 'data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

# Filtrar palabras de categoría 'general'
palabras_general = {palabra: info for palabra, info in diccionario.items() 
                     if info.get('categoria') == 'general'}

print(f"Palabras con categoría 'general': {len(palabras_general)}")
print()

# Verificar si existen archivos GLB
test_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall")

print("VERIFICANDO ARCHIVOS GLB:")
print("=" * 80)

con_glb = []
sin_glb = []

for palabra in sorted(palabras_general.keys()):
    archivo = palabra
    
    # Buscar en diferentes carpetas posibles
    rutas_posibles = [
        test_path / 'horario' / f'Duvall_resultado_{archivo}.glb',
        test_path / 'nuevo' / f'Duvall_resultado_{archivo}.glb',
        test_path / 'general' / f'Duvall_resultado_{archivo}.glb',
    ]
    
    existe = False
    ubicacion = None
    for ruta in rutas_posibles:
        if ruta.exists():
            existe = True
            ubicacion = ruta.parent.name
            break
    
    if existe:
        con_glb.append(palabra)
        print(f"   OK {palabra:30s} -> {ubicacion}")
    else:
        sin_glb.append(palabra)
        print(f"   FALTA {palabra:30s}")

print()
print("=" * 80)
print(f"CON archivo GLB: {len(con_glb)} palabras")
for p in con_glb:
    print(f"   - {p}")

print()
print(f"SIN archivo GLB: {len(sin_glb)} palabras")
for p in sin_glb:
    print(f"   - {p}")

print()
print("=" * 80)
print("RECOMENDACIÓN:")
if sin_glb:
    print(f"   {len(sin_glb)} palabras de categoría 'general' NO tienen archivos GLB")
    print("   Opciones:")
    print("   1. Eliminarlas de data.json para que se deletreen")
    print("   2. Generar los archivos GLB faltantes")
else:
    print("   Todas las palabras 'general' tienen archivos GLB!")
