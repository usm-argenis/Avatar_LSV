"""
Emoción: SORPRESA (Pregunta/Asombro)
Ejecutar en Blender después de setup_facial_emotions_arkit.py

EFECTO:
- Cejas arriba
- Ojos bien abiertos
- Expresión de "¿Qué?" o "¡Wow!"

USO:
1. Importar GLB en Blender
2. Ejecutar setup_facial_emotions_arkit.py primero
3. Ejecutar este script
4. ¡Listo! El personaje queda con expresión de sorpresa
"""

import bpy


def aplicar_sorpresa(intensidad=1.0):
    """
    Aplica expresión de sorpresa
    
    Args:
        intensidad: 0.0 (neutral) a 1.0 (máxima sorpresa)
    """
    # Buscar armature
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
    
    if not armatures:
        print("❌ No se encontró Armature")
        return False
    
    armature = armatures[0]
    
    # Verificar que existe el control
    if 'EMOTION_SORPRESA' not in armature.keys():
        print("❌ Control EMOTION_SORPRESA no existe")
        print("   Ejecuta primero: setup_facial_emotions_arkit.py")
        return False
    
    # Resetear todas las emociones
    for emotion in ['EMOTION_SORPRESA', 'EMOTION_IRA', 'EMOTION_ALEGRIA', 
                    'EMOTION_ASCO', 'EMOTION_TRISTEZA', 'BLINK_CONTROL']:
        if emotion in armature.keys():
            armature[emotion] = 0.0
    
    # Aplicar sorpresa
    armature['EMOTION_SORPRESA'] = intensidad
    
    print(f"✅ Expresión aplicada: 😮 SORPRESA (intensidad: {intensidad})")
    print(f"   Armature: {armature.name}")
    return True


# Ejecutar con intensidad máxima
if __name__ == "__main__":
    print("\n" + "="*50)
    print("😮 APLICANDO EXPRESIÓN: SORPRESA")
    print("="*50)
    
    # Cambiar este valor para ajustar intensidad (0.0 a 1.0)
    INTENSIDAD = 1.0
    
    resultado = aplicar_sorpresa(INTENSIDAD)
    
    if resultado:
        print("\n🎉 ¡EXPRESIÓN APLICADA CON ÉXITO!")
        print("   Cejas arriba y ojos bien abiertos en viewport")
    else:
        print("\n⚠️  Ejecuta primero setup_facial_emotions_arkit.py")
    
    print("\n💡 Para cambiar intensidad, edita la variable INTENSIDAD")
    print("   Valores recomendados:")
    print("   - 0.3 = Sorpresa leve")
    print("   - 0.6 = Sorpresa moderada")
    print("   - 1.0 = Sorpresa máxima")
    print("="*50 + "\n")
