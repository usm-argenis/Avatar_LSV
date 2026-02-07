#!/usr/bin/env blender --python
"""
Verificar transformaciones de los archivos de Duvall procesados
"""
import bpy
import sys
from pathlib import Path

archivos = [
    Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb"),
    Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_amar.glb"),  # Referencia
    Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\alfabeto\Duvall_resultado_a.glb")  # Referencia
]

print(f"\n{'='*80}")
print("VERIFICACIÓN DE TRANSFORMACIONES - DUVALL")
print(f"{'='*80}\n")

for archivo in archivos:
    if not archivo.exists():
        print(f"⚠️  No existe: {archivo.name}\n")
        continue
    
    print(f"📂 {archivo.name}")
    print(f"{'='*80}")
    
    # Limpiar y cargar
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(archivo))
    
    # Buscar armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if armature:
        print(f"🦴 Armature: {armature.name}")
        print(f"   Location: ({armature.location.x:.4f}, {armature.location.y:.4f}, {armature.location.z:.4f})")
        print(f"   Rotation (euler): ({armature.rotation_euler.x:.4f}, {armature.rotation_euler.y:.4f}, {armature.rotation_euler.z:.4f})")
        print(f"   Rotation (quat): ({armature.rotation_quaternion.x:.4f}, {armature.rotation_quaternion.y:.4f}, {armature.rotation_quaternion.z:.4f}, {armature.rotation_quaternion.w:.4f})")
        print(f"   Scale: ({armature.scale.x:.4f}, {armature.scale.y:.4f}, {armature.scale.z:.4f})")
        
        # Verificar problemas
        import math
        rot_quat = armature.rotation_quaternion
        scale = armature.scale
        
        problemas = []
        
        # Verificar rotación problemática (-0.7071, 0, 0, 0.7071) o (1, 0, 0, 0)
        if abs(rot_quat.x + 0.7071) < 0.01 and abs(rot_quat.w - 0.7071) < 0.01:
            problemas.append("⚠️ Rotación -90° detectada")
        elif abs(rot_quat.x - 1.0) < 0.01 and abs(rot_quat.w - 0.0) < 0.01:
            problemas.append("⚠️ Rotación 180° detectada")
        
        # Verificar escala problemática (100)
        if abs(scale.x - 100) < 1:
            problemas.append("⚠️ Escala 100x detectada")
        
        if problemas:
            print(f"\n❌ PROBLEMAS:")
            for p in problemas:
                print(f"   {p}")
        else:
            print(f"\n✅ Transformaciones correctas")
    else:
        print(f"❌ No se encontró Armature")
    
    print()

print(f"{'='*80}\n")
sys.exit(0)
