// ====================================================================
// TRADUCTOR LSV STANDALONE PARA GITHUB PAGES
// Incluye diccionario completo y lógica de traducción
// ====================================================================

const LSV_TRANSLATOR = (function() {
    'use strict';
    
    // ====================================================================
    // DICCIONARIO LSV COMPLETO (311 palabras)
    // ====================================================================
    const DICCIONARIO = {
        "0": {"categoria": "numero", "archivo": "0"},
        "1": {"categoria": "numero", "archivo": "1"},
        "2": {"categoria": "numero", "archivo": "2"},
        "3": {"categoria": "numero", "archivo": "3"},
        "4": {"categoria": "numero", "archivo": "4"},
        "5": {"categoria": "numero", "archivo": "5"},
        "6": {"categoria": "numero", "archivo": "6"},
        "7": {"categoria": "numero", "archivo": "7"},
        "8": {"categoria": "numero", "archivo": "8"},
        "9": {"categoria": "numero", "archivo": "9"},
        "10": {"categoria": "numero", "archivo": "10"},
        "1m": {"categoria": "numero", "archivo": "1M"},
        "a": {"categoria": "alfabeto", "archivo": "a"},
        "b": {"categoria": "alfabeto", "archivo": "b"},
        "c": {"categoria": "alfabeto", "archivo": "c"},
        "d": {"categoria": "alfabeto", "archivo": "d"},
        "e": {"categoria": "alfabeto", "archivo": "e"},
        "f": {"categoria": "alfabeto", "archivo": "f"},
        "g": {"categoria": "alfabeto", "archivo": "g"},
        "h": {"categoria": "alfabeto", "archivo": "h"},
        "i": {"categoria": "alfabeto", "archivo": "i"},
        "j": {"categoria": "alfabeto", "archivo": "j"},
        "k": {"categoria": "alfabeto", "archivo": "k"},
        "l": {"categoria": "alfabeto", "archivo": "l"},
        "m": {"categoria": "alfabeto", "archivo": "m"},
        "n": {"categoria": "alfabeto", "archivo": "n"},
        "o": {"categoria": "alfabeto", "archivo": "o"},
        "p": {"categoria": "alfabeto", "archivo": "p"},
        "q": {"categoria": "alfabeto", "archivo": "q"},
        "r": {"categoria": "alfabeto", "archivo": "r"},
        "t": {"categoria": "alfabeto", "archivo": "t"},
        "u": {"categoria": "alfabeto", "archivo": "u"},
        "v": {"categoria": "alfabeto", "archivo": "v"},
        "w": {"categoria": "alfabeto", "archivo": "w"},
        "x": {"categoria": "alfabeto", "archivo": "x"},
        "y": {"categoria": "alfabeto", "archivo": "y"},
        "z": {"categoria": "alfabeto", "archivo": "z"},
        "ñ": {"categoria": "alfabeto", "archivo": "ñ"},
        
        // Palabras LSV
        "hola": {"categoria": "saludos", "archivo": "hola"},
        "adios": {"categoria": "saludos", "archivo": "adios"},
        "buenos dias": {"categoria": "saludos", "archivo": "buenos dias"},
        "buenas tardes": {"categoria": "saludos", "archivo": "buenas tardes"},
        "buenas noches": {"categoria": "saludos", "archivo": "buenas noches"},
        "chao": {"categoria": "saludos", "archivo": "chao"},
        "bienvenido": {"categoria": "saludos", "archivo": "bienvenido"},
        
        "gracias": {"categoria": "cortesia", "archivo": "gracias"},
        "muchas gracias": {"categoria": "cortesia", "archivo": "muchas gracias"},
        "buen provecho": {"categoria": "cortesia", "archivo": "buen provecho"},
        "permiso": {"categoria": "cortesia", "archivo": "permiso"},
        "de nada": {"categoria": "expresiones", "archivo": "de nada"},
        "mucho gusto": {"categoria": "cortesia", "archivo": "mucho gusto"},
        "a la orden": {"categoria": "cortesia", "archivo": "a la orden"},
        
        "yo": {"categoria": "pronombres", "archivo": "yo"},
        "tu": {"categoria": "pronombres", "archivo": "tu"},
        "el": {"categoria": "pronombres", "archivo": "el"},
        "ella": {"categoria": "pronombres", "archivo": "ella"},
        "nosotros": {"categoria": "pronombres", "archivo": "nosotros"},
        "ustedes": {"categoria": "pronombres", "archivo": "ustedes"},
        "ellos": {"categoria": "pronombres", "archivo": "ellos"},
        "ellas": {"categoria": "pronombres", "archivo": "ellas"},
        "mio": {"categoria": "pronombres", "archivo": "mio"},
        "tuyo": {"categoria": "pronombres", "archivo": "tuyo"},
        "suyo": {"categoria": "pronombres", "archivo": "suyo"},
        "nuestro": {"categoria": "pronombres", "archivo": "nuestro"},
        
        "trabajar": {"categoria": "verbos", "archivo": "trabajar"},
        "estudiar": {"categoria": "verbos", "archivo": "estudiar"},
        "comer": {"categoria": "verbos", "archivo": "comer"},
        "vivir": {"categoria": "verbos", "archivo": "vivir"},
        "dormir": {"categoria": "verbos", "archivo": "dormir"},
        "ver": {"categoria": "verbos", "archivo": "ver"},
        "estar": {"categoria": "verbos", "archivo": "estar"},
        "amar": {"categoria": "verbos", "archivo": "amar"},
        "ayudar": {"categoria": "verbos", "archivo": "ayudar"},
        "cansar": {"categoria": "verbos", "archivo": "cansar"},
        "conocer": {"categoria": "verbos", "archivo": "conocer"},
        "decir": {"categoria": "verbos", "archivo": "decir"},
        "deletrear": {"categoria": "verbos", "archivo": "deletrear"},
        "invitar": {"categoria": "verbos", "archivo": "invitar"},
        "preguntar": {"categoria": "verbos", "archivo": "preguntar"},
        "presentar": {"categoria": "verbos", "archivo": "presentar"},
        "querer": {"categoria": "verbos", "archivo": "querer"},
        "responder": {"categoria": "verbos", "archivo": "responder"},
        "saludar": {"categoria": "verbos", "archivo": "saludar"},
        "sentir": {"categoria": "verbos", "archivo": "sentir"},
        
        "hombre": {"categoria": "personas", "archivo": "hombre"},
        "mujer": {"categoria": "personas", "archivo": "mujer"},
        "niño": {"categoria": "personas", "archivo": "niño"},
        "joven": {"categoria": "personas", "archivo": "joven"},
        "adulto": {"categoria": "personas", "archivo": "adulto"},
        "anciano": {"categoria": "personas", "archivo": "anciano"},
        "mayor": {"categoria": "personas", "archivo": "mayor"},
        "bebe": {"categoria": "personas", "archivo": "bebe"},
        "amigo": {"categoria": "personas", "archivo": "amigo"},
        "compañero": {"categoria": "personas", "archivo": "compañero"},
        "novio": {"categoria": "personas", "archivo": "novio"},
        "señor": {"categoria": "personas", "archivo": "señor"},
        "señorita": {"categoria": "personas", "archivo": "señorita"},
        "persona": {"categoria": "personas", "archivo": "persona"},
        "personas": {"categoria": "personas", "archivo": "personas"},
        "viejo": {"categoria": "personas", "archivo": "viejo"},
        "ciego": {"categoria": "personas", "archivo": "ciego"},
        "sordo": {"categoria": "personas", "archivo": "sordo"},
        "sordociego": {"categoria": "personas", "archivo": "sordociego"},
        "oyente": {"categoria": "personas", "archivo": "oyente"},
        "mayor de edad": {"categoria": "personas", "archivo": "mayor de edad"},
        "menor de edad": {"categoria": "personas", "archivo": "menor de edad"},
        
        "ingeniero": {"categoria": "profesiones", "archivo": "ingeniero"},
        "medico": {"categoria": "profesiones", "archivo": "medico"},
        "profesor": {"categoria": "profesiones", "archivo": "profesor"},
        "abogado": {"categoria": "profesiones", "archivo": "abogado"},
        "enfermera": {"categoria": "profesiones", "archivo": "enfermera"},
        "maestro": {"categoria": "profesiones", "archivo": "maestro"},
        "policia": {"categoria": "profesiones", "archivo": "policia"},
        "contador": {"categoria": "profesiones", "archivo": "contador"},
        "administrador": {"categoria": "profesiones", "archivo": "administrador"},
        "director": {"categoria": "profesiones", "archivo": "director"},
        "gerente": {"categoria": "profesiones", "archivo": "gerente"},
        "psicologo": {"categoria": "profesiones", "archivo": "psicologo"},
        "dentista": {"categoria": "profesiones", "archivo": "dentista"},
        "licenciado": {"categoria": "profesiones", "archivo": "licenciado"},
        "ingeniera": {"categoria": "profesiones", "archivo": "ingeniero"},
        "doctora": {"categoria": "profesiones", "archivo": "medico"},
        "profesora": {"categoria": "profesiones", "archivo": "profesor"},
        "profesion": {"categoria": "profesiones", "archivo": "profesion"},
        "carrera": {"categoria": "profesiones", "archivo": "carrera"},
        
        "ayer": {"categoria": "tiempo", "archivo": "ayer"},
        "hoy": {"categoria": "tiempo", "archivo": "hoy"},
        "mañana": {"categoria": "tiempo", "archivo": "mañana"},
        "anteayer": {"categoria": "tiempo", "archivo": "anteayer"},
        "pasado mañana": {"categoria": "tiempo", "archivo": "pasado mañana"},
        "lunes": {"categoria": "tiempo", "archivo": "lunes"},
        "martes": {"categoria": "tiempo", "archivo": "martes"},
        "miercoles": {"categoria": "tiempo", "archivo": "miercoles"},
        "jueves": {"categoria": "tiempo", "archivo": "jueves"},
        "viernes": {"categoria": "tiempo", "archivo": "viernes"},
        "sabado": {"categoria": "tiempo", "archivo": "sabado"},
        "domingo": {"categoria": "tiempo", "archivo": "domingo"},
        "mes": {"categoria": "tiempo", "archivo": "mes"},
        "semana": {"categoria": "tiempo", "archivo": "semana"},
        "calendario": {"categoria": "tiempo", "archivo": "calendario"},
        "fin de semana": {"categoria": "tiempo", "archivo": "fin de semana"},
        
        "enero": {"categoria": "expresiones", "archivo": "enero"},
        "febrero": {"categoria": "expresiones", "archivo": "febrero"},
        "marzo": {"categoria": "expresiones", "archivo": "marzo"},
        "abril": {"categoria": "expresiones", "archivo": "abril"},
        "mayo": {"categoria": "expresiones", "archivo": "mayo"},
        "junio": {"categoria": "expresiones", "archivo": "junio"},
        "julio": {"categoria": "expresiones", "archivo": "julio"},
        "agosto": {"categoria": "expresiones", "archivo": "agosto"},
        "septiembre": {"categoria": "expresiones", "archivo": "septiembre"},
        "octubre": {"categoria": "expresiones", "archivo": "octubre"},
        "noviembre": {"categoria": "expresiones", "archivo": "noviembre"},
        "diciembre": {"categoria": "expresiones", "archivo": "diciembre"},
        
        "como estas": {"categoria": "interrogantes", "archivo": "como estas"},
        "que tal": {"categoria": "interrogantes", "archivo": "que tal"},
        "cual es tu nombre": {"categoria": "interrogantes", "archivo": "cual es tu nombre"},
        "cual es tu sena": {"categoria": "interrogantes", "archivo": "cual es tu sena"},
        
        "bien": {"categoria": "expresiones", "archivo": "bien"},
        "mal": {"categoria": "expresiones", "archivo": "mal"},
        "regular": {"categoria": "expresiones", "archivo": "regular"},
        "si": {"categoria": "expresiones", "archivo": "si"},
        "no": {"categoria": "expresiones", "archivo": "no"},
        "como": {"categoria": "expresiones", "archivo": "como"},
        "donde": {"categoria": "expresiones", "archivo": "donde"},
        "cuando": {"categoria": "expresiones", "archivo": "cuando"},
        "que": {"categoria": "expresiones", "archivo": "que"},
        "quien": {"categoria": "expresiones", "archivo": "quien"},
        "cual": {"categoria": "expresiones", "archivo": "cual"},
        "porque": {"categoria": "expresiones", "archivo": "porque"},
        "cuantos": {"categoria": "expresiones", "archivo": "cuantos"},
        
        "mucho": {"categoria": "preposiciones", "archivo": "mucho"},
        "poco": {"categoria": "preposiciones", "archivo": "poco"},
        "todo": {"categoria": "preposiciones", "archivo": "todo"},
        "nada": {"categoria": "preposiciones", "archivo": "nada"},
        "algo": {"categoria": "preposiciones", "archivo": "algo"},
        "alguien": {"categoria": "preposiciones", "archivo": "alguien"},
        "algun": {"categoria": "preposiciones", "archivo": "algun"},
        "nadie": {"categoria": "preposiciones", "archivo": "nadie"},
        "ningun": {"categoria": "preposiciones", "archivo": "ningun"},
        "otro": {"categoria": "preposiciones", "archivo": "otro"},
        "mas": {"categoria": "preposiciones", "archivo": "mas"},
        "demasiado": {"categoria": "preposiciones", "archivo": "demasiado"},
        "bastante": {"categoria": "preposiciones", "archivo": "bastante"},
        "cualquier": {"categoria": "preposiciones", "archivo": "cualquier"},
        "quienquiera": {"categoria": "preposiciones", "archivo": "quienquiera"},
        
        "casado": {"categoria": "estado_civil", "archivo": "casado"},
        "soltero": {"categoria": "estado_civil", "archivo": "soltero"},
        "divorciado": {"categoria": "estado_civil", "archivo": "divorciado"},
        "viudo": {"categoria": "estado_civil", "archivo": "viudo"},
        "separado": {"categoria": "estado_civil", "archivo": "separado"},
        "concubino": {"categoria": "estado_civil", "archivo": "concubino"},
        
        "casa": {"categoria": "viviendas", "archivo": "casa"},
        "apartamento": {"categoria": "viviendas", "archivo": "apartamento"},
        "edificio": {"categoria": "viviendas", "archivo": "edificio"},
        "rancho": {"categoria": "viviendas", "archivo": "rancho"},
        "sala": {"categoria": "viviendas", "archivo": "sala"},
        "cocina": {"categoria": "viviendas", "archivo": "cocina"},
        "comedor": {"categoria": "viviendas", "archivo": "comedor"},
        "baño": {"categoria": "viviendas", "archivo": "baño"},
        "cuarto": {"categoria": "viviendas", "archivo": "cuarto"},
        "piso": {"categoria": "viviendas", "archivo": "piso"},
        
        "cerca": {"categoria": "adverbios", "archivo": "cerca"},
        "lejos": {"categoria": "adverbios", "archivo": "lejos"},
        "derecha": {"categoria": "adverbios", "archivo": "derecha"},
        "izquierda": {"categoria": "adverbios", "archivo": "izquierda"},
        "frente": {"categoria": "adverbios", "archivo": "frente"},
        "atras": {"categoria": "adverbios", "archivo": "atras"},
        "al lado": {"categoria": "adverbios", "archivo": "al lado"},
        "lugares": {"categoria": "adverbios", "archivo": "lugares"},
        "adverbios": {"categoria": "adverbios", "archivo": "adverbios"}
    };
    
    // ====================================================================
    // REGLAS LSV
    // ====================================================================
    
    const PALABRAS_OMITIDAS = new Set([
        'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas',
        'de', 'del', 'al', 'a', 'y', 'e', 'o', 'u',
        'se', 'me', 'te', 'le', 'les', 'nos',
        'es', 'son', 'esta', 'están'
    ]);
    
    const PALABRAS_TIEMPO = new Set([
        'ayer', 'hoy', 'mañana', 'anteayer', 'pasado mañana',
        'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo',
        'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
        'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre',
        'mes', 'semana', 'calendario', 'fin de semana'
    ]);
    
    const PALABRAS_FEMENINAS = {
        'ingeniera': 'ingeniero',
        'doctora': 'medico',
        'profesora': 'profesor',
        'abogada': 'abogado',
        'maestra': 'maestro',
        'señora': 'señor',
        'señorita': 'señor',
        'amiga': 'amigo',
        'novia': 'novio',
        'niña': 'niño',
        'compañera': 'compañero'
    };
    
    const NORMALIZACION_VERBOS = {
        'trabajo': 'trabajar', 'trabajas': 'trabajar', 'trabaja': 'trabajar',
        'trabajamos': 'trabajar', 'trabajan': 'trabajar', 'trabajé': 'trabajar',
        'estudio': 'estudiar', 'estudias': 'estudiar', 'estudia': 'estudiar',
        'como': 'comer', 'comes': 'comer', 'come': 'comer',
        'vivo': 'vivir', 'vives': 'vivir', 'vive': 'vivir',
        'estoy': 'estar', 'estás': 'estar', 'está': 'estar',
        'soy': null, 'eres': null, 'somos': null, 'son': null  // Se omiten
    };
    
    const NORMALIZACION_PLURALES = {
        'todos': 'todo', 'todas': 'todo',
        'muchos': 'mucho', 'muchas': 'mucho',
        'pocos': 'poco', 'pocas': 'poco',
        'mi': 'mio', 'mis': 'mio',
        'tu': 'tuyo', 'tus': 'tuyo',
        'nosotras': 'nosotros'
    };
    
    // ====================================================================
    // FUNCIONES DE TRADUCCIÓN
    // ====================================================================
    
    function limpiarTexto(texto) {
        // Eliminar signos de puntuación
        texto = texto.replace(/[¿?¡!,.;:"\'\(\)\[\]{}]/g, ' ');
        // Limpiar espacios múltiples
        texto = texto.replace(/\s+/g, ' ');
        return texto.toLowerCase().trim();
    }
    
    function normalizarPalabra(palabra) {
        if (PALABRAS_OMITIDAS.has(palabra)) return null;
        if (NORMALIZACION_VERBOS[palabra] !== undefined) return NORMALIZACION_VERBOS[palabra];
        if (NORMALIZACION_PLURALES[palabra]) return NORMALIZACION_PLURALES[palabra];
        if (DICCIONARIO[palabra]) return palabra;
        
        // Intentar quitar 's' final (plural)
        if (palabra.endsWith('s') && palabra.length > 3) {
            const singular = palabra.slice(0, -1);
            if (DICCIONARIO[singular]) return singular;
        }
        
        return palabra;
    }
    
    function traducirTexto(texto, opciones = {}) {
        const {
            deletrearDesconocidas = true,
            velocidadDeletreo = 1.2
        } = opciones;
        
        texto = limpiarTexto(texto);
        const palabras = texto.split(' ').filter(p => p);
        
        const palabrasProces adas = [];
        let i = 0;
        
        // Procesar frases compuestas y palabras
        while (i < palabras.length) {
            let encontrada = false;
            
            // Frases de 4 palabras
            if (i + 3 < palabras.length) {
                const frase4 = palabras.slice(i, i + 4).join(' ');
                if (DICCIONARIO[frase4]) {
                    palabrasProcesadas.push({
                        original: frase4,
                        normalizada: frase4,
                        esTiempo: PALABRAS_TIEMPO.has(frase4),
                        esFemenino: false,
                        tipo: 'frase'
                    });
                    i += 4;
                    encontrada = true;
                }
            }
            
            // Frases de 3 palabras
            if (!encontrada && i + 2 < palabras.length) {
                const frase3 = palabras.slice(i, i + 3).join(' ');
                if (DICCIONARIO[frase3]) {
                    palabrasProcesadas.push({
                        original: frase3,
                        normalizada: frase3,
                        esTiempo: PALABRAS_TIEMPO.has(frase3),
                        esFemenino: false,
                        tipo: 'frase'
                    });
                    i += 3;
                    encontrada = true;
                }
            }
            
            // Frases de 2 palabras
            if (!encontrada && i + 1 < palabras.length) {
                const frase2 = palabras.slice(i, i + 2).join(' ');
                if (DICCIONARIO[frase2]) {
                    palabrasProcesadas.push({
                        original: frase2,
                        normalizada: frase2,
                        esTiempo: PALABRAS_TIEMPO.has(frase2),
                        esFemenino: false,
                        tipo: 'frase'
                    });
                    i += 2;
                    encontrada = true;
                }
            }
            
            // Palabra individual
            if (!encontrada) {
                const palabraNorm = normalizarPalabra(palabras[i]);
                
                if (palabraNorm === null) {
                    i++;
                    continue;
                }
                
                const esFemenino = PALABRAS_FEMENINAS[palabras[i]] !== undefined;
                const palabraBase = PALABRAS_FEMENINAS[palabras[i]] || palabraNorm;
                
                palabrasProcesadas.push({
                    original: palabras[i],
                    normalizada: palabraBase,
                    esTiempo: PALABRAS_TIEMPO.has(palabraBase),
                    esFemenino: esFemenino,
                    tipo: DICCIONARIO[palabraBase] ? 'palabra' : 'desconocida'
                });
                i++;
            }
        }
        
        // Reordenar: TIEMPO al inicio
        const palabrasTiempo = palabrasProcesadas.filter(p => p.esTiempo);
        const palabrasResto = palabrasProcesadas.filter(p => !p.esTiempo);
        const secuenciaFinal = [...palabrasTiempo, ...palabrasResto];
        
        // Convertir a animaciones
        const animaciones = [];
        const palabrasDeletreadas = [];
        
        for (const palabra of secuenciaFinal) {
            if (palabra.tipo === 'palabra' || palabra.tipo === 'frase') {
                if (DICCIONARIO[palabra.normalizada]) {
                    const info = DICCIONARIO[palabra.normalizada];
                    animaciones.push({
                        nombre: palabra.normalizada,
                        categoria: info.categoria,
                        archivo: info.archivo,
                        esDeletreo: false
                    });
                    
                    // Agregar MUJER si es femenino
                    if (palabra.esFemenino && DICCIONARIO['mujer']) {
                        animaciones.push({
                            nombre: 'mujer',
                            categoria: 'personas',
                            archivo: 'mujer',
                            esDeletreo: false
                        });
                    }
                }
            } else if (deletrearDesconocidas) {
                palabrasDeletreadas.push(palabra.original);
                
                // Señal DELETREAR
                if (DICCIONARIO['deletrear']) {
                    animaciones.push({
                        nombre: 'deletrear',
                        categoria: 'verbos',
                        archivo: 'deletrear',
                        esDeletreo: true
                    });
                }
                
                // Deletrear cada letra
                for (const letra of palabra.original) {
                    if (DICCIONARIO[letra.toLowerCase()]) {
                        animaciones.push({
                            nombre: letra.toLowerCase(),
                            categoria: 'alfabeto',
                            archivo: letra.toLowerCase(),
                            esDeletreo: true,
                            duracion: velocidadDeletreo
                        });
                    }
                }
            }
        }
        
        return {
            textoOriginal: texto,
            animaciones: animaciones,
            totalAnimaciones: animaciones.length,
            palabrasDeletreadas: palabrasDeletreadas
        };
    }
    
    // ====================================================================
    // API PÚBLICA
    // ====================================================================
    
    return {
        translate: traducirTexto,
        getDiccionario: () => DICCIONARIO,
        version: '1.0.0'
    };
})();

// Exportar para uso global
if (typeof window !== 'undefined') {
    window.LSV_TRANSLATOR = LSV_TRANSLATOR;
}
