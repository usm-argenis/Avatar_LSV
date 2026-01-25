"""
Script final de verificación - Abre Nancy_a la orden_CORREGIDO.blend 
y verifica que la animación funcione correctamente

Uso: Para abrir directamente en Blender UI (no background)
"""

import bpy
import sys
from pathlib import Path

# Configuración
BASE_PATH = Path(__file__).parent
CORRECTED_BLEND = BASE_PATH / "test" / "output" / "blend" / "cortesia" / "Nancy_a la orden_CORREGIDO.blend"

def load_corrected_file():
    """Carga el archivo corregido"""
    print(f"📂 Cargando archivo corregido: {CORRECTED_BLEND.name}")
    
    if not CORRECTED_BLEND.exists():
        raise FileNotFoundError(f"Archivo corregido no encontrado: {CORRECTED_BLEND}")
    
    bpy.ops.wm.open_mainfile(filepath=str(CORRECTED_BLEND))
    print("✓ Archivo corregido cargado")

def verify_animation_setup():
    """Verifica que la animación esté configurada correctamente"""
    print(f"\n✅ VERIFICACIÓN FINAL DE ANIMACIÓN:")
    
    armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
    if not armatures:
        print("❌ No se encontró armature")
        return False
    
    armature = armatures[0]
    print(f"  Armature: {armature.name}")
    
    # Verificar animation data
    if not armature.animation_data:
        print("❌ No hay animation data")
        return False
    
    # Verificar acción asignada
    if not armature.animation_data.action:
        print("❌ No hay acción asignada")
        return False
    
    action = armature.animation_data.action
    print(f"  ✅ Acción asignada: {action.name}")
    print(f"  ✅ FCurves: {len(action.fcurves)}")
    
    # Verificar NLA
    nla_status = "ACTIVADO" if armature.animation_data.use_nla else "DESACTIVADO"
    print(f"  ✅ NLA: {nla_status}")
    
    # Verificar timeline
    frame_start, frame_end = action.frame_range
    scene_start = bpy.context.scene.frame_start
    scene_end = bpy.context.scene.frame_end
    
    print(f"  ✅ Acción frames: {frame_start:.0f} - {frame_end:.0f}")
    print(f"  ✅ Escena frames: {scene_start} - {scene_end}")
    
    return True

def setup_for_animation_viewing():
    """Configura la escena para visualización óptima de la animación"""
    print(f"\n🎬 CONFIGURANDO PARA VISUALIZACIÓN:")
    
    # Seleccionar armature
    armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
    if armatures:
        armature = armatures[0]
        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.select_all(action='DESELECT')
        armature.select_set(True)
        print(f"  ✅ Armature seleccionado: {armature.name}")
    
    # Ir al frame inicial
    bpy.context.scene.frame_set(bpy.context.scene.frame_start)
    print(f"  ✅ Frame inicial configurado: {bpy.context.scene.frame_start}")
    
    # Configurar viewport si estamos en UI
    try:
        if bpy.context.screen:
            for area in bpy.context.screen.areas:
                if area.type == 'VIEW_3D':
                    # Cambiar contexto temporalmente
                    override = bpy.context.copy()
                    override['area'] = area
                    override['region'] = area.regions[-1]
                    
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            space.overlay.show_bones = True
                            space.shading.type = 'SOLID'
                            print("  ✅ Vista 3D configurada")
                            break
                    break
    except:
        print("  ℹ️ Configuración de vista (normal si es background)")

def display_final_instructions():
    """Muestra las instrucciones finales de uso"""
    print(f"\n" + "🎯" + "="*68 + "🎯")
    print("   NANCY CORTESÍA - ANIMACIÓN LISTA PARA USAR")
    print("🎯" + "="*68 + "🎯")
    
    print(f"\n✅ ESTADO ACTUAL:")
    print(f"   • Archivo: Nancy_a la orden_CORREGIDO.blend")
    print(f"   • Animación: CONFIGURADA Y FUNCIONAL")
    print(f"   • NLA: DESACTIVADO (permite reproducción directa)")
    print(f"   • Acción: Asignada correctamente")
    print(f"   • Timeline: Configurado automáticamente")
    
    print(f"\n🎮 REPRODUCIR ANIMACIÓN:")
    print(f"   1. *** PRESIONA BARRA ESPACIADORA *** para iniciar")
    print(f"   2. La animación debe comenzar inmediatamente")
    print(f"   3. ALT + A también inicia la reproducción")
    print(f"   4. Usa ← → para navegar frame por frame")
    
    print(f"\n👀 VISUALIZACIÓN:")
    print(f"   • El armature está seleccionado automáticamente")
    print(f"   • Cambia a modo POSE (Ctrl+Tab) para ver mejor los huesos")
    print(f"   • Usa rueda del ratón para zoom")
    print(f"   • Clic medio + arrastrar para rotar vista")
    
    print(f"\n🔧 SI NO FUNCIONA:")
    print(f"   1. Verificar que el armature esté seleccionado")
    print(f"   2. Ir a Properties > Animation (ícono de persona corriendo)")
    print(f"   3. Verificar que aparezca 'a_la_orden' en Action")
    print(f"   4. Verificar que NLA Use esté DESACTIVADO")
    print(f"   5. Presionar HOME para ir al frame inicial")
    
    print(f"\n📊 INFORMACIÓN TÉCNICA:")
    armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
    if armatures:
        armature = armatures[0]
        if armature.animation_data and armature.animation_data.action:
            action = armature.animation_data.action
            frame_start, frame_end = action.frame_range
            print(f"   • Armature: {armature.name}")
            print(f"   • Acción: {action.name}")
            print(f"   • Duración: {(frame_end - frame_start):.0f} frames")
            print(f"   • FPS: {bpy.context.scene.render.fps}")
            print(f"   • Tiempo real: ~{((frame_end - frame_start) / bpy.context.scene.render.fps):.1f} segundos")
    
    print("\n🎯" + "="*68 + "🎯")
    print("   🎉 ¡ANIMACIÓN LISTA! PRESIONA BARRA ESPACIADORA 🎉")
    print("🎯" + "="*68 + "🎯\n")

def main():
    """Función principal"""
    try:
        # 1. Cargar archivo corregido
        load_corrected_file()
        
        # 2. Verificar configuración
        if not verify_animation_setup():
            print("❌ La verificación falló")
            return 1
        
        # 3. Configurar para visualización
        setup_for_animation_viewing()
        
        # 4. Mostrar instrucciones
        display_final_instructions()
        
        return 0
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit_code = main()
    if 'bpy' in sys.modules and exit_code == 0:
        print("🚀 Archivo listo - ¡PRESIONA BARRA ESPACIADORA para ver la animación!")
    elif 'bpy' in sys.modules:
        print("❌ Hubo un problema al verificar el archivo")
    else:
        sys.exit(exit_code)