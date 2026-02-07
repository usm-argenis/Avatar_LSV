import bpy
import math
from pathlib import Path
from mathutils import Vector

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
DUVALL_INPUT = BASE_DIR / "test" / "output" / "glb" / "Duvall" / "Duvall.glb"
DUVALL_OUTPUT_FBX = BASE_DIR / "test" / "output" / "glb" / "Duvall" / "Duvall_TPose.fbx"
DUVALL_OUTPUT_GLB = BASE_DIR / "test" / "output" / "glb" / "Duvall" / "Duvall_TPose.glb"

def clear_scene():
    """Limpia la escena de Blender"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
def convert_to_tpose():
    """Convierte Duvall.glb de pose A a T-pose - MÉTODO CORRECTO"""
    print(f"🔍 Cargando {DUVALL_INPUT}")
    
    # Limpiar escena
    clear_scene()
    
    # Importar el GLB
    bpy.ops.import_scene.gltf(filepath=str(DUVALL_INPUT))
    
    # Buscar armature y meshes
    armature = None
    all_meshes = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
        elif obj.type == 'MESH':
            all_meshes.append(obj)
    
    if not armature:
        print("❌ No se encontró armature")
        return False
    
    print(f"✅ Armature: {armature.name}")
    print(f"📦 Meshes totales: {len(all_meshes)}")
    
    # VERIFICAR BOUNDING BOX ANTES
    body_mesh_before = None
    for mesh in all_meshes:
        if 'Body' in mesh.name:
            body_mesh_before = mesh
            break
    
    if body_mesh_before:
        bbox = [body_mesh_before.matrix_world @ Vector(corner) for corner in body_mesh_before.bound_box]
        width_before = max(v.x for v in bbox) - min(v.x for v in bbox)
        print(f"📏 Ancho ANTES: {width_before:.3f}")
    
    # Entrar en modo POSE
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    
    # Aplicar quaternions
    bone_quaternions = {
        'LeftArm': (0.862, -0.498, 0.096, -0.020),
        'LeftForeArm': (0.971, 0.100, 0.117, -0.184),
        'RightArm': (0.865, -0.491, -0.038, -0.099),
        'RightForeArm': (0.942, 0.124, -0.226, 0.213),
    }
    
    print("\n🦴 Aplicando rotaciones...")
    for bone_name, quat in bone_quaternions.items():
        if bone_name in armature.pose.bones:
            bone = armature.pose.bones[bone_name]
            bone.rotation_mode = 'QUATERNION'
            bone.rotation_quaternion = quat
            print(f"  ✅ {bone_name}")
    
    # Actualizar escena
    bpy.context.view_layer.update()
    
    # VERIFICAR QUE LOS MESHES SE DEFORMEN EN POSE MODE
    print("\n📊 Verificando deformación en Pose Mode...")
    if body_mesh_before:
        bpy.context.view_layer.update()
        bbox = [body_mesh_before.matrix_world @ Vector(corner) for corner in body_mesh_before.bound_box]
        width_posed = max(v.x for v in bbox) - min(v.x for v in bbox)
        print(f"📏 Ancho EN POSE: {width_posed:.3f}")
        
        if abs(width_posed - width_before) < 0.01:
            print(f"⚠️ WARNING: Mesh NO se deformó!")
            return False
        else:
            print(f"✅ Mesh deformado: +{width_posed - width_before:.3f}")
    
    # CLAVE: NO aplicar como rest pose. En su lugar, "congelar" la deformación
    # Necesitamos BAJAR la pose en los vértices y RESETEAR los huesos
    
    # Volver a object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Para cada mesh, aplicar el modificador armature (congela la deformación)
    print("\n🔧 Congelando deformación en meshes...")
    
    skinned_meshes = []
    for obj in all_meshes:
        for mod in obj.modifiers:
            if mod.type == 'ARMATURE' and mod.object == armature:
                skinned_meshes.append(obj)
                break
    
    print(f"   Meshes con skinning: {len(skinned_meshes)}")
    
    # Eliminar shape keys primero si existen
    for mesh_obj in skinned_meshes:
        if mesh_obj.data.shape_keys:
            bpy.ops.object.select_all(action='DESELECT')
            mesh_obj.select_set(True)
            bpy.context.view_layer.objects.active = mesh_obj
            
            while mesh_obj.data.shape_keys:
                mesh_obj.active_shape_key_index = 0
                bpy.ops.object.shape_key_remove(all=False)
    
    # Aplicar modificador armature a cada mesh
    for mesh_obj in skinned_meshes:
        bpy.ops.object.select_all(action='DESELECT')
        mesh_obj.select_set(True)
        bpy.context.view_layer.objects.active = mesh_obj
        
        for mod in mesh_obj.modifiers:
            if mod.type == 'ARMATURE':
                try:
                    bpy.ops.object.modifier_apply(modifier=mod.name)
                    print(f"   ✅ {mesh_obj.name}")
                except Exception as e:
                    print(f"   ❌ {mesh_obj.name}: {e}")
                break
    
    # Ahora los meshes están congelados en T-pose
    # AHORA SÍ aplicar la pose en el armature para mover los huesos
    print("\n🦴 Aplicando T-pose en huesos...")
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    
    # Re-aplicar las rotaciones T-pose
    for bone_name, quat in bone_quaternions.items():
        if bone_name in armature.pose.bones:
            bone = armature.pose.bones[bone_name]
            bone.rotation_mode = 'QUATERNION'
            bone.rotation_quaternion = quat
    
    # Aplicar como rest pose (ahora solo afecta los huesos, no los meshes)
    bpy.ops.pose.armature_apply(selected=False)
    bpy.ops.object.mode_set(mode='OBJECT')
    print("   ✅ Huesos actualizados a T-pose")
    
    # VERIFICAR DESPUÉS
    body_mesh_check = None
    for mesh in all_meshes:
        if 'Body' in mesh.name:
            body_mesh_check = mesh
            break
    
    if body_mesh_check:
        bbox = [body_mesh_check.matrix_world @ Vector(corner) for corner in body_mesh_check.bound_box]
        width_after = max(v.x for v in bbox) - min(v.x for v in bbox)
        print(f"📏 Ancho FINAL: {width_after:.3f}")
        
        if width_after < 1.4:
            print(f"⚠️ WARNING: Ancho {width_after:.3f} < 1.4")
    
    # Seleccionar todo y exportar
    bpy.ops.object.select_all(action='SELECT')
    
    # Exportar como GLB (preserva texturas en alta resolución)
    print(f"\n💾 Exportando a GLB con texturas completas...")
    bpy.ops.export_scene.gltf(
        filepath=str(DUVALL_OUTPUT_GLB),
        export_format='GLB',
        export_animations=False,
        export_def_bones=True,
        export_image_format='AUTO',
        export_materials='EXPORT'
    )
    print(f"   ✅ GLB: {DUVALL_OUTPUT_GLB.name}")
    
    # También exportar como FBX para compatibilidad
    print(f"\n💾 Exportando a FBX...")
    bpy.ops.export_scene.fbx(
        filepath=str(DUVALL_OUTPUT_FBX),
        use_selection=False,
        bake_anim=False,
        add_leaf_bones=False,
        use_armature_deform_only=True,
        mesh_smooth_type='FACE',
        axis_forward='-Z',
        axis_up='Y',
        path_mode='COPY',
        embed_textures=True
    )
    print(f"   ✅ FBX: {DUVALL_OUTPUT_FBX.name}")
    
    print("\n" + "="*60)
    print("VERIFICACIÓN FINAL - GLB")
    print("="*60)
    
    clear_scene()
    bpy.ops.import_scene.gltf(filepath=str(DUVALL_OUTPUT_GLB))
    
    final_armature = None
    final_meshes = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            final_armature = obj
        elif obj.type == 'MESH':
            final_meshes.append(obj)
    
    if not final_armature:
        print("❌ ERROR: No armature en resultado")
        return False
    
    # Verificar huesos
    bpy.context.view_layer.objects.active = final_armature
    bpy.ops.object.mode_set(mode='EDIT')
    
    print("\n📐 HUESOS:")
    bones_ok = True
    for bone_name in ['LeftArm', 'RightArm']:
        if bone_name in final_armature.data.edit_bones:
            bone = final_armature.data.edit_bones[bone_name]
            direction = (bone.tail - bone.head).normalized()
            print(f"{bone_name}: ({direction.x:.3f}, {direction.y:.3f}, {direction.z:.3f})")
            
            if abs(direction.x) < 0.85:
                print(f"  ❌ NO horizontal")
                bones_ok = False
            else:
                print(f"  ✅ Horizontal")
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Verificar meshes
    body_mesh_final = None
    for mesh in final_meshes:
        if 'Body' in mesh.name:
            body_mesh_final = mesh
            break
    
    mesh_ok = False
    if body_mesh_final:
        bbox = [body_mesh_final.matrix_world @ Vector(corner) for corner in body_mesh_final.bound_box]
        min_x = min(v.x for v in bbox)
        max_x = max(v.x for v in bbox)
        width_final = max_x - min_x
        
        print(f"\n📦 MESH BODY:")
        print(f"  BBox X: {min_x:.3f} to {max_x:.3f}")
        print(f"  Ancho: {width_final:.3f}")
        
        # Debe ser considerablemente más ancho que el original
        if width_final > 1.4:  # Mayor a 1.4m significa brazos extendidos
            print(f"  ✅ EXTENDIDO (T-pose)")
            mesh_ok = True
        else:
            print(f"  ❌ NO EXTENDIDO (ancho={width_final:.3f}, esperado > 1.4)")
    
    print("\n" + "="*60)
    if bones_ok and mesh_ok:
        print("✅✅✅ TODO CORRECTO ✅✅✅")
        return True
    else:
        print("❌❌❌ HAY PROBLEMAS ❌❌❌")
        if not bones_ok:
            print("  - Huesos no en T-pose correcta")
        if not mesh_ok:
            print("  - Mesh no extendido (skinning no funcionó)")
        return False

if __name__ == "__main__":
    try:
        convert_to_tpose()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
