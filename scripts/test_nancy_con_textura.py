import bpy
from pathlib import Path

print("="*80)
print("TEST: Transferir animación Nina → Nancy CON TEXTURAS")
print("="*80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_FILE = BASE_DIR / "Nina" / "saludos" / "Nina_resultado_hola.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_TEST.glb"

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
    nancy_meshes = []
    nancy_materials = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            nancy_armature = obj
        elif obj.type == 'MESH':
            nancy_meshes.append(obj)
            if obj.data.materials:
                nancy_materials.extend(obj.data.materials)
    
    print(f"   ✅ Armature: {nancy_armature.name if nancy_armature else 'NO'}")
    print(f"   ✅ Meshes: {len(nancy_meshes)}")
    print(f"   ✅ Materiales: {len(set(nancy_materials))}")
    
    # Listar materiales
    for mat in set(nancy_materials):
        print(f"      - {mat.name}")
        if mat.use_nodes:
            for node in mat.node_tree.nodes:
                if node.type == 'TEX_IMAGE' and node.image:
                    print(f"        Textura: {node.image.name}")
    
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
    
    if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
        print("❌ ERROR: Nina sin animación")
        exit(1)
    
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    
    print(f"   ✅ Animación: {nina_action.name}")
    print(f"   ✅ Frames: {frame_start} - {frame_end}")
    print(f"   ✅ FCurves: {len(nina_action.fcurves)}")
    
    # 4. Crear constraints
    print(f"\n📌 Creando constraints...")
    for nancy_bone in nancy_armature.pose.bones:
        if nancy_bone.name in nina_armature.pose.bones:
            constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
            constraint.target = nina_armature
            constraint.subtarget = nancy_bone.name
    
    # 5. Configurar frame range ANTES del bake
    bpy.context.scene.frame_start = frame_start
    bpy.context.scene.frame_end = frame_end
    
    # 6. Bake
    print(f"\n🔥 Baking animación...")
    bpy.context.view_layer.objects.active = nancy_armature
    nancy_armature.select_set(True)
    
    bpy.ops.nla.bake(
        frame_start=frame_start,
        frame_end=frame_end,
        step=1,
        only_selected=False,
        visual_keying=True,
        clear_constraints=True,
        bake_types={'POSE'}
    )
    
    # 7. Verificar bake
    if nancy_armature.animation_data and nancy_armature.animation_data.action:
        baked_action = nancy_armature.animation_data.action
        print(f"   ✅ Bake exitoso: {baked_action.name}")
        print(f"   ✅ FCurves: {len(baked_action.fcurves)}")
        print(f"   ✅ Frame range: {baked_action.frame_range}")
    else:
        print("   ❌ ERROR: Bake falló - No hay animación")
        exit(1)
    
    # 8. Eliminar objetos de Nina
    print(f"\n🗑️ Eliminando objetos de Nina...")
    objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
    objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
    
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    print(f"   ✅ {len(objetos_eliminar)} objetos eliminados")
    
    # 9. Verificar que Nancy todavía tiene materiales (AHORA meshes son válidos)
    print(f"\n🎨 Verificando materiales de Nancy...")
    nancy_materials_final = []
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.materials:
            nancy_materials_final.extend(obj.data.materials)
    
    print(f"   ✅ Materiales finales: {len(set(nancy_materials_final))}")
    for mat in set(nancy_materials_final):
        if mat:
            print(f"      - {mat.name}")
    
    # 10. Exportar a GLB
    print(f"\n💾 Exportando a GLB...")
    NANCY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.gltf(
        filepath=str(NANCY_OUTPUT),
        export_format='GLB',
        export_animations=True,
        export_frame_range=True,
        export_force_sampling=True,
        export_def_bones=False,
        export_optimize_animation_size=False,
        # CRÍTICO para texturas
        export_materials='EXPORT',
        export_image_format='AUTO',
        export_texcoords=True,
        export_normals=True,
        export_attributes=True
    )
    
    if NANCY_OUTPUT.exists():
        size_mb = NANCY_OUTPUT.stat().st_size / (1024*1024)
        print(f"   ✅ Archivo generado: {size_mb:.1f} MB")
        
        # 11. Verificación final
        print(f"\n🔍 Verificación final...")
        bpy.ops.wm.read_homefile(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))
        
        test_arm = None
        test_meshes = []
        test_materials = []
        
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                test_arm = obj
            elif obj.type == 'MESH':
                test_meshes.append(obj)
                if obj.data.materials:
                    test_materials.extend(obj.data.materials)
        
        print(f"   Meshes: {len(test_meshes)}")
        print(f"   Materiales: {len(set(test_materials))}")
        
        for mat in set(test_materials):
            if mat:
                print(f"      - {mat.name}")
                if mat.use_nodes:
                    has_texture = False
                    for node in mat.node_tree.nodes:
                        if node.type == 'TEX_IMAGE' and node.image:
                            has_texture = True
                            print(f"        ✅ Textura: {node.image.name}")
                    if not has_texture:
                        print(f"        ⚠️ Sin textura")
        
        if test_arm and test_arm.animation_data and test_arm.animation_data.action:
            test_action = test_arm.animation_data.action
            print(f"   ✅ Animación: {test_action.name}")
            print(f"   ✅ FCurves: {len(test_action.fcurves)}")
            
            # Probar movimiento
            bpy.context.scene.frame_set(frame_start)
            if "LeftHand" in test_arm.pose.bones:
                bone = test_arm.pose.bones["LeftHand"]
                rot_start = bone.rotation_quaternion.copy()
                
                bpy.context.scene.frame_set(frame_end)
                rot_end = test_arm.pose.bones["LeftHand"].rotation_quaternion
                
                diff = abs(rot_start.w - rot_end.w) + abs(rot_start.x - rot_end.x)
                
                print(f"   Movimiento LeftHand: {diff:.3f}")
                
                if diff > 0.01:
                    print(f"\n{'='*80}")
                    print("✅ ✅ ✅ ÉXITO COMPLETO ✅ ✅ ✅")
                    print("Nancy con texturas Y animación correcta")
                    print(f"{'='*80}")
                else:
                    print("\n⚠️ ADVERTENCIA: No hay movimiento detectado")
        else:
            print("   ❌ ERROR: Sin animación en archivo final")
    else:
        print("   ❌ ERROR: Archivo no generado")
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
