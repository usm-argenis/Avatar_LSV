"""
Verificar que los archivos retargeteados tengan animación
"""
import bpy
import sys

def verify_animation(glb_path, avatar_name):
    print(f"\n{'='*60}")
    print(f"VERIFICANDO: {avatar_name}")
    print(f"Archivo: {glb_path}")
    print(f"{'='*60}")
    
    # Limpiar escena
    bpy.ops.wm.read_homefile(use_empty=True)
    
    # Cargar GLB
    bpy.ops.import_scene.gltf(filepath=glb_path)
    
    # Verificar actions
    if not bpy.data.actions:
        print("❌ ERROR: No hay acciones en el archivo")
        return False
    
    print(f"✅ Acciones encontradas: {len(bpy.data.actions)}")
    
    for action in bpy.data.actions:
        frame_start, frame_end = action.frame_range
        frame_count = int(frame_end - frame_start + 1)
        print(f"   - {action.name}: frames {int(frame_start)}-{int(frame_end)} ({frame_count} frames)")
        
        # Verificar fcurves
        fcurve_count = len(action.fcurves)
        print(f"     FCurves: {fcurve_count}")
        
        if fcurve_count == 0:
            print("     ⚠️  ADVERTENCIA: La acción no tiene FCurves")
    
    # Verificar armature
    armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
    if armatures:
        print(f"\n✅ Armatures: {len(armatures)}")
        for arm in armatures:
            print(f"   - {arm.name}: {len(arm.pose.bones)} huesos")
            if arm.animation_data and arm.animation_data.action:
                print(f"     Acción asignada: {arm.animation_data.action.name}")
    else:
        print("❌ No se encontró armature")
        return False
    
    # Verificar meshes
    meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
    print(f"\n✅ Meshes: {len(meshes)}")
    
    print(f"\n{'='*60}")
    print(f"✅ VERIFICACIÓN EXITOSA: {avatar_name}")
    print(f"{'='*60}\n")
    return True

# Verificar ambos archivos
duvall_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\deepmotion\verbo_default_1.glb"
carla_path = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Carla\deepmotion\verbo_default.glb"

duvall_ok = verify_animation(duvall_path, "DUVALL")
carla_ok = verify_animation(carla_path, "CARLA")

print("\n" + "="*60)
print("RESUMEN FINAL")
print("="*60)
print(f"Duvall: {'✅ CORRECTO' if duvall_ok else '❌ ERROR'}")
print(f"Carla:  {'✅ CORRECTO' if carla_ok else '❌ ERROR'}")
print("="*60)

if duvall_ok and carla_ok:
    print("\n🎉 AMBOS ARCHIVOS TIENEN ANIMACIÓN CORRECTAMENTE")
    sys.exit(0)
else:
    print("\n❌ AL MENOS UN ARCHIVO TIENE PROBLEMAS")
    sys.exit(1)
