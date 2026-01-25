"""
Script para Blender: crea un personaje masculino completo (piel blanca, cabello corto, ropa casual),
con todas las extremidades detalladas (dedos de manos y pies) y shape keys completos de ARKit (52 blendshapes).

Uso:
1. Abre Blender 4.5+
2. Window -> Toggle System Console (para ver prints)
3. Scripting -> Text Editor -> Open -> este archivo
4. Alt+P para ejecutar

Salida: `output/MaleCharacter_Complete.fbx` con armature rigged y 52 facial shape keys
"""

import bpy
import os
import math
from mathutils import Vector, Euler

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'output')
OUT_DIR = os.path.abspath(OUT_DIR)
os.makedirs(OUT_DIR, exist_ok=True)
OUT_FBX = os.path.join(OUT_DIR, 'MaleCharacter_Complete.fbx')

# Ruta al GLB/FBX de Nancy para usar su malla (actualizado para nueva estructura)
# Buscar en múltiples ubicaciones posibles
NANCY_PATHS = [
    r'C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Mujer\Nancy.glb',
    r'C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\Nancy.glb',
    r'C:\Users\andre\OneDrive\Documentos\tesis\avatars\Nancy.fbx',
    r'C:\Users\andre\OneDrive\Documentos\tesis\output\Nancy.fbx',
    r'C:\Users\andre\Downloads\Nancy.fbx',
    os.path.join(os.path.dirname(__file__), 'Mujer', 'Nancy.glb'),
    os.path.join(os.path.dirname(__file__), 'Nancy', 'Nancy.glb'),
    os.path.join(os.path.dirname(__file__), '..', '..', 'avatars', 'Nancy.fbx'),
]

NANCY_GLB_PATH = None
for path in NANCY_PATHS:
    if os.path.exists(path):
        NANCY_GLB_PATH = path
        print(f"✓ Nancy encontrado en: {path}")
        break

if not NANCY_GLB_PATH:
    print(f"⚠ Nancy no encontrado. Buscado en:")
    for p in NANCY_PATHS:
        print(f"  - {p}")


# Lista completa de 52 ARKit blendshapes
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


def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for mesh in list(bpy.data.meshes):
        if mesh.users == 0:
            bpy.data.meshes.remove(mesh)
    for arm in list(bpy.data.armatures):
        if arm.users == 0:
            bpy.data.armatures.remove(arm)


def import_remy_mesh():
    """Importa la malla de Remy desde FBX y la retorna"""
    if not REMY_GLB_PATH or not os.path.exists(REMY_GLB_PATH):
        print(f"⚠ No se encontró Remy.fbx, creando malla simple")
        return None
    
    print(f"Importando malla de Remy desde: {REMY_GLB_PATH}")
    
    # Importar FBX
    bpy.ops.import_scene.fbx(filepath=REMY_GLB_PATH)
    
    # Buscar el mesh importado (usualmente se llama Wolf3D_Avatar o similar)
    imported_mesh = None
    imported_armature = None
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and ('Wolf3D' in obj.name or 'Remy' in obj.name or 'Avatar' in obj.name or 'Body' in obj.name):
            imported_mesh = obj
        elif obj.type == 'ARMATURE':
            imported_armature = obj
    
    # Si no encontró mesh específico, tomar el primero
    if not imported_mesh:
        for obj in bpy.data.objects:
            if obj.type == 'MESH':
                imported_mesh = obj
                break
    
    if imported_mesh:
        # Obtener dimensiones de Remy usando el armature original si existe
        if imported_armature:
            # Usar huesos del armature para calcular altura (más preciso)
            bpy.context.view_layer.objects.active = imported_armature
            bpy.ops.object.mode_set(mode='EDIT')
            bones = imported_armature.data.edit_bones
            
            # Buscar hueso Head y Hips/Root para altura
            head_bone = None
            root_bone = None
            
            for bone in bones:
                if 'head' in bone.name.lower():
                    head_bone = bone
                if 'hips' in bone.name.lower() or 'root' in bone.name.lower() or 'pelvis' in bone.name.lower():
                    root_bone = bone
            
            if head_bone and root_bone:
                remy_height = head_bone.tail.z - root_bone.head.z
                print(f"✓ Altura calculada desde armature: {remy_height:.2f} unidades")
            else:
                # Fallback: usar todo el armature
                all_z = [bone.head.z for bone in bones] + [bone.tail.z for bone in bones]
                remy_height = max(all_z) - min(all_z)
                print(f"✓ Altura estimada desde todos los huesos: {remy_height:.2f} unidades")
            
            bpy.ops.object.mode_set(mode='OBJECT')
            
            # Eliminar armature importado (usaremos uno nuevo)
            bpy.data.objects.remove(imported_armature, do_unlink=True)
            print(f"✓ Armature original removido")
        else:
            # Si no hay armature, usar bounding box del mesh (menos preciso)
            bpy.context.view_layer.objects.active = imported_mesh
            bpy.ops.object.select_all(action='DESELECT')
            imported_mesh.select_set(True)
            
            bbox = imported_mesh.bound_box
            min_z = min([v[2] for v in bbox])
            max_z = max([v[2] for v in bbox])
            remy_height = max_z - min_z
            print(f"✓ Altura de Remy (bbox): {remy_height:.2f} unidades")
        
        # Limpiar modificadores de armature existentes
        imported_mesh.modifiers.clear()
        
        # Renombrar
        imported_mesh.name = 'Character_Male'
        print(f"✓ Malla de Remy importada: {imported_mesh.name}")
        
        # Guardar altura para usar después
        imported_mesh['remy_height'] = remy_height
        
        return imported_mesh
    
    print("⚠ No se pudo encontrar mesh en el FBX de Remy")
    return None


