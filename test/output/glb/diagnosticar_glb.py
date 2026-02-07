"""
Script de diagnóstico: Analiza Remy_Alegria_Final.glb
======================================================

Importa el GLB generado y verifica:
- Objetos presentes
- Relación parent mesh-armature
- Modificadores armature
- Vertex groups
- Escalas relativas
- Shape keys activos
"""

import bpy
import os

GLB_PATH = r"C:\output\Remy_Alegria_Final.glb"

def diagnosticar():
    print("\n" + "="*70)
    print("DIAGNÓSTICO: Remy_Alegria_Final.glb")
    print("="*70)
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Importar GLB
    print(f"\nImportando: {GLB_PATH}")
    bpy.ops.import_scene.gltf(filepath=GLB_PATH)
    
    # Analizar objetos
    print("\n[1] OBJETOS EN LA ESCENA:")
    meshes = [o for o in bpy.data.objects if o.type == 'MESH']
    armatures = [o for o in bpy.data.objects if o.type == 'ARMATURE']
    
    print(f"  Meshes: {len(meshes)}")
    for m in meshes:
        print(f"    - {m.name}")
    
    print(f"  Armatures: {len(armatures)}")
    for a in armatures:
        print(f"    - {a.name} ({len(a.data.bones)} huesos)")
    
    if not meshes or not armatures:
        print("\n❌ ERROR: Falta mesh o armature")
        return
    
    mesh = meshes[0]
    armature = armatures[0]
    
    # Verificar parent
    print("\n[2] RELACIÓN PARENT:")
    if mesh.parent:
        print(f"  ✓ Mesh.parent = {mesh.parent.name}")
    else:
        print(f"  ✗ Mesh NO tiene parent")
    
    # Verificar modificadores
    print("\n[3] MODIFICADORES DEL MESH:")
    if len(mesh.modifiers) == 0:
        print(f"  ✗ NO hay modificadores")
    else:
        for mod in mesh.modifiers:
            print(f"  - {mod.type}: {mod.name}")
            if mod.type == 'ARMATURE':
                print(f"    Object: {mod.object.name if mod.object else 'None'}")
    
    # Verificar vertex groups
    print("\n[4] VERTEX GROUPS:")
    print(f"  Total: {len(mesh.vertex_groups)}")
    if len(mesh.vertex_groups) > 0:
        print(f"  Primeros 5:")
        for vg in list(mesh.vertex_groups)[:5]:
            print(f"    - {vg.name}")
    else:
        print(f"  ✗ NO hay vertex groups (skinning no aplicado)")
    
    # Verificar escalas
    print("\n[5] ESCALAS:")
    print(f"  Mesh scale: {mesh.scale}")
    print(f"  Armature scale: {armature.scale}")
    
    # Dimensiones
    print("\n[6] DIMENSIONES:")
    mesh_bbox = mesh.bound_box
    mesh_height = max([v[2] for v in mesh_bbox]) - min([v[2] for v in mesh_bbox])
    print(f"  Mesh altura: {mesh_height:.2f}")
    
    # Buscar huesos Head y Hips
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='EDIT')
    bones = armature.data.edit_bones
    
    head_bone = next((b for b in bones if 'head' in b.name.lower()), None)
    hips_bone = next((b for b in bones if 'hips' in b.name.lower()), None)
    
    if head_bone and hips_bone:
        arm_height = head_bone.tail.z - hips_bone.head.z
        print(f"  Armature altura (Hips->Head): {arm_height:.2f}")
        print(f"  Proporción Mesh/Armature: {mesh_height/arm_height:.2f}")
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Shape keys
    print("\n[7] SHAPE KEYS:")
    if mesh.data.shape_keys:
        keys = mesh.data.shape_keys.key_blocks
        print(f"  Total: {len(keys)}")
        print(f"  Activos (value > 0):")
        active = [k for k in keys if k.value > 0.01]
        if active:
            for k in active:
                print(f"    - {k.name}: {k.value:.2f}")
        else:
            print(f"    ✗ Ninguno activo")
    else:
        print(f"  ✗ NO hay shape keys")
    
    # RESUMEN
    print("\n" + "="*70)
    print("RESUMEN:")
    
    issues = []
    if not mesh.parent:
        issues.append("Mesh no tiene parent (armature)")
    if len(mesh.modifiers) == 0:
        issues.append("Mesh no tiene modificador Armature")
    if len(mesh.vertex_groups) == 0:
        issues.append("NO hay vertex groups (skinning faltante)")
    
    if issues:
        print("❌ PROBLEMAS ENCONTRADOS:")
        for i in issues:
            print(f"  - {i}")
    else:
        print("✅ Todo parece correcto estructuralmente")
    
    print("="*70)

if __name__ == '__main__':
    diagnosticar()
