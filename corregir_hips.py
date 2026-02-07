#!/usr/bin/env python3
"""
Corrige el Node 2 (Hips) para compensar la rotación de 92° en X
Aplica una rotación compensatoria de -90° al Hips
"""
import json
import struct
from pathlib import Path
import shutil
import math

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

def multiplicar_quaternions(q1, q2):
    """Multiplica dos quaternions [x, y, z, w]"""
    x1, y1, z1, w1 = q1
    x2, y2, z2, w2 = q2
    
    w = w1*w2 - x1*x2 - y1*y2 - z1*z2
    x = w1*x2 + x1*w2 + y1*z2 - z1*y2
    y = w1*y2 - x1*z2 + y1*w2 + z1*x2
    z = w1*z2 + x1*y2 - y1*x2 + z1*w2
    
    return [x, y, z, w]

def corregir_hips(gltf):
    """Aplica rotación compensatoria de -90° en X al Node 2 (Hips)"""
    cambios = []
    nodes = gltf.get('nodes', [])
    
    if len(nodes) > 2:
        node = nodes[2]
        nombre = node.get('name', 'Node_2')
        
        print(f"\n🔍 Node 2 ({nombre}):")
        print(f"   Rotación actual: {node.get('rotation')}")
        
        if 'rotation' in node:
            # Rotación actual del Hips (aprox 92° en X)
            rot_actual = node['rotation']
            
            # Rotación compensatoria: -90° en X = [sin(-45°), 0, 0, cos(-45°)]
            # -90° en radianes = -π/2, entonces sin(-π/4) = -0.7071, cos(-π/4) = 0.7071
            rot_compensacion = [-0.7071068, 0, 0, 0.7071068]
            
            # Multiplicar quaternions: nueva_rot = rot_compensacion * rot_actual
            nueva_rot = multiplicar_quaternions(rot_compensacion, rot_actual)
            
            node['rotation'] = nueva_rot
            cambios.append(f"✓ Hips rotado -90° en X")
            print(f"   ✅ Nueva rotación: {nueva_rot}")
        else:
            print(f"   ⚠️ No tiene rotación")
    
    return cambios

if __name__ == "__main__":
    archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")
    
    print(f"\n{'='*70}")
    print(f"🔧 CORRECCIÓN DE HIPS (Node 2)")
    print(f"{'='*70}\n")
    
    if not archivo.exists():
        print(f"❌ Archivo no encontrado")
        exit(1)
    
    # Backup
    backup = archivo.with_suffix('.glb.backup_hips')
    shutil.copy2(archivo, backup)
    print(f"💾 Backup: {backup.name}\n")
    
    # Leer
    gltf, bin_data, version = leer_glb(archivo)
    
    # Corregir
    cambios = corregir_hips(gltf)
    
    if cambios:
        # Escribir
        escribir_glb(archivo, gltf, bin_data, version)
        print(f"\n✅ Archivo corregido")
        print(f"\n{'='*70}\n")
    else:
        print("\n⚠️ No hay cambios")
