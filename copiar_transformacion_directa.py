#!/usr/bin/env python3
"""
Copiar transformaciones de Armature directamente en GLB sin Blender
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

# Archivo de referencia
ref_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")
gltf_ref, _ = leer_glb(ref_path)

# Obtener transformación de Armature de agarrar
ref_armature_transform = None
for node in gltf_ref['nodes']:
    if node.get('name') == 'Armature':
        ref_armature_transform = {
            'rotation': node.get('rotation', [0, 0, 0, 1]),
            'scale': node.get('scale', [1, 1, 1]),
            'translation': node.get('translation', [0, 0, 0])
        }
        break

if not ref_armature_transform:
    print("❌ ERROR: No se encontró Armature en agarrar")
    exit(1)

print(f"\n{'='*80}")
print("COPIANDO TRANSFORMACIONES DE ARMATURE DIRECTAMENTE")
print(f"{'='*80}\n")
print(f"Transformación de referencia (agarrar):")
print(f"  Rotation: {ref_armature_transform['rotation']}")
print(f"  Scale: {ref_armature_transform['scale']}")
print(f"  Translation: {ref_armature_transform['translation']}\n")

# Archivos a procesar
archivos = [
    "amar", "ayudar", "cansar", "comer", "conocer",
    "decir", "deletrear", "dormir", "estar", "estudiar", "invitar",
    "preguntar", "presentar", "querer", "responder", "saludar",
    "sentir", "trabajar", "ver", "vivir"
]

base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos")

procesados = 0
ya_correctos = 0

for nombre in archivos:
    archivo_path = base_dir / f"Duvall_resultado_{nombre}.glb"
    
    if not archivo_path.exists():
        print(f"⚠️  No existe: {archivo_path.name}")
        continue
    
    # Leer archivo
    gltf, binary_data = leer_glb(archivo_path)
    
    # Buscar y modificar Armature
    modificado = False
    for node in gltf['nodes']:
        if node.get('name') == 'Armature':
            # Verificar si ya es correcto
            rot_igual = node.get('rotation', [0, 0, 0, 1]) == ref_armature_transform['rotation']
            scale_igual = node.get('scale', [1, 1, 1]) == ref_armature_transform['scale']
            trans_igual = node.get('translation', [0, 0, 0]) == ref_armature_transform['translation']
            
            if rot_igual and scale_igual and trans_igual:
                print(f"✓ {archivo_path.name} - Ya correcto")
                ya_correctos += 1
            else:
                # Crear backup
                backup_path = archivo_path.with_suffix('.glb.backup_DIRECT')
                if not backup_path.exists():
                    shutil.copy2(archivo_path, backup_path)
                
                # Aplicar transformaciones
                node['rotation'] = ref_armature_transform['rotation'].copy()
                node['scale'] = ref_armature_transform['scale'].copy()
                node['translation'] = ref_armature_transform['translation'].copy()
                
                # Guardar
                escribir_glb(archivo_path, gltf, binary_data)
                print(f"✅ {archivo_path.name} - Corregido")
                procesados += 1
                modificado = True
            break
    
    if not modificado and ya_correctos == 0:
        print(f"⚠️  No se encontró Armature en: {archivo_path.name}")

print(f"\n{'='*80}")
print(f"✅ Corregidos: {procesados}")
print(f"✓ Ya correctos: {ya_correctos}")
print(f"{'='*80}\n")
