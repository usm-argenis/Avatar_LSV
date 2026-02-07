#!/usr/bin/env python3
"""
Corrige el Node 1 (Armature) del archivo agarrar.glb
Elimina la rotación -90° y normaliza la escala a 1x
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

def corregir_armature_node(gltf):
    """Corrige el Node 1 (Armature) eliminando rotación y normalizando escala"""
    cambios = []
    
    nodes = gltf.get('nodes', [])
    
    # Node 1 debe ser Armature
    if len(nodes) > 1:
        node = nodes[1]
        nombre = node.get('name', 'Node_1')
        
        print(f"\n🔍 Analizando {nombre}:")
        print(f"   Rotación actual: {node.get('rotation')}")
        print(f"   Escala actual: {node.get('scale')}")
        
        # Eliminar rotación problemática
        if 'rotation' in node:
            old_rot = node['rotation']
            # Cambiar a rotación identidad (sin rotación)
            node['rotation'] = [0.0, 0.0, 0.0, 1.0]
            cambios.append(f"✓ Rotación eliminada: {old_rot} → [0, 0, 0, 1]")
        
        # Normalizar escala
        if 'scale' in node:
            old_scale = node['scale']
            # Cambiar a escala 1x
            node['scale'] = [1.0, 1.0, 1.0]
            cambios.append(f"✓ Escala normalizada: {old_scale} → [1, 1, 1]")
    
    return cambios

if __name__ == "__main__":
    archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")
    
    print(f"\n{'='*70}")
    print(f"🔧 CORRECCIÓN DE ARMATURE - {archivo.name}")
    print(f"{'='*70}\n")
    
    if not archivo.exists():
        print(f"❌ Archivo no encontrado: {archivo}")
        exit(1)
    
    # Backup
    backup = archivo.with_suffix('.glb.backup_armature')
    shutil.copy2(archivo, backup)
    print(f"💾 Backup creado: {backup.name}\n")
    
    # Leer GLB
    print("📂 Leyendo archivo...")
    gltf, bin_data, version = leer_glb(archivo)
    
    # Corregir
    print("\n🔧 Aplicando correcciones al Node 1 (Armature)...")
    cambios = corregir_armature_node(gltf)
    
    if cambios:
        print(f"\n✅ Cambios aplicados:")
        for cambio in cambios:
            print(f"   {cambio}")
        
        # Escribir
        print(f"\n💾 Guardando archivo corregido...")
        escribir_glb(archivo, gltf, bin_data, version)
        print(f"✅ Archivo guardado: {archivo.name}")
        
        print(f"\n{'='*70}")
        print("✅ CORRECCIÓN COMPLETADA")
        print(f"{'='*70}\n")
        print("⚠️ IMPORTANTE: Esto puede NO funcionar porque el problema está")
        print("   en el Node 2 (Hips) que tiene rotación de 92° inherente al esqueleto.")
        print("   Si el modelo sigue volteado, la solución correcta es:")
        print("   1. Re-exportar desde Blender con 'Apply Transform'")
        print("   2. O aplicar rotación compensatoria en el viewer JavaScript")
        print(f"\n{'='*70}\n")
    else:
        print("\n⚠️ No se encontraron cambios para aplicar")
