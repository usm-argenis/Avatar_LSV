"""
Script para analizar exhaustivamente los huesos del modelo, especialmente hombros y cuello
"""
import json
import struct
import os
import math

def leer_glb(archivo_path):
    """Lee un archivo GLB y extrae información relevante"""
    with open(archivo_path, 'rb') as f:
        magic = f.read(4)
        if magic != b'glTF':
            raise ValueError("No es un archivo GLB válido")
        
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        json_chunk_length = struct.unpack('<I', f.read(4))[0]
        json_chunk_type = f.read(4)
        json_data = f.read(json_chunk_length)
        
        gltf = json.loads(json_data.decode('utf-8'))
        
        binary_data = None
        if f.tell() < length:
            bin_chunk_length = struct.unpack('<I', f.read(4))[0]
            bin_chunk_type = f.read(4)
            binary_data = f.read(bin_chunk_length)
        
        return gltf, binary_data

def escribir_glb(archivo_path, gltf, binary_data):
    """Escribe un archivo GLB con los datos modificados"""
    json_data = json.dumps(gltf, separators=(',', ':')).encode('utf-8')
    json_padding = (4 - (len(json_data) % 4)) % 4
    json_data += b' ' * json_padding
    
    total_length = 12 + 8 + len(json_data)
    if binary_data:
        bin_padding = (4 - (len(binary_data) % 4)) % 4
        binary_data += b'\x00' * bin_padding
        total_length += 8 + len(binary_data)
    
    with open(archivo_path, 'wb') as f:
        f.write(b'glTF')
        f.write(struct.pack('<I', 2))
        f.write(struct.pack('<I', total_length))
        f.write(struct.pack('<I', len(json_data)))
        f.write(b'JSON')
        f.write(json_data)
        
        if binary_data:
            f.write(struct.pack('<I', len(binary_data)))
            f.write(b'BIN\x00')
            f.write(binary_data)

def calcular_magnitud(vector):
    """Calcula la magnitud de un vector 3D"""
    if not vector or len(vector) < 3:
        return 0
    return math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

def comparar_vectores(vec1, vec2):
    """Compara dos vectores y retorna la diferencia"""
    if not vec1 or not vec2:
        return None
    diff = [vec2[i] - vec1[i] for i in range(len(vec1))]
    magnitud_diff = calcular_magnitud(diff)
    return {
        'diferencia': diff,
        'magnitud': magnitud_diff
    }

def analizar_hueso(nombre_hueso, nodo_ref, nodo_duvall, indice):
    """Analiza un hueso específico comparando referencia con Duvall"""
    analisis = {
        'nombre': nombre_hueso,
        'indice': indice,
        'diferencias': {}
    }
    
    # Comparar escala
    if 'scale' in nodo_ref and 'scale' in nodo_duvall:
        comp = comparar_vectores(nodo_duvall['scale'], nodo_ref['scale'])
        if comp and comp['magnitud'] > 0.0001:  # Umbral de diferencia significativa
            analisis['diferencias']['scale'] = {
                'duvall': nodo_duvall['scale'],
                'referencia': nodo_ref['scale'],
                'diferencia': comp['diferencia'],
                'magnitud': comp['magnitud']
            }
    
    # Comparar traslación
    if 'translation' in nodo_ref and 'translation' in nodo_duvall:
        comp = comparar_vectores(nodo_duvall['translation'], nodo_ref['translation'])
        if comp and comp['magnitud'] > 0.0001:
            analisis['diferencias']['translation'] = {
                'duvall': nodo_duvall['translation'],
                'referencia': nodo_ref['translation'],
                'diferencia': comp['diferencia'],
                'magnitud': comp['magnitud']
            }
    
    # Comparar rotación
    if 'rotation' in nodo_ref and 'rotation' in nodo_duvall:
        comp = comparar_vectores(nodo_duvall['rotation'][:3], nodo_ref['rotation'][:3])
        if comp and comp['magnitud'] > 0.01:  # Mayor umbral para rotaciones
            analisis['diferencias']['rotation'] = {
                'duvall': nodo_duvall['rotation'],
                'referencia': nodo_ref['rotation'],
                'diferencia': comp['diferencia'],
                'magnitud': comp['magnitud']
            }
    
    return analisis if analisis['diferencias'] else None

