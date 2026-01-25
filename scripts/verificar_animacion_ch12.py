"""
Script para verificar que Ch12_con_animacion_b_FINAL.fbx tiene la animación
"""
import bpy
from pathlib import Path

def verificar_animacion():
    print("=" * 80)
    print("🔍 VERIFICACIÓN DE ANIMACIÓN EN CH12")
    print("=" * 80)
    
    # Limpiar escena
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    # Cargar archivo GLB (mejor para animaciones)
    archivo = Path("C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/cc/Ch12_con_animacion_b_FINAL.glb")
    
    print(f"\n📥 Cargando: {archivo.name}")
    bpy.ops.import_scene.gltf(filepath=str(archivo))
    
    # Buscar armature
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        print("❌ ERROR: No se encontró armature")
        return False
    
    print(f"✅ Armature encontrado: {armature.name}")
    print(f"   Huesos: {len(armature.data.bones)}")
    
    # Verificar naming de huesos
    print("\n🔍 Verificando naming de huesos:")
    muestra_huesos = list(armature.data.bones)[:5]
    for bone in muestra_huesos:
        print(f"   - {bone.name}")
    
    # Verificar animación
    if not armature.animation_data:
        print("\n❌ ERROR: No tiene animation_data")
        return False
    
    if not armature.animation_data.action:
        print("❌ ERROR: No tiene action")
        return False
    
    action = armature.animation_data.action
    print(f"\n✅ Action encontrado: {action.name}")
    
    # Analizar action
    frame_start = int(action.frame_range[0])
    frame_end = int(action.frame_range[1])
    num_frames = frame_end - frame_start + 1
    
    print(f"   Frame inicial: {frame_start}")
    print(f"   Frame final: {frame_end}")
    print(f"   Total frames: {num_frames}")
    print(f"   FCurves: {len(action.fcurves)}")
    
    if len(action.fcurves) == 0:
        print("\n❌ ERROR: El action no tiene FCurves (sin animación)")
        return False
    
    # Analizar qué huesos están animados
    huesos_animados = set()
    for fcurve in action.fcurves:
        data_path = fcurve.data_path
        if 'pose.bones[' in data_path:
            # Extraer nombre del hueso
            start = data_path.find('["') + 2
            end = data_path.find('"]', start)
            if start > 1 and end > start:
                nombre_hueso = data_path[start:end]
                huesos_animados.add(nombre_hueso)
    
    print(f"\n📊 Huesos animados: {len(huesos_animados)}")
    print("   Muestra de huesos animados:")
    for hueso in list(huesos_animados)[:10]:
        print(f"   - {hueso}")
    
    # Verificar movimiento real
    print(f"\n🎬 Verificando movimiento real...")
    
    bpy.context.scene.frame_set(frame_start)
    bpy.context.view_layer.objects.active = armature
    
    # Obtener posición inicial de un hueso de prueba
    hueso_prueba = "mixamorig:LeftHand"
    if hueso_prueba not in armature.pose.bones:
        print(f"⚠️ Hueso de prueba {hueso_prueba} no encontrado, usando primer hueso animado")
        hueso_prueba = list(huesos_animados)[0]
    
    pose_bone = armature.pose.bones[hueso_prueba]
    pos_inicial = pose_bone.location.copy()
    rot_inicial = pose_bone.rotation_quaternion.copy() if pose_bone.rotation_mode == 'QUATERNION' else pose_bone.rotation_euler.copy()
    
    # Avanzar a mitad de animación
    frame_medio = (frame_start + frame_end) // 2
    bpy.context.scene.frame_set(frame_medio)
    
    pos_medio = pose_bone.location.copy()
    rot_medio = pose_bone.rotation_quaternion.copy() if pose_bone.rotation_mode == 'QUATERNION' else pose_bone.rotation_euler.copy()
    
    # Calcular diferencia
    diff_pos = (pos_medio - pos_inicial).length
    diff_rot = sum(abs(a - b) for a, b in zip(rot_inicial, rot_medio))
    
    print(f"   Hueso analizado: {hueso_prueba}")
    print(f"   Diferencia posición: {diff_pos:.4f}")
    print(f"   Diferencia rotación: {diff_rot:.4f}")
    
    if diff_pos > 0.001 or diff_rot > 0.001:
        print("\n✅ ¡ANIMACIÓN CONFIRMADA! El hueso se mueve correctamente")
        return True
    else:
        print("\n⚠️ ADVERTENCIA: Movimiento mínimo detectado")
        return False

if __name__ == "__main__":
    resultado = verificar_animacion()
    
    print("\n" + "=" * 80)
    if resultado:
        print("✅ VERIFICACIÓN EXITOSA - ANIMACIÓN FUNCIONAL")
    else:
        print("❌ VERIFICACIÓN FALLIDA - REVISAR ANIMACIÓN")
    print("=" * 80)
