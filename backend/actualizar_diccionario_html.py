#!/usr/bin/env python3
"""
Script para actualizar el diccionario en animation_mobile.html
"""
import json
import re
from pathlib import Path

# Leer diccionario desde data.json
data_path = Path(__file__).parent / 'scripts' / 'data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

# Convertir diccionario a formato JavaScript
js_dict_lines = []
for palabra, info in diccionario.items():
    # Escapar comillas en la palabra si es necesario
    palabra_escaped = palabra.replace("'", "\\'")
    js_dict_lines.append(f"            '{palabra_escaped}': {{ categoria: '{info['categoria']}', archivo: '{info['archivo']}' }}")

js_dict_content = ',\n'.join(js_dict_lines)

# Leer animation_mobile.html
html_path = Path(__file__).parent.parent / 'test' / 'animation_mobile.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Buscar y reemplazar el diccionario
pattern = r'const DICCIONARIO = \{[^}]*(?:\{[^}]*\}[^}]*)*\};'

new_dict = f'''const DICCIONARIO = {{
            // 📌 Generado automáticamente desde backend/scripts/data.json ({len(diccionario)} palabras)
{js_dict_content}
        }};'''

# Reemplazar
html_content_updated = re.sub(pattern, new_dict, html_content, flags=re.DOTALL)

# Guardar
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content_updated)

print(f'✅ Diccionario actualizado en animation_mobile.html!')
print(f'📊 Total de palabras: {len(diccionario)}')
print(f'📁 Archivo: {html_path}')
