#!/usr/bin/env python3
"""
Diagnóstico completo de archivo GLB
Verifica orientación, escala, rotación y genera reporte detallado
"""
import json
import struct
from pathlib import Path
import math

def leer_glb(ruta_glb):
    """Lee un archivo GLB y retorna el JSON"""
    with open(ruta_glb, 'rb') as f:
        # Header
        magic = f.read(4)
        version = struct.unpack('<I', f.read(4))[0]
        length = struct.unpack('<I', f.read(4))[0]
        
        # Chunk JSON
        chunk_length = struct.unpack('<I', f.read(4))[0]
        chunk_type = f.read(4)
        json_data = f.read(chunk_length).decode('utf-8')
        
        return json.loads(json_data)

def quaternion_to_euler(q):
    """Convierte quaternion [x,y,z,w] a ángulos Euler en grados"""
    x, y, z, w = q
    
    # Roll (X)
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = math.atan2(sinr_cosp, cosr_cosp)
    
    # Pitch (Y)
    sinp = 2 * (w * y - z * x)
    if abs(sinp) >= 1:
        pitch = math.copysign(math.pi / 2, sinp)
    else:
        pitch = math.asin(sinp)
    
    # Yaw (Z)
    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = math.atan2(siny_cosp, cosy_cosp)
    
    return (math.degrees(roll), math.degrees(pitch), math.degrees(yaw))

def diagnosticar(ruta_glb):
    """Genera diagnóstico completo del GLB"""
    print(f"\n{'='*70}")
    print(f"🔬 DIAGNÓSTICO COMPLETO: {ruta_glb.name}")
    print(f"{'='*70}\n")
    
    gltf = leer_glb(ruta_glb)
    
    problemas = []
    
    # Analizar nodos críticos
    nodes = gltf.get('nodes', [])
    
    print("📊 ANÁLISIS DE NODOS CRÍTICOS:\n")
    
    for i, node in enumerate(nodes):
        nombre = node.get('name', f'Node_{i}')
        
        # Solo analizar nodos importantes
        if nombre not in ['RootNode', 'Armature'] and i > 10:
            continue
        
        print(f"Node {i}: {nombre}")
        
        # Rotación
        if 'rotation' in node:
            rot_quat = node['rotation']
            rot_euler = quaternion_to_euler(rot_quat)
            print(f"  Rotación (quaternion): [{rot_quat[0]:.4f}, {rot_quat[1]:.4f}, {rot_quat[2]:.4f}, {rot_quat[3]:.4f}]")
            print(f"  Rotación (euler): X={rot_euler[0]:.1f}°, Y={rot_euler[1]:.1f}°, Z={rot_euler[2]:.1f}°")
            
            # Detectar rotaciones problemáticas
            if abs(rot_euler[0]) > 80 and abs(rot_euler[0]) < 100:
                problemas.append(f"⚠️ {nombre}: Rotación X ~90° (modelo volteado)")
            elif abs(rot_euler[1]) > 170:
                problemas.append(f"⚠️ {nombre}: Rotación Y ~180° (modelo invertido)")
        
        # Escala
        if 'scale' in node:
            scale = node['scale']
            print(f"  Escala: [{scale[0]:.2f}, {scale[1]:.2f}, {scale[2]:.2f}]")
            
            if abs(scale[0] - 100) < 1:
                problemas.append(f"⚠️ {nombre}: Escala 100x (FBX import sin normalizar)")
            elif abs(scale[0]) < 0.01:
                problemas.append(f"⚠️ {nombre}: Escala muy pequeña")
            elif abs(scale[0]) > 10:
                problemas.append(f"⚠️ {nombre}: Escala muy grande")
        
        # Posición
        if 'translation' in node:
            pos = node['translation']
            print(f"  Posición: [{pos[0]:.4f}, {pos[1]:.4f}, {pos[2]:.4f}]")
        
        print()
    
    # Resumen
    print(f"\n{'='*70}")
    print("📋 RESUMEN DE PROBLEMAS DETECTADOS:")
    print(f"{'='*70}\n")
    
    if problemas:
        for problema in problemas:
            print(f"  {problema}")
    else:
        print("  ✅ No se detectaron problemas evidentes")
    
    print(f"\n{'='*70}")
    
    # Recomendaciones
    print("\n💡 RECOMENDACIONES:\n")
    
    tiene_rotacion_90 = any("90°" in p for p in problemas)
    tiene_escala_100 = any("100x" in p for p in problemas)
    
    if tiene_rotacion_90:
        print("  1. ❌ ROTACIÓN 90°: El modelo fue exportado con orientación incorrecta")
        print("     Solución: Aplicar rotación compensatoria en el viewer (-90° en X)")
        print()
    
    if tiene_escala_100:
        print("  2. ❌ ESCALA 100x: El modelo mantiene escala de FBX sin normalizar")
        print("     Solución: Normalizar escala a 1x en el GLB")
        print()
    
    if not tiene_rotacion_90 and not tiene_escala_100:
        print("  ✅ El GLB está correctamente normalizado")
        print("  ✅ Si aún se ve volteado, el problema está en el viewer")
    
    print(f"\n{'='*70}\n")

if __name__ == "__main__":
    archivo = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb")
    
    if archivo.exists():
        diagnosticar(archivo)
    else:
        print(f"❌ Archivo no encontrado: {archivo}")
