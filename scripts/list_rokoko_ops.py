import bpy

print("\n=== OPERADORES DE ROKOKO DISPONIBLES ===\n")

# Buscar todos los operadores que contienen 'rsl' o 'rokoko'
for op_id in dir(bpy.ops):
    if 'rsl' in op_id.lower() or 'rokoko' in op_id.lower():
        print(f"bpy.ops.{op_id}")
        op_module = getattr(bpy.ops, op_id)
        for subop in dir(op_module):
            if not subop.startswith('_'):
                print(f"  - {subop}")
