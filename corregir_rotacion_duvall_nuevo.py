#!/usr/bin/env python3
"""
Script para corregir la rotación de archivos GLB en la carpeta Duvall/nuevo
Corrige la rotación del Armature de -90° a 0° en el eje X
"""
import json
import struct
from pathlib import Path
import shutil

def leer_glb(ruta_glb):
    """Lee un archivo GLB y retorna el JSON y los datos binarios"""
    with open(ruta_glb, 'rb') as f:
        # Leer header GLB
        magic = f.read(4)
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        # Leer chunk JSON
        chunk_length = struct.unpack('<I', f.read(4))[0]
        chunk_type = f.read(4)
        json_data = f.read(chunk_length).decode('utf-8')
        gltf = json.loads(json_data)
        
        # Leer chunk BIN (si existe)
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
    """Escribe un archivo GLB corregido"""
    json_data = json.dumps(gltf, separators=(',', ':')).encode('utf-8')
    
    # Padding del JSON a múltiplo de 4
    json_padding = (4 - (len(json_data) % 4)) % 4
    json_data += b' ' * json_padding
    
    # Calcular tamaño total
    total_length = 12 + 8 + len(json_data)  # header + json chunk header + json
    if bin_data:
        bin_padding = (4 - (len(bin_data) % 4)) % 4
        bin_data_padded = bin_data + b'\x00' * bin_padding
        total_length += 8 + len(bin_data_padded)  # bin chunk header + bin
    
    with open(ruta_glb, 'wb') as f:
        # Header GLB
        f.write(b'glTF')
        f.write(struct.pack('<I', version))
        f.write(struct.pack('<I', total_length))
        
        # Chunk JSON
        f.write(struct.pack('<I', len(json_data)))
        f.write(b'JSON')
        f.write(json_data)
        
        # Chunk BIN
        if bin_data:
            f.write(struct.pack('<I', len(bin_data_padded)))
            f.write(b'BIN\x00')
            f.write(bin_data_padded)

def corregir_rotacion(gltf):
    """Corrige la rotación problemática del Armature y meshes, y normaliza la escala"""
    cambios = []
    
    # Buscar nodos con rotación -90° en X
    rotacion_problematica = [-0.7071, 0.0000, 0.0000, 0.7071]
    tolerancia = 0.01
    
    for i, node in enumerate(gltf.get('nodes', [])):
        nombre = node.get('name', f'Node_{i}')
        
        # Corregir rotación problemática
        if 'rotation' in node:
            rot = node['rotation']
            
            # Verificar si es la rotación problemática
            if (abs(rot[0] - rotacion_problematica[0]) < tolerancia and
                abs(rot[1] - rotacion_problematica[1]) < tolerancia and
                abs(rot[2] - rotacion_problematica[2]) < tolerancia and
                abs(rot[3] - rotacion_problematica[3]) < tolerancia):
                
                # Corregir a rotación identidad (sin rotación)
                node['rotation'] = [0.0, 0.0, 0.0, 1.0]
                cambios.append(f"Node {i} ({nombre}): Rotación corregida de -90° a 0°")
        
        # Corregir escala 100x (problema de FBX)
        if 'scale' in node:
            scale = node['scale']
            if abs(scale[0] - 100.0) < 0.1 and abs(scale[1] - 100.0) < 0.1 and abs(scale[2] - 100.0) < 0.1:
                # Normalizar escala a 1x
                node['scale'] = [1.0, 1.0, 1.0]
                cambios.append(f"Node {i} ({nombre}): Escala normalizada de 100x a 1x")
    
    return cambios

def procesar_archivo(ruta_glb, hacer_backup=True):
    """Procesa un archivo GLB y corrige su rotación"""
    print(f"\n{'='*70}")
    print(f"📂 Procesando: {ruta_glb.name}")
    print(f"{'='*70}")
    
    # Hacer backup
    if hacer_backup:
        backup_path = ruta_glb.with_suffix('.glb.backup')
        shutil.copy2(ruta_glb, backup_path)
        print(f"💾 Backup creado: {backup_path.name}")
    
    # Leer GLB
    gltf, bin_data, version = leer_glb(ruta_glb)
    
    # Corregir rotación
    cambios = corregir_rotacion(gltf)
    
    if cambios:
        print(f"\n🔧 Cambios aplicados:")
        for cambio in cambios:
            print(f"   ✓ {cambio}")
        
        # Escribir GLB corregido
        escribir_glb(ruta_glb, gltf, bin_data, version)
        print(f"\n✅ Archivo corregido guardado")
    else:
        print(f"\n⚠️ No se encontraron rotaciones problemáticas")
    
    return len(cambios) > 0

def procesar_carpeta(carpeta, patron="*.glb", hacer_backup=True):
    """Procesa todos los archivos GLB en una carpeta"""
    carpeta = Path(carpeta)
    archivos = list(carpeta.glob(patron))
    
    print(f"\n{'='*70}")
    print(f"📁 Carpeta: {carpeta}")
    print(f"📊 Archivos encontrados: {len(archivos)}")
    print(f"{'='*70}")
    
    procesados = 0
    corregidos = 0
    
    for archivo in archivos:
        try:
            if procesar_archivo(archivo, hacer_backup):
                corregidos += 1
            procesados += 1
        except Exception as e:
            print(f"\n❌ Error procesando {archivo.name}: {e}")
    
    print(f"\n{'='*70}")
    print(f"📊 RESUMEN")
    print(f"{'='*70}")
    print(f"   Archivos procesados: {procesados}")
    print(f"   Archivos corregidos: {corregidos}")
    print(f"   Archivos sin cambios: {procesados - corregidos}")
    print(f"{'='*70}")

# Programa principal
if __name__ == "__main__":
    # Carpeta de Duvall/nuevo
    carpeta_nuevo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\nuevo")
    
    print("""
╔═══════════════════════════════════════════════════════════════╗
║     CORRECTOR DE ROTACIÓN GLB - Duvall/nuevo                 ║
╚═══════════════════════════════════════════════════════════════╝
""")
    
    if carpeta_nuevo.exists():
        confirmar = input(f"⚠️ Se procesarán TODOS los GLB en {carpeta_nuevo}. ¿Continuar? (s/n): ")
        if confirmar.lower() == 's':
            procesar_carpeta(carpeta_nuevo, hacer_backup=True)
        else:
            print("❌ Operación cancelada")
    else:
        print(f"❌ Carpeta no encontrada: {carpeta_nuevo}")
