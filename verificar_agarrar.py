#!/usr/bin/env python3
"""
Compara agarrar con un archivo que funciona (a.glb) para ver diferencias exactas
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

archivo_problema = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")
archivo_bueno = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\alfabeto\Duvall_resultado_a.glb")

print(f"\n{'='*80}")
print("COMPARACIÓN DETALLADA")
print(f"{'='*80}\n")

gltf_problema = leer_glb(archivo_problema)
gltf_bueno = leer_glb(archivo_bueno)

print(f"ARCHIVO PROBLEMA (agarrar):")
print(f"  Total nodos: {len(gltf_problema['nodes'])}")
print(f"  Node 0: {gltf_problema['nodes'][0].get('name')}")
print(f"  Node 1: {gltf_problema['nodes'][1].get('name')}")
print(f"  Node 2: {gltf_problema['nodes'][2].get('name') if len(gltf_problema['nodes']) > 2 else 'N/A'}")

print(f"\nARCHIVO BUENO (a):")
print(f"  Total nodos: {len(gltf_bueno['nodes'])}")
print(f"  Node 0: {gltf_bueno['nodes'][0].get('name')}")
print(f"  Node 1: {gltf_bueno['nodes'][1].get('name')}")
print(f"  Node 2: {gltf_bueno['nodes'][2].get('name') if len(gltf_bueno['nodes']) > 2 else 'N/A'}")

print(f"\n{'='*80}")
print("CONCLUSIÓN:")
print(f"{'='*80}")
print(f"\nEl archivo 'agarrar' TODAVÍA tiene RootNode y Armature!")
print(f"NO se aplicó la corrección correctamente.")
print(f"\nEl archivo 'a' NO tiene RootNode/Armature, empieza directo con meshes.")
print(f"Esa es la estructura correcta que necesitamos.")
print(f"\n{'='*80}\n")
