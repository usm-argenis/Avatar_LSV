#!/usr/bin/env python3
"""
Corrige TODOS los archivos problemáticos de Duvall automáticamente
Elimina el Node 0 (RootNode) y Node 1 (Armature) problemáticos
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

def corregir_estructura(gltf):
    """
    Elimina RootNode y Armature, deja Hips como raíz
    Reindexea todos los nodos y actualiza referencias
    """
    nodes = gltf.get('nodes', [])
    
    if len(nodes) < 3:
        return False, "No hay suficientes nodos"
    
    # Verificar que sea la estructura problemática
    if nodes[0].get('name') != 'RootNode' or nodes[1].get('name') != 'Armature':
        return False, "No es la estructura problemática"
    
    # Eliminar Node 0 y Node 1
    nuevos_nodes = nodes[2:]  # Empezar desde Hips (Node 2)
    
    # Actualizar índices de children en todos los nodos
    for node in nuevos_nodes:
        if 'children' in node:
            # Restar 2 a cada índice de child
            node['children'] = [child_idx - 2 for child_idx in node['children']]
    
    # Actualizar scenes para apuntar al nuevo root (Hips, que ahora es índice 0)
    if 'scenes' in gltf:
        for scene in gltf['scenes']:
            if 'nodes' in scene:
                scene['nodes'] = [0]  # Hips es ahora el nodo 0
    
    # Actualizar skins
    if 'skins' in gltf:
        for skin in gltf['skins']:
            if 'skeleton' in skin:
                # Restar 2 al skeleton root
                skin['skeleton'] = skin['skeleton'] - 2
            if 'joints' in skin:
                # Restar 2 a cada joint
                skin['joints'] = [joint_idx - 2 for joint_idx in skin['joints']]
    
    # Actualizar animations
    if 'animations' in gltf:
        for animation in gltf['animations']:
            if 'channels' in animation:
                for channel in animation['channels']:
                    if 'target' in channel and 'node' in channel['target']:
                        # Restar 2 al target node
                        channel['target']['node'] = channel['target']['node'] - 2
    
    gltf['nodes'] = nuevos_nodes
    
    return True, f"Eliminados RootNode y Armature, {len(nuevos_nodes)} nodos restantes"

def procesar_archivo(ruta):
    """Procesa un archivo individual"""
    try:
        gltf, bin_data, version = leer_glb(ruta)
        
        corregido, mensaje = corregir_estructura(gltf)
        
        if corregido:
            # Backup
            backup = ruta.with_suffix('.glb.backup_original')
            if not backup.exists():
                shutil.copy2(ruta, backup)
            
            # Escribir corregido
            escribir_glb(ruta, gltf, bin_data, version)
            return True, mensaje
        else:
            return False, mensaje
    except Exception as e:
        return False, f"Error: {e}"

if __name__ == "__main__":
    # Leer lista de archivos problemáticos
    with open('archivos_problematicos.txt', 'r', encoding='utf-8') as f:
        archivos = [Path(line.strip()) for line in f if line.strip()]
    
    print(f"\n{'='*80}")
    print(f"🔧 CORRECCIÓN MASIVA DE ARCHIVOS DUVALL")
    print(f"{'='*80}\n")
    print(f"Archivos a procesar: {len(archivos)}\n")
    
    exitos = 0
    errores = 0
    
    for archivo in archivos:
        print(f"📂 {archivo.name}...", end=' ')
        
        corregido, mensaje = procesar_archivo(archivo)
        
        if corregido:
            print(f"✅ {mensaje}")
            exitos += 1
        else:
            print(f"❌ {mensaje}")
            errores += 1
    
    print(f"\n{'='*80}")
    print(f"📊 RESUMEN")
    print(f"{'='*80}")
    print(f"   ✅ Corregidos: {exitos}")
    print(f"   ❌ Errores: {errores}")
    print(f"   📊 Total: {len(archivos)}")
    print(f"\n{'='*80}\n")