def create_body_mesh():
    """Crea un cuerpo masculino más detallado con proporciones realistas"""
    # Torso (más anatómico)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 1.4))
    torso = bpy.context.active_object
    torso.name = 'Body'
    torso.scale = (0.45, 0.25, 0.65)
    bpy.ops.object.transform_apply(scale=True)
    
    # Cuello
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.12, depth=0.25, location=(0, 0, 1.95))
    neck = bpy.context.active_object
    neck.name = 'Neck'
    
    # Cabeza (más detallada con subdivisión)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, radius=0.24, location=(0, 0, 2.25))
    head = bpy.context.active_object
    head.name = 'Head'
    # Elongar ligeramente la cabeza
    head.scale = (1.0, 0.95, 1.15)
    bpy.ops.object.transform_apply(scale=True)
    
    # Subdividir la cabeza para shape keys más suaves
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.subdivide(number_cuts=2)
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.shade_smooth()
    
    # Hombros
    bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, radius=0.18, location=(0.50, 0, 1.75))
    shoulder_r = bpy.context.active_object
    shoulder_r.name = 'Shoulder_R'
    shoulder_r.scale = (1.2, 1.0, 0.8)
    
    bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, radius=0.18, location=(-0.50, 0, 1.75))
    shoulder_l = bpy.context.active_object
    shoulder_l.name = 'Shoulder_L'
    shoulder_l.scale = (1.2, 1.0, 0.8)
    
    # Brazos superiores
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.09, depth=0.50, location=(0.50, 0, 1.35))
    upper_arm_r = bpy.context.active_object
    upper_arm_r.name = 'UpperArm_R'
    
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.09, depth=0.50, location=(-0.50, 0, 1.35))
    upper_arm_l = bpy.context.active_object
    upper_arm_l.name = 'UpperArm_L'
    
    # Antebrazos
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.08, depth=0.45, location=(0.50, 0, 0.85))
    forearm_r = bpy.context.active_object
    forearm_r.name = 'Forearm_R'
    
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.08, depth=0.45, location=(-0.50, 0, 0.85))
    forearm_l = bpy.context.active_object
    forearm_l.name = 'Forearm_L'
    
    # Manos (palmas)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.50, 0, 0.55))
    hand_r = bpy.context.active_object
    hand_r.name = 'Hand_R'
    hand_r.scale = (0.11, 0.05, 0.15)
    bpy.ops.object.transform_apply(scale=True)
    
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.50, 0, 0.55))
    hand_l = bpy.context.active_object
    hand_l.name = 'Hand_L'
    hand_l.scale = (0.11, 0.05, 0.15)
    bpy.ops.object.transform_apply(scale=True)
    
    # Dedos de la mano (5 dedos por mano, 3 falanges cada uno)
    fingers_r = create_fingers((0.50, 0, 0.55), 'R')
    fingers_l = create_fingers((-0.50, 0, 0.55), 'L')
    
    # Pelvis
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.95))
    pelvis = bpy.context.active_object
    pelvis.name = 'Pelvis'
    pelvis.scale = (0.42, 0.23, 0.25)
    bpy.ops.object.transform_apply(scale=True)
    
    # Piernas superiores (muslos)
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.11, depth=0.55, location=(0.18, 0, 0.60))
    upper_leg_r = bpy.context.active_object
    upper_leg_r.name = 'UpperLeg_R'
    
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.11, depth=0.55, location=(-0.18, 0, 0.60))
    upper_leg_l = bpy.context.active_object
    upper_leg_l.name = 'UpperLeg_L'
    
    # Piernas inferiores (pantorrillas)
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.09, depth=0.50, location=(0.18, 0, 0.20))
    lower_leg_r = bpy.context.active_object
    lower_leg_r.name = 'LowerLeg_R'
    
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.09, depth=0.50, location=(-0.18, 0, 0.20))
    lower_leg_l = bpy.context.active_object
    lower_leg_l.name = 'LowerLeg_L'
    
    # Pies
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.18, 0.08, -0.03))
    foot_r = bpy.context.active_object
    foot_r.name = 'Foot_R'
    foot_r.scale = (0.10, 0.22, 0.06)
    bpy.ops.object.transform_apply(scale=True)
    
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.18, 0.08, -0.03))
    foot_l = bpy.context.active_object
    foot_l.name = 'Foot_L'
    foot_l.scale = (0.10, 0.22, 0.06)
    bpy.ops.object.transform_apply(scale=True)
    
    # Dedos de los pies (5 dedos simples por pie)
    toes_r = create_toes((0.18, 0.19, -0.03), 'R')
    toes_l = create_toes((-0.18, 0.19, -0.03), 'L')
    
    # Unir todas las partes del cuerpo
    all_parts = [torso, neck, head, shoulder_r, shoulder_l, 
                 upper_arm_r, upper_arm_l, forearm_r, forearm_l,
                 hand_r, hand_l, pelvis, upper_leg_r, upper_leg_l,
                 lower_leg_r, lower_leg_l, foot_r, foot_l]
    all_parts.extend(fingers_r)
    all_parts.extend(fingers_l)
    all_parts.extend(toes_r)
    all_parts.extend(toes_l)
    
    bpy.ops.object.select_all(action='DESELECT')
    for obj in all_parts:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = torso
    bpy.ops.object.join()
    
    character = bpy.context.active_object
    character.name = 'Character_Male'
    bpy.ops.object.shade_smooth()
    
    return character


