"""
Script de verificación para el archivo GLB de Nancy Cortesía
Verifica que se conservaron animaciones, mallas y texturas

Uso: Ejecutar desde Blender para analizar el GLB generado
"""

import bpy
import sys
from pathlib import Path

# Configuración
BASE_PATH = Path(__file__).parent
GLB_PATH = BASE_PATH / "test" / "output" / "blend" / "cortesia" / "Nancy_a la orden_CORREGIDO.glb"

def clear_scene():
    """Limpia la escena de Blender"""
    if bpy.context.active_object and bpy.context.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    for collection in bpy.data.collections:
        bpy.data.collections.remove(collection)

def analyze_glb_content():
    """Analiza el contenido detallado del GLB"""
    print(f"\n📂 Analizando: {GLB_PATH}")
    
    if not GLB_PATH.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {GLB_PATH}")
    
    # Limpiar escena e importar GLB
    clear_scene()
    bpy.ops.import_scene.gltf(filepath=str(GLB_PATH))
    
    print(f"✓ GLB cargado exitosamente")
    print(f"📊 Tamaño del archivo: {GLB_PATH.stat().st_size / 1024:.2f} KB\n")
    
    # Análisis de objetos
    objects = list(bpy.data.objects)
    meshes = [obj for obj in objects if obj.type == 'MESH']
    armatures = [obj for obj in objects if obj.type == 'ARMATURE']
    cameras = [obj for obj in objects if obj.type == 'CAMERA']
    lights = [obj for obj in objects if obj.type == 'LIGHT']
    empties = [obj for obj in objects if obj.type == 'EMPTY']
    
    print("🎯 OBJETOS EN LA ESCENA:")
    print(f"  Total de objetos: {len(objects)}")
    print(f"  Mallas (MESH): {len(meshes)}")
    print(f"  Armatures: {len(armatures)}")
    print(f"  Cámaras: {len(cameras)}")
    print(f"  Luces: {len(lights)}")
    print(f"  Empties: {len(empties)}")
    
    # Detalles de mallas
    print(f"\n🎭 DETALLES DE MALLAS:")
    total_vertices = 0
    total_faces = 0
    
    for mesh_obj in meshes:
        mesh = mesh_obj.data
        vertices = len(mesh.vertices)
        faces = len(mesh.polygons)
        total_vertices += vertices
        total_faces += faces
        
        print(f"  {mesh_obj.name}:")
        print(f"    Vértices: {vertices}")
        print(f"    Caras: {faces}")
        print(f"    Materiales: {len(mesh.materials)}")
        
        # UV maps
        uv_layers = len(mesh.uv_layers)
        if uv_layers > 0:
            print(f"    Mapas UV: {uv_layers}")
        
        # Vertex colors
        vertex_colors = len(mesh.color_attributes)
        if vertex_colors > 0:
            print(f"    Colores de vértice: {vertex_colors}")
    
    print(f"  📊 Total: {total_vertices} vértices, {total_faces} caras")
    
    # Análisis de armatures y animaciones
    print(f"\n🦴 ARMATURES Y ANIMACIONES:")
    
    for armature_obj in armatures:
        armature = armature_obj.data
        bones = len(armature.bones)
        print(f"  {armature_obj.name}:")
        print(f"    Huesos: {bones}")
        
        # Verificar animación
        if armature_obj.animation_data:
            anim_data = armature_obj.animation_data
            
            if anim_data.action:
                action = anim_data.action
                fcurves = len(action.fcurves)
                frame_start, frame_end = action.frame_range
                print(f"    ✅ Animación activa: {action.name}")
                print(f"       FCurves: {fcurves}")
                print(f"       Rango: frame {frame_start:.0f} - {frame_end:.0f}")
                print(f"       Duración: {(frame_end - frame_start):.0f} frames")
                
                # Análisis de huesos animados
                animated_bones = set()
                for fcurve in action.fcurves:
                    if fcurve.data_path.startswith('pose.bones["'):
                        bone_name = fcurve.data_path.split('"')[1]
                        animated_bones.add(bone_name)
                
                print(f"       Huesos animados: {len(animated_bones)}")
                if len(animated_bones) > 0:
                    print(f"       Ejemplos: {', '.join(list(animated_bones)[:5])}")
                    if len(animated_bones) > 5:
                        print(f"       ... y {len(animated_bones) - 5} más")
            else:
                print(f"    ⚠️ No hay animación activa asignada")
                
            # NLA strips
            if anim_data.nla_tracks:
                print(f"    NLA tracks: {len(anim_data.nla_tracks)}")
        else:
            print(f"    ❌ Sin datos de animación")
    
    # Análisis de acciones disponibles
    actions = list(bpy.data.actions)
    if actions:
        print(f"\n🎬 ACCIONES DISPONIBLES:")
        for action in actions:
            fcurves = len(action.fcurves)
            frame_start, frame_end = action.frame_range
            print(f"  {action.name}:")
            print(f"    FCurves: {fcurves}")
            print(f"    Rango: {frame_start:.0f} - {frame_end:.0f}")
    
    # Análisis de materiales
    materials = list(bpy.data.materials)
    print(f"\n🎨 MATERIALES Y TEXTURAS:")
    print(f"  Total de materiales: {len(materials)}")
    
    total_textures = 0
    for material in materials:
        texture_count = 0
        
        if material.use_nodes and material.node_tree:
            # Contar nodos de imagen
            image_nodes = [node for node in material.node_tree.nodes if node.type == 'TEX_IMAGE']
            texture_count = len(image_nodes)
            total_textures += texture_count
            
            print(f"  {material.name}: {texture_count} texturas")
            
            # Mostrar algunas texturas
            for i, node in enumerate(image_nodes[:2]):  # Solo las primeras 2
                if node.image:
                    print(f"    - {node.image.name}")
    
    print(f"  📊 Total de texturas: {total_textures}")
    
    # Análisis de imágenes
    images = list(bpy.data.images)
    print(f"\n🖼️ IMÁGENES:")
    print(f"  Total de imágenes: {len(images)}")
    
    embedded_count = 0
    external_count = 0
    
    for image in images:
        if image.filepath:
            external_count += 1
        else:
            embedded_count += 1
    
    print(f"  Embebidas: {embedded_count}")
    print(f"  Externas: {external_count}")
    
    # Verificación de integridad
    print(f"\n✅ VERIFICACIÓN DE INTEGRIDAD:")
    
    checks = []
    
    # Check 1: Mallas con geometría
    if len(meshes) > 0 and total_vertices > 0:
        checks.append("✅ Geometría: Mallas con vértices encontradas")
    else:
        checks.append("❌ Geometría: No se encontraron mallas válidas")
    
    # Check 2: Materiales
    if len(materials) > 0:
        checks.append("✅ Materiales: Materiales encontrados")
    else:
        checks.append("❌ Materiales: No se encontraron materiales")
    
    # Check 3: Texturas
    if total_textures > 0:
        checks.append("✅ Texturas: Texturas encontradas en materiales")
    else:
        checks.append("❌ Texturas: No se encontraron texturas")
    
    # Check 4: Armature
    if len(armatures) > 0:
        checks.append("✅ Rigging: Armature encontrado")
    else:
        checks.append("❌ Rigging: No se encontró armature")
    
    # Check 5: Animaciones
    animated_armatures = [arm for arm in armatures if arm.animation_data and arm.animation_data.action]
    if len(animated_armatures) > 0:
        checks.append("✅ Animación: Animaciones activas encontradas")
    else:
        checks.append("❌ Animación: No se encontraron animaciones activas")
    
    # Check 6: Acciones
    if len(actions) > 0:
        checks.append("✅ Acciones: Datos de animación disponibles")
    else:
        checks.append("❌ Acciones: No se encontraron datos de animación")
    
    for check in checks:
        print(f"  {check}")
    
    # Puntuación final
    successful_checks = len([c for c in checks if c.startswith("✅")])
    total_checks = len(checks)
    score = (successful_checks / total_checks) * 100
    
    print(f"\n📊 PUNTUACIÓN DE INTEGRIDAD: {score:.1f}% ({successful_checks}/{total_checks})")
    
    if score >= 90:
        print("🎉 EXCELENTE: El GLB conserva casi todo el contenido original")
    elif score >= 70:
        print("👍 BUENO: El GLB conserva la mayoría del contenido")
    elif score >= 50:
        print("⚠️ REGULAR: El GLB tiene algunas pérdidas")
    else:
        print("❌ PROBLEMÁTICO: El GLB tiene pérdidas significativas")
    
    return score >= 70

def main():
    """Función principal"""
    print("\n" + "="*70)
    print("  VERIFICACIÓN DE GLB - NANCY CORTESÍA")
    print("="*70)
    
    try:
        success = analyze_glb_content()
        
        print("\n" + "="*70)
        if success:
            print("  ✅ VERIFICACIÓN EXITOSA ✅")
            print("  El archivo GLB mantiene la integridad del contenido")
        else:
            print("  ⚠️ VERIFICACIÓN CON ADVERTENCIAS ⚠️")
            print("  El archivo GLB puede tener algunas pérdidas")
        print("="*70)
        
        return 0 if success else 1
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        
        print("\n" + "="*70)
        print("  ❌ VERIFICACIÓN FALLIDA ❌")
        print("="*70)
        
        return 1

if __name__ == "__main__":
    exit_code = main()
    if 'bpy' in sys.modules:
        if exit_code == 0:
            print("Verificación completada exitosamente")
        else:
            print("Verificación completada con advertencias")
    else:
        sys.exit(exit_code)