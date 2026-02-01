"""
Script para aplicar animaciones faciales JSON directamente a los archivos GLB de Duvall
Lee los JSON de output/glb/Rostro/ y los aplica a los GLB correspondientes
"""

import bpy
import os
import json
from pathlib import Path

def aplicar_animacion_facial_a_glb(glb_path, json_path):
    """
    Aplica una animación facial JSON a un archivo GLB
    
    Args:
        glb_path: Ruta al archivo GLB
        json_path: Ruta al JSON con la animación facial
    """
    try:
        # Limpiar la escena
        bpy.ops.wm.read_homefile(use_empty=True)
        
        print(f"  Importando GLB...")
        # Importar el GLB
        bpy.ops.import_scene.gltf(filepath=str(glb_path))
        
        # Cargar datos de animación facial
        with open(json_path, 'r', encoding='utf-8') as f:
            facial_data = json.load(f)
        
        # IMPORTANTE: Eliminar/renombrar objetos EMPTY que causan conflictos de nombres
        # Primero, identificar todos los objetos MESH y sus nombres base
        import re
        mesh_nombres = set()
        for obj in bpy.data.objects:
            if obj.type == 'MESH':
                nombre_base = re.sub(r'\.\d+$', '', obj.name)
                mesh_nombres.add(nombre_base)
        
        # Eliminar objetos EMPTY con sufijos que podrían causar conflictos
        objetos_a_eliminar = []
        for obj in bpy.data.objects:
            # Si es EMPTY y tiene sufijo numérico, eliminarlo
            if obj.type != 'MESH' and re.search(r'\.\d+$', obj.name):
                objetos_a_eliminar.append(obj)
            # Si es EMPTY y su nombre base coincide con un MESH, renombrarlo
            elif obj.type != 'MESH' and obj.name in mesh_nombres:
                obj.name = obj.name + "_bone"
        
        # Eliminar objetos vacíos duplicados
        for obj in objetos_a_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # Ahora renombrar los objetos MESH restantes para quitar sufijos
        for obj in bpy.data.objects:
            if obj.type == 'MESH':
                nombre_original = obj.name
                nombre_base = re.sub(r'\.\d+$', '', obj.name)
                if nombre_base != obj.name:
                    obj.name = nombre_base
        
        # Buscar el objeto con la cabeza (Wolf3D_Head)
        head_obj = None
        for obj in bpy.data.objects:
            if 'Wolf3D_Head' in obj.name and obj.type == 'MESH':
                head_obj = obj
                print(f"  Objeto cabeza encontrado: {obj.name}")
                break
        
        if not head_obj:
            print(f"  ⚠️  No se encontró Wolf3D_Head")
            return False
        
        if not head_obj.data.shape_keys:
            print(f"  ⚠️  El objeto no tiene shape keys")
            return False
        
        shape_keys = head_obj.data.shape_keys.key_blocks
        shape_key_names = [sk.name for sk in shape_keys]
        
        print(f"  Shape keys encontrados: {len(shape_key_names)}")
        
        # DEBUG: Mostrar primeros 5 shape keys
        if len(shape_key_names) > 1:
            print(f"  Primeros shape keys: {shape_key_names[1:6]}")
        
        # IMPORTANTE: Usar la acción EXISTENTE del archivo GLB  
        # La animación facial debe agregarse a la misma acción que tiene los movimientos del cuerpo
        action = None
        
        # Buscar la acción existente (debería estar en el Armature)
        if bpy.data.actions:
            # Usar la primera acción encontrada (la del cuerpo)
            action = bpy.data.actions[0]
        
        if not action:
            # Crear acción solo si no existe ninguna
            action = bpy.data.actions.new(name=f"FacialAnimation_{facial_data['word']}")
            if not head_obj.animation_data:
                head_obj.animation_data_create()
            head_obj.animation_data.action = action
            action.use_fake_user = True
        
        # Aplicar shape keys del JSON
        applied_keys = 0
        print(f"  JSON tiene {len(facial_data['shapeKeys'])} shape keys")
        for shape_key_name, frames_data in facial_data['shapeKeys'].items():
            # Verificar si el shape key existe en el modelo
            if shape_key_name not in shape_key_names:
                print(f"    ⚠️  '{shape_key_name}' no existe en el modelo")
                continue
            
            # Crear F-Curve para este shape key apuntando al data del mesh
            # Formato: data.shape_keys.key_blocks["nombre"].value
            data_path = f'data.shape_keys.key_blocks["{shape_key_name}"].value'
            fcurve = action.fcurves.find(data_path)
            if fcurve:
                action.fcurves.remove(fcurve)
            fcurve = action.fcurves.new(data_path)
            
            # Añadir keyframes
            for frame_data in frames_data:
                frame = frame_data['frame']
                value = frame_data['value']
                fcurve.keyframe_points.insert(frame, value)
            
            # Configurar interpolación lineal
            for kf in fcurve.keyframe_points:
                kf.interpolation = 'LINEAR'
            
            applied_keys += 1
        
        print(f"  ✅ Aplicados {applied_keys} shape keys")
        
        # Exportar el GLB modificado
        print(f"  Exportando GLB modificado...")
        bpy.ops.export_scene.gltf(
            filepath=str(glb_path),
            export_format='GLB',
            export_animations=True,
            export_morph=True,
            export_morph_normal=True,
            export_morph_tangent=True
        )
        
        print(f"  ✅ GLB exportado con animaciones faciales")
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def procesar_todos_los_glb():
    """Procesa todos los GLB de Duvall con sus JSONs correspondientes"""
    
    base_dir = Path(__file__).parent
    duvall_dir = base_dir / 'output' / 'glb' / 'Duvall'
    rostro_dir = base_dir / 'output' / 'glb' / 'Rostro'
    
    # Obtener todos los JSONs
    json_files = list(rostro_dir.glob('*.json'))
    
    print(f"Encontrados {len(json_files)} archivos JSON de animaciones faciales")
    print("=" * 70)
    
    procesados = 0
    saltados = 0
    
    for i, json_path in enumerate(json_files, 1):
        word_name = json_path.stem
        print(f"[{i}/{len(json_files)}] {word_name}")
        
        # Buscar el GLB correspondiente
        glb_files = list(duvall_dir.rglob(f"*{word_name}.glb"))
        
        if not glb_files:
            # Intentar sin el prefijo Duvall_resultado_
            glb_files = list(duvall_dir.rglob(f"Duvall_resultado_{word_name}.glb"))
        
        if not glb_files:
            print(f"  ⚠️  No se encontró GLB correspondiente")
            saltados += 1
            continue
        
        glb_path = glb_files[0]
        
        # Aplicar animación facial
        if aplicar_animacion_facial_a_glb(glb_path, json_path):
            procesados += 1
        else:
            saltados += 1
    
    print("=" * 70)
    print(f"✅ Procesados: {procesados}")
    print(f"⚠️  Saltados: {saltados}")
    print("=" * 70)

if __name__ == "__main__":
    procesar_todos_los_glb()
