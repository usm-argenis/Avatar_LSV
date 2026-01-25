import bpy
from pathlib import Path

print("="*80)
print("SOLUCIÓN FINAL: Nina → Nancy via FBX → GLB")
print("="*80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "saludos" / "Nina_resultado_hola.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_FINAL.glb"
FBX_TEMP = NANCY_OUTPUT.with_suffix('.fbx')

print(f"\n📂 Archivos:")
print(f"   Nancy base: {NANCY_BASE}")
print(f"   Nina: {NINA_FILE}")
print(f"   Salida: {NANCY_OUTPUT}")

try:
    # 1. Limpiar escena
    print(f"\n🧹 Limpiando escena...")
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # 2. Importar Nancy
    print(f"\n📦 Importando Nancy...")
    bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
    
    nancy_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            nancy_armature = obj
            break
    
    print(f"   ✅ Nancy Armature encontrado")
    
    if nancy_armature.animation_data:
        nancy_armature.animation_data_clear()
    
    # 3. Importar Nina con animación
    print(f"\n🎬 Importando Nina con animación...")
    bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
    
    nina_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != nancy_armature:
            nina_armature = obj
            break
    
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    
    print(f"   ✅ Animación: {nina_action.name} ({frame_start}-{frame_end})")
    
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
    print(f"   ✅ {len(nancy_action.fcurves)} FCurves copiadas")
    
    # 5. Eliminar objetos de Nina
    print(f"\n🗑️ Eliminando objetos de Nina...")
    objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
    objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
    
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    # 6. Exportar a FBX con texturas
    print(f"\n💾 PASO 1/3: Exportando a FBX...")
    NANCY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.fbx(
        filepath=str(FBX_TEMP),
        use_selection=False,
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=False,
        bake_anim_use_all_actions=False,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=0.0,
        add_leaf_bones=False,
        path_mode='COPY',
        embed_textures=True
    )
    
    print(f"   ✅ FBX temporal generado")
    
    # 7. Reimportar FBX
    print(f"\n💾 PASO 2/3: Reimportando FBX...")
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.fbx(filepath=str(FBX_TEMP))
    
    print(f"   ✅ FBX reimportado")
    
    # 8. Exportar a GLB desde FBX
    print(f"\n💾 PASO 3/3: Exportando FBX a GLB...")
    bpy.ops.export_scene.gltf(
        filepath=str(NANCY_OUTPUT),
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
    
    glb_size = NANCY_OUTPUT.stat().st_size / (1024*1024)
    print(f"   ✅ GLB generado: {glb_size:.1f} MB")
    
    # 9. Verificación final
    print(f"\n🔍 VERIFICACIÓN FINAL...")
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))
    
    test_arm = None
    test_mats = []
    test_texs = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            test_arm = obj
        elif obj.type == 'MESH' and obj.data.materials:
            for mat in obj.data.materials:
                if mat and mat not in test_mats:
                    test_mats.append(mat)
                    if mat.use_nodes:
                        for node in mat.node_tree.nodes:
                            if node.type == 'TEX_IMAGE' and node.image:
                                test_texs.append(node.image.name)
    
    print(f"   Materiales: {len(test_mats)}")
    print(f"   Texturas: {len(test_texs)}")
    
    if test_arm and test_arm.animation_data and test_arm.animation_data.action:
        action = test_arm.animation_data.action
        print(f"   ✅ Animación: {action.name}")
        print(f"   ✅ FCurves: {len(action.fcurves)}")
        
        # Verificar movimiento
        test_bones = ['Hips', 'LeftShoulder', 'RightShoulder', 'LeftArm', 'RightArm', 'LeftHand', 'RightHand']
        
        bpy.context.scene.frame_set(frame_start)
        movement_found = False
        
        for bone_name in test_bones:
            if bone_name in test_arm.pose.bones:
                bone = test_arm.pose.bones[bone_name]
                rot_start = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
                
                bpy.context.scene.frame_set(frame_end)
                rot_end = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
                
                if bone.rotation_mode == 'QUATERNION':
                    diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(4))
                else:
                    diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(3))
                
                if diff > 0.001:
                    print(f"   ✅ {bone_name} se mueve: {diff:.4f}")
                    movement_found = True
        
        if movement_found and len(test_texs) > 0:
            print(f"\n{'='*80}")
            print("✅ ✅ ✅ ÉXITO TOTAL ✅ ✅ ✅")
            print(f"Nancy GLB con {len(test_texs)} texturas Y animación funcional")
            print(f"Archivo: {NANCY_OUTPUT.name}")
            print(f"{'='*80}")
        elif movement_found:
            print(f"\n⚠️ Animación OK pero sin texturas")
        elif len(test_texs) > 0:
            print(f"\n⚠️ Texturas OK pero sin animación")
        else:
            print(f"\n❌ Sin texturas ni animación")
    else:
        print(f"   ❌ Sin animación")
    
    # Limpiar FBX temporal
    if FBX_TEMP.exists():
        FBX_TEMP.unlink()
        print(f"\n🗑️ FBX temporal eliminado")
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