def create_fingers(hand_pos, side):
    """Crea 5 dedos con 3 falanges cada uno"""
    fingers = []
    x, y, z = hand_pos
    
    # Parámetros de dedos
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    # Offsets en X para cada dedo
    if side == 'R':
        x_offsets = [0.05, 0.025, 0.0, -0.025, -0.05]
    else:
        x_offsets = [-0.05, -0.025, 0.0, 0.025, 0.05]
    
    for i, fname in enumerate(finger_names):
        fx = x + x_offsets[i]
        # Pulgar tiene orientación diferente
        if fname == 'Thumb':
            fy_start = y + 0.04
            fz_start = z + 0.05
        else:
            fy_start = y
            fz_start = z + 0.10
        
        # 3 falanges por dedo
        for j in range(3):
            if fname == 'Thumb':
                fz = fz_start + j * 0.04
                fy = fy_start + j * 0.02
            else:
                fz = fz_start + j * 0.035
                fy = fy_start
            
            bpy.ops.mesh.primitive_cylinder_add(vertices=8, radius=0.012, depth=0.03, location=(fx, fy, fz))
            phalanx = bpy.context.active_object
            phalanx.name = f'{fname}_{j+1}_{side}'
            fingers.append(phalanx)
    
    return fingers


def create_toes(foot_pos, side):
    """Crea 5 dedos simples para el pie"""
    toes = []
    x, y, z = foot_pos
    
    if side == 'R':
        x_offsets = [0.04, 0.02, 0.0, -0.02, -0.04]
    else:
        x_offsets = [-0.04, -0.02, 0.0, 0.02, 0.04]
    
    for i, offset in enumerate(x_offsets):
        tx = x + offset
        ty = y + 0.05
        tz = z
        
        bpy.ops.mesh.primitive_cylinder_add(vertices=8, radius=0.015, depth=0.04, location=(tx, ty, tz))
        toe = bpy.context.active_object
        toe.name = f'Toe_{i+1}_{side}'
        toe.rotation_euler[0] = math.radians(90)
        toes.append(toe)
    
    return toes


def add_materials(obj):
    """Material de piel blanca realista"""
    mat = bpy.data.materials.new('Skin_White')
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    
    # Principled BSDF
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = (0.95, 0.88, 0.82, 1.0)  # Piel blanca
    # Blender 4.x usa 'Subsurface Weight' en lugar de 'Subsurface'
    if 'Subsurface Weight' in bsdf.inputs:
        bsdf.inputs['Subsurface Weight'].default_value = 0.15
    elif 'Subsurface' in bsdf.inputs:
        bsdf.inputs['Subsurface'].default_value = 0.15
    if 'Subsurface Color' in bsdf.inputs:
        bsdf.inputs['Subsurface Color'].default_value = (0.9, 0.6, 0.5, 1.0)
    bsdf.inputs['Roughness'].default_value = 0.4
    
    output = nodes.new('ShaderNodeOutputMaterial')
    mat.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    
    obj.data.materials.append(mat)


def create_hair():
    """Cabello corto masculino más detallado"""
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=0.26, location=(0, 0, 2.32))
    hair = bpy.context.active_object
    hair.name = 'Hair'
    
    # Modificar forma para cabello corto masculino
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.transform.resize(value=(1.0, 0.85, 1.0))
    bpy.ops.transform.translate(value=(0, -0.03, 0.02))
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Eliminar parte inferior
    for v in hair.data.vertices:
        if v.co.z < 2.20:
            v.select = True
        else:
            v.select = False
    
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.delete(type='VERT')
    bpy.ops.object.mode_set(mode='OBJECT')
    
    hair.scale = (1.0, 0.9, 1.0)
    bpy.ops.object.shade_smooth()
    
    # Material de cabello
    mat = bpy.data.materials.new('Hair_Brown')
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = (0.12, 0.08, 0.05, 1.0)  # Castaño oscuro
    bsdf.inputs['Roughness'].default_value = 0.6
    
    output = nodes.new('ShaderNodeOutputMaterial')
    mat.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    
    hair.data.materials.append(mat)
    return hair


