import struct
import json
from pathlib import Path

def inspeccionar_glb(ruta):
    archivo = Path(ruta)
    print(f"\nArchivo: {archivo.name}")
    
    with open(archivo, 'rb') as f:
        # Leer header
        f.read(12)  # Skip header
        
        # Leer chunk JSON
        chunk_length = struct.unpack('<I', f.read(4))[0]
        f.read(4)  # Skip chunk type
        
        json_data = f.read(chunk_length).decode('utf-8')
        gltf = json.loads(json_data)
        
        # Verificar contenido
        tiene_animaciones = 'animations' in gltf and len(gltf['animations']) > 0
        tiene_meshes = 'meshes' in gltf and len(gltf['meshes']) > 0
        tiene_nodes = 'nodes' in gltf and len(gltf['nodes']) > 0
        tiene_skins = 'skins' in gltf and len(gltf['skins']) > 0
        
        print(f"  Animaciones: {'SI' if tiene_animaciones else 'NO'}")
        print(f"  Meshes: {'SI' if tiene_meshes else 'NO'}")
        print(f"  Nodes: {'SI' if tiene_nodes else 'NO'}")
        print(f"  Skins: {'SI' if tiene_skins else 'NO'}")
        
        if tiene_meshes:
            print(f"  Total meshes: {len(gltf['meshes'])}")
        if tiene_animaciones:
            print(f"  Total animaciones: {len(gltf['animations'])}")

print("=" * 70)
print("VERIFICACION DE ARCHIVOS GLB")
print("=" * 70)

# Avatares
inspeccionar_glb(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\Nancy.glb")
inspeccionar_glb(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\Duvall.glb")

print("\n" + "=" * 70)
print("ANIMACIONES")
print("=" * 70)

# Animaciones desde carpetas individuales
inspeccionar_glb(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\saludos\saludos_Nancy_resultado_hola.glb")
inspeccionar_glb(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\saludos\Duvall_resultado_hola.glb")
inspeccionar_glb(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Luis\saludos\Luis_resultado_hola.glb")
inspeccionar_glb(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nina\saludos\Nina_resultado_hola.glb")

print("\n" + "=" * 70)
