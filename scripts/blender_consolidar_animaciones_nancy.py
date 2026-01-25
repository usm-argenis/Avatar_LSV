"""
Script para Blender: Consolidar animaciones de Nancy
Autor: Sistema de optimización 3D
Fecha: 2025-12-15

Uso:
1. Abrir Blender
2. Ir a Scripting > Open > Seleccionar este archivo
3. Modificar las rutas en CONFIGURACIÓN
4. Ejecutar (Alt+P o botón Run Script)

Descripción:
- Importa Nancy.glb (modelo base sin animaciones)
- Importa todos los archivos .glb con animaciones de subcarpetas
- Extrae SOLO las animaciones (Actions) sin duplicar mallas
- Las guarda en el proyecto de Nancy con nombres limpios
- Exporta Nancy.glb optimizado con todas las animaciones
"""

import bpy
import os
from pathlib import Path

# ================================
# CONFIGURACIÓN - MODIFICAR AQUÍ
# ================================

# Ruta al modelo base (Nancy sin animaciones)
BASE_MODEL_PATH = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy\Nancy.glb"

# Carpeta raíz donde están las animaciones organizadas en subcarpetas
ANIMATIONS_ROOT = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy"

# Ruta de salida del archivo final
OUTPUT_PATH = r"C:\Users\andre\OneDrive\Documentos\tesis\test\output\glb\Nancy_optimizado.glb"

# Subcarpetas a procesar (dejar vacío [] para procesar todas)
FOLDERS_TO_PROCESS = ["saludos", "tiempo", "dias_semana", "alfabeto", "pronombres", "expresiones", "cortesia", "preguntas"]

# ================================
# FUNCIONES PRINCIPALES
# ================================

def limpiar_escena():
    """Elimina todos los objetos de la escena"""
    print("🧹 Limpiando escena...")
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Limpiar acciones huérfanas
    for action in bpy.data.actions:
        if action.users == 0:
            bpy.data.actions.remove(action)
    
    print("✅ Escena limpia")


def importar_modelo_base():
    """Importa el modelo base Nancy.glb"""
    print(f"📦 Importando modelo base: {BASE_MODEL_PATH}")
    
    if not os.path.exists(BASE_MODEL_PATH):
        raise FileNotFoundError(f"❌ No se encuentra el archivo base: {BASE_MODEL_PATH}")
    
    # Importar GLB
    bpy.ops.import_scene.gltf(filepath=BASE_MODEL_PATH)
    
    # Encontrar el armature (esqueleto)
    armature = None
    for obj in bpy.context.selected_objects:
        if obj.type == 'ARMATURE':
            armature = obj
            break
    
    if not armature:
        raise Exception("❌ No se encontró el Armature en el modelo base")
    
    print(f"✅ Modelo base importado: {armature.name}")
    return armature


def obtener_archivos_animacion():
    """Obtiene lista de archivos .glb con animaciones"""
    print(f"🔍 Buscando archivos de animación en: {ANIMATIONS_ROOT}")
    
    archivos = []
    
    # Buscar en subcarpetas específicas
    for folder in FOLDERS_TO_PROCESS:
        folder_path = os.path.join(ANIMATIONS_ROOT, folder)
        if os.path.exists(folder_path):
            for archivo in os.listdir(folder_path):
                if archivo.endswith('.glb') and 'Nancy_resultado_' in archivo:
                    archivos.append({
                        'path': os.path.join(folder_path, archivo),
                        'categoria': folder,
                        'nombre': archivo.replace('Nancy_resultado_', '').replace('.glb', '')
                    })
    
    print(f"✅ Encontrados {len(archivos)} archivos de animación")
    return archivos


def extraer_animacion(archivo_info, armature_base):
    """Extrae la animación de un archivo .glb y la asigna al armature base"""
    
    filepath = archivo_info['path']
    categoria = archivo_info['categoria']
    nombre = archivo_info['nombre']
    
    print(f"  📥 Procesando: {categoria}/{nombre}")
    
    # Guardar objetos actuales
    objetos_antes = set(bpy.data.objects)
    
    try:
        # Importar archivo con animación
        bpy.ops.import_scene.gltf(filepath=filepath)
        
        # Encontrar el armature importado
        objetos_nuevos = set(bpy.data.objects) - objetos_antes
        armature_importado = None
        
        for obj in objetos_nuevos:
            if obj.type == 'ARMATURE':
                armature_importado = obj
                break
        
        if not armature_importado:
            print(f"    ⚠️  No se encontró armature en {nombre}")
            return False
        
        # Extraer la animación (Action)
        if armature_importado.animation_data and armature_importado.animation_data.action:
            action_original = armature_importado.animation_data.action
            
            # Crear copia de la acción con nombre limpio
            nombre_accion = f"{categoria}_{nombre}"
            action_copia = action_original.copy()
            action_copia.name = nombre_accion
            
            print(f"    ✅ Animación extraída: {nombre_accion}")
            
        else:
            print(f"    ⚠️  No se encontró animación en {nombre}")
        
        # Eliminar objetos importados (solo necesitamos la animación)
        for obj in objetos_nuevos:
            bpy.data.objects.remove(obj, do_unlink=True)
        
        return True
        
    except Exception as e:
        print(f"    ❌ Error procesando {nombre}: {str(e)}")
        return False


