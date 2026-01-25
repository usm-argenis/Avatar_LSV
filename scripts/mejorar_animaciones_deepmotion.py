"""
Script para mejorar animaciones exportadas desde DeepMotion
Soluciona problemas comunes:
- Dedos ocultos en el pecho
- Brazos demasiado pegados al cuerpo
- Manos que atraviesan el torso

Uso:
    python scripts/mejorar_animaciones_deepmotion.py
    
    O especificar archivo:
    python scripts/mejorar_animaciones_deepmotion.py --input path/to/animation.glb
"""

import bpy
import sys
import os
from pathlib import Path
import math
import argparse

def setup_blender_environment():
    """Configurar entorno Blender para procesamiento batch"""
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Configurar rendering (compatible con Blender 4.5+)
    try:
        bpy.context.scene.render.engine = 'BLENDER_EEVEE_NEXT'  # Blender 4.5+
    except:
        try:
            bpy.context.scene.render.engine = 'BLENDER_EEVEE'  # Blender 4.0-4.4
        except:
            pass  # Si ninguno funciona, usar el default
    
    print("✅ Entorno Blender configurado")

def cargar_animacion(filepath):
    """Cargar archivo GLB/FBX"""
    print(f"📂 Cargando: {filepath}")
    
    extension = filepath.suffix.lower()
    
    try:
        if extension == '.glb' or extension == '.gltf':
            bpy.ops.import_scene.gltf(filepath=str(filepath))
        elif extension == '.fbx':
            bpy.ops.import_scene.fbx(filepath=str(filepath))
        else:
            raise ValueError(f"Formato no soportado: {extension}")
        
        # Obtener armature
        armature = None
        for obj in bpy.context.scene.objects:
            if obj.type == 'ARMATURE':
                armature = obj
                break
        
        if not armature:
            raise ValueError("No se encontró armature en el archivo")
        
        print(f"✅ Cargado: {armature.name}")
        return armature
    
    except Exception as e:
        print(f"❌ Error al cargar archivo: {e}")
        return None

def identificar_huesos(armature):
    """Identificar huesos importantes del rig"""
    print("🔍 Identificando huesos...")
    
    bones_map = {
        'spine': None,
        'chest': None,
        'shoulder_l': None,
        'shoulder_r': None,
        'upper_arm_l': None,
        'upper_arm_r': None,
        'forearm_l': None,
        'forearm_r': None,
        'hand_l': None,
        'hand_r': None,
    }
    
    # Patrones comunes de nombres de huesos
    patterns = {
        'spine': ['spine', 'column', 'vertebra'],
        'chest': ['chest', 'upper_body', 'torso', 'ribcage'],
        'shoulder_l': ['shoulder.l', 'shoulder_l', 'leftshoulder', 'l_shoulder', 'clavicle.l'],
        'shoulder_r': ['shoulder.r', 'shoulder_r', 'rightshoulder', 'r_shoulder', 'clavicle.r'],
        'upper_arm_l': ['upperarm.l', 'upper_arm.l', 'arm.l', 'leftarm', 'l_upperarm'],
        'upper_arm_r': ['upperarm.r', 'upper_arm.r', 'arm.r', 'rightarm', 'r_upperarm'],
        'forearm_l': ['forearm.l', 'lowerarm.l', 'leftforearm', 'l_forearm'],
        'forearm_r': ['forearm.r', 'lowerarm.r', 'rightforearm', 'r_forearm'],
        'hand_l': ['hand.l', 'lefthand', 'l_hand', 'wrist.l'],
        'hand_r': ['hand.r', 'righthand', 'r_hand', 'wrist.r'],
    }
    
    pose_bones = armature.pose.bones
    
    for bone in pose_bones:
        bone_name_lower = bone.name.lower()
        
        for key, pattern_list in patterns.items():
            if bones_map[key] is None:
                for pattern in pattern_list:
                    if pattern in bone_name_lower:
                        bones_map[key] = bone.name
                        print(f"  ✓ {key}: {bone.name}")
                        break
    
    return bones_map

