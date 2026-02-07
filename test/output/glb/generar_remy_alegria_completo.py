"""
Script completo automático: Remy con animación de alegría
==========================================================

Este script hace TODO el proceso de una sola vez:
1. Importa Remy.fbx
2. Obtiene dimensiones reales del armature de Remy
3. Crea nuevo armature Mixamo escalado exactamente al tamaño de Remy
4. Agrega 52 shape keys ARKit
5. Configura drivers para emociones
6. Aplica skinning automático
7. Activa emoción ALEGRÍA al 100%
8. Exporta a GLB final

Salida: C:\output\Remy_Alegria_Final.glb

Uso:
- Abrir en Blender
- Alt+P
- Esperar ~30 segundos
- Resultado listo en C:\output\Remy_Alegria_Final.glb
"""

import bpy
import os
from mathutils import Vector

# Rutas
BASE_DIR = os.path.dirname(__file__)#"C:\\\\Remy.fbx"
REMY_FBX = os.path.join(BASE_DIR, 'Users', 'andre', 'Downloads', 'Remy.fbx')
REMY_FBX = os.path.abspath(REMY_FBX)

OUTPUT_DIR = r"C:\output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_GLB = os.path.join(OUTPUT_DIR, 'Remy_Alegria_Final.glb')

# 52 shape keys ARKit
ARKIT_BLENDSHAPES = [
    'browInnerUp', 'browDown_L', 'browDown_R', 'browOuterUp_L', 'browOuterUp_R',
    'eyeLookUp_L', 'eyeLookUp_R', 'eyeLookDown_L', 'eyeLookDown_R',
    'eyeLookIn_L', 'eyeLookIn_R', 'eyeLookOut_L', 'eyeLookOut_R',
    'eyeBlink_L', 'eyeBlink_R', 'eyeSquint_L', 'eyeSquint_R', 'eyeWide_L', 'eyeWide_R',
    'cheekPuff', 'cheekSquint_L', 'cheekSquint_R',
    'noseSneer_L', 'noseSneer_R',
    'jawOpen', 'jawForward', 'jawLeft', 'jawRight',
    'mouthFunnel', 'mouthPucker', 'mouthLeft', 'mouthRight',
    'mouthRollUpper', 'mouthRollLower', 'mouthShrugUpper', 'mouthShrugLower',
    'mouthClose', 'mouthSmile_L', 'mouthSmile_R', 'mouthFrown_L', 'mouthFrown_R',
    'mouthDimple_L', 'mouthDimple_R', 'mouthUpperUp_L', 'mouthUpperUp_R',
    'mouthLowerDown_L', 'mouthLowerDown_R', 'mouthPress_L', 'mouthPress_R',
    'mouthStretch_L', 'mouthStretch_R', 'tongueOut'
]

# Mapeo de emociones a shape keys
EMOTION_MAPPINGS = {
    'EMOTION_ALEGRIA': ['mouthSmile_L', 'mouthSmile_R', 'cheekPuff']
}


