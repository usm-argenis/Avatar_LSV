"""
SOLUCIÓN FINAL: Remy con sonrisa APLICADA (baked)
==================================================

Estrategia:
En lugar de exportar shape keys (que se pierden), aplicamos
la deformación directamente a la geometría y exportamos el
resultado como mesh estático con sonrisa.

Resultado: GLB con Remy sonriendo permanentemente.
"""

import bpy
import os

REMY_FBX = r"C:\Users\andre\OneDrive\Documentos\tesis\avatars\Remy.fbx"
OUTPUT_GLB = r"C:\output\Remy_Sonriendo.glb"
os.makedirs(os.path.dirname(OUTPUT_GLB), exist_ok=True)

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def main():
    print("\n" + "="*70)
    print("REMY CON SONRISA PERMANENTE (GEOMETRÍA APLICADA)")
    print("="*70)
    
    clear_scene()
    
    # Paso 1: Importar Remy completo
    print("\n[1/3] Importando Remy.fbx...")
    if not os.path.exists(REMY_FBX):
        print(f"  ✗ No encontrado: {REMY_FBX}")
        return
    
    bpy.ops.import_scene.fbx(filepath=REMY_FBX)
    
    # Obtener objetos
    meshes = [o for o in bpy.data.objects if o.type == 'MESH']
    armature = next((o for o in bpy.data.objects if o.type == 'ARMATURE'), None)
    
    print(f"  ✓ Importado: {len(meshes)} meshes, armature: {armature.name if armature else 'None'}")
    
    # Paso 2: Unir meshes
    print("\n[2/3] Uniendo meshes...")
    bpy.ops.object.select_all(action='DESELECT')
    for m in meshes:
        m.select_set(True)
    
    bpy.context.view_layer.objects.active = meshes[0]
    bpy.ops.object.join()
    
    mesh = bpy.context.active_object
    mesh.name = 'Remy_Smiling'
    print(f"  ✓ Mesh unificado: {mesh.name}")
    
    # Paso 2.5: Deformar vertices para crear sonrisa
    print("\n[2.5/3] Aplicando deformación de sonrisa...")
    
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Obtener dimensiones
    bbox = mesh.bound_box
    max_z = max([v[2] for v in bbox])
    min_z = min([v[2] for v in bbox])
    height = max_z - min_z
    
    # Zona de boca (aproximadamente 80-85% de altura)
    mouth_min = min_z + height * 0.78
    mouth_max = min_z + height * 0.86
    
    vertices_moved = 0
    
    for v in mesh.data.vertices:
        # Verificar si está en zona de boca
        if v.co.z > mouth_min and v.co.z < mouth_max:
            # Sonrisa: estirar comisuras hacia afuera y arriba
            if v.co.x > 0.02:  # Lado izquierdo
                v.co.x += v.co.x * 0.12
                v.co.z += 0.008
                vertices_moved += 1
            elif v.co.x < -0.02:  # Lado derecho
                v.co.x += v.co.x * 0.12
                v.co.z += 0.008
                vertices_moved += 1
        
        # Mejillas (zona más amplia)
        cheek_min = min_z + height * 0.75
        cheek_max = min_z + height * 0.88
        if v.co.z > cheek_min and v.co.z < cheek_max and abs(v.co.x) > 0.03:
            # Inflar ligeramente
            v.co.x += v.co.x * 0.06
            v.co.y += abs(v.co.x) * 0.03
    
    mesh.data.update()
    
    print(f"  ✓ {vertices_moved} vértices deformados")
    
    # Paso 3: Exportar GLB
    print("\n[3/3] Exportando GLB...")
    print(f"  Destino: {OUTPUT_GLB}")
    
    # Verificar estado antes de exportar
    print(f"\n  Estado del mesh:")
    print(f"    - Vértices: {len(mesh.data.vertices)}")
    print(f"    - Parent: {mesh.parent.name if mesh.parent else 'None'}")
    print(f"    - Vertex groups: {len(mesh.vertex_groups)}")
    
    # Exportar con configuración que preserve skinning
    bpy.ops.export_scene.gltf(
        filepath=OUTPUT_GLB,
        export_format='GLB',
        use_selection=False,
        export_apply=False,
        export_animations=True,
        export_morph=False,  # No morph targets (ya aplicamos la deformación)
        export_skins=True,
        export_all_influences=True,
        export_def_bones=True
    )
    
    if os.path.exists(OUTPUT_GLB):
        size_mb = os.path.getsize(OUTPUT_GLB) / (1024*1024)
        print(f"\n  ✓ Exportado: {size_mb:.2f} MB")
        
        print("\n" + "="*70)
        print("✅ PROCESO COMPLETADO")
        print(f"Archivo: {OUTPUT_GLB}")
        print("\nCaracterísticas:")
        print("  • Remy con sonrisa PERMANENTE (geometría deformada)")
        print("  • Armature original preservado")
        print("  • Listo para usar en Three.js/navegador")
        print("="*70)
    else:
        print("\n  ✗ Error en exportación")

if __name__ == '__main__':
    main()
