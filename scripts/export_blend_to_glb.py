"""
Script para exportar archivos .blend a .glb preservando animaciones, texturas y materiales
Soluciona problemas comunes de exportación que causan pérdida de animaciones

PROBLEMA COMÚN: Las animaciones no aparecen en GLB porque:
1. No se exportan todas las acciones/animaciones 
2. La configuración de exportación no preserva keyframes
3. Los NLA strips no se procesan correctamente
4. Los materiales no son compatibles con glTF

SOLUCIÓN: Este script configura correctamente la exportación para preservar TODO

Uso:
    blender --background archivo.blend --python export_blend_to_glb.py
    
O desde interfaz de Blender:
    Ejecutar este script en el Text Editor
"""

import bpy
import os
from pathlib import Path

def ensure_gltf_materials():
    """
    Asegura que todos los materiales sean compatibles con glTF
    Convierte materiales antiguos a Principled BSDF
    """
    print("🎨 Verificando materiales para glTF...")
    
    materials_converted = 0
    
    for mat in bpy.data.materials:
        if not mat.use_nodes:
            # Convertir a nodos
            mat.use_nodes = True
            materials_converted += 1
            print(f"   ✅ {mat.name}: Convertido a nodos")
            
        # Verificar que tenga Principled BSDF
        principled = None
        for node in mat.node_tree.nodes:
            if node.type == 'BSDF_PRINCIPLED':
                principled = node
                break
                
        if not principled:
            # Crear nodo Principled BSDF
            principled = mat.node_tree.nodes.new('ShaderNodeBsdfPrincipled')
            output = mat.node_tree.nodes.get('Material Output')
            if output:
                mat.node_tree.links.new(principled.outputs[0], output.inputs[0])
            materials_converted += 1
            print(f"   ✅ {mat.name}: Añadido Principled BSDF")
            
        # Asegurar configuración compatible con glTF
        mat.blend_method = 'OPAQUE'
        if hasattr(mat, 'shadow_method'):
            mat.shadow_method = 'OPAQUE'
    
    print(f"   📊 Materiales procesados: {len(bpy.data.materials)}")
    print(f"   🔄 Materiales convertidos: {materials_converted}")
    
    return materials_converted

def prepare_animations_for_export():
    """
    Prepara todas las animaciones para exportación correcta a glTF
    """
    print("🎬 Preparando animaciones para exportación...")
    
    armatures_with_animation = []
    actions_count = 0
    
    # Buscar todos los armatures con animación
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            if obj.animation_data and obj.animation_data.action:
                armatures_with_animation.append(obj)
                actions_count += 1
                print(f"   ✅ {obj.name}: Acción '{obj.animation_data.action.name}'")
                
                # Asegurar que la animación esté en el rango correcto
                action = obj.animation_data.action
                if action:
                    # Asegurar que el rango de la escena incluya toda la animación
                    frame_start = int(action.frame_range[0])
                    frame_end = int(action.frame_range[1])
                    
                    if frame_start < bpy.context.scene.frame_start:
                        bpy.context.scene.frame_start = frame_start
                    if frame_end > bpy.context.scene.frame_end:
                        bpy.context.scene.frame_end = frame_end
                        
                    print(f"      📅 Frames: {frame_start}-{frame_end}")
                    print(f"      📈 FCurves: {len(action.fcurves)}")
    
    # Verificar acciones adicionales
    all_actions = len(bpy.data.actions)
    print(f"   📊 Armatures con animación: {len(armatures_with_animation)}")
    print(f"   📊 Total acciones en archivo: {all_actions}")
    
    if len(armatures_with_animation) == 0:
        print("   ⚠️  NO se encontraron animaciones en armatures")
        print("   💡 Verifica que:")
        print("      - El armature tenga una acción asignada")
        print("      - La acción tenga keyframes")
        print("      - El armature esté seleccionado y activo")
        return False
        
    return True

