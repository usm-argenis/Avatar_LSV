import bpy

"""
Script de VISUALIZACIÓN de correcciones aplicadas
Ejecutar este script en Blender (interfaz gráfica) para ver los cambios
"""

def visualize_corrections():
    """
    Abre el archivo corregido y configura la vista para visualizar los cambios
    """
    print("\n" + "="*80)
    print("👁️ MODO VISUALIZACIÓN - Revisión de Correcciones")
    print("="*80)
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Importar el archivo CORREGIDO
    corrected_file = r"C:\Users\andre\Downloads\r_default_fixed.glb"
    print(f"\n📥 Cargando archivo corregido: {corrected_file}")
    bpy.ops.import_scene.gltf(filepath=corrected_file)
    
    # Buscar armadura
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        print("❌ No se encontró armadura")
        return
    
    # Configurar vista
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    
    # Seleccionar solo los huesos modificados para facilitar visualización
    bpy.ops.pose.select_all(action='DESELECT')
    
    finger_bones = [
        'LeftHandIndex1', 'LeftHandIndex2', 'LeftHandIndex3',
        'LeftHandMiddle1', 'LeftHandMiddle2', 'LeftHandMiddle3',
        'RightHandIndex1', 'RightHandIndex2', 'RightHandIndex3',
        'RightHandMiddle1', 'RightHandMiddle2', 'RightHandMiddle3'
    ]
    
    for bone_name in finger_bones:
        if bone_name in armature.pose.bones:
            armature.pose.bones[bone_name].bone.select = True
    
    # Configurar timeline para el rango de interés
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 50
    bpy.context.scene.frame_current = 30  # Frame donde inician las correcciones
    
    print("\n✓ Archivo cargado y configurado")
    print("\n📋 INSTRUCCIONES PARA REVISAR:")
    print("-" * 80)
    print("1. Los huesos de dedos índice y medio están seleccionados (naranja)")
    print("2. El timeline está configurado en el frame 30")
    print("3. Usa la barra espaciadora para reproducir la animación")
    print("4. Los frames 30-37 muestran el cierre de dedos")
    print("5. Observa que los dedos se cierran suavemente sin temblor")
    print("\n🎬 FRAMES CLAVE:")
    print("   • Frame 1-29: Animación original (sin cambios)")
    print("   • Frame 30-37: DEDOS CERRADOS EN PUÑO (corrección aplicada)")
    print("   • Frame 38+: Animación original (sin cambios)")
    print("\n🖐️ HUESOS MODIFICADOS:")
    for bone_name in finger_bones:
        if bone_name in armature.pose.bones:
            print(f"   ✓ {bone_name}")
    
    print("\n" + "="*80)

if __name__ == "__main__":
    visualize_corrections()