def create_clothes(character):
    """Camiseta casual"""
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 1.45))
    shirt = bpy.context.active_object
    shirt.name = 'Shirt'
    shirt.scale = (0.48, 0.27, 0.68)
    bpy.ops.object.transform_apply(scale=True)
    
    # Mangas
    bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=0.10, depth=0.35, location=(0.50, 0, 1.50))
    sleeve_r = bpy.context.active_object
    sleeve_r.name = 'Sleeve_R'
    
    bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=0.10, depth=0.35, location=(-0.50, 0, 1.50))
    sleeve_l = bpy.context.active_object
    sleeve_l.name = 'Sleeve_L'
    
    # Unir partes de la camisa
    bpy.ops.object.select_all(action='DESELECT')
    shirt.select_set(True)
    sleeve_r.select_set(True)
    sleeve_l.select_set(True)
    bpy.context.view_layer.objects.active = shirt
    bpy.ops.object.join()
    
    shirt = bpy.context.active_object
    bpy.ops.object.shade_smooth()
    
    # Material de camisa
    mat = bpy.data.materials.new('Shirt_Casual')
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = (0.15, 0.35, 0.65, 1.0)  # Azul casual
    bsdf.inputs['Roughness'].default_value = 0.7
    
    output = nodes.new('ShaderNodeOutputMaterial')
    mat.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    
    shirt.data.materials.append(mat)
    shirt.parent = character
    
    # Pantalones
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.60))
    pants = bpy.context.active_object
    pants.name = 'Pants'
    pants.scale = (0.44, 0.24, 0.80)
    bpy.ops.object.transform_apply(scale=True)
    bpy.ops.object.shade_smooth()
    
    # Material de pantalón
    mat_pants = bpy.data.materials.new('Pants_Jeans')
    mat_pants.use_nodes = True
    nodes = mat_pants.node_tree.nodes
    nodes.clear()
    
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = (0.10, 0.15, 0.25, 1.0)  # Azul oscuro (jeans)
    bsdf.inputs['Roughness'].default_value = 0.8
    
    output = nodes.new('ShaderNodeOutputMaterial')
    mat_pants.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    
    pants.data.materials.append(mat_pants)
    pants.parent = character
    
    return [shirt, pants]


