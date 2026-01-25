"""
Script para organizar archivos de Nina desde avatars/Nina a test/output/glb/Nina
"""
import shutil
from pathlib import Path

# Mapeo de archivos viejos -> nuevos con categorías
palabras_nina = [
    {'viejo': 'a la orden_default.glb', 'nuevo': 'Nina_resultado_a la orden.glb', 'cat': 'cortesia'},
    {'viejo': 'adios_default (1).glb', 'nuevo': 'Nina_resultado_adios.glb', 'cat': 'saludos'},
    {'viejo': 'anteayer_default (1).glb', 'nuevo': 'Nina_resultado_anteayer.glb', 'cat': 'tiempo'},
    {'viejo': 'ayer_default (1).glb', 'nuevo': 'Nina_resultado_ayer.glb', 'cat': 'tiempo'},
    {'viejo': 'bienvenido_default (1).glb', 'nuevo': 'Nina_resultado_bienvenido.glb', 'cat': 'saludos'},
    {'viejo': 'buen provecho_default (1).glb', 'nuevo': 'Nina_resultado_buen provecho.glb', 'cat': 'cortesia'},
    {'viejo': 'buenas noches_default (1).glb', 'nuevo': 'Nina_resultado_buenas noches.glb', 'cat': 'saludos'},
    {'viejo': 'buenas tardes_default (1).glb', 'nuevo': 'Nina_resultado_buenas tardes.glb', 'cat': 'saludos'},
    {'viejo': 'buenos dias_default.glb', 'nuevo': 'Nina_resultado_buenos dias.glb', 'cat': 'saludos'},
    {'viejo': 'calendario_default (1).glb', 'nuevo': 'Nina_resultado_calendario.glb', 'cat': 'tiempo'},
    {'viejo': 'chao_default (1).glb', 'nuevo': 'Nina_resultado_chao.glb', 'cat': 'saludos'},
    {'viejo': 'como estas_default.glb', 'nuevo': 'Nina_resultado_como estas.glb', 'cat': 'preguntas'},
    {'viejo': 'cortesia_default (1).glb', 'nuevo': 'Nina_resultado_cortesia.glb', 'cat': 'cortesia'},
    {'viejo': 'cual es tu nombre_default.glb', 'nuevo': 'Nina_resultado_cual es tu nombre.glb', 'cat': 'preguntas'},
    {'viejo': 'cual es tu sena_default.glb', 'nuevo': 'Nina_resultado_cual es tu sena.glb', 'cat': 'preguntas'},
    {'viejo': 'domingo_default.glb', 'nuevo': 'Nina_resultado_domingo.glb', 'cat': 'dias_semana'},
    {'viejo': 'el_default (1).glb', 'nuevo': 'Nina_resultado_el.glb', 'cat': 'pronombres'},
    {'viejo': 'ella_default (1).glb', 'nuevo': 'Nina_resultado_ella.glb', 'cat': 'pronombres'},
    {'viejo': 'ellas_default (1).glb', 'nuevo': 'Nina_resultado_ellas.glb', 'cat': 'pronombres'},
    {'viejo': 'ellos_default (1).glb', 'nuevo': 'Nina_resultado_ellos.glb', 'cat': 'pronombres'},
    {'viejo': 'expresiones_default.glb', 'nuevo': 'Nina_resultado_expresiones.glb', 'cat': 'expresiones'},
    {'viejo': 'fin de semana_default.glb', 'nuevo': 'Nina_resultado_fin de semana.glb', 'cat': 'tiempo'},
    {'viejo': 'gracias_default (1).glb', 'nuevo': 'Nina_resultado_gracias.glb', 'cat': 'cortesia'},
    {'viejo': 'hola_default (1).glb', 'nuevo': 'Nina_resultado_hola.glb', 'cat': 'saludos'},
    {'viejo': 'hoy_default (1).glb', 'nuevo': 'Nina_resultado_hoy.glb', 'cat': 'tiempo'},
    {'viejo': 'jueves_default (1).glb', 'nuevo': 'Nina_resultado_jueves.glb', 'cat': 'dias_semana'},
    {'viejo': 'lunes_default.glb', 'nuevo': 'Nina_resultado_lunes.glb', 'cat': 'dias_semana'},
    {'viejo': 'manana_default (1).glb', 'nuevo': 'Nina_resultado_manana.glb', 'cat': 'tiempo'},
    {'viejo': 'martes_default.glb', 'nuevo': 'Nina_resultado_martes.glb', 'cat': 'dias_semana'},
    {'viejo': 'mes_default (1).glb', 'nuevo': 'Nina_resultado_mes.glb', 'cat': 'tiempo'},
    {'viejo': 'miercoles_default.glb', 'nuevo': 'Nina_resultado_miercoles.glb', 'cat': 'dias_semana'},
    {'viejo': 'nosotros_default (1).glb', 'nuevo': 'Nina_resultado_nosotros.glb', 'cat': 'pronombres'},
    {'viejo': 'pasado manana_default (1).glb', 'nuevo': 'Nina_resultado_pasado manana.glb', 'cat': 'tiempo'},
    {'viejo': 'permiso_default (1).glb', 'nuevo': 'Nina_resultado_permiso.glb', 'cat': 'cortesia'},
    {'viejo': 'que tal_default.glb', 'nuevo': 'Nina_resultado_que tal.glb', 'cat': 'preguntas'},
    {'viejo': 'sabado_default (1).glb', 'nuevo': 'Nina_resultado_sabado.glb', 'cat': 'dias_semana'},
    {'viejo': 'ustedes_default (1).glb', 'nuevo': 'Nina_resultado_ustedes.glb', 'cat': 'pronombres'},
    {'viejo': 'viernes_default.glb', 'nuevo': 'Nina_resultado_viernes.glb', 'cat': 'dias_semana'},
    {'viejo': 'yo_default (1).glb', 'nuevo': 'Nina_resultado_yo.glb', 'cat': 'pronombres'}
]

