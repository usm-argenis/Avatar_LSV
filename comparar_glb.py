#!/usr/bin/env python3
"""
Compara dos archivos GLB y muestra las diferencias clave
"""
import json
import struct
from pathlib import Path
import math

def leer_glb(ruta_glb):
    """Lee un archivo GLB y retorna el JSON"""
    with open(ruta_glb, 'rb') as f:
        magic = f.read(4)
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        chunk_length = struct.unpack('<I', f.read(4))[0]
        chunk_type = f.read(4)
        json_data = f.read(chunk_length).decode('utf-8')
        
        return json.loads(json_data)

def quaternion_to_euler(q):
    """Convierte quaternion a euler en grados"""
    x, y, z, w = q
    
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = math.atan2(sinr_cosp, cosr_cosp)
    
    sinp = 2 * (w * y - z * x)
    if abs(sinp) >= 1:
        pitch = math.copysign(math.pi / 2, sinp)
    else:
        pitch = math.asin(sinp)
    
    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = math.atan2(siny_cosp, cosy_cosp)
    
    return (math.degrees(roll), math.degrees(pitch), math.degrees(yaw))

def comparar_nodos(gltf1, gltf2, nombre1, nombre2):
    """Compara los nodos de dos GLB"""
    print(f"\n{'='*80}")
    print(f"🔍 COMPARANDO NODOS")
    print(f"{'='*80}\n")
    
    nodes1 = gltf1.get('nodes', [])
    nodes2 = gltf2.get('nodes', [])
    
    print(f"Total nodos: {nombre1}={len(nodes1)}, {nombre2}={len(nodes2)}\n")
    
    # Comparar primeros 10 nodos (los más importantes)
    max_compare = min(15, len(nodes1), len(nodes2))
    
    diferencias = []
    
    for i in range(max_compare):
        node1 = nodes1[i]
        node2 = nodes2[i]
        
        name1 = node1.get('name', f'Node_{i}')
        name2 = node2.get('name', f'Node_{i}')
        
        print(f"\n{'─'*80}")
        print(f"Node {i}: {name1} vs {name2}")
        print(f"{'─'*80}")
        
        # Comparar rotación
        rot1 = node1.get('rotation')
        rot2 = node2.get('rotation')
        
        if rot1 or rot2:
            if rot1 and rot2:
                euler1 = quaternion_to_euler(rot1)
                euler2 = quaternion_to_euler(rot2)
                
                print(f"\n📐 ROTACIÓN:")
                print(f"  {nombre1}: quat={rot1}")
                print(f"            euler=({euler1[0]:.1f}°, {euler1[1]:.1f}°, {euler1[2]:.1f}°)")
                print(f"  {nombre2}: quat={rot2}")
                print(f"            euler=({euler2[0]:.1f}°, {euler2[1]:.1f}°, {euler2[2]:.1f}°)")
                
                # Detectar diferencias significativas
                diff_x = abs(euler1[0] - euler2[0])
                diff_y = abs(euler1[1] - euler2[1])
                diff_z = abs(euler1[2] - euler2[2])
                
                if diff_x > 5 or diff_y > 5 or diff_z > 5:
                    print(f"  ⚠️ DIFERENCIA: ΔX={diff_x:.1f}°, ΔY={diff_y:.1f}°, ΔZ={diff_z:.1f}°")
                    diferencias.append({
                        'nodo': i,
                        'nombre': name1,
                        'tipo': 'rotacion',
                        'archivo1': rot1,
                        'archivo2': rot2,
                        'euler1': euler1,
                        'euler2': euler2
                    })
            else:
                print(f"\n📐 ROTACIÓN:")
                print(f"  {nombre1}: {rot1}")
                print(f"  {nombre2}: {rot2}")
                print(f"  ⚠️ Uno tiene rotación y el otro no")
        
        # Comparar escala
        scale1 = node1.get('scale')
        scale2 = node2.get('scale')
        
        if scale1 or scale2:
            if scale1 and scale2:
                print(f"\n📏 ESCALA:")
                print(f"  {nombre1}: [{scale1[0]:.2f}, {scale1[1]:.2f}, {scale1[2]:.2f}]")
                print(f"  {nombre2}: [{scale2[0]:.2f}, {scale2[1]:.2f}, {scale2[2]:.2f}]")
                
                diff_scale = abs(scale1[0] - scale2[0])
                if diff_scale > 0.1:
                    print(f"  ⚠️ DIFERENCIA DE ESCALA: Δ={diff_scale:.2f}")
                    diferencias.append({
                        'nodo': i,
                        'nombre': name1,
                        'tipo': 'escala',
                        'archivo1': scale1,
                        'archivo2': scale2
                    })
            else:
                print(f"\n📏 ESCALA:")
                print(f"  {nombre1}: {scale1}")
                print(f"  {nombre2}: {scale2}")
    
    return diferencias

def generar_solucion(diferencias, archivo_problema, archivo_bueno):
    """Genera código para corregir el archivo problemático"""
    print(f"\n{'='*80}")
    print(f"💡 SOLUCIÓN")
    print(f"{'='*80}\n")
    
    if not diferencias:
        print("✅ No se encontraron diferencias significativas")
        return
    
    print(f"Se encontraron {len(diferencias)} diferencias:\n")
    
    for diff in diferencias:
        print(f"Node {diff['nodo']} ({diff['nombre']}) - {diff['tipo']}:")
        if diff['tipo'] == 'rotacion':
            print(f"  Cambiar de: {diff['archivo1']}")
            print(f"  Cambiar a:  {diff['archivo2']}")
            print(f"  (Euler: {diff['euler1']} → {diff['euler2']})")
        else:
            print(f"  Cambiar de: {diff['archivo1']}")
            print(f"  Cambiar a:  {diff['archivo2']}")
        print()
    
    print("\n🔧 Aplicar correcciones automáticamente? (s/n): ", end='')

if __name__ == "__main__":
    archivo1 = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")
    archivo2 = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\alfabeto\Duvall_resultado_a.glb")
    
    print(f"\n{'='*80}")
    print(f"📊 COMPARACIÓN DE ARCHIVOS GLB")
    print(f"{'='*80}")
    print(f"\n📁 Archivo 1 (PROBLEMA): {archivo1.name}")
    print(f"📁 Archivo 2 (REFERENCIA): {archivo2.name}")
    
    if not archivo1.exists():
        print(f"\n❌ No existe: {archivo1}")
        exit(1)
    
    if not archivo2.exists():
        print(f"\n❌ No existe: {archivo2}")
        exit(1)
    
    print(f"\n📦 Cargando archivos...")
    gltf1 = leer_glb(archivo1)
    gltf2 = leer_glb(archivo2)
    
    print(f"✅ Archivos cargados\n")
    print(f"Tamaño: {archivo1.stat().st_size / 1024:.2f} KB vs {archivo2.stat().st_size / 1024:.2f} KB")
    
    diferencias = comparar_nodos(gltf1, gltf2, archivo1.stem, archivo2.stem)
    generar_solucion(diferencias, archivo1, archivo2)
