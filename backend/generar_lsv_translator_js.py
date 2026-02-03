#!/usr/bin/env python3
"""
Script para generar lsv-translator.js con el diccionario actualizado
"""
import json
from pathlib import Path

# Leer diccionario desde data.json
data_path = Path(__file__).parent / 'scripts' / 'data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    diccionario = json.load(f)

# Generar el contenido JavaScript
js_content = '''// ====================================================================
// TRADUCTOR LSV STANDALONE PARA GITHUB PAGES
// Incluye diccionario completo y lógica de traducción
// Auto-generado desde backend/scripts/data.json
// ====================================================================

const LSV_TRANSLATOR = (function() {
    'use strict';
    
    // ====================================================================
    // DICCIONARIO LSV COMPLETO (''' + str(len(diccionario)) + ''' palabras - Actualizado desde Duvall)
    // ====================================================================
    const DICCIONARIO = ''' + json.dumps(diccionario, indent=4, ensure_ascii=False) + ''';
    
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
        'mes', 'semana', 'calendario', 'fin de semana', 'dia'
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
        texto = texto.replace(/[¿?¡!,.;:"\\'\\(\\)\\[\\]{}]/g, ' ');
        // Limpiar espacios múltiples
        texto = texto.replace(/\\s+/g, ' ');
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
        
        const palabrasProcesadas = [];
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
        version: '2.0.0',
        totalPalabras: ''' + str(len(diccionario)) + '''
    };
})();

// Exportar para uso global
if (typeof window !== 'undefined') {
    window.LSV_TRANSLATOR = LSV_TRANSLATOR;
}
'''

# Guardar en test/lsv-translator.js
output_path = Path(__file__).parent.parent / 'test' / 'lsv-translator.js'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f'✅ lsv-translator.js generado exitosamente!')
print(f'📊 Total de palabras: {len(diccionario)}')
print(f'📁 Guardado en: {output_path}')
