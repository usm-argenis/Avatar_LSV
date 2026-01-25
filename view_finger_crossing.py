import bpy
import math
from mathutils import Quaternion, Euler

"""
Script INTERACTIVO para ajustar el cruce de dedos
Carga el GLB y permite ver el resultado en frame 34
"""

INPUT_GLB = r"C:\Users\andre\Downloads\r_default.glb"

def main():
    try:
        # Limpiar escena
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        
        # Importar GLB
        print("Importando GLB...")
        bpy.ops.import_scene.gltf(filepath=INPUT_GLB)
        
        # Encontrar armadura
        armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                armature = obj
                break
        
        if not armature:
            print("ERROR: No se encontró armadura")
            return
        
        # Seleccionar y entrar en Pose Mode
        bpy.context.view_layer.objects.active = armature
        bpy.ops.object.mode_set(mode='POSE')
        
        # Ir al frame 34
        scene = bpy.context.scene
        scene.frame_set(34)
        
        print("\n" + "="*80)
        print("CONFIGURANDO CRUCE DE DEDOS - FRAME 34")
        print("="*80)
        
        # Obtener huesos
        index_bones = [
            armature.pose.bones['RightHandIndex1'],
            armature.pose.bones['RightHandIndex2'],
            armature.pose.bones['RightHandIndex3']
        ]
        
        middle_bones = [
            armature.pose.bones['RightHandMiddle1'],
            armature.pose.bones['RightHandMiddle2'],
            armature.pose.bones['RightHandMiddle3']
        ]
        
        # CONFIGURACIÓN MEJORADA
        # X = flexión hacia palma (positivo = doblar)
        # Y = movimiento lateral (índice +, medio -)
        # Z = rotación para cruzar
        
        print("\n🔧 Aplicando rotaciones mejoradas...")
        print("\nÍNDICE (dobla fuerte + va derecha + rota para cruzar por delante):")
        
        # Índice base - comienza el movimiento
        euler1 = Euler((math.radians(30), math.radians(20), math.radians(-35)), 'XYZ')
        index_bones[0].rotation_mode = 'QUATERNION'
        index_bones[0].rotation_quaternion = euler1.to_quaternion()
        q1 = index_bones[0].rotation_quaternion
        print(f"  Index1: ({q1.w:.3f}, {q1.x:.3f}, {q1.y:.3f}, {q1.z:.3f})")
        
        # Índice medio - dobla más y cruza
        euler2 = Euler((math.radians(55), math.radians(40), math.radians(-25)), 'XYZ')
        index_bones[1].rotation_mode = 'QUATERNION'
        index_bones[1].rotation_quaternion = euler2.to_quaternion()
        q2 = index_bones[1].rotation_quaternion
        print(f"  Index2: ({q2.w:.3f}, {q2.x:.3f}, {q2.y:.3f}, {q2.z:.3f})")
        
        # Índice punta - completamente doblado y cruzado
        euler3 = Euler((math.radians(75), math.radians(55), math.radians(-20)), 'XYZ')
        index_bones[2].rotation_mode = 'QUATERNION'
        index_bones[2].rotation_quaternion = euler3.to_quaternion()
        q3 = index_bones[2].rotation_quaternion
        print(f"  Index3: ({q3.w:.3f}, {q3.x:.3f}, {q3.y:.3f}, {q3.z:.3f})")
        
        print("\nMEDIO (dobla fuerte + va izquierda + rota para quedar detrás):")
        
        # Medio base
        euler4 = Euler((math.radians(30), math.radians(-20), math.radians(35)), 'XYZ')
        middle_bones[0].rotation_mode = 'QUATERNION'
        middle_bones[0].rotation_quaternion = euler4.to_quaternion()
        q4 = middle_bones[0].rotation_quaternion
        print(f"  Middle1: ({q4.w:.3f}, {q4.x:.3f}, {q4.y:.3f}, {q4.z:.3f})")
        
        # Medio medio
        euler5 = Euler((math.radians(55), math.radians(-40), math.radians(25)), 'XYZ')
        middle_bones[1].rotation_mode = 'QUATERNION'
        middle_bones[1].rotation_quaternion = euler5.to_quaternion()
        q5 = middle_bones[1].rotation_quaternion
        print(f"  Middle2: ({q5.w:.3f}, {q5.x:.3f}, {q5.y:.3f}, {q5.z:.3f})")
        
        # Medio punta
        euler6 = Euler((math.radians(75), math.radians(-55), math.radians(20)), 'XYZ')
        middle_bones[2].rotation_mode = 'QUATERNION'
        middle_bones[2].rotation_quaternion = euler6.to_quaternion()
        q6 = middle_bones[2].rotation_quaternion
        print(f"  Middle3: ({q6.w:.3f}, {q6.x:.3f}, {q6.y:.3f}, {q6.z:.3f})")
        
        print("\n" + "="*80)
        print("✅ ROTACIONES APLICADAS")
        print("="*80)
        print("\n📍 El modelo está en frame 34 en Pose Mode")
        print("🔍 Verifica visualmente si los dedos se cruzan correctamente")
        print("💡 Si no está correcto, ajusta los valores en el script")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