def analizar_estructura_completa(gltf_ref, gltf_duvall):
    """Analiza exhaustivamente todos los huesos importantes"""
    
    # Huesos críticos a analizar (en orden de importancia)
    huesos_criticos = [
        'Hips',
        'Spine', 'Spine1', 'Spine2',
        'Neck', 'Head', 'HeadTop_End',
        'LeftShoulder', 'RightShoulder',
        'LeftArm', 'RightArm',
        'LeftForeArm', 'RightForeArm',
        'LeftHand', 'RightHand',
        'LeftUpLeg', 'RightUpLeg',
        'LeftLeg', 'RightLeg',
        'LeftFoot', 'RightFoot'
    ]
    
    # Crear mapeo de nombres a índices
    nombre_a_indice_ref = {}
    nombre_a_indice_duvall = {}
    
    for i, node in enumerate(gltf_ref['nodes']):
        if 'name' in node:
            nombre_a_indice_ref[node['name']] = i
    
    for i, node in enumerate(gltf_duvall['nodes']):
        if 'name' in node:
            nombre_a_indice_duvall[node['name']] = i
    
    analisis_general = {
        'huesos_criticos': [],
        'huesos_problematicos': [],
        'resumen': {
            'total_diferencias': 0,
            'diferencias_scale': 0,
            'diferencias_translation': 0,
            'diferencias_rotation': 0
        }
    }
    
    print("\n" + "=" * 80)
    print("ANÁLISIS EXHAUSTIVO DE HUESOS")
    print("=" * 80)
    
    for nombre_hueso in huesos_criticos:
        if nombre_hueso in nombre_a_indice_ref and nombre_hueso in nombre_a_indice_duvall:
            idx_ref = nombre_a_indice_ref[nombre_hueso]
            idx_duvall = nombre_a_indice_duvall[nombre_hueso]
            
            nodo_ref = gltf_ref['nodes'][idx_ref]
            nodo_duvall = gltf_duvall['nodes'][idx_duvall]
            
            analisis = analizar_hueso(nombre_hueso, nodo_ref, nodo_duvall, idx_duvall)
            
            if analisis:
                analisis_general['huesos_criticos'].append(analisis)
                
                # Contabilizar diferencias
                if 'scale' in analisis['diferencias']:
                    analisis_general['resumen']['diferencias_scale'] += 1
                if 'translation' in analisis['diferencias']:
                    analisis_general['resumen']['diferencias_translation'] += 1
                if 'rotation' in analisis['diferencias']:
                    analisis_general['resumen']['diferencias_rotation'] += 1
                
                analisis_general['resumen']['total_diferencias'] += 1
                
                # Identificar huesos problemáticos (con diferencias significativas)
                mag_total = 0
                if 'translation' in analisis['diferencias']:
                    mag_total += analisis['diferencias']['translation']['magnitud']
                if 'scale' in analisis['diferencias']:
                    mag_total += analisis['diferencias']['scale']['magnitud']
                
                if mag_total > 0.01:  # Umbral de problema
                    analisis_general['huesos_problematicos'].append({
                        'nombre': nombre_hueso,
                        'magnitud_total': mag_total,
                        'diferencias': analisis['diferencias']
                    })
    
    return analisis_general

