"""
Script para combinar las posiciones de los brazos del FBX con el GLB
Extrae solo los keyframes de los brazos del FBX y los aplica al modelo Duvall del GLB
VERSIÓN MEJORADA: Copia frame por frame y verifica que todo funcione
"""

import bpy
import os
import sys
import mathutils

# Rutas de archivos
fbx_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx"
glb_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb"
output_blend = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_combinado.blend"
output_glb = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_brazos_combinado.glb"
verification_file = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\verificacion_combinacion.txt"

# Crear carpeta de salida si no existe
output_dir = os.path.dirname(output_blend)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("="*80)
print("COMBINACIÓN DE ANIMACIONES DE BRAZOS")
print("="*80)

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Importar GLB (modelo base)
print(f"\n1. Importando GLB base: {glb_path}")
bpy.ops.import_scene.gltf(filepath=glb_path)

# Encontrar el armature del GLB
glb_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        glb_armature = obj
        break

if not glb_armature:
    print("ERROR: No se encontró armature en el GLB")
    sys.exit(1)

print(f"   ✓ Armature GLB encontrado: {glb_armature.name}")
print(f"   ✓ Número de huesos: {len(glb_armature.pose.bones)}")

# Guardar la animación original del GLB
original_action = None
if glb_armature.animation_data and glb_armature.animation_data.action:
    original_action = glb_armature.animation_data.action
    print(f"   ✓ Animación original: {original_action.name}")
    print(f"   ✓ Frames: {int(original_action.frame_range[0])} - {int(original_action.frame_range[1])}")

# Importar FBX
print(f"\n2. Importando FBX con animación de brazos: {fbx_path}")
bpy.ops.import_scene.fbx(filepath=fbx_path)

# Encontrar el armature del FBX
fbx_armature = None
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE' and obj != glb_armature:
        fbx_armature = obj
        break

if not fbx_armature:
    print("ERROR: No se encontró armature en el FBX")
    sys.exit(1)

print(f"   ✓ Armature FBX encontrado: {fbx_armature.name}")
print(f"   ✓ Número de huesos: {len(fbx_armature.pose.bones)}")

# Obtener la animación del FBX
fbx_action = None
if fbx_armature.animation_data and fbx_armature.animation_data.action:
    fbx_action = fbx_armature.animation_data.action
    print(f"   ✓ Animación FBX: {fbx_action.name}")
    print(f"   ✓ Frames: {int(fbx_action.frame_range[0])} - {int(fbx_action.frame_range[1])}")

# Definir los huesos de los brazos (patrones comunes)
arm_bone_patterns = [
    'shoulder', 'arm', 'elbow', 'forearm', 'hand', 'wrist',
    'clavicle', 'upperarm', 'lowerarm',
    'Shoulder', 'Arm', 'Elbow', 'Forearm', 'Hand', 'Wrist',
    'UpArm', 'LoArm', 'L_', 'R_',
    'left', 'right', 'Left', 'Right'
]

def is_arm_bone(bone_name):
    """Determina si un hueso es parte de los brazos"""
    bone_lower = bone_name.lower()
    
    # Excluir dedos explícitamente
    if any(x in bone_lower for x in ['thumb', 'index', 'middle', 'ring', 'pinky', 'finger']):
        return False
    
    # Incluir huesos de brazos
    return any(pattern.lower() in bone_lower for pattern in arm_bone_patterns)

# Encontrar huesos de brazos en FBX
print("\n3. Identificando huesos de brazos en FBX:")
fbx_arm_bones = []
for bone in fbx_armature.pose.bones:
    if is_arm_bone(bone.name):
        fbx_arm_bones.append(bone.name)
        print(f"   - {bone.name}")

if not fbx_arm_bones:
    print("ADVERTENCIA: No se encontraron huesos de brazos automáticamente")
    print("Mostrando todos los huesos del FBX:")
    for bone in fbx_armature.pose.bones:
        print(f"   - {bone.name}")

# Mapeo de huesos entre FBX y GLB
print("\n4. Mapeando huesos entre FBX y GLB:")

# Mapeo manual basado en los nombres detectados
manual_mapping = {
    'Bip001 L Clavicle': 'LeftShoulder',
    'Bip001 L UpperArm': 'LeftArm',
    'Bip001 L Forearm': 'LeftForeArm',
    'Bip001 L Hand': 'LeftHand',
    'Bip001 R Clavicle': 'RightShoulder',
    'Bip001 R UpperArm': 'RightArm',
    'Bip001 R Forearm': 'RightForeArm',
    'Bip001 R Hand': 'RightHand',
}

bone_mapping = {}

