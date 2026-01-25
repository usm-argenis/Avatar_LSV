import bpy
import sys
from pathlib import Path

print("\n" + "="*70)
print("TRANSFERENCIA CON APLICACION DIRECTA DE POSES")
print("="*70)

# Limpiar
bpy.ops.wm.read_homefile(use_empty=True)

# CONFIGURACIÓN: Define qué avatares usar
avatar_origen = "Remy_resultado_b.fbx"  # Avatar CON animación
avatar_destino = "JH.fbx"                # Avatar SIN animación (modelo base)
nombre_salida = "JH_resultado_b"         # Nombre del archivo de salida

print(f"\n📋 Configuración:")
print(f"  Origen (con animación): {avatar_origen}")
print(f"  Destino (modelo base): {avatar_destino}")
print(f"  Salida: {nombre_salida}")

# Importar avatar con animación (origen)
origen_path = r"C:\Users\andre\OneDrive\Documentos\tesis\deploy-viewer-temp\output\\" + avatar_origen
print(f"\n✅ Importando avatar con animación: {Path(origen_path).name}")
bpy.ops.import_scene.fbx(filepath=origen_path)

arm_origen = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        arm_origen = obj
        break

if not arm_origen or not arm_origen.animation_data:
    print("❌ ERROR: No animation data en avatar origen")
    sys.exit(1)

accion_origen = arm_origen.animation_data.action
frame_start = int(accion_origen.frame_range[0])
frame_end = int(accion_origen.frame_range[1])

print(f"  Frames: {frame_start} - {frame_end}")

# Importar avatar destino (modelo base)
destino_path = r"C:\Users\andre\OneDrive\Documentos\tesis\avatars\\" + avatar_destino
print(f"\n✅ Importando avatar destino: {Path(destino_path).name}")
bpy.ops.import_scene.fbx(filepath=destino_path)

arm_destino = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != arm_origen:
        arm_destino = obj
        break

if not arm_destino:
    print("❌ ERROR: No se encontró avatar destino")
    sys.exit(1)

# Mapeo usando los nombres guardados
mapeo = {}
for hueso_origen_nombre in arm_origen.pose.bones.keys():
    # Limpiar prefijos
    nombre_limpio_o = hueso_origen_nombre.replace('mixamorig:', '').replace('mixamorig9:', '')
    
    # Buscar en destino
    for hueso_destino in arm_destino.pose.bones.keys():
        nombre_limpio_d = hueso_destino.replace('mixamorig:', '').replace('mixamorig9:', '')
        if nombre_limpio_o == nombre_limpio_d:
            mapeo[hueso_origen_nombre] = hueso_destino
            break

print(f"✅ Huesos mapeados: {len(mapeo)}")

# Calcular escala entre origen y destino
# Usar Hips como referencia
hips_origen = None
hips_destino = None

for hueso_o in arm_origen.pose.bones:
    if "Hips" in hueso_o.name:
        hips_origen = hueso_o
        break

for hueso_d in arm_destino.pose.bones:
    if "Hips" in hueso_d.name:
        hips_destino = hueso_d
        break

if hips_origen and hips_destino:
    pos_origen = arm_origen.matrix_world @ hips_origen.head
    pos_destino = arm_destino.matrix_world @ hips_destino.head
    
    # Calcular escala para igualar tamaños
    # Multiplicamos por la escala del origen para que queden iguales
    escala_origen = arm_origen.scale.z  # Obtener escala del origen (debería ser 0.01)
    escala = (pos_origen.z / pos_destino.z) * escala_origen if pos_destino.z != 0 else escala_origen
    
    print(f"\n📏 Ajustando escala del avatar destino:")
    print(f"  Escala origen: {escala_origen:.6f}")
    print(f"  Hips origen Z: {pos_origen.z:.6f}")
    print(f"  Hips destino Z (antes): {pos_destino.z:.6f}")
    print(f"  Escala a aplicar: {escala:.6f}")
    print(f"  Hips destino Z (después): {pos_destino.z * escala:.6f}")
    
    # Aplicar escala al armature del destino (NO aplicar transform, dejar la escala en el objeto)
    arm_destino.scale = (escala, escala, escala)
    print(f"  ✅ Escala aplicada al objeto (NO a los huesos)")
    
    bpy.context.view_layer.objects.active = arm_destino
else:
    print("\n⚠️ WARNING: No se encontraron Hips, usando escala 1.0")

# Crear nueva acción para el avatar destino
if not arm_destino.animation_data:
    arm_destino.animation_data_create()

nueva_accion = bpy.data.actions.new(f"{nombre_salida}_Anim")
arm_destino.animation_data.action = nueva_accion

# METODO: Copiar frame por frame PERO usando las propiedades del hueso directamente
print("\n🎬 Copiando animación frame por frame...")
bpy.context.view_layer.objects.active = arm_destino