def add_arkit_shapekeys(character):
    """Agrega los 52 shape keys de ARKit con deformaciones anatómicas realistas"""
    bpy.context.view_layer.objects.active = character
    
    if character.type != 'MESH':
        print("ERROR: El objeto no es una malla")
        return False
    
    # Basis shape key
    if not character.data.shape_keys:
        character.shape_key_add(name='Basis')
    
    print(f"Creando {len(ARKIT_BLENDSHAPES)} shape keys ARKit...")
    
    # Regiones anatómicas aproximadas (basadas en coordenadas Z de la cabeza)
    mesh = character.data
    
    # Crear cada shape key
    for sk_name in ARKIT_BLENDSHAPES:
        sk = character.shape_key_add(name=sk_name)
        
        # Aplicar deformaciones según el tipo de blendshape
        for i, v in enumerate(mesh.vertices):
            co = v.co.copy()
            
            # Solo modificar vértices de la cabeza (z > 2.0)
            if co.z < 2.0:
                sk.data[i].co = co
                continue
            
            delta = Vector((0, 0, 0))
            
            # CEJAS
            if 'brow' in sk_name.lower():
                if 2.35 < co.z < 2.48:  # Región de cejas
                    if 'InnerUp' in sk_name:
                        if abs(co.x) < 0.08:
                            delta.z = 0.02
                    elif 'Down' in sk_name:
                        if ('_L' in sk_name and co.x > 0.05) or ('_R' in sk_name and co.x < -0.05):
                            delta.z = -0.015
                    elif 'OuterUp' in sk_name:
                        if ('_L' in sk_name and co.x > 0.12) or ('_R' in sk_name and co.x < -0.12):
                            delta.z = 0.02
            
            # OJOS - Parpadeo
            elif 'eyeBlink' in sk_name:
                if 2.20 < co.z < 2.32:  # Región de ojos
                    if ('_L' in sk_name and co.x > 0.06) or ('_R' in sk_name and co.x < -0.06):
                        delta.z = -0.025
                        delta.y = -0.01
            
            # OJOS - Entrecerrar
            elif 'eyeSquint' in sk_name:
                if 2.18 < co.z < 2.28:
                    if ('_L' in sk_name and co.x > 0.06) or ('_R' in sk_name and co.x < -0.06):
                        delta.z = -0.015
                        delta.y = 0.005
            
            # OJOS - Abrir ampliamente
            elif 'eyeWide' in sk_name:
                if 2.20 < co.z < 2.32:
                    if ('_L' in sk_name and co.x > 0.06) or ('_R' in sk_name and co.x < -0.06):
                        delta.z = 0.02
            
            # OJOS - Mirada (movimiento de párpados)
            elif 'eyeLook' in sk_name:
                if 2.22 < co.z < 2.30:
                    if 'Up' in sk_name and (('_L' in sk_name and co.x > 0.06) or ('_R' in sk_name and co.x < -0.06)):
                        delta.z = 0.01
                    elif 'Down' in sk_name and (('_L' in sk_name and co.x > 0.06) or ('_R' in sk_name and co.x < -0.06)):
                        delta.z = -0.01
            
            # MEJILLAS
            elif 'cheekPuff' in sk_name:
                if 2.10 < co.z < 2.25:
                    if abs(co.x) > 0.08:
                        delta.x = co.x * 0.15  # Inflar hacia afuera
                        delta.y = abs(co.x) * 0.1
            
            elif 'cheekSquint' in sk_name:
                if 2.12 < co.z < 2.22:
                    if ('_L' in sk_name and co.x > 0.08) or ('_R' in sk_name and co.x < -0.08):
                        delta.z = 0.015
            
            # NARIZ
            elif 'noseSneer' in sk_name:
                if 2.15 < co.z < 2.25:
                    if ('_L' in sk_name and 0.02 < co.x < 0.10) or ('_R' in sk_name and -0.10 < co.x < -0.02):
                        delta.z = 0.015
                        delta.y = -0.01
            
            # MANDÍBULA
            elif 'jawOpen' in sk_name:
                if 2.05 < co.z < 2.18:
                    delta.z = -0.08
                    delta.y = 0.02
            
            elif 'jawForward' in sk_name:
                if 2.05 < co.z < 2.18:
                    delta.y = 0.04
            
            elif 'jawLeft' in sk_name:
                if 2.05 < co.z < 2.18:
                    delta.x = -0.03
            
            elif 'jawRight' in sk_name:
                if 2.05 < co.z < 2.18:
                    delta.x = 0.03
            
            # BOCA - Sonrisa
            elif 'mouthSmile' in sk_name:
                if 2.08 < co.z < 2.18:
                    if ('_L' in sk_name and co.x > 0.05) or ('_R' in sk_name and co.x < -0.05):
                        delta.x = co.x * 0.25  # Estirar hacia afuera
                        delta.z = 0.02  # Subir ligeramente
            
            # BOCA - Ceño fruncido
            elif 'mouthFrown' in sk_name:
                if 2.08 < co.z < 2.16:
                    if ('_L' in sk_name and co.x > 0.05) or ('_R' in sk_name and co.x < -0.05):
                        delta.z = -0.02
            
            # BOCA - Embudo
            elif 'mouthFunnel' in sk_name:
                if 2.08 < co.z < 2.18:
                    if abs(co.x) < 0.10:
                        delta.y = 0.03
                        delta.x = co.x * 0.5  # Contraer hacia el centro
            
            # BOCA - Puchero
            elif 'mouthPucker' in sk_name:
                if 2.08 < co.z < 2.18:
                    if abs(co.x) < 0.10:
                        delta.y = 0.04
                        delta.x = co.x * 0.3
            
            # BOCA - Izquierda/Derecha
            elif 'mouthLeft' in sk_name:
                if 2.08 < co.z < 2.18:
                    if abs(co.x) < 0.12:
                        delta.x = -0.03
            
            elif 'mouthRight' in sk_name:
                if 2.08 < co.z < 2.18:
                    if abs(co.x) < 0.12:
                        delta.x = 0.03
            
            # BOCA - Labio superior arriba
            elif 'mouthUpperUp' in sk_name:
                if 2.14 < co.z < 2.20:
                    if ('_L' in sk_name and co.x > 0.02) or ('_R' in sk_name and co.x < -0.02):
                        delta.z = 0.02
            
            # BOCA - Labio inferior abajo
            elif 'mouthLowerDown' in sk_name:
                if 2.08 < co.z < 2.14:
                    if ('_L' in sk_name and co.x > 0.02) or ('_R' in sk_name and co.x < -0.02):
                        delta.z = -0.02
            
            # BOCA - Presionar labios
            elif 'mouthPress' in sk_name:
                if 2.10 < co.z < 2.17:
                    if ('_L' in sk_name and co.x > 0.02) or ('_R' in sk_name and co.x < -0.02):
                        delta.y = -0.01
            
            # BOCA - Estirar
            elif 'mouthStretch' in sk_name:
                if 2.08 < co.z < 2.18:
                    if ('_L' in sk_name and co.x > 0.05) or ('_R' in sk_name and co.x < -0.05):
                        delta.x = co.x * 0.3
            
            # BOCA - Enrollar labios
            elif 'mouthRollUpper' in sk_name:
                if 2.14 < co.z < 2.20:
                    if abs(co.x) < 0.10:
                        delta.y = -0.015
            
            elif 'mouthRollLower' in sk_name:
                if 2.08 < co.z < 2.14:
                    if abs(co.x) < 0.10:
                        delta.y = -0.015
            
            # BOCA - Hombros (shrug)
            elif 'mouthShrugUpper' in sk_name:
                if 2.14 < co.z < 2.20:
                    if abs(co.x) < 0.10:
                        delta.z = 0.01
                        delta.y = 0.01
            
            elif 'mouthShrugLower' in sk_name:
                if 2.08 < co.z < 2.14:
                    if abs(co.x) < 0.10:
                        delta.z = -0.01
                        delta.y = 0.01
            
            # BOCA - Cerrar
            elif 'mouthClose' in sk_name:
                if 2.10 < co.z < 2.17:
                    if abs(co.x) < 0.10:
                        delta.y = -0.01
            
            # BOCA - Hoyuelos
            elif 'mouthDimple' in sk_name:
                if 2.10 < co.z < 2.16:
                    if ('_L' in sk_name and 0.08 < co.x < 0.14) or ('_R' in sk_name and -0.14 < co.x < -0.08):
                        delta.y = -0.015
                        delta.z = -0.01
            
            # LENGUA
            elif 'tongueOut' in sk_name:
                if 2.08 < co.z < 2.14:
                    if abs(co.x) < 0.06:
                        delta.y = 0.05
                        delta.z = -0.01
            
            sk.data[i].co = co + delta
        
        sk.value = 0.0
    
    print(f"✓ {len(ARKIT_BLENDSHAPES)} shape keys creados exitosamente")
    return True


