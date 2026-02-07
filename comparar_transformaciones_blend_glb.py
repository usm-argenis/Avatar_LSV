#!/usr/bin/env blender --python
"""
Comparar transformaciones entre agarrar.blend y amar.glb
"""
import bpy
import sys
from pathlib import Path
import mathutils

archivo_agarrar_blend = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_agarrar.blend")
archivo_amar_glb = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\verbos\Duvall_resultado_amar.glb")

print(f"\n{'='*80}")
print("COMPARACIÓN: agarrar.blend vs amar.glb")
print(f"{'='*80}\n")

# ========== AGARRAR.BLEND ==========
print("📂 Cargando agarrar.blend...")
bpy.ops.wm.open_mainfile(filepath=str(archivo_agarrar_blend))

agarrar_info = {
    'objetos': [],
    'armature': None
}

for obj in bpy.data.objects:
    info = {
        'nombre': obj.name,
        'tipo': obj.type,
        'location': obj.location.copy(),
        'rotation_euler': obj.rotation_euler.copy(),
        'rotation_quaternion': obj.rotation_quaternion.copy(),
        'scale': obj.scale.copy()
    }
    agarrar_info['objetos'].append(info)
    
    if obj.type == 'ARMATURE':
        agarrar_info['armature'] = info

print(f"✅ Objetos en agarrar.blend: {len(agarrar_info['objetos'])}")
if agarrar_info['armature']:
    arm = agarrar_info['armature']
    print(f"\n🦴 Armature en AGARRAR.BLEND:")
    print(f"   Nombre: {arm['nombre']}")
    print(f"   Location: ({arm['location'].x:.4f}, {arm['location'].y:.4f}, {arm['location'].z:.4f})")
    print(f"   Rotation (euler): ({arm['rotation_euler'].x:.4f}, {arm['rotation_euler'].y:.4f}, {arm['rotation_euler'].z:.4f})")
    print(f"   Rotation (quat): ({arm['rotation_quaternion'].x:.4f}, {arm['rotation_quaternion'].y:.4f}, {arm['rotation_quaternion'].z:.4f}, {arm['rotation_quaternion'].w:.4f})")
    print(f"   Scale: ({arm['scale'].x:.4f}, {arm['scale'].y:.4f}, {arm['scale'].z:.4f})")

# ========== AMAR.GLB ==========
print(f"\n📂 Cargando amar.glb...")
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(archivo_amar_glb))

amar_info = {
    'objetos': [],
    'armature': None
}

for obj in bpy.data.objects:
    info = {
        'nombre': obj.name,
        'tipo': obj.type,
        'location': obj.location.copy(),
        'rotation_euler': obj.rotation_euler.copy(),
        'rotation_quaternion': obj.rotation_quaternion.copy(),
        'scale': obj.scale.copy()
    }
    amar_info['objetos'].append(info)
    
    if obj.type == 'ARMATURE':
        amar_info['armature'] = info

print(f"✅ Objetos en amar.glb: {len(amar_info['objetos'])}")
if amar_info['armature']:
    arm = amar_info['armature']
    print(f"\n🦴 Armature en AMAR.GLB:")
    print(f"   Nombre: {arm['nombre']}")
    print(f"   Location: ({arm['location'].x:.4f}, {arm['location'].y:.4f}, {arm['location'].z:.4f})")
    print(f"   Rotation (euler): ({arm['rotation_euler'].x:.4f}, {arm['rotation_euler'].y:.4f}, {arm['rotation_euler'].z:.4f})")
    print(f"   Rotation (quat): ({arm['rotation_quaternion'].x:.4f}, {arm['rotation_quaternion'].y:.4f}, {arm['rotation_quaternion'].z:.4f}, {arm['rotation_quaternion'].w:.4f})")
    print(f"   Scale: ({arm['scale'].x:.4f}, {arm['scale'].y:.4f}, {arm['scale'].z:.4f})")

# ========== COMPARACIÓN ==========
print(f"\n{'='*80}")
print("🔍 DIFERENCIAS")
print(f"{'='*80}\n")

if agarrar_info['armature'] and amar_info['armature']:
    ag = agarrar_info['armature']
    am = amar_info['armature']
    
    diff_loc = (ag['location'] - am['location']).length
    diff_scale = (ag['scale'] - am['scale']).length
    
    print(f"📍 Location:")
    print(f"   Agarrar: ({ag['location'].x:.4f}, {ag['location'].y:.4f}, {ag['location'].z:.4f})")
    print(f"   Amar:    ({am['location'].x:.4f}, {am['location'].y:.4f}, {am['location'].z:.4f})")
    print(f"   Diferencia: {diff_loc:.4f}")
    
    print(f"\n📐 Rotation (euler):")
    print(f"   Agarrar: ({ag['rotation_euler'].x:.4f}, {ag['rotation_euler'].y:.4f}, {ag['rotation_euler'].z:.4f})")
    print(f"   Amar:    ({am['rotation_euler'].x:.4f}, {am['rotation_euler'].y:.4f}, {am['rotation_euler'].z:.4f})")
    
    print(f"\n📐 Rotation (quaternion):")
    print(f"   Agarrar: ({ag['rotation_quaternion'].x:.4f}, {ag['rotation_quaternion'].y:.4f}, {ag['rotation_quaternion'].z:.4f}, {ag['rotation_quaternion'].w:.4f})")
    print(f"   Amar:    ({am['rotation_quaternion'].x:.4f}, {am['rotation_quaternion'].y:.4f}, {am['rotation_quaternion'].z:.4f}, {am['rotation_quaternion'].w:.4f})")
    
    print(f"\n📏 Scale:")
    print(f"   Agarrar: ({ag['scale'].x:.4f}, {ag['scale'].y:.4f}, {ag['scale'].z:.4f})")
    print(f"   Amar:    ({am['scale'].x:.4f}, {am['scale'].y:.4f}, {am['scale'].z:.4f})")
    print(f"   Diferencia: {diff_scale:.4f}")
    
    # Detectar problemas
    print(f"\n{'='*80}")
    print("⚠️  PROBLEMAS DETECTADOS")
    print(f"{'='*80}\n")
    
    problemas = []
    
    if diff_loc > 0.001:
        problemas.append(f"❌ Location diferente: {diff_loc:.4f}")
    
    if diff_scale > 0.001:
        problemas.append(f"❌ Scale diferente: {diff_scale:.4f}")
    
    # Verificar rotación (convertir a ángulo)
    rot_diff = ag['rotation_quaternion'].rotation_difference(am['rotation_quaternion']).angle
    import math
    rot_diff_deg = math.degrees(rot_diff)
    if rot_diff > 0.01:
        problemas.append(f"❌ Rotation diferente: {rot_diff_deg:.2f}°")
    
    if problemas:
        for p in problemas:
            print(p)
        
        print(f"\n💡 SOLUCIÓN:")
        print(f"   El Armature de agarrar.blend debería tener:")
        print(f"   - Location: ({am['location'].x:.4f}, {am['location'].y:.4f}, {am['location'].z:.4f})")
        print(f"   - Rotation: ({am['rotation_euler'].x:.4f}, {am['rotation_euler'].y:.4f}, {am['rotation_euler'].z:.4f})")
        print(f"   - Scale: ({am['scale'].x:.4f}, {am['scale'].y:.4f}, {am['scale'].z:.4f})")
    else:
        print("✅ No hay diferencias significativas")

print(f"\n{'='*80}\n")
sys.exit(0)
