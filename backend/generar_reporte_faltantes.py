"""
Generar reporte HTML de palabras faltantes
"""
import json
from pathlib import Path

# Cargar diccionario
data_path = Path('C:/Users/andre/OneDrive/Documentos/tesis/backend/scripts/data.json')
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

# Mapeo
MAPEO_CATEGORIAS = {
    'alfabeto': 'alfabeto',
    'verbos': 'verbos',
    'numero': 'numero',
    'expresiones': 'expresiones',
    'cortesia': 'cortesia',
    'saludos': 'saludos',
    'personas': 'personas',
    'pronombres': 'pronombres',
    'ordinales': 'numeros ordinales',
    'profesiones': 'profesion',
    'adverbios': 'adverbios lugares',
    'viviendas': 'tipos de vivienda',
    'estado_civil': 'estado civil',
    'interrogantes': 'preguntas',
    'preposiciones': 'preposicion',
    'dias_semana': 'dias_semana',
    'tiempo': 'tiempo',
    'lugares': 'lugares',
    'transporte': 'medios transporte',
    'general': 'horario'
}

def obtener_nombre_carpeta(categoria):
    return MAPEO_CATEGORIAS.get(categoria, categoria)

# Verificar archivos
base_path = Path("C:/Users/andre/OneDrive/Documentos/tesis/test/output/glb/Duvall")
avatar = "Duvall"

palabras_faltantes = []

for palabra, info in diccionario.items():
    categoria = info['categoria']
    archivo = info['archivo']
    nombre_carpeta = obtener_nombre_carpeta(categoria)
    ruta_esperada = base_path / nombre_carpeta / f"{avatar}_resultado_{archivo}.glb"
    
    if not ruta_esperada.exists():
        palabras_faltantes.append({
            'palabra': palabra,
            'categoria': categoria,
            'carpeta': nombre_carpeta,
            'archivo': archivo
        })

# Generar HTML
html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Palabras Faltantes - LSV</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        .stats {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }}
        .stat-box {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
        }}
        .stat-value {{
            font-size: 32px;
            font-weight: bold;
        }}
        .stat-label {{
            font-size: 14px;
            opacity: 0.9;
            margin-top: 5px;
        }}
        table {{
            width: 100%;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-collapse: collapse;
        }}
        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
        }}
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #eee;
        }}
        tr:hover {{
            background: #f8f9fa;
        }}
        .prioridad-alta {{
            background: #fff3cd;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
        }}
        .badge-defensa {{
            background: #ff6b6b;
            color: white;
        }}
        .badge-normal {{
            background: #95a5a6;
            color: white;
        }}
    </style>
</head>
<body>
    <h1>📋 Palabras Faltantes en Diccionario LSV</h1>
    
    <div class="stats">
        <h2>📊 Estadísticas</h2>
        <div class="stats-grid">
            <div class="stat-box">
                <div class="stat-value">{len(diccionario)}</div>
                <div class="stat-label">Total Palabras</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">{len(diccionario) - len(palabras_faltantes)}</div>
                <div class="stat-label">Con GLB</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">{len(palabras_faltantes)}</div>
                <div class="stat-label">Sin GLB</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">{((len(diccionario) - len(palabras_faltantes)) / len(diccionario) * 100):.1f}%</div>
                <div class="stat-label">Completado</div>
            </div>
        </div>
    </div>
    
    <h2>❌ Palabras sin Archivo GLB ({len(palabras_faltantes)})</h2>
    <table>
        <thead>
            <tr>
                <th>#</th>
                <th>Palabra</th>
                <th>Categoría</th>
                <th>Carpeta</th>
                <th>Prioridad</th>
            </tr>
        </thead>
        <tbody>
"""

palabras_defensa = ['defensa', 'teg', 'aporte', 'tecnologico', 'integracion', 'comunidad', 
                    'venezuela', 'jurado', 'presentacion', 'traduccion']

for i, item in enumerate(palabras_faltantes, 1):
    es_defensa = item['palabra'] in palabras_defensa
    clase = 'prioridad-alta' if es_defensa else ''
    badge = 'badge-defensa' if es_defensa else 'badge-normal'
    badge_text = '🔴 DEFENSA' if es_defensa else '⚪ Normal'
    
    html += f"""
            <tr class="{clase}">
                <td>{i}</td>
                <td><strong>{item['palabra']}</strong></td>
                <td>{item['categoria']}</td>
                <td>{item['carpeta']}</td>
                <td><span class="badge {badge}">{badge_text}</span></td>
            </tr>
"""

html += """
        </tbody>
    </table>
    
    <div class="stats" style="margin-top: 30px;">
        <h3>💡 Notas</h3>
        <ul>
            <li>🔴 <strong>Prioridad ALTA (DEFENSA):</strong> Necesarias para la presentación de la tesis</li>
            <li>⚪ <strong>Prioridad Normal:</strong> Palabras generales del diccionario</li>
            <li>Las palabras marcadas en amarillo son prioritarias para crear</li>
        </ul>
    </div>
</body>
</html>
"""

# Guardar HTML
output_path = Path('C:/Users/andre/OneDrive/Documentos/tesis/test/palabras_faltantes.html')
output_path.write_text(html, encoding='utf-8')

print(f"✅ Reporte generado: {output_path}")
print(f"📊 Total faltantes: {len(palabras_faltantes)}")
print(f"🔴 Prioridad DEFENSA: {sum(1 for p in palabras_faltantes if p['palabra'] in palabras_defensa)}")
