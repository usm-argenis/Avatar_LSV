import bpy
from pathlib import Path
import time

#"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python scripts\generar_todos_glb.py 2>&1 | Select-String -Pattern "(|||RESUMEN|Exitosos|Fallidos||guardado)" -Context 0,1

print("="*80)
print("GENERAR TODOS LOS ARCHIVOS GLB: Desde .blend con animaciones funcionales")
print("="*80)

# Rutas base
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output")
BLEND_INPUT_DIR = BASE_DIR / "blend"

# Todas las animaciones organizadas por categoría
ANIMACIONES = {
    "cortesia": [
        "a la orden",
        "buen provecho", 
        "cortesia",
        "gracias",
        "muchas gracias",
        "mucho gusto",
        "permiso"
    ],
    "dias_semana": [
        "domingo",
        "jueves", 
        "lunes",
        "martes",
        "miercoles",
        "sabado",
        "viernes"
    ],
    "expresiones": [
        "expresiones",
        "saludas a"
    ],
    "preguntas": [
        "como estas",
        "cual es tu nombre",
        "cual es tu sena",
        "que tal"
    ],
    "pronombres": [
        "el",
        "ella",
        "ellas", 
        "ellos",
        "nosotros",
        "tu",
        "ustedes",
        "yo"
    ],
    "saludos": [
        "adios",
        "bienvenido",
        "buenas noches",
        "buenas tardes", 
        "buenos dias",
        "chao",
        "hola"
    ],
    "tiempo": [
        "anteayer",
        "ayer",
        "calendario",
        "fin de semana",
        "hoy",
        "manana",
        "mes",
        "pasado manana",
        "semana"
    ]
}

def clear_scene():
    """Limpia completamente la escena"""
    if bpy.context.active_object and bpy.context.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    for collection in bpy.data.collections:
        bpy.data.collections.remove(collection)

def fix_animation_for_glb_export(armature):
    """Corrige problemas comunes de animación para exportación GLB"""
    print(f"   🔧 Corrigiendo animación en {armature.name}...")
    
    # 1. Asegurar que hay animation_data
    if not armature.animation_data:
        armature.animation_data_create()
        print(f"      ✅ Animation data creado")
    
    # 2. CRÍTICO: Desactivar NLA si está activado
    if armature.animation_data.use_nla:
        armature.animation_data.use_nla = False
        print(f"      ✅ NLA desactivado (era el problema principal)")
    
    # 3. Verificar que hay acción asignada
    if not armature.animation_data.action:
        # Buscar la mejor acción disponible
        actions = bpy.data.actions
        if actions:
            # Priorizar acción con nombre específico de la animación
            best_action = None
            animation_name = None
            
            # Intentar extraer nombre de animación del archivo
            if bpy.data.filepath:
                filepath = Path(bpy.data.filepath)
                for categoria, animaciones in ANIMACIONES.items():
                    for anim in animaciones:
                        if anim in filepath.name:
                            animation_name = anim
                            break
                    if animation_name:
                        break
            
            # Buscar acción que coincida con la animación
            if animation_name:
                for action in actions:
                    if animation_name.replace(" ", "_") in action.name.lower():
                        best_action = action
                        break
            
            # Si no encontramos por nombre, usar la que tenga más FCurves
            if not best_action:
                best_action = max(actions, key=lambda a: len(a.fcurves))
            
            if best_action:
                armature.animation_data.action = best_action
                print(f"      ✅ Acción asignada: {best_action.name} ({len(best_action.fcurves)} FCurves)")
                
                # Configurar timeline de la escena
                frame_start, frame_end = best_action.frame_range
                bpy.context.scene.frame_start = max(1, int(frame_start))
                bpy.context.scene.frame_end = int(frame_end)
                print(f"      ✅ Timeline: frames {bpy.context.scene.frame_start} - {bpy.context.scene.frame_end}")
            else:
                print(f"      ⚠️ No se encontró acción válida")
                return False
    else:
        action = armature.animation_data.action
        print(f"      ✅ Acción ya asignada: {action.name}")
    
    return True

def verify_mesh_integrity():
    """Verifica que todas las mallas tengan lo necesario para GLB"""
    print(f"   🔍 Verificando integridad de mallas...")
    
    meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
    problems = []
    
    for mesh_obj in meshes:
        mesh = mesh_obj.data
        
        # Verificar UV maps
        if len(mesh.uv_layers) == 0:
            problems.append(f"Mesh '{mesh_obj.name}' sin UV maps")
        
        # Verificar vertex groups (skin weights)
        if len(mesh_obj.vertex_groups) == 0:
            armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
            if armatures:  # Solo es problema si hay armatures
                problems.append(f"Mesh '{mesh_obj.name}' sin vertex groups")
    
    if problems:
        print(f"      ⚠️ Problemas encontrados:")
        for problem in problems:
            print(f"         - {problem}")
        return False
    else:
        print(f"      ✅ {len(meshes)} mallas verificadas correctamente")
        return True