def aplicar_mejoras_pose(armature, bones_map, separacion_brazos=30, elevacion_brazos=20):
    """
    Aplicar transformaciones para evitar colisiones con el pecho
    
    Args:
        armature: Armature object
        bones_map: Diccionario con nombres de huesos identificados
        separacion_brazos: Grados de separación lateral (0-40)
        elevacion_brazos: Grados de elevación frontal (0-30)
    """
    print("\n🔧 Aplicando mejoras...")
    print(f"  📐 Separación lateral: {separacion_brazos}°")
    print(f"  📐 Elevación frontal: {elevacion_brazos}°")
    
    # Seleccionar armature y entrar en pose mode
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    
    # IMPORTANTE: Fijar modo de rotación ANTES de aplicar transformaciones
    print("  🔧 Configurando modos de rotación...")
    for bone_key in ['shoulder_l', 'shoulder_r', 'upper_arm_l', 'upper_arm_r', 'spine', 'chest']:
        if bones_map.get(bone_key):
            bone = armature.pose.bones[bones_map[bone_key]]
            bone.rotation_mode = 'XYZ'  # Usar Euler XYZ para todos
    
    # Obtener action actual
    if not armature.animation_data or not armature.animation_data.action:
        print("⚠️ No hay animación, aplicando pose estática")
        aplicar_pose_estatica(armature, bones_map, separacion_brazos, elevacion_brazos)
        return
    
    action = armature.animation_data.action
    frame_start = int(action.frame_range[0])
    frame_end = int(action.frame_range[1])
    total_frames = frame_end - frame_start + 1
    
    print(f"  🎬 Procesando {total_frames} frames ({frame_start} → {frame_end})")
    
    # NUEVO ENFOQUE: Modificar directamente las F-Curves (keyframes) en lugar de bakear
    print("  🔧 Modificando keyframes directamente...")
    
    # Para cada hueso que queremos modificar
    for bone_key in ['shoulder_l', 'shoulder_r', 'upper_arm_l', 'upper_arm_r', 'spine']:
        if not bones_map.get(bone_key):
            continue
            
        bone_name = bones_map[bone_key]
        bone = armature.pose.bones[bone_name]
        
        # Calcular los offsets según el tipo de hueso
        offset_x = 0
        offset_y = 0
        offset_z = 0
        
        if bone_key == 'shoulder_l':
            offset_z = math.radians(separacion_brazos * 1.2)
        elif bone_key == 'shoulder_r':
            offset_z = -math.radians(separacion_brazos * 1.2)
        elif bone_key == 'upper_arm_l':
            offset_x = math.radians(elevacion_brazos * 1.3)
            offset_z = math.radians(separacion_brazos * 0.8)
        elif bone_key == 'upper_arm_r':
            offset_x = math.radians(elevacion_brazos * 1.3)
            offset_z = -math.radians(separacion_brazos * 0.8)
        elif bone_key == 'spine':
            offset_x = -math.radians(5)  # Enderezar
        
        # Buscar las F-Curves de rotación Euler para este hueso
        data_path = f'pose.bones["{bone_name}"].rotation_euler'
        
        # Modificar cada componente (X, Y, Z) si existe
        for axis_index, offset in enumerate([offset_x, offset_y, offset_z]):
            if offset == 0:
                continue
                
            fcurve = None
            for fc in action.fcurves:
                if fc.data_path == data_path and fc.array_index == axis_index:
                    fcurve = fc
                    break
            
            if fcurve:
                # Modificar cada keyframe sumando el offset
                for keyframe in fcurve.keyframe_points:
                    keyframe.co[1] += offset  # co[1] es el valor Y (la rotación)
                    keyframe.handle_left[1] += offset
                    keyframe.handle_right[1] += offset
    
    print(f"  ✅ Keyframes modificados en {len([k for k in bones_map.keys() if bones_map.get(k)])} huesos")
    
    # Volver a object mode
    bpy.ops.object.mode_set(mode='OBJECT')

def corregir_postura_torso(armature, bones_map):
    """Corregir postura del torso (alinear tren superior con inferior)"""
    if bones_map.get('spine'):
        bone = armature.pose.bones[bones_map['spine']]
        # Enderezar la espalda ligeramente (reducir curvatura)
        # Rotación negativa en X para enderezar
        bone.rotation_euler[0] -= math.radians(5)  # Enderezar 5 grados
    
    if bones_map.get('chest'):
        bone = armature.pose.bones[bones_map['chest']]
        # Alinear el pecho
        bone.rotation_euler[0] -= math.radians(3)  # Enderezar 3 grados

def ajustar_brazo_izquierdo(armature, bones_map, separacion, elevacion):
    """Ajustar brazo izquierdo para evitar colisión con pecho"""
    # Shoulder
    if bones_map.get('shoulder_l'):
        bone = armature.pose.bones[bones_map['shoulder_l']]
        # Separar lateralmente (más agresivo)
        bone.rotation_euler[2] += math.radians(separacion * 1.2)  # Z-axis (20% más)
    
    # Upper arm
    if bones_map.get('upper_arm_l'):
        bone = armature.pose.bones[bones_map['upper_arm_l']]
        # Elevar hacia adelante (más visible)
        bone.rotation_euler[0] += math.radians(elevacion * 1.3)   # X-axis (30% más)
        # Separar del cuerpo
        bone.rotation_euler[2] += math.radians(separacion * 0.8)  # Z-axis