def limpiar_acciones_duplicadas():
    """Elimina acciones duplicadas y las renombra correctamente"""
    print("🧹 Limpiando acciones duplicadas...")
    
    acciones_limpias = {}
    
    for action in bpy.data.actions:
        # Remover sufijos .001, .002, etc.
        nombre_base = action.name.split('.')[0]
        
        if nombre_base not in acciones_limpias:
            action.name = nombre_base
            acciones_limpias[nombre_base] = action
        else:
            # Eliminar duplicado
            bpy.data.actions.remove(action)
    
    print(f"✅ {len(acciones_limpias)} acciones únicas guardadas")


def exportar_modelo_final(armature):
    """Exporta el modelo final con todas las animaciones"""
    print(f"💾 Exportando modelo final a: {OUTPUT_PATH}")
    
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    # Seleccionar solo el armature y sus hijos
    bpy.ops.object.select_all(action='DESELECT')
    armature.select_set(True)
    
    # Seleccionar también las mallas hijas
    for obj in bpy.data.objects:
        if obj.parent == armature or obj.type == 'MESH':
            obj.select_set(True)
    
    # Exportar como GLB
    bpy.ops.export_scene.gltf(
        filepath=OUTPUT_PATH,
        export_format='GLB',
        use_selection=True,
        export_animations=True,
        export_apply=False
    )
    
    print(f"✅ Modelo exportado exitosamente")


def mostrar_resumen():
    """Muestra un resumen de las animaciones consolidadas"""
    print("\n" + "="*60)
    print("📊 RESUMEN DE ANIMACIONES CONSOLIDADAS")
    print("="*60)
    
    animaciones_por_categoria = {}
    
    for action in bpy.data.actions:
        nombre = action.name
        categoria = nombre.split('_')[0] if '_' in nombre else "sin_categoria"
        
        if categoria not in animaciones_por_categoria:
            animaciones_por_categoria[categoria] = []
        
        animaciones_por_categoria[categoria].append(nombre)
    
    total = 0
    for categoria, animaciones in sorted(animaciones_por_categoria.items()):
        print(f"\n📁 {categoria.upper()}: {len(animaciones)} animaciones")
        for anim in sorted(animaciones):
            print(f"   - {anim}")
            total += 1
    
    print(f"\n✅ TOTAL: {total} animaciones consolidadas")
    print("="*60 + "\n")


# ================================
# EJECUCIÓN PRINCIPAL
# ================================

def main():
    """Función principal que ejecuta todo el proceso"""
    
    print("\n" + "="*60)
    print("🚀 INICIANDO CONSOLIDACIÓN DE ANIMACIONES NANCY")
    print("="*60 + "\n")
    
    try:
        # Paso 1: Limpiar escena
        limpiar_escena()
        
        # Paso 2: Importar modelo base
        armature_base = importar_modelo_base()
        
        # Paso 3: Obtener archivos de animación
        archivos_animacion = obtener_archivos_animacion()
        
        if not archivos_animacion:
            print("⚠️  No se encontraron archivos de animación")
            return
        
        # Paso 4: Extraer animaciones
        print(f"\n📥 Extrayendo {len(archivos_animacion)} animaciones...\n")
        exitosas = 0
        
        for archivo_info in archivos_animacion:
            if extraer_animacion(archivo_info, armature_base):
                exitosas += 1
        
        print(f"\n✅ {exitosas}/{len(archivos_animacion)} animaciones extraídas correctamente")
        
        # Paso 5: Limpiar duplicados
        limpiar_acciones_duplicadas()
        
        # Paso 6: Exportar modelo final
        exportar_modelo_final(armature_base)
        
        # Paso 7: Mostrar resumen
        mostrar_resumen()
        
        print("🎉 ¡PROCESO COMPLETADO EXITOSAMENTE!")
        print(f"📦 Archivo generado: {OUTPUT_PATH}\n")
        
    except Exception as e:
        print(f"\n❌ ERROR CRÍTICO: {str(e)}\n")
        import traceback
        traceback.print_exc()


# Ejecutar el script
if __name__ == "__main__":
    main()
