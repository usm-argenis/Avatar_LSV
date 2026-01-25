"""
Emoción: ASCO (Desaprobación)
Ejecutar en Blender después de setup_facial_emotions_arkit.py

EFECTO:
- Nariz arrugada
- Labio superior levantado
- Expresión de disgusto o desaprobación

USO:
1. Importar GLB en Blender
2. Ejecutar setup_facial_emotions_arkit.py primero
3. Ejecutar este script
4. ¡Listo! El personaje queda con expresión de asco
"""

import bpy


def aplicar_asco(intensidad=1.0):
    """
    Aplica expresión de asco/desaprobación
    
    Args:
        intensidad: 0.0 (neutral) a 1.0 (máximo asco)
    """
    # Buscar armature
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
    
    if not armatures:
        print("❌ No se encontró Armature")
        return False
    
    armature = armatures[0]
    
    # Verificar que existe el control
    if 'EMOTION_ASCO' not in armature.keys():
        print("❌ Control EMOTION_ASCO no existe")
        print("   Ejecuta primero: setup_facial_emotions_arkit.py")
        return False
    
    # Resetear todas las emociones
    for emotion in ['EMOTION_SORPRESA', 'EMOTION_IRA', 'EMOTION_ALEGRIA', 
                    'EMOTION_ASCO', 'EMOTION_TRISTEZA', 'BLINK_CONTROL']:
        if emotion in armature.keys():
            armature[emotion] = 0.0
    
    # Aplicar asco
    armature['EMOTION_ASCO'] = intensidad
    
    print(f"✅ Expresión aplicada: 🤢 ASCO (intensidad: {intensidad})")
    print(f"   Armature: {armature.name}")
    return True


# Ejecutar con intensidad máxima
if __name__ == "__main__":
    print("\n" + "="*50)
    print("🤢 APLICANDO EXPRESIÓN: ASCO/DESAPROBACIÓN")
    print("="*50)
    
    # Cambiar este valor para ajustar intensidad (0.0 a 1.0)
    INTENSIDAD = 0.8
    
    resultado = aplicar_asco(INTENSIDAD)
    
    if resultado:
        print("\n🎉 ¡EXPRESIÓN APLICADA CON ÉXITO!")
        print("   Nariz arrugada y labio superior levantado en viewport")
    else:
        print("\n⚠️  Ejecuta primero setup_facial_emotions_arkit.py")
    
    print("\n💡 Para cambiar intensidad, edita la variable INTENSIDAD")
    print("   Valores recomendados:")
    print("   - 0.3 = Disgusto leve")
    print("   - 0.6 = Desaprobación")
    print("   - 0.8 = Asco moderado")
    print("   - 1.0 = Asco máximo")
    print("="*50 + "\n")
