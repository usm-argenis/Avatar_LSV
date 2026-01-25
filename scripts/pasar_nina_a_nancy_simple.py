import bpy
from pathlib import Path

print("="*80)
print("TRANSFERENCIA: Nina 'a la orden' → Nancy.glb")
print("="*80)

# Rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_MODEL = BASE_DIR / "Nancy" / "Nancy.glb"  # Modelo base limpio
NINA_FILE = BASE_DIR / "Nina" / "cortesia" / "Nina_resultado_a la orden.glb"
NANCY_OUTPUT = BASE_DIR / "Nancy" / "cortesia" / "Nancy_resultado_a la orden.glb"

print(f"\n📂 Configuración:")
print(f"   Modelo: {NANCY_MODEL.name}")
print(f"   Animación: {NINA_FILE.name}")
print(f"   Salida: {NANCY_OUTPUT.name}")

try:
    # PASO 1: Limpiar y cargar Nancy
    bpy.ops.wm.read_factory_settings(use_empty=True)
    print(f"\n📦 Cargando {NANCY_MODEL.name}...")
    bpy.ops.import_scene.gltf(filepath=str(NANCY_MODEL))
    
    nancy_armature = None
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            nancy_armature = obj
            break
    
    if not nancy_armature:
        print("❌ No armature en Nancy")
        exit(1)
    
    print(f"   ✅ Armature: {nancy_armature.name}")
    
    # Eliminar animación previa si existe
    if nancy_armature.animation_data:
        nancy_armature.animation_data_clear()
    
    # PASO 2: Cargar Nina CON animación
    print(f"\n🎬 Cargando animación de Nina...")
    objetos_antes = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(NINA_FILE))
    objetos_nina = set(bpy.data.objects) - objetos_antes
    
    nina_armature = None
    for obj in objetos_nina:
        if obj.type == 'ARMATURE':
            nina_armature = obj
            break
    
    if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
        print("❌ Nina no tiene animación")
        exit(1)
    
    nina_action = nina_armature.animation_data.action
    print(f"   ✅ Action: {nina_action.name}")
    print(f"   ✅ FCurves: {len(nina_action.fcurves)}")
    print(f"   ✅ Frames: {nina_action.frame_range[1] - nina_action.frame_range[0]:.0f}")
    
    # PASO 3: Copiar action de Nina a Nancy
    print(f"\n📋 Copiando animación...")
    
    if not nancy_armature.animation_data:
        nancy_armature.animation_data_create()
    
    # USAR .copy() que es el método que funcionó
    nancy_action = nina_action.copy()
    nancy_action.name = "Nancy_a_la_orden"
    nancy_armature.animation_data.action = nancy_action
    
    # Establecer frame range
    bpy.context.scene.frame_start = int(nina_action.frame_range[0])
    bpy.context.scene.frame_end = int(nina_action.frame_range[1])
    
    print(f"   ✅ Action copiada: {nancy_action.name}")
    
    # PASO 4: Eliminar Nina
    print(f"\n🗑️ Eliminando objetos de Nina...")
    for obj in objetos_nina:
        bpy.data.objects.remove(obj, do_unlink=True)
    
    # PASO 5: Exportar con la configuración que funcionó antes
    print(f"\n💾 Exportando...")
    NANCY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    
    bpy.ops.export_scene.gltf(
        filepath=str(NANCY_OUTPUT),
        export_format='GLB',
        export_animations=True,
        export_frame_range=True,
        export_current_frame=False,
        export_force_sampling=False,  # CAMBIO CRÍTICO
        export_def_bones=False,
        export_optimize_animation_size=False,
        export_nla_strips=False,
        export_apply=False  # CAMBIO CRÍTICO
    )
    
    if NANCY_OUTPUT.exists():
        size_mb = NANCY_OUTPUT.stat().st_size / (1024 * 1024)
        print(f"   ✅ Generado: {size_mb:.1f} MB")
        
        # VERIFICACIÓN
        print(f"\n🔍 Verificando...")
        bpy.ops.wm.read_factory_settings(use_empty=True)
        bpy.ops.import_scene.gltf(filepath=str(NANCY_OUTPUT))
        
        test_arm = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                test_arm = obj
                break
        
        if test_arm and test_arm.animation_data and test_arm.animation_data.action:
            test_action = test_arm.animation_data.action
            
            # Contar keyframes que realmente cambian
            fcurves_con_movimiento = 0
            for fc in test_action.fcurves:
                if len(fc.keyframe_points) > 1:
                    valores = [kf.co[1] for kf in fc.keyframe_points[:5]]
                    if len(set([round(v, 4) for v in valores])) > 1:
                        fcurves_con_movimiento += 1
            
            print(f"   Action: {test_action.name}")
            print(f"   FCurves totales: {len(test_action.fcurves)}")
            print(f"   FCurves con movimiento: {fcurves_con_movimiento}")
            
            # Test de movimiento real
            bpy.context.scene.frame_set(0)
            pos_inicial = test_arm.pose.bones["Hips"].matrix.translation.copy()
            bpy.context.scene.frame_set(30)
            pos_final = test_arm.pose.bones["Hips"].matrix.translation.copy()
            distancia = (pos_final - pos_inicial).length
            
            if distancia > 0.001 or fcurves_con_movimiento > 50:
                print(f"\n✅ ✅ ✅ ÉXITO - Animación funcionando ✅ ✅ ✅")
                print(f"Movimiento detectado: {distancia:.4f} unidades")
            else:
                print(f"\n⚠️ ADVERTENCIA - Sin movimiento detectado")
                print(f"Distancia: {distancia:.6f}")
        else:
            print(f"\n❌ Sin animación en archivo exportado")
    else:
        print(f"   ❌ No se generó archivo")
        
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    exit(1)
