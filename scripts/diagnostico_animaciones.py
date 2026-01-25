"""
Script de diagnóstico para archivos .blend con problemas de animación
Identifica y soluciona problemas comunes que impiden la exportación correcta de animaciones

Uso desde Blender:
    1. Abre tu archivo .blend en Blender
    2. Ve a Scripting > Text Editor
    3. Carga este script y ejecuta
    
Uso desde línea de comandos:
    blender archivo.blend --python diagnostico_animaciones.py
"""

import bpy
from pathlib import Path

def print_header(text):
    """Imprime un encabezado formateado"""
    print("\n" + "="*60)
    print(f" {text}")
    print("="*60)

def print_section(text):
    """Imprime una sección"""
    print(f"\n🔍 {text}")
    print("-" * 40)

def check_scene_basics():
    """Verifica información básica de la escena"""
    print_section("INFORMACIÓN BÁSICA DE LA ESCENA")
    
    # Archivo actual
    if bpy.data.filepath:
        filepath = Path(bpy.data.filepath)
        print(f"📁 Archivo: {filepath.name}")
        print(f"📍 Ruta: {filepath.parent}")
    else:
        print("📁 Archivo: Sin guardar")
    
    # Objetos en la escena
    print(f"🎭 Total objetos: {len(bpy.data.objects)}")
    
    # Tipos de objetos
    object_types = {}
    for obj in bpy.data.objects:
        obj_type = obj.type
        object_types[obj_type] = object_types.get(obj_type, 0) + 1
    
    for obj_type, count in object_types.items():
        print(f"   {obj_type}: {count}")
    
    # Rango de frames
    scene = bpy.context.scene
    print(f"📅 Rango de frames: {scene.frame_start} - {scene.frame_end}")
    print(f"📅 Frame actual: {scene.frame_current}")
    print(f"🎬 FPS: {scene.render.fps}")

def check_armatures():
    """Verifica armatures y sus animaciones"""
    print_section("ANÁLISIS DE ARMATURES Y ANIMACIONES")
    
    armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
    
    if not armatures:
        print("❌ NO hay armatures en la escena")
        print("   💡 Para tener animaciones necesitas un armature")
        return False
    
    print(f"🦴 Armatures encontrados: {len(armatures)}")
    
    has_animations = False
    
    for i, armature in enumerate(armatures):
        print(f"\n[{i+1}] Armature: {armature.name}")
        print(f"   🦴 Huesos: {len(armature.data.bones)}")
        
        # Verificar datos de animación
        if not armature.animation_data:
            print(f"   ❌ Sin animation_data")
            continue
            
        anim_data = armature.animation_data
        
        # Acción activa
        if anim_data.action:
            action = anim_data.action
            print(f"   ✅ Acción activa: {action.name}")
            print(f"   📈 FCurves: {len(action.fcurves)}")
            print(f"   📅 Frame range: {int(action.frame_range[0])}-{int(action.frame_range[1])}")
            has_animations = True
            
            # Verificar keyframes
            total_keyframes = 0
            for fcurve in action.fcurves:
                total_keyframes += len(fcurve.keyframe_points)
            print(f"   🔑 Total keyframes: {total_keyframes}")
            
            # Huesos con animación
            animated_bones = set()
            for fcurve in action.fcurves:
                if 'pose.bones[' in fcurve.data_path:
                    bone_name = fcurve.data_path.split('"')[1]
                    animated_bones.add(bone_name)
            
            print(f"   🎭 Huesos animados: {len(animated_bones)}")
            
            if len(animated_bones) == 0:
                print(f"   ⚠️  La acción existe pero no anima huesos")
                
        else:
            print(f"   ❌ Sin acción activa")
        
        # NLA Tracks
        nla_tracks = len(anim_data.nla_tracks) if anim_data.nla_tracks else 0
        print(f"   🎵 NLA Tracks: {nla_tracks}")
    
    return has_animations

def check_actions():
    """Verifica todas las acciones disponibles"""
    print_section("ANÁLISIS DE ACCIONES")
    
    actions = bpy.data.actions
    print(f"🎬 Total acciones: {len(actions)}")
    
    if len(actions) == 0:
        print("❌ NO hay acciones en el archivo")
        print("   💡 Sin acciones no hay animaciones para exportar")
        return False
    
    for i, action in enumerate(actions):
        print(f"\n[{i+1}] Acción: {action.name}")
        print(f"   📈 FCurves: {len(action.fcurves)}")
        print(f"   📅 Frame range: {int(action.frame_range[0])}-{int(action.frame_range[1])}")
        print(f"   👥 Usuarios: {action.users}")
        
        if action.users == 0:
            print(f"   ⚠️  Acción no está siendo usada")
        
        # Analizar FCurves
        if len(action.fcurves) == 0:
            print(f"   ❌ Acción vacía (sin FCurves)")
        else:
            # Tipos de propiedades animadas
            properties = set()
            for fcurve in action.fcurves:
                if 'pose.bones[' in fcurve.data_path:
                    prop = fcurve.data_path.split('.')[-1]
                    properties.add(prop)
            
            print(f"   🎯 Propiedades animadas: {', '.join(properties)}")
    
    return True

