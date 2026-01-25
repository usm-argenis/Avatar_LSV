"""
Script de prueba para transferir UNA animación de Nina a Nancy
VERIFICANDO QUE LAS TEXTURAS SE PRESERVEN
"""
import bpy
from pathlib import Path

# Configuración
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_BASE = BASE_DIR / "Nancy" / "Nancy.glb"
NINA_ANIM = BASE_DIR / "Nina" / "saludos" / "Nina_resultado_hola.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "saludos" / "Nancy_resultado_hola_TEST.glb"

print("=" * 80)
print("TEST: Transferencia Nina → Nancy CON TEXTURAS")
print("=" * 80)
print(f"Nancy base: {NANCY_BASE}")
print(f"Nina anim: {NINA_ANIM}")
print(f"Salida: {NANCY_OUTPUT}")
print()

try:
    # 1. Limpiar
    print("[1/8] Limpiando escena...")
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # 2. Importar Nancy
    print("[2/8] Importando Nancy base (CON TEXTURAS)...")
    bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
    
    nancy_armature = None
    nancy_meshes = []
    nancy_materials = []
    
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            nancy_armature = obj
        elif obj.type == 'MESH':
            nancy_meshes.append(obj)
            # Recolectar materiales
            for mat_slot in obj.material_slots:
                if mat_slot.material and mat_slot.material not in nancy_materials:
                    nancy_materials.append(mat_slot.material)
    
    print(f"   ✅ Armature: {nancy_armature.name}")
    print(f"   ✅ Meshes: {len(nancy_meshes)}")
    print(f"   ✅ Materiales: {len(nancy_materials)}")
    
    # Mostrar detalles de materiales
    for mat in nancy_materials:
        print(f"      - {mat.name}: {len(mat.node_tree.nodes) if mat.node_tree else 0} nodos")
        if mat.node_tree:
            for node in mat.node_tree.nodes:
                if node.type == 'TEX_IMAGE' and node.image:
                    print(f"         • Textura: {node.image.name} ({node.image.size[0]}x{node.image.size[1]})")
    
    # 3. Importar Nina
    print("[3/8] Importando Nina con animación...")
    bpy.ops.import_scene.gltf(filepath=str(NINA_ANIM))
    
    nina_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE' and obj != nancy_armature:
            nina_armature = obj
            break
    
    if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
        raise Exception("Nina no tiene animación")
    
    nina_action = nina_armature.animation_data.action
    frame_start = int(nina_action.frame_range[0])
    frame_end = int(nina_action.frame_range[1])
    
    print(f"   ✅ Animación: {nina_action.name}")
    print(f"   ✅ Frames: {frame_start} - {frame_end}")
    
    # 4. Crear constraints
    print("[4/8] Creando constraints...")
    for nancy_bone in nancy_armature.pose.bones:
        if nancy_bone.name in nina_armature.pose.bones:
            constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
            constraint.target = nina_armature
            constraint.subtarget = nancy_bone.name
    
    # 5. Bake
    print("[5/8] Baking animación...")
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
    
    print("   ✅ Bake completado")
    
    # 6. Eliminar objetos de Nina (NO materiales)
    print("[6/8] Eliminando objetos de Nina...")
    objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
    objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
    
    for obj in objetos_eliminar:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    print(f"   ✅ Eliminados: {len(objetos_eliminar)} objetos")
    
    # 7. VERIFICAR MATERIALES ANTES DE EXPORTAR
    print("[7/8] Verificando materiales antes de exportar...")
    materiales_actuales = []
    # Usar objetos actuales en la escena, no la referencia guardada
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            for mat_slot in obj.material_slots:
                if mat_slot.material and mat_slot.material not in materiales_actuales:
                    materiales_actuales.append(mat_slot.material)
    
    print(f"   ✅ Materiales preservados: {len(materiales_actuales)}")
    for mat in materiales_actuales:
        print(f"      - {mat.name}")
    
    # 8. Exportar DIRECTAMENTE a GLB
    print("[8/8] Exportando a GLB CON TEXTURAS...")
    NANCY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.gltf(
        filepath=str(NANCY_OUTPUT),
        export_format='GLB',
        # Animación
        export_animations=True,
        export_frame_range=True,
        export_force_sampling=True,
        export_def_bones=False,
        export_optimize_animation_size=False,
        # TEXTURAS Y MATERIALES (CRÍTICO)
        export_materials='EXPORT',  # Exportar materiales
        export_image_format='AUTO',  # Formato automático de imagen
        export_texcoords=True,  # Coordenadas de textura
        export_normals=True,  # Normales
        export_tangents=False,
        export_apply=False  # No aplicar modificadores
    )
    
    if NANCY_OUTPUT.exists():
        size_mb = NANCY_OUTPUT.stat().st_size / (1024 * 1024)
        print(f"\n✅ ARCHIVO GENERADO: {size_mb:.2f} MB")
        
        # VERIFICACIÓN FINAL
        print("\n" + "=" * 80)
        print("VERIFICACIÓN FINAL")
        print("=" * 80)
        
        bpy.ops.wm.read_homefile(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))
        
        test_armature = None
        test_meshes = []
        test_materials = []
        
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                test_armature = obj
            elif obj.type == 'MESH':
                test_meshes.append(obj)
                for mat_slot in obj.material_slots:
                    if mat_slot.material and mat_slot.material not in test_materials:
                        test_materials.append(mat_slot.material)
        
        print(f"✅ Armature: {test_armature.name if test_armature else 'NO ENCONTRADO'}")
        print(f"✅ Meshes: {len(test_meshes)}")
        print(f"✅ Materiales: {len(test_materials)}")
        
        if test_materials:
            print("\n📦 Materiales encontrados:")
            for mat in test_materials:
                print(f"   - {mat.name}")
                if mat.node_tree:
                    texturas = [node for node in mat.node_tree.nodes if node.type == 'TEX_IMAGE' and node.image]
                    if texturas:
                        for tex_node in texturas:
                            print(f"      • Textura: {tex_node.image.name} ({tex_node.image.size[0]}x{tex_node.image.size[1]})")
                    else:
                        print(f"      ⚠️ Sin texturas")
        else:
            print("\n⚠️ NO SE ENCONTRARON MATERIALES")
        
        # Verificar animación
        if test_armature and test_armature.animation_data and test_armature.animation_data.action:
            test_action = test_armature.animation_data.action
            print(f"\n✅ Animación: {test_action.name}")
            print(f"✅ FCurves: {len(test_action.fcurves)}")
            
            # Test movimiento
            bpy.context.scene.frame_set(frame_start)
            if "LeftHand" in test_armature.pose.bones:
                bone_start = test_armature.pose.bones["LeftHand"].rotation_quaternion.copy()
                bpy.context.scene.frame_set(frame_end)
                bone_end = test_armature.pose.bones["LeftHand"].rotation_quaternion
                diff = sum(abs(a - b) for a, b in zip(bone_start, bone_end))
                
                if diff > 0.01:
                    print(f"✅ Animación FUNCIONANDO (diff: {diff:.3f})")
                else:
                    print(f"⚠️ Animación NO se mueve")
        else:
            print("\n❌ NO SE ENCONTRÓ ANIMACIÓN")
        
        print("\n" + "=" * 80)
        if test_materials and test_armature.animation_data:
            print("✅ ✅ ✅ ÉXITO TOTAL ✅ ✅ ✅")
            print("Archivo tiene TEXTURAS y ANIMACIÓN")
        elif test_materials:
            print("⚠️ ÉXITO PARCIAL: Texturas OK, pero sin animación")
        elif test_armature.animation_data:
            print("⚠️ ÉXITO PARCIAL: Animación OK, pero SIN TEXTURAS")
        else:
            print("❌ FALLO: Sin texturas ni animación")
        print("=" * 80)
        
    else:
        print("❌ ERROR: No se generó el archivo")
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
