"""
Extrae SOLO las animaciones de archivos GLB y las guarda sin geometría ni materiales.
Para usar con Nancy: carga el modelo base una vez y aplica animaciones separadas.
"""

import os
import json
import struct
from pathlib import Path

def extraer_animacion_pura(input_path, output_path):
    """
    Extrae solo la animación de un GLB, eliminando meshes y materiales.
    """
    try:
        with open(input_path, 'rb') as f:
            # Leer header GLB
            magic = f.read(4)
            if magic != b'glTF':
                print(f"❌ No es un archivo GLB válido: {input_path}")
                return False
            
            version = struct.unpack('<I', f.read(4))[0]
            length = struct.unpack('<I', f.read(4))[0]
            
            # Leer chunk JSON
            json_chunk_length = struct.unpack('<I', f.read(4))[0]
            json_chunk_type = struct.unpack('<I', f.read(4))[0]
            json_data = json.loads(f.read(json_chunk_length).decode('utf-8'))
            
            # Leer chunk BIN
            bin_chunk_length = struct.unpack('<I', f.read(4))[0]
            bin_chunk_type = struct.unpack('<I', f.read(4))[0]
            bin_data = f.read(bin_chunk_length)
        
        # Verificar que tenga animaciones
        if 'animations' not in json_data or len(json_data['animations']) == 0:
            print(f"⚠️  No hay animaciones en: {input_path}")
            return False
        
        # Crear nuevo GLB solo con animación
        nuevo_gltf = {
            "asset": json_data.get("asset", {"version": "2.0"}),
            "animations": json_data["animations"],
            "accessors": [],
            "bufferViews": [],
            "buffers": [{"byteLength": bin_chunk_length}],
            "nodes": json_data.get("nodes", []),
            "skins": json_data.get("skins", [])
        }
        
        # Mantener solo accessors usados por animaciones
        used_accessors = set()
        for anim in json_data["animations"]:
            for sampler in anim.get("samplers", []):
                used_accessors.add(sampler.get("input"))
                used_accessors.add(sampler.get("output"))
        
        # Copiar accessors necesarios
        accessor_map = {}
        for idx in sorted(used_accessors):
            if idx is not None and idx < len(json_data.get("accessors", [])):
                nuevo_gltf["accessors"].append(json_data["accessors"][idx])
                accessor_map[idx] = len(nuevo_gltf["accessors"]) - 1
        
        # Actualizar índices en samplers
        for anim in nuevo_gltf["animations"]:
            for sampler in anim.get("samplers", []):
                if sampler.get("input") in accessor_map:
                    sampler["input"] = accessor_map[sampler["input"]]
                if sampler.get("output") in accessor_map:
                    sampler["output"] = accessor_map[sampler["output"]]
        
        # Copiar bufferViews necesarios
        used_bufferviews = set()
        for accessor in nuevo_gltf["accessors"]:
            if "bufferView" in accessor:
                used_bufferviews.add(accessor["bufferView"])
        
        bufferview_map = {}
        for idx in sorted(used_bufferviews):
            if idx < len(json_data.get("bufferViews", [])):
                nuevo_gltf["bufferViews"].append(json_data["bufferViews"][idx])
                bufferview_map[idx] = len(nuevo_gltf["bufferViews"]) - 1
        
        # Actualizar índices en accessors
        for accessor in nuevo_gltf["accessors"]:
            if "bufferView" in accessor and accessor["bufferView"] in bufferview_map:
                accessor["bufferView"] = bufferview_map[accessor["bufferView"]]
        
        # Escribir nuevo GLB
        json_string = json.dumps(nuevo_gltf, separators=(',', ':'))
        json_bytes = json_string.encode('utf-8')
        
        # Padding para alineación de 4 bytes
        json_padding = (4 - (len(json_bytes) % 4)) % 4
        json_bytes += b' ' * json_padding
        
        total_length = 12 + 8 + len(json_bytes) + 8 + len(bin_data)
        
        with open(output_path, 'wb') as f:
            # Header GLB
            f.write(b'glTF')
            f.write(struct.pack('<I', 2))
            f.write(struct.pack('<I', total_length))
            
            # Chunk JSON
            f.write(struct.pack('<I', len(json_bytes)))
            f.write(struct.pack('<I', 0x4E4F534A))  # 'JSON'
            f.write(json_bytes)
            
            # Chunk BIN
            f.write(struct.pack('<I', len(bin_data)))
            f.write(struct.pack('<I', 0x004E4942))  # 'BIN\0'
            f.write(bin_data)
        
        return True
        
    except Exception as e:
        print(f"❌ Error procesando {input_path}: {e}")
        return False

def procesar_carpeta_nancy():
    """
    Procesa todas las animaciones en las subcarpetas de Nancy desde estructura por género
    """
    # Buscar primero en nueva estructura por género
    base_paths = [
        Path(__file__).parent / "Mujer",  # Nueva estructura
        Path(__file__).parent / "Nancy"   # Fallback estructura anterior
    ]
    
    base_path = None
    for path in base_paths:
        if path.exists():
            base_path = path
            print(f"✅ Usando estructura: {base_path}")
            break
    
    if not base_path:
        print(f"❌ No existe ninguna carpeta: {[str(p) for p in base_paths]}")
        return
    
    output_path = Path(__file__).parent / "Nancy_animation"
    output_path.mkdir(exist_ok=True)
    print(f"✅ Carpeta de salida: {output_path}")
    
    categorias = [
        'alfabeto', 'cortesia', 'dias_semana', 'expresiones',
        'preguntas', 'pronombres', 'saludos', 'tiempo'
    ]
    
    total_procesados = 0
    total_exitosos = 0
    
    for categoria in categorias:
        categoria_path = base_path / categoria
        if not categoria_path.exists():
            print(f"⚠️  No existe: {categoria}")
            continue
        
        print(f"\n📁 Procesando: {categoria}")
        
        archivos_glb = list(categoria_path.glob("*.glb"))
        for archivo in archivos_glb:
            total_procesados += 1
            nombre_salida = f"{categoria}_{archivo.name}"
            salida = output_path / nombre_salida
            
            print(f"  🔄 {archivo.name} → {nombre_salida}", end=" ")
            
            if extraer_animacion_pura(str(archivo), str(salida)):
                total_exitosos += 1
                size_original = archivo.stat().st_size
                size_nuevo = salida.stat().st_size
                reduccion = ((size_original - size_nuevo) / size_original) * 100
                print(f"✅ ({size_original//1024}KB → {size_nuevo//1024}KB, -{reduccion:.1f}%)")
            else:
                print("❌")
    
    print(f"\n{'='*60}")
    print(f"✅ Procesados: {total_procesados}")
    print(f"✅ Exitosos: {total_exitosos}")
    print(f"❌ Fallidos: {total_procesados - total_exitosos}")
    print(f"📁 Archivos en: {output_path}")
    print(f"{'='*60}")

if __name__ == "__main__":
    procesar_carpeta_nancy()
