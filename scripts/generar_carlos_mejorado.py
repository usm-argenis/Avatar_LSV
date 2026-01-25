"""
Script mejorado para generar animaciones de Carlos desde Ch12
Con manejo de errores y reinicio automático
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
    
    for block in bpy.data.textures:
        if block.users == 0:
            bpy.data.textures.remove(block)
    
    for block in bpy.data.images:
        if block.users == 0:
            bpy.data.images.remove(block)

def renombrar_huesos_ch12(armature):
    """Renombrar huesos de mixamorig4: a mixamorig:"""
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='EDIT')
    
    renombrados = 0
    for bone in armature.data.edit_bones:
        if bone.name.startswith('mixamorig4:'):
            nuevo_nombre = bone.name.replace('mixamorig4:', 'mixamorig:')
            bone.name = nuevo_nombre
            renombrados += 1
    
    bpy.ops.object.mode_set(mode='OBJECT')
    return renombrados

def procesar_animacion(ch12_path, remy_glb_path, output_path):
    """Procesar una animación individual"""
    try:
        limpiar_escena()
        
        # Cargar Ch12
        bpy.ops.import_scene.fbx(filepath=str(ch12_path))
        
        ch12_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                ch12_armature = obj
                break
        
        if not ch12_armature:
            raise Exception("No se encontró armature en Ch12")
        
        # Renombrar huesos
        renombrar_huesos_ch12(ch12_armature)
        
        # Cargar animación de Remy
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
        
        # Crear nueva acción para Ch12
        if not ch12_armature.animation_data:
            ch12_armature.animation_data_create()
        
        nueva_accion = bpy.data.actions.new(name="animacion")
        ch12_armature.animation_data.action = nueva_accion
        
        # Copiar keyframes
        frame_inicio = int(remy_action.frame_range[0])
        frame_fin = int(remy_action.frame_range[1])
        
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
        
        # Eliminar modelo de Remy
        objetos_a_eliminar = []
        for obj in bpy.data.objects:
            if obj.parent == remy_armature or obj == remy_armature:
                objetos_a_eliminar.append(obj)
        
        for obj in objetos_a_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        # Exportar GLB
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
        
        return True, f"Frames: {frame_inicio}-{frame_fin}"
        
    except Exception as e:
        return False, str(e)

def main():
    base_path = Path("C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb")
    ch12_path = base_path / "cc" / "Ch12_nonPBR (1).fbx"
    
    # Cargar progreso
    progress_file = base_path / "progreso_carlos.json"
    if progress_file.exists():
        with open(progress_file, 'r') as f:
            procesados = json.load(f)
    else:
        procesados = []
    
    categorias = ['alfabeto', 'dias_semana', 'tiempo', 'pronombres', 
                  'saludos', 'cortesia', 'preguntas', 'expresiones']
    
    total_procesados = 0
    total_errores = 0
    
    print("=" * 80)
    print("🎬 GENERANDO ANIMACIONES DE CARLOS")
    print("=" * 80)
    print(f"Ya procesados: {len(procesados)}")
    print()
    
    for categoria in categorias:
        remy_cat_path = base_path / "Remy" / categoria
        carlos_cat_path = base_path / "Carlos" / categoria
        
        archivos_remy = sorted(remy_cat_path.glob("Remy_resultado_*.glb"))
        
        print(f"\n📁 {categoria.upper()}")
        print("-" * 80)
        
        for idx, archivo_remy in enumerate(archivos_remy, 1):
            nombre_base = archivo_remy.stem.replace("Remy_resultado_", "")
            archivo_carlos = carlos_cat_path / f"Carlos_resultado_{nombre_base}.glb"
            
            # Saltar si ya se procesó
            if str(archivo_carlos) in procesados:
                print(f"   ⏭️  [{idx:2}/{len(archivos_remy)}] Saltado: {nombre_base}")
                continue
            
            print(f"   🔄 [{idx:2}/{len(archivos_remy)}] Procesando: {nombre_base}")
            
            exito, mensaje = procesar_animacion(ch12_path, archivo_remy, archivo_carlos)
            
            if exito:
                print(f"      ✅ Generado ({mensaje})")
                procesados.append(str(archivo_carlos))
                total_procesados += 1
                
                # Guardar progreso
                with open(progress_file, 'w') as f:
                    json.dump(procesados, f)
            else:
                print(f"      ❌ Error: {mensaje}")
                total_errores += 1
                
                # Guardar progreso incluso en error
                with open(progress_file, 'w') as f:
                    json.dump(procesados, f)
    
    print("\n" + "=" * 80)
    print(f"✅ Procesados: {total_procesados}")
    print(f"❌ Errores: {total_errores}")
    print(f"📁 Total archivos Carlos: {len(procesados)}")
    print("=" * 80)

if __name__ == "__main__":
    main()
