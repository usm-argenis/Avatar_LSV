"""
Script para convertir archivos FBX a GLB con compresión Draco
Uso: blender --background --python convertir_fbx_a_glb_draco.py
"""

import bpy
import os
import sys
from pathlib import Path

# Configuración
DIRECTORIO_FBX = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output"
DIRECTORIO_GLB = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb"

# Archivos a convertir
ARCHIVOS_A_CONVERTIR = [
    "Remy_resultado_b.fbx",
    "Remy_resultado_c.fbx",
    "Remy_resultado_d.fbx",
    "Remy_resultado_e.fbx",
    "Leonard_resultado_b.fbx",
    "Leonard_resultado_c.fbx",
    "JH_final.fbx",
]

print("=" * 70)
print("CONVERSIÓN DE FBX A GLB CON COMPRESIÓN DRACO")
print("=" * 70)

# Crear directorio de salida si no existe
Path(DIRECTORIO_GLB).mkdir(parents=True, exist_ok=True)
print(f"\n📁 Directorio de salida: {DIRECTORIO_GLB}")

# Contador de archivos procesados
procesados = 0
errores = 0

for archivo_fbx in ARCHIVOS_A_CONVERTIR:
    ruta_fbx = os.path.join(DIRECTORIO_FBX, archivo_fbx)
    nombre_base = Path(archivo_fbx).stem
    ruta_glb = os.path.join(DIRECTORIO_GLB, f"{nombre_base}.glb")
    
    print(f"\n{'=' * 70}")
    print(f"📦 Procesando: {archivo_fbx}")
    print(f"{'=' * 70}")
    
    # Verificar que el archivo FBX existe
    if not os.path.exists(ruta_fbx):
        print(f"   ❌ ERROR: No se encontró el archivo {ruta_fbx}")
        errores += 1
        continue
    
    try:
        # Limpiar escena
        print("   🧹 Limpiando escena...")
        bpy.ops.wm.read_factory_settings(use_empty=True)
        
        # Importar FBX
        print(f"   📥 Importando FBX...")
        bpy.ops.import_scene.fbx(filepath=ruta_fbx)
        
        # Verificar que se importó algo
        if len(bpy.data.objects) == 0:
            print(f"   ❌ ERROR: No se importaron objetos del FBX")
            errores += 1
            continue
        
        # Mostrar información de lo importado
        meshes = [obj for obj in bpy.data.objects if obj.type == 'MESH']
        armatures = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE']
        
        print(f"   ✓ Importado correctamente:")
        print(f"      - Meshes: {len(meshes)}")
        print(f"      - Armatures: {len(armatures)}")
        
        # Contar vértices y polígonos
        total_vertices = sum(len(mesh.data.vertices) for mesh in meshes)
        total_polygons = sum(len(mesh.data.polygons) for mesh in meshes)
        print(f"      - Vértices totales: {total_vertices:,}")
        print(f"      - Polígonos totales: {total_polygons:,}")
        
        # Exportar a GLB con compresión Draco
        print(f"   📤 Exportando a GLB con compresión Draco...")
        print(f"      - Nivel de compresión: 6")
        print(f"      - Formato: Binary GLB")
        
        bpy.ops.export_scene.gltf(
            filepath=ruta_glb,
            export_format='GLB',  # Binary GLB (un solo archivo)
            
            # Incluir solo lo necesario
            use_selection=False,
            export_cameras=False,
            export_lights=False,
            
            # Geometría
            export_apply=True,  # Aplicar modificadores
            
            # Materiales y texturas
            export_materials='EXPORT',
            export_image_format='AUTO',
            
            # Animación
            export_animations=True,
            export_frame_range=True,
            export_frame_step=1,
            export_force_sampling=True,
            export_nla_strips=True,
            export_def_bones=False,
            export_current_frame=False,
            
            # Compresión Draco (¡CLAVE PARA REDUCIR TAMAÑO!)
            export_draco_mesh_compression_enable=True,
            export_draco_mesh_compression_level=6,  # Nivel 6 (balance entre tamaño y calidad)
            export_draco_position_quantization=14,
            export_draco_normal_quantization=10,
            export_draco_texcoord_quantization=12,
            export_draco_color_quantization=10,
            export_draco_generic_quantization=12,
            
            # Optimización adicional
            export_extras=False,
        )
        
        # Verificar tamaño del archivo generado
        if os.path.exists(ruta_glb):
            tamaño_fbx = os.path.getsize(ruta_fbx) / (1024 * 1024)  # MB
            tamaño_glb = os.path.getsize(ruta_glb) / (1024 * 1024)  # MB
            reduccion = ((tamaño_fbx - tamaño_glb) / tamaño_fbx) * 100
            
            print(f"   ✅ Exportación exitosa:")
            print(f"      - Tamaño original (FBX): {tamaño_fbx:.2f} MB")
            print(f"      - Tamaño comprimido (GLB): {tamaño_glb:.2f} MB")
            print(f"      - Reducción: {reduccion:.1f}%")
            print(f"      - Archivo: {Path(ruta_glb).name}")
            procesados += 1
        else:
            print(f"   ❌ ERROR: No se generó el archivo GLB")
            errores += 1
            
    except Exception as e:
        print(f"   ❌ ERROR al procesar {archivo_fbx}: {str(e)}")
        errores += 1

# Resumen final
print("\n" + "=" * 70)
print("RESUMEN DE CONVERSIÓN")
print("=" * 70)
print(f"✅ Archivos procesados correctamente: {procesados}")
print(f"❌ Archivos con errores: {errores}")
print(f"📁 Archivos GLB guardados en: {DIRECTORIO_GLB}")
print("=" * 70)

if procesados > 0:
    print("\n🎯 Los archivos GLB están listos para usar!")
    print("   - Mucho más ligeros gracias a la compresión Draco")
    print("   - Cargan más rápido en navegadores web")
    print("   - Formato estándar para visualizadores 3D")
else:
    print("\n⚠️ No se procesó ningún archivo correctamente")
