"""
LSV Optimizer COMPLETO - Traductor de Español a Lengua de Señas Venezolana
Versión optimizada con todas las reglas lingüísticas de LSV
"""

import re
import json
from pathlib import Path
from typing import List, Dict, Tuple, Optional

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
    Optimizador LSV con conocimiento completo de:
    - 311 palabras en diccionario
    - 18 categorías semánticas
    - Reglas gramaticales venezolanas
    - Orden temporal (TIEMPO-SUJETO-VERBO-OBJETO)
    - Sistema de género (HOMBRE/MUJER después de profesiones/personas)
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
            
            # Preposiciones que se omiten
            'de', 'del', 'al', 'a',
            
            # Conjunciones
            'y', 'e', 'o', 'u',
            
            # Pronombres reflexivos/átonos
            'se', 'me', 'te', 'le', 'les', 'nos',
            
            # Verbos ser/estar en presente (se infieren por contexto)
            'es', 'son', 'esta', 'están',
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
            
            # Períodos
            'mes', 'semana', 'año', 'dia',
            'fin de semana', 'calendario',
        }
        
        # ==========================================
        # REGLA 3: GÉNERO EN LSV
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
        # REGLA 4: NORMALIZACIÓN LSV
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
        }
        
        # ==========================================
        # REGLA 5: VERBOS - Infinitivo siempre
        # ==========================================
        self.normalizacion_verbos = {
            # TRABAJAR
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
            'presento': 'presentar', 'presenta': 'presentar',
            'quiero': 'querer', 'quiere': 'querer',
            'respondo': 'responder', 'responde': 'responder',
            'saludo': 'saludar', 'saluda': 'saludar',
            'siento': 'sentir', 'siente': 'sentir',
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
        todas_palabras.update(self.normalizacion_verbos.keys())
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
        Retorna: (texto_corregido, lista_correcciones)
        """
        # Limpiar TODOS los signos de puntuación y caracteres especiales
        texto = re.sub(r'[¿?¡!,.;:"\'\(\)\[\]{}]', ' ', texto)
        # Limpiar espacios múltiples
        texto = re.sub(r'\s+', ' ', texto)
        palabras = texto.lower().strip().split()
        
        palabras_corregidas = []
        correcciones = []
        
        for palabra in palabras:
            # Omitir palabras eliminadas
            if palabra in self.palabras_omitidas:
                palabras_corregidas.append(palabra)
                continue
            
            # Números directos
            if palabra.isdigit():
                palabras_corregidas.append(palabra)
                continue
            
            # 1. Verificar si existe tal cual
            if palabra in self.diccionario:
                palabras_corregidas.append(palabra)
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
                continue
            
            # 3. Buscar palabra similar
            resultado = self.encontrar_palabra_similar(palabra, max_distancia=2)
            
            if resultado:
                palabra_similar, distancia = resultado
                confianza = 100 - (distancia * 30)
                
                if confianza >= 50:
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
        
        texto_corregido = ' '.join(palabras_corregidas)
        return (texto_corregido, correcciones)
    
    def numero_a_glosas(self, numero: str) -> List[str]:
        """Convertir número a secuencia de glosas LSV"""
        num = int(numero)
        
        # 0-10: directos
        if 0 <= num <= 10:
            return [str(num)]
        
        # 11-19: 10 + dígito
        if 11 <= num <= 19:
            return ['10', str(num % 10)]
        
        # 20+: dígitos separados
        return list(numero)
    
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
        
        # Normalizaciones explícitas
        if palabra_lower in self.normalizacion_lsv:
            return self.normalizacion_lsv[palabra_lower]
        
        # Verbos
        if palabra_lower in self.normalizacion_verbos:
            return self.normalizacion_verbos[palabra_lower]
        
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
        Traducir texto español a secuencia de animaciones LSV
        Aplica TODAS las reglas lingüísticas de LSV venezolano
        
        Retorna:
        {
            texto_original: str,
            texto_corregido: str,
            correcciones: [...],
            animaciones: [...],
            total_animaciones: int,
            palabras_deletreadas: [...]
        }
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
        # Limpiar espacios múltiples
        texto = re.sub(r'\s+', ' ', texto)
        palabras = texto.lower().strip().split()
        
        animaciones = []
        palabras_deletreadas = []
        palabras_procesadas = []
        
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
        
        # 4. REORDENAR: TIEMPO AL INICIO (regla fundamental LSV)
        palabras_tiempo = [p for p in palabras_procesadas if p.get('es_tiempo')]
        palabras_resto = [p for p in palabras_procesadas if not p.get('es_tiempo')]
        secuencia_final = palabras_tiempo + palabras_resto
        
        # 5. CONVERTIR A ANIMACIONES
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
            
            # Palabras conocidas
            if palabra['tipo'] in ('palabra', 'frase'):
                if palabra['normalizada'] in self.diccionario:
                    info = self.diccionario[palabra['normalizada']]
                    animaciones.append({
                        'nombre': palabra['normalizada'],
                        'categoria': info['categoria'],
                        'archivo': info['archivo'],
                        'es_deletreo': False
                    })
                    
                    # GÉNERO: Agregar MUJER después de profesiones/personas femeninas
                    if palabra['es_femenino'] and 'mujer' in self.diccionario:
                        info_mujer = self.diccionario['mujer']
                        animaciones.append({
                            'nombre': 'mujer',
                            'categoria': info_mujer['categoria'],
                            'archivo': info_mujer['archivo'],
                            'es_deletreo': False
                        })
                continue
            
            # Palabras desconocidas → deletrear
            if deletrear_desconocidas:
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
        
        return {
            'texto_original': texto_original,
            'texto_corregido': texto,
            'correcciones': correcciones,
            'animaciones': animaciones,
            'total_animaciones': len(animaciones),
            'palabras_deletreadas': palabras_deletreadas
        }
