"""
PRUEBA SIMPLE - Ver si los controles funcionan
Ejecutar en Blender

Este script hace cambios VISIBLES para verificar que todo funciona
"""

import bpy


def prueba_simple():
    """Prueba rápida y visual"""
    
    print("\n" + "="*60)
    print("🧪 PRUEBA SIMPLE DEL SISTEMA")
    print("="*60)
    
    # Buscar armature
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
    
    if not armatures:
        print("\n❌ NO HAY ARMATURE")
        print("→ Importa un modelo GLB primero")
        return
    
    armature = armatures[0]
    print(f"\n✅ Armature: {armature.name}")
    
    # Verificar controles
    controles = ['EMOTION_SORPRESA', 'EMOTION_IRA', 'EMOTION_ALEGRIA', 
                 'EMOTION_ASCO', 'EMOTION_TRISTEZA', 'BLINK_CONTROL']
    
    print("\n📋 Controles disponibles:")
    controles_ok = []
    for control in controles:
        if control in armature.keys():
            print(f"   ✅ {control}")
            controles_ok.append(control)
        else:
            print(f"   ❌ {control} - NO EXISTE")
    
    if not controles_ok:
        print("\n❌ NO HAY CONTROLES")
        print("→ Ejecuta primero: setup_facial_emotions_arkit.py")
        return
    
    # Buscar mesh con shape keys
    mesh = None
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.shape_keys:
            mesh = obj
            break
    
    if not mesh:
        print("\n❌ NO HAY MESH CON SHAPE KEYS")
        return
    
    print(f"\n✅ Mesh: {mesh.name}")
    print(f"   Shape Keys: {len(mesh.data.shape_keys.key_blocks)}")
    
    # RESETEAR TODO
    print("\n🔄 Reseteando todos los controles a 0.0...")
    for control in controles_ok:
        armature[control] = 0.0
    
    bpy.context.view_layer.update()
    
    # PRUEBA 1: SORPRESA
    if 'EMOTION_SORPRESA' in controles_ok:
        print("\n😮 PRUEBA 1: SORPRESA")
        print("   Cambiando a 1.0...")
        armature['EMOTION_SORPRESA'] = 1.0
        bpy.context.view_layer.update()
        
        # Verificar cambios
        shape_keys = mesh.data.shape_keys.key_blocks
        for bs in ['BrowInnerUp', 'BrowOuterUpLeft', 'EyeWideLeft']:
            if bs in shape_keys:
                valor = shape_keys[bs].value
                print(f"      {bs}: {valor:.3f}", 
                      "✅ CAMBIÓ" if valor > 0.01 else "❌ NO CAMBIÓ")
        
        input("   Presiona ENTER para continuar...")
        armature['EMOTION_SORPRESA'] = 0.0
        bpy.context.view_layer.update()
    
    # PRUEBA 2: ALEGRÍA
    if 'EMOTION_ALEGRIA' in controles_ok:
        print("\n😄 PRUEBA 2: ALEGRÍA")
        print("   Cambiando a 1.0...")
        armature['EMOTION_ALEGRIA'] = 1.0
        bpy.context.view_layer.update()
        
        shape_keys = mesh.data.shape_keys.key_blocks
        for bs in ['MouthSmileLeft', 'MouthSmileRight']:
            if bs in shape_keys:
                valor = shape_keys[bs].value
                print(f"      {bs}: {valor:.3f}", 
                      "✅ CAMBIÓ" if valor > 0.01 else "❌ NO CAMBIÓ")
        
        input("   Presiona ENTER para continuar...")
        armature['EMOTION_ALEGRIA'] = 0.0
        bpy.context.view_layer.update()
    
    # PRUEBA 3: PARPADEO
    if 'BLINK_CONTROL' in controles_ok:
        print("\n😑 PRUEBA 3: PARPADEO")
        print("   Cambiando a 1.0...")
        armature['BLINK_CONTROL'] = 1.0
        bpy.context.view_layer.update()
        
        shape_keys = mesh.data.shape_keys.key_blocks
        for bs in ['EyeBlinkLeft', 'EyeBlinkRight']:
            if bs in shape_keys:
                valor = shape_keys[bs].value
                print(f"      {bs}: {valor:.3f}", 
                      "✅ CAMBIÓ" if valor > 0.01 else "❌ NO CAMBIÓ")
        
        input("   Presiona ENTER para resetear...")
        armature['BLINK_CONTROL'] = 0.0
        bpy.context.view_layer.update()
    
    print("\n✅ PRUEBA COMPLETADA")
    print("="*60 + "\n")


if __name__ == "__main__":
    prueba_simple()
