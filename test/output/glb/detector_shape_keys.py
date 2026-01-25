"""
DETECTOR DE SHAPE KEYS EN GLB
Escanea todos los GLB para encontrar cuales tienen blendshapes faciales
"""

import bpy
import os
from pathlib import Path


DIRECTORIO_GLB = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb"


def escanear_glb(ruta_glb):
    """Importa un GLB y verifica si tiene shape keys"""
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Importar
    try:
        bpy.ops.import_scene.gltf(filepath=ruta_glb, loglevel=50)  # loglevel=50 = ERROR only
    except:
        return None
    
    # Buscar meshes con shape keys
    meshes_con_shapes = []
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.shape_keys:
            num_shapes = len(obj.data.shape_keys.key_blocks)
            
            # Verificar si tiene ARKit blendshapes
            shape_names = [kb.name for kb in obj.data.shape_keys.key_blocks]
            arkit_shapes = [s for s in shape_names if 'Mouth' in s or 'Eye' in s or 'Brow' in s or 'Nose' in s or 'Cheek' in s]
            
            meshes_con_shapes.append({
                'mesh': obj.name,
                'total_shapes': num_shapes,
                'arkit_shapes': len(arkit_shapes),
                'shapes': shape_names[:10]  # primeros 10
            })
    
    return meshes_con_shapes


def escanear_todos():
    """Escanea todos los GLB del directorio"""
    
    print("\n" + "="*70)
    print("DETECTOR DE SHAPE KEYS EN ARCHIVOS GLB")
    print("="*70)
    print(f"\nDirectorio: {DIRECTORIO_GLB}\n")
    
    # Obtener todos los GLB
    archivos_glb = list(Path(DIRECTORIO_GLB).glob("*.glb"))
    
    print(f"Archivos GLB encontrados: {len(archivos_glb)}\n")
    
    # Resultados
    con_shapes = []
    sin_shapes = []
    errores = []
    
    for i, archivo in enumerate(archivos_glb, 1):
        nombre = archivo.name
        print(f"[{i}/{len(archivos_glb)}] Escaneando: {nombre}...", end=" ")
        
        try:
            resultado = escanear_glb(str(archivo))
            
            if resultado is None:
                print("ERROR")
                errores.append(nombre)
            elif len(resultado) == 0:
                print("SIN shape keys")
                sin_shapes.append(nombre)
            else:
                total_arkit = sum(m['arkit_shapes'] for m in resultado)
                print(f"OK - {total_arkit} ARKit shapes")
                con_shapes.append({
                    'archivo': nombre,
                    'meshes': resultado,
                    'total_arkit': total_arkit
                })
        except Exception as e:
            print(f"ERROR: {e}")
            errores.append(nombre)
    
    # RESUMEN
    print("\n" + "="*70)
    print("RESUMEN")
    print("="*70)
    
    print(f"\nCON shape keys ARKit: {len(con_shapes)}")
    if con_shapes:
        print("\nArchivos con ARKit blendshapes:")
        # Ordenar por cantidad de ARKit shapes
        con_shapes.sort(key=lambda x: x['total_arkit'], reverse=True)
        
        for item in con_shapes:
            print(f"\n  {item['archivo']}")
            print(f"     Total ARKit shapes: {item['total_arkit']}")
            for mesh in item['meshes']:
                print(f"     - {mesh['mesh']}: {mesh['arkit_shapes']} ARKit / {mesh['total_shapes']} total")
                if mesh['shapes']:
                    print(f"       Ejemplos: {', '.join(mesh['shapes'][:5])}")
    
    print(f"\n\nSIN shape keys: {len(sin_shapes)}")
    
    print(f"\n\nErrores: {len(errores)}")
    
    # Recomendación
    if con_shapes:
        mejor = con_shapes[0]
        print("\n" + "="*70)
        print("RECOMENDACION")
        print("="*70)
        print(f"\nUSA ESTE ARCHIVO: {mejor['archivo']}")
        print(f"Tiene {mejor['total_arkit']} ARKit blendshapes")
        print("\nCambia en generar_remy_alegria.py:")
        print(f"RUTA_GLB_ORIGINAL = r\"{DIRECTORIO_GLB}\\{mejor['archivo']}\"")
    else:
        print("\n" + "="*70)
        print("NINGUN ARCHIVO TIENE ARKIT BLENDSHAPES")
        print("="*70)
        print("\nLos modelos GLB no incluyen shape keys faciales.")
        print("Necesitas exportar desde DeepMotion con 'Face Animation' habilitado.")
    
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    escanear_todos()
