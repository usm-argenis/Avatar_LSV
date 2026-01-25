"""
Script para ajustar la altura del modelo Duvall comparando con un modelo de referencia
"""
import json
import struct
import os

def leer_glb(archivo_path):
    """Lee un archivo GLB y extrae información relevante"""
    with open(archivo_path, 'rb') as f:
        # Leer header GLB
        magic = f.read(4)
        if magic != b'glTF':
            raise ValueError("No es un archivo GLB válido")
        
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        # Leer chunk JSON
        json_chunk_length = struct.unpack('<I', f.read(4))[0]
        json_chunk_type = f.read(4)
        json_data = f.read(json_chunk_length)
        
        # Parsear JSON
        gltf = json.loads(json_data.decode('utf-8'))
        
        # Leer chunk binario si existe
        binary_data = None
        if f.tell() < length:
            bin_chunk_length = struct.unpack('<I', f.read(4))[0]
            bin_chunk_type = f.read(4)
            binary_data = f.read(bin_chunk_length)
        
        return gltf, binary_data

def analizar_transformaciones(gltf):
    """Analiza las transformaciones (escala, traslación) de los nodos"""
    info = {
        'nodes': [],
        'scene_info': {},
        'scale_values': [],
        'translation_values': []
    }
    
    if 'nodes' in gltf:
        for i, node in enumerate(gltf['nodes']):
            node_info = {
                'index': i,
                'name': node.get('name', f'Node_{i}'),
                'scale': node.get('scale'),
                'translation': node.get('translation'),
                'rotation': node.get('rotation'),
                'matrix': node.get('matrix')
            }
            info['nodes'].append(node_info)
            
            if node.get('scale'):
                info['scale_values'].append(node['scale'])
            if node.get('translation'):
                info['translation_values'].append(node['translation'])
    
    # Información de la escena
    if 'scene' in gltf and 'scenes' in gltf:
        scene = gltf['scenes'][gltf['scene']]
        info['scene_info'] = {
            'name': scene.get('name', 'Scene'),
            'nodes': scene.get('nodes', [])
        }
    
    return info

def escribir_glb(archivo_path, gltf, binary_data):
    """Escribe un archivo GLB con los datos modificados"""
    # Convertir JSON a bytes
    json_data = json.dumps(gltf, separators=(',', ':')).encode('utf-8')
    
    # Padding del JSON a múltiplo de 4
    json_padding = (4 - (len(json_data) % 4)) % 4
    json_data += b' ' * json_padding
    
    # Calcular longitud total
    total_length = 12 + 8 + len(json_data)  # header + json chunk header + json data
    if binary_data:
        bin_padding = (4 - (len(binary_data) % 4)) % 4
        binary_data += b'\x00' * bin_padding
        total_length += 8 + len(binary_data)  # binary chunk header + binary data
    
    with open(archivo_path, 'wb') as f:
        # Header GLB
        f.write(b'glTF')
        f.write(struct.pack('<I', 2))  # version
        f.write(struct.pack('<I', total_length))
        
        # Chunk JSON
        f.write(struct.pack('<I', len(json_data)))
        f.write(b'JSON')
        f.write(json_data)
        
        # Chunk binario
        if binary_data:
            f.write(struct.pack('<I', len(binary_data)))
            f.write(b'BIN\x00')
            f.write(binary_data)

