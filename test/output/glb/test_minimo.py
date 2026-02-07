"""
PRUEBA MINIMA - Solo importar y exportar
Para verificar que el flujo basico funciona
"""

import bpy
import os

RUTA_ORIGEN = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Mujer\Nancy.glb"
RUTA_DESTINO = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\TEST_export.glb"

print("\n" + "="*60)
print("PRUEBA MINIMA - IMPORTAR Y EXPORTAR")
print("="*60)

# 1. Verificar archivo existe
print("\n1. Verificando archivo...")
if not os.path.exists(RUTA_ORIGEN):
    print(f"   ERROR: No existe {RUTA_ORIGEN}")
else:
    print(f"   OK - Archivo existe")

# 2. Limpiar escena
print("\n2. Limpiando escena...")
try:
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    print("   OK - Escena limpia")
except Exception as e:
    print(f"   ERROR: {e}")

# 3. Importar
print("\n3. Importando GLB...")
try:
    result = bpy.ops.import_scene.gltf(filepath=RUTA_ORIGEN)
    print(f"   Resultado: {result}")
    
    # Verificar que importó algo
    objetos = len(bpy.context.scene.objects)
    print(f"   OK - Importado ({objetos} objetos en escena)")
    
    # Listar objetos
    print("\n   Objetos importados:")
    for obj in bpy.context.scene.objects:
        print(f"      - {obj.name} ({obj.type})")
    
except Exception as e:
    print(f"   ERROR: {e}")
    import traceback
    traceback.print_exc()

# 4. Exportar
print("\n4. Exportando GLB de prueba...")
try:
    result = bpy.ops.export_scene.gltf(
        filepath=RUTA_DESTINO,
        export_format='GLB'
    )
    print(f"   Resultado: {result}")
    
    # Verificar que creó el archivo
    if os.path.exists(RUTA_DESTINO):
        tamano = os.path.getsize(RUTA_DESTINO)
        print(f"   OK - Archivo creado: {tamano / 1024 / 1024:.2f} MB")
    else:
        print("   ERROR - Archivo no se creo")
        
except Exception as e:
    print(f"   ERROR: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*60)
print("PRUEBA COMPLETADA")
print("="*60 + "\n")
