"""
Script para generar animaciones de Carlos UNA POR UNA
Permite verificar cada resultado antes de continuar
"""
import bpy
import sys
from pathlib import Path
import json

def limpiar_escena():
    """Limpiar toda la escena"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)
    
    for block in bpy.data.materials:
        if block.users == 0:
            bpy.data.materials.remove(block)
    
    for block in bpy.data.actions:
        if block.users == 0:
            bpy.data.actions.remove(block)

def renombrar_huesos_ch12(armature):
    """Renombrar huesos de mixamorig4: a mixamorig:"""
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='EDIT')
    
    for bone in armature.data.edit_bones:
        if bone.name.startswith('mixamorig4:'):
            bone.name = bone.name.replace('mixamorig4:', 'mixamorig:')
    
    bpy.ops.object.mode_set(mode='OBJECT')

def procesar_una_animacion(nombre_base):
    """Procesar UNA animación específica"""
    base_path = Path("C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb")
    ch12_path = base_path / "cc" / "Ch12_nonPBR (1).fbx"
    
    # Buscar el archivo de Remy en todas las categorías
    categorias = ['alfabeto', 'dias_semana', 'tiempo', 'pronombres', 
                  'saludos', 'cortesia', 'preguntas', 'expresiones']
    
    remy_glb_path = None
    categoria_encontrada = None
    
    for categoria in categorias:
        path_candidato = base_path / "Remy" / categoria / f"Remy_resultado_{nombre_base}.glb"
        if path_candidato.exists():
            remy_glb_path = path_candidato
            categoria_encontrada = categoria
            break
    
    if not remy_glb_path:
        print(f"❌ Error: No se encontró Remy_resultado_{nombre_base}.glb en ninguna categoría")
        return False
    
    output_path = base_path / "Carlos" / categoria_encontrada / f"Carlos_resultado_{nombre_base}.glb"
    
    print("\n" + "=" * 80)
    print(f"🎬 PROCESANDO: {nombre_base}")
    print("=" * 80)
    print(f"📁 Categoría: {categoria_encontrada}")
    print(f"📥 Origen: {remy_glb_path.name}")
    print(f"📤 Destino: {output_path.name}")
    print()
    
    try:
        limpiar_escena()
        
        # Cargar Ch12
        print("⏳ Cargando Ch12...")
        bpy.ops.import_scene.fbx(filepath=str(ch12_path))
        
        ch12_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                ch12_armature = obj
                break
        
        if not ch12_armature:
            raise Exception("No se encontró armature en Ch12")
        
        print("✅ Ch12 cargado")
        
        # Renombrar huesos
        print("🔄 Renombrando huesos...")
        renombrar_huesos_ch12(ch12_armature)
        print("✅ Huesos renombrados")
        
        # Cargar animación de Remy
        print("⏳ Cargando animación de Remy...")
        bpy.ops.import_scene.gltf(filepath=str(remy_glb_path))
        
        # Buscar armature de Remy
        remy_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != ch12_armature:
                remy_armature = obj
                break
        
        if not remy_armature:
            raise Exception("No se encontró animación de Remy")
        
        if not remy_armature.animation_data or not remy_armature.animation_data.action:
            raise Exception("No se encontró action en Remy")
        
        remy_action = remy_armature.animation_data.action
        print(f"✅ Animación cargada: {remy_action.name}")
        
        # Obtener huesos animados
        huesos_animados = set()
        for fcurve in remy_action.fcurves:
            data_path = fcurve.data_path
            if 'pose.bones[' in data_path:
                start = data_path.find('["') + 2
                end = data_path.find('"]', start)
                if start > 1 and end > start:
                    nombre_hueso = data_path[start:end]
                    huesos_animados.add(nombre_hueso)
        
        print(f"📊 Huesos animados: {len(huesos_animados)}")
        
        # Crear nueva acción para Ch12
        if not ch12_armature.animation_data:
            ch12_armature.animation_data_create()
        
        nueva_accion = bpy.data.actions.new(name=f"animacion_{nombre_base}")
        ch12_armature.animation_data.action = nueva_accion
        
        # Copiar keyframes
        frame_inicio = int(remy_action.frame_range[0])
        frame_fin = int(remy_action.frame_range[1])
        
        print(f"⏳ Copiando {frame_fin - frame_inicio + 1} frames...")
        
        for frame in range(frame_inicio, frame_fin + 1):
            bpy.context.scene.frame_set(frame)
            
            for bone_name in huesos_animados:
                if bone_name in remy_armature.pose.bones and bone_name in ch12_armature.pose.bones:
                    remy_bone = remy_armature.pose.bones[bone_name]
                    ch12_bone = ch12_armature.pose.bones[bone_name]
                    
                    ch12_bone.location = remy_bone.location.copy()
                    ch12_bone.rotation_quaternion = remy_bone.rotation_quaternion.copy()
                    ch12_bone.rotation_euler = remy_bone.rotation_euler.copy()
                    ch12_bone.scale = remy_bone.scale.copy()
                    
                    ch12_bone.keyframe_insert(data_path="location", frame=frame)
                    ch12_bone.keyframe_insert(data_path="rotation_quaternion", frame=frame)
                    ch12_bone.keyframe_insert(data_path="rotation_euler", frame=frame)
                    ch12_bone.keyframe_insert(data_path="scale", frame=frame)
        
        print("✅ Frames copiados")
        
        # Eliminar modelo de Remy
        print("🗑️  Eliminando modelo de Remy...")
        objetos_a_eliminar = []
        for obj in bpy.data.objects:
            if obj.parent == remy_armature or obj == remy_armature:
                objetos_a_eliminar.append(obj)
        
        for obj in objetos_a_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # Exportar GLB
        print("💾 Exportando GLB...")
        bpy.ops.object.select_all(action='DESELECT')
        ch12_armature.select_set(True)
        
        for obj in bpy.data.objects:
            if obj.parent == ch12_armature:
                obj.select_set(True)
        
        bpy.ops.export_scene.gltf(
            filepath=str(output_path),
            use_selection=True,
            export_animations=True,
            export_frame_range=True,
            export_current_frame=False,
            export_nla_strips=False,
            export_def_bones=False
        )
        
        print("\n" + "=" * 80)
        print(f"✅ COMPLETADO: {nombre_base}")
        print("=" * 80)
        print(f"📁 Archivo: {output_path}")
        print(f"🎬 Frames: {frame_inicio} → {frame_fin}")
        print(f"📈 FCurves: {len(nueva_accion.fcurves)}")
        
        return True
        
    except Exception as e:
        print("\n" + "=" * 80)
        print(f"❌ ERROR: {nombre_base}")
        print("=" * 80)
        print(f"Error: {str(e)}")
        return False

# Obtener el nombre de la animación desde argumentos
if len(sys.argv) > 4:  # sys.argv[0] es blender, [1-3] son flags, [4] es el script, [5+] son nuestros args
    nombre = sys.argv[5] if len(sys.argv) > 5 else "hola"
else:
    nombre = "hola"  # Por defecto

procesar_una_animacion(nombre)
