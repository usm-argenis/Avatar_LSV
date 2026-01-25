import bpy
import math
from mathutils import Quaternion, Euler

"""
Script de PRUEBA para encontrar los valores correctos de rotación
que hagan que el índice y medio se crucen correctamente
"""

INPUT_GLB = r"C:\Users\andre\Downloads\r_default.glb"
OUTPUT_GLB = r"C:\Users\andre\Downloads\r_default_test.glb"
TEST_FRAME = 34

def setup_scene():
    """Limpia e importa el GLB"""
    print("Limpiando e importando GLB...")
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    bpy.ops.import_scene.gltf(filepath=INPUT_GLB)
    
    armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    return armature

def main():
    try:
        armature = setup_scene()
        scene = bpy.context.scene
        scene.frame_set(TEST_FRAME)
        
        print("\n" + "="*80)
        print("PROBANDO CONFIGURACIÓN DE SEÑA DE CRUCE")
        print("="*80)
        
        # Obtener los huesos
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
        
        # ÍNDICE: Doblar hacia palma + mover hacia la derecha (hacia el medio)
        # Rotaciones en grados (X, Y, Z) -> convertir a Euler -> Quaternion
        
        print("\n📝 Aplicando rotaciones al ÍNDICE (dobla y va a la derecha)...")
        
        # Base del índice
        euler1 = Euler((math.radians(20), math.radians(15), math.radians(-25)), 'XYZ')
        index_bones[0].rotation_mode = 'QUATERNION'
        index_bones[0].rotation_quaternion = euler1.to_quaternion()
        index_bones[0].keyframe_insert(data_path="rotation_quaternion", frame=TEST_FRAME)
        print(f"   Index1: X=20°, Y=15°, Z=-25° -> Quat {index_bones[0].rotation_quaternion}")
        
        # Medio del índice
        euler2 = Euler((math.radians(35), math.radians(30), math.radians(-15)), 'XYZ')
        index_bones[1].rotation_mode = 'QUATERNION'
        index_bones[1].rotation_quaternion = euler2.to_quaternion()
        index_bones[1].keyframe_insert(data_path="rotation_quaternion", frame=TEST_FRAME)
        print(f"   Index2: X=35°, Y=30°, Z=-15° -> Quat {index_bones[1].rotation_quaternion}")
        
        # Punta del índice
        euler3 = Euler((math.radians(50), math.radians(45), math.radians(-10)), 'XYZ')
        index_bones[2].rotation_mode = 'QUATERNION'
        index_bones[2].rotation_quaternion = euler3.to_quaternion()
        index_bones[2].keyframe_insert(data_path="rotation_quaternion", frame=TEST_FRAME)
        print(f"   Index3: X=50°, Y=45°, Z=-10° -> Quat {index_bones[2].rotation_quaternion}")
        
        print("\n📝 Aplicando rotaciones al MEDIO (dobla y va a la izquierda)...")
        
        # Base del medio
        euler4 = Euler((math.radians(20), math.radians(-15), math.radians(25)), 'XYZ')
        middle_bones[0].rotation_mode = 'QUATERNION'
        middle_bones[0].rotation_quaternion = euler4.to_quaternion()
        middle_bones[0].keyframe_insert(data_path="rotation_quaternion", frame=TEST_FRAME)
        print(f"   Middle1: X=20°, Y=-15°, Z=25° -> Quat {middle_bones[0].rotation_quaternion}")
        
        # Medio del medio
        euler5 = Euler((math.radians(35), math.radians(-30), math.radians(15)), 'XYZ')
        middle_bones[1].rotation_mode = 'QUATERNION'
        middle_bones[1].rotation_quaternion = euler5.to_quaternion()
        middle_bones[1].keyframe_insert(data_path="rotation_quaternion", frame=TEST_FRAME)
        print(f"   Middle2: X=35°, Y=-30°, Z=15° -> Quat {middle_bones[1].rotation_quaternion}")
        
        # Punta del medio
        euler6 = Euler((math.radians(50), math.radians(-45), math.radians(10)), 'XYZ')
        middle_bones[2].rotation_mode = 'QUATERNION'
        middle_bones[2].rotation_quaternion = euler6.to_quaternion()
        middle_bones[2].keyframe_insert(data_path="rotation_quaternion", frame=TEST_FRAME)
        print(f"   Middle3: X=50°, Y=-45°, Z=10° -> Quat {middle_bones[2].rotation_quaternion}")
        
        # Exportar para verificar visualmente
        print("\n💾 Exportando resultado de prueba...")
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.export_scene.gltf(filepath=OUTPUT_GLB, export_format='GLB')
        
        print("\n" + "="*80)
        print("✅ PRUEBA COMPLETADA")
        print("="*80)
        print(f"📁 Archivo de prueba: {OUTPUT_GLB}")
        print(f"📍 Frame de prueba: {TEST_FRAME}")
        print("\n🔍 Abre el archivo en Blender y verifica:")
        print("   1. Los dedos se doblan hacia la palma")
        print("   2. El índice va hacia la derecha (hacia el medio)")
        print("   3. El medio va hacia la izquierda (hacia el índice)")
        print("   4. Se cruzan formando la seña")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
