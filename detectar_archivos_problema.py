#!/usr/bin/env python3
"""
Detectar archivos GLB con problemas de RootNode/Armature
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

# Buscar en todas las categorías de Duvall y Carla
base_dirs = [
    Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall"),
    Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Carla")
]

archivos_con_problema = []

print(f"\n{'='*80}")
print("DETECTANDO ARCHIVOS CON PROBLEMAS")
print(f"{'='*80}\n")

for base_dir in base_dirs:
    if not base_dir.exists():
        print(f"⚠️  No existe: {base_dir}")
        continue
    
    print(f"\n📂 Personaje: {base_dir.name}")
    print(f"{'='*80}")
    
    for categoria_dir in base_dir.iterdir():
        if categoria_dir.is_dir():
            categoria = categoria_dir.name
            print(f"  📁 {categoria}")
            
            # Buscar archivos GLB (Duvall_resultado_* o Carla_resultado_*)
            patron_busqueda = f"{base_dir.name}_resultado_*.glb"
            for glb_file in categoria_dir.glob(patron_busqueda):
                try:
                    gltf = leer_glb(glb_file)
                    
                    # Verificar si tiene RootNode o Armature problemático
                    tiene_problema = False
                    
                    if len(gltf['nodes']) > 0:
                        node0 = gltf['nodes'][0]
                        node1 = gltf['nodes'][1] if len(gltf['nodes']) > 1 else None
                        
                        # Problema 1: Node 0 es RootNode
                        if node0.get('name') == 'RootNode':
                            tiene_problema = True
                            motivo = "RootNode en Node 0"
                        
                        # Problema 2: Node 1 es Armature con rotación/escala incorrecta
                        elif node1 and node1.get('name') == 'Armature':
                            rotation = node1.get('rotation', [0, 0, 0, 1])
                            scale = node1.get('scale', [1, 1, 1])
                            
                            # Verificar rotación X = -0.7071 (90 grados) y escala = 100
                            if abs(rotation[0] + 0.7071) < 0.01 and abs(scale[0] - 100) < 1:
                                tiene_problema = True
                                motivo = "Armature con rotación -90° y escala 100"
                    
                    if tiene_problema:
                        archivos_con_problema.append({
                            'archivo': glb_file,
                            'personaje': base_dir.name,
                            'categoria': categoria,
                            'motivo': motivo
                        })
                        print(f"     ❌ {glb_file.name} - {motivo}")
                        
                except Exception as e:
                    print(f"     ⚠️  Error leyendo {glb_file.name}: {e}")

print(f"\n{'='*80}")
print(f"📊 RESUMEN")
print(f"{'='*80}\n")
print(f"Total archivos con problemas: {len(archivos_con_problema)}\n")

if archivos_con_problema:
    # Guardar lista
    lista_file = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\archivos_con_problema_detectados.txt")
    with open(lista_file, 'w', encoding='utf-8') as f:
        for item in archivos_con_problema:
            f.write(f"{item['archivo']}\n")
    
    print(f"📝 Lista guardada en: {lista_file.name}\n")
    
    print("Archivos detectados:")
    for item in archivos_con_problema:
        print(f"  - {item['personaje']}/{item['categoria']}/{item['archivo'].name}")

print(f"\n{'='*80}\n")
