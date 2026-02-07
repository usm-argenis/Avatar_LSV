"""
DIAGNÓSTICO COMPLETO DEL SISTEMA FACIAL
Ejecutar en Blender para ver qué está pasando

Este script verifica:
1. Si existe Armature
2. Si existen las Custom Properties
3. Si existen los Shape Keys
4. Si existen los Drivers
5. Estado actual de cada control
"""

import bpy


def diagnosticar():
    """Diagnóstico completo del sistema"""
    
    print("\n" + "="*70)
    print("🔍 DIAGNÓSTICO DEL SISTEMA DE EXPRESIONES FACIALES")
    print("="*70)
    
    # 1. BUSCAR ARMATURE
    print("\n📦 1. BUSCANDO ARMATURE...")
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
    
    if not armatures:
        print("   ❌ NO SE ENCONTRÓ ARMATURE")
        print("   → Importa primero un modelo GLB desde DeepMotion")
        return False
    
    armature = armatures[0]
    print(f"   ✅ Armature encontrado: {armature.name}")
    
    # 2. VERIFICAR CUSTOM PROPERTIES
    print("\n🎛️  2. VERIFICANDO CUSTOM PROPERTIES...")
    controles = ['EMOTION_SORPRESA', 'EMOTION_IRA', 'EMOTION_ALEGRIA', 
                 'EMOTION_ASCO', 'EMOTION_TRISTEZA', 'BLINK_CONTROL']
    
    controles_existentes = 0
    for control in controles:
        if control in armature.keys():
            valor = armature[control]
            print(f"   ✅ {control}: {valor}")
            controles_existentes += 1
        else:
            print(f"   ❌ {control}: NO EXISTE")
    
    if controles_existentes == 0:
        print("\n   ⚠️  NO HAY CUSTOM PROPERTIES")
        print("   → Ejecuta primero: setup_facial_emotions_arkit.py")
        return False
    
    print(f"\n   Controles creados: {controles_existentes}/6")
    
    # 3. BUSCAR MESH CON SHAPE KEYS
    print("\n👤 3. BUSCANDO MESH CON SHAPE KEYS...")
    meshes_con_shapes = []
    
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.shape_keys:
            meshes_con_shapes.append(obj)
            print(f"   ✅ Mesh: {obj.name}")
            print(f"      Shape Keys: {len(obj.data.shape_keys.key_blocks)}")
    
    if not meshes_con_shapes:
        print("   ❌ NO SE ENCONTRÓ MESH CON SHAPE KEYS")
        print("   → El modelo GLB no tiene blendshapes")
        return False
    
    # 4. ANALIZAR SHAPE KEYS
    print("\n🎭 4. ANALIZANDO SHAPE KEYS (ARKit)...")
    
    mesh = meshes_con_shapes[0]
    shape_keys = mesh.data.shape_keys.key_blocks
    
    # ARKit blendshapes que debemos tener
    arkit_necesarios = {
        'SORPRESA': ['BrowInnerUp', 'BrowOuterUpLeft', 'BrowOuterUpRight', 
                     'EyeWideLeft', 'EyeWideRight'],
        'IRA': ['BrowDownLeft', 'BrowDownRight', 'MouthFrownLeft', 'MouthFrownRight'],
        'ALEGRIA': ['MouthSmileLeft', 'MouthSmileRight', 'CheekPuff'],
        'ASCO': ['NoseSneerLeft', 'NoseSneerRight', 'MouthUpperUpLeft', 'MouthUpperUpRight'],
        'TRISTEZA': ['MouthDimpleLeft', 'MouthDimpleRight', 'MouthLowerDownLeft', 'MouthLowerDownRight'],
        'BLINK': ['EyeBlinkLeft', 'EyeBlinkRight']
    }
    
    total_encontrados = 0
    total_necesarios = sum(len(v) for v in arkit_necesarios.values())
    
    for emocion, blendshapes in arkit_necesarios.items():
        print(f"\n   {emocion}:")
        for bs in blendshapes:
            if bs in shape_keys:
                valor = shape_keys[bs].value
                print(f"      ✅ {bs}: {valor:.3f}")
                total_encontrados += 1
            else:
                print(f"      ❌ {bs}: NO EXISTE")
    
    print(f"\n   Total ARKit encontrados: {total_encontrados}/{total_necesarios}")
    
    # 5. VERIFICAR DRIVERS
    print("\n🔗 5. VERIFICANDO DRIVERS...")
    
    if not mesh.data.shape_keys.animation_data:
        print("   ❌ NO HAY ANIMATION DATA")
        print("   → No se han creado drivers")
        print("   → Ejecuta: setup_facial_emotions_arkit.py")
        return False
    
    drivers = mesh.data.shape_keys.animation_data.drivers
    
    if not drivers:
        print("   ❌ NO HAY DRIVERS")
        print("   → Ejecuta: setup_facial_emotions_arkit.py")
        return False
    
    print(f"   ✅ Drivers encontrados: {len(drivers)}")
    
    # Analizar cada driver
    for driver in drivers:
        shape_key_name = driver.data_path.split('"')[1]
        if shape_key_name in shape_keys:
            print(f"\n      Shape Key: {shape_key_name}")
            
            fcurve = driver
            if fcurve.driver and fcurve.driver.variables:
                for var in fcurve.driver.variables:
                    if var.targets:
                        target = var.targets[0]
                        prop_name = target.data_path.replace('["', '').replace('"]', '')
                        print(f"         → Conectado a: {prop_name}")
                        
                        # Verificar si el target existe
                        if target.id and prop_name in target.id.keys():
                            valor_control = target.id[prop_name]
                            valor_shape = shape_keys[shape_key_name].value
                            print(f"         Control: {valor_control:.3f} → Shape: {valor_shape:.3f}")
                        else:
                            print(f"         ⚠️  Target no válido")
    
    # 6. PRUEBA DE CAMBIO EN VIVO
    print("\n\n🧪 6. PRUEBA EN VIVO...")
    print("   Cambiando EMOTION_SORPRESA a 1.0...")
    
    # Guardar valor original
    valor_original = armature['EMOTION_SORPRESA'] if 'EMOTION_SORPRESA' in armature.keys() else 0.0
    
    # Cambiar valor
    if 'EMOTION_SORPRESA' in armature.keys():
        armature['EMOTION_SORPRESA'] = 1.0
        
        # Forzar actualización
        bpy.context.view_layer.update()
        
        # Verificar si los shape keys cambiaron
        print("\n   Valores de Shape Keys afectados:")
        for bs in ['BrowInnerUp', 'BrowOuterUpLeft', 'BrowOuterUpRight', 
                   'EyeWideLeft', 'EyeWideRight']:
            if bs in shape_keys:
                valor = shape_keys[bs].value
                if valor > 0.01:
                    print(f"      ✅ {bs}: {valor:.3f} (CAMBIÓ)")
                else:
                    print(f"      ❌ {bs}: {valor:.3f} (NO CAMBIÓ)")
        
        # Restaurar valor
        armature['EMOTION_SORPRESA'] = valor_original
        bpy.context.view_layer.update()
    
    # RESUMEN FINAL
    print("\n" + "="*70)
    print("📊 RESUMEN DEL DIAGNÓSTICO")
    print("="*70)
    
    if controles_existentes == 6 and total_encontrados == total_necesarios and len(drivers) > 0:
        print("✅ SISTEMA COMPLETO Y FUNCIONAL")
        print("\nSi las expresiones no se ven:")
        print("   1. Verifica que estás en OBJECT MODE")
        print("   2. Asegúrate de ver el personaje en la vista 3D")
        print("   3. Los cambios son sutiles, prueba con valores de 1.0")
        print("   4. Revisa que la cámara enfoque la cara")
    else:
        print("⚠️  SISTEMA INCOMPLETO")
        if controles_existentes < 6:
            print(f"   - Faltan controles: {6 - controles_existentes}")
        if total_encontrados < total_necesarios:
            print(f"   - Faltan blendshapes: {total_necesarios - total_encontrados}")
        if not drivers or len(drivers) == 0:
            print("   - Faltan drivers")
        print("\n👉 Ejecuta: setup_facial_emotions_arkit.py")
    
    print("="*70 + "\n")
    
    return True


# Ejecutar diagnóstico
if __name__ == "__main__":
    diagnosticar()
