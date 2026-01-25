import bpy
from pathlib import Path
import time
#"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python scripts\generar_todos_blend.py 2>&1 | Select-String -Pattern "(|||RESUMEN|Exitosos|Fallidos||guardado)" -Context 0,1
print("="*80)
print("GENERAR TODOS LOS ARCHIVOS BLEND: Nina → Nancy con Rokoko")
print("="*80)

# Rutas base
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
NANCY_MODEL = BASE_DIR / "Nancy" / "Nancy.glb"
BLEND_OUTPUT_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\blend")

# Todas las animaciones organizadas por categoría
ANIMACIONES = {
   "dias_semana":[
       "luz",]
   
}

def retarget_animacion(categoria, animacion_nombre):
    """Retargetear una animación de Nina a Nancy usando Rokoko"""
    
    print(f"\n{'='*80}")
    print(f"📝 {categoria.upper()} → {animacion_nombre}")
    print(f"{'='*80}")
    
    # Archivos
    nina_file = BASE_DIR / "Carla" / categoria / f"Carla_resultado_{animacion_nombre}.glb"
    blend_output = BLEND_OUTPUT_DIR / categoria / f"Nancy_resultado_{animacion_nombre}.blend"
    
    if not nina_file.exists():
        print(f"❌ ERROR: No existe {nina_file}")
        return False
    
    try:
        # Limpiar escena
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar Nancy (destino)
        print(f"📦 Importando Nancy...")
        bpy.ops.import_scene.gltf(filepath=str(NANCY_MODEL))
        
        nancy_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                nancy_armature = obj
                nancy_armature.name = "Nancy_Armature"
                break
        
        if not nancy_armature:
            print("❌ ERROR: No armature de Nancy")
            return False
        
        # Limpiar animación previa
        if nancy_armature.animation_data:
            nancy_armature.animation_data_clear()
        
        # Importar Nina (source con animación)
        print(f"🎬 Importando Nina con animación...")
        bpy.ops.import_scene.gltf(filepath=str(nina_file))
        
        nina_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != nancy_armature:
                nina_armature = obj
                nina_armature.name = "Nina_Armature"
                break
        
        if not nina_armature:
            print("❌ ERROR: No armature de Nina")
            return False
        
        if not nina_armature.animation_data or not nina_armature.animation_data.action:
            print("❌ ERROR: Nina no tiene animación")
            return False
        
        nina_action = nina_armature.animation_data.action
        frame_start = int(nina_action.frame_range[0])
        frame_end = int(nina_action.frame_range[1])
        
        print(f"   Frames: {frame_start} → {frame_end}")
        print(f"   FCurves: {len(nina_action.fcurves)}")
        
        # Aplicar retargeting manual con baking
        print(f"🔄 Aplicando retargeting manual...")
        
        # Configurar frame range
        bpy.context.scene.frame_start = frame_start
        bpy.context.scene.frame_end = frame_end
        
        # Crear constraints Copy Transforms para todos los huesos
        print(f"   📌 Creando constraints...")
        bpy.context.view_layer.objects.active = nancy_armature
        nancy_armature.select_set(True)
        
        constraints_creados = 0
        for nancy_bone in nancy_armature.pose.bones:
            if nancy_bone.name in nina_armature.pose.bones:
                constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = nina_armature
                constraint.subtarget = nancy_bone.name
                constraints_creados += 1
        
        print(f"   ✅ {constraints_creados} constraints creados")
        
        # Bake la animación
        print(f"   🔥 Baking animación...")
        start_time = time.time()
        bpy.ops.object.select_all(action='DESELECT')
        nancy_armature.select_set(True)
        bpy.context.view_layer.objects.active = nancy_armature
        
        bpy.ops.nla.bake(
            frame_start=frame_start,
            frame_end=frame_end,
            step=1,
            only_selected=False,
            visual_keying=True,
            clear_constraints=True,
            clear_parents=False,
            use_current_action=False,
            clean_curves=False,
            bake_types={'POSE'}
        )
        
        retarget_time = time.time() - start_time
        print(f"   ✅ Baking completado: {retarget_time:.2f}s")
        
        # Verificar animación en Nancy
        if not nancy_armature.animation_data or not nancy_armature.animation_data.action:
            print(f"❌ ERROR: Nancy no recibió animación")
            return False
        
        nancy_action = nancy_armature.animation_data.action
        print(f"   ✅ Action: {nancy_action.name}")
        print(f"   ✅ FCurves: {len(nancy_action.fcurves)}")
        
        # Verificar movimiento
        bpy.context.scene.frame_set(frame_start)
        bpy.context.view_layer.update()
        
        if "Hips" in nancy_armature.pose.bones:
            bone = nancy_armature.pose.bones["Hips"]
            pos_start = bone.matrix.translation.copy()
            rot_start = bone.matrix.to_quaternion().copy()
            
            bpy.context.scene.frame_set(frame_end)
            bpy.context.view_layer.update()
            
            pos_end = bone.matrix.translation
            rot_end = bone.matrix.to_quaternion()
            
            pos_diff = (pos_start - pos_end).length
            rot_diff = abs(rot_start.w - rot_end.w) + abs(rot_start.x - rot_end.x) + \
                      abs(rot_start.y - rot_end.y) + abs(rot_start.z - rot_end.z)
            
            print(f"   Hips movimiento: pos={pos_diff:.4f}, rot={rot_diff:.4f}")
            
            if pos_diff > 0.001 or rot_diff > 0.001:
                print(f"   ✅ Animación verificada - hay movimiento")
            else:
                print(f"   ⚠️ Advertencia: Poco movimiento detectado")
        
        # Eliminar objetos de Nina
        objetos_nancy = []
        for obj in bpy.data.objects:
            if obj == nancy_armature or obj.parent == nancy_armature:
                objetos_nancy.append(obj)
        
        objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
        for obj in objetos_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        print(f"   🗑️ {len(objetos_eliminar)} objetos Nina eliminados")
        
        # Guardar .blend
        blend_output.parent.mkdir(parents=True, exist_ok=True)
        bpy.ops.wm.save_as_mainfile(filepath=str(blend_output))
        
        if blend_output.exists():
            size_mb = blend_output.stat().st_size / (1024 * 1024)
            print(f"   💾 BLEND guardado: {size_mb:.1f} MB")
            print(f"   ✅ ÉXITO: {blend_output.name}")
            return True
        else:
            print(f"   ❌ ERROR: No se guardó el archivo")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

