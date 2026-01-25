"""
Translator API - Convierte texto en español a secuencias de señas
Utiliza NLP para mapear palabras a señas de lengua de señas venezolana
"""

import json
import re
from typing import List, Dict, Optional
from pathlib import Path


class SignTranslator:
    """
    Traductor de texto en español a lengua de señas venezolana
    """
    
    def __init__(self, dictionary_path: str = None):
        """
        Inicializa el traductor
        
        Args:
            dictionary_path: Ruta al diccionario de señas (opcional)
        """
        self.dictionary = {}
        self.synonyms = {}
        
        if dictionary_path and Path(dictionary_path).exists():
            self._load_dictionary(dictionary_path)
        else:
            self._create_default_dictionary()
    
    def _load_dictionary(self, path: str):
        """
        Carga diccionario desde archivo JSON
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.dictionary = data.get('dictionary', {})
                self.synonyms = data.get('synonyms', {})
            print(f"✅ Diccionario cargado: {len(self.dictionary)} palabras")
        except Exception as e:
            print(f"❌ Error cargando diccionario: {e}")
            self._create_default_dictionary()
    
    def _create_default_dictionary(self):
        """
        Crea un diccionario básico de señas
        """
        # Saludos y expresiones básicas
        self.dictionary = {
            # Saludos
            "hola": {"sign": "hola", "category": "saludo"},
            "buenos": {"sign": "buenos", "category": "saludo"},
            "dias": {"sign": "dias", "category": "saludo"},
            "tardes": {"sign": "tardes", "category": "saludo"},
            "noches": {"sign": "noches", "category": "saludo"},
            "adios": {"sign": "adios", "category": "saludo"},
            
            # Cortesía
            "gracias": {"sign": "gracias", "category": "cortesia"},
            "favor": {"sign": "favor", "category": "cortesia"},
            "por": {"sign": "por", "category": "cortesia"},
            "perdon": {"sign": "perdon", "category": "cortesia"},
            "disculpa": {"sign": "disculpa", "category": "cortesia"},
            
            # Pronombres
            "yo": {"sign": "yo", "category": "pronombre"},
            "tu": {"sign": "tu", "category": "pronombre"},
            "el": {"sign": "el", "category": "pronombre"},
            "ella": {"sign": "ella", "category": "pronombre"},
            "nosotros": {"sign": "nosotros", "category": "pronombre"},
            
            # Familia
            "mama": {"sign": "mama", "category": "familia"},
            "papa": {"sign": "papa", "category": "familia"},
            "hermano": {"sign": "hermano", "category": "familia"},
            "hermana": {"sign": "hermana", "category": "familia"},
            "hijo": {"sign": "hijo", "category": "familia"},
            "hija": {"sign": "hija", "category": "familia"},
            
            # Verbos comunes
            "ir": {"sign": "ir", "category": "verbo"},
            "venir": {"sign": "venir", "category": "verbo"},
            "hacer": {"sign": "hacer", "category": "verbo"},
            "ver": {"sign": "ver", "category": "verbo"},
            "comer": {"sign": "comer", "category": "verbo"},
            "beber": {"sign": "beber", "category": "verbo"},
            
            # Números (0-10)
            "cero": {"sign": "0", "category": "numero"},
            "uno": {"sign": "1", "category": "numero"},
            "dos": {"sign": "2", "category": "numero"},
            "tres": {"sign": "3", "category": "numero"},
            "cuatro": {"sign": "4", "category": "numero"},
            "cinco": {"sign": "5", "category": "numero"},
            "seis": {"sign": "6", "category": "numero"},
            "siete": {"sign": "7", "category": "numero"},
            "ocho": {"sign": "8", "category": "numero"},
            "nueve": {"sign": "9", "category": "numero"},
            "diez": {"sign": "10", "category": "numero"},
        }
        
        # Sinónimos
        self.synonyms = {
            "hola": ["saludos", "que tal", "hey"],
            "gracias": ["muchas gracias", "agradecido", "agradecida"],
            "adios": ["hasta luego", "chao", "nos vemos"],
            "perdon": ["disculpa", "disculpe", "perdona"],
        }
        
        print(f"📚 Diccionario base creado: {len(self.dictionary)} palabras")
    
    def translate(self, text: str) -> List[Dict]:
        """
        Traduce texto a secuencia de señas
        
        Args:
            text: Texto en español
            
        Returns:
            Lista de señas con metadata
        """
        # Normalizar texto
        text = text.lower().strip()
        text = self._normalize_text(text)
        
        # Dividir en palabras
        words = text.split()
        
        # Traducir palabra por palabra
        sign_sequence = []
        
        for word in words:
            sign_data = self._translate_word(word)
            if sign_data:
                sign_sequence.append(sign_data)
        
        return sign_sequence
    
    def _normalize_text(self, text: str) -> str:
        """
        Normaliza texto removiendo caracteres especiales
        """
        # Remover puntuación
        text = re.sub(r'[^\w\s]', '', text)
        
        # Remover espacios extra
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def _translate_word(self, word: str) -> Optional[Dict]:
        """
        Traduce una palabra individual
        
        Args:
            word: Palabra a traducir
            
        Returns:
            Diccionario con datos de la seña o None
        """
        # Buscar palabra directa
        if word in self.dictionary:
            sign_data = self.dictionary[word].copy()
            sign_data['original_word'] = word
            return sign_data
        
        # Buscar sinónimos
        for main_word, synonym_list in self.synonyms.items():
            if word in synonym_list:
                sign_data = self.dictionary[main_word].copy()
                sign_data['original_word'] = word
                sign_data['synonym_of'] = main_word
                return sign_data
        
        # Si no se encuentra, deletrear
        print(f"⚠️  '{word}' no encontrada, deletreando...")
        return {
            "sign": word,
            "category": "deletreo",
            "original_word": word,
            "spell_out": True
        }
    
    def get_word_category(self, word: str) -> Optional[str]:
        """
        Obtiene la categoría de una palabra
        """
        if word in self.dictionary:
            return self.dictionary[word].get('category')
        return None
    
    def add_word(self, word: str, sign: str, category: str = "general"):
        """
        Agrega una nueva palabra al diccionario
        
        Args:
            word: Palabra en español
            sign: Nombre de la seña correspondiente
            category: Categoría de la palabra
        """
        self.dictionary[word.lower()] = {
            "sign": sign,
            "category": category
        }
        print(f"✅ Palabra agregada: '{word}' -> seña '{sign}'")
    
    def save_dictionary(self, path: str):
        """
        Guarda el diccionario en archivo JSON
        """
        try:
            data = {
                "dictionary": self.dictionary,
                "synonyms": self.synonyms
            }
            
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Diccionario guardado en: {path}")
            return True
        except Exception as e:
            print(f"❌ Error guardando diccionario: {e}")
            return False


def test_translator():
    """
    Prueba del traductor
    """
    print("=" * 60)
    print("🧪 PRUEBA DE TRADUCTOR")
    print("=" * 60)
    
    translator = SignTranslator()
    
    test_sentences = [
        "hola",
        "buenos dias",
        "gracias",
        "yo estoy bien",
        "mama y papa",
        "uno dos tres"
    ]
    
    for sentence in test_sentences:
        print(f"\n📝 Texto: '{sentence}'")
        signs = translator.translate(sentence)
        print(f"🔤 Señas: {[s['sign'] for s in signs]}")
        print(f"📊 Detalles: {json.dumps(signs, indent=2, ensure_ascii=False)}")


if __name__ == "__main__":
    test_translator()
