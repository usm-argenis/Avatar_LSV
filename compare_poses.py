import bpy
from pathlib import Path
from mathutils import Vector

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall")
ORIGINAL = BASE_DIR / "Duvall.glb"
TPOSE = BASE_DIR / "Duvall_TPose.glb"

def analyze_file(filepath, label):
    print(f"\n{'='*60}")
    print(f"ANALIZANDO: {label}")
    print(f"Archivo: {filepath}")
    print(f"{'='*60}")
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Cargar archivo
    bpy.ops.import_scene.gltf(filepath=str(filepath))
    
    # Buscar armature
    armature = None
    meshes = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
        elif obj.type == 'MESH':
            meshes.append(obj)
    
    if not armature:
        print("❌ No hay armature")
        return
    
    # Analizar en modo EDIT (rest pose real)
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='EDIT')
    
    print(f"\n📐 REST POSE DE LOS HUESOS:")
    arm_data = {}
    
    for bone_name in ['LeftArm', 'RightArm', 'LeftForeArm', 'RightForeArm']:
        if bone_name in armature.data.edit_bones:
            bone = armature.data.edit_bones[bone_name]
            direction = (bone.tail - bone.head).normalized()
            
            arm_data[bone_name] = {
                'head': bone.head.copy(),
                'tail': bone.tail.copy(),
                'direction': direction
            }
            
            print(f"\n{bone_name}:")
            print(f"  Head: ({bone.head.x:.3f}, {bone.head.y:.3f}, {bone.head.z:.3f})")
            print(f"  Tail: ({bone.tail.x:.3f}, {bone.tail.y:.3f}, {bone.tail.z:.3f})")
            print(f"  Direction: ({direction.x:.3f}, {direction.y:.3f}, {direction.z:.3f})")
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Analizar meshes
    print(f"\n📦 MESHES:")
    print(f"  Total meshes: {len(meshes)}")
    
    # Buscar mesh del cuerpo
    body_mesh = None
    for mesh in meshes:
        if 'Body' in mesh.name:
            body_mesh = mesh
            break
    
    if body_mesh:
        bbox = [body_mesh.matrix_world @ Vector(corner) for corner in body_mesh.bound_box]
        min_x = min(v.x for v in bbox)
        max_x = max(v.x for v in bbox)
        width = max_x - min_x
        
        print(f"\n  Body mesh: '{body_mesh.name}'")
        print(f"  BBox X: {min_x:.3f} to {max_x:.3f}")
        print(f"  Ancho total: {width:.3f}")
    
    return arm_data

# Analizar ambos archivos
print("\n" + "="*80)
print("COMPARACIÓN DE ARCHIVOS")
print("="*80)

original_data = analyze_file(ORIGINAL, "ORIGINAL (Pose A)")
tpose_data = analyze_file(TPOSE, "T-POSE (Nuevo)")

# Comparar
if original_data and tpose_data:
    print(f"\n{'='*60}")
    print("COMPARACIÓN DE DIRECCIONES")
    print(f"{'='*60}")
    
    for bone_name in ['LeftArm', 'RightArm']:
        if bone_name in original_data and bone_name in tpose_data:
            orig = original_data[bone_name]['direction']
            new = tpose_data[bone_name]['direction']
            
            print(f"\n{bone_name}:")
            print(f"  Original:  ({orig.x:6.3f}, {orig.y:6.3f}, {orig.z:6.3f})")
            print(f"  T-Pose:    ({new.x:6.3f}, {new.y:6.3f}, {new.z:6.3f})")
            print(f"  Cambio X:  {new.x - orig.x:+.3f}")
            print(f"  Cambio Y:  {new.y - orig.y:+.3f}")
            print(f"  Cambio Z:  {new.z - orig.z:+.3f}")

print("\n" + "="*80)
print("ANÁLISIS COMPLETO")
print("="*80)