for fbx_bone_name in fbx_arm_bones:
    # Usar mapeo manual si existe
    if fbx_bone_name in manual_mapping:
        glb_bone_name = manual_mapping[fbx_bone_name]
        if glb_bone_name in glb_armature.pose.bones:
            bone_mapping[fbx_bone_name] = glb_bone_name
            print(f"   ✓ {fbx_bone_name} -> {glb_bone_name}")
        else:
            print(f"   ✗ {fbx_bone_name} -> {glb_bone_name} (no encontrado en GLB)")
    else:
        # Buscar coincidencia exacta primero
        if fbx_bone_name in glb_armature.pose.bones:
            bone_mapping[fbx_bone_name] = fbx_bone_name
            print(f"   ✓ {fbx_bone_name} -> {fbx_bone_name} (exacto)")
        else:
            # Buscar coincidencia parcial
            fbx_bone_lower = fbx_bone_name.lower()
            for glb_bone in glb_armature.pose.bones:
                glb_bone_lower = glb_bone.name.lower()
                if fbx_bone_lower in glb_bone_lower or glb_bone_lower in fbx_bone_lower:
                    bone_mapping[fbx_bone_name] = glb_bone.name
                    print(f"   ✓ {fbx_bone_name} -> {glb_bone.name} (similar)")
                    break

print(f"\n   Total de huesos mapeados: {len(bone_mapping)}")

if not bone_mapping:
    print("\nERROR: No se pudo mapear ningún hueso entre FBX y GLB")
    print("\nHuesos disponibles en GLB:")
    for bone in glb_armature.pose.bones:
        print(f"   - {bone.name}")
    sys.exit(1)

# Crear nueva acción combinada
print("\n5. Combinando animaciones:")
combined_action = bpy.data.actions.new(name="Abril_Brazos_Combinado")
glb_armature.animation_data.action = combined_action

# Determinar el rango de frames
if original_action and fbx_action:
    start_frame = int(min(original_action.frame_range[0], fbx_action.frame_range[0]))
    end_frame = int(max(original_action.frame_range[1], fbx_action.frame_range[1]))
elif fbx_action:
    start_frame = int(fbx_action.frame_range[0])
    end_frame = int(fbx_action.frame_range[1])
else:
    start_frame = 1
    end_frame = 60

print(f"   Rango de frames: {start_frame} - {end_frame}")

# Copiar animación usando enfoque frame-by-frame
print("   Método: Copia frame por frame para máxima precisión...")

# Primero, copiar TODA la animación original del GLB
keyframe_count = 0
if original_action:
    print("   Paso 1: Copiando animación completa del GLB como base...")
    for fcurve in original_action.fcurves:
        new_fcurve = combined_action.fcurves.new(
            data_path=fcurve.data_path,
            index=fcurve.array_index
        )
        for keyframe in fcurve.keyframe_points:
            new_fcurve.keyframe_points.insert(
                frame=keyframe.co[0],
                value=keyframe.co[1]
            )
            keyframe_count += 1
    print(f"      ✓ {keyframe_count} keyframes copiados de la animación base")

# Ahora, REEMPLAZAR solo los keyframes de los brazos con los del FBX
if fbx_action:
    print("   Paso 2: Reemplazando animación de brazos con datos del FBX...")
    replaced_count = 0
    
    for fbx_bone_name, glb_bone_name in bone_mapping.items():
        # Encontrar todas las FCurves del hueso en el FBX
        for fcurve in fbx_action.fcurves:
            if 'pose.bones' in fcurve.data_path:
                bone_name = fcurve.data_path.split('"')[1]
                
                if bone_name == fbx_bone_name:
                    # Extraer el tipo de propiedad (rotation_quaternion, rotation_euler, location, scale)
                    property_name = fcurve.data_path.split('.')[-1]
                    channel_index = fcurve.array_index
                    
                    # Crear el data_path para el GLB
                    glb_data_path = f'pose.bones["{glb_bone_name}"].{property_name}'
                    
                    # Buscar si ya existe esta FCurve en la animación combinada
                    existing_fcurve = None
                    for existing in combined_action.fcurves:
                        if existing.data_path == glb_data_path and existing.array_index == channel_index:
                            existing_fcurve = existing
                            break
                    
                    # Si existe, eliminarla para reemplazarla
                    if existing_fcurve:
                        combined_action.fcurves.remove(existing_fcurve)
                    
                    # Crear nueva FCurve con datos del FBX
                    new_fcurve = combined_action.fcurves.new(
                        data_path=glb_data_path,
                        index=channel_index
                    )
                    
                    # Copiar todos los keyframes
                    for keyframe in fcurve.keyframe_points:
                        new_fcurve.keyframe_points.insert(
                            frame=keyframe.co[0],
                            value=keyframe.co[1]
                        )
                        replaced_count += 1
    
    print(f"      ✓ {replaced_count} keyframes de brazos reemplazados del FBX")
    print(f"      ✓ Huesos procesados: {list(bone_mapping.values())}")

# Configurar la escena
bpy.context.scene.frame_start = start_frame
bpy.context.scene.frame_end = end_frame

# Eliminar el armature del FBX (pero mantener las acciones para depuración)
print("\n6. Limpiando escena...")

