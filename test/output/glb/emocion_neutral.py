"""
RESETEAR - Volver a expresión neutral
Ejecutar en Blender después de setup_facial_emotions_arkit.py

EFECTO:
- Pone todas las emociones en 0.0
- Vuelve el personaje a expresión neutral/normal

USO:
1. Importar GLB en Blender
2. Ejecutar setup_facial_emotions_arkit.py primero
3. Ejecutar este script cuando quieras volver a neutral
4. ¡Listo! Expresión neutral
"""

import bpy


def resetear_emociones():
    """
    Resetea todas las emociones a 0.0 (neutral)
    """
    # Buscar armature
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
    
    if not armatures:
        print("❌ No se encontró Armature")
        return False
    
    armature = armatures[0]
    
    # Resetear todas las emociones
    emociones_reseteadas = 0
    for emotion in ['EMOTION_SORPRESA', 'EMOTION_IRA', 'EMOTION_ALEGRIA', 
                    'EMOTION_ASCO', 'EMOTION_TRISTEZA', 'BLINK_CONTROL']:
        if emotion in armature.keys():
            armature[emotion] = 0.0
            emociones_reseteadas += 1
    
    print(f"✅ Expresión aplicada: 😐 NEUTRAL")
    print(f"   {emociones_reseteadas} controles reseteados a 0.0")
    print(f"   Armature: {armature.name}")
    return True


# Ejecutar
if __name__ == "__main__":
    print("\n" + "="*50)
    print("😐 RESETEANDO A EXPRESIÓN NEUTRAL")
    print("="*50)
    
    resultado = resetear_emociones()
    
    if resultado:
        print("\n🎉 ¡RESETEO COMPLETADO!")
        print("   Expresión neutral restaurada en viewport")
    else:
        print("\n⚠️  No se encontró armature en la escena")
    
    print("\n💡 Todos los controles de emociones ahora en 0.0")
    print("   El personaje tiene expresión neutral")
    print("="*50 + "\n")
