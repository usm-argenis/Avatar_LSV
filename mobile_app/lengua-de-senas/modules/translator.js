/**
 * LSVTranslator - Traductor de texto español a Lengua de Señas Venezolana (LSV)
 * 
 * Características:
 * - Normalización de texto (acentos, mayúsculas)
 * - Tokenización inteligente
 * - Mapeo a animaciones disponibles
 * - Deletreo automático de palabras sin seña
 * - Manejo de números y expresiones comunes
 */

class LSVTranslator {
    constructor() {
        this.dictionary = this._buildDictionary();
        this.alphabet = this._buildAlphabet();
        this.numbers = this._buildNumbers();
    }

    /**
     * Traducir texto a secuencia de animaciones
     * @param {string} text - Texto en español
     * @param {Object} options - Opciones de traducción
     * @returns {Array<string>} Lista de nombres de animaciones
     */
    translate(text, options = {}) {
        const {
            spellUnknownWords = true, // Deletrear palabras sin seña
            includeIdle = false, // Incluir idle entre palabras
            idleDuration = 0.5, // Duración de idle en segundos
            maxSpellingLength = 10 // Máximo de letras a deletrear
        } = options;

        console.log(`📝 Traduciendo: "${text}"`);

        // Normalizar texto
        const normalized = this._normalizeText(text);
        console.log(`🔄 Normalizado: "${normalized}"`);

        // Tokenizar
        const tokens = this._tokenize(normalized);
        console.log(`🔤 Tokens:`, tokens);

        // Mapear tokens a animaciones
        const animations = [];
        
        for (const token of tokens) {
            // Buscar en diccionario principal
            if (this.dictionary.has(token)) {
                animations.push(this.dictionary.get(token));
                if (includeIdle) animations.push('idle');
                continue;
            }

            // Buscar números
            if (this._isNumeric(token)) {
                const numberAnims = this._translateNumber(token);
                animations.push(...numberAnims);
                if (includeIdle) animations.push('idle');
                continue;
            }

            // Deletrear palabra desconocida
            if (spellUnknownWords && token.length <= maxSpellingLength) {
                console.log(`🔡 Deletreando: "${token}"`);
                const spelled = this._spellWord(token);
                animations.push(...spelled);
                if (includeIdle) animations.push('idle');
            } else {
                console.warn(`⚠️ Token "${token}" sin traducción y muy largo para deletrear`);
            }
        }

        console.log(`✅ Traducción completa: ${animations.length} animaciones`);
        console.log(`🎬 Secuencia:`, animations);

        return animations;
    }

    /**
     * Verificar si un texto tiene traducción directa
     * @param {string} text - Texto a verificar
     * @returns {boolean}
     */
    hasTranslation(text) {
        const normalized = this._normalizeText(text);
        return this.dictionary.has(normalized);
    }

    /**
     * Obtener animación para una palabra específica
     * @param {string} word - Palabra a buscar
     * @returns {string|null} Nombre de animación o null
     */
    getAnimation(word) {
        const normalized = this._normalizeText(word);
        return this.dictionary.get(normalized) || null;
    }

    /**
     * Agregar nueva palabra al diccionario
     * @param {string} word - Palabra en español
     * @param {string} animation - Nombre de animación correspondiente
     */
    addWord(word, animation) {
        const normalized = this._normalizeText(word);
        this.dictionary.set(normalized, animation);
        console.log(`➕ Añadido: "${word}" → ${animation}`);
    }

    /**
     * Obtener todas las palabras del diccionario
     * @returns {Array<string>}
     */
    getVocabulary() {
        return Array.from(this.dictionary.keys()).sort();
    }

    /**
     * Obtener estadísticas del diccionario
     * @returns {Object}
     */
    getStats() {
        return {
            totalWords: this.dictionary.size,
            alphabetSize: this.alphabet.size,
            numbersSupported: this.numbers.size,
            categories: this._getCategoryCount()
        };
    }

    // ============= MÉTODOS INTERNOS =============

    /**
     * Normalizar texto (minúsculas, sin acentos, sin puntuación)
     * @private
     */
    _normalizeText(text) {
        return text
            .toLowerCase()
            .normalize('NFD').replace(/[\u0300-\u036f]/g, '') // Quitar acentos
            .replace(/[^a-z0-9\s]/g, '') // Solo letras, números y espacios
            .trim();
    }

