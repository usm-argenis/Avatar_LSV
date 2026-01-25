"""
Control: PARPADEO
Ejecutar en Blender después de setup_facial_emotions_arkit.py

EFECTO:
- Cierra los ojos
- Útil para parpadeos o expresión de ojos cerrados

USO:
1. Importar GLB en Blender
2. Ejecutar setup_facial_emotions_arkit.py primero
3. Ejecutar este script
4. ¡Listo! El personaje cierra los ojos
"""

import bpy


def aplicar_parpadeo(intensidad=1.0):
    """
    Aplica parpadeo (cierre de ojos)
    
    Args:
        intensidad: 0.0 (ojos abiertos) a 1.0 (ojos cerrados)
    """
    # Buscar armature
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
    
    if not armatures:
        print("❌ No se encontró Armature")
        return False
    
    armature = armatures[0]
    
    # Verificar que existe el control
    if 'BLINK_CONTROL' not in armature.keys():
        print("❌ Control BLINK_CONTROL no existe")
        print("   Ejecuta primero: setup_facial_emotions_arkit.py")
        return False
    
    # Resetear todas las emociones
    for emotion in ['EMOTION_SORPRESA', 'EMOTION_IRA', 'EMOTION_ALEGRIA', 
                    'EMOTION_ASCO', 'EMOTION_TRISTEZA', 'BLINK_CONTROL']:
        if emotion in armature.keys():
            armature[emotion] = 0.0
    
    # Aplicar parpadeo
    armature['BLINK_CONTROL'] = intensidad
    
    print(f"✅ Expresión aplicada: 😑 PARPADEO (intensidad: {intensidad})")
    print(f"   Armature: {armature.name}")
    return True


# Ejecutar con intensidad máxima
if __name__ == "__main__":
    print("\n" + "="*50)
    print("😑 APLICANDO: PARPADEO (OJOS CERRADOS)")
    print("="*50)
    
    # Cambiar este valor para ajustar intensidad (0.0 a 1.0)
    INTENSIDAD = 1.0  # 1.0 para cerrar completamente
    
    resultado = aplicar_parpadeo(INTENSIDAD)
    
    if resultado:
        print("\n🎉 ¡PARPADEO APLICADO CON ÉXITO!")
        print("   Ojos cerrados visibles en viewport")
    else:
        print("\n⚠️  Ejecuta primero setup_facial_emotions_arkit.py")
    
    print("\n💡 Para cambiar intensidad, edita la variable INTENSIDAD")
    print("   Valores recomendados:")
    print("   - 0.0 = Ojos completamente abiertos")
    print("   - 0.5 = Ojos medio cerrados (somnoliento)")
    print("   - 1.0 = Ojos completamente cerrados")
    print("="*50 + "\n")
