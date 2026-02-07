"""
Emoción: ALEGRÍA (Sonrisa/Risa)
Ejecutar en Blender después de setup_facial_emotions_arkit.py

EFECTO:
- Sonrisa amplia
- Mejillas elevadas
- Expresión feliz y positiva

USO:
1. Importar GLB en Blender
2. Ejecutar setup_facial_emotions_arkit.py primero
3. Ejecutar este script
4. ¡Listo! El personaje queda con expresión alegre
"""

import bpy


def aplicar_alegria(intensidad=1.0):
    """
    Aplica expresión de alegría/felicidad
    
    Args:
        intensidad: 0.0 (neutral) a 1.0 (máxima alegría)
    """
    # Buscar armature
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
    
    if not armatures:
        print("❌ No se encontró Armature")
        return False
    
    armature = armatures[0]
    
    # Verificar que existe el control
    if 'EMOTION_ALEGRIA' not in armature.keys():
        print("❌ Control EMOTION_ALEGRIA no existe")
        print("   Ejecuta primero: setup_facial_emotions_arkit.py")
        return False
    
    # Resetear todas las emociones
    for emotion in ['EMOTION_SORPRESA', 'EMOTION_IRA', 'EMOTION_ALEGRIA', 
                    'EMOTION_ASCO', 'EMOTION_TRISTEZA', 'BLINK_CONTROL']:
        if emotion in armature.keys():
            armature[emotion] = 0.0
    
    # Aplicar alegría
    armature['EMOTION_ALEGRIA'] = intensidad
    
    print(f"✅ Expresión aplicada: 😊 ALEGRÍA (intensidad: {intensidad})")
    print(f"   Armature: {armature.name}")
    return True


# Ejecutar con intensidad máxima
if __name__ == "__main__":
    print("\n" + "="*50)
    print("😊 APLICANDO EXPRESIÓN: ALEGRÍA/FELICIDAD")
    print("="*50)
    
    # Cambiar este valor para ajustar intensidad (0.0 a 1.0)
    INTENSIDAD = 0.9  # 0.9 para sonrisa natural
    
    resultado = aplicar_alegria(INTENSIDAD)
    
    if resultado:
        print("\n🎉 ¡EXPRESIÓN APLICADA CON ÉXITO!")
        print("   Puedes ver la sonrisa en el viewport de Blender")
    else:
        print("\n⚠️  Ejecuta primero setup_facial_emotions_arkit.py")
    
    print("\n💡 Para cambiar intensidad, edita la variable INTENSIDAD")
    print("   Valores recomendados:")
    print("   - 0.3 = Sonrisa leve")
    print("   - 0.6 = Sonrisa moderada")
    print("   - 0.9 = Sonrisa amplia")
    print("   - 1.0 = Risa/alegría máxima")
    print("="*50 + "\n")
