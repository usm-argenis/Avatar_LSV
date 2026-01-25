"""
Script para convertir UNA animación a TODOS los avatares
Considerando las proporciones correctas:
- Luis y Duvall tienen las mismas proporciones (masculino)
- Nina y Nancy tienen las mismas proporciones (femenino)

Uso MODO 1 - Por ruta directa (editar la variable RUTA_ARCHIVO_GLB):
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python scripts\convertir_animacion_todos_avatares.py

Uso MODO 2 - Por argumentos:
"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe" --background --python scripts\convertir_animacion_todos_avatares.py -- "cortesia" "gracias"
"""

import bpy
from pathlib import Path
import sys
import time
import re

# ============================================================================
# CONFIGURACIÓN: Coloca aquí la ruta del archivo GLB fuente
# ============================================================================
RUTA_ARCHIVO_GLB = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Duvall\alfabeto\Duvall_resultado_r.glb"
# ============================================================================

print("="*80)
print("CONVERTIR UNA ANIMACIÓN A TODOS LOS AVATARES")
print("="*80)

# Determinar modo: ruta directa o argumentos
CATEGORIA = None
ANIMACION = None

# Intentar usar la ruta directa primero
if RUTA_ARCHIVO_GLB and RUTA_ARCHIVO_GLB.strip():
    archivo_path = Path(RUTA_ARCHIVO_GLB)
    if archivo_path.exists():
        print(f"\n📂 Modo: Ruta directa")
        print(f"📁 Archivo: {archivo_path}")
        
        # Extraer categoría y animación del path
        # Formato esperado: .../[Avatar]/[categoria]/[Avatar]_resultado_[animacion].glb
        parts = archivo_path.parts
        CATEGORIA = parts[-2]  # Penúltima parte es la categoría
        
        # Extraer nombre de animación del archivo
        filename = archivo_path.stem  # Sin extensión
        # Buscar patrón: [Avatar]_resultado_[animacion]
        match = re.search(r'_resultado_(.+)$', filename)
        if match:
            ANIMACION = match.group(1)
        
        if not CATEGORIA or not ANIMACION:
            print("❌ ERROR: No se pudo extraer categoría/animación de la ruta")
            print(f"   Categoría detectada: {CATEGORIA}")
            print(f"   Animación detectada: {ANIMACION}")
            sys.exit(1)
    else:
        print(f"⚠️ Archivo no existe: {RUTA_ARCHIVO_GLB}")
        print("Intentando modo argumentos...")

# Si no hay ruta válida, usar argumentos de línea de comandos
if not CATEGORIA or not ANIMACION:
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
        if len(argv) >= 2:
            print(f"\n📂 Modo: Argumentos")
            CATEGORIA = argv[0]
            ANIMACION = argv[1]
        else:
            print("❌ ERROR: Faltan argumentos")
            print("Uso: blender --background --python script.py -- <categoria> <animacion>")
            sys.exit(1)
    else:
        print("❌ ERROR: Debes proporcionar categoría y animación o configurar RUTA_ARCHIVO_GLB")
        print("\nOPCIÓN 1: Edita la variable RUTA_ARCHIVO_GLB en el script")
        print("OPCIÓN 2: Usa argumentos: blender --background --python script.py -- cortesia gracias")
        sys.exit(1)

print(f"\n📝 Categoría: {CATEGORIA}")
print(f"📝 Animación: {ANIMACION}")

