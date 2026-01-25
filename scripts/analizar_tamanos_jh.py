import bpy
import sys
from pathlib import Path

print("\n" + "="*70)
print("ANÁLISIS DE TAMAÑOS: ESQUELETO vs MALLA")
print("="*70)

# ========== ANÁLISIS 1: JH_resultado_b (esqueleto con animación) ==========
bpy.ops.wm.read_homefile(use_empty=True)

esqueleto_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\JH_resultado_b.fbx"
print(f"\n📊 ARCHIVO 1: {Path(esqueleto_path).name}")
bpy.ops.import_scene.fbx(filepath=esqueleto_path)

for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        print(f"\n  🦴 Armature: {obj.name}")
        print(f"     Escala: {obj.scale}")
        
        # Buscar Hips
        for bone in obj.pose.bones:
            if "Hips" in bone.name:
                pos = obj.matrix_world @ bone.head
                print(f"     Hips: {bone.name}")
                print(f"     Posición Z: {pos.z:.6f}")
                break
                
    elif obj.type == 'MESH':
        print(f"\n  📦 Mesh: {obj.name}")
        print(f"     Escala: {obj.scale}")
        print(f"     Vértices: {len(obj.data.vertices)}")
        
        # Calcular bounding box
        bbox = [obj.matrix_world @ v.co for v in obj.data.vertices]
        min_z = min(v.z for v in bbox)
        max_z = max(v.z for v in bbox)
        altura = max_z - min_z
        
        print(f"     Altura del mesh: {altura:.6f}")
        print(f"     Min Z: {min_z:.6f}, Max Z: {max_z:.6f}")

# ========== ANÁLISIS 2: JH_malla (solo malla) ==========
bpy.ops.wm.read_homefile(use_empty=True)

malla_path = r"C:\Users\andre\OneDrive\Documentos\tesis\deploy-viewer-temp\output\JH_malla.fbx"
print(f"\n\n📊 ARCHIVO 2: {Path(malla_path).name}")
bpy.ops.import_scene.fbx(filepath=malla_path)

for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        print(f"\n  🦴 Armature: {obj.name}")
        print(f"     Escala: {obj.scale}")
        
        # Buscar Hips
        for bone in obj.pose.bones:
            if "Hips" in bone.name:
                pos = obj.matrix_world @ bone.head
                print(f"     Hips: {bone.name}")
                print(f"     Posición Z: {pos.z:.6f}")
                break
                
    elif obj.type == 'MESH':
        print(f"\n  📦 Mesh: {obj.name}")
        print(f"     Escala: {obj.scale}")
        print(f"     Vértices: {len(obj.data.vertices)}")
        
        # Calcular bounding box
        bbox = [obj.matrix_world @ v.co for v in obj.data.vertices]
        min_z = min(v.z for v in bbox)
        max_z = max(v.z for v in bbox)
        altura = max_z - min_z
        
        print(f"     Altura del mesh: {altura:.6f}")
        print(f"     Min Z: {min_z:.6f}, Max Z: {max_z:.6f}")

print("\n" + "="*70)
print("CONCLUSIÓN:")
print("  Compara las alturas de los meshes y las posiciones de Hips")
print("  La diferencia indica cuánto hay que escalar la malla")
print("="*70)