    /**
     * Tokenizar texto en palabras
     * @private
     */
    _tokenize(text) {
        return text.split(/\s+/).filter(token => token.length > 0);
    }

    /**
     * Verificar si es numérico
     * @private
     */
    _isNumeric(str) {
        return /^\d+$/.test(str);
    }

    /**
     * Deletrear palabra letra por letra
     * @private
     */
    _spellWord(word) {
        const letters = word.split('');
        return letters
            .map(letter => this.alphabet.get(letter))
            .filter(anim => anim !== undefined);
    }

    /**
     * Traducir número a señas
     * @private
     */
    _translateNumber(numStr) {
        const digits = numStr.split('');
        return digits
            .map(digit => this.numbers.get(digit))
            .filter(anim => anim !== undefined);
    }

    /**
     * Construir diccionario principal LSV
     * Basado en las animaciones disponibles de Nancy/Duvall/Luis
     * @private
     */
    _buildDictionary() {
        const dict = new Map();

        // === SALUDOS ===
        dict.set('hola', 'hola');
        dict.set('adios', 'adios');
        dict.set('chao', 'chao');
        dict.set('buenos dias', 'buenos_dias');
        dict.set('buenas tardes', 'buenas_tardes');
        dict.set('buenas noches', 'buenas_noches');
        dict.set('bienvenido', 'bienvenido');
        dict.set('bienvenida', 'bienvenido');

        // === CORTESÍA ===
        dict.set('gracias', 'gracias');
        dict.set('muchas gracias', 'muchas_gracias');
        dict.set('de nada', 'de_nada');
        dict.set('por favor', 'por_favor');
        dict.set('perdon', 'perdon');
        dict.set('disculpa', 'disculpa');
        dict.set('permiso', 'permiso');
        dict.set('mucho gusto', 'mucho_gusto');
        dict.set('buen provecho', 'buen_provecho');
        dict.set('a la orden', 'a_la_orden');

        // === PREGUNTAS ===
        dict.set('como estas', 'como_estas');
        dict.set('que tal', 'que_tal');
        dict.set('cual es tu nombre', 'cual_es_tu_nombre');
        dict.set('cual es tu sena', 'cual_es_tu_sena');
        dict.set('donde', 'donde');
        dict.set('cuando', 'cuando');
        dict.set('por que', 'por_que');
        dict.set('como', 'como');
        dict.set('quien', 'quien');
        dict.set('que', 'que');

        // === PRONOMBRES ===
        dict.set('yo', 'yo');
        dict.set('tu', 'tu');
        dict.set('el', 'el');
        dict.set('ella', 'ella');
        dict.set('nosotros', 'nosotros');
        dict.set('nosotras', 'nosotros');
        dict.set('ustedes', 'ustedes');
        dict.set('ellos', 'ellos');
        dict.set('ellas', 'ellas');
        dict.set('mi', 'mi');
        dict.set('mio', 'mio');
        dict.set('tuyo', 'tuyo');

        // === TIEMPO ===
        dict.set('hoy', 'hoy');
        dict.set('ayer', 'ayer');
        dict.set('manana', 'manana');
        dict.set('mañana', 'manana');
        dict.set('anteayer', 'anteayer');
        dict.set('pasado manana', 'pasado_manana');
        dict.set('ahora', 'ahora');
        dict.set('antes', 'antes');
        dict.set('despues', 'despues');
        dict.set('tarde', 'tarde');
        dict.set('temprano', 'temprano');

        // === DÍAS DE LA SEMANA ===
        dict.set('lunes', 'lunes');
        dict.set('martes', 'martes');
        dict.set('miercoles', 'miercoles');
        dict.set('jueves', 'jueves');
        dict.set('viernes', 'viernes');
        dict.set('sabado', 'sabado');
        dict.set('domingo', 'domingo');
        dict.set('semana', 'semana');
        dict.set('fin de semana', 'fin_de_semana');
        dict.set('dia', 'dia');
        dict.set('mes', 'mes');
        dict.set('ano', 'ano');
        dict.set('año', 'ano');

        // === EXPRESIONES ===
        dict.set('si', 'si');
        dict.set('no', 'no');
        dict.set('bien', 'bien');
        dict.set('mal', 'mal');
        dict.set('mas', 'mas');
        dict.set('menos', 'menos');
        dict.set('mucho', 'mucho');
        dict.set('poco', 'poco');
        dict.set('todo', 'todo');
        dict.set('nada', 'nada');
        dict.set('siempre', 'siempre');
        dict.set('nunca', 'nunca');
        dict.set('quizas', 'quizas');
        dict.set('quiza', 'quizas');

        // === VERBOS COMUNES ===
        dict.set('ser', 'ser');
        dict.set('estar', 'estar');
        dict.set('tener', 'tener');
        dict.set('hacer', 'hacer');
        dict.set('ir', 'ir');
        dict.set('venir', 'venir');
        dict.set('poder', 'poder');
        dict.set('querer', 'querer');
        dict.set('saber', 'saber');
        dict.set('decir', 'decir');
        dict.set('comer', 'comer');
        dict.set('beber', 'beber');
        dict.set('dormir', 'dormir');
        dict.set('trabajar', 'trabajar');
        dict.set('estudiar', 'estudiar');

        // === PALABRAS ADICIONALES ===
        dict.set('nombre', 'nombre');
        dict.set('sena', 'sena');
        dict.set('seña', 'sena');
        dict.set('familia', 'familia');
        dict.set('amigo', 'amigo');
        dict.set('casa', 'casa');
        dict.set('escuela', 'escuela');
        dict.set('trabajo', 'trabajo');
        dict.set('comida', 'comida');
        dict.set('agua', 'agua');
        dict.set('ayuda', 'ayuda');
        dict.set('importante', 'importante');
        dict.set('necesario', 'necesario');
        dict.set('posible', 'posible');
        dict.set('imposible', 'imposible');

        return dict;
    }