origen = Path("C:/Users/andre/OneDrive/Documentos/tesis/avatars/Nina")
destino = Path("C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Nina")

print("=" * 60)
print("ORGANIZANDO ARCHIVOS DE NINA")
print("=" * 60)
print()

copiados = 0
no_encontrados = []

for palabra in palabras_nina:
    src = origen / palabra['viejo']
    categoria_path = destino / palabra['cat']
    dst = categoria_path / palabra['nuevo']
    
    if src.exists():
        # Crear carpeta de categoría si no existe
        categoria_path.mkdir(parents=True, exist_ok=True)
        
        # Copiar archivo
        shutil.copy2(src, dst)
        print(f"✓ {palabra['nuevo']:<45} -> {palabra['cat']}")
        copiados += 1
    else:
        print(f"✗ NO ENCONTRADO: {palabra['viejo']}")
        no_encontrados.append(palabra['viejo'])

print()
print("=" * 60)
print(f"✅ Archivos copiados: {copiados}")
print(f"❌ Archivos no encontrados: {len(no_encontrados)}")
print("=" * 60)

if no_encontrados:
    print("\nArchivos faltantes:")
    for archivo in no_encontrados:
        print(f"  - {archivo}")

# Verificar archivos que ya existen en glb/Nina y no están en avatars/Nina
print("\n" + "=" * 60)
print("VERIFICANDO ARCHIVOS ÚNICOS EN GLB/NINA")
print("=" * 60)
print()

archivos_existentes = set()
for cat in ['cortesia', 'dias_semana', 'expresiones', 'preguntas', 'pronombres', 'saludos', 'tiempo']:
    cat_path = destino / cat
    if cat_path.exists():
        for archivo in cat_path.glob("*.glb"):
            archivos_existentes.add(archivo.name)

archivos_nuevos = set(p['nuevo'] for p in palabras_nina)
archivos_solo_en_glb = archivos_existentes - archivos_nuevos

if archivos_solo_en_glb:
    print("Archivos que YA EXISTEN en glb/Nina (no necesitan copiarse):")
    for archivo in sorted(archivos_solo_en_glb):
        palabra = archivo.replace('Nina_resultado_', '').replace('.glb', '')
        print(f"  ✓ {palabra}")
else:
    print("Todos los archivos de glb/Nina se actualizaron desde avatars/Nina")

print()
print("=" * 60)
print("PROCESO COMPLETADO")
print("=" * 60)