def mostrar_analisis_detallado(analisis):
    """Muestra el análisis de forma detallada y organizada"""
    
    print(f"\n📊 RESUMEN GENERAL:")
    print(f"   Total de huesos con diferencias: {analisis['resumen']['total_diferencias']}")
    print(f"   Diferencias en SCALE: {analisis['resumen']['diferencias_scale']}")
    print(f"   Diferencias en TRANSLATION: {analisis['resumen']['diferencias_translation']}")
    print(f"   Diferencias en ROTATION: {analisis['resumen']['diferencias_rotation']}")
    
    if analisis['huesos_problematicos']:
        print("\n" + "=" * 80)
        print("⚠️  HUESOS PROBLEMÁTICOS (Requieren atención especial)")
        print("=" * 80)
        
        # Ordenar por magnitud de mayor a menor
        huesos_ordenados = sorted(analisis['huesos_problematicos'], 
                                  key=lambda x: x['magnitud_total'], 
                                  reverse=True)
        
        for i, hueso in enumerate(huesos_ordenados, 1):
            print(f"\n{i}. 🦴 {hueso['nombre']}")
            print(f"   Magnitud total de diferencia: {hueso['magnitud_total']:.6f}")
            
            for tipo, datos in hueso['diferencias'].items():
                print(f"\n   {tipo.upper()}:")
                print(f"      Duvall:      {[f'{v:.6f}' for v in datos['duvall']]}")
                print(f"      Referencia:  {[f'{v:.6f}' for v in datos['referencia']]}")
                print(f"      Diferencia:  {[f'{v:.6f}' for v in datos['diferencia']]}")
                print(f"      Magnitud:    {datos['magnitud']:.6f}")
    
    # Análisis específico de hombros y cuello
    print("\n" + "=" * 80)
    print("🎯 ANÁLISIS ESPECÍFICO: HOMBROS Y CUELLO")
    print("=" * 80)
    
    huesos_objetivo = ['Neck', 'Head', 'LeftShoulder', 'RightShoulder', 'Spine2']
    
    for hueso_critico in analisis['huesos_criticos']:
        if hueso_critico['nombre'] in huesos_objetivo:
            print(f"\n🔍 {hueso_critico['nombre']} (Índice: {hueso_critico['indice']})")
            
            if not hueso_critico['diferencias']:
                print("   ✅ Sin diferencias significativas")
            else:
                for tipo, datos in hueso_critico['diferencias'].items():
                    print(f"\n   {tipo.upper()}:")
                    print(f"      Duvall:      {datos['duvall']}")
                    print(f"      Referencia:  {datos['referencia']}")
                    print(f"      Diferencia:  {datos['diferencia']}")
                    print(f"      Magnitud:    {datos['magnitud']:.6f}")

def aplicar_correcciones_mejoradas(gltf_ref, gltf_duvall, analisis):
    """Aplica correcciones basadas en el análisis detallado"""
    
    print("\n" + "=" * 80)
    print("🔧 APLICANDO CORRECCIONES MEJORADAS")
    print("=" * 80)
    
    modificaciones = []
    
    # Crear mapeo de nombres a índices
    nombre_a_indice_ref = {}
    nombre_a_indice_duvall = {}
    
    for i, node in enumerate(gltf_ref['nodes']):
        if 'name' in node:
            nombre_a_indice_ref[node['name']] = i
    
    for i, node in enumerate(gltf_duvall['nodes']):
        if 'name' in node:
            nombre_a_indice_duvall[node['name']] = i
    
    # Aplicar correcciones a huesos críticos
    for hueso_info in analisis['huesos_criticos']:
        nombre = hueso_info['nombre']
        idx_duvall = hueso_info['indice']
        
        if nombre in nombre_a_indice_ref:
            idx_ref = nombre_a_indice_ref[nombre]
            nodo_ref = gltf_ref['nodes'][idx_ref]
            nodo_duvall = gltf_duvall['nodes'][idx_duvall]
            
            cambios_nodo = []
            
            # Copiar scale si hay diferencia
            if 'scale' in hueso_info['diferencias']:
                if 'scale' in nodo_ref:
                    valor_anterior = nodo_duvall.get('scale', [1, 1, 1])
                    nodo_duvall['scale'] = nodo_ref['scale'].copy()
                    cambios_nodo.append(f"scale: {valor_anterior} → {nodo_ref['scale']}")
            
            # Copiar translation si hay diferencia
            if 'translation' in hueso_info['diferencias']:
                if 'translation' in nodo_ref:
                    valor_anterior = nodo_duvall.get('translation', [0, 0, 0])
                    nodo_duvall['translation'] = nodo_ref['translation'].copy()
                    cambios_nodo.append(f"translation: {valor_anterior} → {nodo_ref['translation']}")
            
            # Copiar rotation si hay diferencia significativa
            if 'rotation' in hueso_info['diferencias']:
                if 'rotation' in nodo_ref:
                    valor_anterior = nodo_duvall.get('rotation', [0, 0, 0, 1])
                    nodo_duvall['rotation'] = nodo_ref['rotation'].copy()
                    cambios_nodo.append(f"rotation: {valor_anterior} → {nodo_ref['rotation']}")
            
            if cambios_nodo:
                modificaciones.append({
                    'nodo': idx_duvall,
                    'nombre': nombre,
                    'cambios': cambios_nodo
                })
    
    if modificaciones:
        print(f"\n✅ Se aplicaron {len(modificaciones)} correcciones:")
        for mod in modificaciones:
            print(f"\n   Nodo {mod['nodo']}: {mod['nombre']}")
            for cambio in mod['cambios']:
                print(f"      • {cambio}")
    else:
        print("\n⚠️ No se aplicaron correcciones (no se encontraron diferencias)")
    
    return modificaciones

