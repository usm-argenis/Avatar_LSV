import bpy
from pathlib import Path

print("="*80)
print("SOLUCIÓN SIN FBX: Preservar materiales originales de Nancy")
print("="*80)

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "saludos" / "Nina_resultado_hola.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_PERFECTO.glb"

print(f"\n📂 Archivos:")
print(f"   Nancy: {NANCY_BASE}")
print(f"   Nina: {NINA_FILE}")
print(f"   Salida: {NANCY_OUTPUT}")

try:
    # 1. Limpiar escena
    print(f"\n🧹 Limpiando escena...")
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # 2. Importar Nancy PRIMERO (para preservar materiales)
    print(f"\n📦 Importando Nancy con materiales originales...")
    bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
    
    nancy_armature = None
    nancy_meshes = []
    nancy_materials = {}
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            nancy_armature = obj
            nancy_armature.name = "Nancy_Armature"
        elif obj.type == 'MESH':
            nancy_meshes.append(obj)
            # Guardar materiales originales
            if obj.data.materials:
                for mat in obj.data.materials:
                    if mat:
                        nancy_materials[mat.name] = mat
    
    print(f"   ✅ Armature: {nancy_armature.name}")
    print(f"   ✅ Meshes: {len(nancy_meshes)}")
    print(f"   ✅ Materiales únicos: {len(nancy_materials)}")
    
    # Contar texturas originales
    texturas_originales = []
    for mat in nancy_materials.values():
        if mat.use_nodes:
            for node in mat.node_tree.nodes:
                if node.type == 'TEX_IMAGE' and node.image:
                    texturas_originales.append({
                        'material': mat.name,
                        'nombre': node.image.name,
                        'size': node.image.size[:],
                        'pixels': len(node.image.pixels)
                    })
    
    print(f"   ✅ Texturas: {len(texturas_originales)}")
    for tex in texturas_originales:
        print(f"      📷 {tex['material']}: {tex['nombre']} ({tex['size'][0]}x{tex['size'][1]})")
    
    # Limpiar animación de Nancy
    if nancy_armature.animation_data:
        nancy_armature.animation_data_clear()
    
    # 3. Importar Nina CON animación
    print(f"\n🎬 Importando animación de Nina...")
    bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
    
    nina_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != nancy_armature:
            nina_armature = obj
            break
    
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    
    print(f"   ✅ Animación: {nina_action.name}")
    print(f"   ✅ Frames: {frame_start}-{frame_end}")
    print(f"   ✅ FCurves: {len(nina_action.fcurves)}")
    
    # 4. Copiar animación directamente (sin baking)
    print(f"\n🔄 Copiando animación a Nancy...")
    
    # Crear nueva acción para Nancy con nombre limpio
    nancy_action = bpy.data.actions.new(name=nina_action.name)
    
    fcurves_copiadas = 0
    for fcurve in nina_action.fcurves:
        data_path = fcurve.data_path
        
        # Solo copiar animación de huesos
        if 'pose.bones[' in data_path:
            bone_name_start = data_path.find('["') + 2
            bone_name_end = data_path.find('"]')
            bone_name = data_path[bone_name_start:bone_name_end]
            
            # Verificar que el hueso existe en Nancy
            if bone_name in nancy_armature.data.bones:
                # Crear FCurve en la acción de Nancy
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
                    
                fcurves_copiadas += 1
    
    # Asignar acción a Nancy
    if not nancy_armature.animation_data:
        nancy_armature.animation_data_create()
    
    nancy_armature.animation_data.action = nancy_action
    
    print(f"   ✅ {fcurves_copiadas} FCurves copiadas")
    
    # 5. Verificar movimiento ANTES de eliminar Nina
    print(f"\n🔍 Verificando movimiento en Nancy...")
    bpy.context.scene.frame_set(frame_start)
    
    test_bones = ['Hips', 'LeftArm', 'RightArm']
    movement_ok = False
    
    for bone_name in test_bones:
        if bone_name in nancy_armature.pose.bones:
            bone = nancy_armature.pose.bones[bone_name]
            rot_start = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
            
            bpy.context.scene.frame_set(frame_end)
            rot_end = bone.rotation_quaternion.copy() if bone.rotation_mode == 'QUATERNION' else bone.rotation_euler.copy()
            
            if bone.rotation_mode == 'QUATERNION':
                diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(4))
            else:
                diff = sum(abs(rot_end[i] - rot_start[i]) for i in range(3))
            
            if diff > 0.001:
                print(f"   ✅ {bone_name} se mueve: {diff:.4f}")
                movement_ok = True
    
    if not movement_ok:
        raise Exception("La animación no se copió correctamente - no hay movimiento")
    
    # 6. Eliminar SOLO objetos de Nina (meshes y armature)
    print(f"\n🗑️ Eliminando objetos de Nina...")
    objetos_nancy = [nancy_armature] + nancy_meshes
    objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
    
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    print(f"   ✅ {len(objetos_eliminar)} objetos de Nina eliminados")
    print(f"   ✅ {len(objetos_nancy)} objetos de Nancy preservados")
    
    # 7. Verificar que los materiales siguen intactos
    print(f"\n🎨 Verificando materiales antes de exportar...")
    materiales_actuales = {}
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.materials:
            for mat in obj.data.materials:
                if mat and mat.name not in materiales_actuales:
                    materiales_actuales[mat.name] = mat
    
    print(f"   Materiales: {len(materiales_actuales)}/{len(nancy_materials)}")
    
    if len(materiales_actuales) != len(nancy_materials):
        print(f"   ⚠️ ADVERTENCIA: Se perdieron materiales")
    
    # Verificar texturas
    texturas_actuales = []
    for mat in materiales_actuales.values():
        if mat.use_nodes:
            for node in mat.node_tree.nodes:
                if node.type == 'TEX_IMAGE' and node.image:
                    texturas_actuales.append({
                        'nombre': node.image.name,
                        'size': node.image.size[:]
                    })
    
    print(f"   Texturas: {len(texturas_actuales)}/{len(texturas_originales)}")
    
    # 8. Exportar DIRECTAMENTE a GLB (SIN FBX)
    print(f"\n💾 Exportando DIRECTAMENTE a GLB (sin FBX)...")
    NANCY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    # Configurar frame range
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    
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
        export_attributes=True,
        export_apply=False  # NO aplicar transformaciones
    )
    
    glb_size = NANCY_OUTPUT.stat().st_size / (1024*1024)
    print(f"   ✅ GLB generado: {glb_size:.1f} MB")
    
    # 9. VERIFICACIÓN FINAL COMPLETA
    print(f"\n🔍 VERIFICACIÓN FINAL...")
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))
    
    test_arm = None
    test_mats = {}
    test_texs = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            test_arm = obj
        elif obj.type == 'MESH' and obj.data.materials:
            for mat in obj.data.materials:
                if mat and mat.name not in test_mats:
                    test_mats[mat.name] = mat
                    if mat.use_nodes:
                        for node in mat.node_tree.nodes:
                            if node.type == 'TEX_IMAGE' and node.image:
                                test_texs.append({
                                    'material': mat.name,
                                    'nombre': node.image.name,
                                    'size': node.image.size[:],
                                    'pixels': len(node.image.pixels)
                                })
    
    print(f"\n📦 Resultado:")
    print(f"   Materiales: {len(test_mats)}")
    print(f"   Texturas: {len(test_texs)}")
    
    print(f"\n   Detalle de texturas:")
    for tex in test_texs:
        print(f"      📷 {tex['material']}: {tex['nombre']} ({tex['size'][0]}x{tex['size'][1]})")
    
    # Verificar animación
    if test_arm and test_arm.animation_data and test_arm.animation_data.action:
        action = test_arm.animation_data.action
        print(f"\n   ✅ Animación: {action.name}")
        print(f"   ✅ FCurves: {len(action.fcurves)}")
        
        # Probar movimiento
        test_bones = ['Hips', 'LeftArm', 'RightArm', 'LeftHand', 'RightHand']
        
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
        
        # EVALUACIÓN FINAL
        print(f"\n{'='*80}")
        
        texturas_alta_res = sum(1 for t in test_texs if t['size'][0] >= 512 or t['size'][1] >= 512)
        
        if movement_found and len(test_texs) >= 12 and texturas_alta_res > 0:
            print("✅ ✅ ✅ ÉXITO PERFECTO ✅ ✅ ✅")
            print(f"Nancy con {len(test_texs)} texturas EN ALTA RESOLUCIÓN Y animación funcional")
            print(f"Texturas originales preservadas: {texturas_alta_res}/{len(test_texs)} en alta resolución")
        elif movement_found and len(test_texs) >= 12:
            print("⚠️ PARCIALMENTE EXITOSO")
            print("Animación funciona, texturas presentes pero en baja resolución")
        elif movement_found:
            print("⚠️ ANIMACIÓN OK, pero texturas incompletas")
        else:
            print("❌ FALLÓ: No hay movimiento de animación")
        
        print(f"{'='*80}")
    else:
        print(f"\n❌ Sin animación")
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
