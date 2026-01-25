"""
Emoción: TRISTEZA (Pena/Preocupación)
Ejecutar en Blender después de setup_facial_emotions_arkit.py

EFECTO:
- Comisuras de la boca hacia abajo
- Labio inferior caído
- Expresión triste o preocupada

USO:
1. Importar GLB en Blender
2. Ejecutar setup_facial_emotions_arkit.py primero
3. Ejecutar este script
4. ¡Listo! El personaje queda con expresión triste
"""

import bpy


def aplicar_tristeza(intensidad=1.0):
    """
    Aplica expresión de tristeza/pena
    
    Args:
        intensidad: 0.0 (neutral) a 1.0 (máxima tristeza)
    """
    # Buscar armature
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
    
    if not armatures:
        print("❌ No se encontró Armature")
        return False
    
    armature = armatures[0]
    
    # Verificar que existe el control
    if 'EMOTION_TRISTEZA' not in armature.keys():
        print("❌ Control EMOTION_TRISTEZA no existe")
        print("   Ejecuta primero: setup_facial_emotions_arkit.py")
        return False
    
    # Resetear todas las emociones
    for emotion in ['EMOTION_SORPRESA', 'EMOTION_IRA', 'EMOTION_ALEGRIA', 
                    'EMOTION_ASCO', 'EMOTION_TRISTEZA', 'BLINK_CONTROL']:
        if emotion in armature.keys():
            armature[emotion] = 0.0
    
    # Aplicar tristeza
    armature['EMOTION_TRISTEZA'] = intensidad
    
    print(f"✅ Expresión aplicada: 😢 TRISTEZA (intensidad: {intensidad})")
    print(f"   Armature: {armature.name}")
    return True


# Ejecutar con intensidad máxima
if __name__ == "__main__":
    print("\n" + "="*50)
    print("😢 APLICANDO EXPRESIÓN: TRISTEZA/PENA")
    print("="*50)
    
    # Cambiar este valor para ajustar intensidad (0.0 a 1.0)
    INTENSIDAD = 0.8
    
    resultado = aplicar_tristeza(INTENSIDAD)
    
    if resultado:
        print("\n🎉 ¡EXPRESIÓN APLICADA CON ÉXITO!")
        print("   Comisuras de boca hacia abajo en viewport")
    else:
        print("\n⚠️  Ejecuta primero setup_facial_emotions_arkit.py")
    
    print("\n💡 Para cambiar intensidad, edita la variable INTENSIDAD")
    print("   Valores recomendados:")
    print("   - 0.3 = Preocupación leve")
    print("   - 0.6 = Tristeza moderada")
    print("   - 0.8 = Tristeza notable")
    print("   - 1.0 = Tristeza profunda")
    print("="*50 + "\n")
