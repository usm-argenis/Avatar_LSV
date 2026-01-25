"""
Script FINAL simplificado: Remy con emoción alegría
====================================================

Estrategia NUEVA (más simple):
1. Importa Remy.fbx COMPLETO (con su armature original)
2. Une todos los meshes en uno solo
3. Agrega shape keys ARKit al mesh unificado
4. Activa emoción ALEGRÍA
5. Exporta a GLB (preserva el armature original de Remy)

NO crea armature nuevo - usa el de Remy que ya tiene skinning correcto.
"""

import bpy
import os
from mathutils import Vector

# Configuración
REMY_FBX = r"C:\Users\andre\OneDrive\Documentos\tesis\avatars\Remy.fbx"
OUTPUT_GLB = r"C:\output\Remy_Alegria_FINAL.glb"
os.makedirs(os.path.dirname(OUTPUT_GLB), exist_ok=True)

# Shape keys para alegría
SMILE_SHAPES = ['mouthSmile_L', 'mouthSmile_R', 'cheekPuff']

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def import_and_prepare_remy():
    """Importa Remy y une meshes, conserva armature original"""
    print("\n[1/4] Importando Remy.fbx...")
    
    if not os.path.exists(REMY_FBX):
        raise FileNotFoundError(f"Remy.fbx no encontrado: {REMY_FBX}")
    
    bpy.ops.import_scene.fbx(filepath=REMY_FBX)
    
    # Obtener meshes y armature
    meshes = [o for o in bpy.data.objects if o.type == 'MESH']
    armature = next((o for o in bpy.data.objects if o.type == 'ARMATURE'), None)
    
    print(f"  Meshes: {len(meshes)}, Armature: {'Sí' if armature else 'No'}")
    
    if not meshes or not armature:
        raise Exception("Remy incompleto")
    
    # Unir meshes
    print(f"  Uniendo {len(meshes)} meshes...")
    bpy.ops.object.select_all(action='DESELECT')
    for m in meshes:
        m.select_set(True)
    
    bpy.context.view_layer.objects.active = meshes[0]
    bpy.ops.object.join()
    
    unified = bpy.context.active_object
    unified.name = 'Remy_Body'
    
    print(f"  ✓ Mesh unificado: {unified.name}")
    print(f"  ✓ Armature: {armature.name} ({len(armature.data.bones)} huesos)")
    
    return unified, armature

def add_simple_shapekeys(mesh):
    """Agrega shape keys básicos para sonrisa"""
    print("\n[2/4] Creando shape keys para sonrisa...")
    
    if not mesh.data.shape_keys:
        mesh.shape_key_add(name='Basis')
    
    # Obtener dimensiones de la cabeza
    bbox = mesh.bound_box
    max_z = max([v[2] for v in bbox])
    min_z = min([v[2] for v in bbox])
    height = max_z - min_z
    
    # Zona de cabeza (75% superior)
    head_threshold = min_z + height * 0.70
    mouth_zone_z = min_z + height * 0.82
    
    # Sonrisa izquierda
    sk_smile_l = mesh.shape_key_add(name='mouthSmile_L')
    for i, v in enumerate(mesh.data.vertices):
        co = v.co.copy()
        if co.z > head_threshold and co.z < mouth_zone_z and co.x > 0.02:
            # Estirar hacia afuera y arriba (sonrisa)
            delta = Vector((co.x * 0.15, 0, 0.01))
            sk_smile_l.data[i].co = co + delta
        else:
            sk_smile_l.data[i].co = co
    
    # Sonrisa derecha
    sk_smile_r = mesh.shape_key_add(name='mouthSmile_R')
    for i, v in enumerate(mesh.data.vertices):
        co = v.co.copy()
        if co.z > head_threshold and co.z < mouth_zone_z and co.x < -0.02:
            delta = Vector((co.x * 0.15, 0, 0.01))
            sk_smile_r.data[i].co = co + delta
        else:
            sk_smile_r.data[i].co = co
    
    # Mejillas infladas
    sk_cheek = mesh.shape_key_add(name='cheekPuff')
    cheek_zone_z_min = min_z + height * 0.76
    cheek_zone_z_max = min_z + height * 0.88
    for i, v in enumerate(mesh.data.vertices):
        co = v.co.copy()
        if co.z > cheek_zone_z_min and co.z < cheek_zone_z_max and abs(co.x) > 0.03:
            delta = Vector((co.x * 0.10, abs(co.x) * 0.05, 0))
            sk_cheek.data[i].co = co + delta
        else:
            sk_cheek.data[i].co = co
    
    print(f"  ✓ 3 shape keys creados: mouthSmile_L, mouthSmile_R, cheekPuff")
    
    return True

def activate_smile(mesh):
    """Activa los shape keys de sonrisa al 100%"""
    print("\n[3/4] Activando sonrisa...")
    
    if not mesh.data.shape_keys:
        print("  ✗ No hay shape keys")
        return False
    
    keys = mesh.data.shape_keys.key_blocks
    
    for name in SMILE_SHAPES:
        if name in keys:
            keys[name].value = 1.0
            print(f"  ✓ {name} = 1.0")
        else:
            print(f"  ✗ {name} no encontrado")
    
    # Force update
    bpy.context.view_layer.update()
    
    return True

def export_glb(filepath):
    """Exporta con configuración optimizada"""
    print(f"\n[4/4] Exportando GLB...")
    print(f"  Destino: {filepath}")
    
    bpy.ops.export_scene.gltf(
        filepath=filepath,
        export_format='GLB',
        use_selection=False,
        export_apply=False,
        export_animations=True,
        export_morph=True,
        export_skins=True,
        export_all_influences=True,
        export_def_bones=True,
        export_current_frame=True
    )
    
    if os.path.exists(filepath):
        size_mb = os.path.getsize(filepath) / (1024*1024)
        print(f"  ✓ Exportado: {size_mb:.2f} MB")
        return True
    else:
        print(f"  ✗ Error")
        return False

def main():
    print("\n" + "="*70)
    print("REMY CON SONRISA - VERSIÓN SIMPLIFICADA")
    print("="*70)
    
    try:
        clear_scene()
        
        # Paso 1: Importar y preparar
        mesh, armature = import_and_prepare_remy()
        
        # Paso 2: Shape keys
        add_simple_shapekeys(mesh)
        
        # Paso 3: Activar sonrisa
        activate_smile(mesh)
        
        # Paso 4: Exportar
        success = export_glb(OUTPUT_GLB)
        
        print("\n" + "="*70)
        if success:
            print("✅ COMPLETADO")
            print(f"Archivo: {OUTPUT_GLB}")
            print("\nEl GLB contiene:")
            print("  • Armature original de Remy (con skinning)")
            print("  • Shape keys de sonrisa ACTIVADOS")
            print("  • Mesh unificado")
        else:
            print("❌ ERROR EN EXPORTACIÓN")
        print("="*70)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
