#!/usr/bin/env python3
"""
Detectar archivos GLB donde Node 0 NO es Hips (estructura incorrecta)
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

archivos_con_estructura_incorrecta = []

print(f"\n{'='*80}")
print("DETECTANDO ARCHIVOS CON ESTRUCTURA INCORRECTA")
print("(Node 0 NO es Hips - meshes primero en lugar de huesos)")
print(f"{'='*80}\n")

for base_dir in base_dirs:
    if not base_dir.exists():
        continue
    
    print(f"\n📂 Personaje: {base_dir.name}")
    print(f"{'='*80}")
    
    for categoria_dir in base_dir.iterdir():
        if categoria_dir.is_dir():
            categoria = categoria_dir.name
            
            # Buscar archivos GLB
            patron_busqueda = f"{base_dir.name}_resultado_*.glb"
            archivos_en_categoria = []
            
            for glb_file in categoria_dir.glob(patron_busqueda):
                # Ignorar backups
                if 'backup' in glb_file.name.lower():
                    continue
                    
                try:
                    gltf = leer_glb(glb_file)
                    
                    if len(gltf['nodes']) > 0:
                        node0 = gltf['nodes'][0]
                        node0_name = node0.get('name', 'N/A')
                        
                        # Si Node 0 NO es Hips, está mal reorganizado
                        if node0_name != 'Hips':
                            archivos_en_categoria.append({
                                'archivo': glb_file,
                                'personaje': base_dir.name,
                                'categoria': categoria,
                                'node0': node0_name
                            })
                            archivos_con_estructura_incorrecta.append(archivos_en_categoria[-1])
                        
                except Exception as e:
                    pass
            
            if archivos_en_categoria:
                print(f"  📁 {categoria}")
                for item in archivos_en_categoria:
                    print(f"     ❌ {item['archivo'].name} (Node 0: {item['node0']})")

print(f"\n{'='*80}")
print(f"📊 RESUMEN")
print(f"{'='*80}\n")
print(f"Total archivos con estructura incorrecta: {len(archivos_con_estructura_incorrecta)}\n")

if archivos_con_estructura_incorrecta:
    # Guardar lista
    lista_file = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\archivos_estructura_incorrecta.txt")
    with open(lista_file, 'w', encoding='utf-8') as f:
        for item in archivos_con_estructura_incorrecta:
            f.write(f"{item['archivo']}\n")
    
    print(f"📝 Lista guardada en: {lista_file.name}\n")
    
    print("Archivos a corregir:")
    for item in archivos_con_estructura_incorrecta:
        print(f"  - {item['personaje']}/{item['categoria']}/{item['archivo'].name}")
else:
    print("✅ No hay archivos con estructura incorrecta")

print(f"\n{'='*80}\n")