def ajustar_brazo_derecho(armature, bones_map, separacion, elevacion):
    """Ajustar brazo derecho para evitar colisión con pecho"""
    # Shoulder
    if bones_map.get('shoulder_r'):
        bone = armature.pose.bones[bones_map['shoulder_r']]
        # Separar lateralmente (invertido para derecha, más agresivo)
        bone.rotation_euler[2] -= math.radians(separacion * 1.2)
    
    # Upper arm
    if bones_map.get('upper_arm_r'):
        bone = armature.pose.bones[bones_map['upper_arm_r']]
        # Elevar hacia adelante (más visible)
        bone.rotation_euler[0] += math.radians(elevacion * 1.3)
        # Separar del cuerpo (invertido para derecha)
        bone.rotation_euler[2] -= math.radians(separacion * 0.8)

def aplicar_pose_estatica(armature, bones_map, separacion, elevacion):
    """Aplicar ajustes a pose estática (sin animación)"""
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    
    # Fijar modos de rotación
    for bone_key in ['shoulder_l', 'shoulder_r', 'upper_arm_l', 'upper_arm_r', 'spine', 'chest']:
        if bones_map.get(bone_key):
            bone = armature.pose.bones[bones_map[bone_key]]
            bone.rotation_mode = 'XYZ'
    
    corregir_postura_torso(armature, bones_map)
    ajustar_brazo_izquierdo(armature, bones_map, separacion, elevacion)
    ajustar_brazo_derecho(armature, bones_map, separacion, elevacion)
    
    bpy.ops.object.mode_set(mode='OBJECT')
    print("  ✅ Pose estática ajustada")

def exportar_resultado(armature, output_path, formato='glb'):
    """Exportar animación mejorada"""
    print(f"\n💾 Exportando a: {output_path}")
    
    # Seleccionar solo el armature y su mesh
    bpy.ops.object.select_all(action='DESELECT')
    armature.select_set(True)
    
    # Seleccionar meshes hijos
    for obj in bpy.data.objects:
        if obj.parent == armature:
            obj.select_set(True)
    
    bpy.context.view_layer.objects.active = armature
    
    try:
        if formato == 'glb':
            # Blender 4.5+ cambió los parámetros del exportador
            try:
                # Intenta con parámetros de Blender 4.5+
                bpy.ops.export_scene.gltf(
                    filepath=str(output_path),
                    export_format='GLB',
                    use_selection=True,  # Cambió de export_selected a use_selection
                    export_animations=True,
                    export_animation_mode='ACTIONS',
                    export_bake_animation=True,
                    export_optimize_animation_size=False,
                    export_hierarchy_flatten_bones=False
                )
            except TypeError:
                # Fallback para Blender 4.0-4.4
                bpy.ops.export_scene.gltf(
                    filepath=str(output_path),
                    export_format='GLB',
                    export_selected=True,
                    export_animations=True,
                    export_force_sampling=True,
                    export_def_bones=False,
                    export_optimize_animation_size=False
                )
        elif formato == 'fbx':
            bpy.ops.export_scene.fbx(
                filepath=str(output_path),
                use_selection=True,
                bake_anim=True,
                add_leaf_bones=False
            )
        
        print(f"✅ Exportado: {output_path}")
        return True
    
    except Exception as e:
        print(f"❌ Error al exportar: {e}")
        return False

def procesar_archivo(input_path, output_path=None, separacion=15, elevacion=10):
    """Procesar un archivo completo"""
    input_path = Path(input_path)
    
    if not input_path.exists():
        print(f"❌ Archivo no encontrado: {input_path}")
        return False
    
    # Generar nombre de salida si no se proporciona
    if output_path is None:
        output_path = input_path.parent / f"{input_path.stem}_mejorado{input_path.suffix}"
    else:
        output_path = Path(output_path)
    
    print("=" * 70)
    print("🚀 MEJORADOR DE ANIMACIONES DEEPMOTION")
    print("=" * 70)
    print(f"📥 Input:  {input_path}")
    print(f"📤 Output: {output_path}")
    print(f"🎚️  Separación: {separacion}° | Elevación: {elevacion}°")
    print("=" * 70)
    
    # Limpiar escena
    setup_blender_environment()
    
    # Cargar archivo
    armature = cargar_animacion(input_path)
    if not armature:
        return False
    
    # Identificar huesos
    bones_map = identificar_huesos(armature)
    
    # Verificar que se encontraron huesos importantes
    huesos_criticos = ['upper_arm_l', 'upper_arm_r']
    if not all(bones_map.get(key) for key in huesos_criticos):
        print("⚠️ Advertencia: No se encontraron todos los huesos críticos")
        print("   Continuando con los huesos disponibles...")
    
    # Aplicar mejoras
    aplicar_mejoras_pose(armature, bones_map, separacion, elevacion)
    
    # Exportar
    success = exportar_resultado(armature, output_path, formato=input_path.suffix[1:])
    
    if success:
        print("\n" + "=" * 70)
        print("✅ PROCESO COMPLETADO EXITOSAMENTE")
        print("=" * 70)
        print(f"📁 Archivo mejorado guardado en:")
        print(f"   {output_path.absolute()}")
        print("\n💡 Consejos:")
        print("   • Si los brazos siguen muy pegados, aumenta --separacion")
        print("   • Si las manos atraviesan el pecho, aumenta --elevacion")
        print("   • Valores recomendados: separacion=10-20, elevacion=5-15")
    
    return success