# Configuración de rutas
BASE_DIR = Path(r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb")
OUTPUT_DIR = BASE_DIR

# Definición de avatares y sus proporciones
# Luis y Duvall = mismo grupo (masculino)
# Nina y Nancy = mismo grupo (femenino)
AVATARES = {
    "Luis": {
        "model": BASE_DIR / "Luis" / "Luis.glb",
        "grupo": "masculino",
        "output_dir": BASE_DIR / "Luis"
    },
    "Duvall": {
        "model": BASE_DIR / "Duvall" / "Duvall.glb",
        "grupo": "masculino",
        "output_dir": BASE_DIR / "Duvall"
    },
    "Nina": {
        "model": BASE_DIR / "Nina" / "Nina.glb",
        "grupo": "femenino",
        "output_dir": BASE_DIR / "Nina"
    },
    "Nancy": {
        "model": BASE_DIR / "Nancy" / "Nancy.glb",
        "grupo": "femenino",
        "output_dir": BASE_DIR / "Nancy"
    }
}

# Buscar la animación fuente (puede estar en cualquier avatar)
def encontrar_animacion_fuente():
    """Busca el archivo de animación fuente en cualquier avatar"""
    for avatar_name, avatar_info in AVATARES.items():
        posible_archivo = avatar_info["output_dir"] / CATEGORIA / f"{avatar_name}_resultado_{ANIMACION}.glb"
        if posible_archivo.exists():
            print(f"✅ Animación fuente encontrada: {avatar_name}")
            return avatar_name, posible_archivo, avatar_info["grupo"]
    
    return None, None, None

# Encontrar archivo fuente
AVATAR_FUENTE, ARCHIVO_FUENTE, GRUPO_FUENTE = encontrar_animacion_fuente()

if not ARCHIVO_FUENTE:
    print(f"❌ ERROR: No se encontró la animación {ANIMACION} en categoría {CATEGORIA}")
    print(f"Buscado en:")
    for avatar_name, avatar_info in AVATARES.items():
        posible = avatar_info["output_dir"] / CATEGORIA / f"{avatar_name}_resultado_{ANIMACION}.glb"
        print(f"   - {posible}")
    sys.exit(1)

print(f"📦 Archivo fuente: {ARCHIVO_FUENTE}")
print(f"👤 Avatar fuente: {AVATAR_FUENTE} (grupo: {GRUPO_FUENTE})")

# ============================================================================
# FUNCIÓN AUXILIAR: ENCONTRAR ACCIÓN CON MOVIMIENTO
# ============================================================================

def encontrar_accion_con_movimiento(armature, actions):
    """Encuentra la acción que tiene movimiento real"""
    
    for action in actions:
        if not armature.animation_data:
            armature.animation_data_create()
        
        armature.animation_data.action = action
        armature.animation_data.use_nla = False
        
        frame_start, frame_end = action.frame_range
        
        # Verificar movimiento en Hips
        if 'Hips' in armature.pose.bones:
            bpy.context.scene.frame_set(int(frame_start))
            bpy.context.view_layer.update()
            
            pos_start = armature.pose.bones['Hips'].matrix.translation.copy()
            
            bpy.context.scene.frame_set(int(frame_end))
            bpy.context.view_layer.update()
            
            pos_end = armature.pose.bones['Hips'].matrix.translation.copy()
            movement = (pos_start - pos_end).length
            
            if movement > 0.001:
                return action
    
    return None

# ============================================================================
# FUNCIÓN PRINCIPAL: RETARGETEAR ANIMACIÓN
# ============================================================================

def retarget_animacion(avatar_destino, avatar_info):
    """Retargetea la animación del avatar fuente al avatar destino"""
    
    print(f"\n{'='*80}")
    print(f"🎯 Retargeting: {AVATAR_FUENTE} → {avatar_destino}")
    print(f"{'='*80}")
    
    # Si es el mismo avatar, solo copiar
    if avatar_destino == AVATAR_FUENTE:
        print(f"   ℹ️ Es el mismo avatar, ya existe")
        return True
    
    # Verificar si tienen las mismas proporciones
    grupo_destino = avatar_info["grupo"]
    mismas_proporciones = (GRUPO_FUENTE == grupo_destino)
    
    print(f"   Grupo fuente: {GRUPO_FUENTE}")
    print(f"   Grupo destino: {grupo_destino}")
    print(f"   Mismas proporciones: {'✅ SÍ' if mismas_proporciones else '❌ NO'}")
    
    if not mismas_proporciones:
        print(f"   ⚠️ ADVERTENCIA: Diferentes proporciones - el resultado puede necesitar ajustes")
    
    # Archivo de salida
    output_file = avatar_info["output_dir"] / CATEGORIA / f"{avatar_destino}_resultado_{ANIMACION}.glb"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        # Limpiar escena
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar modelo destino
        print(f"📦 Importando {avatar_destino}...")
        modelo_destino = avatar_info["model"]
        
        if not modelo_destino.exists():
            print(f"❌ ERROR: No existe el modelo {modelo_destino}")
            return False
        
        bpy.ops.import_scene.gltf(filepath=str(modelo_destino))
        
        destino_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE':
                destino_armature = obj
                destino_armature.name = f"{avatar_destino}_Armature"
                break
        
        if not destino_armature:
            print(f"❌ ERROR: No armature de {avatar_destino}")
            return False
        
        # Limpiar animación previa
        if destino_armature.animation_data:
            destino_armature.animation_data_clear()
        
        # Importar animación fuente
        print(f"🎬 Importando animación de {AVATAR_FUENTE}...")
        bpy.ops.import_scene.gltf(filepath=str(ARCHIVO_FUENTE))
        
        fuente_armature = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj != destino_armature:
                fuente_armature = obj
                fuente_armature.name = f"{AVATAR_FUENTE}_Armature"
                break
        
        if not fuente_armature:
            print(f"❌ ERROR: No armature de {AVATAR_FUENTE}")
            return False
        
        if not fuente_armature.animation_data or not fuente_armature.animation_data.action:
            print(f"❌ ERROR: {AVATAR_FUENTE} no tiene animación")
            return False
        
        fuente_action = fuente_armature.animation_data.action
        frame_start = int(fuente_action.frame_range[0])
        frame_end = int(fuente_action.frame_range[1])
        
        print(f"   Frames: {frame_start} → {frame_end}")
        print(f"   FCurves: {len(fuente_action.fcurves)}")
        
        # Aplicar retargeting con baking
        print(f"🔄 Aplicando retargeting...")
        
        # Configurar frame range
        bpy.context.scene.frame_start = frame_start
        bpy.context.scene.frame_end = frame_end
        
        # Crear constraints Copy Transforms
        bpy.context.view_layer.objects.active = destino_armature
        destino_armature.select_set(True)
        
        constraints_creados = 0
        for destino_bone in destino_armature.pose.bones:
            if destino_bone.name in fuente_armature.pose.bones:
                constraint = destino_bone.constraints.new('COPY_TRANSFORMS')
                constraint.target = fuente_armature
                constraint.subtarget = destino_bone.name
                constraints_creados += 1
        
        print(f"   ✅ {constraints_creados} constraints creados")
        
        # Bake la animación
        print(f"   🔥 Baking animación...")
        start_time = time.time()
        bpy.ops.object.select_all(action='DESELECT')
        destino_armature.select_set(True)
        bpy.context.view_layer.objects.active = destino_armature
        
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
        
        bake_time = time.time() - start_time
        print(f"   ✅ Baking completado: {bake_time:.2f}s")
        
        # Verificar animación
        if not destino_armature.animation_data or not destino_armature.animation_data.action:
            print(f"❌ ERROR: {avatar_destino} no recibió animación")
            return False
        
        destino_action = destino_armature.animation_data.action
        print(f"   ✅ Action: {destino_action.name}")
        print(f"   ✅ FCurves: {len(destino_action.fcurves)}")
        
        # Limpiar acciones múltiples si existen
        all_actions = list(bpy.data.actions)
        if len(all_actions) > 1:
            print(f"   🔍 Encontradas {len(all_actions)} acciones, limpiando...")
            good_action = encontrar_accion_con_movimiento(destino_armature, all_actions)
            
            if good_action:
                # Eliminar acciones inservibles
                actions_to_remove = [a for a in all_actions if a != good_action]
                for action in actions_to_remove:
                    bpy.data.actions.remove(action)
                
                # Asignar la acción correcta
                destino_armature.animation_data.action = good_action
                destino_armature.animation_data.use_nla = False
                print(f"   ✅ Limpieza: {len(actions_to_remove)} acciones eliminadas")
        
        # Verificar movimiento
        bpy.context.scene.frame_set(frame_start)
        bpy.context.view_layer.update()
        
        if "Hips" in destino_armature.pose.bones:
            bone = destino_armature.pose.bones["Hips"]
            pos_start = bone.matrix.translation.copy()
            rot_start = bone.matrix.to_quaternion().copy()
            
            bpy.context.scene.frame_set(frame_end)
            bpy.context.view_layer.update()
            
            pos_end = bone.matrix.translation
            rot_end = bone.matrix.to_quaternion()
            
            pos_diff = (pos_start - pos_end).length
            rot_diff = abs(rot_start.w - rot_end.w) + abs(rot_start.x - rot_end.x) + \
                      abs(rot_start.y - rot_end.y) + abs(rot_start.z - rot_end.z)
            
            print(f"   Hips movimiento: pos={pos_diff:.4f}, rot={rot_diff:.4f}")
            
            if pos_diff > 0.001 or rot_diff > 0.001:
                print(f"   ✅ Animación verificada - hay movimiento")
            else:
                print(f"   ⚠️ Advertencia: Poco movimiento detectado")
        
        # Eliminar objetos del avatar fuente
        objetos_destino = []
        for obj in bpy.data.objects:
            if obj == destino_armature or obj.parent == destino_armature:
                objetos_destino.append(obj)
        
        objetos_eliminar = [obj for obj in bpy.data.objects if obj not in objetos_destino]
        for obj in objetos_eliminar:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        print(f"   🗑️ {len(objetos_eliminar)} objetos fuente eliminados")
        
        # Exportar GLB
        print(f"   📤 Exportando GLB...")
        
        bpy.ops.object.select_all(action='SELECT')
        
        bpy.ops.export_scene.gltf(
            filepath=str(output_file),
            export_format='GLB',
            export_image_format='AUTO',
            export_texcoords=True,
            export_normals=True,
            export_draco_mesh_compression_enable=False,
            export_materials='EXPORT',
            export_cameras=False,
            use_selection=False,
            use_visible=True,
            use_renderable=True,
            use_active_collection=False,
            export_yup=True,
            export_apply=False,
            export_animations=True,
            export_frame_range=True,
            export_frame_step=1,
            export_force_sampling=True,
            export_nla_strips=False,
            export_def_bones=True,
            export_skins=True,
            export_morph=True,
            export_lights=False
        )
        
        if output_file.exists():
            size_kb = output_file.stat().st_size / 1024
            print(f"   💾 GLB guardado: {size_kb:.1f} KB")
            print(f"   ✅ ÉXITO: {output_file.name}")
            return True
        else:
            print(f"   ❌ ERROR: No se generó el archivo")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# MAIN: PROCESAR TODOS LOS AVATARES
# ============================================================================

print(f"\n{'#'*80}")
print(f"PROCESANDO TODOS LOS AVATARES")
print(f"{'#'*80}")

resultados = {
    "exitosos": [],
    "fallidos": []
}

inicio_total = time.time()

for avatar_nombre, avatar_info in AVATARES.items():
    exito = retarget_animacion(avatar_nombre, avatar_info)
    
    if exito:
        resultados["exitosos"].append(avatar_nombre)
    else:
        resultados["fallidos"].append(avatar_nombre)

tiempo_total = time.time() - inicio_total

# ============================================================================
# RESUMEN FINAL
# ============================================================================

print(f"\n{'='*80}")
print(f"RESUMEN FINAL")
print(f"{'='*80}")
print(f"📝 Animación: {CATEGORIA}/{ANIMACION}")
print(f"👤 Avatar fuente: {AVATAR_FUENTE} ({GRUPO_FUENTE})")
print(f"⏱️ Tiempo total: {tiempo_total:.1f} segundos")
print(f"✅ Exitosos: {len(resultados['exitosos'])}/4 avatares")
print(f"❌ Fallidos: {len(resultados['fallidos'])}")

if resultados["exitosos"]:
    print(f"\n✅ Avatares generados:")
    for avatar in resultados["exitosos"]:
        if avatar != AVATAR_FUENTE:  # No mostrar el original
            grupo = AVATARES[avatar]["grupo"]
            output = AVATARES[avatar]["output_dir"] / CATEGORIA / f"{avatar}_resultado_{ANIMACION}.glb"
            print(f"   - {avatar} ({grupo}): {output}")

if resultados["fallidos"]:
    print(f"\n❌ Avatares fallidos:")
    for avatar in resultados["fallidos"]:
        print(f"   - {avatar}")

print(f"\n{'='*80}")
print(f"🎉 PROCESO COMPLETADO")
print(f"{'='*80}")
