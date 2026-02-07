#!/usr/bin/env python3
"""
Corrección completa de agarrar.glb
Reorganiza los nodos para que los meshes estén primero, como en los otros archivos
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
print("CORRECCIÓN COMPLETA DE AGARRAR.GLB - REORGANIZACIÓN DE NODOS")
print(f"{'='*80}\n")

# Backup
backup = archivo.with_suffix('.glb.backup_REORG')
shutil.copy2(archivo, backup)
print(f"💾 Backup creado: {backup.name}\n")

# Leer
gltf, bin_data, version = leer_glb(archivo)

print("ANTES:")
print(f"  Total nodos: {len(gltf['nodes'])}")
print(f"  Scene nodes: {gltf['scenes'][0]['nodes']}")
print(f"  Node 0: {gltf['nodes'][0].get('name')} (tipo: {'mesh' if 'mesh' in gltf['nodes'][0] else 'bone'})")
print(f"  Skins: {len(gltf.get('skins', []))}")

# Separar nodos en dos grupos: meshes y bones
mesh_nodes = []
bone_nodes = []
mesh_node_indices = {}  # mapa de índice viejo -> nuevo
bone_node_indices = {}  # mapa de índice viejo -> nuevo

for i, node in enumerate(gltf['nodes']):
    if 'mesh' in node:
        mesh_node_indices[i] = len(mesh_nodes)
        mesh_nodes.append(node.copy())
    else:
        bone_node_indices[i] = len(bone_nodes)
        bone_nodes.append(node.copy())

# Nuevo orden: primero meshes, luego bones
nuevos_nodes = mesh_nodes + bone_nodes

# Crear mapa completo de reindexación
index_map = {}
index_map.update(mesh_node_indices)
for old_idx, new_bone_idx in bone_node_indices.items():
    index_map[old_idx] = len(mesh_nodes) + new_bone_idx

# Actualizar children en todos los nodos
for node in nuevos_nodes:
    if 'children' in node:
        node['children'] = [index_map[c] for c in node['children']]

# Actualizar scenes para apuntar al último mesh (como en amar.glb)
# En amar, la escena apunta al nodo 88, que es el último nodo
if 'scenes' in gltf:
    for scene in gltf['scenes']:
        scene['nodes'] = [len(nuevos_nodes) - 1]

# Actualizar skins
if 'skins' in gltf:
    for skin in gltf['skins']:
        if 'skeleton' in skin:
            skin['skeleton'] = index_map[skin['skeleton']]
        if 'joints' in skin:
            skin['joints'] = [index_map[j] for j in skin['joints']]

# Consolidar skins en uno solo (como en los archivos correctos)
if 'skins' in gltf and len(gltf['skins']) > 1:
    # Tomar el primer skin como base
    gltf['skins'] = [gltf['skins'][0]]
    # Eliminar la referencia al skeleton
    if 'skeleton' in gltf['skins'][0]:
        del gltf['skins'][0]['skeleton']

# Actualizar meshes (skin index)
if 'meshes' in gltf:
    for mesh in gltf['meshes']:
        for primitive in mesh['primitives']:
            if 'attributes' in primitive and 'JOINTS_0' in primitive['attributes']:
                # Asegurarse de que use el skin 0
                pass  # Ya debería estar en 0

# Actualizar animations
if 'animations' in gltf:
    for animation in gltf['animations']:
        if 'channels' in animation:
            for channel in animation['channels']:
                if 'target' in channel and 'node' in channel['target']:
                    old_node = channel['target']['node']
                    channel['target']['node'] = index_map[old_node]

# Actualizar referencias de skin en nodos de mesh
for i, node in enumerate(nuevos_nodes):
    if 'skin' in node:
        # Todos usan skin 0
        node['skin'] = 0

gltf['nodes'] = nuevos_nodes

print(f"\nDESPUÉS:")
print(f"  Total nodos: {len(gltf['nodes'])}")
print(f"  Scene nodes: {gltf['scenes'][0]['nodes']}")
print(f"  Node 0: {gltf['nodes'][0].get('name')} (tipo: {'mesh' if 'mesh' in gltf['nodes'][0] else 'bone'})")
print(f"  Skins: {len(gltf.get('skins', []))}")
print(f"  Primeros 5 nodos:")
for i in range(min(5, len(gltf['nodes']))):
    node = gltf['nodes'][i]
    tipo = 'mesh' if 'mesh' in node else 'bone'
    print(f"    {i}: {node.get('name')} ({tipo})")

# Escribir
escribir_glb(archivo, gltf, bin_data, version)

print(f"\n✅ ARCHIVO REORGANIZADO Y CORREGIDO")
print(f"\n{'='*80}\n")