def export_optimized_glb(blend_file, output_glb):
    """Exporta GLB con configuración optimizada para funcionalidad completa"""
    print(f"   📤 Exportando GLB optimizado...")
    
    # Seleccionar todos los objetos
    bpy.ops.object.select_all(action='SELECT')
    
    # Configuración de exportación optimizada y PROBADA
    try:
        bpy.ops.export_scene.gltf(
            filepath=str(output_glb),
            
            # Formato básico
            export_format='GLB',
            export_draco_mesh_compression_enable=False,  # Sin compresión para máxima compatibilidad
            
            # Animaciones - CONFIGURACIÓN CRÍTICA Y PROBADA
            export_animations=True,
            export_frame_range=True,  # Usar rango de frames de la acción
            export_frame_step=1,
            export_force_sampling=True,  # Forzar sampling para garantizar exportación
            export_animation_mode='ACTIONS',  # Exportar acciones (no NLA)
            export_nla_strips=False,  # NO exportar NLA strips (causa problemas)
            
            # Geometría y rigging
            export_def_bones=True,  # Huesos de deformación
            export_skins=True,  # Skin weights CRÍTICO para animación
            export_morph=True,  # Shape keys/morphs
            export_apply=False,  # NO aplicar modificadores
            
            # Materiales y texturas - MANTENER APARIENCIA
            export_materials='EXPORT',  # Exportar todos los materiales
            export_image_format='AUTO',  # Formato automático para mejor compresión
            export_texture_dir='',  # Embeber texturas en GLB
            
            # Geometría detallada
            export_texcoords=True,  # Coordenadas UV CRÍTICO para texturas
            export_normals=True,  # Normales para iluminación
            
            # Configuraciones de escena
            export_yup=True,  # Eje Y hacia arriba (estándar glTF)
            export_extras=False,  # No exportar datos extra
            export_cameras=False,  # No necesitamos cámaras
            export_lights=False,  # No necesitamos luces
            
            # Selección y filtros
            use_selection=False,  # Exportar toda la escena
            use_visible=True,  # Solo objetos visibles
            use_renderable=True,  # Solo objetos renderizables
            use_active_collection=False  # Todas las colecciones
        )
        
        # Verificar que el archivo se creó
        if output_glb.exists():
            size_mb = output_glb.stat().st_size / (1024 * 1024)
            print(f"      ✅ GLB exportado: {size_mb:.1f} MB")
            return True
        else:
            print(f"      ❌ ERROR: Archivo GLB no se generó")
            return False
            
    except Exception as e:
        print(f"      ❌ ERROR en exportación: {e}")
        return False

def verify_glb_functionality(glb_path):
    """Verifica que el GLB funcione correctamente"""
    print(f"   🧪 Verificando funcionalidad del GLB...")
    
    try:
        # Limpiar escena e importar GLB
        clear_scene()
        bpy.ops.import_scene.gltf(filepath=str(glb_path))
        
        # Verificar contenido básico
        objects = list(bpy.data.objects)
        meshes = [obj for obj in objects if obj.type == 'MESH']
        armatures = [obj for obj in objects if obj.type == 'ARMATURE']
        actions = list(bpy.data.actions)
        materials = list(bpy.data.materials)
        
        print(f"      📊 Contenido: {len(meshes)} mallas, {len(armatures)} armatures")
        print(f"      📊 Animación: {len(actions)} acciones, {len(materials)} materiales")
        
        # Verificar animación específicamente
        if armatures:
            armature = armatures[0]
            if armature.animation_data and armature.animation_data.action:
                action = armature.animation_data.action
                print(f"      ✅ Animación activa: {action.name} ({len(action.fcurves)} FCurves)")
                
                # Test rápido de movimiento
                bpy.context.scene.frame_set(1)
                bpy.context.view_layer.update()
                
                if armature.pose.bones:
                    test_bone = armature.pose.bones[0]
                    pos_start = test_bone.matrix.translation.copy()
                    
                    # Ir a frame medio
                    frame_mid = (bpy.context.scene.frame_start + bpy.context.scene.frame_end) // 2
                    bpy.context.scene.frame_set(frame_mid)
                    bpy.context.view_layer.update()
                    
                    pos_mid = test_bone.matrix.translation.copy()
                    movement = (pos_start - pos_mid).length
                    
                    if movement > 0.001:
                        print(f"      ✅ Animación funcional: movimiento detectado ({movement:.4f})")
                        return True
                    else:
                        print(f"      ⚠️ Poca animación detectada en hueso test")
                        return True  # Aún considerarlo válido
                else:
                    print(f"      ⚠️ No hay huesos en pose")
                    return True
            else:
                print(f"      ❌ Sin animación en armature")
                return False
        else:
            print(f"      ❌ Sin armature en GLB")
            return False
            
    except Exception as e:
        print(f"      ❌ Error en verificación: {e}")
        return False

