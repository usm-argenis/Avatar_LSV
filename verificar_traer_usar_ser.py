#!/usr/bin/env python3
"""
Verificar y procesar traer, usar y ser de Duvall
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

base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos")
archivos = ["traer", "usar", "ser"]

print(f"\n{'='*80}")
print("VERIFICANDO ARCHIVOS DUVALL")
print(f"{'='*80}\n")

necesitan_proceso = []

for nombre in archivos:
    archivo_path = base_dir / f"Duvall_resultado_{nombre}.glb"
    
    if not archivo_path.exists():
        print(f"⚠️  No existe: {archivo_path.name}")
        continue
    
    gltf = leer_glb(archivo_path)
    
    print(f"📄 {archivo_path.name}")
    print(f"   Total nodos: {len(gltf['nodes'])}")
    print(f"   Node 0: {gltf['nodes'][0].get('name', 'N/A')}")
    
    # Buscar Armature
    for i, node in enumerate(gltf['nodes']):
        if node.get('name') == 'Armature':
            rotation = node.get('rotation', [0, 0, 0, 1])
            scale = node.get('scale', [1, 1, 1])
            
            print(f"   Armature Node: {i}")
            print(f"   Armature Rotation: {rotation}")
            print(f"   Armature Scale: {scale}")
            
            # Verificar si necesita procesamiento
            if (gltf['nodes'][0].get('name') == 'RootNode' or 
                rotation != [0, 0, 0, 1] or 
                scale != [1, 1, 1]):
                print(f"   ❌ NECESITA PROCESAMIENTO")
                necesitan_proceso.append(nombre)
            else:
                print(f"   ✅ YA ESTÁ CORRECTO")
            break
    print()

if necesitan_proceso:
    print(f"\n{'='*80}")
    print(f"Archivos que necesitan procesamiento: {len(necesitan_proceso)}")
    for n in necesitan_proceso:
        print(f"  - {n}")
    
    # Guardar lista para Blender
    with open(r"C:\Users\andre\OneDrive\Documentos\tesis\archivos_procesar_blender.txt", 'w') as f:
        for n in necesitan_proceso:
            f.write(f"{n}\n")
    
    print(f"\nLista guardada en: archivos_procesar_blender.txt")
else:
    print(f"\n✅ Todos los archivos ya están correctos")

print(f"\n{'='*80}\n")
