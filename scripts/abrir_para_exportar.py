import bpy
import sys

print("\n" + "="*70)
print("EXPORTAR FBX DESDE BLENDER GUI - Script Automático")
print("="*70)

# Este script se ejecutará DENTRO de Blender con GUI abierta
# El usuario solo necesita ejecutar File → Export → FBX después

# Abrir el archivo .blend
blend_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\Leonard_con_animacion_b.blend"
bpy.ops.wm.open_mainfile(filepath=blend_path)

print(f"\n✓ Archivo abierto: {blend_path}")

# Verificar animación
arm = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        arm = obj
        break

if arm and arm.animation_data and arm.animation_data.action:
    action = arm.animation_data.action
    print(f"\n✓ Animación: {action.name}")
    print(f"  Frames: {int(action.frame_range[0])} - {int(action.frame_range[1])}")
    print(f"  FCurves: {len(action.fcurves)}")
    
    # Configurar el timeline
    bpy.context.scene.frame_start = int(action.frame_range[0])
    bpy.context.scene.frame_end = int(action.frame_range[1])
    bpy.context.scene.frame_set(1)
    
    print("\n" + "="*70)
    print("INSTRUCCIONES:")
    print("="*70)
    print("\n1. Presiona ESPACIO para verificar la animación")
    print("\n2. Ve a: File → Export → FBX (.fbx)")
    print("\n3. En el panel de exportación (derecha):")
    print("   - Navega a: output/")
    print("   - Nombre: Leonard_con_animacion_b.fbx")
    print("   - Expande 'Armature' tab:")
    print("     ✓ Primary Bone Axis: Y Forward")
    print("     ✓ Secondary Bone Axis: X Up")
    print("   - Expande 'Bake Animation' tab:")
    print("     ✓ Marcar 'Baked Animation'")
    print("     ✓ Marcar 'Key All Bones'")
    print("     ✓ Marcar 'Force Start/End Keying'")
    print("     ✓ Sampling Rate: 1.0")
    print("     ✓ Simplify: 0.0")
    print("\n4. Click en 'Export FBX'")
    print("\n" + "="*70)
else:
    print("\n❌ ERROR: No hay animación")
    sys.exit(1)
