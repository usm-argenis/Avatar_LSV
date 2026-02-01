import bpy
from pathlib import Path

# Rutas
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\ROKOKO_RETARGET_PREPARADO.blend")

print("="*80)
print("PREPARANDO ARCHIVO PARA ROKOKO RETARGETING")
print("="*80)

# Limpiar
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Importar GLB (Target)
print("\nImportando GLB (DeepMotion - TARGET)...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))
glb_armature = bpy.context.selected_objects[0]
glb_armature.name = "DeepMotion_Target"

# Obtener meshes del GLB
glb_meshes = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

print(f"✓ Target armature: {glb_armature.name}")
print(f"✓ Meshes: {len(glb_meshes)}")

# Importar FBX (Source)
print("\nImportando FBX (QuickMagic - SOURCE)...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_objects = [obj for obj in bpy.context.selected_objects if obj != glb_armature and obj not in glb_meshes]
fbx_armature = next((obj for obj in fbx_objects if obj.type == 'ARMATURE'), None)
fbx_armature.name = "QuickMagic_Source"

# Obtener meshes del FBX
fbx_meshes = [obj for obj in fbx_objects if obj.type == 'MESH']

print(f"✓ Source armature: {fbx_armature.name}")
print(f"✓ Meshes: {len(fbx_meshes)}")

# Escalar FBX para que coincida con GLB (factor 0.0123)
scale_factor = 0.0123
fbx_armature.scale = (scale_factor, scale_factor, scale_factor)
for mesh in fbx_meshes:
    mesh.scale = (scale_factor, scale_factor, scale_factor)

# Mover FBX a un lado para verlos juntos
fbx_armature.location.x = 1.0
for mesh in fbx_meshes:
    mesh.location.x = 1.0

print(f"\n✓ FBX escalado por {scale_factor}")
print(f"✓ FBX movido 1.0 unidad en X")

# Actualizar escena
bpy.context.view_layer.update()

# Guardar
output_path.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(output_path))

print("\n" + "="*80)
print("ARCHIVO GUARDADO Y LISTO PARA ROKOKO")
print("="*80)
print(f"Ubicación: {output_path}")
print("\n" + "="*80)
print("INSTRUCCIONES PARA USAR ROKOKO STUDIO LIVE:")
print("="*80)
print("\n1. Abre este archivo en Blender (GUI)")
print("\n2. Presiona 'N' para abrir el panel derecho")
print("\n3. Ve a la pestaña 'Rokoko'")
print("\n4. En la sección 'Retargeting':")
print("   - Source Rig: QuickMagic_Source")
print("   - Target Rig: DeepMotion_Target")
print("\n5. IMPORTANTE - Mapea SOLO estos 8 huesos de BRAZOS:")
print("   ")
print("   BRAZO IZQUIERDO:")
print("   Bip001 L Clavicle  →  LeftShoulder")
print("   Bip001 L UpperArm  →  LeftArm")
print("   Bip001 L Forearm   →  LeftForeArm")
print("   Bip001 L Hand      →  LeftHand")
print("   ")
print("   BRAZO DERECHO:")
print("   Bip001 R Clavicle  →  RightShoulder")
print("   Bip001 R UpperArm  →  RightArm")
print("   Bip001 R Forearm   →  RightForeArm")
print("   Bip001 R Hand      →  RightHand")
print("\n6. Click 'Build Bone List'")
print("\n7. Click 'Bake to Rig' o 'Retarget Animation'")
print("   - Frame Start: 1")
print("   - Frame End: 73")
print("   - Bake only selected bones: SÍ")
print("\n8. Elimina QuickMagic_Source cuando termines")
print("\n9. Exporta DeepMotion_Target como GLB")
print("\n" + "="*80)
print("NOTA: Rokoko maneja automáticamente las diferencias entre")
print("DeepMotion y QuickMagic gracias a su sistema de retargeting.")
print("="*80)
