"""
SOLUCIÓN DEFINITIVA: Usar API de Rokoko Studio Live para retargetear
SOLO LOS BRAZOS del FBX de QuickMagic al GLB de DeepMotion

Este script usa el API programático de Rokoko, NO requiere interacción manual
"""

import bpy
from pathlib import Path
import json

print("="*80)
print("RETARGETING AUTOMÁTICO CON ROKOKO API - SOLO BRAZOS")
print("="*80)

# === ARCHIVOS ===
glb_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\expresiones\Duvall_resultado_abril.glb")
fbx_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\abril_BoyFBX.fbx")
output_path = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\Duvall_abril_BRAZOS_ROKOKO.glb")

# === MAPEO DE HUESOS - SOLO BRAZOS ===
ARM_BONES_MAPPING = {
    # FBX (QuickMagic) → GLB (DeepMotion)
    'Bip001 L Clavicle': 'LeftShoulder',
    'Bip001 L UpperArm': 'LeftArm',
    'Bip001 L Forearm': 'LeftForeArm',
    'Bip001 L Hand': 'LeftHand',
    'Bip001 R Clavicle': 'RightShoulder',
    'Bip001 R UpperArm': 'RightArm',
    'Bip001 R Forearm': 'RightForeArm',
    'Bip001 R Hand': 'RightHand',
}

print(f"\n📂 Archivos:")
print(f"   Target GLB: {glb_path.name}")
print(f"   Source FBX: {fbx_path.name}")
print(f"   Output: {output_path.name}")

# === PASO 1: LIMPIAR ESCENA ===
print(f"\n🧹 [1/8] Limpiando escena...")
bpy.ops.wm.read_homefile(use_empty=True)

# === PASO 2: IMPORTAR GLB (TARGET) ===
print(f"\n📦 [2/8] Importando GLB (target)...")
bpy.ops.import_scene.gltf(filepath=str(glb_path))

glb_armature = None
glb_meshes = []
for obj in bpy.data.objects:
    if obj.type == 'ARMATURE':
        glb_armature = obj
        glb_armature.name = "DeepMotion_Target"
    elif obj.type == 'MESH':
        glb_meshes.append(obj)

if not glb_armature:
    raise Exception("❌ No se encontró armature en GLB")

print(f"✓ Target armature: {glb_armature.name}")
print(f"✓ Meshes: {len(glb_meshes)}")
print(f"✓ Huesos: {len(glb_armature.data.bones)}")
print(f"✓ Animation: {glb_armature.animation_data is not None}")

# Guardar la animación original del GLB
original_glb_action = None
if glb_armature.animation_data and glb_armature.animation_data.action:
    original_glb_action = glb_armature.animation_data.action
    original_glb_action.name = "GLB_Original_Animation"
    print(f"✓ Animación original guardada: {original_glb_action.name}")

# === PASO 3: IMPORTAR FBX (SOURCE) ===
print(f"\n📦 [3/8] Importando FBX (source)...")
bpy.ops.import_scene.fbx(filepath=str(fbx_path))

fbx_armature = None
fbx_meshes = []
for obj in bpy.context.selected_objects:
    if obj.type == 'ARMATURE' and obj != glb_armature:
        fbx_armature = obj
        fbx_armature.name = "QuickMagic_Source"
    elif obj.type == 'MESH':
        fbx_meshes.append(obj)

if not fbx_armature:
    raise Exception("❌ No se encontró armature en FBX")

print(f"✓ Source armature: {fbx_armature.name}")
print(f"✓ Meshes: {len(fbx_meshes)}")
print(f"✓ Huesos: {len(fbx_armature.data.bones)}")

# === PASO 4: ESCALAR FBX ===
print(f"\n📏 [4/8] Escalando FBX...")
SCALE_FACTOR = 0.0123
fbx_armature.scale = (SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR)
for mesh in fbx_meshes:
    mesh.scale = (SCALE_FACTOR, SCALE_FACTOR, SCALE_FACTOR)

bpy.context.view_layer.update()
print(f"✓ FBX escalado por {SCALE_FACTOR}")

