"""
Script para regenerar archivos de Nancy con:
- Texturas preservadas (15 texturas de Nancy)
- Animaciones de Nina sin piernas
- Flujo: GLB(Nina) → FBX(temp) → GLB(final con texturas)

El flujo FBX es necesario porque GLTF no exporta correctamente 
animaciones desde la acción activa en Blender 4.5.2
"""

import bpy
from pathlib import Path

# Configuración
base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
nancy_base = base_dir / "test/output/glb/Nancy/Nancy.glb"
carpeta_entrada = base_dir / "test/output/glb/Nina"
carpeta_salida = base_dir / "test/output/glb/Nancy"
carpeta_temp = base_dir / "test/output/temp"
carpeta_temp.mkdir(exist_ok=True)

# Huesos de piernas a eliminar
huesos_piernas = [
    'Hips', 'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase',
    'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase'
]

# Buscar todos los archivos de Nina
archivos = []
for categoria_path in carpeta_entrada.iterdir():
    if categoria_path.is_dir():
        for archivo in categoria_path.glob("Nina_resultado_*.glb"):
            archivos.append((categoria_path.name, archivo))

print(f"\n{'='*80}")
print(f"REGENERACIÓN NANCY CON FLUJO FBX")
print(f"Archivos a procesar: {len(archivos)}")
print(f"{'='*80}\n")

total_procesados = 0
total_fallidos = 0

for categoria, archivo_nina in archivos:
    animacion = archivo_nina.stem.replace("Nina_resultado_", "")
    
    # Rutas de salida
    carpeta_cat = carpeta_salida / categoria
    carpeta_cat.mkdir(parents=True, exist_ok=True)
    archivo_fbx_temp = carpeta_temp / f"temp_{animacion}.fbx"
    archivo_salida = carpeta_cat / f"Nancy_resultado_{animacion}.glb"
    
    print(f"[{total_procesados+1}/{len(archivos)}] {categoria}/{animacion}")
    
    try:
        # ===== PASO 1: Crear FBX con animación =====
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar Nancy base
        bpy.ops.import_scene.gltf(filepath=str(nancy_base))
        nancy_objs = list(bpy.data.objects)
        nancy_armature = next((obj for obj in nancy_objs if obj.type == 'ARMATURE'), None)
        
        if not nancy_armature:
            raise Exception("No se encontró armature de Nancy")
        
        # Importar animación de Nina
        bpy.ops.import_scene.gltf(filepath=str(archivo_nina))
        nina_objs = [obj for obj in bpy.data.objects if obj not in nancy_objs]
        nina_armature = next((obj for obj in nina_objs if obj.type == 'ARMATURE'), None)
        
        if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
            raise Exception("Nina no tiene animación")
        
        action_original = nina_armature.animation_data.action
        
        # Copiar y limpiar acción
        action = action_original.copy()
        action.name = f"{animacion}_limpia"
        
        frame_start = action.frame_range[0]
        frame_end = action.frame_range[1]
        
        # Eliminar FCurves de piernas
        fcurves_eliminadas = [fc for fc in action.fcurves if any(bone in fc.data_path for bone in huesos_piernas)]
        for fc in fcurves_eliminadas:
            action.fcurves.remove(fc)
        
        # Eliminar objetos de Nina
        for obj in nina_objs:
            if obj != nina_armature:
                bpy.data.objects.remove(obj, do_unlink=True)
        
        # Eliminar acciones no usadas
        acciones_a_eliminar = [act for act in bpy.data.actions if act != action]
        for act in acciones_a_eliminar:
            bpy.data.actions.remove(act)
        
        # Asignar acción a Nancy
        if not nancy_armature.animation_data:
            nancy_armature.animation_data_create()
        
        nancy_armature.animation_data.action = action
        bpy.context.scene.frame_start = int(frame_start)
        bpy.context.scene.frame_end = int(frame_end)
        
        # Exportar a FBX temporal
        bpy.ops.export_scene.fbx(
            filepath=str(archivo_fbx_temp),
            use_selection=False,
            bake_anim=True,
            bake_anim_use_all_actions=False,
            bake_anim_use_nla_strips=False,
            add_leaf_bones=False
        )
        
        # ===== PASO 2: Combinar animación (FBX) + texturas (Nancy base) =====
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar Nancy base (texturas)
        bpy.ops.import_scene.gltf(filepath=str(nancy_base))
        nancy_objs = list(bpy.data.objects)
        nancy_armature = next((obj for obj in nancy_objs if obj.type == 'ARMATURE'), None)
        texturas_nancy = len(bpy.data.images)
        
        # Importar FBX con animación
        bpy.ops.import_scene.fbx(filepath=str(archivo_fbx_temp))
        fbx_objs = [obj for obj in bpy.data.objects if obj not in nancy_objs]
        fbx_armature = next((obj for obj in fbx_objs if obj.type == 'ARMATURE'), None)
        
        if not fbx_armature or not fbx_armature.animation_data or not fbx_armature.animation_data.action:
            raise Exception("FBX no tiene animación")
        
        fbx_action = fbx_armature.animation_data.action
        
        # Copiar la acción
        accion_limpia = fbx_action.copy()
        accion_limpia.name = animacion
        
        # Eliminar objetos del FBX
        for obj in fbx_objs:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # Eliminar TODAS las otras acciones
        acciones_a_eliminar = [act for act in bpy.data.actions if act != accion_limpia]
        for act in acciones_a_eliminar:
            bpy.data.actions.remove(act)
        
        # Crear animation_data si no existe
        if not nancy_armature.animation_data:
            nancy_armature.animation_data_create()
        
        # Limpiar NLA tracks existentes
        while len(nancy_armature.animation_data.nla_tracks) > 0:
            nancy_armature.animation_data.nla_tracks.remove(nancy_armature.animation_data.nla_tracks[0])
        
        # Crear NLA strip para exportación (GLTF solo exporta desde NLA strips)
        nla_track = nancy_armature.animation_data.nla_tracks.new()
        nla_track.name = accion_limpia.name
        nla_strip = nla_track.strips.new(accion_limpia.name, int(frame_start), accion_limpia)
        
        # CRÍTICO: Activar el strip para que se exporte correctamente
        nla_track.mute = False  # No silenciar
        nla_strip.influence = 1.0  # Influencia completa
        nla_strip.mute = False  # No silenciar el strip
        
        # Configurar timeline
        bpy.context.scene.frame_start = int(frame_start)
        bpy.context.scene.frame_end = int(frame_end)
        
        # Exportar GLB final
        bpy.ops.export_scene.gltf(
            filepath=str(archivo_salida),
            export_format='GLB',
            export_animations=True,
            export_nla_strips=True,  # Exportar desde NLA strips
            export_image_format='AUTO'
        )
        
        # Limpiar archivo temporal
        archivo_fbx_temp.unlink()
        
        file_size = archivo_salida.stat().st_size / (1024*1024)
        texturas_finales = len(bpy.data.images)
        
        print(f"   ✅ {file_size:.1f}MB | {texturas_finales} texturas | {len(accion_limpia.fcurves)} FCurves")
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