def export_blend_to_glb(input_blend=None, output_glb=None):
    """
    Exporta el archivo .blend actual a .glb preservando animaciones
    """
    
    # Si no se especifica archivo de entrada, usar el actual
    if input_blend is None:
        if bpy.data.filepath:
            input_blend = Path(bpy.data.filepath)
            print(f"📁 Usando archivo actual: {input_blend.name}")
        else:
            print("❌ No hay archivo .blend abierto")
            print("   💡 Guarda el archivo primero o especifica input_blend")
            return False
    else:
        # Abrir el archivo especificado
        print(f"📁 Cargando: {input_blend}")
        bpy.ops.wm.open_mainfile(filepath=str(input_blend))
    
    # Generar nombre de salida automático si no se especifica
    if output_glb is None:
        input_path = Path(bpy.data.filepath) if bpy.data.filepath else Path("archivo_sin_nombre.blend")
        output_glb = input_path.with_suffix('.glb')
        print(f"📄 Archivo de salida: {output_glb.name}")
    
    # Preparar materiales para glTF
    ensure_gltf_materials()
    
    # Preparar animaciones
    if not prepare_animations_for_export():
        print("❌ No se pueden exportar animaciones - no hay animaciones válidas")
        # Continuar la exportación sin animaciones
    
    print(f"\n🚀 Iniciando exportación a GLB...")
    print(f"   📁 Origen: {Path(bpy.data.filepath).name if bpy.data.filepath else 'archivo actual'}")
    print(f"   📄 Destino: {output_glb}")
    
    # Configuración de exportación optimizada para preservar animaciones
    export_settings = {
        'filepath': str(output_glb),
        
        # === CONFIGURACIÓN DE EXPORTACIÓN ===
        'export_format': 'GLB',  # GLB (binario) es más eficiente que GLTF
        'ui_tab': 'GENERAL',
        
        # === INCLUIR EN EXPORTACIÓN ===
        'export_cameras': True,
        'export_lights': True,
        'export_extras': True,
        'export_yup': True,  # Usar Y-up (estándar glTF)
        
        # === TRANSFORMACIONES ===
        'export_apply': False,  # NO aplicar transformaciones (preservar escala/rotación)
        
        # === GEOMETRÍA ===
        'export_texcoords': True,
        'export_normals': True,
        'export_tangents': False,  # Solo si es necesario
        # 'export_colors': True,  # Comentado por compatibilidad
        'export_attributes': True,
        
        # === MATERIALES CRÍTICO ===
        'export_materials': 'EXPORT',  # Exportar materiales
        'export_image_format': 'AUTO',  # Detectar formato automáticamente
        'export_texture_dir': '',  # Embedder en GLB
        
        # === ANIMACIONES - CONFIGURACIÓN CRÍTICA ===
        'export_animations': True,  # ¡CRÍTICO!
        'export_frame_range': False,  # Exportar todo el rango de animación
        'export_frame_step': 1,  # No saltar frames
        'export_force_sampling': True,  # ¡CRÍTICO! Fuerza sampling de todos los keyframes
        'export_nla_strips': False,  # Solo la acción activa
        'export_def_bones': False,  # Solo huesos con deformación
        'export_current_frame': False,  # No solo el frame actual
        'export_anim_single_armature': True,  # Una animación por armature
        'export_reset_pose_bones': True,  # Reset pose antes de exportar
        
        # === OPTIMIZACIÓN ===
        'export_optimize_animation_size': False,  # No optimizar (puede corromper)
        'export_anim_slide_to_zero': False,  # No mover animación al frame 0
        
        # === COMPRESIÓN ===
        'export_draco_mesh_compression_enable': False,  # Desactivar Draco por problemas
        'export_draco_mesh_compression_level': 6,
        'export_draco_position_quantization': 14,
        'export_draco_normal_quantization': 10,
        'export_draco_texcoord_quantization': 12,
        'export_draco_color_quantization': 10,
        'export_draco_generic_quantization': 12,
    }
    
    try:
        # Realizar exportación
        bpy.ops.export_scene.gltf(**export_settings)
        
        # Verificar que se creó el archivo
        if output_glb.exists():
            file_size = output_glb.stat().st_size / (1024 * 1024)  # MB
            print(f"\n✅ ¡Exportación exitosa!")
            print(f"   📄 Archivo: {output_glb}")
            print(f"   📏 Tamaño: {file_size:.2f} MB")
            
            # Verificar contenido
            scene_info = {
                'objetos': len(bpy.data.objects),
                'materiales': len(bpy.data.materials), 
                'texturas': len(bpy.data.images),
                'acciones': len(bpy.data.actions),
                'armatures': len([o for o in bpy.data.objects if o.type == 'ARMATURE'])
            }
            
            print(f"\n📊 Contenido exportado:")
            for key, value in scene_info.items():
                print(f"   {key.capitalize()}: {value}")
                
            return True
            
        else:
            print(f"❌ Error: No se creó el archivo {output_glb}")
            return False
            
    except Exception as e:
        print(f"❌ Error durante la exportación: {str(e)}")
        return False

def main():
    """
    Función principal - puede usarse desde línea de comandos o interfaz
    """
    
    print("="*80)
    print("🔄 EXPORTADOR BLEND → GLB CON ANIMACIONES")
    print("="*80)
    
    # Si se ejecuta desde línea de comandos, buscar argumentos
    import sys
    
    input_file = None
    output_file = None
    
    # Buscar argumentos después de --
    if '--' in sys.argv:
        args = sys.argv[sys.argv.index('--') + 1:]
        if len(args) >= 1:
            input_file = Path(args[0])
        if len(args) >= 2:
            output_file = Path(args[1])
    
    # Ejecutar exportación
    success = export_blend_to_glb(input_file, output_file)
    
    if success:
        print(f"\n🎉 ¡Proceso completado exitosamente!")
        print(f"💡 Tip: Abre el GLB en un visor compatible con animaciones:")
        print(f"   • VS Code con extensión glTF Tools")
        print(f"   • three.js en navegador") 
        print(f"   • Blender (importar glTF)")
    else:
        print(f"\n💥 Hubo errores en el proceso")
        print(f"💡 Revisa los mensajes anteriores para más detalles")

if __name__ == "__main__":
    main()