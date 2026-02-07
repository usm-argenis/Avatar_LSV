#!/usr/bin/env python3
"""
Verificar con precisión las transformaciones del Armature en los archivos GLB
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

def obtener_transformacion_armature(glb_path):
    """Obtiene la transformación del Armature"""
    gltf = leer_glb(glb_path)
    
    for i, node in enumerate(gltf['nodes']):
        if node.get('name') == 'Armature':
            return {
                'rotation': node.get('rotation', [0, 0, 0, 1]),
                'scale': node.get('scale', [1, 1, 1]),
                'translation': node.get('translation', [0, 0, 0]),
                'node_index': i
            }
    return None

# Archivo de referencia (agarrar)
referencia_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")

print(f"\n{'='*80}")
print("VERIFICACIÓN DE PRECISIÓN - TRANSFORMACIONES ARMATURE")
print(f"{'='*80}\n")

# Leer transformación de agarrar
ref_transform = obtener_transformacion_armature(referencia_path)

if not ref_transform:
    print(f"❌ ERROR: No se encontró Armature en {referencia_path.name}")
    exit(1)

print(f"📌 ARCHIVO REFERENCIA: {referencia_path.name}")
print(f"   Node Index: {ref_transform['node_index']}")
print(f"   Rotation:    {ref_transform['rotation']}")
print(f"   Scale:       {ref_transform['scale']}")
print(f"   Translation: {ref_transform['translation']}")

# Archivos a verificar
archivos_verificar = [
    "amar", "ayudar", "cansar", "comer", "conocer",
    "decir", "deletrear", "dormir", "estar", "estudiar", "invitar",
    "preguntar", "presentar", "querer", "responder", "saludar",
    "sentir", "trabajar", "ver", "vivir"
]

base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos")

print(f"\n{'='*80}")
print("COMPARACIÓN CON ARCHIVOS PROCESADOS")
print(f"{'='*80}\n")

diferentes = []
identicos = 0

for nombre in archivos_verificar:
    archivo_path = base_dir / f"Duvall_resultado_{nombre}.glb"
    
    if not archivo_path.exists():
        print(f"⚠️  No existe: {archivo_path.name}")
        continue
    
    transform = obtener_transformacion_armature(archivo_path)
    
    if not transform:
        print(f"❌ {archivo_path.name} - No se encontró Armature")
        diferentes.append(nombre)
        continue
    
    # Comparar con precisión
    rot_igual = transform['rotation'] == ref_transform['rotation']
    scale_igual = transform['scale'] == ref_transform['scale']
    trans_igual = transform['translation'] == ref_transform['translation']
    
    if rot_igual and scale_igual and trans_igual:
        print(f"✅ {archivo_path.name} - IDÉNTICO")
        identicos += 1
    else:
        print(f"❌ {archivo_path.name} - DIFERENTE")
        if not rot_igual:
            print(f"   Rotation:    {transform['rotation']} (esperado: {ref_transform['rotation']})")
        if not scale_igual:
            print(f"   Scale:       {transform['scale']} (esperado: {ref_transform['scale']})")
        if not trans_igual:
            print(f"   Translation: {transform['translation']} (esperado: {ref_transform['translation']})")
        diferentes.append(nombre)

print(f"\n{'='*80}")
print(f"RESUMEN")
print(f"{'='*80}\n")
print(f"✅ Idénticos a agarrar: {identicos}")
print(f"❌ Diferentes: {len(diferentes)}")

if diferentes:
    print(f"\nArchivos con diferencias:")
    for nombre in diferentes:
        print(f"  - {nombre}")

print(f"\n{'='*80}\n")
