import bpy
from pathlib import Path

# Directorio base
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy")

# Buscar todos los archivos GLB de Nancy con animaciones (excepto el modelo base)
archivos = []
for glb_file in BASE_DIR.rglob("Nancy_resultado_*.glb"):
    if "_BACKUP" not in glb_file.name:  # Saltar backups
        archivos.append(glb_file)

print(f"\n{'='*80}")
print(f"REGENERANDO ARCHIVOS CON TEXTURAS - NANCY")
print(f"{'='*80}")
print(f"📂 Encontrados: {len(archivos)} archivos\n")

# Archivo base con texturas
NANCY_BASE = BASE_DIR / "Nancy.glb"

# Lista de huesos del tren inferior
huesos_piernas = [
    "Hips",
    "LeftUpLeg",
    "LeftLeg",
    "LeftFoot",
    "LeftToeBase",
    "LeftToe_End",
    "RightUpLeg",
    "RightLeg",
    "RightFoot",
    "RightToeBase",
    "RightToe_End"
]

total_procesados = 0
total_fallidos = 0

for idx, archivo in enumerate(archivos, 1):
    categoria = archivo.parent.name
    anim_name = archivo.stem.replace("Nancy_resultado_", "")
    print(f"[{idx}/{len(archivos)}] {categoria}/{anim_name}")
    
    try:
        # Limpiar escena
        bpy.ops.wm.read_homefile(use_empty=True)
        
        # Importar Nancy base (CON texturas)
        bpy.ops.import_scene.gltf(filepath=str(NANCY_BASE))
        nancy_armature = bpy.data.objects.get("Nancy_Armature") or bpy.data.objects.get("Armature")
        
        # Guardar referencia a las texturas originales
        texturas_originales = {img.name: img for img in bpy.data.images}
        
        # Importar el archivo con animación (SIN texturas)
        bpy.ops.import_scene.gltf(filepath=str(archivo))
        
        # Buscar el segundo armature (el que tiene animación)
        anim_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != nancy_armature:
                anim_armature = obj
                break
        
        if not anim_armature or not anim_armature.animation_data or not anim_armature.animation_data.action:
            print(f"   ⚠️ Sin animación")
            continue
        
        # Copiar la animación al armature de Nancy
        action_original = anim_armature.animation_data.action
        action = action_original.copy()
        action.name = f"{action_original.name}_fixed"
        
        # Obtener el rango de frames de la animación
        if action.fcurves:
            frame_start = min([min([kf.co[0] for kf in fc.keyframe_points]) for fc in action.fcurves])
            frame_end = max([max([kf.co[0] for kf in fc.keyframe_points]) for fc in action.fcurves])
        else:
            frame_start, frame_end = 1, 250
        
        # Eliminar FCurves de piernas
        fcurves_a_eliminar = []
        for fcurve in action.fcurves:
            for hueso in huesos_piernas:
                if f'pose.bones["{hueso}"]' in fcurve.data_path:
                    fcurves_a_eliminar.append(fcurve)
                    break
        
        for fcurve in fcurves_a_eliminar:
            action.fcurves.remove(fcurve)
        
        # Eliminar objetos del segundo import (el que no tiene texturas)
        objetos_nancy = [obj for obj in bpy.data.objects if obj == nancy_armature or obj.parent == nancy_armature]
        objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_nancy]
        
        for obj in objetos_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # CRÍTICO: Eliminar TODAS las otras acciones de bpy.data.actions PRIMERO
        # El exportador GLTF exporta todas las acciones con users>0 como NLA tracks
        acciones_a_eliminar = [act for act in bpy.data.actions if act != action]
        for act in acciones_a_eliminar:
            bpy.data.actions.remove(act)
        
        # Crear/limpiar animation_data
        if not nancy_armature.animation_data:
            nancy_armature.animation_data_create()
        
        # Limpiar NLA tracks existentes
        while len(nancy_armature.animation_data.nla_tracks) > 0:
            nancy_armature.animation_data.nla_tracks.remove(nancy_armature.animation_data.nla_tracks[0])
        
        # Asignar la acción directamente (SIN NLA)
        nancy_armature.animation_data.action = action
        
        # NO usar NLA
        nancy_armature.animation_data.use_nla = False
        
        # Configurar el rango de frames en la escena
        bpy.context.scene.frame_start = int(frame_start)
        bpy.context.scene.frame_end = int(frame_end)
        
        # Resetear pose de piernas
        bpy.context.view_layer.objects.active = nancy_armature
        bpy.ops.object.mode_set(mode='POSE')
        
        for bone_name in huesos_piernas:
            if bone_name in nancy_armature.pose.bones:
                pose_bone = nancy_armature.pose.bones[bone_name]
                pose_bone.location = (0, 0, 0)
                pose_bone.rotation_quaternion = (1, 0, 0, 0)
                pose_bone.rotation_euler = (0, 0, 0)
                pose_bone.scale = (1, 1, 1)
        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Verificar texturas antes de exportar
        texturas_finales = len([img for img in bpy.data.images if img.packed_file])
        
        # Exportar directamente a GLB (sin pasar por FBX)
        # export_force_sampling=True asegura que las animaciones se exporten desde la acción activa
        bpy.ops.export_scene.gltf(
            filepath=str(archivo),
            export_format='GLB',
            export_animations=True,
            export_force_sampling=True,  # CRÍTICO: Exportar desde acción activa, no desde NLA
            export_image_format='AUTO'  # Mantener formato original de imágenes
        )
        
        file_size = archivo.stat().st_size / (1024*1024)
        print(f"   ✅ {file_size:.1f}MB | {texturas_finales} texturas | -{len(fcurves_a_eliminar)} FCurves piernas")
        total_procesados += 1
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        total_fallidos += 1

print(f"\n{'='*80}")
print(f"RESUMEN FINAL")
print(f"{'='*80}")
print(f"✅ Procesados: {total_procesados}/{len(archivos)}")
print(f"❌ Fallidos: {total_fallidos}/{len(archivos)}")
print(f"{'='*80}\n")
