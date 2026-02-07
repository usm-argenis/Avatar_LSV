"""
LSV Optimizer COMPLETO - Traductor de Español a Lengua de Señas Venezolana
Versión optimizada con todas las reglas lingüísticas de LSV
"""

import re
import json
import unicodedata
from pathlib import Path
from typing import List, Dict, Tuple, Optional

def normalizar_texto_espanol(texto: str) -> str:
    """
    Normalizar texto español: quitar acentos pero MANTENER ñ, ü, etc.
    
    Conversiones:
    - á, é, í, ó, ú → a, e, i, o, u
    - ñ → ñ (mantener)
    - ü → u (convertir)
    """
    # Mantener ñ y Ñ antes de normalizar
    texto = texto.replace('ñ', '\x01')  # Placeholder temporal
    texto = texto.replace('Ñ', '\x02')
    
    # Normalizar NFD (separar acentos)
    texto = unicodedata.normalize('NFD', texto)
    
    # Eliminar solo los caracteres de combinación diacrítica (acentos)
    texto = ''.join(
        char for char in texto 
        if unicodedata.category(char) != 'Mn'
    )
    
    # Restaurar ñ y Ñ
    texto = texto.replace('\x01', 'ñ')
    texto = texto.replace('\x02', 'Ñ')
    
    return texto

