"""
VERIFICAR SI REMY_ALEGRIA.GLB SE CREO
Ejecutar DESPUES de generar_remy_alegria.py
"""

import os

RUTA_ESPERADA = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy_ALEGRIA.glb"

print("\n" + "="*60)
print("VERIFICACION DE ARCHIVO GENERADO")
print("="*60)

print(f"\nBuscando: {RUTA_ESPERADA}")

if os.path.exists(RUTA_ESPERADA):
    tamano = os.path.getsize(RUTA_ESPERADA)
    tamano_mb = tamano / 1024 / 1024
    
    print("\nOK - ARCHIVO ENCONTRADO")
    print(f"   Tamano: {tamano_mb:.2f} MB ({tamano:,} bytes)")
    
    # Obtener fecha de modificacion
    import datetime
    mod_time = os.path.getmtime(RUTA_ESPERADA)
    fecha = datetime.datetime.fromtimestamp(mod_time)
    print(f"   Creado/Modificado: {fecha.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Verificar que no está vacío
    if tamano > 1000:
        print("\nEXITO - El archivo parece valido")
    else:
        print("\nADVERTENCIA - El archivo es muy pequeno, puede estar vacio")
        
else:
    print("\nERROR - ARCHIVO NO ENCONTRADO")
    print("\nPosibles causas:")
    print("1. El script generar_remy_alegria.py no se ejecuto")
    print("2. Hubo un error durante la exportacion")
    print("3. La ruta de salida es incorrecta")
    print("\nVerifica el output de generar_remy_alegria.py")

print("="*60 + "\n")
