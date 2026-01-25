"""
Regenerar SOLO buenos dias en saludos
"""

import bpy
from pathlib import Path
import time

print("="*80)
print("REGENERAR: saludos/buenos dias")
print("="*80)

BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_MODEL = BASE_DIR / "Nancy" / "Nancy.glb"
BLEND_OUTPUT_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\blend")

def retarget_animacion():
    """Retargetear buenos dias de Nina a Nancy usando Rokoko"""
    
    categoria = "saludos"
    animacion_nombre = "buenos dias"
    
    print(f"\n{'='*80}")
    print(f"📝 {categoria.upper()} → {animacion_nombre}")
    print(f"{'='*80}")
    
    nina_file = BASE_DIR / "Nina" / categoria / f"Nina_resultado_{animacion_nombre}.glb"
    blend_output = BLEND_OUTPUT_DIR / categoria / f"Nancy_{animacion_nombre}.blend"
    
    if not nina_file.exists():
        print(f"❌ ERROR: No existe {nina_file}")
        return False
    
    print(f"✅ Archivo fuente encontrado: {nina_file.stat().st_size / 1024:.1f} KB")
    
    try:
        # Limpiar escena
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar Nancy (destino)
        print(f"📦 Importando Nancy...")
        bpy.ops.import_scene.gltf(filepath=str(NANCY_MODEL))
        
        nancy_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                nancy_armature = obj
                break
        
        if not nancy_armature:
            print("❌ ERROR: No se encontró armature de Nancy")
            return False
        
        print(f"   ✅ Nancy Armature: {nancy_armature.name}")
        
        # Importar Nina (fuente de animación)
        print(f"📦 Importando Nina...")
        bpy.ops.import_scene.gltf(filepath=str(nina_file))
        
        nina_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != nancy_armature:
                nina_armature = obj
                break
        
        if not nina_armature:
            print("❌ ERROR: No se encontró armature de Nina")
            return False
        
        print(f"   ✅ Nina Armature: {nina_armature.name}")
        
        # Verificar que Nina tenga animación
        if not nina_armature.animation_data or not nina_armature.animation_data.action:
            print("❌ ERROR: Nina no tiene animación")
            return False
        
        nina_action = nina_armature.animation_data.action
        print(f"   ✅ Acción de Nina: {nina_action.name} ({nina_action.frame_range[0]:.0f}-{nina_action.frame_range[1]:.0f})")
        
        # Seleccionar Nancy
        bpy.ops.object.select_all(action='DESELECT')
        nancy_armature.select_set(True)
        bpy.context.view_layer.objects.active = nancy_armature
        
        # Aplicar retargeting con Rokoko
        print(f"🎯 Iniciando retargeting con Rokoko...")
        
        bpy.ops.rsl.retarget(
            armature_source=nina_armature.name,
            use_actor=False,
            remap_to_arp=False
        )
        
        print(f"   ✅ Retargeting aplicado")
        
        # Verificar resultado
        if not nancy_armature.animation_data or not nancy_armature.animation_data.action:
            print("❌ ERROR: No se generó animación en Nancy")
            return False
        
        nancy_action = nancy_armature.animation_data.action
        print(f"   ✅ Acción generada: {nancy_action.name}")
        
        # Configurar escena
        frame_start, frame_end = nancy_action.frame_range
        bpy.context.scene.frame_start = int(frame_start)
        bpy.context.scene.frame_end = int(frame_end)
        bpy.context.scene.frame_set(int(frame_start))
        
        # Eliminar Nina
        print(f"🧹 Limpiando escena...")
        bpy.ops.object.select_all(action='DESELECT')
        nina_armature.select_set(True)
        for child in nina_armature.children:
            child.select_set(True)
        bpy.ops.object.delete()
        
        # Guardar blend
        blend_output.parent.mkdir(parents=True, exist_ok=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_output))
        
        if blend_output.exists():
            size_mb = blend_output.stat().st_size / (1024 * 1024)
            print(f"   ✅ ÉXITO: {size_mb:.2f} MB")
            print(f"   📁 Guardado en: {blend_output}")
            return True
        else:
            print(f"   ❌ No se guardó el archivo")
            return False
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

# Ejecutar
inicio = time.time()
exito = retarget_animacion()
tiempo = time.time() - inicio

print(f"\n{'='*80}")
print(f"RESUMEN")
print(f"{'='*80}")
print(f"⏱️ Tiempo: {tiempo:.1f} segundos")
print(f"✅ Resultado: {'ÉXITO' if exito else 'FALLIDO'}")
print(f"{'='*80}")
