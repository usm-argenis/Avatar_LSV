import bpy
import sys

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)

print("\n" + "="*70)
print("VERIFICANDO TAMAÑOS EN FBX EXPORTADOS")
print("="*70)

archivos = [
    ("Remy", "output/Remy_resultado_b.fbx"),
    ("Leonard", "output/Leonard_resultado_b.fbx")
]

resultados = []

for nombre, ruta in archivos:
    print(f"\n📊 Cargando {nombre}: {ruta}")
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    try:
        bpy.ops.import_scene.fbx(filepath=ruta)
        
        # Buscar armature
        arm = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                arm = obj
                break
        
        if not arm:
            print(f"❌ No se encontró armature en {nombre}")
            continue
            
        print(f"✅ Armature encontrado: {arm.name}")
        print(f"   Escala del objeto: {arm.scale}")
        
        # Buscar Hips
        hips = None
        for bone_name in ['mixamorig:Hips', 'Hips', 'hips', 'mixamorig9:Hips']:
            if bone_name in arm.data.bones:
                hips = arm.data.bones[bone_name]
                break
        
        if hips:
            # Calcular posición world
            pos_world = arm.matrix_world @ hips.head_local
            pos_local = hips.head_local
            
            print(f"✅ Hips encontrado: {hips.name}")
            print(f"   Posición Local Z: {pos_local.z:.6f}")
            print(f"   Posición World Z: {pos_world.z:.6f}")
            print(f"   Longitud del hueso: {hips.length:.6f}")
            
            resultados.append({
                'nombre': nombre,
                'escala': arm.scale,
                'hips_local_z': pos_local.z,
                'hips_world_z': pos_world.z,
                'bone_length': hips.length
            })
        else:
            print(f"❌ No se encontró Hips en {nombre}")
            
    except Exception as e:
        print(f"❌ Error cargando {nombre}: {e}")

# Comparar resultados
print("\n" + "="*70)
print("COMPARACIÓN")
print("="*70)

if len(resultados) == 2:
    remy = resultados[0]
    leonard = resultados[1]
    
    print(f"\n{remy['nombre']}:")
    print(f"  Escala objeto: {remy['escala']}")
    print(f"  Hips World Z: {remy['hips_world_z']:.6f}")
    
    print(f"\n{leonard['nombre']}:")
    print(f"  Escala objeto: {leonard['escala']}")
    print(f"  Hips World Z: {leonard['hips_world_z']:.6f}")
    
    ratio = leonard['hips_world_z'] / remy['hips_world_z']
    print(f"\n📏 Ratio (Leonard/Remy): {ratio:.6f}")
    
    if abs(ratio - 1.0) < 0.01:
        print("✅ LOS TAMAÑOS SON IGUALES (±1%)")
    else:
        print(f"❌ LOS TAMAÑOS SON DIFERENTES")
        print(f"   Leonard es {ratio:.3f}x el tamaño de Remy")
        escala_necesaria = 1.0 / ratio
        print(f"   💡 Para igualar en el visor, Leonard necesita escala: {escala_necesaria:.6f}")

print("="*70)
