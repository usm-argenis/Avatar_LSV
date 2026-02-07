#!/usr/bin/env python3
"""
Script genérico para procesar archivos GLB con Blender
Uso: blender --background --python procesar_glb_carpeta.py -- <ruta_carpeta>
"""
import bpy
import sys
import json
import struct
from pathlib import Path

def leer_glb(ruta_glb):
    """Lee un archivo GLB y retorna el JSON"""
    try:
        with open(ruta_glb, 'rb') as f:
            magic = f.read(4)
            version = struct.unpack('<I', f.read(4))[0]
            length = struct.unpack('<I', f.read(4))[0]
            
            chunk_length = struct.unpack('<I', f.read(4))[0]
            chunk_type = f.read(4)
            json_data = f.read(chunk_length).decode('utf-8')
            
            return json.loads(json_data)
    except:
        return None

def necesita_procesamiento(gltf):
    """Determina si un archivo GLB necesita procesamiento"""
    if not gltf or 'nodes' not in gltf:
        return False
    
    # Verificar si tiene RootNode en Node 0
    if gltf['nodes'][0].get('name') == 'RootNode':
        return True
    
    # Verificar transformaciones del Armature
    for node in gltf['nodes']:
        if node.get('name') == 'Armature':
            rotation = node.get('rotation', [0, 0, 0, 1])
            scale = node.get('scale', [1, 1, 1])
            
            # Si tiene rotación o escala incorrecta
            if rotation != [0, 0, 0, 1] or scale != [1, 1, 1]:
                return True
            break
    
    return False

# Obtener argumentos
argv = sys.argv
argv = argv[argv.index("--") + 1:] if "--" in argv else []

if len(argv) < 1:
    print("\n❌ ERROR: Falta la ruta de la carpeta")
    print("Uso: blender --background --python procesar_glb_carpeta.py -- <ruta_carpeta>")
    sys.exit(1)

carpeta = Path(argv[0])

if not carpeta.exists() or not carpeta.is_dir():
    print(f"\n❌ ERROR: La carpeta no existe: {carpeta}")
    sys.exit(1)

print(f"\n{'='*80}")
print(f"PROCESANDO ARCHIVOS GLB EN: {carpeta}")
print(f"{'='*80}\n")

# Buscar archivos GLB
archivos_glb = list(carpeta.glob("*.glb"))

if not archivos_glb:
    print(f"⚠️  No se encontraron archivos GLB en: {carpeta}")
    sys.exit(0)

print(f"📁 Encontrados {len(archivos_glb)} archivos GLB\n")

# Filtrar archivos que necesitan procesamiento
archivos_a_procesar = []
for glb_file in archivos_glb:
    # Ignorar backups
    if 'backup' in glb_file.name.lower():
        continue
    
    gltf = leer_glb(glb_file)
    if necesita_procesamiento(gltf):
        archivos_a_procesar.append(glb_file)
        print(f"❌ Necesita procesamiento: {glb_file.name}")
    else:
        print(f"✅ Ya correcto: {glb_file.name}")

if not archivos_a_procesar:
    print(f"\n✅ Todos los archivos ya están correctos")
    sys.exit(0)

print(f"\n{'='*80}")
print(f"PROCESANDO {len(archivos_a_procesar)} ARCHIVOS")
print(f"{'='*80}\n")

procesados = 0
errores = 0

for glb_input in archivos_a_procesar:
    glb_output = glb_input
    
    try:
        # Limpiar escena
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar GLB
        bpy.ops.import_scene.gltf(filepath=str(glb_input))
        
        # Buscar Armature
        armature_obj = None
        for obj in bpy.data.objects:
            if obj.type == 'ARMATURE' and obj.name == 'Armature':
                armature_obj = obj
                break
        
        if armature_obj:
            # Asegurarse de que está en modo object
            if bpy.context.mode != 'OBJECT':
                bpy.ops.object.mode_set(mode='OBJECT')
            
            # Seleccionar solo el Armature
            bpy.ops.object.select_all(action='DESELECT')
            armature_obj.select_set(True)
            bpy.context.view_layer.objects.active = armature_obj
            
            # Aplicar las transformaciones
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            
            print(f"✅ Transformaciones aplicadas: {glb_input.name}")
        else:
            print(f"⚠️  No se encontró Armature en: {glb_input.name}")
        
        # Exportar a GLB
        bpy.ops.export_scene.gltf(
            filepath=str(glb_output),
            export_format='GLB',
            use_selection=False,
            export_animations=True,
            export_frame_range=True,
            export_force_sampling=True,
            export_def_bones=False,
            export_optimize_animation_size=False
        )
        
        print(f"   ➜ Exportado: {glb_output.name}")
        procesados += 1
        
    except Exception as e:
        print(f"❌ Error en {glb_input.name}: {str(e)}")
        errores += 1

print(f"\n{'='*80}")
print(f"✅ Procesados: {procesados}")
print(f"❌ Errores: {errores}")
print(f"{'='*80}\n")
