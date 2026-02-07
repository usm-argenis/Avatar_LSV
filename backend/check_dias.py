import json
from pathlib import Path

d = json.loads(Path('C:/Users/andre/OneDrive/Documentos/tesis/backend/scripts/data.json').read_text(encoding='utf-8'))
dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo', 'dia']

print('Días de la semana en diccionario:')
for dia in dias:
    if dia in d:
        print(f'  {dia}: {d[dia]["categoria"]}')
    else:
        print(f'  {dia}: NO ENCONTRADO')
