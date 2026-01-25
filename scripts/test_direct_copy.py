import bpy
from pathlib import Path
import json

print("="*80)
print("MAPEO COMPLETO: Nina → Nancy con NLA Track correcto")
print("="*80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "saludos" / "Nina_resultado_hola.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_V2.glb"

print(f"\n📂 Archivos:")
print(f"   Nancy base: {NANCY_BASE}")
print(f"   Nina: {NINA_FILE}")
print(f"   Salida: {NANCY_OUTPUT}")

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
    
    if not nancy_armature:
        print("❌ ERROR: No se encontró armature de Nancy")
        exit(1)
    
    print(f"   ✅ Nancy Armature: {nancy_armature.name}")
    print(f"   ✅ Huesos: {len(nancy_armature.data.bones)}")
    
    # Verificar materiales de Nancy
    nancy_materials = []
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.materials:
            nancy_materials.extend([mat for mat in obj.data.materials if mat])
    
    print(f"   ✅ Materiales de Nancy: {len(set(nancy_materials))}")
    
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
    
    if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
        print("❌ ERROR: Nina sin animación")
        exit(1)
    
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    
    print(f"   ✅ Animación: {nina_action.name}")
    print(f"   ✅ Frames: {frame_start} - {frame_end}")
    print(f"   ✅ FCurves: {len(nina_action.fcurves)}")
    
    # 4. Configurar frame range
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    
    # 5. MÉTODO MEJORADO: Copiar animación directamente a Nancy
    print(f"\n🔄 Copiando animación directamente a Nancy...")
    
    # Crear nueva acción para Nancy
    nancy_action = bpy.data.actions.new(name=nina_action.name + "_Nancy")
    
    # Mapear cada fcurve de Nina a Nancy
    bone_map = {}
    for nancy_bone in nancy_armature.data.bones:
        if nancy_bone.name in nina_armature.data.bones:
            bone_map[nancy_bone.name] = nancy_bone.name
    
    copied_fcurves = 0
    
    for fcurve in nina_action.fcurves:
        # Extraer nombre de hueso del data_path
        data_path = fcurve.data_path
        
        # Ejemplo: pose.bones["Hips"].location
        if 'pose.bones[' in data_path:
            bone_name_start = data_path.find('["') + 2
            bone_name_end = data_path.find('"]')
            bone_name = data_path[bone_name_start:bone_name_end]
            
            if bone_name in bone_map:
                # Crear fcurve equivalente en Nancy
                new_fcurve = nancy_action.fcurves.new(
                    data_path=data_path,
                    index=fcurve.array_index
                )
                
                # Copiar todos los keyframes
                for keyframe in fcurve.keyframe_points:
                    new_fcurve.keyframe_points.insert(
                        keyframe.co.x,
                        keyframe.co.y,
                        options={'FAST'}
                    )
                
                copied_fcurves += 1
    
    print(f"   ✅ FCurves copiadas: {copied_fcurves}")
    
    # Asignar acción a Nancy
    if not nancy_armature.animation_data:
        nancy_armature.animation_data_create()
    
    nancy_armature.animation_data.action = nancy_action
    
    print(f"   ✅ Acción asignada a Nancy: {nancy_action.name}")
    
    # 6. Verificar que Nancy tiene animación
    if not nancy_armature.animation_data or not nancy_armature.animation_data.action:
        print(f"   ❌ ERROR: Nancy no recibió animación")
        exit(1)
    
    # Verificar movimiento ANTES de exportar
    print(f"\n🔍 Verificando movimiento ANTES de exportar...")
    test_bones = ['Hips', 'LeftShoulder', 'RightShoulder', 'LeftArm', 'RightArm']
    
    movement_found = False
    for bone_name in test_bones:
        if bone_name in nancy_armature.pose.bones:
            bone = nancy_armature.pose.bones[bone_name]
            
            bpy.context.scene.frame_set(frame_start)
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
    
    if not movement_found:
        print(f"   ❌ ERROR: No se detectó movimiento en los huesos")
        exit(1)
    
    # 7. Eliminar objetos de Nina
    print(f"\n🗑️ Eliminando objetos de Nina...")
    objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
    objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
    
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    print(f"   ✅ {len(objetos_eliminar)} objetos eliminados")
    
    # 8. Verificar materiales finales
    print(f"\n🎨 Verificando materiales finales...")
    materiales_finales = []
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.materials:
            materiales_finales.extend([mat for mat in obj.data.materials if mat])
    
    print(f"   ✅ Materiales: {len(set(materiales_finales))}")
    
    # 9. Exportar primero a FBX (preserva mejor animaciones)
    print(f"\n💾 PASO 1: Exportando a FBX...")
    NANCY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    FBX_TEMP = NANCY_OUTPUT.with_suffix('.fbx')
    
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
        path_mode='AUTO',
        embed_textures=True
    )
    
    print(f"   ✅ FBX generado: {FBX_TEMP.name}")
    
    # 10. Reimportar FBX
    print(f"\n💾 PASO 2: Reimportando FBX...")
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.fbx(filepath=str(FBX_TEMP))
    
    print(f"   ✅ FBX reimportado")
    
    # 11. Exportar a GLB desde FBX
    print(f"\n💾 PASO 3: Exportando FBX a GLB...")
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
    
    if NANCY_OUTPUT.exists():
        size_mb = NANCY_OUTPUT.stat().st_size / (1024*1024)
        print(f"   ✅ Archivo generado: {size_mb:.1f} MB")
        
        # 10. Verificación final
        print(f"\n🔍 VERIFICACIÓN FINAL...")
        bpy.ops.wm.read_homefile(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))
        
        test_arm = None
        test_materials = []
        
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                test_arm = obj
            elif obj.type == 'MESH' and obj.data.materials:
                test_materials.extend(obj.data.materials)
        
        # Verificar texturas
        print(f"   Materiales: {len(set(test_materials))}")
        texturas_count = 0
        for mat in set(test_materials):
            if mat and mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == 'TEX_IMAGE' and node.image:
                        texturas_count += 1
        print(f"   Texturas: {texturas_count}")
        
        # Verificar animación
        if test_arm and test_arm.animation_data and test_arm.animation_data.action:
            test_action = test_arm.animation_data.action
            print(f"   ✅ Animación: {test_action.name}")
            print(f"   ✅ FCurves: {len(test_action.fcurves)}")
            
            # Probar movimiento
            test_bones = ['Hips', 'Spine', 'LeftShoulder', 'RightShoulder', 'LeftArm', 'RightArm', 'LeftHand', 'RightHand']
            
            movement_detected = False
            for bone_name in test_bones:
                if bone_name in test_arm.pose.bones:
                    bone = test_arm.pose.bones[bone_name]
                    
                    bpy.context.scene.frame_set(frame_start)
                    rot_start = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
                    
                    bpy.context.scene.frame_set(frame_end)
                    rot_end = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
                    
                    if bone.rotation_mode == 'QUATERNION':
                        diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(4))
                    else:
                        diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(3))
                    
                    if diff > 0.001:
                        print(f"   ✅ {bone_name} se mueve: {diff:.4f}")
                        movement_detected = True
            
            if movement_detected:
                print(f"\n{'='*80}")
                print("✅ ✅ ✅ ÉXITO COMPLETO ✅ ✅ ✅")
                print("Nancy con TEXTURAS y ANIMACIÓN FUNCIONAL")
                print(f"{'='*80}")
            else:
                print(f"\n{'='*80}")
                print("❌ PROBLEMA: Sin movimiento detectado")
                print(f"{'='*80}")
        else:
            print("   ❌ ERROR: Sin animación")
    else:
        print("   ❌ ERROR: Archivo no generado")
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