for frame in range(frame_start, frame_end + 1):
    bpy.context.scene.frame_set(frame)
    
    # Leer poses del origen en este frame
    for hueso_o_name, hueso_d_name in mapeo.items():
        hueso_o = arm_origen.pose.bones[hueso_o_name]
        hueso_d = arm_destino.pose.bones[hueso_d_name]
        
        # Copiar rotación
        hueso_d.rotation_quaternion = hueso_o.rotation_quaternion.copy()
        hueso_d.location = hueso_o.location.copy()
        hueso_d.scale = hueso_o.scale.copy()
        
        # INSERTAR KEYFRAME DIRECTAMENTE
        hueso_d.keyframe_insert(data_path="rotation_quaternion", frame=frame)
        hueso_d.keyframe_insert(data_path="location", frame=frame)
        hueso_d.keyframe_insert(data_path="scale", frame=frame)
    
    if frame % 10 == 0:
        print(f"  Frame {frame}/{frame_end}")

print("\n✅ Keyframes insertados")

# Verificar resultado
print("\n=== VERIFICANDO ACCION ===")
print(f"Action: {nueva_accion.name}")
print(f"FCurves: {len(nueva_accion.fcurves)}")

# Buscar RightArm
for fc in nueva_accion.fcurves:
    if "RightArm" in fc.data_path and "rotation_quaternion" in fc.data_path and fc.array_index == 0:
        valores = [kf.co[1] for kf in fc.keyframe_points]
        print(f"\n{fc.data_path}[{fc.array_index}]:")
        print(f"  Keyframes: {len(valores)}")
        print(f"  Valores (primeros 10): {valores[:10]}")
        print(f"  Min: {min(valores):.6f}, Max: {max(valores):.6f}")
        print(f"  Unicos: {len(set([round(v, 6) for v in valores]))}")
        break

# Exportar
output_path_fbx = r"C:\Users\andre\OneDrive\Documentos\tesis\output\\" + nombre_salida + ".fbx"
print(f"\n=== EXPORTANDO ===")

# IMPORTANTE: ELIMINAR objetos del origen ANTES de guardar .blend
print("\n🗑️ Eliminando objetos del avatar origen...")
objetos_eliminados = 0

for obj in list(bpy.data.objects):
    # Eliminar armature del origen y sus meshes
    if obj.type == 'ARMATURE' and obj != arm_destino:
        print(f"  - Eliminando armature: {obj.name}")
        bpy.data.objects.remove(obj, do_unlink=True)
        objetos_eliminados += 1
    elif obj.type == 'MESH' and obj.parent != arm_destino:
        print(f"  - Eliminando mesh: {obj.name}")
        bpy.data.objects.remove(obj, do_unlink=True)
        objetos_eliminados += 1

print(f"✅ {objetos_eliminados} objetos eliminados")

# Limpiar datos huérfanos
print("\n🧹 Limpiando datos huérfanos...")
for armature_data in list(bpy.data.armatures):
    if armature_data.users == 0:
        bpy.data.armatures.remove(armature_data)

for mesh_data in list(bpy.data.meshes):
    if mesh_data.users == 0:
        bpy.data.meshes.remove(mesh_data)

# Guardar primero como .blend para debug
blend_path = r"C:\Users\andre\OneDrive\Documentos\tesis\output\\" + nombre_salida + ".blend"
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print(f"\n✅ Guardado .blend: {Path(blend_path).name}")
print(f"  (Solo contiene avatar destino con animación transferida)")

# CRUCIAL: Configurar el frame range de la escena Y de la acción
bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = frame_end
bpy.context.scene.frame_set(frame_start)

# Ajustar frame range de la acción
nueva_accion.frame_range = (frame_start, frame_end)
nueva_accion.use_frame_range = True

print(f"Frame range (scene): {frame_start} - {frame_end}")
print(f"Frame range (action): {nueva_accion.frame_range[0]} - {nueva_accion.frame_range[1]}")

# Seleccionar solo el avatar destino y sus meshes
bpy.ops.object.select_all(action='DESELECT')
arm_destino.select_set(True)
bpy.context.view_layer.objects.active = arm_destino

# Seleccionar meshes del avatar destino
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        obj.select_set(True)

print(f"\n📦 Exportando a FBX: {Path(output_path_fbx).name}")

bpy.ops.export_scene.fbx(
    filepath=output_path_fbx,
    # Selección
    use_selection=False,
    use_visible=False,
    use_active_collection=False,
    
    # Escala y transformación - CLAVE PARA QUE FUNCIONE
    global_scale=1.0,
    apply_unit_scale=True,
    apply_scale_options='FBX_SCALE_NONE',
    use_space_transform=True,
    bake_space_transform=False,
    
    # Tipos de objetos
    object_types={'ARMATURE', 'MESH'},
    use_mesh_modifiers=True,
    use_mesh_modifiers_render=True,
    mesh_smooth_type='FACE',
    
    # Armature - CLAVE: use_armature_deform_only=False
    use_armature_deform_only=False,
    armature_nodetype='NULL',
    add_leaf_bones=False,
    primary_bone_axis='Y',
    secondary_bone_axis='X',
    
    # ANIMACIÓN
    bake_anim=True,
    bake_anim_use_all_bones=True,
    bake_anim_use_nla_strips=False,
    bake_anim_use_all_actions=False,
    bake_anim_force_startend_keying=True,
    bake_anim_step=1.0,
    bake_anim_simplify_factor=0.0,
    
    # Otros
    path_mode='AUTO',
    embed_textures=True,
    axis_forward='-Z',
    axis_up='Y'
)

print("\n✓ Exportado!")
print("="*70)
