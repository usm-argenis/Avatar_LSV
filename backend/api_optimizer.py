"""
LSV Optimizer - Traductor de Español a Lengua de Señas Venezolana
Implementa todas las reglas lingüísticas de LSV + corrección ortográfica
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
            # Costo de inserción, eliminación o sustitución
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

class LSVOptimizer:
    def __init__(self):
        """Inicializar el optimizador con todas las reglas LSV"""
        
        # Cargar diccionario de glosas
        self.diccionario = self._cargar_diccionario()
        
        # Palabras que se omiten en LSV
        self.palabras_omitidas = {
            'el', 'la', 'los', 'las',
            'un', 'una', 'unos', 'unas',
            'de', 'del', 'al',
            'y', 'e', 'o', 'u',
            'se', 'me', 'te', 'le', 'les', 'nos',
        }
        
        # Palabras de TIEMPO (van al inicio)
        self.palabras_tiempo = {
            'ayer', 'hoy', 'mañana', 'anteayer', 'pasado mañana',
            'hace rato', 'hace años', 'había una vez', 'antes',
            'ahora', 'despues', 'luego', 'pronto', 'tarde', 'temprano',
            'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo',
            'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
            'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre',
        }
        
        # Palabras femeninas → masculino neutro + MUJER
        # Solo personas, NO carreras ni objetos
        self.palabras_femeninas = {
            # Familia
            'mama': 'papa', 'madre': 'padre',
            'madrastra': 'padrastro', 'madrina': 'padrino',
            'abuela': 'abuelo', 'nieta': 'nieto',
            'tia': 'tio', 'prima': 'primo',
            'sobrina': 'sobrino', 'suegra': 'suegro',
            'cuñada': 'cuñado', 'hermana': 'hermano',
            'hija': 'hijo', 'hijastra': 'hijastro',
            'hermanastra': 'hermanastro',
            
            # Profesiones (personas)
            'maestra': 'maestro', 'profesora': 'profesor',
            'doctora': 'medico', 'ingeniera': 'ingeniero',
            'abogada': 'abogado', 'administradora': 'administrador',
            'contadora': 'contador', 'directora': 'director',
            'gerenta': 'gerente', 'vendedora': 'vendedor',
            'cocinera': 'cocinero', 'psicologa': 'psicologo',
            'inspectora': 'inspector', 'instructora': 'instructor',
            'jefa': 'jefe', 'mensajera': 'mensajero',
            'mesonera': 'mesonero', 'pintora': 'pintor',
            'supervisora': 'supervisor', 'traductora': 'traductor',
            'vigilanta': 'vigilante', 'escritora': 'escritor',
            'fotografa': 'fotografo', 'auxiliar': 'auxiliar',  # neutro
            
            # Personas
            'señora': 'señor', 'señorita': 'señor',
            'novia': 'novio', 'amiga': 'amigo',
            'compañera': 'compañero',
            'vieja': 'viejo', 'niña': 'niño',
            'joven': 'joven',  # neutro
            'anciana': 'anciano',
            'adulta': 'adulto',
            'mayor': 'mayor',  # neutro
            'ciega': 'ciego',
            'sorda': 'sordo',
            'sordociega': 'sordociego',
            'oyente': 'oyente',  # neutro
            
            # Estado civil
            'casada': 'casado',
            'soltera': 'soltero',
            'divorciada': 'divorciado',
            'separada': 'separado',
            'viuda': 'viudo',
            'concubina': 'concubino',
        }
        
        # Normalizaciones LSV
        self.normalizacion_lsv = {
            'todos': 'todo', 'todas': 'todo',
            'muchos': 'mucho', 'muchas': 'mucho',
            'pocos': 'poco', 'pocas': 'poco',
            'algunos': 'algun', 'algunas': 'algun',
            'ningunos': 'ningun', 'ningunas': 'ningun',
            'otros': 'otro', 'otras': 'otro',
            'demasiados': 'demasiado', 'demasiadas': 'demasiado',
            'bastantes': 'bastante',
            'dias': 'dia', 'años': 'año', 'meses': 'mes',
            'semanas': 'semana', 'horas': 'hora',
            'minutos': 'minuto', 'segundos': 'segundo',
            'nosotras': 'nosotros',
            'vosotros': 'ustedes', 'vosotras': 'ustedes',
            'mi': 'mio', 'mis': 'mio',
            'tu': 'tuyo', 'tus': 'tuyo',
            'su': 'suyo', 'sus': 'suyo',
            'nuestro': 'nuestro', 'nuestra': 'nuestro',
            'nuestros': 'nuestro', 'nuestras': 'nuestro',
        }
        
        # Normalización de verbos
        self.normalizacion_verbos = {
            # Trabajar
            'trabajo': 'trabajar', 'trabajas': 'trabajar', 'trabaja': 'trabajar',
            'trabajamos': 'trabajar', 'trabajan': 'trabajar', 'trabajé': 'trabajar',
            'trabajaste': 'trabajar', 'trabajó': 'trabajar', 'trabajaron': 'trabajar',
            'trabajaba': 'trabajar', 'trabajando': 'trabajar',
            # Estudiar
            'estudio': 'estudiar', 'estudias': 'estudiar', 'estudia': 'estudiar',
            'estudiamos': 'estudiar', 'estudian': 'estudiar', 'estudié': 'estudiar',
            'estudiaste': 'estudiar', 'estudió': 'estudiar', 'estudiaron': 'estudiar',
            'estudiaba': 'estudiar', 'estudiando': 'estudiar',
            # Comer
            'como': 'comer', 'comes': 'comer', 'come': 'comer',
            'comemos': 'comer', 'comen': 'comer', 'comí': 'comer',
            'comiste': 'comer', 'comió': 'comer', 'comieron': 'comer',
            'comía': 'comer', 'comiendo': 'comer',
            # Vivir
            'vivo': 'vivir', 'vives': 'vivir', 'vive': 'vivir',
            'vivimos': 'vivir', 'viven': 'vivir', 'viví': 'vivir',
            'viviste': 'vivir', 'vivió': 'vivir', 'vivieron': 'vivir',
            'vivía': 'vivir', 'viviendo': 'vivir',
            # Dormir
            'duermo': 'dormir', 'duermes': 'dormir', 'duerme': 'dormir',
            'dormimos': 'dormir', 'duermen': 'dormir', 'dormí': 'dormir',
            'dormiste': 'dormir', 'durmió': 'dormir', 'durmieron': 'dormir',
            'dormía': 'dormir', 'durmiendo': 'dormir',
            # Ver
            'veo': 'ver', 'ves': 'ver', 've': 'ver',
            'vemos': 'ver', 'ven': 'ver', 'vi': 'ver',
            'viste': 'ver', 'vio': 'ver', 'vieron': 'ver',
            'veía': 'ver', 'viendo': 'ver',
            # Estar
            'estoy': 'estar', 'estás': 'estar', 'está': 'estar',
            'estamos': 'estar', 'están': 'estar', 'estuve': 'estar',
            'estuviste': 'estar', 'estuvo': 'estar', 'estuvieron': 'estar',
            'estaba': 'estar', 'estando': 'estar',
            # Ser
            'soy': 'ser', 'eres': 'ser', 'es': 'ser',
            'somos': 'ser', 'son': 'ser', 'fui': 'ser',
            'fuiste': 'ser', 'fue': 'ser', 'fueron': 'ser',
            'era': 'ser', 'siendo': 'ser',
            # Otros verbos comunes
            'ayudo': 'ayudar', 'ayudas': 'ayudar', 'ayuda': 'ayudar',
            'amo': 'amar', 'amas': 'amar', 'ama': 'amar',
            'canso': 'cansar', 'cansas': 'cansar', 'cansa': 'cansar',
            'conozco': 'conocer', 'conoces': 'conocer', 'conoce': 'conocer',
            'digo': 'decir', 'dices': 'decir', 'dice': 'decir',
            'invito': 'invitar', 'invitas': 'invitar', 'invita': 'invitar',
            'pregunto': 'preguntar', 'preguntas': 'preguntar', 'pregunta': 'preguntar',
            'presento': 'presentar', 'presentas': 'presentar', 'presenta': 'presentar',
            'quiero': 'querer', 'quieres': 'querer', 'quiere': 'querer',
            'respondo': 'responder', 'respondes': 'responder', 'responde': 'responder',
            'saludo': 'saludar', 'saludas': 'saludar', 'saluda': 'saludar',
            'siento': 'sentir', 'sientes': 'sentir', 'siente': 'sentir',
            'corro': 'correr', 'corres': 'correr', 'corre': 'correr',
            'entro': 'entrar', 'entras': 'entrar', 'entra': 'entrar',
            'viajo': 'viajar', 'viajas': 'viajar', 'viaja': 'viajar',
        }
        
    def _cargar_diccionario(self) -> Dict[str, Dict[str, str]]:
        """Cargar diccionario de glosas desde archivo JSON"""
        diccionario_path = Path(__file__).parent / 'scripts' / 'data.json'
        
        # Si existe el archivo, cargarlo
        if diccionario_path.exists():
            with open(diccionario_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Diccionario básico de respaldo
        print("⚠️ Usando diccionario básico de respaldo")
        diccionario_basico = {
            'deletrear': {'categoria': 'verbos', 'archivo': 'deletrear'},
            'mujer': {'categoria': 'personas', 'archivo': 'mujer'},
        }
        
        # Agregar números
        for i in range(11):
            diccionario_basico[str(i)] = {'categoria': 'numero', 'archivo': str(i)}
        
        # Agregar alfabeto
        for letra in 'abcdefghijklmnopqrstuvwxyzñ':
            diccionario_basico[letra] = {'categoria': 'alfabeto', 'archivo': letra}
        
        return diccionario_basico
    
    def encontrar_palabra_similar(self, palabra: str, max_distancia: int = 2) -> Optional[Tuple[str, int]]:
        """
        Encontrar la palabra más similar en el diccionario
        Retorna: (palabra_similar, distancia) o None
        """
        palabra_lower = palabra.lower()
        
        # Si la palabra ya existe, retornarla directamente
        if palabra_lower in self.diccionario:
            return (palabra_lower, 0)
        
        # Buscar en todas las normalizaciones y verbos también
        todas_palabras = set(self.diccionario.keys())
        todas_palabras.update(self.normalizacion_lsv.keys())
        todas_palabras.update(self.normalizacion_verbos.keys())
        todas_palabras.update(self.palabras_femeninas.keys())
        
        candidatos = []
        
        for palabra_dict in todas_palabras:
            # Priorizar palabras de longitud similar
            diff_longitud = abs(len(palabra_dict) - len(palabra_lower))
            if diff_longitud > 3:
                continue
            
            distancia = distancia_levenshtein(palabra_lower, palabra_dict)
            
            if distancia <= max_distancia:
                # Priorizar por: 1) menor distancia, 2) menor diferencia de longitud
                prioridad = (distancia * 10) + diff_longitud
                candidatos.append((palabra_dict, distancia, prioridad))
        
        if candidatos:
            # Ordenar por prioridad y retornar el mejor
            candidatos.sort(key=lambda x: x[2])
            return (candidatos[0][0], candidatos[0][1])
        
        return None
    
    def corregir_texto(self, texto: str) -> Tuple[str, List[Dict]]:
        """
        Corregir errores ortográficos en el texto
        Retorna: (texto_corregido, lista_de_correcciones)
        """
        # Limpiar signos
        texto = re.sub(r'[¿?¡!]', '', texto)
        palabras = texto.lower().strip().split()
        
        palabras_corregidas = []
        correcciones = []
        
        for palabra in palabras:
            # Omitir palabras que se eliminan
            if palabra in self.palabras_omitidas:
                palabras_corregidas.append(palabra)
                continue
            
            # Verificar si es número
            if palabra.isdigit():
                palabras_corregidas.append(palabra)
                continue
            
            # PRIMERO: Verificar si la palabra ya existe tal cual en el diccionario
            if palabra in self.diccionario:
                palabras_corregidas.append(palabra)
                continue
            
            # SEGUNDO: Intentar normalizar
            palabra_normalizada = self.normalizar_palabra(palabra)
            
            # Si existe después de normalizar, usar esa
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
            
            # TERCERO: Si no existe, buscar palabra similar (solo si confianza > 50%)
            resultado = self.encontrar_palabra_similar(palabra, max_distancia=2)
            
            if resultado:
                palabra_similar, distancia = resultado
                confianza = 100 - (distancia * 30)  # 1 char = 70%, 2 chars = 40%
                
                # Solo aplicar corrección si confianza >= 50%
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
                    # Confianza muy baja, mantener original
                    palabras_corregidas.append(palabra)
            else:
                # No se encontró similar, mantener original
                palabras_corregidas.append(palabra)
        
        texto_corregido = ' '.join(palabras_corregidas)
        return (texto_corregido, correcciones)
    
    def numero_a_glosas(self, numero: str) -> List[str]:
        """Convertir número a secuencia de glosas LSV"""
        num = int(numero)
        
        # 0-10: directos
        if 0 <= num <= 10:
            return [str(num)]
        
        # 11-19: 10 + segundo dígito
        if 11 <= num <= 19:
            return ['10', str(num % 10)]
        
        # 20+: separar dígitos
        return list(numero)
    
    def normalizar_palabra(self, palabra: str) -> Optional[str]:
        """Normalizar palabra según reglas LSV con expansión automática de plurales"""
        palabra_lower = palabra.lower()
        
        # Verificar si es número
        if palabra_lower.isdigit():
            return palabra_lower
        
        # Verificar si se omite
        if palabra_lower in self.palabras_omitidas:
            return None
        
        # Verificar normalizaciones LSV explícitas
        if palabra_lower in self.normalizacion_lsv:
            return self.normalizacion_lsv[palabra_lower]
        
        # Verificar normalizaciones de verbos
        if palabra_lower in self.normalizacion_verbos:
            return self.normalizacion_verbos[palabra_lower]
        
        # Si está en diccionario directamente, retornar
        if palabra_lower in self.diccionario:
            return palabra_lower
        
        # NORMALIZACIÓN AUTOMÁTICA DE PLURALES
        # Regla 1: palabras terminadas en -s (plurales)
        if palabra_lower.endswith('s') and len(palabra_lower) > 3:
            singular = palabra_lower[:-1]
            if singular in self.diccionario:
                return singular
        
        # Regla 2: palabras terminadas en -es
        if palabra_lower.endswith('es') and len(palabra_lower) > 4:
            singular = palabra_lower[:-2]
            if singular in self.diccionario:
                return singular
            # También probar agregando vocal final
            for vocal in ['a', 'e', 'i', 'o', 'u']:
                candidato = singular + vocal
                if candidato in self.diccionario:
                    return candidato
        
        # Si está en diccionario después de normalizar, retornar
        if palabra_lower in self.diccionario:
            return palabra_lower
        
        # Reglas genéricas para verbos
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
        Traduce texto a secuencia de animaciones LSV
        Retorna: {
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
        
        # Corregir ortografía si está habilitado
        if corregir_ortografia:
            texto, correcciones = self.corregir_texto(texto)
            print(f"📝 Texto original: {texto_original}")
            print(f"✅ Texto corregido: {texto}")
            if correcciones:
                for corr in correcciones:
                    print(f"   🔧 {corr['original']} → {corr['corregida']} ({corr['tipo']}, {corr['confianza']}%)")
        
        # Limpiar texto
        texto = re.sub(r'[¿?¡!]', '', texto)
        palabras = texto.lower().strip().split()
        
        animaciones = []
        palabras_deletreadas = []
        palabras_procesadas = []
        
        # Procesar palabras
        i = 0
        while i < len(palabras):
            encontrada = False
            
            # Frases de 4 palabras (para "cual es tu nombre", etc.)
            if i + 3 < len(palabras):
                frase4 = ' '.join(palabras[i:i+4])
                frase4_norm = self.normalizar_palabra(frase4)
                
                # Buscar tanto la frase normalizada como la original
                if (frase4_norm and frase4_norm in self.diccionario) or (frase4 in self.diccionario):
                    frase_final = frase4_norm if frase4_norm in self.diccionario else frase4
                    palabras_procesadas.append({
                        'original': frase4,
                        'normalizada': frase_final,
                        'es_tiempo': frase_final in self.palabras_tiempo,
                        'es_femenino': False,
                        'tipo': 'frase'
                    })
                    i += 4
                    encontrada = True
            
            # Frases de 3 palabras
            if not encontrada and i + 2 < len(palabras):
                frase3 = ' '.join(palabras[i:i+3])
                frase3_norm = self.normalizar_palabra(frase3)
                
                # Buscar tanto la frase normalizada como la original
                if (frase3_norm and frase3_norm in self.diccionario) or (frase3 in self.diccionario):
                    frase_final = frase3_norm if frase3_norm in self.diccionario else frase3
                    palabras_procesadas.append({
                        'original': frase3,
                        'normalizada': frase_final,
                        'es_tiempo': frase_final in self.palabras_tiempo,
                        'es_femenino': False,
                        'tipo': 'frase'
                    })
                    i += 3
                    encontrada = True
            
            # Frases de 2 palabras
            if not encontrada and i + 1 < len(palabras):
                frase2 = ' '.join(palabras[i:i+2])
                frase2_norm = self.normalizar_palabra(frase2)
                
                # Buscar tanto la frase normalizada como la original
                if (frase2_norm and frase2_norm in self.diccionario) or (frase2 in self.diccionario):
                    frase_final = frase2_norm if frase2_norm in self.diccionario else frase2
                    palabras_procesadas.append({
                        'original': frase2,
                        'normalizada': frase_final,
                        'es_tiempo': frase_final in self.palabras_tiempo,
                        'es_femenino': False,
                        'tipo': 'frase'
                    })
                    i += 2
                    encontrada = True
            
            # Palabra individual
            if not encontrada:
                palabra_norm = self.normalizar_palabra(palabras[i])
                
                # Omitir si es None
                if palabra_norm is None:
                    i += 1
                    continue
                
                # Verificar si es femenino
                es_femenino = palabras[i] in self.palabras_femeninas
                palabra_base = self.palabras_femeninas.get(palabras[i], palabra_norm)
                
                # Verificar si es número
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
        
        # Reordenar: TIEMPO al inicio
        palabras_tiempo = [p for p in palabras_procesadas if p.get('es_tiempo')]
        palabras_resto = [p for p in palabras_procesadas if not p.get('es_tiempo')]
        secuencia_final = palabras_tiempo + palabras_resto
        
        # Convertir a animaciones
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
                        'nombre': palabra['normalizada'],  # USAR NORMALIZADA para que frontend pueda buscar en diccionario
                        'categoria': info['categoria'],
                        'archivo': info['archivo'],
                        'es_deletreo': False
                    })
                    
                    # Agregar MUJER si es femenino
                    if palabra['es_femenino'] and 'mujer' in self.diccionario:
                        info_mujer = self.diccionario['mujer']
                        animaciones.append({
                            'nombre': 'mujer',  # USAR 'mujer' como nombre
                            'categoria': info_mujer['categoria'],
                            'archivo': info_mujer['archivo'],
                            'es_deletreo': False
                        })
                continue
            
            # Palabras desconocidas - deletrear
            if deletrear_desconocidas:
                palabras_deletreadas.append(palabra['original'])
                
                # Agregar DELETREAR
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
