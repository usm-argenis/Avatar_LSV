"""
Script de prueba simple para verificar que Blender funciona
"""
import bpy
import sys
from pathlib import Path

print("\n" + "=" * 70)
print("✅ PRUEBA DE BLENDER - TODO FUNCIONA CORRECTAMENTE")
print("=" * 70)
print(f"\nVersionar Blender: {bpy.app.version_string}")
print(f"Python: {sys.version}")
print(f"Directorio actual: {Path.cwd()}")
print("\n" + "=" * 70)
print("✅ Sistema funcionando correctamente")
print("=" * 70 + "\n")