# MAIN
print(f"\n📊 Total de animaciones a procesar:")
total = 0
for categoria, animaciones in ANIMACIONES.items():
    print(f"   {categoria}: {len(animaciones)} animaciones")
    total += len(animaciones)
print(f"   TOTAL: {total} animaciones")

# Procesar todas las animaciones
resultados = {
    "exitosos": [],
    "fallidos": []
}

inicio_total = time.time()

for categoria, animaciones in ANIMACIONES.items():
    print(f"\n{'#'*80}")
    print(f"CATEGORÍA: {categoria.upper()}")
    print(f"{'#'*80}")
    
    for animacion in animaciones:
        exito = retarget_animacion(categoria, animacion)
        
        if exito:
            resultados["exitosos"].append(f"{categoria}/{animacion}")
        else:
            resultados["fallidos"].append(f"{categoria}/{animacion}")

tiempo_total = time.time() - inicio_total

# Resumen final
print(f"\n{'='*80}")
print(f"RESUMEN FINAL")
print(f"{'='*80}")
print(f"⏱️ Tiempo total: {tiempo_total/60:.1f} minutos")
print(f"✅ Exitosos: {len(resultados['exitosos'])}/{total}")
print(f"❌ Fallidos: {len(resultados['fallidos'])}/{total}")

if resultados["fallidos"]:
    print(f"\n❌ Animaciones fallidas:")
    for item in resultados["fallidos"]:
        print(f"   - {item}")

if resultados["exitosos"]:
    print(f"\n✅ Archivos .blend generados en:")
    print(f"   {BLEND_OUTPUT_DIR}")
    print(f"\n{'='*80}")
    print(f"🎉 PROCESO COMPLETADO")
    print(f"{'='*80}")
