import bpy
import math

"""
Script CONFIGURADOR RÁPIDO
Permite ajustar rápidamente el cierre de dedos sin editar código
Ejecutar en Blender UI (Text Editor)
"""

# ============================================================================
# AJUSTA ESTOS VALORES FÁCILMENTE
# ============================================================================

# ¿Qué tanto quieres cerrar los dedos? (0-100%)
CIERRE_PORCENTAJE = 100  # 100% = puño completamente cerrado

# ¿En qué frames quieres la corrección?
FRAME_INICIAL = 30
FRAME_FINAL = 37

# ¿Qué mano(s) corregir?
CORREGIR_MANO_IZQUIERDA = True
CORREGIR_MANO_DERECHA = True

# ¿Qué dedos corregir?
CORREGIR_INDICE = True
CORREGIR_MEDIO = True

# Nivel de suavizado (1-5, más = más suave)
NIVEL_SUAVIZADO = 2

# ============================================================================
# NO NECESITAS MODIFICAR NADA ABAJO DE ESTA LÍNEA
# ============================================================================

def calcular_rotacion_por_porcentaje(porcentaje):
    """
    Calcula las rotaciones basadas en el porcentaje de cierre deseado
    """
    # Valores máximos para un puño completamente cerrado
    max_base = 80    # Base del dedo
    max_medio = 90   # Medio del dedo
    max_punta = 80   # Punta del dedo
    
    factor = porcentaje / 100.0
    
    return {
        'base': max_base * factor,
        'medio': max_medio * factor,
        'punta': max_punta * factor
    }


def aplicar_cierre_interactivo():
    """
    Aplica el cierre de dedos con los valores configurados arriba
    """
    print("\n" + "="*80)
    print("🎛️ CONFIGURADOR RÁPIDO DE CIERRE DE DEDOS")
    print("="*80)
    
    # Verificar que hay un objeto activo
    armature = bpy.context.active_object
    if not armature or armature.type != 'ARMATURE':
        print("❌ ERROR: Selecciona una armadura en Pose Mode primero")
        return
    
    if bpy.context.mode != 'POSE':
        print("❌ ERROR: Debes estar en Pose Mode")
        print("   Presiona Ctrl+Tab para entrar en Pose Mode")
        return
    
    print(f"\n📊 CONFIGURACIÓN:")
    print(f"   • Cierre: {CIERRE_PORCENTAJE}%")
    print(f"   • Frames: {FRAME_INICIAL} - {FRAME_FINAL}")
    print(f"   • Mano Izquierda: {'✓' if CORREGIR_MANO_IZQUIERDA else '✗'}")
    print(f"   • Mano Derecha: {'✓' if CORREGIR_MANO_DERECHA else '✗'}")
    print(f"   • Índice: {'✓' if CORREGIR_INDICE else '✗'}")
    print(f"   • Medio: {'✓' if CORREGIR_MEDIO else '✗'}")
    print(f"   • Suavizado: Nivel {NIVEL_SUAVIZADO}")
    
    # Calcular rotaciones
    rotaciones = calcular_rotacion_por_porcentaje(CIERRE_PORCENTAJE)
    
    # Construir lista de huesos a modificar
    huesos_modificar = []
    
    if CORREGIR_MANO_IZQUIERDA:
        if CORREGIR_INDICE:
            huesos_modificar.extend([
                ('LeftHandIndex1', -rotaciones['base']),
                ('LeftHandIndex2', -rotaciones['medio']),
                ('LeftHandIndex3', -rotaciones['punta'])
            ])
        if CORREGIR_MEDIO:
            huesos_modificar.extend([
                ('LeftHandMiddle1', -rotaciones['base']),
                ('LeftHandMiddle2', -rotaciones['medio']),
                ('LeftHandMiddle3', -rotaciones['punta'])
            ])
    
    if CORREGIR_MANO_DERECHA:
        if CORREGIR_INDICE:
            huesos_modificar.extend([
                ('RightHandIndex1', rotaciones['base']),
                ('RightHandIndex2', rotaciones['medio']),
                ('RightHandIndex3', rotaciones['punta'])
            ])
        if CORREGIR_MEDIO:
            huesos_modificar.extend([
                ('RightHandMiddle1', rotaciones['base']),
                ('RightHandMiddle2', rotaciones['medio']),
                ('RightHandMiddle3', rotaciones['punta'])
            ])
    
    print(f"\n🦴 Modificando {len(huesos_modificar)} huesos...")
    
    # Convertir a Euler primero
    for bone_name, _ in huesos_modificar:
        if bone_name in armature.pose.bones:
            bone = armature.pose.bones[bone_name]
            if bone.rotation_mode != 'XYZ':
                bone.rotation_mode = 'XYZ'
    
    # Aplicar rotaciones
    scene = bpy.context.scene
    keyframes_count = 0
    
    for frame in range(FRAME_INICIAL, FRAME_FINAL + 1):
        scene.frame_set(frame)
        
        for bone_name, rotacion_z in huesos_modificar:
            if bone_name not in armature.pose.bones:
                continue
            
            bone = armature.pose.bones[bone_name]
            bone.rotation_euler[2] = math.radians(rotacion_z)
            bone.keyframe_insert(data_path="rotation_euler", frame=frame)
            keyframes_count += 1
    
    print(f"✓ {keyframes_count} keyframes insertados")
    
    # Suavizar curvas
    if armature.animation_data and armature.animation_data.action:
        action = armature.animation_data.action
        curves_smoothed = 0
        
        for fcurve in action.fcurves:
            for bone_name, _ in huesos_modificar:
                if f'pose.bones["{bone_name}"]' in fcurve.data_path:
                    if 'rotation_euler' in fcurve.data_path:
                        for _ in range(NIVEL_SUAVIZADO):
                            for kf in fcurve.keyframe_points:
                                if FRAME_INICIAL <= kf.co[0] <= FRAME_FINAL:
                                    kf.interpolation = 'BEZIER'
                                    kf.handle_left_type = 'AUTO_CLAMPED'
                                    kf.handle_right_type = 'AUTO_CLAMPED'
                        curves_smoothed += 1
                        break
        
        print(f"✓ {curves_smoothed} curvas suavizadas")
    
    # Mostrar vista previa en el frame inicial
    scene.frame_set(FRAME_INICIAL)
    
    print("\n" + "="*80)
    print("✅ CORRECCIÓN APLICADA")
    print("="*80)
    print("\n💡 SIGUIENTE PASO:")
    print("   1. Presiona ESPACIO para reproducir la animación")
    print("   2. Verifica que el cierre se vea correcto")
    print("   3. Si quieres más/menos cierre:")
    print("      • Ajusta CIERRE_PORCENTAJE arriba (0-120%)")
    print("      • Ejecuta el script de nuevo (Alt+P)")
    print("\n📁 Para guardar: File > Export > glTF 2.0")
    print("="*80)


# ============================================================================
# EJECUCIÓN
# ============================================================================

if __name__ == "__main__":
    aplicar_cierre_interactivo()
