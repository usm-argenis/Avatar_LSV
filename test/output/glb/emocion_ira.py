"""
Emoción: IRA (Enojo/Tensión)
Ejecutar en Blender después de setup_facial_emotions_arkit.py

EFECTO:
- Cejas fruncidas hacia abajo
- Boca apretada/fruncida
- Expresión de enojo o tensión

USO:
1. Importar GLB en Blender
2. Ejecutar setup_facial_emotions_arkit.py primero
3. Ejecutar este script
4. ¡Listo! El personaje queda con expresión de ira
"""

import bpy


def aplicar_ira(intensidad=1.0):
    """
    Aplica expresión de ira/enojo
    
    Args:
        intensidad: 0.0 (neutral) a 1.0 (máximo enojo)
    """
    # Buscar armature
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
    
    if not armatures:
        print("❌ No se encontró Armature")
        return False
    
    armature = armatures[0]
    
    # Verificar que existe el control
    if 'EMOTION_IRA' not in armature.keys():
        print("❌ Control EMOTION_IRA no existe")
        print("   Ejecuta primero: setup_facial_emotions_arkit.py")
        return False
    
    # Resetear todas las emociones
    for emotion in ['EMOTION_SORPRESA', 'EMOTION_IRA', 'EMOTION_ALEGRIA', 
                    'EMOTION_ASCO', 'EMOTION_TRISTEZA', 'BLINK_CONTROL']:
        if emotion in armature.keys():
            armature[emotion] = 0.0
    
    # Aplicar ira
    armature['EMOTION_IRA'] = intensidad
    
    print(f"✅ Expresión aplicada: 😠 IRA (intensidad: {intensidad})")
    print(f"   Armature: {armature.name}")
    return True


# Ejecutar con intensidad máxima
if __name__ == "__main__":
    print("\n" + "="*50)
    print("😠 APLICANDO EXPRESIÓN: IRA/ENOJO")
    print("="*50)
    
    # Cambiar este valor para ajustar intensidad (0.0 a 1.0)
    INTENSIDAD = 0.8  # 0.8 para enojo contenido, más natural
    
    resultado = aplicar_ira(INTENSIDAD)
    
    if resultado:
        print("\n🎉 ¡EXPRESIÓN APLICADA CON ÉXITO!")
        print("   Cejas fruncidas y boca tensa visible en viewport")
    else:
        print("\n⚠️  Ejecuta primero setup_facial_emotions_arkit.py")
    
    print("\n💡 Para cambiar intensidad, edita la variable INTENSIDAD")
    print("   Valores recomendados:")
    print("   - 0.3 = Molestia leve")
    print("   - 0.6 = Enojo moderado")
    print("   - 0.8 = Enojo fuerte")
    print("   - 1.0 = Ira máxima")
    print("="*50 + "\n")