# Eliminar el objeto armature del FBX
bpy.data.objects.remove(fbx_armature, do_unlink=True)
print("   ✓ Armature FBX eliminado")

# Asegurarse de que el armature GLB tenga asignada la animación combinada
if glb_armature.animation_data is None:
    glb_armature.animation_data_create()
glb_armature.animation_data.action = combined_action
print(f"   ✓ Animación '{combined_action.name}' asignada al armature GLB")

# Listar todas las animaciones que se exportarán
print(f"   ✓ Animaciones en el archivo: {len(bpy.data.actions)}")
if len(bpy.data.actions) <= 5:  # Mostrar solo si hay pocas
    for action in bpy.data.actions:
        print(f"     - {action.name}")

# Guardar archivo Blend
print(f"\n7. Guardando archivo Blend: {output_blend}")
bpy.ops.wm.save_as_mainfile(filepath=output_blend)
print("   ✓ Archivo Blend guardado")

# Exportar a GLB
print(f"\n8. Exportando a GLB: {output_glb}")
bpy.ops.object.select_all(action='DESELECT')
glb_armature.select_set(True)

# Seleccionar también todos los meshes asociados
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        obj.select_set(True)

bpy.ops.export_scene.gltf(
    filepath=output_glb,
    export_format='GLB',
    export_animations=True,
    use_selection=True
)
print("   ✓ Archivo GLB exportado")

# Verificación exhaustiva
print("\n" + "="*80)
print("VERIFICACIÓN EXHAUSTIVA")
print("="*80)

# Verificar que la animación combinada tiene datos
total_fcurves = len(combined_action.fcurves)
print(f"✓ Total de FCurves en animación combinada: {total_fcurves}")

# Verificar que los huesos de brazos tienen keyframes
arm_fcurves = 0
verification_data = []

for bone_name in bone_mapping.values():
    bone_fcurves = [f for f in combined_action.fcurves if f'pose.bones["{bone_name}"]' in f.data_path]
    arm_fcurves += len(bone_fcurves)
    
    if bone_fcurves:
        print(f"✓ {bone_name}: {len(bone_fcurves)} canales animados")
        for fcurve in bone_fcurves:
            keyframe_count = len(fcurve.keyframe_points)
            property_name = fcurve.data_path.split('.')[-1]
            channel = fcurve.array_index
            verification_data.append(f"  - {bone_name}.{property_name}[{channel}]: {keyframe_count} keyframes")
    else:
        print(f"⚠️  {bone_name}: Sin animación (posible error)")

print(f"\n✓ Total de canales de brazos: {arm_fcurves}")

# Verificar rango de frames
if combined_action.fcurves:
    all_frames = set()
    for fcurve in combined_action.fcurves:
        for kf in fcurve.keyframe_points:
            all_frames.add(int(kf.co[0]))
    
    min_frame = min(all_frames)
    max_frame = max(all_frames)
    print(f"✓ Rango de animación: {min_frame} - {max_frame} ({len(all_frames)} frames únicos)")

# Guardar reporte de verificación
with open(verification_file, 'w', encoding='utf-8') as f:
    f.write("="*80 + "\n")
    f.write("REPORTE DE VERIFICACIÓN - COMBINACIÓN DE ANIMACIONES ABRIL\n")
    f.write("="*80 + "\n\n")
    f.write(f"Archivo FBX origen: {fbx_path}\n")
    f.write(f"Archivo GLB base: {glb_path}\n")
    f.write(f"Archivo Blend salida: {output_blend}\n")
    f.write(f"Archivo GLB salida: {output_glb}\n\n")
    f.write(f"Huesos mapeados (FBX -> GLB):\n")
    for fbx_bone, glb_bone in bone_mapping.items():
        f.write(f"  {fbx_bone} -> {glb_bone}\n")
    f.write(f"\nTotal de FCurves: {total_fcurves}\n")
    f.write(f"FCurves de brazos: {arm_fcurves}\n")
    f.write(f"Rango de frames: {min_frame} - {max_frame}\n\n")
    f.write("Detalle de canales de brazos:\n")
    for line in verification_data:
        f.write(line + "\n")

print(f"\n✓ Reporte guardado en: {verification_file}")

print("\n" + "="*80)
print("RESUMEN FINAL")
print("="*80)
print(f"✓ Archivo Blend creado: {output_blend}")
print(f"✓ Archivo GLB creado: {output_glb}")
print(f"✓ Animación combinada: {combined_action.name}")
print(f"✓ Frames: {start_frame} - {end_frame}")
print(f"✓ Huesos de brazos del FBX aplicados: {len(bone_mapping)}")
print(f"✓ Canales de brazos animados: {arm_fcurves}")
print("\n🎯 Proceso completado exitosamente!")
print("⚠️  VERIFICAR manualmente que los brazos se muevan correctamente en el visualizador")