def create_armature(target_height=1.80):
    """Crea un armature completo estilo Mixamo con todos los huesos de dedos
    
    Args:
        target_height: Altura total deseada del armature (desde pies hasta cabeza)
    """
    bpy.ops.object.armature_add(location=(0, 0, 0))
    armature = bpy.context.active_object
    armature.name = 'Armature'
    armature.show_in_front = True
    
    bpy.ops.object.mode_set(mode='EDIT')
    bones = armature.data.edit_bones
    
    # Limpiar hueso por defecto
    bones.remove(bones[0])
    
    # Calcular factor de escala basado en altura objetivo
    # Altura base del esqueleto = 2.50 (head tail)
    base_height = 2.50
    scale_factor = target_height / base_height
    
    print(f"  Escalando armature: factor {scale_factor:.3f} (altura objetivo: {target_height:.2f})")
    
    def scaled(z):
        """Escala coordenada Z"""
        return z * scale_factor
    
    # HIPS (root)
    hips = bones.new('Hips')
    hips.head = (0, 0, scaled(0.95))
    hips.tail = (0, 0, scaled(1.10))
    
    # SPINE (columna vertebral)
    spine = bones.new('Spine')
    spine.head = (0, 0, scaled(0.95))
    spine.tail = (0, 0, scaled(1.25))
    spine.parent = hips
    
    spine1 = bones.new('Spine1')
    spine1.head = (0, 0, scaled(1.25))
    spine1.tail = (0, 0, scaled(1.50))
    spine1.parent = spine
    
    spine2 = bones.new('Spine2')
    spine2.head = (0, 0, scaled(1.50))
    spine2.tail = (0, 0, scaled(1.75))
    spine2.parent = spine1
    
    # NECK y HEAD
    neck = bones.new('Neck')
    neck.head = (0, 0, scaled(1.75))
    neck.tail = (0, 0, scaled(1.95))
    neck.parent = spine2
    
    head = bones.new('Head')
    head.head = (0, 0, scaled(1.95))
    head.tail = (0, 0, scaled(2.50))
    head.parent = neck
    
    # BRAZOS Y MANOS (ambos lados)
    for side, sign in [('Left', -1), ('Right', 1)]:
        # Hombro/Clavícula
        shoulder = bones.new(f'{side}Shoulder')
        shoulder.head = (0, 0, scaled(1.75))
        shoulder.tail = (sign * 0.25 * scale_factor, 0, scaled(1.75))
        shoulder.parent = spine2
        
        # Brazo superior
        arm = bones.new(f'{side}Arm')
        arm.head = (sign * 0.25 * scale_factor, 0, scaled(1.75))
        arm.tail = (sign * 0.50 * scale_factor, 0, scaled(1.10))
        arm.parent = shoulder
        
        # Antebrazo
        forearm = bones.new(f'{side}ForeArm')
        forearm.head = (sign * 0.50 * scale_factor, 0, scaled(1.10))
        forearm.tail = (sign * 0.50 * scale_factor, 0, scaled(0.60))
        forearm.parent = arm
        
        # Mano
        hand = bones.new(f'{side}Hand')
        hand.head = (sign * 0.50 * scale_factor, 0, scaled(0.60))
        hand.tail = (sign * 0.50 * scale_factor, 0, scaled(0.48))
        hand.parent = forearm
        
        # DEDOS DE LA MANO (5 dedos × 3 falanges cada uno)
        # Pulgar (Thumb)
        thumb1 = bones.new(f'{side}HandThumb1')
        thumb1.head = (sign * 0.50 * scale_factor, 0.03 * scale_factor, scaled(0.58))
        thumb1.tail = (sign * 0.52 * scale_factor, 0.05 * scale_factor, scaled(0.60))
        thumb1.parent = hand
        
        thumb2 = bones.new(f'{side}HandThumb2')
        thumb2.head = thumb1.tail
        thumb2.tail = (sign * 0.54 * scale_factor, 0.07 * scale_factor, scaled(0.62))
        thumb2.parent = thumb1
        
        thumb3 = bones.new(f'{side}HandThumb3')
        thumb3.head = thumb2.tail
        thumb3.tail = (sign * 0.56 * scale_factor, 0.09 * scale_factor, scaled(0.63))
        thumb3.parent = thumb2
        
        # Índice (Index)
        index1 = bones.new(f'{side}HandIndex1')
        index1.head = (sign * 0.525 * scale_factor, 0, scaled(0.50))
        index1.tail = (sign * 0.525 * scale_factor, 0, scaled(0.47))
        index1.parent = hand
        
        index2 = bones.new(f'{side}HandIndex2')
        index2.head = index1.tail
        index2.tail = (sign * 0.525 * scale_factor, 0, scaled(0.44))
        index2.parent = index1
        
        index3 = bones.new(f'{side}HandIndex3')
        index3.head = index2.tail
        index3.tail = (sign * 0.525 * scale_factor, 0, scaled(0.41))
        index3.parent = index2
        
        # Medio (Middle)
        middle1 = bones.new(f'{side}HandMiddle1')
        middle1.head = (sign * 0.50 * scale_factor, 0, scaled(0.50))
        middle1.tail = (sign * 0.50 * scale_factor, 0, scaled(0.47))
        middle1.parent = hand
        
        middle2 = bones.new(f'{side}HandMiddle2')
        middle2.head = middle1.tail
        middle2.tail = (sign * 0.50 * scale_factor, 0, scaled(0.44))
        middle2.parent = middle1
        
        middle3 = bones.new(f'{side}HandMiddle3')
        middle3.head = middle2.tail
        middle3.tail = (sign * 0.50 * scale_factor, 0, scaled(0.40))
        middle3.parent = middle2
        
        # Anular (Ring)
        ring1 = bones.new(f'{side}HandRing1')
        ring1.head = (sign * 0.475 * scale_factor, 0, scaled(0.50))
        ring1.tail = (sign * 0.475 * scale_factor, 0, scaled(0.47))
        ring1.parent = hand
        
        ring2 = bones.new(f'{side}HandRing2')
        ring2.head = ring1.tail
        ring2.tail = (sign * 0.475 * scale_factor, 0, scaled(0.44))
        ring2.parent = ring1
        
        ring3 = bones.new(f'{side}HandRing3')
        ring3.head = ring2.tail
        ring3.tail = (sign * 0.475 * scale_factor, 0, scaled(0.41))
        ring3.parent = ring2
        
        # Meñique (Pinky)
        pinky1 = bones.new(f'{side}HandPinky1')
        pinky1.head = (sign * 0.45 * scale_factor, 0, scaled(0.50))
        pinky1.tail = (sign * 0.45 * scale_factor, 0, scaled(0.48))
        pinky1.parent = hand
        
        pinky2 = bones.new(f'{side}HandPinky2')
        pinky2.head = pinky1.tail
        pinky2.tail = (sign * 0.45 * scale_factor, 0, scaled(0.46))
        pinky2.parent = pinky1
        
        pinky3 = bones.new(f'{side}HandPinky3')
        pinky3.head = pinky2.tail
        pinky3.tail = (sign * 0.45 * scale_factor, 0, scaled(0.44))
        pinky3.parent = pinky2
    
    # PIERNAS Y PIES (ambos lados)
    for side, sign in [('Left', -1), ('Right', 1)]:
        # Muslo
        upleg = bones.new(f'{side}UpLeg')
        upleg.head = (sign * 0.18 * scale_factor, 0, scaled(0.95))
        upleg.tail = (sign * 0.18 * scale_factor, 0, scaled(0.35))
        upleg.parent = hips
        
        # Pantorrilla
        leg = bones.new(f'{side}Leg')
        leg.head = (sign * 0.18 * scale_factor, 0, scaled(0.35))
        leg.tail = (sign * 0.18 * scale_factor, 0, scaled(-0.05))
        leg.parent = upleg
        
        # Pie
        foot = bones.new(f'{side}Foot')
        foot.head = (sign * 0.18 * scale_factor, 0, scaled(-0.05))
        foot.tail = (sign * 0.18 * scale_factor, 0.15 * scale_factor, scaled(-0.05))
        foot.parent = leg
        
        # Dedos del pie
        toebase = bones.new(f'{side}ToeBase')
        toebase.head = (sign * 0.18 * scale_factor, 0.15 * scale_factor, scaled(-0.05))
        toebase.tail = (sign * 0.18 * scale_factor, 0.22 * scale_factor, scaled(-0.05))
        toebase.parent = foot
    
    bpy.ops.object.mode_set(mode='OBJECT')
    return armature


