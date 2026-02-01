import bpy
import json
import sys
from pathlib import Path
from mathutils import Quaternion

def aplicar_manos_quaternions(hand_json_path, glb_input_path, glb_output_path):
    """
    Aplica cuaterniones de manos desde JSON de MediaPipe a un archivo GLB.
    
    Args:
        hand_json_path: Ruta al JSON con cuaterniones de MediaPipe
        glb_input_path: Ruta al GLB de entrada
        glb_output_path: Ruta al GLB de salida modificado
    """
    
    print(f"\n{'='*80}")
    print(f"🖐️  APLICANDO CUATERNIONES DE MANOS A GLB")
    print(f"{'='*80}")
    
    # Cargar JSON de cuaterniones
    print(f"\n📂 Cargando datos de manos...")
    with open(hand_json_path, 'r', encoding='utf-8') as f:
        hand_data = json.load(f)
    
    frames_data = hand_data['frames']
    total_frames = len(frames_data)
    print(f"✅ Cargados {total_frames} frames de datos de manos")
    
    # Verificar archivos
    if not Path(glb_input_path).exists():
        raise FileNotFoundError(f"Archivo GLB no encontrado: {glb_input_path}")
    
    print(f"\n📥 Importando GLB: {Path(glb_input_path).name}")
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Importar GLB
    bpy.ops.import_scene.gltf(filepath=str(glb_input_path))
    
    # Buscar armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        raise ValueError("No se encontró armature en el archivo GLB")
    
    print(f"✅ Armature encontrado: {armature.name}")
    
    # Verificar que tiene animación
    if not armature.animation_data or not armature.animation_data.action:
        raise ValueError("El armature no tiene animación")
    
    action = armature.animation_data.action
    print(f"✅ Animación encontrada: {action.name}")
    print(f"   Duración original: {action.frame_range[0]:.0f} - {action.frame_range[1]:.0f}")
    
    # Mapeo de dedos MediaPipe a huesos de Duvall (RIGHT HAND)
    # MediaPipe: thumb, index, middle, ring, pinky
    # Cada dedo tiene 4 segmentos (0=metacarpo/base, 1=proximal, 2=middle, 3=distal)
    
    finger_mapping = {
        'thumb': {
            0: 'RightHandThumb1',
            1: 'RightHandThumb2',
            2: 'RightHandThumb3',
            3: 'RightHandThumb4'
        },
        'index': {
            0: 'RightHandIndex1',
            1: 'RightHandIndex2',
            2: 'RightHandIndex3',
            3: 'RightHandIndex4'
        },
        'middle': {
            0: 'RightHandMiddle1',
            1: 'RightHandMiddle2',
            2: 'RightHandMiddle3',
            3: 'RightHandMiddle4'
        },
        'ring': {
            0: 'RightHandRing1',
            1: 'RightHandRing2',
            2: 'RightHandRing3',
            3: 'RightHandRing4'
        },
        'pinky': {
            0: 'RightHandPinky1',
            1: 'RightHandPinky2',
            2: 'RightHandPinky3',
            3: 'RightHandPinky4'
        }
    }
    
    print(f"\n🦴 Preparando modificación de huesos de mano...")
    
    # Verificar qué huesos existen
    available_bones = set(armature.pose.bones.keys())
    
    # Recopilar todos los huesos que vamos a modificar
    bones_to_modify = {}
    for finger_name, segments in finger_mapping.items():
        for segment_idx, bone_name in segments.items():
            if bone_name in available_bones:
                bones_to_modify[bone_name] = (finger_name, segment_idx)
            else:
                print(f"⚠️  Hueso no encontrado: {bone_name}")
    
    print(f"✅ Encontrados {len(bones_to_modify)} huesos de mano para modificar")
    
    # Procesar cada frame
    print(f"\n🎬 Aplicando cuaterniones frame por frame...")
    
    frames_modified = 0
    bones_modified_count = 0
    
    for frame_idx, frame_data in enumerate(frames_data):
        frame_number = frame_idx + 1  # Blender frames empiezan en 1
        
        if frame_idx % 10 == 0:
            print(f"   Frame {frame_idx + 1}/{total_frames}...", end='\r')
        
        # Verificar que hay datos de manos
        if 'hands' not in frame_data or len(frame_data['hands']) == 0:
            continue
        
        # Tomar la primera mano detectada (asumiendo mano derecha)
        hand_info = frame_data['hands'][0]
        
        # Procesar cada dedo
        for finger_name in ['thumb', 'index', 'middle', 'ring', 'pinky']:
            finger_data = hand_info['fingers'][finger_name]
            
            # Procesar cada segmento del dedo
            for segment_idx in range(4):
                # Obtener nombre del hueso
                if finger_name not in finger_mapping or segment_idx not in finger_mapping[finger_name]:
                    continue
                
                bone_name = finger_mapping[finger_name][segment_idx]
                
                if bone_name not in bones_to_modify:
                    continue
                
                # Obtener cuaternión desde JSON (formato: [qx, qy, qz, qw])
                quat_data = finger_data[segment_idx]
                
                # MediaPipe usa [qx, qy, qz, qw] pero Blender usa (qw, qx, qy, qz)
                # Además, MediaPipe usa un sistema de coordenadas diferente:
                # MediaPipe: X=derecha, Y=abajo, Z=hacia cámara
                # Blender: X=derecha, Y=adelante, Z=arriba
                # Transformación: intercambiar Y y Z, invertir nuevo Y
                
                mp_quat = Quaternion((
                    quat_data[3],  # w
                    quat_data[0],  # x
                    quat_data[1],  # y  
                    quat_data[2]   # z
                ))
                
                # Transformar coordenadas de MediaPipe a Blender
                # Convertir Y↔Z y negar el nuevo Y
                target_quat = Quaternion((
                    mp_quat.w,
                    mp_quat.x,
                    -mp_quat.z,  # -Z de MediaPipe → Y de Blender
                    mp_quat.y    # Y de MediaPipe → Z de Blender
                ))
                
                # Buscar o crear fcurves para este hueso
                data_path = f'pose.bones["{bone_name}"].rotation_quaternion'
                
                fcurves = [fc for fc in action.fcurves if fc.data_path == data_path]
                
                # Si no existen fcurves, crearlas
                if len(fcurves) == 0:
                    for i in range(4):
                        fc = action.fcurves.new(data_path=data_path, index=i)
                        fcurves.append(fc)
                
                # Ordenar por array_index
                fcurves_sorted = sorted(fcurves, key=lambda fc: fc.array_index)
                
                # Aplicar valores
                target_components = [target_quat.w, target_quat.x, target_quat.y, target_quat.z]
                
                for i, fc in enumerate(fcurves_sorted):
                    # Buscar keyframe existente
                    kf = None
                    for k in fc.keyframe_points:
                        if abs(k.co[0] - frame_number) < 0.01:
                            kf = k
                            break
                    
                    # Actualizar o crear keyframe
                    if kf:
                        kf.co[1] = target_components[i]
                        kf.interpolation = 'LINEAR'
                    else:
                        fc.keyframe_points.insert(frame_number, target_components[i])
                        fc.update()
                
                bones_modified_count += 1
        
        frames_modified += 1
    
    print(f"\n✅ Procesados {frames_modified} frames")
    print(f"✅ Modificados {bones_modified_count} huesos-frame")
    
    # Actualizar rango de frames si es necesario
    if total_frames > action.frame_range[1]:
        action.frame_range = (action.frame_range[0], total_frames)
        print(f"📊 Rango de animación actualizado: {action.frame_range[0]:.0f} - {action.frame_range[1]:.0f}")
    
    # Exportar GLB modificado
    print(f"\n💾 Exportando GLB modificado...")
    print(f"   Destino: {glb_output_path}")
    
    bpy.ops.export_scene.gltf(
        filepath=str(glb_output_path),
        export_format='GLB',
        export_animations=True,
        export_nla_strips=False
    )
    
    output_size = Path(glb_output_path).stat().st_size / (1024 * 1024)
    print(f"✅ Exportación completa: {output_size:.2f} MB")
    
    print(f"\n{'='*80}")
    print(f"✨ PROCESO COMPLETADO EXITOSAMENTE")
    print(f"{'='*80}")
    print(f"📊 Resumen:")
    print(f"   • Frames procesados: {frames_modified}")
    print(f"   • Huesos modificados: {len(bones_to_modify)}")
    print(f"   • Total modificaciones: {bones_modified_count}")
    print(f"   • Archivo salida: {Path(glb_output_path).name}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    # Obtener argumentos de línea de comandos
    argv = sys.argv
    
    # Cuando se ejecuta desde Blender con --python, los args después de -- son accesibles
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        argv = []
    
    if len(argv) < 3:
        print("❌ Error: Se requieren 3 argumentos")
        print("Uso: blender --background --python aplicar_manos_quaternions.py -- <hand_json> <input_glb> <output_glb>")
        sys.exit(1)
    
    hand_json = argv[0]
    input_glb = argv[1]
    output_glb = argv[2]
    
    # Ejecutar
    aplicar_manos_quaternions(hand_json, input_glb, output_glb)
