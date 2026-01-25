"""
PRUEBA DE ACTUALIZACIÓN FORZADA
Este script verifica y fuerza la actualización de los shape keys
"""

import bpy


def test_actualizacion():
    """Prueba si los shape keys se actualizan correctamente"""
    
    print("\n" + "="*70)
    print("🔧 PRUEBA DE ACTUALIZACIÓN DE SHAPE KEYS")
    print("="*70)
    
    # 1. Buscar componentes
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
    if not armatures:
        print("❌ No hay Armature")
        return
    
    armature = armatures[0]
    
    # Buscar mesh
    mesh = None
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.shape_keys:
            mesh = obj
            break
    
    if not mesh:
        print("❌ No hay mesh con shape keys")
        return
    
    print(f"✅ Armature: {armature.name}")
    print(f"✅ Mesh: {mesh.name}")
    
    # 2. Verificar que existe el control
    if 'EMOTION_SORPRESA' not in armature.keys():
        print("❌ No existe EMOTION_SORPRESA")
        print("   Ejecuta: setup_facial_emotions_arkit.py")
        return
    
    # 3. Resetear todo
    print("\n🔄 Reseteando controles...")
    for prop in ['EMOTION_SORPRESA', 'EMOTION_IRA', 'EMOTION_ALEGRIA', 
                 'EMOTION_ASCO', 'EMOTION_TRISTEZA', 'BLINK_CONTROL']:
        if prop in armature.keys():
            armature[prop] = 0.0
    
    # FORZAR ACTUALIZACIÓN MÚLTIPLE
    bpy.context.view_layer.update()
    bpy.context.evaluated_depsgraph_get().update()
    
    # 4. Cambiar valor y verificar
    print("\n📊 Cambiando EMOTION_SORPRESA a 1.0...")
    armature['EMOTION_SORPRESA'] = 1.0
    
    # Marcar armature como modificado
    armature.update_tag()
    
    # Forzar actualización completa
    bpy.context.view_layer.update()
    bpy.context.evaluated_depsgraph_get().update()
    
    # Si hay objeto seleccionado, forzar actualización
    if bpy.context.active_object:
        bpy.context.active_object.update_tag()
    
    # Verificar valores
    shape_keys = mesh.data.shape_keys.key_blocks
    
    print("\n🎭 Valores de Shape Keys:")
    cambios = 0
    
    for bs_name in ['BrowInnerUp', 'BrowOuterUpLeft', 'BrowOuterUpRight', 
                    'EyeWideLeft', 'EyeWideRight']:
        if bs_name in shape_keys:
            valor = shape_keys[bs_name].value
            estado = "✅ CAMBIÓ" if valor > 0.01 else "❌ SIN CAMBIO"
            print(f"   {bs_name}: {valor:.3f} {estado}")
            if valor > 0.01:
                cambios += 1
        else:
            print(f"   {bs_name}: ❌ NO EXISTE")
    
    # 5. Verificar drivers
    print("\n🔗 Verificando drivers...")
    
    if mesh.data.shape_keys.animation_data and mesh.data.shape_keys.animation_data.drivers:
        drivers = mesh.data.shape_keys.animation_data.drivers
        print(f"   Drivers totales: {len(drivers)}")
        
        # Buscar driver de BrowInnerUp
        for driver in drivers:
            try:
                path = driver.data_path
                if 'BrowInnerUp' in path:
                    print(f"\n   Driver encontrado para BrowInnerUp:")
                    print(f"      Data path: {path}")
                    print(f"      Type: {driver.driver.type}")
                    print(f"      Expression: {driver.driver.expression}")
                    
                    if driver.driver.variables:
                        for var in driver.driver.variables:
                            print(f"      Variable: {var.name}")
                            if var.targets:
                                target = var.targets[0]
                                print(f"         Target ID: {target.id.name if target.id else 'None'}")
                                print(f"         Data path: {target.data_path}")
                    
                    # Intentar evaluar el driver manualmente
                    try:
                        if driver.driver.variables:
                            var = driver.driver.variables[0]
                            target = var.targets[0]
                            if target.id:
                                prop_name = target.data_path.replace('["', '').replace('"]', '')
                                if prop_name in target.id.keys():
                                    valor_control = target.id[prop_name]
                                    print(f"      ✅ Valor del control: {valor_control}")
                                else:
                                    print(f"      ❌ Propiedad no existe: {prop_name}")
                    except Exception as e:
                        print(f"      ⚠️  Error al evaluar: {e}")
                    
                    break
            except:
                pass
    else:
        print("   ❌ No hay drivers")
    
    # RESUMEN
    print("\n" + "="*70)
    if cambios > 0:
        print(f"✅ SISTEMA FUNCIONANDO - {cambios} shape keys cambiaron")
    else:
        print("❌ PROBLEMA DETECTADO - Los shape keys no cambian")
        print("\nPosibles causas:")
        print("1. Los drivers no están conectados correctamente")
        print("2. Los nombres de shape keys no coinciden")
        print("3. El modelo no tiene ARKit blendshapes")
        print("\n👉 Ejecuta: diagnostico_sistema.py para más detalles")
    
    print("="*70 + "\n")


if __name__ == "__main__":
    test_actualizacion()