def export_fbx(filepath):
    """Exporta la escena completa a FBX"""
    print(f"\n=== Exportando a: {filepath} ===")
    bpy.ops.export_scene.fbx(
        filepath=filepath,
        use_selection=False,
        apply_unit_scale=True,
        apply_scale_options='FBX_SCALE_ALL',
        bake_space_transform=False,
        object_types={'ARMATURE', 'MESH'},
        use_mesh_modifiers=True,
        mesh_smooth_type='FACE',
        use_custom_props=True,
        bake_anim=False
    )
    
    if os.path.exists(filepath):
        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        print(f"✓ Exportación exitosa: {size_mb:.2f} MB")
    else:
        print("✗ Error: archivo no se creó")


def export_glb(filepath):
    """Exporta la escena a formato GLB"""
    glb_path = filepath.replace('.fbx', '.glb')
    print(f"\n=== Exportando también a GLB: {glb_path} ===")
    
    bpy.ops.export_scene.gltf(
        filepath=glb_path,
        export_format='GLB',
        use_selection=False,
        export_apply=True,
        export_animations=False,
        export_morph=True,  # Exportar shape keys
        export_skins=True,  # Exportar skinning
        export_materials='EXPORT'
    )
    
    if os.path.exists(glb_path):
        size_mb = os.path.getsize(glb_path) / (1024 * 1024)
        print(f"✓ Exportación GLB exitosa: {size_mb:.2f} MB")
        return glb_path
    else:
        print("✗ Error: archivo GLB no se creó")
        return None