def clear_scene():
    """Limpia toda la escena"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for mesh in list(bpy.data.meshes):
        if mesh.users == 0:
            bpy.data.meshes.remove(mesh)
    for arm in list(bpy.data.armatures):
        if arm.users == 0:
            bpy.data.armatures.remove(arm)


def import_remy():
    """Importa Remy, une todos los meshes y extrae altura del armature original"""
    print(f"\n[1] Importando Remy desde: {REMY_FBX}")
    
    if not os.path.exists(REMY_FBX):
        raise FileNotFoundError(f"No se encontró Remy.fbx en: {REMY_FBX}")
    
    bpy.ops.import_scene.fbx(filepath=REMY_FBX)
    
    # Buscar TODOS los meshes y el armature
    meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
    armature = next((obj for obj in bpy.data.objects if obj.type == 'ARMATURE'), None)
    
    if not meshes:
        raise Exception("No se encontraron meshes en Remy.fbx")
    
    print(f"  ✓ Meshes encontrados: {len(meshes)}")
    for m in meshes:
        print(f"    - {m.name}")
    
    # UNIR TODOS LOS MESHES EN UNO SOLO
    print(f"\n  Uniendo {len(meshes)} meshes...")
    bpy.ops.object.select_all(action='DESELECT')
    for m in meshes:
        m.select_set(True)
    
    bpy.context.view_layer.objects.active = meshes[0]
    bpy.ops.object.join()
    
    unified_mesh = bpy.context.active_object
    unified_mesh.name = 'Remy_Unified'
    print(f"  ✓ Meshes unidos en: {unified_mesh.name}")
    
    # Calcular altura desde armature si existe
    remy_height = 1.80  # default
    
    if armature:
        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.mode_set(mode='EDIT')
        bones = armature.data.edit_bones
        
        head_bone = None
        root_bone = None
        
        for bone in bones:
            name_lower = bone.name.lower()
            if 'head' in name_lower and not head_bone:
                head_bone = bone
            if any(x in name_lower for x in ['hips', 'root', 'pelvis']) and not root_bone:
                root_bone = bone
        
        if head_bone and root_bone:
            remy_height = head_bone.tail.z - root_bone.head.z
            print(f"  ✓ Altura detectada desde armature: {remy_height:.2f}")
        else:
            all_z = [b.head.z for b in bones] + [b.tail.z for b in bones]
            remy_height = max(all_z) - min(all_z)
            print(f"  ✓ Altura estimada: {remy_height:.2f}")
        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Eliminar armature original
        bpy.data.objects.remove(armature, do_unlink=True)
        print(f"  ✓ Armature original removido")
    
    # Limpiar modificadores del mesh unificado
    unified_mesh.modifiers.clear()
    
    return unified_mesh, remy_height


def create_armature_scaled(height):
    """Crea armature Mixamo completo escalado al tamaño de Remy"""
    print(f"\n[2] Creando armature Mixamo (altura: {height:.2f})")
    
    bpy.ops.object.armature_add(location=(0, 0, 0))
    armature = bpy.context.active_object
    armature.name = 'Armature'
    armature.show_in_front = True
    
    bpy.ops.object.mode_set(mode='EDIT')
    bones = armature.data.edit_bones
    bones.remove(bones[0])
    
    # Factor de escala
    base_height = 2.50
    scale = height / base_height
    
    print(f"  Factor de escala: {scale:.3f}")
    
    def s(val):
        """Escala valor"""
        return val * scale
    
    # Crear todos los huesos
    hips = bones.new('Hips')
    hips.head = (0, 0, s(0.95))
    hips.tail = (0, 0, s(1.10))
    
    spine = bones.new('Spine')
    spine.head = (0, 0, s(0.95))
    spine.tail = (0, 0, s(1.25))
    spine.parent = hips
    
    spine1 = bones.new('Spine1')
    spine1.head = (0, 0, s(1.25))
    spine1.tail = (0, 0, s(1.50))
    spine1.parent = spine
    
    spine2 = bones.new('Spine2')
    spine2.head = (0, 0, s(1.50))
    spine2.tail = (0, 0, s(1.75))
    spine2.parent = spine1
    
    neck = bones.new('Neck')
    neck.head = (0, 0, s(1.75))
    neck.tail = (0, 0, s(1.95))
    neck.parent = spine2
    
    head = bones.new('Head')
    head.head = (0, 0, s(1.95))
    head.tail = (0, 0, s(2.50))
    head.parent = neck
    
    # Brazos y manos
    for side, sign in [('Left', -1), ('Right', 1)]:
        shoulder = bones.new(f'{side}Shoulder')
        shoulder.head = (0, 0, s(1.75))
        shoulder.tail = (sign * s(0.25), 0, s(1.75))
        shoulder.parent = spine2
        
        arm = bones.new(f'{side}Arm')
        arm.head = (sign * s(0.25), 0, s(1.75))
        arm.tail = (sign * s(0.50), 0, s(1.10))
        arm.parent = shoulder
        
        forearm = bones.new(f'{side}ForeArm')
        forearm.head = (sign * s(0.50), 0, s(1.10))
        forearm.tail = (sign * s(0.50), 0, s(0.60))
        forearm.parent = arm
        
        hand = bones.new(f'{side}Hand')
        hand.head = (sign * s(0.50), 0, s(0.60))
        hand.tail = (sign * s(0.50), 0, s(0.48))
        hand.parent = forearm
        
        # Dedos de manos (simplificados - solo 1 hueso por dedo)
        finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
        finger_x = [0.52, 0.525, 0.50, 0.475, 0.45]
        
        for fname, fx in zip(finger_names, finger_x):
            finger = bones.new(f'{side}Hand{fname}1')
            finger.head = (sign * s(fx), 0, s(0.50))
            finger.tail = (sign * s(fx), 0, s(0.42))
            finger.parent = hand
    
    # Piernas
    for side, sign in [('Left', -1), ('Right', 1)]:
        upleg = bones.new(f'{side}UpLeg')
        upleg.head = (sign * s(0.18), 0, s(0.95))
        upleg.tail = (sign * s(0.18), 0, s(0.35))
        upleg.parent = hips
        
        leg = bones.new(f'{side}Leg')
        leg.head = (sign * s(0.18), 0, s(0.35))
        leg.tail = (sign * s(0.18), 0, s(-0.05))
        leg.parent = upleg
        
        foot = bones.new(f'{side}Foot')
        foot.head = (sign * s(0.18), 0, s(-0.05))
        foot.tail = (sign * s(0.18), s(0.15), s(-0.05))
        foot.parent = leg
        
        toe = bones.new(f'{side}ToeBase')
        toe.head = (sign * s(0.18), s(0.15), s(-0.05))
        toe.tail = (sign * s(0.18), s(0.22), s(-0.05))
        toe.parent = foot
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    print(f"  ✓ Armature creado con {len(armature.data.bones)} huesos")
    
    return armature


def add_shape_keys(mesh):
    """Agrega 52 shape keys ARKit a la malla"""
    print(f"\n[3] Creando {len(ARKIT_BLENDSHAPES)} shape keys ARKit")
    
    bpy.context.view_layer.objects.active = mesh
    
    if not mesh.data.shape_keys:
        mesh.shape_key_add(name='Basis')
    
    mesh_data = mesh.data
    
    for sk_name in ARKIT_BLENDSHAPES:
        sk = mesh.shape_key_add(name=sk_name)
        
        # Aplicar deformaciones solo en región de cabeza
        for i, v in enumerate(mesh_data.vertices):
            co = v.co.copy()
            
            # Detectar región de cabeza (ajustar según escala de Remy)
            # Asumimos que la cabeza está en la parte superior
            bbox = mesh.bound_box
            max_z = max([vert[2] for vert in bbox])
            min_z = min([vert[2] for vert in bbox])
            height = max_z - min_z
            head_threshold = min_z + height * 0.75  # 75% de altura = cabeza
            
            if co.z < head_threshold:
                sk.data[i].co = co
                continue
            
            delta = Vector((0, 0, 0))
            
            # Deformaciones faciales (simplificadas pero funcionales)
            head_center_z = min_z + height * 0.85
            
            if 'mouthSmile' in sk_name:
                # Sonrisa: estirar comisuras hacia afuera y arriba
                if abs(co.x) > 0.05 and co.z > head_center_z - 0.15 and co.z < head_center_z - 0.05:
                    delta.x = co.x * 0.2
                    delta.z = 0.015
            
            elif 'eyeBlink' in sk_name:
                # Parpadeo: bajar párpados
                if abs(co.x) > 0.03 and co.z > head_center_z - 0.08 and co.z < head_center_z:
                    delta.z = -0.02
            
            elif 'browInnerUp' in sk_name:
                # Cejas arriba centro
                if abs(co.x) < 0.05 and co.z > head_center_z and co.z < head_center_z + 0.08:
                    delta.z = 0.02
            
            elif 'browDown' in sk_name:
                # Cejas abajo
                if co.z > head_center_z and co.z < head_center_z + 0.08:
                    if ('_L' in sk_name and co.x > 0.03) or ('_R' in sk_name and co.x < -0.03):
                        delta.z = -0.015
            
            elif 'browOuterUp' in sk_name:
                # Cejas arriba exterior
                if co.z > head_center_z and co.z < head_center_z + 0.08:
                    if ('_L' in sk_name and co.x > 0.08) or ('_R' in sk_name and co.x < -0.08):
                        delta.z = 0.02
            
            elif 'cheekPuff' in sk_name:
                # Inflar mejillas
                if abs(co.x) > 0.05 and co.z > head_center_z - 0.12 and co.z < head_center_z - 0.02:
                    delta.x = co.x * 0.15
                    delta.y = abs(co.x) * 0.08
            
            elif 'jawOpen' in sk_name:
                # Abrir boca
                if co.z > head_center_z - 0.20 and co.z < head_center_z - 0.08:
                    delta.z = -0.06
            
            elif 'eyeWide' in sk_name:
                # Ojos abiertos
                if abs(co.x) > 0.03 and co.z > head_center_z - 0.08 and co.z < head_center_z:
                    delta.z = 0.015
            
            elif 'mouthFrown' in sk_name:
                # Ceño
                if abs(co.x) > 0.05 and co.z > head_center_z - 0.15 and co.z < head_center_z - 0.08:
                    delta.z = -0.015
            
            elif 'noseSneer' in sk_name:
                # Arrugar nariz
                if co.z > head_center_z - 0.10 and co.z < head_center_z - 0.05:
                    if ('_L' in sk_name and co.x > 0.01) or ('_R' in sk_name and co.x < -0.01):
                        delta.z = 0.01
            
            elif 'mouthUpperUp' in sk_name:
                # Labio superior arriba
                if co.z > head_center_z - 0.12 and co.z < head_center_z - 0.08:
                    if ('_L' in sk_name and co.x > 0.02) or ('_R' in sk_name and co.x < -0.02):
                        delta.z = 0.015
            
            elif 'mouthLowerDown' in sk_name:
                # Labio inferior abajo
                if co.z > head_center_z - 0.15 and co.z < head_center_z - 0.11:
                    if ('_L' in sk_name and co.x > 0.02) or ('_R' in sk_name and co.x < -0.02):
                        delta.z = -0.015
            
            elif 'mouthDimple' in sk_name:
                # Hoyuelos
                if co.z > head_center_z - 0.13 and co.z < head_center_z - 0.09:
                    if ('_L' in sk_name and co.x > 0.06) or ('_R' in sk_name and co.x < -0.06):
                        delta.y = -0.01
            
            sk.data[i].co = co + delta
        
        sk.value = 0.0
    
    print(f"  ✓ {len(ARKIT_BLENDSHAPES)} shape keys creados")


def setup_emotion_drivers(mesh, armature):
    """Configura drivers para control de emociones"""
    print(f"\n[4] Configurando drivers de emociones")
    
    bpy.context.view_layer.objects.active = armature
    
    # Crear custom property para ALEGRIA
    armature['EMOTION_ALEGRIA'] = 0.0
    
    # Configurar UI
    id_props = armature.id_properties_ui('EMOTION_ALEGRIA')
    id_props.update(min=0.0, max=1.0, soft_min=0.0, soft_max=1.0, description="Sonrisa/Risa")
    
    # Crear drivers
    shape_keys = mesh.data.shape_keys.key_blocks
    
    drivers_created = 0
    for sk_name in EMOTION_MAPPINGS['EMOTION_ALEGRIA']:
        if sk_name not in shape_keys:
            continue
        
        sk = shape_keys[sk_name]
        
        # Eliminar driver existente
        if sk.driver_remove('value'):
            pass
        
        # Crear nuevo driver
        driver = sk.driver_add('value').driver
        driver.type = 'AVERAGE'
        
        var = driver.variables.new()
        var.name = 'emotion'
        var.type = 'SINGLE_PROP'
        
        target = var.targets[0]
        target.id = armature
        target.data_path = '["EMOTION_ALEGRIA"]'
        
        drivers_created += 1
    
    print(f"  ✓ {drivers_created} drivers creados para ALEGRIA")


def apply_skinning(mesh, armature):
    """Aplica skinning automático y verifica que funcionó"""
    print(f"\n[5] Aplicando skinning automático")
    
    bpy.ops.object.select_all(action='DESELECT')
    mesh.select_set(True)
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    
    try:
        bpy.ops.object.parent_set(type='ARMATURE_AUTO')
        print(f"  ✓ Parent_set ejecutado")
    except Exception as e:
        print(f"  ✗ Error en parent_set: {e}")
        return False
    
    # VERIFICAR que el skinning se aplicó
    print(f"\n  Verificando skinning...")
    
    # Check 1: Parent relationship
    if mesh.parent == armature:
        print(f"  ✓ Mesh.parent = Armature")
    else:
        print(f"  ✗ Mesh.parent no es Armature")
        return False
    
    # Check 2: Armature modifier
    arm_mod = next((m for m in mesh.modifiers if m.type == 'ARMATURE'), None)
    if arm_mod:
        print(f"  ✓ Modificador Armature existe")
        print(f"    - Object: {arm_mod.object.name if arm_mod.object else 'None'}")
    else:
        print(f"  ✗ NO hay modificador Armature")
        return False
    
    # Check 3: Vertex groups
    vg_count = len(mesh.vertex_groups)
    print(f"  ✓ Vertex groups: {vg_count}")
    if vg_count == 0:
        print(f"  ✗ NO se crearon vertex groups")
        return False
    
    print(f"  ✓ Skinning aplicado correctamente")
    return True


def activate_emotion(armature, emotion='EMOTION_ALEGRIA', intensity=1.0):
    """Activa una emoción"""
    print(f"\n[6] Activando emoción: {emotion} (intensidad: {intensity})")
    
    if emotion in armature:
        armature[emotion] = intensity
        bpy.context.view_layer.update()
        print(f"  ✓ Emoción activada")
    else:
        print(f"  ✗ Propiedad {emotion} no existe")


def export_glb(filepath):
    """Exporta a GLB con verificación previa"""
    print(f"\n[7] Preparando exportación GLB")
    
    # Verificación final antes de exportar
    mesh = bpy.data.objects.get('Remy_Unified')
    armature = bpy.data.objects.get('Armature')
    
    if not mesh or not armature:
        print(f"  ✗ Objetos no encontrados")
        return False
    
    print(f"  Verificación pre-exportación:")
    print(f"    - Mesh: {mesh.name}")
    print(f"    - Armature: {armature.name}")
    print(f"    - Parent: {mesh.parent.name if mesh.parent else 'None'}")
    print(f"    - Modificadores: {len(mesh.modifiers)}")
    print(f"    - Vertex groups: {len(mesh.vertex_groups)}")
    print(f"    - Shape keys: {len(mesh.data.shape_keys.key_blocks) if mesh.data.shape_keys else 0}")
    
    if mesh.parent != armature:
        print(f"  ✗ ADVERTENCIA: Mesh no está parented a armature")
    
    if len(mesh.vertex_groups) == 0:
        print(f"  ✗ ADVERTENCIA: No hay vertex groups")
    
    print(f"\n  Exportando a: {filepath}")
    
    bpy.ops.export_scene.gltf(
        filepath=filepath,
        export_format='GLB',
        use_selection=False,
        export_apply=False,  # NO aplicar transformaciones
        export_animations=False,
        export_morph=True,
        export_skins=True,
        export_def_bones=True,
        export_draco_mesh_compression_enable=False
    )
    
    if os.path.exists(filepath):
        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        print(f"  ✓ Exportación exitosa: {size_mb:.2f} MB")
        return True
    else:
        print(f"  ✗ Error en exportación")
        return False


def main():
    print("\n" + "="*70)
    print("GENERACIÓN AUTOMÁTICA: REMY CON EMOCIÓN ALEGRÍA")
    print("="*70)
    
    try:
        clear_scene()
        
        # Paso 1: Importar Remy
        mesh, remy_height = import_remy()
        
        # Paso 2: Crear armature escalado
        armature = create_armature_scaled(remy_height)
        
        # Paso 3: Agregar shape keys
        add_shape_keys(mesh)
        
        # Paso 4: Setup drivers
        setup_emotion_drivers(mesh, armature)
        
        # Paso 5: Skinning
        skinning_ok = apply_skinning(mesh, armature)
        if not skinning_ok:
            print("\n❌ ERROR: Skinning no se aplicó correctamente")
            print("  El GLB no tendrá el mesh conectado al armature")
            return
        
        # Paso 6: Activar alegría
        activate_emotion(armature, 'EMOTION_ALEGRIA', 1.0)
        
        # Paso 7: Exportar
        success = export_glb(OUTPUT_GLB)
        
        print("\n" + "="*70)
        if success:
            print("✅ PROCESO COMPLETADO CON ÉXITO")
            print(f"Archivo: {OUTPUT_GLB}")
            print("\nVerifica:")
            print("  • Esqueleto del tamaño correcto de Remy")
            print("  • Emoción ALEGRÍA visible (sonrisa)")
            print("  • Skinning funcionando correctamente")
        else:
            print("❌ ERROR EN LA EXPORTACIÓN")
        print("="*70)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
