#!/usr/bin/env python3
"""
Corrige ESPECÍFICAMENTE el archivo agarrar.glb
"""
import json
import struct
from pathlib import Path
import shutil

def leer_glb(ruta_glb):
    with open(ruta_glb, 'rb') as f:
        magic = f.read(4)
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        chunk_length = struct.unpack('<I', f.read(4))[0]
        chunk_type = f.read(4)
        json_data = f.read(chunk_length).decode('utf-8')
        gltf = json.loads(json_data)
        
        bin_data = None
        try:
            bin_chunk_length = struct.unpack('<I', f.read(4))[0]
            bin_chunk_type = f.read(4)
            if bin_chunk_type == b'BIN\x00':
                bin_data = f.read(bin_chunk_length)
        except:
            pass
        
        return gltf, bin_data, version

def escribir_glb(ruta_glb, gltf, bin_data, version=2):
    json_data = json.dumps(gltf, separators=(',', ':')).encode('utf-8')
    json_padding = (4 - (len(json_data) % 4)) % 4
    json_data += b' ' * json_padding
    
    total_length = 12 + 8 + len(json_data)
    if bin_data:
        bin_padding = (4 - (len(bin_data) % 4)) % 4
        bin_data_padded = bin_data + b'\x00' * bin_padding
        total_length += 8 + len(bin_data_padded)
    
    with open(ruta_glb, 'wb') as f:
        f.write(b'glTF')
        f.write(struct.pack('<I', version))
        f.write(struct.pack('<I', total_length))
        
        f.write(struct.pack('<I', len(json_data)))
        f.write(b'JSON')
        f.write(json_data)
        
        if bin_data:
            f.write(struct.pack('<I', len(bin_data_padded)))
            f.write(b'BIN\x00')
            f.write(bin_data_padded)

archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")

print(f"\n{'='*80}")
print("CORRECCIÓN FINAL DE AGARRAR.GLB")
print(f"{'='*80}\n")

# Backup
backup = archivo.with_suffix('.glb.backup_FINAL')
shutil.copy2(archivo, backup)
print(f"💾 Backup creado: {backup.name}\n")

# Leer
gltf, bin_data, version = leer_glb(archivo)

print(f"ANTES:")
print(f"  Nodos: {len(gltf['nodes'])}")
print(f"  Node 0: {gltf['nodes'][0].get('name')}")
print(f"  Node 1: {gltf['nodes'][1].get('name')}")

# Eliminar Node 0 y 1
nuevos_nodes = gltf['nodes'][2:]

# Actualizar children
for node in nuevos_nodes:
    if 'children' in node:
        node['children'] = [c - 2 for c in node['children']]

# Actualizar scenes
if 'scenes' in gltf:
    for scene in gltf['scenes']:
        if 'nodes' in scene:
            scene['nodes'] = [0]

# Actualizar skins
if 'skins' in gltf:
    for skin in gltf['skins']:
        if 'skeleton' in skin:
            skin['skeleton'] = skin['skeleton'] - 2
        if 'joints' in skin:
            skin['joints'] = [j - 2 for j in skin['joints']]

# Actualizar animations
if 'animations' in gltf:
    for animation in gltf['animations']:
        if 'channels' in animation:
            for channel in animation['channels']:
                if 'target' in channel and 'node' in channel['target']:
                    channel['target']['node'] = channel['target']['node'] - 2

gltf['nodes'] = nuevos_nodes

print(f"\nDESPUÉS:")
print(f"  Nodos: {len(gltf['nodes'])}")
print(f"  Node 0: {gltf['nodes'][0].get('name')}")
print(f"  Node 1: {gltf['nodes'][1].get('name')}")

# Escribir
escribir_glb(archivo, gltf, bin_data, version)

print(f"\n✅ ARCHIVO CORREGIDO")
print(f"\n{'='*80}\n")
