#!/usr/bin/env python3
"""
Verifica la estructura de múltiples archivos de verbos
"""
import json
import struct
from pathlib import Path

def leer_glb(ruta_glb):
    with open(ruta_glb, 'rb') as f:
        magic = f.read(4)
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        chunk_length = struct.unpack('<I', f.read(4))[0]
        chunk_type = f.read(4)
        json_data = f.read(chunk_length).decode('utf-8')
        
        return json.loads(json_data)

verbos_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos")

# Seleccionar algunos archivos para comparar
archivos = [
    "Duvall_resultado_agarrar.glb",
    "Duvall_resultado_amar.glb",
    "Duvall_resultado_comer.glb",
    "Duvall_resultado_estudiar.glb",
    "Duvall_resultado_saludar.glb"
]

print(f"\n{'='*80}")
print("COMPARACIÓN DE ESTRUCTURA DE NODOS - VERBOS")
print(f"{'='*80}\n")

print(f"{'ARCHIVO':<20} {'NODOS':>8} {'NODE 0':<25} {'NODE 1':<25}")
print(f"{'-'*80}")

for archivo in archivos:
    ruta = verbos_dir / archivo
    if ruta.exists():
        try:
            gltf = leer_glb(ruta)
            nombre = archivo.replace("Duvall_resultado_", "").replace(".glb", "").upper()
            num_nodos = len(gltf['nodes'])
            node0 = gltf['nodes'][0].get('name', 'N/A')
            node1 = gltf['nodes'][1].get('name', 'N/A')
            
            print(f"{nombre:<20} {num_nodos:>8} {node0:<25} {node1:<25}")
        except Exception as e:
            print(f"{archivo:<20} ERROR: {e}")

print(f"\n{'='*80}\n")
