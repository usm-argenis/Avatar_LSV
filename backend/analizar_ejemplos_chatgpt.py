import json
from pathlib import Path

# Cargar diccionario actual
data_path = Path(__file__).parent.parent / "scripts" / "data.json"
with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

palabras_existentes = set(data.keys())

# Ejemplos de ChatGPT con glosas LSV
ejemplos = [
    ("Buenos días a todos los presentes.", "BUENOS DÍAS TODOS PRESENTE"),
    ("Gracias por su atención durante la presentación.", "GRACIAS SU ATENCIÓN PRESENTACIÓN"),
    ("Este proyecto busca integrar tecnología y educación.", "PROYECTO ESTE INTEGRAR TECNOLOGÍA EDUCACIÓN"),
    ("Queremos evaluar el impacto social del sistema.", "NOSOTROS EVALUAR IMPACTO SOCIAL SISTEMA"),
    ("La inclusión de estudiantes con discapacidad es esencial.", "INCLUSIÓN ESTUDIANTE DISCAPACIDAD ESENCIAL"),
    ("Este sistema permite traducir señas en tiempo real.", "SISTEMA ESTE PERMITIR TRADUCIR SEÑAS TIEMPO REAL"),
    ("La comunidad universitaria mostró interés en el proyecto.", "COMUNIDAD UNIVERSITARIA MOSTRAR INTERÉS PROYECTO"),
    ("Necesitamos crear un manual de uso para el sistema.", "NECESITAR CREAR MANUAL USO SISTEMA"),
    ("La accesibilidad debe ser una prioridad en la educación.", "ACCESIBILIDAD SER PRIORIDAD EDUCACIÓN"),
    ("Este trabajo considera aspectos lingüísticos y culturales.", "TRABAJO ESTE CONSIDERAR ASPECTO LINGÜÍSTICO CULTURAL"),
    ("Queremos fomentar la participación activa de los estudiantes.", "NOSOTROS FOMENTAR PARTICIPACIÓN ACTIVA ESTUDIANTE"),
    ("Este sistema busca mejorar la comprensión de contenidos académicos.", "SISTEMA ESTE BUSCAR MEJORAR COMPRENSIÓN CONTENIDO ACADÉMICO"),
    ("La implementación requiere planificación y supervisión constante.", "IMPLEMENTACIÓN REQUERIR PLANIFICACIÓN SUPERVISIÓN CONSTANTE"),
    ("Este proyecto ayuda a reducir la brecha comunicativa.", "PROYECTO ESTE AYUDAR REDUCIR BRECHA COMUNICACIÓN"),
    ("Queremos que el sistema sea confiable y fácil de usar.", "NOSOTROS SISTEMA SER CONFIABLE FÁCIL USAR"),
    ("La lengua de señas venezolana es un derecho de todos.", "LENGUA SEÑAS VENEZUELA DERECHO TODOS"),
    ("Este trabajo promueve la equidad en el aprendizaje universitario.", "TRABAJO ESTE PROMOVER EQUIDAD APRENDIZAJE UNIVERSIDAD"),
    ("Necesitamos capacitar a los usuarios antes de la implementación.", "NECESITAR CAPACITAR USUARIO ANTES IMPLEMENTACIÓN"),
    ("Este proyecto integra inteligencia artificial y señas venezolanas.", "PROYECTO ESTE INTEGRAR INTELIGENCIA ARTIFICIAL SEÑAS VENEZUELA"),
    ("La evaluación de resultados permite mejorar el sistema.", "EVALUACIÓN RESULTADO PERMITIR MEJORAR SISTEMA"),
    ("Queremos que los docentes utilicen el sistema correctamente.", "NOSOTROS DOCENTE USAR SISTEMA CORRECTO"),
    ("Este trabajo considera las recomendaciones de la comunidad sorda.", "TRABAJO ESTE CONSIDERAR RECOMENDACIÓN COMUNIDAD SORDA"),
    ("La interacción entre estudiantes se facilita con este sistema.", "INTERACCIÓN ESTUDIANTE FACILITAR SISTEMA ESTE"),
    ("Este proyecto busca promover la inclusión digital.", "PROYECTO ESTE BUSCAR PROMOVER INCLUSIÓN DIGITAL"),
    ("Queremos que todos los estudiantes tengan acceso a la tecnología.", "NOSOTROS ESTUDIANTE TODOS TENER ACCESO TECNOLOGÍA"),
    ("Este sistema integra reconocimiento de gestos y aprendizaje automático.", "SISTEMA ESTE INTEGRAR RECONOCIMIENTO GESTO APRENDIZAJE AUTOMÁTICO"),
    ("La participación activa mejora la comprensión de los contenidos.", "PARTICIPACIÓN ACTIVA MEJORAR COMPRENSIÓN CONTENIDO"),
    ("Este trabajo ayuda a reducir barreras de comunicación en la universidad.", "TRABAJO ESTE AYUDAR REDUCIR BARRERA COMUNICACIÓN UNIVERSIDAD"),
    ("Queremos que la lengua de señas sea visible en todas las aulas.", "NOSOTROS LENGUA SEÑAS SER VISIBLE TODA AULA"),
    ("Este proyecto combina investigación, desarrollo y tecnología.", "PROYECTO ESTE COMBINAR INVESTIGACIÓN DESARROLLO TECNOLOGÍA"),
    ("La evaluación constante garantiza la efectividad del sistema.", "EVALUACIÓN CONSTANTE GARANTIZAR EFECTIVIDAD SISTEMA"),
    ("Este trabajo promueve la inclusión de estudiantes con discapacidad auditiva.", "TRABAJO ESTE PROMOVER INCLUSIÓN ESTUDIANTE DISCAPACIDAD AUDITIVA"),
    ("Queremos crear un sistema intuitivo y fácil de usar.", "NOSOTROS CREAR SISTEMA INTUITIVO FÁCIL USAR"),
    ("Este proyecto tiene un impacto positivo en la comunidad educativa.", "PROYECTO ESTE IMPACTO POSITIVO COMUNIDAD EDUCATIVA"),
    ("La implementación del sistema requiere recursos y planificación.", "IMPLEMENTACIÓN SISTEMA REQUERIR RECURSO PLANIFICACIÓN"),
    ("Este trabajo integra recomendaciones de expertos y comunidad sorda.", "TRABAJO ESTE INTEGRAR RECOMENDACIÓN EXPERTO COMUNIDAD SORDA"),
    ("La accesibilidad digital es fundamental para la inclusión.", "ACCESIBILIDAD DIGITAL FUNDAMENTAL INCLUSIÓN"),
    ("Este sistema permite traducir textos y señas de manera simultánea.", "SISTEMA ESTE PERMITIR TRADUCIR TEXTO SEÑAS SIMULTÁNEO"),
    ("Queremos que el proyecto sea un referente en educación inclusiva.", "NOSOTROS PROYECTO SER REFERENTE EDUCACIÓN INCLUSIVA"),
    ("Este trabajo busca optimizar la comunicación entre estudiantes y docentes.", "TRABAJO ESTE BUSCAR OPTIMIZAR COMUNICACIÓN ESTUDIANTE DOCENTE"),
    ("La lengua de señas es esencial para la participación universitaria.", "LENGUA SEÑAS ESENCIAL PARTICIPACIÓN UNIVERSITARIA"),
    ("Este proyecto facilita la interacción en entornos educativos.", "PROYECTO ESTE FACILITAR INTERACCIÓN ENTORNO EDUCATIVO"),
]