def check_materials():
    """Verifica materiales para compatibilidad con glTF"""
    print_section("ANÁLISIS DE MATERIALES (COMPATIBILIDAD glTF)")
    
    materials = bpy.data.materials
    print(f"🎨 Total materiales: {len(materials)}")
    
    if len(materials) == 0:
        print("⚠️  No hay materiales en la escena")
        return True
    
    compatible_materials = 0
    
    for i, mat in enumerate(materials):
        print(f"\n[{i+1}] Material: {mat.name}")
        
        if not mat.use_nodes:
            print(f"   ❌ No usa nodos - incompatible con glTF")
            print(f"   💡 Solución: Convertir a Shader Editor con nodos")
        else:
            # Buscar nodo Principled BSDF
            principled = None
            for node in mat.node_tree.nodes:
                if node.type == 'BSDF_PRINCIPLED':
                    principled = node
                    break
            
            if principled:
                print(f"   ✅ Tiene Principled BSDF")
                compatible_materials += 1
            else:
                print(f"   ❌ Sin Principled BSDF - incompatible con glTF")
                print(f"   💡 Solución: Añadir nodo Principled BSDF")
        
        print(f"   📊 Usuarios: {mat.users}")
        
        if mat.users == 0:
            print(f"   ⚠️  Material no está siendo usado")
    
    print(f"\n📊 Resumen materiales:")
    print(f"   ✅ Compatibles: {compatible_materials}")
    print(f"   ❌ Incompatibles: {len(materials) - compatible_materials}")
    
    return compatible_materials == len(materials)

def check_textures():
    """Verifica texturas e imágenes"""
    print_section("ANÁLISIS DE TEXTURAS E IMÁGENES")
    
    images = bpy.data.images
    print(f"🖼️  Total imágenes: {len(images)}")
    
    if len(images) == 0:
        print("⚠️  No hay texturas en la escena")
        return True
    
    packed_count = 0
    missing_count = 0
    
    for i, img in enumerate(images):
        print(f"\n[{i+1}] Imagen: {img.name}")
        print(f"   📏 Tamaño: {img.size[0]}x{img.size[1]}")
        
        if img.packed_file:
            print(f"   ✅ Empacada en archivo .blend")
            packed_count += 1
        elif img.filepath:
            filepath = Path(img.filepath_abs) if img.filepath_abs else Path(img.filepath)
            if filepath.exists():
                print(f"   📁 Archivo externo: {filepath.name}")
                print(f"   📍 Ruta: {filepath}")
            else:
                print(f"   ❌ Archivo faltante: {img.filepath}")
                missing_count += 1
        else:
            print(f"   🎨 Imagen generada/procedural")
        
        print(f"   👥 Usuarios: {img.users}")
    
    print(f"\n📊 Resumen texturas:")
    print(f"   📦 Empacadas: {packed_count}")
    print(f"   📁 Externas: {len(images) - packed_count - missing_count}")
    print(f"   ❌ Faltantes: {missing_count}")
    
    if missing_count > 0:
        print(f"   💡 Solución: Reemplaza o elimina texturas faltantes")
    
    return missing_count == 0

def suggest_fixes():
    """Sugiere soluciones a problemas comunes"""
    print_section("RECOMENDACIONES Y SOLUCIONES")
    
    print("💡 Para exportar animaciones correctamente a GLB:")
    print()
    print("1. 🦴 ARMATURE Y ANIMACIONES:")
    print("   • Asegúrate de tener un armature en la escena")
    print("   • Verifica que el armature tenga una acción asignada")
    print("   • La acción debe tener keyframes en huesos")
    print("   • Prueba la animación: presiona ESPACIO en Blender")
    print()
    print("2. 🎨 MATERIALES:")
    print("   • Convierte materiales a usar nodos")
    print("   • Usa Principled BSDF como material principal")
    print("   • Evita materiales muy complejos")
    print()
    print("3. 🖼️  TEXTURAS:")
    print("   • Empaca todas las texturas: File > External Data > Pack All")
    print("   • O asegúrate de que las rutas sean correctas")
    print()
    print("4. ⚙️  CONFIGURACIÓN:")
    print("   • Usa export_force_sampling=True en exportación")
    print("   • Exporta solo la acción activa (no NLA strips)")
    print("   • Mantén el rango de frames correcto")
    print()
    print("5. 🔧 HERRAMIENTAS:")
    print("   • Usa export_blend_to_glb.py para exportar")
    print("   • Valida el resultado con test_glb_export.py")
    print("   • Prueba en navegador con test_glb_animation.html")

def main():
    """Función principal de diagnóstico"""
    
    print_header("DIAGNÓSTICO DE ANIMACIONES PARA EXPORTACIÓN GLB")
    
    # Verificaciones básicas
    check_scene_basics()
    
    # Verificar armatures (crítico)
    has_armatures = check_armatures()
    
    # Verificar acciones (crítico)
    has_actions = check_actions()
    
    # Verificar materiales
    materials_ok = check_materials()
    
    # Verificar texturas
    textures_ok = check_textures()
    
    # Resumen final
    print_section("RESUMEN DEL DIAGNÓSTICO")
    
    issues = []
    
    if not has_armatures:
        issues.append("❌ Sin armatures")
    
    if not has_actions:
        issues.append("❌ Sin acciones/animaciones")
    
    if not materials_ok:
        issues.append("⚠️  Materiales incompatibles")
    
    if not textures_ok:
        issues.append("⚠️  Texturas faltantes")
    
    if len(issues) == 0:
        print("🎉 ¡Todo parece estar en orden!")
        print("✅ El archivo debería exportar correctamente a GLB")
        print("💡 Usa export_blend_to_glb.py para exportar")
    else:
        print("💥 Se encontraron problemas:")
        for issue in issues:
            print(f"   {issue}")
        print()
        print("💡 Revisa las recomendaciones anteriores")
    
    # Mostrar sugerencias
    suggest_fixes()

if __name__ == "__main__":
    main()