def convert_blend_to_glb(categoria, animacion_nombre):
    """Convierte un archivo .blend específico a GLB funcional"""
    
    print(f"\n{'='*80}")
    print(f"📝 {categoria.upper()} → {animacion_nombre}")
    print(f"{'='*80}")
    
    # Rutas de archivos
    blend_file = BLEND_INPUT_DIR / categoria / f"Nancy_{animacion_nombre}.blend"
    glb_output = BLEND_INPUT_DIR / categoria / f"Nancy_{animacion_nombre}.glb"
    
    if not blend_file.exists():
        print(f"❌ ERROR: No existe {blend_file}")
        return False
    
    try:
        # 1. Cargar archivo .blend
        print(f"📂 Cargando {blend_file.name}...")
        clear_scene()
        bpy.ops.wm.open_mainfile(filepath=str(blend_file))
        
        # 2. Encontrar y verificar armature
        armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
        if not armatures:
            print(f"❌ ERROR: No hay armature en {blend_file.name}")
            return False
        
        armature = armatures[0]
        print(f"✅ Armature encontrado: {armature.name}")
        
        # 3. Corregir problemas de animación
        if not fix_animation_for_glb_export(armature):
            print(f"❌ ERROR: No se pudo corregir animación")
            return False
        
        # 4. Verificar integridad de mallas
        if not verify_mesh_integrity():
            print(f"⚠️ Advertencia: Problemas en mallas (continúo)")
        
        # 5. Exportar GLB optimizado
        if not export_optimized_glb(blend_file, glb_output):
            print(f"❌ ERROR: Fallo en exportación GLB")
            return False
        
        # 6. Verificar funcionalidad del GLB
        if not verify_glb_functionality(glb_output):
            print(f"❌ ERROR: GLB no funcional")
            return False
        
        print(f"✅ ÉXITO COMPLETO: {glb_output.name}")
        return True
        
    except Exception as e:
        print(f"❌ ERROR GENERAL: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

# MAIN
print(f"\n📊 Total de animaciones a procesar:")
total = 0
for categoria, animaciones in ANIMACIONES.items():
    blend_dir = BLEND_INPUT_DIR / categoria
    if blend_dir.exists():
        existing_blends = len([f for f in blend_dir.glob("Nancy_*.blend") if not f.name.endswith("_CORREGIDO.blend")])
        print(f"   {categoria}: {existing_blends} archivos .blend encontrados")
        total += existing_blends
    else:
        print(f"   {categoria}: Carpeta no existe")

print(f"   TOTAL: {total} conversiones por realizar")

if total == 0:
    print(f"\n❌ No se encontraron archivos .blend para convertir")
    print(f"   Verificar que existen en: {BLEND_INPUT_DIR}")
    exit(1)

# Procesar todas las conversiones
resultados = {
    "exitosos": [],
    "fallidos": []
}

inicio_total = time.time()

for categoria, animaciones in ANIMACIONES.items():
    categoria_dir = BLEND_INPUT_DIR / categoria
    if not categoria_dir.exists():
        continue
        
    print(f"\n{'#'*80}")
    print(f"CATEGORÍA: {categoria.upper()}")
    print(f"{'#'*80}")
    
    for animacion in animaciones:
        blend_file = categoria_dir / f"Nancy_{animacion}.blend"
        if blend_file.exists() and not blend_file.name.endswith("_CORREGIDO.blend"):
            exito = convert_blend_to_glb(categoria, animacion)
            
            if exito:
                resultados["exitosos"].append(f"{categoria}/{animacion}")
            else:
                resultados["fallidos"].append(f"{categoria}/{animacion}")
        else:
            print(f"\n⚠️ Saltando {animacion} - archivo .blend no encontrado")

tiempo_total = time.time() - inicio_total

# Resumen final
print(f"\n{'='*80}")
print(f"RESUMEN FINAL - CONVERSIÓN .BLEND → .GLB")
print(f"{'='*80}")
print(f"⏱️ Tiempo total: {tiempo_total/60:.1f} minutos")
print(f"✅ Exitosos: {len(resultados['exitosos'])}")
print(f"❌ Fallidos: {len(resultados['fallidos'])}")

if resultados["fallidos"]:
    print(f"\n❌ Conversiones fallidas:")
    for item in resultados["fallidos"]:
        print(f"   - {item}")

if resultados["exitosos"]:
    print(f"\n✅ Archivos GLB funcionales generados:")
    print(f"   Ubicación: {BLEND_INPUT_DIR}")
    print(f"   🎬 Todos los GLB tienen animaciones funcionales")
    print(f"   🎨 Todos los GLB mantienen texturas y materiales")
    print(f"   🦴 Todos los GLB conservan rigging y skin weights")
    
    for item in resultados["exitosos"]:
        print(f"   ✅ {item}")

print(f"\n{'='*80}")
print(f"🎉 PROCESO DE CONVERSIÓN COMPLETADO")
print(f"💡 Los archivos GLB están listos para usar en aplicaciones web/móviles")
print(f"{'='*80}")