#!/usr/bin/env python3
"""
Detectar archivos GLB que necesitan reorganización de nodos
(archivos donde Node 0 es un hueso en lugar de mesh)
"""
import json
import struct
from pathlib import Path

def leer_glb(ruta_glb):
    with open(ruta_glb, 'rb') as f:
        magic = f.read(4)
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        chunk_length = struct.unpack('<I', f.read(4))[0]
        chunk_type = f.read(4)
        json_data = f.read(chunk_length).decode('utf-8')
        
        return json.loads(json_data)

# Buscar en Duvall y Carla
base_dirs = [
    Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall"),
    Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Carla")
]

# Nombres de huesos comunes
nombres_huesos = ['Hips', 'Spine', 'Neck', 'Head', 'LeftArm', 'RightArm', 'LeftLeg', 'RightLeg', 'Armature', 'RootNode']

archivos_necesitan_reorganizacion = []

print(f"\n{'='*80}")
print("DETECTANDO ARCHIVOS QUE NECESITAN REORGANIZACIÓN")
print(f"{'='*80}\n")

for base_dir in base_dirs:
    if not base_dir.exists():
        continue
    
    print(f"📂 Personaje: {base_dir.name}")
    print(f"{'='*80}")
    
    for categoria_dir in base_dir.iterdir():
        if not categoria_dir.is_dir():
            continue
        
        categoria = categoria_dir.name
        patron_busqueda = f"{base_dir.name}_resultado_*.glb"
        
        for glb_file in categoria_dir.glob(patron_busqueda):
            try:
                gltf = leer_glb(glb_file)
                
                if len(gltf['nodes']) > 0:
                    node0_name = gltf['nodes'][0].get('name', '')
                    
                    # Verificar si Node 0 es un hueso (necesita reorganización)
                    # o si es un mesh (ya está bien)
                    es_hueso = any(hueso in node0_name for hueso in nombres_huesos)
                    
                    # También verificar si tiene 'mesh' en node 0
                    tiene_mesh = 'mesh' in gltf['nodes'][0]
                    
                    if es_hueso or not tiene_mesh:
                        # Este archivo necesita reorganización
                        archivos_necesitan_reorganizacion.append({
                            'archivo': glb_file,
                            'personaje': base_dir.name,
                            'categoria': categoria,
                            'node0': node0_name
                        })
                        
            except Exception as e:
                pass

print()
print(f"{'='*80}")
print(f"📊 RESUMEN")
print(f"{'='*80}\n")
print(f"Total archivos que necesitan reorganización: {len(archivos_necesitan_reorganizacion)}\n")

if archivos_necesitan_reorganizacion:
    # Guardar lista
    lista_file = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\archivos_necesitan_reorganizacion.txt")
    with open(lista_file, 'w', encoding='utf-8') as f:
        for item in archivos_necesitan_reorganizacion:
            f.write(f"{item['archivo']}\n")
    
    print(f"📝 Lista guardada en: {lista_file.name}\n")
    
    print(f"Primeros 20 archivos detectados:")
    for item in archivos_necesitan_reorganizacion[:20]:
        print(f"  - {item['personaje']}/{item['categoria']}/{item['archivo'].name} (Node 0: {item['node0']})")
    
    if len(archivos_necesitan_reorganizacion) > 20:
        print(f"  ... y {len(archivos_necesitan_reorganizacion) - 20} más")

print(f"\n{'='*80}\n")