# Extraer todas las palabras únicas de las glosas
todas_palabras_glosa = set()
for _, glosa in ejemplos:
    palabras = glosa.split()
    todas_palabras_glosa.update([p.lower() for p in palabras])

# Identificar palabras faltantes
palabras_faltantes = todas_palabras_glosa - palabras_existentes

print("=" * 80)
print(f"ANÁLISIS DE EJEMPLOS CHATGPT - {len(ejemplos)} frases")
print("=" * 80)
print(f"\nTotal palabras únicas en glosas LSV: {len(todas_palabras_glosa)}")
print(f"Palabras existentes en diccionario: {len(palabras_existentes)}")
print(f"Palabras FALTANTES: {len(palabras_faltantes)}")

# Categorizar palabras faltantes (heurística básica)
verbos_faltantes = []
sustantivos_faltantes = []
adjetivos_faltantes = []
otros_faltantes = []

# Heurística para categorización
verbos_infinitivos = ['integrar', 'evaluar', 'permitir', 'traducir', 'mostrar', 
                      'necesitar', 'considerar', 'fomentar', 'buscar', 'mejorar',
                      'requerir', 'ayudar', 'reducir', 'usar', 'promover', 'capacitar',
                      'facilitar', 'combinar', 'garantizar', 'optimizar']

adjetivos = ['social', 'esencial', 'real', 'universitaria', 'activa', 'académico',
             'constante', 'confiable', 'fácil', 'cultural', 'lingüístico', 'digital',
             'automático', 'visible', 'auditiva', 'intuitivo', 'positivo', 'educativa',
             'fundamental', 'simultáneo', 'inclusiva']

for palabra in sorted(palabras_faltantes):
    if palabra in verbos_infinitivos or palabra == 'ser':
        verbos_faltantes.append(palabra)
    elif palabra in adjetivos:
        adjetivos_faltantes.append(palabra)
    else:
        # Heurística: palabras que terminan en -ión son sustantivos
        if palabra.endswith('ión') or palabra.endswith('ción'):
            sustantivos_faltantes.append(palabra)
        else:
            sustantivos_faltantes.append(palabra)

print("\n" + "=" * 80)
print("PALABRAS FALTANTES POR CATEGORÍA")
print("=" * 80)

print(f"\n📌 VERBOS ({len(verbos_faltantes)}):")
for v in sorted(verbos_faltantes):
    print(f"  - {v}")

print(f"\n📌 SUSTANTIVOS ({len(sustantivos_faltantes)}):")
for s in sorted(sustantivos_faltantes):
    print(f"  - {s}")

print(f"\n📌 ADJETIVOS ({len(adjetivos_faltantes)}):")
for a in sorted(adjetivos_faltantes):
    print(f"  - {a}")

if otros_faltantes:
    print(f"\n📌 OTROS ({len(otros_faltantes)}):")
    for o in sorted(otros_faltantes):
        print(f"  - {o}")

print("\n" + "=" * 80)
print("PALABRAS FALTANTES COMO LISTA (para copiar)")
print("=" * 80)
print("\nLista completa alfabética:")
for p in sorted(palabras_faltantes):
    print(f"{p}", end=", ")
print()

# Generar JSON de ejemplo para agregar al diccionario
print("\n" + "=" * 80)
print("SUGERENCIA: Archivos GLB necesarios")
print("=" * 80)
print("\nArchivos que necesitarías crear o buscar:")
for p in sorted(palabras_faltantes):
    print(f"  {p}.glb")