    /**
     * Construir mapeo de alfabeto
     * @private
     */
    _buildAlphabet() {
        const alphabet = new Map();
        
        // Letras a-z
        const letters = 'abcdefghijklmnopqrstuvwxyz'.split('');
        letters.forEach(letter => {
            alphabet.set(letter, `alfabeto_${letter}`);
        });

        // Letras especiales del español
        alphabet.set('ñ', 'alfabeto_ñ');
        alphabet.set('ch', 'alfabeto_ch');
        alphabet.set('ll', 'alfabeto_ll');
        alphabet.set('rr', 'alfabeto_rr');

        return alphabet;
    }

    /**
     * Construir mapeo de números
     * @private
     */
    _buildNumbers() {
        const numbers = new Map();
        
        for (let i = 0; i <= 10; i++) {
            numbers.set(i.toString(), `numero_${i}`);
        }

        return numbers;
    }

    /**
     * Contar palabras por categoría
     * @private
     */
    _getCategoryCount() {
        const categories = {
            saludos: ['hola', 'adios', 'chao', 'buenos_dias', 'buenas_tardes', 'buenas_noches', 'bienvenido'],
            cortesia: ['gracias', 'muchas_gracias', 'de_nada', 'por_favor', 'perdon', 'disculpa', 'permiso', 'mucho_gusto'],
            preguntas: ['como_estas', 'que_tal', 'cual_es_tu_nombre', 'donde', 'cuando', 'por_que', 'como', 'quien', 'que'],
            pronombres: ['yo', 'tu', 'el', 'ella', 'nosotros', 'ustedes', 'ellos', 'mi'],
            tiempo: ['hoy', 'ayer', 'manana', 'anteayer', 'ahora', 'antes', 'despues'],
            dias_semana: ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'],
            expresiones: ['si', 'no', 'bien', 'mal', 'mas', 'menos', 'mucho', 'poco', 'todo', 'nada']
        };

        const counts = {};
        for (const [cat, words] of Object.entries(categories)) {
            counts[cat] = words.length;
        }
        return counts;
    }
}

// Exportar para uso en diferentes entornos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LSVTranslator; // Node.js/React Native
} else {
    window.LSVTranslator = LSVTranslator; // Browser
}