def ajustar_altura_modelo(archivo_origen, archivo_destino, archivo_referencia):
    """
    Ajusta la altura del modelo de origen basándose en la referencia
    """
    print("=" * 80)
    print("ANÁLISIS DE MODELOS GLB - AJUSTE DE ALTURA")
    print("=" * 80)
    
    # Leer modelos
    print(f"\n📖 Leyendo modelo de referencia: {os.path.basename(archivo_referencia)}")
    gltf_ref, binary_ref = leer_glb(archivo_referencia)
    info_ref = analizar_transformaciones(gltf_ref)
    
    print(f"\n📖 Leyendo modelo de Duvall: {os.path.basename(archivo_origen)}")
    gltf_duvall, binary_duvall = leer_glb(archivo_origen)
    info_duvall = analizar_transformaciones(gltf_duvall)
    
    # Mostrar información de referencia
    print("\n" + "=" * 80)
    print("MODELO DE REFERENCIA (hola_default.glb)")
    print("=" * 80)
    print(f"Total de nodos: {len(info_ref['nodes'])}")
    
    if info_ref['scale_values']:
        print(f"\n📏 Escalas encontradas en referencia:")
        for scale in info_ref['scale_values']:
            print(f"   Scale: {scale}")
    
    if info_ref['translation_values']:
        print(f"\n📍 Traslaciones encontradas en referencia:")
        for trans in info_ref['translation_values']:
            print(f"   Translation: {trans}")
    
    # Mostrar información de Duvall
    print("\n" + "=" * 80)
    print("MODELO ACTUAL DE DUVALL")
    print("=" * 80)
    print(f"Total de nodos: {len(info_duvall['nodes'])}")
    
    if info_duvall['scale_values']:
        print(f"\n📏 Escalas encontradas en Duvall:")
        for scale in info_duvall['scale_values']:
            print(f"   Scale: {scale}")
    
    if info_duvall['translation_values']:
        print(f"\n📍 Traslaciones encontradas en Duvall:")
        for trans in info_duvall['translation_values']:
            print(f"   Translation: {trans}")
    
    # Análisis de nodos específicos
    print("\n" + "=" * 80)
    print("ANÁLISIS DETALLADO DE NODOS")
    print("=" * 80)
    
    print("\n🔍 Nodos en REFERENCIA con transformaciones:")
    for node_info in info_ref['nodes']:
        if node_info['scale'] or node_info['translation'] or node_info['matrix']:
            print(f"\n   Nodo {node_info['index']}: {node_info['name']}")
            if node_info['scale']:
                print(f"      Scale: {node_info['scale']}")
            if node_info['translation']:
                print(f"      Translation: {node_info['translation']}")
            if node_info['rotation']:
                print(f"      Rotation: {node_info['rotation']}")
    
    print("\n🔍 Nodos en DUVALL con transformaciones:")
    for node_info in info_duvall['nodes']:
        if node_info['scale'] or node_info['translation'] or node_info['matrix']:
            print(f"\n   Nodo {node_info['index']}: {node_info['name']}")
            if node_info['scale']:
                print(f"      Scale: {node_info['scale']}")
            if node_info['translation']:
                print(f"      Translation: {node_info['translation']}")
            if node_info['rotation']:
                print(f"      Rotation: {node_info['rotation']}")
    
    # Buscar nodos principales (usualmente el root o el armature)
    print("\n" + "=" * 80)
    print("PROPUESTA DE AJUSTE")
    print("=" * 80)
    
    # Copiar transformaciones de referencia a Duvall
    modificaciones = []
    
    for i, node_duvall in enumerate(gltf_duvall['nodes']):
        if i < len(gltf_ref['nodes']):
            node_ref = gltf_ref['nodes'][i]
            
            # Si el nodo de referencia tiene scale y el de Duvall también
            if 'scale' in node_ref and 'scale' in node_duvall:
                scale_original = node_duvall['scale']
                scale_nueva = node_ref['scale']
                if scale_original != scale_nueva:
                    node_duvall['scale'] = scale_nueva
                    modificaciones.append({
                        'nodo': i,
                        'nombre': node_duvall.get('name', f'Node_{i}'),
                        'tipo': 'scale',
                        'anterior': scale_original,
                        'nueva': scale_nueva
                    })
            
            # Si el nodo de referencia tiene translation y el de Duvall también
            if 'translation' in node_ref and 'translation' in node_duvall:
                trans_original = node_duvall['translation']
                trans_nueva = node_ref['translation']
                if trans_original != trans_nueva:
                    node_duvall['translation'] = trans_nueva
                    modificaciones.append({
                        'nodo': i,
                        'nombre': node_duvall.get('name', f'Node_{i}'),
                        'tipo': 'translation',
                        'anterior': trans_original,
                        'nueva': trans_nueva
                    })
    
    if modificaciones:
        print("\n✏️ Modificaciones a realizar:")
        for mod in modificaciones:
            print(f"\n   Nodo {mod['nodo']}: {mod['nombre']}")
            print(f"      {mod['tipo'].upper()}")
            print(f"      Antes: {mod['anterior']}")
            print(f"      Después: {mod['nueva']}")
    else:
        print("\n⚠️ No se encontraron diferencias significativas en las transformaciones.")
        print("   Los modelos ya tienen valores similares.")
    
    # Guardar modelo modificado
    print(f"\n💾 Guardando modelo modificado en: {os.path.basename(archivo_destino)}")
    escribir_glb(archivo_destino, gltf_duvall, binary_duvall)
    
    print("\n" + "=" * 80)
    print("✅ PROCESO COMPLETADO")
    print("=" * 80)
    print(f"\nArchivo modificado guardado en:")
    print(f"   {archivo_destino}")
    print(f"\nTotal de modificaciones aplicadas: {len(modificaciones)}")
    
    return modificaciones

if __name__ == "__main__":
    # Rutas de archivos
    archivo_referencia = r"C:\Users\andre\Downloads\hola_default.glb"
    archivo_origen = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\saludos\Duvall_resultado_hola.glb"
    archivo_destino = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\saludos\Duvall_resultado_hola_ajustado.glb"
    
    # Verificar que existen los archivos
    if not os.path.exists(archivo_referencia):
        print(f"❌ Error: No se encuentra el archivo de referencia en {archivo_referencia}")
        exit(1)
    
    if not os.path.exists(archivo_origen):
        print(f"❌ Error: No se encuentra el archivo de Duvall en {archivo_origen}")
        exit(1)
    
    # Ejecutar ajuste
    try:
        modificaciones = ajustar_altura_modelo(archivo_origen, archivo_destino, archivo_referencia)
        
        if modificaciones:
            print("\n" + "=" * 80)
            print("INSTRUCCIONES")
            print("=" * 80)
            print("\n1. Revisa el archivo generado en:")
            print(f"   {archivo_destino}")
            print("\n2. Compara la visualización con el modelo original")
            print("\n3. Si está correcto, confirma para aplicar a todos los modelos de Duvall")
            print("\n4. Si necesita ajustes, modifica el script y vuelve a ejecutar")
        
    except Exception as e:
        print(f"\n❌ Error durante el proceso: {str(e)}")
        import traceback
        traceback.print_exc()