if __name__ == "__main__":
    # Rutas de archivos
    archivo_referencia = r"C:\Users\andre\Downloads\hola_default.glb"
    archivo_origen = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\saludos\Duvall_resultado_hola.glb"
    archivo_destino = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\saludos\Duvall_resultado_hola_corregido.glb"
    
    print("=" * 80)
    print("ANÁLISIS EXHAUSTIVO DE HUESOS - DUVALL")
    print("=" * 80)
    print(f"\n📖 Modelo de referencia: {os.path.basename(archivo_referencia)}")
    print(f"📖 Modelo de Duvall: {os.path.basename(archivo_origen)}")
    
    # Verificar archivos
    if not os.path.exists(archivo_referencia):
        print(f"❌ Error: No se encuentra el archivo de referencia")
        exit(1)
    
    if not os.path.exists(archivo_origen):
        print(f"❌ Error: No se encuentra el archivo de Duvall")
        exit(1)
    
    try:
        # Leer modelos
        gltf_ref, binary_ref = leer_glb(archivo_referencia)
        gltf_duvall, binary_duvall = leer_glb(archivo_origen)
        
        # Analizar estructura
        analisis = analizar_estructura_completa(gltf_ref, gltf_duvall)
        
        # Mostrar análisis detallado
        mostrar_analisis_detallado(analisis)
        
        # Aplicar correcciones
        modificaciones = aplicar_correcciones_mejoradas(gltf_ref, gltf_duvall, analisis)
        
        # Guardar modelo corregido
        print(f"\n💾 Guardando modelo corregido...")
        escribir_glb(archivo_destino, gltf_duvall, binary_duvall)
        
        print("\n" + "=" * 80)
        print("✅ PROCESO COMPLETADO")
        print("=" * 80)
        print(f"\n📁 Archivo guardado en:")
        print(f"   {archivo_destino}")
        print(f"\n📊 Estadísticas:")
        print(f"   • Total de correcciones aplicadas: {len(modificaciones)}")
        print(f"   • Diferencias en escala: {analisis['resumen']['diferencias_scale']}")
        print(f"   • Diferencias en posición: {analisis['resumen']['diferencias_translation']}")
        print(f"   • Diferencias en rotación: {analisis['resumen']['diferencias_rotation']}")
        
        if analisis['huesos_problematicos']:
            print(f"\n⚠️  Huesos que requerían más atención: {len(analisis['huesos_problematicos'])}")
            for hueso in analisis['huesos_problematicos'][:5]:  # Mostrar top 5
                print(f"   • {hueso['nombre']}: diferencia de {hueso['magnitud_total']:.6f}")
        
        print("\n" + "=" * 80)
        print("SIGUIENTE PASO:")
        print("=" * 80)
        print("\n1. Visualiza el archivo corregido y compáralo con la referencia")
        print("2. Verifica especialmente los hombros, cuello y cabeza")
        print("3. Si está correcto, confirma para aplicar a todos los modelos")
        
    except Exception as e:
        print(f"\n❌ Error durante el proceso: {str(e)}")
        import traceback
        traceback.print_exc()
