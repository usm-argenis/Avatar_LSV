import bpy
from pathlib import Path

result_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_CORRECTO.blend")
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")

# Abrir resultado
bpy.ops.wm.open_mainfile(filepath=str(result_path))

glb_armature = bpy.data.objects['GLB']

# Importar FBX original
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_armature = None
for obj in bpy.context.selected_objects:
    if obj.type == 'ARMATURE':
        fbx_armature = obj
        break

# Posicionar lado a lado
fbx_armature.location.x = 1.5

# Escalar FBX al tamaño del GLB
fbx_armature.scale = (0.0123, 0.0123, 0.0123)

# Aplicar transformaciones
bpy.context.view_layer.update()

# Verificar visualmente en frames clave
test_frames = [10, 30, 50, 70]

print("\n" + "="*80)
print("VERIFICACIÓN VISUAL LADO A LADO")
print("="*80)

for frame in test_frames:
    bpy.context.scene.frame_set(frame)
    bpy.context.view_layer.update()
    
    print(f"\nFRAME {frame}:")
    
    # Comparar posiciones de manos en WORLD space
    glb_left_hand = glb_armature.pose.bones['LeftHand']
    fbx_left_hand = fbx_armature.pose.bones['Bip001 L Hand']
    
    glb_hand_world = glb_armature.matrix_world @ glb_left_hand.matrix
    fbx_hand_world = fbx_armature.matrix_world @ fbx_left_hand.matrix
    
    glb_hand_pos = glb_hand_world.translation
    fbx_hand_pos = fbx_hand_world.translation
    
    distance = (glb_hand_pos - fbx_hand_pos).length
    
    print(f"  Mano izquierda GLB: {glb_hand_pos}")
    print(f"  Mano izquierda FBX: {fbx_hand_pos}")
    print(f"  Distancia: {distance:.4f}")
    
    if distance < 0.1:
        print(f"  ✓ POSICIONES SIMILARES")
    elif distance < 0.3:
        print(f"  ⚠ ALGO DIFERENTE")
    else:
        print(f"  ✗ MUY DIFERENTE")

# Guardar archivo de comparación
comp_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\VERIFICACION_LADO_A_LADO.blend")
bpy.ops.wm.save_as_mainfile(filepath=str(comp_path))

print("\n" + "="*80)
print(f"✓ Guardado: {comp_path}")
print("\nAbre este archivo y reproduce la animación.")
print("GLB (izquierda) y FBX escalado (derecha) deben moverse igual.")
print("="*80)
