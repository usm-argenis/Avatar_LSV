"""
Script para convertir los archivos 'buenos dias' que faltaron
"""

import bpy
from pathlib import Path
import time

print("="*80)
print("CONVERTIR BUENOS DIAS - LOS ARCHIVOS FALTANTES")
print("="*80)

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\blend")

# Los dos archivos que faltaron
ARCHIVOS = [
    ("cortesia", "buenos dias"),
    ("saludos", "buenos dias")
]

def encontrar_accion_con_movimiento(armature, actions):
    """Encuentra la acción que tiene movimiento real"""
    print(f"   🔍 Analizando {len(actions)} acciones...")
    
    for action in actions:
        if not armature.animation_data:
            armature.animation_data_create()
        
        armature.animation_data.action = action
        armature.animation_data.use_nla = False
        
        frame_start, frame_end = action.frame_range
        
        if 'Hips' in armature.pose.bones:
            bpy.context.scene.frame_set(int(frame_start))
            bpy.context.view_layer.update()
            
            pos_start = armature.pose.bones['Hips'].matrix.translation.copy()
            
            bpy.context.scene.frame_set(int(frame_end))
            bpy.context.view_layer.update()
            
            pos_end = armature.pose.bones['Hips'].matrix.translation.copy()
            movement = (pos_start - pos_end).length
            
            if movement > 0.001:
                print(f"   ✅ Acción con movimiento: {action.name} (movimiento: {movement:.4f})")
                return action
    
    return None

def convertir_blend_a_glb(categoria, animacion_nombre):
    """Convierte un archivo .blend a GLB funcional"""
    
    print(f"\n{'='*80}")
    print(f"📝 {categoria.upper()} → {animacion_nombre}")
    print(f"{'='*80}")
    
    blend_file = BASE_DIR / categoria / f"Nancy_{animacion_nombre}.blend"
    glb_output = BASE_DIR / categoria / f"Nancy_{animacion_nombre}.glb"
    
    if not blend_file.exists():
        print(f"❌ No existe: {blend_file}")
        return False
    
    try:
        bpy.ops.wm.open_mainfile(filepath=str(blend_file))
        
        armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
        if not armatures:
            print("❌ No hay armature")
            return False
        
        armature = armatures[0]
        print(f"   Armature: {armature.name}")
        
        actions = list(bpy.data.actions)
        if not actions:
            print("❌ No hay acciones")
            return False
        
        print(f"   Acciones totales: {len(actions)}")
        
        good_action = encontrar_accion_con_movimiento(armature, actions)
        
        if not good_action:
            print("❌ No se encontró acción con movimiento")
            return False
        
        actions_to_remove = []
        for action in bpy.data.actions:
            if action != good_action:
                actions_to_remove.append(action)
        
        print(f"   🗑️ Eliminando {len(actions_to_remove)} acciones inservibles...")
        for action in actions_to_remove:
            bpy.data.actions.remove(action)
        
        if not armature.animation_data:
            armature.animation_data_create()
        
        armature.animation_data.action = good_action
        armature.animation_data.use_nla = False
        
        frame_start, frame_end = good_action.frame_range
        bpy.context.scene.frame_start = int(frame_start)
        bpy.context.scene.frame_end = int(frame_end)
        bpy.context.scene.frame_set(int(frame_start))
        
        print(f"   ✅ Configurado: {good_action.name} ({frame_start:.0f}-{frame_end:.0f})")
        
        print(f"   📤 Exportando GLB...")
        
        bpy.ops.object.select_all(action='SELECT')
        
        bpy.ops.export_scene.gltf(
            filepath=str(glb_output),
            export_format='GLB',
            export_image_format='AUTO',
            export_texcoords=True,
            export_normals=True,
            export_draco_mesh_compression_enable=False,
            export_materials='EXPORT',
            export_cameras=False,
            use_selection=False,
            use_visible=True,
            use_renderable=True,
            use_active_collection=False,
            export_yup=True,
            export_apply=False,
            export_animations=True,
            export_frame_range=True,
            export_frame_step=1,
            export_force_sampling=True,
            export_nla_strips=False,
            export_def_bones=True,
            export_skins=True,
            export_morph=True,
            export_lights=False
        )
        
        if glb_output.exists():
            size_kb = glb_output.stat().st_size / 1024
            print(f"   ✅ ÉXITO: {size_kb:.1f} KB")
            return True
        else:
            print(f"   ❌ No se generó el archivo")
            return False
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

# MAIN
inicio = time.time()
exitosos = []
fallidos = []

for categoria, animacion in ARCHIVOS:
    exito = convertir_blend_a_glb(categoria, animacion)
    
    if exito:
        exitosos.append(f"{categoria}/{animacion}")
    else:
        fallidos.append(f"{categoria}/{animacion}")

tiempo_total = time.time() - inicio

print(f"\n{'='*80}")
print(f"RESUMEN")
print(f"{'='*80}")
print(f"⏱️ Tiempo: {tiempo_total:.1f} segundos")
print(f"✅ Exitosos: {len(exitosos)}/{len(ARCHIVOS)}")
print(f"❌ Fallidos: {len(fallidos)}/{len(ARCHIVOS)}")

if exitosos:
    print(f"\n✅ Archivos convertidos:")
    for item in exitosos:
        print(f"   - {item}")

if fallidos:
    print(f"\n❌ Archivos fallidos:")
    for item in fallidos:
        print(f"   - {item}")

print(f"\n{'='*80}")
print(f"🎉 CONVERSIÓN COMPLETADA")
print(f"{'='*80}")
