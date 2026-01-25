"""
Script para transferir animación de Remy a JH.fbx
Maneja diferentes esqueletos y proporciones
"""

import bpy
import mathutils
from pathlib import Path
import json

# Configuración de rutas
BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "output"
TEST_OUTPUT = BASE_DIR / "test" / "output"

def clear_scene():
    """Limpia la escena de Blender"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    for block in bpy.data.meshes:
        bpy.data.meshes.remove(block)
    for block in bpy.data.materials:
        bpy.data.materials.remove(block)
    for block in bpy.data.textures:
        bpy.data.textures.remove(block)
    for block in bpy.data.images:
        bpy.data.images.remove(block)
    for block in bpy.data.armatures:
        bpy.data.armatures.remove(block)

def analyze_armature(armature):
    """Analiza un armature y retorna información"""
    info = {
        'name': armature.name,
        'bone_count': len(armature.data.bones),
        'scale': tuple(armature.scale),
        'bones': {}
    }
    
    for bone in armature.data.bones:
        info['bones'][bone.name] = {
            'head': tuple(bone.head_local),
            'tail': tuple(bone.tail_local),
            'length': bone.length,
            'parent': bone.parent.name if bone.parent else None
        }
    
    return info

def find_bone_mapping(source_armature, target_armature):
    """
    Encuentra mapeo entre huesos de dos armatures
    Método mejorado para detectar variaciones de prefijos
    """
    mapping = {}
    
    source_bones = {b.name: b for b in source_armature.data.bones}
    target_bones = {b.name: b for b in target_armature.data.bones}
    
    print("\n🔍 Buscando mapeo de huesos...")
    
    # Detectar prefijos comunes
    src_prefixes = ['mixamorig:', 'mixamorig_', '']
    tgt_prefixes = ['mixamorig9:', 'mixamorig:', 'mixamorig_', '']
    
    # Método 1: Nombres exactos
    for src_name in source_bones:
        if src_name in target_bones:
            mapping[src_name] = src_name
            print(f"  ✅ Exacto: {src_name}")
    
    # Método 2: Matching por nombre base (sin prefijos)
    for src_name in source_bones:
        if src_name in mapping:
            continue
        
        # Probar todas las combinaciones de prefijos
        src_base = src_name
        for prefix in src_prefixes:
            if src_name.startswith(prefix):
                src_base = src_name[len(prefix):]
                break
        
        # Buscar coincidencia en target
        for tgt_name in target_bones:
            tgt_base = tgt_name
            for prefix in tgt_prefixes:
                if tgt_name.startswith(prefix):
                    tgt_base = tgt_name[len(prefix):]
                    break
            
            # Comparar bases (ignorar mayúsculas)
            if src_base.lower() == tgt_base.lower():
                mapping[src_name] = tgt_name
                print(f"  🔄 Mapeado: {src_name} → {tgt_name}")
                break
    
    # Método 3: Mapeo especial para huesos problemáticos (ojos, etc)
    special_mappings = {
        # Si source tiene ojos pero target no, intentar variaciones
        'LeftEye': ['LeftEye', 'eye_l', 'eye.L', 'L_eye'],
        'RightEye': ['RightEye', 'eye_r', 'eye.R', 'R_eye'],
    }
    
    for base_name, variations in special_mappings.items():
        # Buscar en source con cualquier prefijo
        src_found = None
        for src_name in source_bones:
            for prefix in src_prefixes:
                test_name = prefix + base_name
                if src_name == test_name or src_name.endswith(base_name):
                    src_found = src_name
                    break
            if src_found:
                break
        
        if not src_found or src_found in mapping:
            continue
        
        # Buscar en target
        for tgt_name in target_bones:
            for var in variations:
                for prefix in tgt_prefixes:
                    test_name = prefix + var
                    if tgt_name == test_name or var.lower() in tgt_name.lower():
                        mapping[src_found] = tgt_name
                        print(f"  👁️ Especial: {src_found} → {tgt_name}")
                        break
                if src_found in mapping:
                    break
            if src_found in mapping:
                break
    
    print(f"\n📊 Mapeo completado: {len(mapping)}/{len(source_bones)} huesos mapeados")
    
    # Mostrar huesos NO mapeados (para debug)
    unmapped = [name for name in source_bones if name not in mapping]
    if unmapped:
        if len(unmapped) <= 5:
            print(f"⚠️ Huesos sin mapear: {', '.join(unmapped)}")
        else:
            print(f"⚠️ {len(unmapped)} huesos sin mapear")
    
    return mapping

def retarget_animation(source_obj, target_obj, bone_mapping, scale_factor=1.0):
    """
    Retargetea la animación de source a target usando el mapeo de huesos
    """
    if not source_obj.animation_data or not source_obj.animation_data.action:
        print("⚠️ No hay animación en el objeto source")
        return False
    
    source_action = source_obj.animation_data.action
    
    # Crear nueva acción para target
    target_action = bpy.data.actions.new(name=f"{source_action.name}_retarget")
    
    if not target_obj.animation_data:
        target_obj.animation_data_create()
    
    target_obj.animation_data.action = target_action
    
    print(f"\n🎬 Retargeteando animación: {source_action.name}")
    print(f"   Frames: {source_action.frame_range[0]} - {source_action.frame_range[1]}")
    
    # Obtener rango de frames
    frame_start = int(source_action.frame_range[0])
    frame_end = int(source_action.frame_range[1])
    
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    
    # Activar target
    bpy.context.view_layer.objects.active = target_obj
    bpy.ops.object.mode_set(mode='POSE')
    
    keyframes_created = 0
    
    # Para cada hueso mapeado
    for src_bone_name, tgt_bone_name in bone_mapping.items():
        if src_bone_name not in source_obj.pose.bones:
            continue
        if tgt_bone_name not in target_obj.pose.bones:
            continue
        
        src_bone = source_obj.pose.bones[src_bone_name]
        tgt_bone = target_obj.pose.bones[tgt_bone_name]
        
        # Buscar FCurves del hueso source
        fcurves = [fc for fc in source_action.fcurves 
                   if fc.data_path.startswith(f'pose.bones["{src_bone_name}"]')]
        
        if not fcurves:
            continue
        
        # Copiar keyframes frame por frame
        for frame in range(frame_start, frame_end + 1):
            bpy.context.scene.frame_set(frame)
            
            # Copiar rotación (el componente más importante)
            if src_bone.rotation_mode == 'QUATERNION':
                tgt_bone.rotation_mode = 'QUATERNION'
                tgt_bone.rotation_quaternion = src_bone.rotation_quaternion.copy()
                tgt_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
            else:
                tgt_bone.rotation_mode = src_bone.rotation_mode
                tgt_bone.rotation_euler = src_bone.rotation_euler.copy()
                tgt_bone.keyframe_insert(data_path="rotation_euler", frame=frame)
            
            # Copiar location para huesos root (con scale factor)
            if not tgt_bone.parent or 'hips' in tgt_bone_name.lower() or 'root' in tgt_bone_name.lower():
                tgt_bone.location = src_bone.location * scale_factor
                tgt_bone.keyframe_insert(data_path="location", frame=frame)
            
            keyframes_created += 1
    
    print(f"   ✅ Keyframes creados: {keyframes_created}")
    
    bpy.ops.object.mode_set(mode='OBJECT')
    return True

def calculate_scale_factor(source_armature, target_armature, bone_mapping):
    """
    Calcula el factor de escala entre dos armatures
    basándose en huesos mapeados
    """
    if not bone_mapping:
        return 1.0
    
    scale_ratios = []
    
    for src_name, tgt_name in bone_mapping.items():
        if src_name not in source_armature.data.bones:
            continue
        if tgt_name not in target_armature.data.bones:
            continue
        
        src_bone = source_armature.data.bones[src_name]
        tgt_bone = target_armature.data.bones[tgt_name]
        
        if src_bone.length > 0.001:  # Evitar divisiones por cero
            ratio = tgt_bone.length / src_bone.length
            scale_ratios.append(ratio)
    
    if scale_ratios:
        avg_scale = sum(scale_ratios) / len(scale_ratios)
        print(f"\n📏 Factor de escala calculado: {avg_scale:.3f}")
        return avg_scale
    
    return 1.0

def transfer_animation(source_fbx, target_fbx, output_fbx):
    """
    Función principal: transfiere animación de source a target
    """
    print("="*70)
    print("🔄 TRANSFERENCIA DE ANIMACIÓN")
    print("="*70)
    print(f"Source: {source_fbx.name}")
    print(f"Target: {target_fbx.name}")
    print(f"Output: {output_fbx.name}")
    
    # Limpiar escena
    clear_scene()
    
    # Importar SOURCE (Remy con animación)
    print("\n📥 Importando SOURCE...")
    bpy.ops.import_scene.fbx(
        filepath=str(source_fbx),
        global_scale=1.0
    )
    
    source_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            source_armature = obj
            break
    
    if not source_armature:
        print("❌ No se encontró armature en SOURCE")
        return False
    
    source_info = analyze_armature(source_armature)
    print(f"✅ Source Armature: {source_info['name']}")
    print(f"   Huesos: {source_info['bone_count']}")
    print(f"   Escala: {source_info['scale']}")
    
    # Renombrar para evitar conflictos
    source_armature.name = "SOURCE_Armature"
    
    # Importar TARGET (JH)
    print("\n📥 Importando TARGET...")
    bpy.ops.import_scene.fbx(
        filepath=str(target_fbx),
        global_scale=1.0,
        use_image_search=True,  # Buscar imágenes en carpetas cercanas
        use_custom_normals=True
    )
    
    target_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj.name != source_armature.name:
            target_armature = obj
            break
    
    if not target_armature:
        print("❌ No se encontró armature en TARGET")
        return False
    
    target_info = analyze_armature(target_armature)
    print(f"✅ Target Armature: {target_info['name']}")
    print(f"   Huesos: {target_info['bone_count']}")
    print(f"   Escala: {target_info['scale']}")
    
    # Encontrar mapeo de huesos
    bone_mapping = find_bone_mapping(source_armature, target_armature)
    
    if len(bone_mapping) < 5:
        print("⚠️ Muy pocos huesos mapeados. Mostrando todos los huesos:")
        print("\nSOURCE bones:")
        for bone in list(source_armature.data.bones)[:20]:
            print(f"  - {bone.name}")
        print("\nTARGET bones:")
        for bone in list(target_armature.data.bones)[:20]:
            print(f"  - {bone.name}")
        return False
    
    # Calcular factor de escala
    scale_factor = calculate_scale_factor(source_armature, target_armature, bone_mapping)
    
    # Retargetear animación
    success = retarget_animation(source_armature, target_armature, bone_mapping, scale_factor)
    
    if not success:
        print("❌ Error al retargetear animación")
        return False
    
    # Verificar y corregir materiales del target
    print("\n🎨 Verificando materiales y texturas...")
    target_meshes = [obj for obj in bpy.data.objects if obj.parent == target_armature and obj.type == 'MESH']
    
    textures_found = 0
    for mesh in target_meshes:
        print(f"   Mesh: {mesh.name}")
        if mesh.data.materials:
            for slot_idx, mat in enumerate(mesh.data.materials):
                if mat:
                    print(f"     Material {slot_idx}: {mat.name}")
                    
                    # Asegurar que el material no es transparente
                    if mat.use_nodes:
                        # Buscar nodo Principled BSDF y texturas
                        principled = None
                        for node in mat.node_tree.nodes:
                            if node.type == 'BSDF_PRINCIPLED':
                                principled = node
                                # Asegurar alpha en 1.0 (opaco)
                                if 'Alpha' in node.inputs:
                                    node.inputs['Alpha'].default_value = 1.0
                                
                                # Verificar que tiene color base
                                if 'Base Color' in node.inputs:
                                    base_color_input = node.inputs['Base Color']
                                    # Buscar textura conectada
                                    if base_color_input.is_linked:
                                        linked_node = base_color_input.links[0].from_node
                                        if linked_node.type == 'TEX_IMAGE':
                                            img = linked_node.image
                                            if img:
                                                print(f"       🖼️ Textura: {img.name}")
                                                # Asegurar que la imagen está empacada o tiene filepath
                                                if not img.packed_file and img.filepath:
                                                    try:
                                                        # Intentar cargar la imagen si existe
                                                        img.reload()
                                                        print(f"       ✅ Imagen recargada: {img.filepath}")
                                                    except:
                                                        print(f"       ⚠️ No se pudo recargar imagen")
                                                elif img.packed_file:
                                                    print(f"       ✅ Imagen empacada")
                                                textures_found += 1
                                            else:
                                                print(f"       ⚠️ Nodo de textura sin imagen")
                                    else:
                                        # No hay textura, usar color sólido
                                        print(f"       📦 Color sólido: {base_color_input.default_value[:3]}")
                        
                        if principled:
                            print(f"       ✅ Material configurado (Alpha 1.0)")
                    
                    # Asegurar blend mode
                    mat.blend_method = 'OPAQUE'
                    # shadow_method solo existe en EEVEE, no en todos los casos
                    if hasattr(mat, 'shadow_method'):
                        mat.shadow_method = 'OPAQUE'
    
    print(f"\n📊 Total texturas encontradas: {textures_found}")
    
    # Verificar que todas las imágenes estén disponibles
    print("\n🖼️ Imágenes en la escena:")
    for img in bpy.data.images:
        if img.users > 0:  # Solo imágenes en uso
            status = "📦 Empacada" if img.packed_file else f"📁 {img.filepath}"
            print(f"   - {img.name}: {status}")
    
    # Eliminar source armature (solo queremos el target con animación)
    bpy.ops.object.select_all(action='DESELECT')
    source_armature.select_set(True)
    # También seleccionar meshes del source
    for obj in bpy.data.objects:
        if obj.parent == source_armature:
            obj.select_set(True)
    bpy.ops.object.delete()
    
    print("\n💾 Exportando resultado...")
    
    # Exportar solo el target con la nueva animación
    bpy.ops.export_scene.fbx(
        filepath=str(output_fbx),
        use_selection=False,
        global_scale=1.0,
        apply_unit_scale=False,
        apply_scale_options='FBX_SCALE_NONE',
        bake_space_transform=False,
        object_types={'ARMATURE', 'MESH'},
        use_mesh_modifiers=True,
        mesh_smooth_type='FACE',
        use_armature_deform_only=True,
        add_leaf_bones=False,
        primary_bone_axis='Y',
        secondary_bone_axis='X',
        armature_nodetype='NULL',
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=False,
        bake_anim_use_all_actions=False,
        bake_anim_force_startend_keying=True,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=0.0,
        path_mode='COPY',
        embed_textures=True,
        # Preservar materiales
        use_custom_props=True
    )
    
    file_size = output_fbx.stat().st_size / (1024 * 1024)
    print(f"✅ Exportado: {output_fbx.name} ({file_size:.2f} MB)")
    
    return True

def main():
    """Función principal"""
    source_fbx = OUTPUT_DIR / "Remy_resultado_e.fbx"
    target_fbx = BASE_DIR / "avatars" / "Leonard.fbx"  # Avatar original
    output_fbx = OUTPUT_DIR / "JH_resultado_e.fbx"
    
    if not source_fbx.exists():
        print(f"❌ No existe: {source_fbx}")
        return
    
    if not target_fbx.exists():
        print(f"❌ No existe: {target_fbx}")
        return
    
    success = transfer_animation(source_fbx, target_fbx, output_fbx)
    
    if success:
        print("\n" + "="*70)
        print("✅ TRANSFERENCIA COMPLETADA")
        print("="*70)
    else:
        print("\n" + "="*70)
        print("❌ TRANSFERENCIA FALLIDA")
        print("="*70)

if __name__ == "__main__":
    main()