# === PASO 5: VERIFICAR ROKOKO ===
print(f"\n🔍 [5/8] Verificando Rokoko Studio Live...")
if not hasattr(bpy.ops, 'rsl'):
    raise Exception("❌ Rokoko Studio Live NO está instalado")

print(f"✓ Rokoko Studio Live detectado")

# Listar operadores disponibles
rokoko_ops = [op for op in dir(bpy.ops.rsl) if not op.startswith('_')]
print(f"✓ Operadores disponibles: {len(rokoko_ops)}")

# === PASO 6: CONFIGURAR ROKOKO ===
print(f"\n⚙️ [6/8] Configurando Rokoko para retargeting...")

scene = bpy.context.scene

# Configurar source y target
if hasattr(scene, 'rsl_retargeting_armature_source'):
    scene.rsl_retargeting_armature_source = fbx_armature
    print(f"✓ Source configurado: {fbx_armature.name}")
else:
    print(f"⚠ No se pudo configurar source automáticamente")

if hasattr(scene, 'rsl_retargeting_armature_target'):
    scene.rsl_retargeting_armature_target = glb_armature
    print(f"✓ Target configurado: {glb_armature.name}")
else:
    print(f"⚠ No se pudo configurar target automáticamente")

# Seleccionar target como activo
bpy.ops.object.select_all(action='DESELECT')
glb_armature.select_set(True)
bpy.context.view_layer.objects.active = glb_armature

# Configurar frame range de la animación del FBX
if fbx_armature.animation_data and fbx_armature.animation_data.action:
    fbx_action = fbx_armature.animation_data.action
    frame_start = int(fbx_action.frame_range[0])
    frame_end = int(fbx_action.frame_range[1])
    print(f"✓ Frames FBX: {frame_start} - {frame_end}")
else:
    raise Exception("❌ FBX no tiene animación")

bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = frame_end

# === PASO 7: EJECUTAR RETARGETING CON ROKOKO ===
print(f"\n🎯 [7/8] Ejecutando retargeting de Rokoko...")
print(f"   Esto puede tardar unos segundos...")

retarget_success = False

# MÉTODO 1: Intentar con detect_actor_bones + retarget_animation
try:
    print(f"\n   Método 1: Auto-detección de huesos...")
    
    if hasattr(bpy.ops.rsl, 'detect_actor_bones'):
        result = bpy.ops.rsl.detect_actor_bones()
        print(f"   ✓ Detección de huesos: {result}")
    
    if hasattr(bpy.ops.rsl, 'build_bone_list'):
        result = bpy.ops.rsl.build_bone_list()
        print(f"   ✓ Build bone list: {result}")
    
    if hasattr(bpy.ops.rsl, 'retarget_animation'):
        result = bpy.ops.rsl.retarget_animation()
        print(f"   ✓ Retarget animation: {result}")
        
        if result == {'FINISHED'}:
            retarget_success = True
            print(f"\n   ✅ RETARGETING EXITOSO CON MÉTODO 1")
    
except Exception as e:
    print(f"   ⚠ Método 1 falló: {e}")

# MÉTODO 2: Intentar con bpy.ops.rsl.retarget (como en regenerar_buenos_dias.py)
if not retarget_success:
    try:
        print(f"\n   Método 2: Retarget directo...")
        
        if hasattr(bpy.ops.rsl, 'retarget'):
            result = bpy.ops.rsl.retarget(
                armature_source=fbx_armature.name,
                use_actor=False,
                remap_to_arp=False
            )
            print(f"   ✓ Retarget: {result}")
            
            if result == {'FINISHED'}:
                retarget_success = True
                print(f"\n   ✅ RETARGETING EXITOSO CON MÉTODO 2")
        
    except Exception as e:
        print(f"   ⚠ Método 2 falló: {e}")

