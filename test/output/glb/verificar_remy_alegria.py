"""
VERIFICADOR VISUAL - Abre Remy_ALEGRIA.glb y verifica la expresión
Ejecutar DESPUÉS de generar_remy_alegria.py
"""

import bpy
import os


RUTA_GLB_ALEGRIA = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy_ALEGRIA.glb"


def verificar_remy_alegria():
    """Carga y verifica el GLB generado"""
    
    print("\n" + "="*70)
    print("🔍 VERIFICADOR - REMY CON ALEGRÍA")
    print("="*70)
    
    # Limpiar escena
    print("\n🧹 Limpiando escena...")
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Verificar archivo existe
    print("\n📦 Verificando archivo...")
    if not os.path.exists(RUTA_GLB_ALEGRIA):
        print(f"   ❌ ERROR: Archivo no encontrado:")
        print(f"      {RUTA_GLB_ALEGRIA}")
        print("\n   👉 Ejecuta primero: generar_remy_alegria.py")
        return False
    
    print(f"   ✅ Archivo encontrado")
    
    # Importar
    print("\n📥 Importando Remy_ALEGRIA.glb...")
    try:
        bpy.ops.import_scene.gltf(filepath=RUTA_GLB_ALEGRIA)
        print("   ✅ Importado correctamente")
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        return False
    
    # Buscar componentes
    print("\n🔎 Analizando modelo...")
    
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == 'ARMATURE']
    if not armatures:
        print("   ❌ No se encontró Armature")
        return False
    
    armature = armatures[0]
    print(f"   ✅ Armature: {armature.name}")
    
    # Buscar mesh
    mesh = None
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.data.shape_keys:
            mesh = obj
            break
    
    if not mesh:
        print("   ❌ No se encontró mesh con shape keys")
        return False
    
    print(f"   ✅ Mesh: {mesh.name}")
    
    # Verificar custom properties
    print("\n📊 Custom Properties:")
    
    controles = ['EMOTION_SORPRESA', 'EMOTION_IRA', 'EMOTION_ALEGRIA', 
                 'EMOTION_ASCO', 'EMOTION_TRISTEZA', 'BLINK_CONTROL']
    
    tiene_controles = True
    for control in controles:
        if control in armature.keys():
            valor = armature[control]
            if control == 'EMOTION_ALEGRIA' and valor > 0.01:
                print(f"   ✅ {control}: {valor:.3f} ← ACTIVO")
            elif valor > 0.01:
                print(f"   ⚠️  {control}: {valor:.3f}")
            else:
                print(f"   ✓  {control}: {valor:.3f}")
        else:
            print(f"   ❌ {control}: NO EXISTE")
            tiene_controles = False
    
    if not tiene_controles:
        print("\n   ⚠️  Faltan algunos controles")
    
    # Verificar shape keys
    print("\n🎭 Shape Keys de ALEGRÍA:")
    
    shape_keys = mesh.data.shape_keys.key_blocks
    alegria_shapes = ['MouthSmileLeft', 'MouthSmileRight', 'CheekPuff']
    
    cambios = 0
    for bs_name in alegria_shapes:
        if bs_name in shape_keys:
            valor = shape_keys[bs_name].value
            if valor > 0.01:
                print(f"   ✅ {bs_name}: {valor:.3f} (ACTIVO)")
                cambios += 1
            else:
                print(f"   ❌ {bs_name}: {valor:.3f} (INACTIVO)")
        else:
            print(f"   ❌ {bs_name}: NO EXISTE")
    
    # Verificar drivers
    print("\n🔗 Drivers:")
    
    if mesh.data.shape_keys.animation_data and mesh.data.shape_keys.animation_data.drivers:
        drivers = mesh.data.shape_keys.animation_data.drivers
        print(f"   ✅ Total de drivers: {len(drivers)}")
        
        # Contar drivers de alegría
        drivers_alegria = 0
        for driver in drivers:
            for bs_name in alegria_shapes:
                if bs_name in driver.data_path:
                    drivers_alegria += 1
                    break
        
        print(f"   ✅ Drivers de ALEGRÍA: {drivers_alegria}/{len(alegria_shapes)}")
    else:
        print("   ❌ No hay drivers")
    
    # RESUMEN
    print("\n" + "="*70)
    
    if cambios >= 2 and tiene_controles:
        print("✅ VERIFICACIÓN EXITOSA")
        print("="*70)
        print("\n😄 Remy tiene expresión de ALEGRÍA aplicada")
        print(f"\n   Shape keys activos: {cambios}/{len(alegria_shapes)}")
        print(f"   EMOTION_ALEGRIA: {armature['EMOTION_ALEGRIA']:.3f}")
        print("\n🎉 El modelo está listo para usar")
    else:
        print("⚠️  VERIFICACIÓN CON PROBLEMAS")
        print("="*70)
        if cambios == 0:
            print("\n   ❌ Los shape keys no tienen valores")
            print("   → La expresión no se aplicó correctamente")
        if not tiene_controles:
            print("\n   ❌ Faltan custom properties")
            print("   → El setup no se completó")
        print("\n   👉 Revisa el output de generar_remy_alegria.py")
    
    print("="*70 + "\n")
    
    return cambios > 0


if __name__ == "__main__":
    verificar_remy_alegria()