def procesar_directorio(input_dir, output_dir=None, separacion=15, elevacion=10):
    """Procesar todos los archivos GLB/FBX en un directorio"""
    input_dir = Path(input_dir)
    
    if not input_dir.exists():
        print(f"❌ Directorio no encontrado: {input_dir}")
        return
    
    if output_dir is None:
        output_dir = input_dir / "mejorados"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Buscar archivos
    archivos = list(input_dir.glob("*.glb")) + list(input_dir.glob("*.fbx"))
    
    if not archivos:
        print(f"⚠️ No se encontraron archivos GLB/FBX en: {input_dir}")
        return
    
    print(f"\n📂 Procesando {len(archivos)} archivos...")
    
    exitosos = 0
    fallidos = 0
    
    for i, archivo in enumerate(archivos, 1):
        print(f"\n{'='*70}")
        print(f"📄 Archivo {i}/{len(archivos)}: {archivo.name}")
        print('='*70)
        
        output_path = output_dir / f"{archivo.stem}_mejorado{archivo.suffix}"
        
        if procesar_archivo(archivo, output_path, separacion, elevacion):
            exitosos += 1
        else:
            fallidos += 1
        
        # Limpiar escena para siguiente archivo
        setup_blender_environment()
    
    print(f"\n{'='*70}")
    print("📊 RESUMEN FINAL")
    print('='*70)
    print(f"✅ Exitosos: {exitosos}")
    print(f"❌ Fallidos: {fallidos}")
    print(f"📁 Archivos guardados en: {output_dir.absolute()}")

def main():
    """Función principal con argumentos de línea de comandos"""
    parser = argparse.ArgumentParser(
        description='Mejorar animaciones de DeepMotion evitando colisiones con el pecho',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  # Procesar un archivo individual
  blender --background --python mejorar_animaciones_deepmotion.py -- --input Remy_resultado_c.glb

  # Procesar con ajustes personalizados
  blender --background --python mejorar_animaciones_deepmotion.py -- --input animation.glb --separacion 20 --elevacion 15

  # Procesar todos los archivos de un directorio
  blender --background --python mejorar_animaciones_deepmotion.py -- --directorio test/output/glb

  # Especificar directorio de salida
  blender --background --python mejorar_animaciones_deepmotion.py -- --directorio test/output/glb --output mejorados
        """
    )
    
    parser.add_argument('--input', '-i', type=str, help='Archivo GLB/FBX de entrada')
    parser.add_argument('--output', '-o', type=str, help='Archivo de salida (opcional)')
    parser.add_argument('--directorio', '-d', type=str, help='Procesar todos los archivos en este directorio')
    parser.add_argument('--separacion', '-s', type=float, default=30, 
                       help='Grados de separación lateral de brazos (default: 30)')
    parser.add_argument('--elevacion', '-e', type=float, default=20,
                       help='Grados de elevación frontal de brazos (default: 20)')
    
    # Parsear argumentos (ignorar los de Blender)
    args_list = sys.argv
    if '--' in args_list:
        args_list = args_list[args_list.index('--') + 1:]
    else:
        args_list = []
    
    args = parser.parse_args(args_list)
    
    # Validar que se proporcionó input o directorio
    if not args.input and not args.directorio:
        parser.print_help()
        print("\n❌ Error: Debes especificar --input o --directorio")
        return
    
    # Procesar
    if args.directorio:
        procesar_directorio(args.directorio, args.output, args.separacion, args.elevacion)
    else:
        procesar_archivo(args.input, args.output, args.separacion, args.elevacion)

if __name__ == "__main__":
    main()
