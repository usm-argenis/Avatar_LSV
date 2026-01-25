"""
Script FINAL para regenerar archivos de Nancy con:
- Animaciones de Nina transferidas con constraints + bake
- Texturas preservadas (15 de Nancy)  
- Sin animación de piernas (90 FCurves eliminados)

NOTA: Los archivos GLB exportados tendrán NLA tracks que Blender importa como "muted".
Para reproducir correctamente, los visores deben configurar use_nla=False y usar la acción directamente.
"""

import bpy
from pathlib import Path

# Configuración
base_dir = Path(r"C:\Users\andre\OneDrive\Documentos\tesis")
nancy_base = base_dir / "test/output/glb/Nancy/Nancy.glb"
carpeta_entrada = base_dir / "test/output/glb/Nina"
carpeta_salida = base_dir / "test/output/glb/Nancy"

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
print(f"REGENERACIÓN NANCY - Método constraints + bake")
print(f"Archivos a procesar: {len(archivos)}")
print(f"{'='*80}\n")

total_procesados = 0
total_fallidos = 0

for categoria, archivo_nina in archivos:
    animacion = archivo_nina.stem.replace("Nina_resultado_", "")
    
    carpeta_cat = carpeta_salida / categoria
    carpeta_cat.mkdir(parents=True, exist_ok=True)
    archivo_salida = carpeta_cat / f"Nancy_resultado_{animacion}.glb"
    
    print(f"[{total_procesados+1}/{len(archivos)}] {categoria}/{animacion}")
    
    try:
        # Limpiar escena
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # 1. Importar Nancy base (CON TEXTURAS)
        bpy.ops.import_scene.gltf(filepath=str(nancy_base))
        nancy_objs = list(bpy.data.objects)
        nancy_armature = next((obj for obj in nancy_objs if obj.type == 'ARMATURE'), None)
        
        if not nancy_armature:
            raise Exception("No se encontró armature de Nancy")
        
        # 2. Importar Nina con animación
        bpy.ops.import_scene.gltf(filepath=str(archivo_nina))
        nina_objs = [obj for obj in bpy.data.objects if obj not in nancy_objs]
        nina_armature = next((obj for obj in nina_objs if obj.type == 'ARMATURE'), None)
        
        if not nina_armature or not nina_armature.animation_data or not nina_armature.animation_data.action:
            raise Exception("Nina no tiene animación")
        
        action_nina = nina_armature.animation_data.action
        frame_start = int(action_nina.frame_range[0])
        frame_end = int(action_nina.frame_range[1])
        
        # 3. Retarget con constraints + bake
        bpy.context.scene.frame_start = frame_start
        bpy.context.scene.frame_end = frame_end
        bpy.context.view_layer.objects.active = nancy_armature
        
        # Crear constraints Copy Transforms
        for nancy_bone in nancy_armature.pose.bones:
            if nancy_bone.name in nina_armature.pose.bones:
                constraint = nancy_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = nina_armature
                constraint.subtarget = nancy_bone.name
        
        # Bake la animación
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
        
        # 4. Eliminar FCurves de piernas
        if not nancy_armature.animation_data or not nancy_armature.animation_data.action:
            raise Exception("Nancy no tiene animación después del bake")
        
        action_nancy = nancy_armature.animation_data.action
        fcurves_eliminadas = [fc for fc in action_nancy.fcurves if any(bone in fc.data_path for bone in huesos_piernas)]
        for fc in fcurves_eliminadas:
            action_nancy.fcurves.remove(fc)
        
        # 5. Eliminar objetos de Nina
        for obj in nina_objs:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # 6. Limpiar acciones no usadas
        acciones_a_eliminar = [act for act in bpy.data.actions if act != action_nancy]
        for act in acciones_a_eliminar:
            bpy.data.actions.remove(act)
        
        # 7. Limpiar NLA tracks
        if nancy_armature.animation_data:
            while len(nancy_armature.animation_data.nla_tracks) > 0:
                nancy_armature.animation_data.nla_tracks.remove(nancy_armature.animation_data.nla_tracks[0])
        
        # 8. Exportar a GLB
        bpy.ops.export_scene.gltf(
            filepath=str(archivo_salida),
            export_format='GLB',
            export_animations=True,
            export_force_sampling=True,
            export_image_format='AUTO'
        )
        
        file_size = archivo_salida.stat().st_size / (1024*1024)
        texturas_finales = len(bpy.data.images)
        
        print(f"   ✅ {file_size:.1f}MB | {texturas_finales} texturas | {len(action_nancy.fcurves)} FCurves")
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
