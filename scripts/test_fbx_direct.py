import bpy
from pathlib import Path

print("="*80)
print("EXPORTACIÓN FBX DIRECTO (sin reimportar): Nina → Nancy")
print("="*80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "saludos" / "Nina_resultado_hola.glb"
NANCY_OUTPUT_GLB = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_V3.glb"
NANCY_OUTPUT_FBX = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_V3.fbx"

print(f"\n📂 Archivos:")
print(f"   Nancy base: {NANCY_BASE}")
print(f"   Nina: {NINA_FILE}")
print(f"   Salida FBX: {NANCY_OUTPUT_FBX}")
print(f"   Salida GLB: {NANCY_OUTPUT_GLB}")

try:
    # 1. Limpiar escena
    print(f"\n🧹 Limpiando escena...")
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # 2. Importar Nancy (destino)
    print(f"\n📦 Importando Nancy (destino)...")
    bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
    
    nancy_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            nancy_armature = obj
            nancy_armature.name = "Nancy_Armature"
            break
    
    print(f"   ✅ Nancy Armature: {nancy_armature.name}")
    
    # Limpiar animación previa
    if nancy_armature.animation_data:
        nancy_armature.animation_data_clear()
    
    # 3. Importar Nina con animación
    print(f"\n🎬 Importando Nina con animación...")
    bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
    
    nina_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != nancy_armature:
            nina_armature = obj
            nina_armature.name = "Nina_Armature"
            break
    
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    
    print(f"   ✅ Animación: {nina_action.name}")
    print(f"   ✅ Frames: {frame_start} - {frame_end}")
    
    # 4. Copiar animación a Nancy
    print(f"\n🔄 Copiando animación a Nancy...")
    
    nancy_action = bpy.data.actions.new(name=nina_action.name + "_Nancy")
    
    for fcurve in nina_action.fcurves:
        data_path = fcurve.data_path
        
        if 'pose.bones[' in data_path:
            bone_name_start = data_path.find('["') + 2
            bone_name_end = data_path.find('"]')
            bone_name = data_path[bone_name_start:bone_name_end]
            
            if bone_name in nancy_armature.data.bones:
                new_fcurve = nancy_action.fcurves.new(
                    data_path=data_path,
                    index=fcurve.array_index
                )
                
                for keyframe in fcurve.keyframe_points:
                    new_fcurve.keyframe_points.insert(
                        keyframe.co.x,
                        keyframe.co.y,
                        options={'FAST'}
                    )
    
    if not nancy_armature.animation_data:
        nancy_armature.animation_data_create()
    
    nancy_armature.animation_data.action = nancy_action
    print(f"   ✅ Animación asignada a Nancy")
    
    # 5. Eliminar objetos de Nina
    print(f"\n🗑️ Eliminando objetos de Nina...")
    objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
    objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
    
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    print(f"   ✅ {len(objetos_eliminar)} objetos eliminados")
    
    # 6. Verificar materiales ANTES de exportar
    print(f"\n🎨 Materiales antes de exportar:")
    materiales = []
    texturas = []
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.materials:
            for mat in obj.data.materials:
                if mat and mat not in materiales:
                    materiales.append(mat)
                    if mat.use_nodes:
                        for node in mat.node_tree.nodes:
                            if node.type == 'TEX_IMAGE' and node.image:
                                texturas.append(node.image.name)
                                print(f"   📷 {mat.name}: {node.image.name}")
    
    print(f"   ✅ Materiales: {len(materiales)}")
    print(f"   ✅ Texturas: {len(texturas)}")
    
    # 7. Exportar DIRECTAMENTE a FBX con texturas embebidas
    print(f"\n💾 Exportando a FBX CON TEXTURAS...")
    NANCY_OUTPUT_FBX.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.fbx(
        filepath=str(NANCY_OUTPUT_FBX),
        use_selection=False,
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=False,
        bake_anim_use_all_actions=False,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=0.0,
        add_leaf_bones=False,
        path_mode='COPY',  # COPIAR texturas
        embed_textures=True  # EMBEBER texturas
    )
    
    fbx_size = NANCY_OUTPUT_FBX.stat().st_size / (1024*1024)
    print(f"   ✅ FBX generado: {fbx_size:.1f} MB")
    
    # 8. Exportar TAMBIÉN a GLB directo (sin pasar por FBX)
    print(f"\n💾 Exportando TAMBIÉN a GLB directo...")
    
    bpy.ops.export_scene.gltf(
        filepath=str(NANCY_OUTPUT_GLB),
        export_format='GLB',
        export_animations=True,
        export_frame_range=True,
        export_force_sampling=True,
        export_def_bones=False,
        export_optimize_animation_size=False,
        export_materials='EXPORT',
        export_image_format='AUTO',
        export_texcoords=True,
        export_normals=True,
        export_attributes=True
    )
    
    glb_size = NANCY_OUTPUT_GLB.stat().st_size / (1024*1024)
    print(f"   ✅ GLB generado: {glb_size:.1f} MB")
    
    # 9. VERIFICACIÓN: Importar FBX
    print(f"\n🔍 VERIFICACIÓN 1: Reimportando FBX...")
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.fbx(filepath=str(NANCY_OUTPUT_FBX))
    
    fbx_arm = None
    fbx_mats = []
    fbx_texs = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            fbx_arm = obj
        elif obj.type == 'MESH' and obj.data.materials:
            for mat in obj.data.materials:
                if mat and mat not in fbx_mats:
                    fbx_mats.append(mat)
                    if mat.use_nodes:
                        for node in mat.node_tree.nodes:
                            if node.type == 'TEX_IMAGE' and node.image:
                                fbx_texs.append(node.image.name)
    
    print(f"   Materiales: {len(fbx_mats)}")
    print(f"   Texturas: {len(fbx_texs)}")
    
    if fbx_arm and fbx_arm.animation_data and fbx_arm.animation_data.action:
        print(f"   ✅ Animación: {fbx_arm.animation_data.action.name}")
        print(f"   ✅ FCurves: {len(fbx_arm.animation_data.action.fcurves)}")
        
        # Probar movimiento
        bpy.context.scene.frame_set(frame_start)
        if 'Hips' in fbx_arm.pose.bones:
            bone = fbx_arm.pose.bones['Hips']
            rot_start = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
            
            bpy.context.scene.frame_set(frame_end)
            rot_end = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
            
            if bone.rotation_mode == 'QUATERNION':
                diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(4))
            else:
                diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(3))
            
            if diff > 0.001:
                print(f"   ✅ Hips se mueve: {diff:.4f}")
    
    # 10. VERIFICACIÓN: Importar GLB
    print(f"\n🔍 VERIFICACIÓN 2: Reimportando GLB...")
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT_GLB))
    
    glb_arm = None
    glb_mats = []
    glb_texs = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            glb_arm = obj
        elif obj.type == 'MESH' and obj.data.materials:
            for mat in obj.data.materials:
                if mat and mat not in glb_mats:
                    glb_mats.append(mat)
                    if mat.use_nodes:
                        for node in mat.node_tree.nodes:
                            if node.type == 'TEX_IMAGE' and node.image:
                                glb_texs.append(node.image.name)
    
    print(f"   Materiales: {len(glb_mats)}")
    print(f"   Texturas: {len(glb_texs)}")
    
    if glb_arm and glb_arm.animation_data and glb_arm.animation_data.action:
        print(f"   ✅ Animación: {glb_arm.animation_data.action.name}")
        print(f"   ✅ FCurves: {len(glb_arm.animation_data.action.fcurves)}")
        
        # Probar movimiento
        bpy.context.scene.frame_set(frame_start)
        if 'Hips' in glb_arm.pose.bones:
            bone = glb_arm.pose.bones['Hips']
            rot_start = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
            
            bpy.context.scene.frame_set(frame_end)
            rot_end = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
            
            if bone.rotation_mode == 'QUATERNION':
                diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(4))
            else:
                diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(3))
            
            if diff > 0.001:
                print(f"   ✅ Hips se mueve: {diff:.4f}")
    
    # RESUMEN
    print(f"\n{'='*80}")
    print("RESUMEN DE RESULTADOS:")
    print(f"{'='*80}")
    print(f"\n📦 FBX ({fbx_size:.1f} MB):")
    print(f"   Texturas: {len(fbx_texs)}")
    print(f"   Animación: {'✅ SÍ' if fbx_arm and fbx_arm.animation_data else '❌ NO'}")
    
    print(f"\n📦 GLB ({glb_size:.1f} MB):")
    print(f"   Texturas: {len(glb_texs)}")
    print(f"   Animación: {'✅ SÍ' if glb_arm and glb_arm.animation_data else '❌ NO'}")
    
    # Decisión
    if len(glb_texs) > 0 and glb_arm and glb_arm.animation_data:
        print(f"\n{'='*80}")
        print("✅ ✅ ✅ GLB TIENE TEXTURAS Y ANIMACIÓN ✅ ✅ ✅")
        print("USAR GLB DIRECTO - NO NECESITA FBX")
        print(f"{'='*80}")
    elif len(fbx_texs) > 0 and fbx_arm and fbx_arm.animation_data:
        print(f"\n{'='*80}")
        print("✅ FBX TIENE TEXTURAS Y ANIMACIÓN")
        print("NECESITAMOS CONVERTIR FBX → GLB preservando texturas")
        print(f"{'='*80}")
    else:
        print(f"\n{'='*80}")
        print("⚠️ PROBLEMA PERSISTE")
        print(f"{'='*80}")
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