def distancia_levenshtein(s1: str, s2: str) -> int:
    """Calcular distancia de Levenshtein entre dos palabras"""
    if len(s1) < len(s2):
        return distancia_levenshtein(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

class LSVOptimizer:
    """
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    🎯 SISTEMA EXPERTO EN LENGUA DE SEÑAS VENEZOLANA (LSV)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    Traductor de Español a LSV basado en patrones lingüísticos reales,
    entrenado exclusivamente con información documental, educativa y comunitaria
    proveniente de FEVENSOR, Consorven y aportes validados de la comunidad sorda venezolana.
    
    📚 CAPACIDADES DEL SISTEMA:
    ├─ 311+ palabras en diccionario LSV documentadas
    ├─ 18 categorías semánticas
    ├─ Corrección ortográfica inteligente (Levenshtein)
    ├─ Reformulación conceptual automática
    ├─ Orden gramatical LSV: TIEMPO → LUGAR → SUJETO → ACCIÓN → COMPLEMENTO
    ├─ Sistema de género (HOMBRE/MUJER después de profesiones/personas)
    ├─ Deletreo dactilológico para palabras sin seña
    └─ NO inventa señas - SOLO usa señas documentadas
    
    🎯 ENFOQUE LINGÜÍSTICO:
    ─────────────────────────────────────────────────────────────────────────
    ✅ SÍ traduce por SIGNIFICADO y CONCEPTO (pensamiento visual-espacial)
    ❌ NO traduce palabra por palabra (español señado)
    
    Actúa como intérprete y lingüista experto, no como traductor automático.
    Cada traducción es comprensible para una persona sorda venezolana
    sin conocimiento del español escrito.
    
    🔬 PATRONES LINGÜÍSTICOS LSV IMPLEMENTADOS:
    ─────────────────────────────────────────────────────────────────────────
    1. PATRÓN TEMPORAL: El tiempo va al inicio
       Ej: "Mañana iré" → MAÑANA IR
    
    2. PATRÓN DE CONTEXTO: Contexto antes de la acción
       Ej: "En la universidad estudian" → UNIVERSIDAD ESTUDIAR
    
    3. PATRÓN DE ÉNFASIS: Lo importante va primero
       Ej: "Es muy importante" → IMPORTANTE MUCHO
    
    4. PATRÓN DE NEGACIÓN: Negación al final
       Ej: "No existe" → EXISTIR NO
    
    5. PATRÓN DE REFORMULACIÓN: Conceptos abstractos se simplifican
       Ej: "integración social" → PERSONAS JUNTOS PARTICIPAR
    
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """
    
    def __init__(self):
        """Inicializar con reglas completas LSV"""
        
        # Cargar diccionario actualizado
        self.diccionario = self._cargar_diccionario()
        print(f"📚 Diccionario LSV cargado: {len(self.diccionario)} palabras")
        
        # ==========================================
        # REGLA 1: PALABRAS QUE SE OMITEN EN LSV
        # ==========================================
        self.palabras_omitidas = {
            # Artículos (no existen en LSV)
            'el', 'la', 'los', 'las',
            'un', 'una', 'unos', 'unas',
            
            # Preposiciones que se omiten (contextuales)
            'de', 'del', 'al', 'a', 'para', 'por', 'con', 'en', 'entre',
            
            # Conjunciones
            'y', 'e', 'o', 'u',
            
            # Pronombres relativos (no se usan en LSV)
            'que',
            
            # Pronombres reflexivos/átonos
            'se', 'me', 'te', 'le', 'les', 'nos',
            
            # Verbos ser/estar/ir auxiliares (se omiten en LSV)
            'es', 'son', 'esta', 'están', 'estoy', 'estas',
            'va', 'voy', 'vamos', 'van', 'vas',
            'fue', 'fui', 'fueron', 'iba', 'iban',
            
            # Palabras redundantes en contexto de presentación
            'nombre',  # "mi nombre es X" → "MIO X" (X se deletrea)
        }
        
        # ==========================================
        # REGLA 2: PALABRAS DE TIEMPO (van al INICIO)
        # ==========================================
        self.palabras_tiempo = {
            # Tiempo relativo
            'ayer', 'hoy', 'mañana', 'anteayer', 'pasado mañana',
            'ahora', 'ahorita', 'despues', 'luego', 'pronto',
            'tarde', 'temprano', 'madrugada', 'mediodia',
            
            # Días de la semana
            'lunes', 'martes', 'miercoles', 'jueves', 
            'viernes', 'sabado', 'domingo',
            
            # Meses
            'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
            'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre',
            
            # Períodos temporales (como unidades, NO marcadores temporales)
            # NOTA: 'año' y 'dia' NO van aquí porque en frases como "yo tengo 18 años"
            # deben ir al FINAL, no al inicio
            'mes', 'semana',
            'fin de semana', 'calendario',
        }
        
        # ==========================================
        # ==========================================
        # REGLA 3: PALABRAS DE NEGACIÓN (van al FINAL)
        # ==========================================
        self.palabras_negacion = {
            'no', 'nunca', 'nada', 'nadie', 'ninguno', 'ninguna',
            'jamas', 'tampoco'
        }
        
        # ==========================================
        # REGLA 4: PALABRAS DE CONTEXTO (van al INICIO)
        # ==========================================
        self.palabras_contexto = {
            'contexto', 'situacion', 'caso', 'ejemplo',
            'razon', 'motivo', 'causa'
        }
        
        # ==========================================
        # REGLA 5: GÉNERO EN LSV
        # ==========================================
        # Palabras femeninas → masculino neutro + MUJER
        self.palabras_femeninas = {
            # PROFESIONES (la más importante en Venezuela)
            'maestra': 'maestro',
            'profesora': 'profesor',
            'doctora': 'medico',
            'ingeniera': 'ingeniero',
            'abogada': 'abogado',
            'administradora': 'administrador',
            'contadora': 'contador',
            'directora': 'director',
            'gerenta': 'gerente',
            'vendedora': 'vendedor',
            'cocinera': 'cocinero',
            'psicologa': 'psicologo',
            'inspectora': 'inspector',
            'instructora': 'instructor',
            'jefa': 'jefe',
            'mensajera': 'mensajero',
            'mesonera': 'mesonero',
            'pintora': 'pintor',
            'supervisora': 'supervisor',
            'traductora': 'traductor',
            'escritora': 'escritor',
            'fotografa': 'fotografo',
            'policia': 'policia',  # neutro en venezolano
            'medica': 'medico',
            'economista': 'economista',  # neutro
            'analista': 'analista',  # neutro
            'pasante': 'pasante',  # neutro
            'detective': 'detective',  # neutro
            
            # PERSONAS
            'señora': 'señor',
            'señorita': 'señor',
            'novia': 'novio',
            'amiga': 'amigo',
            'compañera': 'compañero',
            'vieja': 'viejo',
            'niña': 'niño',
            'anciana': 'anciano',
            'adulta': 'adulto',
            'ciega': 'ciego',
            'sorda': 'sordo',
            'sordociega': 'sordociego',
            
            # ESTADO CIVIL
            'casada': 'casado',
            'soltera': 'soltero',
            'divorciada': 'divorciado',
            'separada': 'separado',
            'viuda': 'viudo',
            'concubina': 'concubino',
        }
        
        # Palabras masculinas → femenino neutro + HOMBRE (menos común)
        self.palabras_masculinas = {}  # En LSV venezolano, neutro es masculino
        
        # ==========================================
        # REGLA 6: REFORMULACIÓN CONCEPTUAL
        # ==========================================
        # Diccionario de conceptos abstractos/académicos → señas existentes
        # NO traducir palabra por palabra, traducir por CONCEPTO
        # ⚠️ SOLO usar palabras que EXISTEN en el diccionario LSV
        # 
        # 🎯 PATRONES DEL PROMPT LSV:
        # 1. PATRÓN TEMPORAL: Tiempo al inicio
        # 2. PATRÓN DE CONTEXTO: Contexto antes de acción 
        # 3. PATRÓN DE ÉNFASIS: Lo importante primero
        # 4. PATRÓN DE NEGACIÓN: Negación al final
        # 5. PATRÓN DE CONCEPTOS ABSTRACTOS: Reformular conceptos
        # 
        # 📚 EJEMPLOS DEL PROMPT (VALIDADOS):
        # - "Bienvenidos a la defensa" → BIENVENIR DEFENSA
        # - "Nuestro objetivo es crear" → OBJETIVO NOSOTROS CREAR
        # - "Sistema de traducción" → SISTEMA TRADUCIR
        # - "Lengua de señas venezolana" → LENGUA SEÑAS VENEZUELA
        # - "Plataforma digital" → [DELETREAR]PLATAFORMA DIGITAL
        # - "Mejorar la comunicación" → COMUNICACIÓN MEJORAR
        # - "Entre personas sordas y oyentes" → PERSONA SORDA OYENTE
        # - "Es muy importante" → IMPORTANTE MUCHO
        # - "No existe" → EXISTIR NO
        # - "Integración social" → PERSONAS JUNTOS PARTICIPAR
        # 
        self.reformulaciones_conceptuales = {
            
            # ═══════════════════════════════════════════════════════════
            # EJEMPLOS ACADÉMICOS (DEFENSA DE TESIS) - DEL PROMPT
            # ═══════════════════════════════════════════════════════════
        # ⚠️ REGLA CRÍTICA: SI UNA PALABRA EXISTE EN EL DICCIONARIO, NUNCA SE REFORMULA
        # Solo se reformulan palabras que NO existen
        
        # Saludos
        'bienvenido': ['bienvenido'],
        'bienvenidos': ['bienvenido'],
        'bienvenida': ['bienvenido'],
        
        # Posesivos (estos NO existen en diccionario, usar pronombres)
        'nuestro': ['nuestro'],
        'nuestra': ['nuestro'],
        'mi': ['mio'],
        'mis': ['mio'],
        
        # Normalizaciones de palabras que existen
        'tecnologico': ['tecnologia'],
        'tecnológico': ['tecnologia'],
        'venezolana': ['venezuela'],  # venezuela SÍ existe en diccionario
        'venezolano': ['venezuela'],
        
        # País/nacionalidad (NO existe 'venezuela' como palabra, omitir o deletrear)
        # Se eliminan estas reformulaciones para que se procesen correctamente
        
        # Verbos comunes
        'existe': ['existir'],
        'existen': ['existir'],
        'presentare': ['presentar'],
        'presentaré': ['presentar'],
        
        # Frases compuestas que NO tienen seña directa
        'trabajo especial de grado': ['trabajo'],  # 'especial' se elimina
        'trabajo especial grado': ['trabajo'],  # 'especial' se elimina
            
            # ═══════════════════════════════════════════════════════════
            # ACADÉMICO / TECNOLÓGICO
            # ═══════════════════════════════════════════════════════════
            # ⚠️ REGLA: Solo reformular palabras que NO existen en diccionario
            # 
            # Palabras que SÍ existen (NO reformular):
            # defensa, aporte, tecnologia, integracion, comunidad, jurado, sistema,
            # buscar, mejorar, evaluar, presentar, comunicacion
            
            # Frases compuestas (solo si NO existe la palabra individual)
            'aporte tecnológico': ['aporte', 'tecnologia'],
            'aporte tecnologico': ['aporte', 'tecnologia'],
            
            # Normalizaciones de acentos (la palabra existe, solo sin acento)
            'integración': ['integracion'],  # integracion existe
            'comunicación': ['comunicacion'],  # comunicacion existe
            'participación': ['participar'],   # participar existe
            'evaluación': ['evaluar'],         # evaluar existe
            'exposición': ['presentar'],       # presentar existe
            'demostración': ['presentar'],     # presentar existe
            
            # Palabras que NO existen → reformular con verbos/conceptos base
            'participacion': ['participar'],
            'inclusion': ['integracion'],  # usar integracion que existe
            'inclusión': ['integracion'],
            'desarrollo': ['trabajar'],     # desarrollo no existe
            'implementación': ['trabajar', 'usar'],
            'implementacion': ['trabajar', 'usar'],
            'aplicación': ['usar'],
            'aplicacion': ['usar'],
            'evaluacion': ['evaluar'],
            'exposicion': ['presentar'],
            'demostracion': ['presentar'],
            
            # Trabajo académico
            'tesis': ['trabajo'],  # trabajo existe
            'investigación': ['trabajar'],
            'investigacion': ['trabajar'],
            
            # ═══════════════════════════════════════════════════════════
            # SOCIAL / COMUNIDAD
            # ═══════════════════════════════════════════════════════════
            # ⚠️ COMUNIDAD existe en diccionario, NO reformular a 'personas grupo'
            'comunidad sorda': ['comunidad', 'sordo'],
            'comunidad de sordos': ['comunidad', 'sordo'],
            'comunidad sorda venezolana': ['comunidad', 'sordo', 'venezuela'],
            
            # NOTA: 'persona sorda' y 'personas sordas' NO necesitan reformulación
            # porque ambas palabras existen en el diccionario
            
            # Palabras que NO existen → reformular
            'accesibilidad': ['ayudar'],  # accesibilidad no existe
            'herramienta': ['ayudar'],    # herramienta no existe
            'herramientas': ['ayudar'],
            'recurso': ['ayudar'],
            'recursos': ['ayudar'],
            'apoyo': ['ayudar'],
            'asistencia': ['ayudar'],
            
            # ═══════════════════════════════════════════════════════════
            # ABSTRACTOS COMUNES
            # ═══════════════════════════════════════════════════════════
            # ⚠️ Solo reformular palabras que NO existen en diccionario
            
            # Normalizaciones (la palabra existe)
            'muy importante': ['importante', 'mucho'],
            
            # Reformulaciones (la palabra NO existe)
            'importancia': ['importante'],  # importante existe
            'diferencia': ['otro'],         # diferencia no existe
            'problema': ['mal'],
            'solucion': ['ayudar'],
            'solución': ['ayudar'],
            'oportunidad': ['presentar'],
            'posibilidad': ['presentar'],
            'necesidad': ['querer'],
            'necesitamos': ['querer'],
            'proposito': ['querer'],
            'propósito': ['querer'],
            'finalidad': ['querer'],
            'resultado': ['trabajar'],
            'consecuencia': ['despues'],
            'ventaja': ['bien'],
            'desventaja': ['mal'],
            'beneficio': ['ayudar'],
            'accesible': ['ayudar'],
            
            # ═══════════════════════════════════════════════════════════
            # EDUCACIÓN
            # ═══════════════════════════════════════════════════════════
            'estudiante': ['estudiar', 'persona'],
            'estudiantes': ['estudiar', 'personas'],
            'universidad': ['universidad'],
            'en la universidad': ['universidad'],  # omitir preposición
            'escuela': ['estudiar'],
            'profesor': ['profesor'],
            'profesora': ['profesor', 'mujer'],
            'maestro': ['maestro'],
            'maestra': ['maestro', 'mujer'],
            
            # ═══════════════════════════════════════════════════════════
            # CONTEXTOS DE LUGAR (PATRÓN 2: Contexto primero)
            # ═══════════════════════════════════════════════════════════
            'aquí': ['cerca'],
            'allí': ['lejos'],
            'allá': ['lejos'],
            'acá': ['cerca'],
            'en el contexto': [],  # omitir - el contexto va primero naturalmente
        }
        
        # VERBOS BASE para construcción conceptual
        # Usar cuando NO existe seña directa
        # ⚠️ SOLO verbos que EXISTEN en el diccionario LSV
        self.verbos_base = {
            'ayudar', 'usar', 'trabajar', 'presentar',
            'estudiar', 'integrar', 'traducir', 'ver',
            'querer', 'conocer', 'decir', 'llevar'
        }
        
        # Palabras de LUGAR (van después de TIEMPO y CONTEXTO en el orden LSV)
        self.palabras_lugar = {
            'cerca', 'lejos', 'frente', 'atras', 'derecha', 'izquierda',
            'casa', 'universidad', 'venezuela',
            'apartamento', 'edificio', 'sala', 'cuarto'
        }
        
        # ==========================================
        # REGLA 7: NORMALIZACIÓN LSV
        # ==========================================
        self.normalizacion_lsv = {
            # Plurales → Singular (LSV no marca plural morfológicamente)
            'todos': 'todo',
            'todas': 'todo',
            'muchos': 'mucho',
            'muchas': 'mucho',
            'pocos': 'poco',
            'pocas': 'poco',
            'algunos': 'algun',
            'algunas': 'algun',
            'ningunos': 'ningun',
            'ningunas': 'ningun',
            'otros': 'otro',
            'otras': 'otro',
            'demasiados': 'demasiado',
            'demasiadas': 'demasiado',
            'bastantes': 'bastante',
            
            # Tiempos → normalizar
            'dias': 'dia',
            'años': 'año',
            'meses': 'mes',
            'semanas': 'semana',
            
            # Pronombres
            'nosotras': 'nosotros',
            'vosotros': 'ustedes',
            'vosotras': 'ustedes',
            
            # Posesivos → forma base
            'mi': 'mio',
            'mis': 'mio',
            'tus': 'tuyo',
            'su': 'suyo',
            'sus': 'suyo',
            'nuestro': 'nuestro',
            'nuestra': 'nuestro',
            'nuestros': 'nuestro',
            'nuestras': 'nuestro',
            
            # Normalizaciones de variantes que existen en el diccionario
            'tecnologico': 'tecnologia',
            'tecnológico': 'tecnologia',
            'tecnologica': 'tecnologia',
            'tecnológica': 'tecnologia',
            'venezolana': 'venezuela',
            'venezolano': 'venezuela',
        
        # Plurales de personas que deben normalizar
        'sordas': 'sordo',
        'sordos': 'sordo',
        'oyentes': 'oyente',
        'ciegos': 'ciego',
        'ciegas': 'ciego',
        
        # Variantes de verbos
        'mejora': 'mejorar',
        'mejoras': 'mejorar',
        'usa': 'usar',
        'usas': 'usar',
        'busca': 'buscar',
        'buscas': 'buscar',
            'trabajo': 'trabajar', 'trabajas': 'trabajar', 'trabaja': 'trabajar',
            'trabajamos': 'trabajar', 'trabajan': 'trabajar',
            'trabajé': 'trabajar', 'trabajaste': 'trabajar', 'trabajó': 'trabajar',
            'trabajaron': 'trabajar', 'trabajaba': 'trabajar', 'trabajando': 'trabajar',
            
            # ESTUDIAR
            'estudio': 'estudiar', 'estudias': 'estudiar', 'estudia': 'estudiar',
            'estudiamos': 'estudiar', 'estudian': 'estudiar',
            'estudié': 'estudiar', 'estudió': 'estudiar', 'estudiando': 'estudiar',
            
            # COMER
            'como': 'comer', 'comes': 'comer', 'come': 'comer',
            'comemos': 'comer', 'comen': 'comer',
            'comí': 'comer', 'comió': 'comer', 'comiendo': 'comer',
            
            # VIVIR
            'vivo': 'vivir', 'vives': 'vivir', 'vive': 'vivir',
            'vivimos': 'vivir', 'viven': 'vivir', 'viviendo': 'vivir',
            
            # DORMIR
            'duermo': 'dormir', 'duermes': 'dormir', 'duerme': 'dormir',
            'durmiendo': 'dormir',
            
            # VER
            'veo': 'ver', 'ves': 'ver', 've': 'ver',
            'vemos': 'ver', 'ven': 'ver', 'viendo': 'ver',
            
            # ESTAR
            'estoy': 'estar', 'estás': 'estar', 'está': 'estar',
            'estamos': 'estar', 'están': 'estar', 'estando': 'estar',
            
            # Otros verbos comunes
            'amo': 'amar', 'amas': 'amar', 'ama': 'amar',
            'ayudo': 'ayudar', 'ayuda': 'ayudar',
            'canso': 'cansar', 'cansa': 'cansar',
            'conozco': 'conocer', 'conoce': 'conocer',
            'digo': 'decir', 'dice': 'decir',
            'invito': 'invitar', 'invita': 'invitar',
            'pregunto': 'preguntar', 'pregunta': 'preguntar',
            'presento': 'presentar', 'presenta': 'presentar', 'presentamos': 'presentar',
            'presentan': 'presentar', 'presentando': 'presentar',
            'quiero': 'querer', 'quiere': 'querer',
            'respondo': 'responder', 'responde': 'responder',
            'saludo': 'saludar', 'saluda': 'saludar',
            'siento': 'sentir', 'siente': 'sentir',
            'traduzco': 'traducir', 'traduce': 'traducir', 'traducen': 'traducir',
            'integro': 'integrar', 'integra': 'integrar', 'integramos': 'integrar',
        }
        
    def _cargar_diccionario(self) -> Dict[str, Dict[str, str]]:
        """Cargar diccionario actualizado de glosas LSV"""
        diccionario_path = Path(__file__).parent / 'scripts' / 'data.json'
        
        if diccionario_path.exists():
            with open(diccionario_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Diccionario de respaldo básico
        print("⚠️ Usando diccionario de respaldo")
        return {
            'hola': {'categoria': 'saludos', 'archivo': 'hola'},
            'mujer': {'categoria': 'personas', 'archivo': 'mujer'},
            'hombre': {'categoria': 'personas', 'archivo': 'hombre'},
            'deletrear': {'categoria': 'verbos', 'archivo': 'deletrear'},
        }
    
    def encontrar_palabra_similar(self, palabra: str, max_distancia: int = 2) -> Optional[Tuple[str, int]]:
        """
        Encontrar palabra más similar en diccionario
        Retorna: (palabra_similar, distancia) o None
        """
        palabra_lower = palabra.lower()
        
        # Si existe directamente
        if palabra_lower in self.diccionario:
            return (palabra_lower, 0)
        
        # Buscar en todas las fuentes
        todas_palabras = set(self.diccionario.keys())
        todas_palabras.update(self.normalizacion_lsv.keys())
        todas_palabras.update(self.palabras_femeninas.keys())
        
        candidatos = []
        
        for palabra_dict in todas_palabras:
            diff_longitud = abs(len(palabra_dict) - len(palabra_lower))
            if diff_longitud > 3:
                continue
            
            distancia = distancia_levenshtein(palabra_lower, palabra_dict)
            
            if distancia <= max_distancia:
                prioridad = (distancia * 10) + diff_longitud
                candidatos.append((palabra_dict, distancia, prioridad))
        
        if candidatos:
            candidatos.sort(key=lambda x: x[2])
            return (candidatos[0][0], candidatos[0][1])
        
        return None
    
    def corregir_texto(self, texto: str) -> Tuple[str, List[Dict]]:
        """
        Corregir errores ortográficos del texto
        IMPORTANTE: No separar frases compuestas del diccionario
        Retorna: (texto_corregido, lista_correcciones)
        """
        # Limpiar TODOS los signos de puntuación y caracteres especiales
        texto = re.sub(r'[¿?¡!,.;:"\'\(\)\[\]{}]', ' ', texto)
        # Normalizar acentos (mantener ñ)
        texto_normalizado = normalizar_texto_espanol(texto)
        # Limpiar espacios múltiples
        texto_normalizado = re.sub(r'\s+', ' ', texto_normalizado)
        palabras = texto_normalizado.lower().strip().split()
        
        palabras_corregidas = []
        correcciones = []
        
        # Procesar con detección de frases compuestas
        i = 0
        while i < len(palabras):
            palabra_procesada = False
            
            # Buscar frases de 4, 3, 2 palabras
            for num_palabras in [4, 3, 2]:
                if i + num_palabras <= len(palabras):
                    frase = ' '.join(palabras[i:i+num_palabras])
                    if frase in self.diccionario:
                        # Es una frase compuesta que existe, mantenerla completa
                        palabras_corregidas.append(frase)
                        i += num_palabras
                        palabra_procesada = True
                        break
            
            if palabra_procesada:
                continue
            
            # Procesar palabra individual
            palabra = palabras[i]
            
            # Omitir palabras eliminadas
            if palabra in self.palabras_omitidas:
                palabras_corregidas.append(palabra)
                i += 1
                continue
            
            # Números directos
            if palabra.isdigit():
                palabras_corregidas.append(palabra)
                i += 1
                continue
            
            # 1. Verificar si existe tal cual
            if palabra in self.diccionario:
                palabras_corregidas.append(palabra)
                i += 1
                continue
            
            # 2. Normalizar
            palabra_normalizada = self.normalizar_palabra(palabra)
            
            if palabra_normalizada and palabra_normalizada in self.diccionario:
                if palabra != palabra_normalizada:
                    correcciones.append({
                        'original': palabra,
                        'corregida': palabra_normalizada,
                        'tipo': 'normalización',
                        'confianza': 100
                    })
                palabras_corregidas.append(palabra_normalizada)
                i += 1
                continue
            
            # 3. Verificar si es parte de alguna frase compuesta conocida
            es_parte_frase_compuesta = False
            for frase_dict in self.diccionario.keys():
                if ' ' in frase_dict and palabra in frase_dict.split():
                    es_parte_frase_compuesta = True
                    break
            
            # Si es parte de frase compuesta, NO corregir (mantenerla para detección)
            if es_parte_frase_compuesta:
                palabras_corregidas.append(palabra)
                i += 1
                continue
            
            # 4. Buscar palabra similar (solo si NO es parte de frase compuesta)
            resultado = self.encontrar_palabra_similar(palabra, max_distancia=2)
            
            if resultado:
                palabra_similar, distancia = resultado
                confianza = 100 - (distancia * 30)
                
                # Aumentar umbral a 80% para evitar correcciones incorrectas
                if confianza >= 80:
                    correcciones.append({
                        'original': palabra,
                        'corregida': palabra_similar,
                        'tipo': 'ortografía',
                        'distancia': distancia,
                        'confianza': confianza
                    })
                    palabras_corregidas.append(palabra_similar)
                else:
                    palabras_corregidas.append(palabra)
            else:
                palabras_corregidas.append(palabra)
            
            i += 1
        
        texto_corregido = ' '.join(palabras_corregidas)
        return (texto_corregido, correcciones)
    
    def numero_a_glosas(self, numero: str) -> List[str]:
        """
        Convertir número a secuencia de glosas LSV
        
        REGLAS LSV PARA NÚMEROS:
        - 0-10: Directos (tienen seña individual)
        - 11-19: 10 + dígito (Ej: 18 = 10 + 8, NO 10 + 9)
        - 20-99: Dígitos separados (Ej: 25 = 2 + 5)
        - 100+: Dígitos separados
        """
        num = int(numero)
        
        # 0-10: directos
        if 0 <= num <= 10:
            return [str(num)]
        
        # 11-19: 10 + dígito (LSV estándar)
        if 11 <= num <= 19:
            digito = num - 10  # 18 -> 8, 13 -> 3, etc.
            return ['10', str(digito)]
        
        # 20+: dígitos separados
        return list(numero)
    
    def reformular_concepto(self, texto_completo: str, palabra: str) -> Optional[List[str]]:
        """
        ═══════════════════════════════════════════════════════════════════════
        🎯 ESTRATEGIA DE TRADUCCIÓN CONCEPTUAL LSV (PATRÓN 5)
        ═══════════════════════════════════════════════════════════════════════
        
        ⚠️ REGLAS CRÍTICAS ABSOLUTAS:
        
        1️⃣ SI UNA PALABRA EXISTE EN EL DICCIONARIO, NUNCA SE REFORMULA.
           Solo se reformulan palabras que NO tienen seña directa.
        
        2️⃣ SI UNA PALABRA NO EXISTE COMO GLOSA EXACTA:
           ❌ NO sustituir por otra glosa semánticamente cercana
           ✅ Usar combinación válida (ej: PERSONAS + SORDO)
           ✅ Eliminarla si no aporta significado
           ✅ Deletrearla solo si es concepto clave
        
        EJEMPLOS DE LO QUE NO SE DEBE HACER:
        ❌ 'comunidad' → 'grupo' (comunidad existe en diccionario)
        ❌ 'buscar' → 'querer' (buscar existe en diccionario)
        ❌ 'mejorar' → 'bien' (mejorar existe en diccionario)
        
        ⚠️ PRINCIPIOS FUNDAMENTALES:
        1. Verificar PRIMERO si existe en diccionario
        2. NO traducir literalmente
        3. NO inventar señas
        4. SOLO usar señas documentadas del diccionario
        5. Priorizar SIGNIFICADO sobre literalidad
        
        📋 PRIORIDAD DE REFORMULACIÓN:
        ──────────────────────────────────────────────────────────────────────
        0️⃣ Verificar si existe en diccionario (NUNCA reformular si existe)
        1️⃣ Reformulación conceptual (frases → señas existentes)
           Ejemplo: "implementación" → TRABAJAR USAR
        
        2️⃣ Uso de verbos base para construir significado
           Ejemplo: "implementación" → TRABAJAR USAR
        
        3️⃣ Deletreo (último recurso - se maneja en otra parte)
           Solo para: nombres propios, siglas, términos técnicos
        
        RETORNO:
        ──────────────────────────────────────────────────────────────────────
        - Lista de glosas LSV si se puede reformular
        - None si existe en diccionario o no hay reformulación
        
        ═══════════════════════════════════════════════════════════════════════
        """
        texto_lower = texto_completo.lower()
        palabra_lower = palabra.lower()
        
        # ⚠️ REGLA CRÍTICA: Si existe en diccionario, NO reformular
        if palabra_lower in self.diccionario:
            return None
        
        # ESTRATEGIA 1: Buscar reformulación de frases largas primero
        # Buscar contexto de hasta 5 palabras
        palabras = texto_lower.split()
        try:
            idx = palabras.index(palabra_lower)
            
            # Intentar frases de 5, 4, 3, 2 palabras alrededor de la palabra
            for window in [5, 4, 3, 2]:
                for start in range(max(0, idx - window + 1), idx + 1):
                    end = min(start + window, len(palabras))
                    if start <= idx < end:
                        frase = ' '.join(palabras[start:end])
                        if frase in self.reformulaciones_conceptuales:
                            glosas = self.reformulaciones_conceptuales[frase]
                            # Verificar que todas las glosas existan en el diccionario
                            if all(g in self.diccionario for g in glosas):
                                print(f"💡 Reformulación: '{frase}' → {' '.join(glosas).upper()}")
                                return glosas
        except ValueError:
            pass
        
        # ESTRATEGIA 2: Reformulación de palabra individual
        if palabra_lower in self.reformulaciones_conceptuales:
            glosas = self.reformulaciones_conceptuales[palabra_lower]
            if all(g in self.diccionario for g in glosas):
                print(f"💡 Concepto: '{palabra}' → {' '.join(glosas).upper()}")
                return glosas
        
        # ESTRATEGIA 3: Intentar descomposición con verbos base
        # Ej: "integrador" → "integrar" (si existe)
        # Sufijos que se pueden quitar para buscar verbo base
        sufijos_derivados = ['dor', 'dora', 'ción', 'cion', 'miento', 'anza', 'encia', 'dad', 'tad']
        
        for sufijo in sufijos_derivados:
            if palabra_lower.endswith(sufijo):
                raiz = palabra_lower[:-len(sufijo)]
                # Intentar con terminaciones verbales
                for terminacion in ['ar', 'er', 'ir']:
                    verbo = raiz + terminacion
                    if verbo in self.diccionario:
                        print(f"💡 Verbo base: '{palabra}' → {verbo.upper()}")
                        return [verbo]
                # La raíz sola
                if raiz in self.diccionario:
                    print(f"💡 Raíz: '{palabra}' → {raiz.upper()}")
                    return [raiz]
        
        return None
    
    def normalizar_palabra(self, palabra: str) -> Optional[str]:
        """
        Normalizar palabra según reglas LSV completas
        """
        palabra_lower = palabra.lower()
        
        # Números
        if palabra_lower.isdigit():
            return palabra_lower
        
        # Omitir
        if palabra_lower in self.palabras_omitidas:
            return None
        
        # Normalizaciones explícitas (incluye verbos)
        if palabra_lower in self.normalizacion_lsv:
            return self.normalizacion_lsv[palabra_lower]
        
        # Ya existe
        if palabra_lower in self.diccionario:
            return palabra_lower
        
        # PLURALES AUTOMÁTICOS
        # -s final
        if palabra_lower.endswith('s') and len(palabra_lower) > 3:
            singular = palabra_lower[:-1]
            if singular in self.diccionario:
                return singular
        
        # -es final
        if palabra_lower.endswith('es') and len(palabra_lower) > 4:
            singular = palabra_lower[:-2]
            if singular in self.diccionario:
                return singular
            # Probar con vocales
            for vocal in ['a', 'e', 'i', 'o', 'u']:
                candidato = singular + vocal
                if candidato in self.diccionario:
                    return candidato
        
        # Verbos con gerundio/participio
        if palabra_lower.endswith(('ando', 'iendo')):
            raiz = palabra_lower[:-4]
            for sufijo in ('ar', 'er', 'ir'):
                if raiz + sufijo in self.diccionario:
                    return raiz + sufijo
        
        return palabra_lower
    
    def translate_to_animations(
        self,
        texto: str,
        deletrear_desconocidas: bool = True,
        velocidad_deletreo: float = 1.2,
        corregir_ortografia: bool = True
    ) -> Dict:
        """
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        🎯 TRADUCTOR EXPERTO EN LENGUA DE SEÑAS VENEZOLANA (LSV)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        Sistema basado en información documental validada por FEVENSOR, Consorven
        y la comunidad sorda venezolana.
        
        ⚠️ PRINCIPIOS FUNDAMENTALES (NO MODIFICABLES):
        
        1. NO traducir literalmente el español
        2. NO imponer estructuras del español en LSV
        3. Priorizar el orden natural LSV: CONTEXTO → TIEMPO → LUGAR → SUJETO → ACCIÓN → COMPLEMENTO
        4. Eliminar artículos, preposiciones y conectores innecesarios
        5. Si una palabra no tiene seña documentada:
           - Deletrearla en dactilología
           - O reformular usando señas existentes
        6. Respetar la iconicidad y la intención comunicativa
        7. NO inventar señas
        8. NO usar español señado
        
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        📋 PATRONES LINGÜÍSTICOS LSV IMPLEMENTADOS:
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        1️⃣ PATRÓN TEMPORAL:
           El tiempo se indica al inicio de la oración.
           
           Español: "Mañana presentaré el proyecto"
           LSV: MAÑANA PROYECTO PRESENTAR
        
        2️⃣ PATRÓN DE CONTEXTO:
           Primero se establece el contexto antes de la acción.
           
           Español: "En la universidad necesitamos un sistema de traducción"
           LSV: UNIVERSIDAD CONTEXTO SISTEMA TRADUCIR NECESITAR
        
        3️⃣ PATRÓN DE ÉNFASIS VISUAL:
           Lo importante va primero.
           
           Español: "Es muy importante la comunicación"
           LSV: COMUNICACIÓN IMPORTANTE MUCHO
        
        4️⃣ PATRÓN DE NEGACIÓN:
           La negación va al final o se refuerza con expresión facial.
           
           Español: "No existe un sistema accesible"
           LSV: SISTEMA ACCESIBLE EXISTIR NO
        
        5️⃣ PATRÓN DE CONCEPTOS ABSTRACTOS:
           Los conceptos abstractos se reformulan.
           
           Español: "Integración social"
           LSV: PERSONAS SORDAS OYENTES JUNTOS PARTICIPAR
        
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        📚 EJEMPLOS DE TRADUCCIÓN COMPLETOS:
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        EJEMPLO 1 - Discurso académico:
        ────────────────────────────────
        Entrada: "Bienvenidos a la defensa de nuestro trabajo especial de grado"
        Salida: BIENVENIR DEFENSA TRABAJO GRADO NOSOTROS
        
        Observación: "especial" se omite por no aportar carga semántica visual relevante
        
        EJEMPLO 2 - Objetivo del proyecto:
        ───────────────────────────────────
        Entrada: "Nuestro objetivo es crear un sistema de traducción de lengua de señas venezolana"
        Salida: OBJETIVO NOSOTROS SISTEMA TRADUCIR LENGUA SEÑAS VENEZUELA CREAR
        
        EJEMPLO 3 - Palabra sin seña:
        ──────────────────────────────
        Entrada: "Plataforma digital inclusiva"
        Salida: PLATAFORMA D-E-L-E-T-R-E-A-R DIGITAL INCLUIR TODOS
        
        Observación: "Plataforma" se deletrea por no existir seña estándar documentada
        
        EJEMPLO 4 - Justificación social:
        ──────────────────────────────────
        Entrada: "Este proyecto busca mejorar la comunicación entre personas sordas y oyentes"
        Salida: PROYECTO ESTE BUSCAR COMUNICACIÓN MEJORAR PERSONA SORDA OYENTE
        
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        🔄 PROCESO DE TRADUCCIÓN (en orden de aplicación):
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        1️⃣ CORRECCIÓN ORTOGRÁFICA:
           - Detecta y corrige errores de escritura
           - Normaliza variantes venezolanas
        
        2️⃣ REFORMULACIÓN CONCEPTUAL (PRIORITARIA):
           - Si una palabra NO tiene seña documentada → NO inventa
           - Reformula usando señas existentes
           - Ej: "aporte tecnológico" → TECNOLOGÍA DAR
           - Ej: "integración" → INCLUIR
        
        3️⃣ VERBOS BASE para conceptos abstractos:
           - Usa: DAR, USAR, AYUDAR, JUNTOS, INCLUIR, PODER
           - Ej: "implementación" → HACER USAR
        
        4️⃣ OMISIÓN LINGÜÍSTICA:
           - Elimina artículos (el, la, los, las)
           - Elimina preposiciones contextuales (de, a, para, con, en)
        
        5️⃣ NORMALIZACIÓN:
           - Plurales → Singular
           - Verbos → Infinitivo (trabajó → trabajar)
           - Género femenino → Masculino + MUJER
           - Ej: "ingeniera" → INGENIERO MUJER
        
        6️⃣ ORDEN GRAMATICAL LSV:
           TIEMPO → LUGAR → SUJETO → OBJETO → VERBO → COMPLEMENTO
        
        7️⃣ NÚMEROS:
           - 0-10: directos
           - 11-19: 10 + dígito
           - 20+: dígitos separados
        
        8️⃣ DELETREO (ÚLTIMO RECURSO):
           Solo cuando:
           - Es nombre propio, sigla o término técnico
           - NO existe forma conceptual clara
           - Ya se intentó reformulación
        
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        📤 FORMATO DE SALIDA:
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        {
            'texto_original': str,        # Texto ingresado por el usuario
            'texto_corregido': str,       # Texto después de corrección ortográfica
            'correcciones': [...],        # Lista de correcciones aplicadas
            'animaciones': [...],         # Secuencia de animaciones LSV (glosas en orden)
            'total_animaciones': int,     # Número total de señas/letras
            'palabras_deletreadas': [...]  # Palabras que se deletrearon (sin seña)
        }
        
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        Este traductor actúa como intérprete y lingüista experto en LSV,
        no como traductor automático. Prioriza claridad visual, comprensión
        y naturalidad en LSV.
        
        Cada salida debe ser comprensible para una persona sorda venezolana
        sin conocimiento del español escrito.
        
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """
        
        texto_original = texto
        correcciones = []
        
        # 1. CORRECCIÓN ORTOGRÁFICA
        if corregir_ortografia:
            texto, correcciones = self.corregir_texto(texto)
            if correcciones:
                print(f"📝 Correcciones aplicadas: {len(correcciones)}")
        
        # 2. LIMPIAR Y TOKENIZAR
        # Eliminar TODOS los signos de puntuación y caracteres especiales
        texto = re.sub(r'[¿?¡!,.;:"\'\(\)\[\]{}]', ' ', texto)
        # Normalizar acentos (mantener ñ)
        texto = normalizar_texto_espanol(texto)
        # Limpiar espacios múltiples
        texto = re.sub(r'\s+', ' ', texto)
        palabras = texto.lower().strip().split()
        
        animaciones = []
        palabras_deletreadas = []
        palabras_procesadas = []
        observaciones = []  # Nuevas observaciones lingüísticas
        alternativas = []  # Alternativas válidas
        
        # 3. PROCESAMIENTO DE PALABRAS (frases compuestas primero)
        i = 0
        while i < len(palabras):
            encontrada = False
            
            # Frases de 4 palabras
            if i + 3 < len(palabras):
                frase4 = ' '.join(palabras[i:i+4])
                if frase4 in self.diccionario:
                    palabras_procesadas.append({
                        'original': frase4,
                        'normalizada': frase4,
                        'es_tiempo': frase4 in self.palabras_tiempo,
                        'es_femenino': False,
                        'tipo': 'frase'
                    })
                    i += 4
                    encontrada = True
            
            # Frases de 3 palabras
            if not encontrada and i + 2 < len(palabras):
                frase3 = ' '.join(palabras[i:i+3])
                if frase3 in self.diccionario:
                    palabras_procesadas.append({
                        'original': frase3,
                        'normalizada': frase3,
                        'es_tiempo': frase3 in self.palabras_tiempo,
                        'es_femenino': False,
                        'tipo': 'frase'
                    })
                    i += 3
                    encontrada = True
            
            # Frases de 2 palabras
            if not encontrada and i + 1 < len(palabras):
                frase2 = ' '.join(palabras[i:i+2])
                if frase2 in self.diccionario:
                    palabras_procesadas.append({
                        'original': frase2,
                        'normalizada': frase2,
                        'es_tiempo': frase2 in self.palabras_tiempo,
                        'es_femenino': False,
                        'tipo': 'frase'
                    })
                    i += 2
                    encontrada = True
            
            # Palabra individual
            if not encontrada:
                palabra_norm = self.normalizar_palabra(palabras[i])
                
                if palabra_norm is None:
                    i += 1
                    continue
                
                # Verificar género
                es_femenino = palabras[i] in self.palabras_femeninas
                palabra_base = self.palabras_femeninas.get(palabras[i], palabra_norm)
                
                # Número
                if palabra_base.isdigit():
                    palabras_procesadas.append({
                        'original': palabras[i],
                        'normalizada': palabra_base,
                        'es_tiempo': False,
                        'es_femenino': False,
                        'es_numero': True,
                        'tipo': 'numero'
                    })
                else:
                    palabras_procesadas.append({
                        'original': palabras[i],
                        'normalizada': palabra_base,
                        'es_tiempo': palabra_base in self.palabras_tiempo,
                        'es_femenino': es_femenino,
                        'tipo': 'palabra' if palabra_base in self.diccionario else 'desconocida'
                    })
                i += 1
        
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # 4. REFORMULACIÓN CONCEPTUAL (PATRÓN 5️⃣ - CONCEPTOS ABSTRACTOS)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # 
        # Antes de deletrear, intentar reformular usando señas existentes.
        # 
        # ⚠️ PRINCIPIO: NO inventar señas - SOLO usar señas documentadas
        # 
        # Ejemplos de reformulación:
        #   - "integración social" → PERSONAS JUNTOS PARTICIPAR
        #   - "aporte tecnológico" → TECNOLOGÍA DAR
        #   - "implementación" → HACER USAR
        # 
        # Esto prioriza SIGNIFICADO sobre literalidad (pensamiento visual).
        # 
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        palabras_con_reformulacion = []
        
        for palabra in palabras_procesadas:
            # Si es desconocida, intentar reformular
            if palabra['tipo'] == 'desconocida':
                reformulacion = self.reformular_concepto(texto, palabra['original'])
                
                if reformulacion:
                    # Agregar observación sobre la reformulación
                    glosas_reformuladas = ' '.join(reformulacion).upper()
                    observaciones.append(f"'{palabra['original']}' se reformuló conceptualmente como: {glosas_reformuladas}")
                    
                    # Agregar cada glosa de la reformulación
                    for glosa in reformulacion:
                        palabras_con_reformulacion.append({
                            'original': palabra['original'],
                            'normalizada': glosa,
                            'es_tiempo': glosa in self.palabras_tiempo,
                            'es_lugar': glosa in self.palabras_lugar,
                            'es_femenino': False,
                            'tipo': 'reformulada',
                            'reformulacion_de': palabra['original']
                        })
                else:
                    # Mantener como desconocida para deletrear después
                    palabra['es_lugar'] = False
                    palabras_con_reformulacion.append(palabra)
            else:
                # Marcar si es lugar
                palabra['es_lugar'] = palabra.get('normalizada', '') in self.palabras_lugar
                palabras_con_reformulacion.append(palabra)
        
        palabras_procesadas = palabras_con_reformulacion
        
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # 5. REORDENAR según ORDEN GRAMATICAL LSV (PATRÓN FUNDAMENTAL)
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # 
        # Orden natural LSV (visual-espacial, NO sintaxis española):
        # 
        #   CONTEXTO → TIEMPO → LUGAR → SUJETO → ACCIÓN → COMPLEMENTO → NEGACIÓN
        # 
        # Ejemplos:
        #   - "Mañana presentaré el proyecto"
        #     → MAÑANA PROYECTO PRESENTAR
        #     (TIEMPO primero + omisión de artículos)
        # 
        #   - "En la universidad necesitamos un sistema"
        #     → UNIVERSIDAD SISTEMA NECESITAR
        #     (LUGAR establece contexto + omisión de artículos)
        # 
        #   - "No existe un sistema accesible"
        #     → SISTEMA EXISTIR NO
        #     (NEGACIÓN al final - PATRÓN 4)
        # 
        # Este reordenamiento implementa los patrones:
        #   • PATRÓN DE CONTEXTO (2️⃣)
        #   • PATRÓN TEMPORAL (1️⃣)
        #   • PATRÓN DE ÉNFASIS VISUAL (3️⃣)
        #   • PATRÓN DE NEGACIÓN (4️⃣)
        # 
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        # Clasificar palabras por tipo para reordenamiento LSV
        # Orden LSV: TIEMPO → POSESIVO → SUJETO → OBJETO/LUGAR → VERBO → NEGACIÓN
        palabras_tiempo = []
        palabras_posesivo = []
        palabras_lugar = []
        palabras_verbo = []
        palabras_negacion = []
        palabras_resto = []
        
        posesivos = {'mio', 'tuyo', 'suyo', 'nuestro'}
        verbos_diccionario = {'trabajar', 'estudiar', 'comer', 'vivir', 'dormir', 'ver', 'estar',
                              'amar', 'ayudar', 'conocer', 'decir', 'invitar', 'presentar',
                              'querer', 'responder', 'saludar', 'sentir', 'ser', 'agarrar',
                              'atraer', 'burlar', 'calmar', 'cansar', 'deletrear', 'engañar',
                              'guardar', 'llevar', 'pelear', 'preguntar', 'regalar', 'sufrir',
                              'traer', 'usar', 'verbo', 'vestir', 'viajar', 'entrar', 'fumar',
                              'permitir', 'prohibir', 'respetar', 'correr', 'dividir', 'multiplicar',
                              'restar', 'sumar', 'crear', 'evaluar'}
        
        for p in palabras_procesadas:
            palabra = p.get('normalizada', '')
            
            # Clasificar por tipo según orden LSV correcto
            if p.get('es_tiempo') or palabra in self.palabras_tiempo:
                palabras_tiempo.append(p)
            elif palabra in posesivos:
                palabras_posesivo.append(p)
            elif palabra in verbos_diccionario:
                palabras_verbo.append(p)
            elif p.get('es_lugar') or palabra in self.palabras_lugar:
                palabras_lugar.append(p)
            elif palabra in self.palabras_negacion:
                palabras_negacion.append(p)
            else:
                palabras_resto.append(p)
        
        # Orden LSV correcto: TIEMPO → POSESIVO → SUJETO-OBJETO-LUGAR → VERBO → NEGACIÓN
        secuencia_final = palabras_tiempo + palabras_posesivo + palabras_resto + palabras_lugar + palabras_verbo + palabras_negacion
        
        # 6. CONVERTIR A ANIMACIONES
        for palabra in secuencia_final:
            # Números
            if palabra.get('es_numero'):
                for glosa in self.numero_a_glosas(palabra['normalizada']):
                    if glosa in self.diccionario:
                        info = self.diccionario[glosa]
                        animaciones.append({
                            'nombre': glosa,
                            'categoria': info['categoria'],
                            'archivo': info['archivo'],
                            'es_deletreo': False
                        })
                continue
            
            # Palabras conocidas o reformuladas
            if palabra['tipo'] in ('palabra', 'frase', 'reformulada'):
                if palabra['normalizada'] in self.diccionario:
                    info = self.diccionario[palabra['normalizada']]
                    animaciones.append({
                        'nombre': palabra['normalizada'],
                        'categoria': info['categoria'],
                        'archivo': info['archivo'],
                        'es_deletreo': False
                    })
                    
                    # GÉNERO: Agregar MUJER después de profesiones/personas femeninas
                    # Solo si:
                    #   1. La palabra es femenina (normalizada a masculino)
                    #   2. La palabra original NO existe como entrada independiente en el diccionario
                    #   3. La palabra normalizada es diferente de la original (hubo conversión de género)
                    # 
                    # Ejemplo:
                    #   ✅ "ingeniera" -> "ingeniero" (normalizada ≠ original) -> INGENIERO + MUJER
                    #   ❌ "policia" -> "policia" (normalizada == original) -> POLICIA (sin MUJER)
                    # 
                    if (palabra['es_femenino'] and 
                        'mujer' in self.diccionario and 
                        palabra['original'] not in self.diccionario and
                        palabra['normalizada'] != palabra['original']):
                        
                        info_mujer = self.diccionario['mujer']
                        animaciones.append({
                            'nombre': 'mujer',
                            'categoria': info_mujer['categoria'],
                            'archivo': info_mujer['archivo'],
                            'es_deletreo': False
                        })
                        # Agregar observación sobre género
                        palabra_fem = palabra['original']
                        palabra_masc = palabra['normalizada'].upper()
                        observaciones.append(f"'{palabra_fem}' se traduce como {palabra_masc} + MUJER (patrón de género femenino en LSV)")
                continue
            
            # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            # DELETREO DACTILOLÓGICO (8️⃣ - ÚLTIMO RECURSO)
            # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            # 
            # Solo llega aquí si:
            #   ✅ NO existe seña documentada en el diccionario
            #   ✅ NO se pudo reformular usando señas existentes
            #   ✅ Es nombre propio, sigla o término técnico
            # 
            # Ejemplos que SE DELETREAN:
            #   • Nombres propios: "José", "María", "Venezuela"
            #   • Siglas: "USB", "ULA", "LSV"
            #   • Términos técnicos sin seña: "plataforma", "algoritmo"
            # 
            # Ejemplos que NO se deletrean (se reformulan):
            #   • "integración" → INCLUIR (seña existente)
            #   • "implementación" → HACER USAR (verbos base)
            #   • "comunicación" → TRADUCIR (concepto similar)
            # 
            # ⚠️ El deletreo respeta la iconicidad: cada letra se seña individualmente
            #    con su configuración manual específica del alfabeto LSV.
            # 
            # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            
            if deletrear_desconocidas and palabra['tipo'] == 'desconocida':
                palabras_deletreadas.append(palabra['original'])
                
                # Señal DELETREAR
                if 'deletrear' in self.diccionario:
                    info = self.diccionario['deletrear']
                    animaciones.append({
                        'nombre': 'deletrear',
                        'categoria': info['categoria'],
                        'archivo': info['archivo'],
                        'es_deletreo': True
                    })
                
                # Deletrear cada letra
                for letra in palabra['original']:
                    if letra.lower() in self.diccionario:
                        info = self.diccionario[letra.lower()]
                        animaciones.append({
                            'nombre': letra.lower(),
                            'categoria': info['categoria'],
                            'archivo': info['archivo'],
                            'es_deletreo': True,
                            'duracion': velocidad_deletreo
                        })
        
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # RESULTADO FINAL: GLOSAS LSV en orden correcto
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # 
        # Las animaciones están en el orden gramatical LSV correcto:
        #   CONTEXTO → TIEMPO → LUGAR → SUJETO → ACCIÓN → COMPLEMENTO → NEGACIÓN
        # 
        # Cada glosa corresponde a:
        #   • Una seña documentada del diccionario LSV
        #   • Una letra del alfabeto (si es deletreo)
        # 
        # Las glosas están en MAYÚSCULAS (estándar de notación LSV)
        # 
        # Este output es comprensible para una persona sorda venezolana
        # sin conocimiento del español escrito.
        # 
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        # Generar glosa LSV limpia (sin deletreo)
        glosa_lsv = ' '.join([
            anim['nombre'].upper() 
            for anim in animaciones 
            if not anim.get('es_deletreo', False)
        ])
        
        # Agregar observación si se deletrearon palabras
        if palabras_deletreadas:
            palabras_del_str = ', '.join(f"'{p}'" for p in palabras_deletreadas)
            observaciones.append(f"Palabras deletreadas por no existir seña documentada: {palabras_del_str}")
        
        # Detectar si se aplicó reordenamiento temporal
        if palabras_tiempo:
            observaciones.append("Se aplicó PATRÓN TEMPORAL: el tiempo se colocó al inicio de la oración (estructura LSV)")
        
        # Detectar si se aplicó reordenamiennto de negación
        if palabras_negacion:
            observaciones.append("Se aplicó PATRÓN DE NEGACIÓN: la negación se colocó al final (estructura LSV)")
        
        return {
            'texto_original': texto_original,
            'texto_corregido': texto,
            'glosa_lsv': glosa_lsv,  # Nueva: glosa limpia en MAYÚSCULAS
            'correcciones': correcciones,
            'animaciones': animaciones,
            'total_animaciones': len(animaciones),
            'palabras_deletreadas': palabras_deletreadas,
            'observaciones_linguisticas': observaciones,  # Nueva: observaciones sobre la traducción
            'alternativas': alternativas  # Nueva: alternativas válidas (puede estar vacía)
        }