def test_shapekeys(character):
    """Prueba los shape keys aplicando valores y verificando"""
    if not character.data.shape_keys:
        print("⚠ El personaje no tiene shape keys")
        return
    
    print(f"\nProbando {len(character.data.shape_keys.key_blocks)} shape keys...")
    
    # Probar algunos shape keys representativos
    test_keys = ['mouthSmile_L', 'mouthSmile_R', 'eyeBlink_L', 'eyeBlink_R', 
                 'browInnerUp', 'jawOpen', 'mouthFunnel', 'cheekPuff']
    
    for key_name in test_keys:
        if key_name in character.data.shape_keys.key_blocks:
            key = character.data.shape_keys.key_blocks[key_name]
            key.value = 1.0
            print(f"  ✓ {key_name}: activado (value=1.0)")
        else:
            print(f"  ✗ {key_name}: no encontrado")
    
    # Resetear todos
    for key in character.data.shape_keys.key_blocks:
        key.value = 0.0
    
    print("\n✓ Prueba completada - todos los shape keys reseteados")
    print("  Importa el GLB/FBX y verifica los shape keys manualmente")


def main():
    print('\n' + '='*60)
    print('CREANDO PERSONAJE MASCULINO COMPLETO CON MALLA DE REMY')
    print('='*60)
    
    clear_scene()
    
    print('\n[1/7] Importando malla de Remy...')
    character = import_remy_mesh()
    
    # Si no se pudo importar Remy, crear cuerpo simple
    if not character:
        print('[1/7] Creando cuerpo alternativo...')
        character = create_body_mesh()
        print('[2/7] Aplicando materiales de piel...')
        add_materials(character)
        print('[3/7] Creando cabello corto...')
        hair = create_hair()
        hair.parent = character
        print('[4/7] Agregando ropa casual...')
        clothes = create_clothes(character)
    else:
        print('[2/7] Malla de Remy cargada correctamente')
        # Remy ya tiene materiales, saltar pasos de creación
        print('[3/7] Usando materiales existentes de Remy')
        print('[4/7] Usando ropa existente de Remy')
    
    print(f'[5/7] Creando {len(ARKIT_BLENDSHAPES)} shape keys ARKit...')
    success = add_arkit_shapekeys(character)
    if not success:
        print('ERROR: No se pudieron crear los shape keys')
        return
    
    print('[6/7] Creando armature tipo Mixamo escalado a Remy...')
    # Obtener altura de Remy si está disponible
    remy_height = character.get('remy_height', 1.80)
    armature = create_armature(target_height=remy_height)
    
    print('[6.5/7] Aplicando skinning automático (Automatic Weights)...')
    # Seleccionar mesh y armature
    bpy.ops.object.select_all(action='DESELECT')
    character.select_set(True)
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    
    # Parent con Automatic Weights
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')
    print('✓ Skinning aplicado')
    
    print('[7/7] Exportando a FBX...')
    export_fbx(OUT_FBX)
    
    print('[7.5/7] Exportando a GLB...')
    glb_file = export_glb(OUT_FBX)
    
    print('\n' + '='*60)
    print('✓ PROCESO COMPLETADO')
    print(f'Archivo FBX: {OUT_FBX}')
    if glb_file:
        print(f'Archivo GLB: {glb_file}')
    print('='*60)
    print('\nVerifica que el personaje tenga:')
    print('  • Malla de Remy con skinning automático')
    print(f'  • {len(ARKIT_BLENDSHAPES)} shape keys ARKit')
    print('  • Armature Mixamo con 65+ huesos (dedos incluidos)')
    print('  • Vertex weights aplicados automáticamente')
    
    # Probar shape keys
    print('\n' + '='*60)
    print('PROBANDO SHAPE KEYS')
    print('='*60)
    test_shapekeys(character)


if __name__ == '__main__':
    main()
