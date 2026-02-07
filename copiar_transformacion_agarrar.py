#!/usr/bin/env python3
"""
Copia las transformaciones del Armature de agarrar a otros archivos
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
        json_bytes = f.read(chunk_length)
        json_data = json_bytes.decode('utf-8')
        
        # Leer chunk binario si existe
        binary_data = None
        if f.tell() < length:
            bin_chunk_length = struct.unpack('<I', f.read(4))[0]
            bin_chunk_type = f.read(4)
            binary_data = f.read(bin_chunk_length)
        
        return json.loads(json_data), binary_data

def escribir_glb(ruta_glb, gltf, binary_data):
    with open(ruta_glb, 'wb') as f:
        # Header
        f.write(b'glTF')
        f.write(struct.pack('<I', 2))  # version
        
        # Calcular tamaño total después
        json_str = json.dumps(gltf, separators=(',', ':'))
        json_bytes = json_str.encode('utf-8')
        
        # Padding JSON a múltiplo de 4
        json_padding = (4 - len(json_bytes) % 4) % 4
        json_bytes += b' ' * json_padding
        
        total_length = 12 + 8 + len(json_bytes)  # header + json chunk header + json
        if binary_data:
            bin_padding = (4 - len(binary_data) % 4) % 4
            total_length += 8 + len(binary_data) + bin_padding
        
        f.write(struct.pack('<I', total_length))
        
        # JSON chunk
        f.write(struct.pack('<I', len(json_bytes)))
        f.write(b'JSON')
        f.write(json_bytes)
        
        # Binary chunk
        if binary_data:
            bin_data_padded = binary_data + b'\x00' * bin_padding
            f.write(struct.pack('<I', len(bin_data_padded)))
            f.write(b'BIN\x00')
            f.write(bin_data_padded)

# Archivos a procesar en Carla/verbo_c
archivos_destino = [
    "sufrir", "traer", "usar", "atraer", "burlar", "enganar", 
    "guardar", "llevar", "pelear", "regalar", "ser", "vestir",
    "calmar", "verbo"
]

# Leer transformación de agarrar
ruta_agarrar = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Carla\verbo_c\Carla_resultado_agarrar.glb")
print(f"📖 Leyendo transformaciones de: {ruta_agarrar.name}")

gltf_agarrar, _ = leer_glb(ruta_agarrar)

# Buscar el nodo Armature en agarrar
armature_transform = None
for i, node in enumerate(gltf_agarrar['nodes']):
    if node.get('name') == 'Armature':
        armature_transform = {
            'rotation': node.get('rotation', [0, 0, 0, 1]),
            'scale': node.get('scale', [1, 1, 1]),
            'translation': node.get('translation', [0, 0, 0])
        }
        print(f"\n✅ Transformación encontrada en agarrar:")
        print(f"   Rotation: {armature_transform['rotation']}")
        print(f"   Scale: {armature_transform['scale']}")
        print(f"   Translation: {armature_transform['translation']}")
        break

if not armature_transform:
    print("❌ ERROR: No se encontró Armature en agarrar")
    exit(1)

# Aplicar a cada archivo destino
base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Carla\verbo_c")

print(f"\n{'='*80}")
print("APLICANDO TRANSFORMACIONES")
print(f"{'='*80}\n")

procesados = 0
for nombre_archivo in archivos_destino:
    ruta_glb = base_dir / f"Carla_resultado_{nombre_archivo}.glb"
    
    if not ruta_glb.exists():
        print(f"⚠️  No existe: {ruta_glb.name}")
        continue
    
    # Crear backup
    backup_path = ruta_glb.with_suffix('.glb.backup_TRANSFORM')
    if not backup_path.exists():
        shutil.copy2(ruta_glb, backup_path)
    
    # Leer archivo destino
    gltf_destino, binary_destino = leer_glb(ruta_glb)
    
    # Buscar y modificar Armature
    modificado = False
    for i, node in enumerate(gltf_destino['nodes']):
        if node.get('name') == 'Armature':
            # Aplicar transformaciones de agarrar
            node['rotation'] = armature_transform['rotation'].copy()
            node['scale'] = armature_transform['scale'].copy()
            node['translation'] = armature_transform['translation'].copy()
            modificado = True
            break
    
    if modificado:
        # Guardar archivo modificado
        escribir_glb(ruta_glb, gltf_destino, binary_destino)
        print(f"✅ {ruta_glb.name}")
        procesados += 1
    else:
        print(f"⚠️  No se encontró Armature en: {ruta_glb.name}")

print(f"\n{'='*80}")
print(f"✅ Procesados: {procesados} archivos")
print(f"{'='*80}\n")
