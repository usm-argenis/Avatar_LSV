#!/usr/bin/env python3
"""
Analiza TODOS los archivos GLB de Duvall y determina cuáles funcionan correctamente
Compara estructura y rotaciones para encontrar el patrón correcto
"""
import json
import struct
from pathlib import Path
import math

def leer_glb(ruta_glb):
    with open(ruta_glb, 'rb') as f:
        magic = f.read(4)
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        chunk_length = struct.unpack('<I', f.read(4))[0]
        chunk_type = f.read(4)
        json_data = f.read(chunk_length).decode('utf-8')
        
        return json.loads(json_data)

def analizar_estructura(gltf):
    """Extrae información clave del GLB"""
    nodes = gltf.get('nodes', [])
    
    info = {
        'total_nodes': len(nodes),
        'node0_name': nodes[0].get('name') if len(nodes) > 0 else None,
        'node0_rotation': nodes[0].get('rotation') if len(nodes) > 0 else None,
        'node0_scale': nodes[0].get('scale') if len(nodes) > 0 else None,
        'node1_name': nodes[1].get('name') if len(nodes) > 1 else None,
        'node1_rotation': nodes[1].get('rotation') if len(nodes) > 1 else None,
        'node1_scale': nodes[1].get('scale') if len(nodes) > 1 else None,
        'node2_name': nodes[2].get('name') if len(nodes) > 2 else None,
        'node2_rotation': nodes[2].get('rotation') if len(nodes) > 2 else None,
    }
    
    return info

def categorizar_archivo(info):
    """Determina el tipo de estructura del archivo"""
    if info['node0_name'] == 'RootNode' and info['node1_name'] == 'Armature':
        if info['node1_rotation'] and abs(info['node1_rotation'][0] + 0.707) < 0.01:
            return 'PROBLEMA', 'RootNode+Armature con rotación -90°'
        else:
            return 'OK', 'RootNode+Armature sin rotación problemática'
    elif info['node0_name'] and 'Eye' in str(info['node0_name']):
        return 'OK', 'Estructura directa sin RootNode/Armature'
    else:
        return 'DESCONOCIDO', f"Estructura: {info['node0_name']}, {info['node1_name']}"

if __name__ == "__main__":
    carpeta = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall")
    archivos = list(carpeta.rglob("*.glb"))
    
    # Filtrar backups
    archivos = [f for f in archivos if '.backup' not in f.name]
    
    print(f"\n{'='*80}")
    print(f"📊 ANÁLISIS DE TODOS LOS ARCHIVOS DUVALL ({len(archivos)} archivos)")
    print(f"{'='*80}\n")
    
    problematicos = []
    correctos = []
    desconocidos = []
    
    for archivo in archivos:
        try:
            gltf = leer_glb(archivo)
            info = analizar_estructura(gltf)
            categoria, descripcion = categorizar_archivo(info)
            
            if categoria == 'PROBLEMA':
                problematicos.append((archivo, info, descripcion))
            elif categoria == 'OK':
                correctos.append((archivo, info, descripcion))
            else:
                desconocidos.append((archivo, info, descripcion))
        except Exception as e:
            print(f"❌ Error en {archivo.name}: {e}")
    
    print(f"\n📊 RESUMEN:")
    print(f"   ✅ Correctos: {len(correctos)}")
    print(f"   ⚠️ Problemáticos: {len(problematicos)}")
    print(f"   ❓ Desconocidos: {len(desconocidos)}")
    
    if problematicos:
        print(f"\n⚠️ ARCHIVOS PROBLEMÁTICOS ({len(problematicos)}):")
        for archivo, info, desc in problematicos[:10]:
            print(f"   - {archivo.relative_to(carpeta)}")
            print(f"     {desc}")
    
    if correctos:
        print(f"\n✅ ARCHIVOS CORRECTOS (muestra de 5):")
        for archivo, info, desc in correctos[:5]:
            print(f"   - {archivo.relative_to(carpeta)}")
            print(f"     Nodos: {info['total_nodes']}, Node0: {info['node0_name']}, Node1: {info['node1_name']}")
    
    # Guardar listas para procesamiento
    with open('archivos_problematicos.txt', 'w', encoding='utf-8') as f:
        for archivo, _, _ in problematicos:
            f.write(str(archivo) + '\n')
    
    with open('archivos_correctos.txt', 'w', encoding='utf-8') as f:
        for archivo, _, _ in correctos:
            f.write(str(archivo) + '\n')
    
    print(f"\n💾 Listas guardadas: archivos_problematicos.txt, archivos_correctos.txt")
    print(f"\n{'='*80}\n")
