#!/usr/bin/env python3
"""
Agregar 'proyecto' al diccionario LSV
"""

import json
from pathlib import Path

# Ruta al diccionario
DICT_PATH = Path(__file__).parent / "backend" / "scripts" / "data.json"

def agregar_proyecto():
    """Agregar la palabra 'proyecto' al diccionario"""
    
    # Leer diccionario actual
    with open(DICT_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"📖 Diccionario actual: {len(data)} palabras\n")
    
    # Verificar si ya existe
    if 'proyecto' in data:
        print("⚠️ 'proyecto' ya existe en el diccionario")
        print(f"   Categoría: {data['proyecto']['categoria']}")
        print(f"   Archivo: {data['proyecto']['archivo']}")
        return
    
    # Agregar nueva palabra
    palabra_nueva = {
        "proyecto": {
            "categoria": "general",
            "archivo": "proyecto"
        }
    }
    
    data.update(palabra_nueva)
    
    # Ordenar alfabéticamente (mantener números al inicio)
    numeros = {k: v for k, v in data.items() if k[0].isdigit()}
    palabras = {k: v for k, v in data.items() if not k[0].isdigit()}
    palabras_ordenadas = dict(sorted(palabras.items()))
    
    data_ordenada = {**numeros, **palabras_ordenadas}
    
    # Guardar
    with open(DICT_PATH, 'w', encoding='utf-8') as f:
        json.dump(data_ordenada, f, indent=2, ensure_ascii=False)
    
    print("✅ Palabra agregada:")
    print("   • proyecto → proyecto.glb (categoría: general)")
    print(f"\n📊 Total palabras: {len(data_ordenada)}")

if __name__ == "__main__":
    agregar_proyecto()
