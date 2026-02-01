import bpy
from pathlib import Path

# Rutas
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_ROKOKO.blend")

# Limpiar
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

print("Importando GLB (TARGET)...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))
glb_armature = bpy.context.selected_objects[0]
glb_armature.name = "Target_Armature"
print(f"✓ Target: {glb_armature.name}")

print("\nImportando FBX (SOURCE)...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))
fbx_objects = [obj for obj in bpy.context.selected_objects if obj != glb_armature]
fbx_armature = next((obj for obj in fbx_objects if obj.type == 'ARMATURE'), None)
fbx_armature.name = "Source_Armature"
print(f"✓ Source: {fbx_armature.name}")

# Verificar que Rokoko está disponible
print("\nVerificando addon de Rokoko...")
if 'rsl_comm_unity' in dir(bpy.ops):
    print("✓ Rokoko Studio Live detectado")
    
    # Mapeo de huesos para Rokoko
    bone_mapping = {
        'Bip001 L Clavicle': 'LeftShoulder',
        'Bip001 L UpperArm': 'LeftArm',
        'Bip001 L Forearm': 'LeftForeArm',
        'Bip001 L Hand': 'LeftHand',
        'Bip001 R Clavicle': 'RightShoulder',
        'Bip001 R UpperArm': 'RightArm',
        'Bip001 R Forearm': 'RightForeArm',
        'Bip001 R Hand': 'RightHand',
    }
    
    print("\nCONFIGURACIÓN MANUAL REQUERIDA:")
    print("="*80)
    print("Rokoko requiere configuración manual en la interfaz de Blender:")
    print("\n1. Ve a la pestaña 'Rokoko' en el panel derecho")
    print("2. En 'Retargeting', configura:")
    print("   - Source Armature: Source_Armature")
    print("   - Target Armature: Target_Armature")
    print("\n3. Mapea los huesos:")
    for fbx_bone, glb_bone in bone_mapping.items():
        print(f"   {fbx_bone} -> {glb_bone}")
    print("\n4. Haz clic en 'Build Bone List' y luego 'Retarget Animation'")
    print("="*80)
    
else:
    print("✗ Rokoko Studio Live NO detectado")
    print("\nUSANDO MÉTODO ALTERNATIVO CON NLA...")
    
    # Método alternativo: usar NLA para combinar animaciones
    # Seleccionar GLB
    bpy.context.view_layer.objects.active = glb_armature
    glb_armature.select_set(True)
    
    # Crear una acción si no existe
    if not glb_armature.animation_data:
        glb_armature.animation_data_create()
    
    if not glb_armature.animation_data.action:
        action = bpy.data.actions.new(name="CombinedAction")
        glb_armature.animation_data.action = action
    
    print("\nUSA ROKOKO MANUALMENTE:")
    print("1. Abre Blender en modo GUI")
    print("2. Abre este archivo guardado")
    print("3. Usa la interfaz de Rokoko para retargetear")

# Guardar archivo preparado
output_path.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(output_path))
print(f"\n✓ Archivo guardado: {output_path}")
print("\n¡ABRE ESTE ARCHIVO EN BLENDER GUI Y USA ROKOKO PARA RETARGETEAR!")
