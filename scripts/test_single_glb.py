import bpy
from pathlib import Path
import time

#"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python scripts\test_single_glb.py

print("="*80)
print("TEST ÚNICO GLB: Probando conversión individual")
print("="*80)

# Rutas base
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output")
BLEND_INPUT_DIR = BASE_DIR / "blend" / "cortesia"

def clear_scene():
    """Limpia completamente la escena"""
    if bpy.context.active_object and bpy.context.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    for collection in bpy.data.collections:
        bpy.data.collections.remove(collection)

def fix_animation_for_glb_export(armature):
    """Corrige problemas comunes de animación para exportación GLB"""
    print(f"   🔧 Corrigiendo animación en {armature.name}...")
    
    # 1. Asegurar que hay animation_data
    if not armature.animation_data:
        armature.animation_data_create()
        print(f"      ✅ Animation data creado")
    
    # 2. CRÍTICO: Desactivar NLA si está activado
    if armature.animation_data.use_nla:
        armature.animation_data.use_nla = False
        print(f"      ✅ NLA desactivado (era el problema principal)")
    
    # 3. Verificar que hay acción asignada
    if not armature.animation_data.action:
        actions = bpy.data.actions
        if actions:
            best_action = max(actions, key=lambda a: len(a.fcurves))
            armature.animation_data.action = best_action
            print(f"      ✅ Acción asignada: {best_action.name}")
    else:
        action = armature.animation_data.action
        print(f"      ✅ Acción ya asignada: {action.name}")
        
        # Configurar timeline
        frame_start, frame_end = action.frame_range
        bpy.context.scene.frame_start = max(1, int(frame_start))
        bpy.context.scene.frame_end = int(frame_end)
        print(f"      ✅ Timeline: frames {bpy.context.scene.frame_start} - {bpy.context.scene.frame_end}")
    
    return True

def export_glb_test(blend_file, output_glb):
    """Exporta GLB con configuración simplificada y funcional"""
    print(f"   📤 Exportando GLB...")
    
    bpy.ops.object.select_all(action='SELECT')
    
    try:
        bpy.ops.export_scene.gltf(
            filepath=str(output_glb),
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
            export_apply=False,
            export_materials='EXPORT',
            export_image_format='AUTO',
            export_texture_dir='',
            export_texcoords=True,
            export_normals=True,
            export_yup=True,
            export_extras=False,
            export_cameras=False,
            export_lights=False,
            use_selection=False,
            use_visible=True,
            use_renderable=True,
            use_active_collection=False
        )
        
        if output_glb.exists():
            size_mb = output_glb.stat().st_size / (1024 * 1024)
            print(f"      ✅ GLB exportado: {size_mb:.1f} MB")
            return True
        else:
            print(f"      ❌ ERROR: Archivo GLB no se generó")
            return False
            
    except Exception as e:
        print(f"      ❌ ERROR en exportación: {e}")
        return False

def verify_glb_test(glb_path):
    """Verifica rápidamente el GLB"""
    print(f"   🧪 Verificando GLB...")
    
    try:
        clear_scene()
        bpy.ops.import_scene.gltf(filepath=str(glb_path))
        
        armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
        actions = list(bpy.data.actions)
        
        if armatures and armatures[0].animation_data and armatures[0].animation_data.action:
            action = armatures[0].animation_data.action
            print(f"      ✅ Animación funcional: {action.name} ({len(action.fcurves)} FCurves)")
            return True
        else:
            print(f"      ❌ Sin animación en GLB")
            return False
            
    except Exception as e:
        print(f"      ❌ Error en verificación: {e}")
        return False

# Test con un archivo específico
blend_file = BLEND_INPUT_DIR / "Nancy_a la orden.blend"
glb_output = BLEND_INPUT_DIR / "Nancy_a la orden_TEST.glb"

print(f"\n🧪 PROBANDO: {blend_file.name}")

if not blend_file.exists():
    print(f"❌ ERROR: No existe {blend_file}")
    exit(1)

try:
    # 1. Cargar .blend
    print(f"📂 Cargando {blend_file.name}...")
    clear_scene()
    bpy.ops.wm.open_mainfile(filepath=str(blend_file))
    
    # 2. Verificar armature
    armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
    if not armatures:
        print(f"❌ ERROR: No hay armature")
        exit(1)
    
    armature = armatures[0]
    print(f"✅ Armature: {armature.name}")
    
    # 3. Corregir animación
    if not fix_animation_for_glb_export(armature):
        print(f"❌ ERROR: No se pudo corregir animación")
        exit(1)
    
    # 4. Exportar
    if not export_glb_test(blend_file, glb_output):
        print(f"❌ ERROR: Exportación falló")
        exit(1)
    
    # 5. Verificar
    if not verify_glb_test(glb_output):
        print(f"❌ ERROR: GLB no funcional")
        exit(1)
    
    print(f"\n🎉 ¡ÉXITO! GLB funcional generado: {glb_output.name}")
    
except Exception as e:
    print(f"❌ ERROR GENERAL: {e}")
    import traceback
    traceback.print_exc()
    exit(1)