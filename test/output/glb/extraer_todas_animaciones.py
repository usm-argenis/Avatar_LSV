"""
Script maestro para extraer animaciones de TODOS los avatares
Ejecuta los scripts individuales en secuencia
"""

import subprocess
import os

AVATARES = ['Luis', 'Duvall', 'Carlos', 'Nina', 'Remy']

def ejecutar_extraccion(avatar):
    """
    Ejecuta el script de extracción para un avatar específico
    """
    script = f"extraer_animaciones_{avatar.lower()}.py"
    
    if not os.path.exists(script):
        print(f"⚠️  Script no encontrado: {script}")
        return False
    
    print(f"\n{'='*70}")
    print(f"🎬 PROCESANDO: {avatar.upper()}")
    print(f"{'='*70}\n")
    
    try:
        result = subprocess.run(['python', script], check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Error procesando {avatar}: {e}")
        return False

def main():
    print("\n" + "="*70)
    print("🎯 EXTRACCIÓN MASIVA DE ANIMACIONES")
    print("="*70)
    print(f"📂 Avatares a procesar: {', '.join(AVATARES)}")
    print("="*70 + "\n")
    
    resultados = {}
    
    for avatar in AVATARES:
        exito = ejecutar_extraccion(avatar)
        resultados[avatar] = exito
    
    # Resumen final
    print("\n" + "="*70)
    print("📊 RESUMEN FINAL")
    print("="*70)
    
    exitosos = sum(1 for v in resultados.values() if v)
    fallidos = len(AVATARES) - exitosos
    
    for avatar, exito in resultados.items():
        estado = "✅" if exito else "❌"
        print(f"{estado} {avatar}: {'Completado' if exito else 'Fallido'}")
    
    print()
    print(f"✅ Exitosos: {exitosos}/{len(AVATARES)}")
    print(f"❌ Fallidos: {fallidos}/{len(AVATARES)}")
    print()
    
    if exitosos == len(AVATARES):
        print("🎉 ¡Todas las extracciones completadas exitosamente!")
    else:
        print("⚠️  Algunas extracciones fallaron. Revisa los logs arriba.")
    
    print()

if __name__ == "__main__":
    main()