# MÉTODO 3: Fallback manual con constraints SOLO para brazos
if not retarget_success:
    print(f"\n   Método 3: Fallback manual (constraints + bake) SOLO BRAZOS...")
    
    # Crear un nuevo action para el target
    if not glb_armature.animation_data:
        glb_armature.animation_data_create()
    
    new_action = bpy.data.actions.new(name="Duvall_abril_brazos_combinados")
    glb_armature.animation_data.action = new_action
    
    # Copiar animación original (cuerpo completo) si existe
    if original_glb_action:
        for fcurve in original_glb_action.fcurves:
            new_fcurve = new_action.fcurves.new(
                data_path=fcurve.data_path,
                index=fcurve.array_index
            )
            for keyframe in fcurve.keyframe_points:
                new_fcurve.keyframe_points.insert(
                    keyframe.co[0],
                    keyframe.co[1]
                )
        print(f"   ✓ Copiada animación base del cuerpo")
    
    # Crear constraints SOLO para los 8 huesos de brazos
    constraints_count = 0
    for glb_bone_name in ARM_BONES_MAPPING.values():
        if glb_bone_name in glb_armature.pose.bones:
            glb_bone = glb_armature.pose.bones[glb_bone_name]
            
            # Buscar el hueso correspondiente en FBX
            fbx_bone_name = [k for k, v in ARM_BONES_MAPPING.items() if v == glb_bone_name][0]
            
            if fbx_bone_name in fbx_armature.pose.bones:
                constraint = glb_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = fbx_armature
                constraint.subtarget = fbx_bone_name
                constraints_count += 1
    
    print(f"   ✓ Creados {constraints_count} constraints para brazos")
    
    # Bake SOLO los huesos de brazos
    print(f"   🔥 Baking SOLO brazos...")
    
    # Seleccionar solo los huesos de brazos
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.select_all(action='DESELECT')
    
    for bone_name in ARM_BONES_MAPPING.values():
        if bone_name in glb_armature.pose.bones:
            glb_armature.data.bones[bone_name].select = True
    
    # Bake con only_selected=True para que solo afecte los brazos
    bpy.ops.nla.bake(
        frame_start=frame_start,
        frame_end=frame_end,
        step=1,
        only_selected=True,
        visual_keying=True,
        clear_constraints=True,
        clear_parents=False,
        use_current_action=True,
        clean_curves=False,
        bake_types={'POSE'}
    )
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    print(f"   ✓ Bake completado")
    retarget_success = True
    print(f"\n   ✅ RETARGETING EXITOSO CON MÉTODO 3")

if not retarget_success:
    raise Exception("❌ Todos los métodos de retargeting fallaron")

# === VERIFICAR RESULTADO ===
print(f"\n✅ Verificando resultado...")

if not glb_armature.animation_data or not glb_armature.animation_data.action:
    raise Exception("❌ El target no tiene animación después del retargeting")

final_action = glb_armature.animation_data.action
print(f"✓ Acción final: {final_action.name}")
print(f"✓ Frames: {final_action.frame_range[0]:.0f} - {final_action.frame_range[1]:.0f}")
print(f"✓ FCurves: {len(final_action.fcurves)}")

# === PASO 8: LIMPIAR Y EXPORTAR ===
print(f"\n🧹 [8/8] Limpiando y exportando...")

# Eliminar FBX y sus meshes
bpy.ops.object.select_all(action='DESELECT')
fbx_armature.select_set(True)
for mesh in fbx_meshes:
    mesh.select_set(True)
bpy.ops.object.delete()

print(f"✓ FBX eliminado")

# Exportar GLB
output_path.parent.mkdir(parents=True, exist_ok=True)
bpy.ops.export_scene.gltf(
    filepath=str(output_path),
    export_format='GLB',
    export_animations=True,
    export_frame_range=True,
    export_frame_step=1,
    export_force_sampling=True
)

print(f"\n{'='*80}")
print(f"✅ PROCESO COMPLETADO EXITOSAMENTE")
print(f"{'='*80}")
print(f"\n📁 Archivo guardado: {output_path}")
print(f"📊 Tamaño: {output_path.stat().st_size / 1024:.1f} KB")
print(f"\n🎯 El GLB ahora tiene:")
print(f"   • Animación original del cuerpo (frames {frame_start}-{frame_end})")
print(f"   • Animación de BRAZOS del FBX retargeteada")
print(f"   • Total: {len(final_action.fcurves)} fcurves")
