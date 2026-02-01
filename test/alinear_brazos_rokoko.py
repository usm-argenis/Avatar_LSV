import bpy
from pathlib import Path
import mathutils

# Rutas
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_ROKOKO_ALINEADO.blend")

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

# Calcular posición de los brazos en ambos modelos
print("\nCalculando posiciones de brazos...")

# Usar LeftArm como referencia para alinear
fbx_left_arm = None
glb_left_arm = None

if 'Bip001 L UpperArm' in fbx_armature.data.bones:
    fbx_left_arm = fbx_armature.data.bones['Bip001 L UpperArm']
    print(f"FBX LeftArm encontrado: {fbx_left_arm.name}")

if 'LeftArm' in glb_armature.data.bones:
    glb_left_arm = glb_armature.data.bones['LeftArm']
    print(f"GLB LeftArm encontrado: {glb_left_arm.name}")

if fbx_left_arm and glb_left_arm:
    # Obtener posiciones en world space
    fbx_left_arm_world_pos = fbx_armature.matrix_world @ fbx_left_arm.head_local
    glb_left_arm_world_pos = glb_armature.matrix_world @ glb_left_arm.head_local
    
    print(f"\nPosición FBX LeftArm (world): {fbx_left_arm_world_pos}")
    print(f"Posición GLB LeftArm (world): {glb_left_arm_world_pos}")
    
    # Calcular diferencia
    offset = glb_left_arm_world_pos - fbx_left_arm_world_pos
    print(f"Offset necesario: {offset}")
    
    # Aplicar offset al FBX armature
    fbx_armature.location = fbx_armature.location + offset
    
    # Aplicar el mismo offset a todos los meshes del FBX
    for obj in fbx_objects:
        if obj.type == 'MESH':
            obj.location = obj.location + offset
    
    print(f"\n✓ FBX movido por offset: {offset}")
    
    # Actualizar la escena
    bpy.context.view_layer.update()
    
    # Verificar nueva posición
    fbx_left_arm_world_pos_new = fbx_armature.matrix_world @ fbx_left_arm.head_local
    print(f"\nNueva posición FBX LeftArm (world): {fbx_left_arm_world_pos_new}")
    print(f"Diferencia con GLB: {(glb_left_arm_world_pos - fbx_left_arm_world_pos_new).length:.4f} unidades")

# También ajustar escala si es necesario
print("\nCalculando escala...")
# El ratio de tamaño es aproximadamente 0.0123
scale_factor = 0.0123
print(f"Factor de escala: {scale_factor}")

# Aplicar escala al FBX
fbx_armature.scale = (scale_factor, scale_factor, scale_factor)
for obj in fbx_objects:
    if obj.type == 'MESH':
        obj.scale = (scale_factor, scale_factor, scale_factor)

bpy.context.view_layer.update()

print("✓ Escala aplicada")

# Verificar posición final después de escalar
if fbx_left_arm and glb_left_arm:
    fbx_left_arm_world_pos_final = fbx_armature.matrix_world @ fbx_left_arm.head_local
    glb_left_arm_world_pos_final = glb_armature.matrix_world @ glb_left_arm.head_local
    
    print(f"\nPosición final FBX LeftArm: {fbx_left_arm_world_pos_final}")
    print(f"Posición final GLB LeftArm: {glb_left_arm_world_pos_final}")
    
    final_diff = (glb_left_arm_world_pos_final - fbx_left_arm_world_pos_final).length
    print(f"Diferencia final: {final_diff:.4f} unidades")
    
    if final_diff < 0.1:
        print("✓ BRAZOS ALINEADOS CORRECTAMENTE")
    else:
        # Ajuste fino
        final_offset = glb_left_arm_world_pos_final - fbx_left_arm_world_pos_final
        fbx_armature.location = fbx_armature.location + final_offset
        for obj in fbx_objects:
            if obj.type == 'MESH':
                obj.location = obj.location + final_offset
        
        bpy.context.view_layer.update()
        print(f"✓ Ajuste fino aplicado: {final_offset}")

# Guardar
output_path.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(output_path))
print(f"\n✓ Archivo guardado: {output_path}")

print("\n" + "="*80)
print("ARCHIVO PREPARADO PARA ROKOKO RETARGETING")
print("="*80)
print("\nLos brazos del FBX ahora están alineados con los del GLB.")
print("Usa Rokoko Studio Live en Blender para hacer el retargeting:")
print("\n1. Pestaña 'Rokoko' > Retargeting")
print("2. Source: Source_Armature (FBX)")
print("3. Target: Target_Armature (GLB)")
print("4. Mapea los 8 huesos de brazos")
print("5. Click 'Build Bone List' > 'Retarget Animation'")
print("="*80)
