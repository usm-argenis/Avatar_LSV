"""
Diagnóstico completo y solución para exportación GLB con animaciones
NO mostrar al usuario hasta que funcione al 100%
"""

import bpy
import sys
from pathlib import Path
import time

# Configuración
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output")
BLEND_DIR = BASE_DIR / "blend" / "cortesia"
TEST_BLEND = BLEND_DIR / "Nancy_a la orden.blend"

print("\n" + "="*80)
print("DIAGNÓSTICO COMPLETO - EXPORTACIÓN GLB")
print("="*80)

def test_1_load_blend():
    """Test 1: Cargar el archivo .blend"""
    print("\n🔍 TEST 1: Cargando archivo .blend...")
    
    if not TEST_BLEND.exists():
        print(f"❌ No existe: {TEST_BLEND}")
        return False
    
    try:
        bpy.ops.wm.open_mainfile(filepath=str(TEST_BLEND))
        print(f"✅ Archivo cargado: {TEST_BLEND.name}")
        
        # Información básica
        armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
        meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
        actions = list(bpy.data.actions)
        materials = list(bpy.data.materials)
        images = list(bpy.data.images)
        
        print(f"   Armatures: {len(armatures)}")
        print(f"   Mallas: {len(meshes)}")
        print(f"   Acciones: {len(actions)}")
        print(f"   Materiales: {len(materials)}")
        print(f"   Imágenes: {len(images)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_2_check_animation():
    """Test 2: Verificar que hay animación funcional"""
    print("\n🔍 TEST 2: Verificando animación...")
    
    armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
    if not armatures:
        print("❌ No hay armature")
        return None
    
    armature = armatures[0]
    print(f"   Armature: {armature.name}")
    
    # Verificar animation data
    if not armature.animation_data:
        print("❌ No hay animation_data")
        return None
    
    if not armature.animation_data.action:
        print("❌ No hay action asignada")
        return None
    
    action = armature.animation_data.action
    frame_start, frame_end = action.frame_range
    
    print(f"✅ Acción: {action.name}")
    print(f"   FCurves: {len(action.fcurves)}")
    print(f"   Rango: {frame_start:.0f} - {frame_end:.0f}")
    
    # Verificar movimiento real
    if armature.pose.bones:
        bpy.context.scene.frame_set(int(frame_start))
        bpy.context.view_layer.update()
        
        test_bone = armature.pose.bones[0]
        pos_start = test_bone.matrix.translation.copy()
        
        bpy.context.scene.frame_set(int(frame_end))
        bpy.context.view_layer.update()
        
        pos_end = test_bone.matrix.translation.copy()
        movement = (pos_start - pos_end).length
        
        print(f"   Movimiento {test_bone.name}: {movement:.4f}")
        
        if movement > 0.001:
            print("✅ HAY MOVIMIENTO REAL")
            return armature
        else:
            print("⚠️ Poco movimiento detectado")
            return armature
    
    return armature

def test_3_check_materials():
    """Test 3: Verificar materiales y texturas"""
    print("\n🔍 TEST 3: Verificando materiales y texturas...")
    
    meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
    if not meshes:
        print("❌ No hay mallas")
        return False
    
    print(f"   Mallas: {len(meshes)}")
    
    total_materials = 0
    total_textures = 0
    
    for mesh in meshes:
        materials = mesh.data.materials
        if materials:
            total_materials += len(materials)
            for mat in materials:
                if mat and mat.use_nodes:
                    for node in mat.node_tree.nodes:
                        if node.type == 'TEX_IMAGE' and node.image:
                            total_textures += 1
    
    print(f"✅ Total materiales: {total_materials}")
    print(f"✅ Total texturas: {total_textures}")
    
    if total_materials > 0 and total_textures > 0:
        return True
    
    print("⚠️ Faltan materiales o texturas")
    return False

def test_4_export_glb_method_1(armature):
    """Test 4: Método 1 - Exportación estándar"""
    print("\n🔍 TEST 4: Método 1 - Exportación estándar...")
    
    output_file = BLEND_DIR / "TEST_metodo1.glb"
    
    try:
        # Seleccionar todo
        bpy.ops.object.select_all(action='SELECT')
        
        # Exportar
        bpy.ops.export_scene.gltf(
            filepath=str(output_file),
            export_format='GLB',
            export_animations=True,
            export_frame_range=True,
            export_force_sampling=True,
            export_animation_mode='ACTIONS',
            export_def_bones=True,
            export_skins=True,
            export_materials='EXPORT',
            export_texcoords=True,
            export_normals=True,
            use_selection=False
        )
        
        if output_file.exists():
            size_kb = output_file.stat().st_size / 1024
            print(f"✅ Exportado: {size_kb:.1f} KB")
            return output_file
        else:
            print("❌ No se generó el archivo")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_5_verify_exported_glb(glb_file):
    """Test 5: Verificar GLB exportado"""
    print(f"\n🔍 TEST 5: Verificando GLB exportado...")
    
    if not glb_file or not glb_file.exists():
        print("❌ Archivo no existe")
        return False
    
    # Limpiar escena
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    try:
        # Importar GLB
        bpy.ops.import_scene.gltf(filepath=str(glb_file))
        
        armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
        meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
        actions = list(bpy.data.actions)
        materials = list(bpy.data.materials)
        
        print(f"   Armatures: {len(armatures)}")
        print(f"   Mallas: {len(meshes)}")
        print(f"   Acciones: {len(actions)}")
        print(f"   Materiales: {len(materials)}")
        
        # Verificar animación
        if armatures and armatures[0].animation_data and armatures[0].animation_data.action:
            action = armatures[0].animation_data.action
            print(f"✅ Animación: {action.name}")
            print(f"   FCurves: {len(action.fcurves)}")
            
            # Verificar movimiento
            if armatures[0].pose.bones:
                frame_start, frame_end = action.frame_range
                bpy.context.scene.frame_set(int(frame_start))
                bpy.context.view_layer.update()
                
                test_bone = armatures[0].pose.bones[0]
                pos_start = test_bone.matrix.translation.copy()
                
                bpy.context.scene.frame_set(int(frame_end))
                bpy.context.view_layer.update()
                
                pos_end = test_bone.matrix.translation.copy()
                movement = (pos_start - pos_end).length
                
                print(f"   Movimiento: {movement:.4f}")
                
                if movement > 0.001:
                    print("✅✅✅ GLB TIENE ANIMACIÓN FUNCIONAL")
                    return True
                else:
                    print("❌ No hay movimiento en GLB")
                    return False
        else:
            print("❌ GLB no tiene animación")
            return False
            
    except Exception as e:
        print(f"❌ Error al verificar: {e}")
        return False

def test_6_export_glb_method_2(armature):
    """Test 6: Método 2 - Con configuración optimizada"""
    print("\n🔍 TEST 6: Método 2 - Configuración optimizada...")
    
    # Recargar original
    bpy.ops.wm.open_mainfile(filepath=str(TEST_BLEND))
    
    armature = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE'][0]
    
    # Asegurar configuración de animación
    if not armature.animation_data:
        armature.animation_data_create()
    
    # Desactivar NLA
    if armature.animation_data.use_nla:
        armature.animation_data.use_nla = False
        print("   NLA desactivado")
    
    # Asegurar que hay acción
    if not armature.animation_data.action:
        actions = list(bpy.data.actions)
        if actions:
            armature.animation_data.action = actions[0]
            print(f"   Acción asignada: {actions[0].name}")
    
    action = armature.animation_data.action
    frame_start, frame_end = action.frame_range
    
    # Configurar escena
    bpy.context.scene.frame_start = int(frame_start)
    bpy.context.scene.frame_end = int(frame_end)
    bpy.context.scene.frame_set(int(frame_start))
    
    output_file = BLEND_DIR / "TEST_metodo2.glb"
    
    try:
        bpy.ops.object.select_all(action='SELECT')
        
        bpy.ops.export_scene.gltf(
            filepath=str(output_file),
            export_format='GLB',
            export_animations=True,
            export_frame_range=True,
            export_frame_step=1,
            export_force_sampling=True,
            export_animation_mode='ACTIONS',
            export_nla_strips=False,
            export_def_bones=True,
            export_skins=True,
            export_morph=True,
            export_materials='EXPORT',
            export_image_format='AUTO',
            export_texcoords=True,
            export_normals=True,
            export_draco_mesh_compression_enable=False,
            use_selection=False,
            use_visible=True,
            use_renderable=True
        )
        
        if output_file.exists():
            size_kb = output_file.stat().st_size / 1024
            print(f"✅ Exportado: {size_kb:.1f} KB")
            return output_file
        else:
            print("❌ No se generó")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None

def run_all_tests():
    """Ejecutar todos los tests"""
    print("\nINICIANDO BATERÍA DE TESTS...")
    
    results = {}
    
    # Test 1: Cargar blend
    results['load'] = test_1_load_blend()
    if not results['load']:
        print("\n❌ FALLO EN TEST 1 - No se puede continuar")
        return results
    
    # Test 2: Verificar animación
    armature = test_2_check_animation()
    results['animation'] = armature is not None
    if not results['animation']:
        print("\n❌ FALLO EN TEST 2 - No hay animación")
        return results
    
    # Test 3: Verificar materiales
    results['materials'] = test_3_check_materials()
    
    # Test 4: Método 1 de exportación
    glb1 = test_4_export_glb_method_1(armature)
    results['export_m1'] = glb1 is not None
    
    if glb1:
        # Test 5: Verificar GLB método 1
        results['verify_m1'] = test_5_verify_exported_glb(glb1)
        
        if results['verify_m1']:
            print("\n" + "🎉"*40)
            print("✅✅✅ MÉTODO 1 FUNCIONA AL 100% ✅✅✅")
            print("🎉"*40)
            return results
    
    # Test 6: Método 2 de exportación
    glb2 = test_6_export_glb_method_2(armature)
    results['export_m2'] = glb2 is not None
    
    if glb2:
        results['verify_m2'] = test_5_verify_exported_glb(glb2)
        
        if results['verify_m2']:
            print("\n" + "🎉"*40)
            print("✅✅✅ MÉTODO 2 FUNCIONA AL 100% ✅✅✅")
            print("🎉"*40)
            return results
    
    return results

# EJECUTAR
try:
    results = run_all_tests()
    
    print("\n" + "="*80)
    print("RESULTADOS FINALES")
    print("="*80)
    
    for test, result in results.items():
        status = "✅" if result else "❌"
        print(f"{status} {test}")
    
    # Determinar solución
    if results.get('verify_m1'):
        print("\n" + "🎯"*40)
        print("SOLUCIÓN ENCONTRADA: MÉTODO 1")
        print("🎯"*40)
    elif results.get('verify_m2'):
        print("\n" + "🎯"*40)
        print("SOLUCIÓN ENCONTRADA: MÉTODO 2")
        print("🎯"*40)
    else:
        print("\n❌ NINGÚN MÉTODO FUNCIONÓ - INVESTIGAR MÁS")
    
except Exception as e:
    print(f"\n❌ ERROR FATAL: {e}")
    import traceback
    traceback.print_exc()
