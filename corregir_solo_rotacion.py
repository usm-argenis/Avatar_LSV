#!/usr/bin/env python3
"""
Corrige SOLO la rotación del Armature, manteniendo la escala 100x
"""
import json
import struct
from pathlib import Path
import shutil

def leer_glb(ruta_glb):
    """Lee un archivo GLB"""
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
    """Escribe un archivo GLB"""
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

def corregir_solo_rotacion(gltf):
    """Corrige SOLO la rotación del Armature, mantiene la escala"""
    cambios = []
    
    nodes = gltf.get('nodes', [])
    
    if len(nodes) > 1:
        node = nodes[1]
        nombre = node.get('name', 'Node_1')
        
        print(f"\n🔍 Node 1 ({nombre}):")
        print(f"   Rotación: {node.get('rotation')}")
        print(f"   Escala: {node.get('scale')}")
        
        # SOLO eliminar rotación, mantener escala
        if 'rotation' in node:
            old_rot = node['rotation']
            node['rotation'] = [0.0, 0.0, 0.0, 1.0]
            cambios.append(f"✓ Rotación eliminada")
            print(f"   ✅ Nueva rotación: [0, 0, 0, 1]")
        
        # MANTENER escala 100x (no modificar)
        print(f"   ✅ Escala mantenida: {node.get('scale')}")
    
    return cambios

if __name__ == "__main__":
    archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")
    
    print(f"\n{'='*70}")
    print(f"🔧 CORRECCIÓN DE ROTACIÓN ÚNICAMENTE")
    print(f"{'='*70}\n")
    
    if not archivo.exists():
        print(f"❌ Archivo no encontrado")
        exit(1)
    
    # Backup
    backup = archivo.with_suffix('.glb.backup_final')
    shutil.copy2(archivo, backup)
    print(f"💾 Backup: {backup.name}\n")
    
    # Leer
    gltf, bin_data, version = leer_glb(archivo)
    
    # Corregir
    cambios = corregir_solo_rotacion(gltf)
    
    if cambios:
        # Escribir
        escribir_glb(archivo, gltf, bin_data, version)
        print(f"\n✅ Archivo corregido y guardado")
        print(f"\n{'='*70}\n")
    else:
        print("\n⚠️ No hay cambios")
