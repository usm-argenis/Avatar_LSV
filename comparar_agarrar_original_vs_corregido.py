#!/usr/bin/env blender --python
"""
Comparar agarrar ORIGINAL vs archivos de referencia
"""
import bpy
import sys
from pathlib import Path

archivos = [
    (Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb.backup_FINAL"), "AGARRAR ORIGINAL (backup)"),
    (Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.glb"), "AGARRAR CORREGIDO"),
    (Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_amar.glb"), "AMAR (referencia)"),
]

print(f"\n{'='*80}")
print("COMPARACIÓN: AGARRAR ORIGINAL vs CORREGIDO vs REFERENCIA")
print(f"{'='*80}\n")

for archivo, descripcion in archivos:
    if not archivo.exists():
        print(f"⚠️  No existe: {descripcion}\n")
        continue
    
    print(f"📂 {descripcion}")
    print(f"   Archivo: {archivo.name}")
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
        print(f"   Rotation (quat): ({armature.rotation_quaternion.x:.4f}, {armature.rotation_quaternion.y:.4f}, {armature.rotation_quaternion.z:.4f}, {armature.rotation_quaternion.w:.4f})")
        print(f"   Scale: ({armature.scale.x:.4f}, {armature.scale.y:.4f}, {armature.scale.z:.4f})")
        
        import math
        # Convertir quaternion a ángulo
        rot_quat = armature.rotation_quaternion
        angle = 2 * math.acos(rot_quat.w)
        angle_deg = math.degrees(angle)
        
        if abs(rot_quat.x) > 0.1:
            axis = "X"
            if rot_quat.x < 0:
                angle_deg = -angle_deg
        elif abs(rot_quat.y) > 0.1:
            axis = "Y"
        elif abs(rot_quat.z) > 0.1:
            axis = "Z"
        else:
            axis = "None"
            angle_deg = 0
        
        print(f"   Rotación: {angle_deg:.1f}° alrededor de {axis}")
        
    else:
        print(f"❌ No se encontró Armature")
    
    print()

print(f"{'='*80}")
print("💡 CONCLUSIÓN:")
print(f"{'='*80}")
print("Si AGARRAR CORREGIDO se ve bien pero los demás se ven volteados,")
print("entonces TODOS los demás archivos necesitan la MISMA corrección")
print("que aplicamos a agarrar (aplicar transformaciones del armature).")
print(f"{'='*80}\n")

sys.exit(0)
