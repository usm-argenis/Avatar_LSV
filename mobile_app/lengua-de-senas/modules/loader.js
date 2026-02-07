/**
 * AvatarLoader - Módulo para cargar avatares 3D y sus animaciones
 * Compatible con Three.js y React Native (expo-three)
 * 
 * Características:
 * - Carga el modelo base una sola vez
 * - Extrae animaciones de archivos externos
 * - Gestiona múltiples avatares (Nancy, Duvall, Luis)
 * - Optimizado para móviles
 */

class AvatarLoader {
    constructor(THREE, GLTFLoader, customBaseURL = null) {
        this.THREE = THREE;
        this.GLTFLoader = GLTFLoader;
        this.avatars = new Map(); // { name: { model, animations, mixer, skeleton } }
        this.loadingCallbacks = new Map();
        this.errorCallbacks = new Map();
        
        // URL base del servidor HTTP que sirve los archivos GLB
        // Puede ser sobreescrita pasando customBaseURL en el constructor
        // Por defecto: http://192.168.86.27:8000/
        this.BASE_URL = customBaseURL || 'http://192.168.86.27:8000/';
        
        console.log(`🌐 AvatarLoader configurado con BASE_URL: ${this.BASE_URL}`);
    }

    /**
     * Mapeo de animaciones a sus categorías específicas
     * Esto permite cargar la animación desde la carpeta correcta
     */
    static ANIMATION_CATEGORIES = {
        // Saludos
        'hola': 'saludos',
        'adios': 'saludos',
        'chao': 'saludos',
        'buenos_dias': 'saludos',
        'buenas_tardes': 'saludos',
        'buenas_noches': 'saludos',
        'bienvenido': 'saludos',
        
        // Cortesía
        'gracias': 'cortesia',
        'muchas_gracias': 'cortesia',
        'de_nada': 'cortesia',
        'por_favor': 'cortesia',
        'perdon': 'cortesia',
        'disculpa': 'cortesia',
        'permiso': 'cortesia',
        'mucho_gusto': 'cortesia',
        'buen_provecho': 'cortesia',
        'a_la_orden': 'cortesia',
        
        // Preguntas
        'como_estas': 'preguntas',
        'que_tal': 'preguntas',
        'cual_es_tu_nombre': 'preguntas',
        'cual_es_tu_sena': 'preguntas',
        'donde': 'preguntas',
        'cuando': 'preguntas',
        'por_que': 'preguntas',
        'como': 'preguntas',
        'quien': 'preguntas',
        'que': 'preguntas',
        
        // Pronombres
        'yo': 'pronombres',
        'tu': 'pronombres',
        'el': 'pronombres',
        'ella': 'pronombres',
        'nosotros': 'pronombres',
        'ustedes': 'pronombres',
        'ellos': 'pronombres',
        'ellas': 'pronombres',
        'mi': 'pronombres',
        'mio': 'pronombres',
        'tuyo': 'pronombres',
        
        // Tiempo
        'hoy': 'tiempo',
        'ayer': 'tiempo',
        'manana': 'tiempo',
        'anteayer': 'tiempo',
        'pasado_manana': 'tiempo',
        'ahora': 'tiempo',
        'antes': 'tiempo',
        'despues': 'tiempo',
        'tarde': 'tiempo',
        'temprano': 'tiempo',
        
        // Días de la semana
        'lunes': 'dias_semana',
        'martes': 'dias_semana',
        'miercoles': 'dias_semana',
        'jueves': 'dias_semana',
        'viernes': 'dias_semana',
        'sabado': 'dias_semana',
        'domingo': 'dias_semana',
        'semana': 'dias_semana',
        'fin_de_semana': 'dias_semana',
        'dia': 'dias_semana',
        'mes': 'dias_semana',
        'ano': 'dias_semana',
        
        // Expresiones
        'si': 'expresiones',
        'no': 'expresiones',
        'bien': 'expresiones',
        'mal': 'expresiones',
        'mas': 'expresiones',
        'menos': 'expresiones',
        'mucho': 'expresiones',
        'poco': 'expresiones',
        'todo': 'expresiones',
        'nada': 'expresiones',
        'siempre': 'expresiones',
        'nunca': 'expresiones',
        'quizas': 'expresiones',
        
        // Verbos
        'ser': 'verbos',
        'estar': 'verbos',
        'tener': 'verbos',
        'hacer': 'verbos',
        'ir': 'verbos',
        'venir': 'verbos',
        'poder': 'verbos',
        'querer': 'verbos',
        'saber': 'verbos',
        'decir': 'verbos',
        'comer': 'verbos',
        'beber': 'verbos',
        'dormir': 'verbos',
        'trabajar': 'verbos',
        'estudiar': 'verbos',
        'agarrar': 'verbos',
        'amar': 'verbos',
        'atraer': 'verbos',
        'ayudar': 'verbos',
        'burlar': 'verbos',
        'calmar': 'verbos',
        'cansar': 'verbos',
        'conocer': 'verbos',
        'deletrear': 'verbos',
        'enganar': 'verbos',
        'guardar': 'verbos',
        'invitar': 'verbos',
        'llevar': 'verbos',
        'pelear': 'verbos',
        'preguntar': 'verbos',
        'presentar': 'verbos',
        'regalar': 'verbos',
        'responder': 'verbos',
        'saludar': 'verbos',
        'sentir': 'verbos',
        'sufrir': 'verbos',
        'traer': 'verbos',
        'usar': 'verbos',
        'ver': 'verbos',
        'verbo': 'verbos',
        'vestir': 'verbos',
        'vivir': 'verbos',
        
        // Palabras adicionales (expresiones generales)
        'nombre': 'expresiones',
        'sena': 'expresiones',
        'familia': 'expresiones',
        'amigo': 'expresiones',
        'casa': 'expresiones',
        'escuela': 'expresiones',
        'trabajo': 'expresiones',
        'comida': 'expresiones',
        'agua': 'expresiones',
        'ayuda': 'expresiones',
        'importante': 'expresiones',
        'necesario': 'expresiones',
        'posible': 'expresiones',
        'imposible': 'expresiones'
    };

    /**
     * Configuración de rutas para cada avatar
     * Modificar estas rutas según tu estructura de proyecto
     */
    static AVATAR_PATHS = {
        Nancy: {
            base: 'output/glb/Nancy/Nancy.glb',
            animations: {
                saludos: 'output/glb/Nancy/saludos/',
                tiempo: 'output/glb/Nancy/tiempo/',
                dias_semana: 'output/glb/Nancy/dias_semana/',
                alfabeto: 'output/glb/Nancy/alfabeto/',
                pronombres: 'output/glb/Nancy/pronombres/',
                expresiones: 'output/glb/Nancy/expresiones/',
                cortesia: 'output/glb/Nancy/cortesia/',
                preguntas: 'output/glb/Nancy/preguntas/',
                verbos: 'output/glb/Nancy/verbos/',
                numero: 'output/glb/Nancy/numero/'
            }
        },
        Duvall: {
            base: 'output/glb/Duvall/Duvall.glb',
            animations: {
                saludos: 'output/glb/Duvall/saludos/',
                tiempo: 'output/glb/Duvall/tiempo/',
                dias_semana: 'output/glb/Duvall/dias_semana/',
                alfabeto: 'output/glb/Duvall/alfabeto/',
                pronombres: 'output/glb/Duvall/pronombres/',
                expresiones: 'output/glb/Duvall/expresiones/',
                cortesia: 'output/glb/Duvall/cortesia/',
                preguntas: 'output/glb/Duvall/preguntas/',
                verbos: 'output/glb/Duvall/verbos/',
                numero: 'output/glb/Duvall/numero/'
            }
        },
        luis: {
            base: 'output/glb/Luis/Luis.glb',
            animations: {
                saludos: 'output/glb/Luis/saludos/',
                tiempo: 'output/glb/Luis/tiempo/',
                dias_semana: 'output/glb/Luis/dias_semana/',
                alfabeto: 'output/glb/Luis/alfabeto/',
                pronombres: 'output/glb/Luis/pronombres/',
                expresiones: 'output/glb/Luis/expresiones/',
                cortesia: 'output/glb/Luis/cortesia/',
                preguntas: 'output/glb/Luis/preguntas/',
                verbos: 'output/glb/Luis/verbos/',
                numero: 'output/glb/Luis/numero/'
            }
        },
        Carlos: {
            base: 'output/glb/Carlos/Carlos.glb',
            animations: {
                saludos: 'output/glb/Carlos/saludos/',
                tiempo: 'output/glb/Carlos/tiempo/',
                dias_semana: 'output/glb/Carlos/dias_semana/',
                alfabeto: 'output/glb/Carlos/alfabeto/',
                pronombres: 'output/glb/Carlos/pronombres/',
                expresiones: 'output/glb/Carlos/expresiones/',
                cortesia: 'output/glb/Carlos/cortesia/',
                preguntas: 'output/glb/Carlos/preguntas/',
                verbos: 'output/glb/Carlos/verbos/',
                numero: 'output/glb/Carlos/numero/'
            }
        },
        Carla: {
            base: 'output/glb/Carla/Carla.glb',
            animations: {
                saludos: 'output/glb/Carla/saludos/',
                tiempo: 'output/glb/Carla/tiempo/',
                dias_semana: 'output/glb/Carla/dias_semana/',
                alfabeto: 'output/glb/Carla/alfabeto/',
                pronombres: 'output/glb/Carla/pronombres/',
                expresiones: 'output/glb/Carla/expresiones/',
                cortesia: 'output/glb/Carla/cortesia/',
                preguntas: 'output/glb/Carla/preguntas/',
                verbos: 'output/glb/Carla/verbos/',
                numero: 'output/glb/Carla/numero/'
            }
        },
       
    };

    /**
     * Cargar avatar base y preparar para animaciones
     * @param {string} avatarName - Nombre del avatar (Nancy, Duvall, Luis)
     * @param {function} onProgress - Callback de progreso (opcional)
     * @returns {Promise<Object>} Avatar cargado con estructura
     */
    async loadAvatar(avatarName, onProgress = null) {
        return new Promise((resolve, reject) => {
            const config = AvatarLoader.AVATAR_PATHS[avatarName];
            if (!config) {
                reject(new Error(`Avatar "${avatarName}" no encontrado. Disponibles: ${Object.keys(AvatarLoader.AVATAR_PATHS).join(', ')}`));
                return;
            }

            console.log(`🔄 Cargando avatar base: ${avatarName}...`);
            
            const loader = new this.GLTFLoader();
            const fullPath = this.BASE_URL + config.base;
            console.log(`📍 Ruta completa: ${fullPath}`);
            
            loader.load(
                fullPath,
                (gltf) => {
                    console.log(`✅ Avatar ${avatarName} cargado exitosamente`);
                    
                    // Extraer componentes del modelo
                    const model = gltf.scene;
                    const skeleton = this._extractSkeleton(model);
                    const mixer = new this.THREE.AnimationMixer(model);

                    // Guardar avatar en caché
                    const avatarData = {
                        name: avatarName,
                        model: model,
                        skeleton: skeleton,
                        mixer: mixer,
                        animations: new Map(), // { animationName: THREE.AnimationClip }
                        config: config,
                        loaded: true
                    };

                    this.avatars.set(avatarName, avatarData);
                    
                    // Callback de éxito
                    if (this.loadingCallbacks.has(avatarName)) {
                        this.loadingCallbacks.get(avatarName)(avatarData);
                    }
                    
                    resolve(avatarData);
                },
                (progress) => {
                    const percentComplete = (progress.loaded / progress.total) * 100;
                    console.log(`📊 Cargando ${avatarName}: ${percentComplete.toFixed(1)}%`);
                    if (onProgress) onProgress(percentComplete);
                },
                (error) => {
                    console.error(`❌ Error cargando ${avatarName}:`, error);
                    if (this.errorCallbacks.has(avatarName)) {
                        this.errorCallbacks.get(avatarName)(error);
                    }
                    reject(error);
                }
            );
        });
    }

    /**
     * Cargar animaciones desde archivos externos
     * Solo extrae los AnimationClips, NO los modelos
     * @param {string} avatarName - Nombre del avatar
     * @param {Array<string>} animationNames - Lista de nombres de animaciones
     * @param {function} onProgress - Callback de progreso
     * @returns {Promise<Map>} Mapa de animaciones cargadas
     */
    async loadAnimations(avatarName, animationNames, onProgress = null) {
        const avatarData = this.avatars.get(avatarName);
        if (!avatarData) {
            throw new Error(`Avatar "${avatarName}" no está cargado. Llama primero a loadAvatar()`);
        }

        console.log(`🎬 Cargando ${animationNames.length} animaciones para ${avatarName}...`);
        const loader = new this.GLTFLoader();
        const loadedAnimations = new Map();
        let loaded = 0;

        const promises = animationNames.map((animName) => {
            return new Promise((resolve, reject) => {
                const animPath = this._buildAnimationPath(avatarData.config, animName, avatarName);
                
                if (!animPath) {
                    console.warn(`⚠️ No se pudo construir ruta para "${animName}"`);
                    resolve(null);
                    return;
                }
                
                loader.load(
                    animPath,
                    (gltf) => {
                        // Extraer SOLO las animaciones, ignorar mesh/materiales
                        if (gltf.animations && gltf.animations.length > 0) {
                            const clip = gltf.animations[0]; // Primer clip
                            clip.name = animName; // Renombrar para identificación
                            loadedAnimations.set(animName, clip);
                            avatarData.animations.set(animName, clip);
                            
                            loaded++;
                            const progress = (loaded / animationNames.length) * 100;
                            console.log(`✅ Animación "${animName}" cargada (${loaded}/${animationNames.length})`);
                            if (onProgress) onProgress(progress, animName);
                            
                            resolve(clip);
                        } else {
                            console.warn(`⚠️ Archivo "${animPath}" no contiene animaciones`);
                            resolve(null);
                        }
                    },
                    undefined,
                    (error) => {
                        console.error(`❌ Error cargando animación "${animName}":`, error);
                        resolve(null); // No rechazar, continuar con otras
                    }
                );
            });
        });

        await Promise.all(promises);
        console.log(`🎉 Total animaciones cargadas: ${loadedAnimations.size}/${animationNames.length}`);
        return loadedAnimations;
    }

    /**
     * Cargar todas las animaciones de una categoría
     * @param {string} avatarName - Nombre del avatar
     * @param {string} category - Categoría (saludos, tiempo, etc.)
     * @param {function} onProgress - Callback de progreso
     * @returns {Promise<Map>} Animaciones de la categoría
     */
    async loadCategory(avatarName, category, onProgress = null) {
        const avatarData = this.avatars.get(avatarName);
        if (!avatarData) {
            throw new Error(`Avatar "${avatarName}" no está cargado`);
        }

        const categoryPath = avatarData.config.animations[category];
        if (!categoryPath) {
            throw new Error(`Categoría "${category}" no existe para ${avatarName}`);
        }

        // En un entorno web, necesitarías una lista predefinida o endpoint para listar archivos
        // Por ahora, asumimos que tienes la lista de animaciones disponibles
        console.warn(`⚠️ loadCategory requiere implementación específica para listar archivos`);
        return new Map();
    }

    /**
     * Obtener avatar cargado
     * @param {string} avatarName - Nombre del avatar
     * @returns {Object|null} Datos del avatar
     */
    getAvatar(avatarName) {
        return this.avatars.get(avatarName) || null;
    }

    /**
     * Verificar si un avatar está cargado
     * @param {string} avatarName - Nombre del avatar
     * @returns {boolean}
     */
    isAvatarLoaded(avatarName) {
        return this.avatars.has(avatarName);
    }

    /**
     * Obtener lista de avatares disponibles
     * @returns {Array<string>}
     */
    getAvailableAvatars() {
        return Object.keys(AvatarLoader.AVATAR_PATHS);
    }

    /**
     * Obtener lista de animaciones cargadas para un avatar
     * @param {string} avatarName - Nombre del avatar
     * @returns {Array<string>} Lista de nombres de animaciones
     */
    getLoadedAnimations(avatarName) {
        const avatar = this.avatars.get(avatarName);
        return avatar ? Array.from(avatar.animations.keys()) : [];
    }

    /**
     * Obtener clip de animación específico
     * @param {string} avatarName - Nombre del avatar
     * @param {string} animationName - Nombre de la animación
     * @returns {THREE.AnimationClip|null}
     */
    getAnimationClip(avatarName, animationName) {
        const avatar = this.avatars.get(avatarName);
        return avatar ? avatar.animations.get(animationName) : null;
    }

    /**
     * Limpiar avatar de la memoria
     * @param {string} avatarName - Nombre del avatar
     */
    disposeAvatar(avatarName) {
        const avatar = this.avatars.get(avatarName);
        if (avatar) {
            // Limpiar geometrías y materiales
            avatar.model.traverse((child) => {
                if (child.geometry) child.geometry.dispose();
                if (child.material) {
                    if (Array.isArray(child.material)) {
                        child.material.forEach(mat => mat.dispose());
                    } else {
                        child.material.dispose();
                    }
                }
            });
            
            // Detener mixer
            if (avatar.mixer) {
                avatar.mixer.stopAllAction();
            }
            
            this.avatars.delete(avatarName);
            console.log(`🗑️ Avatar ${avatarName} eliminado de la memoria`);
        }
    }

    /**
     * Registrar callback cuando avatar se cargue
     * @param {string} avatarName - Nombre del avatar
     * @param {function} callback - Función a ejecutar
     */
    onAvatarLoaded(avatarName, callback) {
        this.loadingCallbacks.set(avatarName, callback);
    }

    /**
     * Registrar callback de error
     * @param {string} avatarName - Nombre del avatar
     * @param {function} callback - Función a ejecutar
     */
    onAvatarError(avatarName, callback) {
        this.errorCallbacks.set(avatarName, callback);
    }

    // ============= MÉTODOS INTERNOS =============

    /**
     * Extraer esqueleto del modelo
     * @private
     */
    _extractSkeleton(model) {
        let skeleton = null;
        model.traverse((child) => {
            if (child.isSkinnedMesh && child.skeleton) {
                skeleton = child.skeleton;
            }
        });
        return skeleton;
    }

    /**
     * Construir ruta de animación basada en nombre y avatar
     * Busca automáticamente en las categorías usando el mapeo
     * @private
     */
    _buildAnimationPath(config, animName, avatarName) {
        // Normalizar nombre de animación
        let fileName = animName.toLowerCase();
        
        // Detectar si es alfabeto
        if (fileName.startsWith('alfabeto_')) {
            const letter = fileName.replace('alfabeto_', '');
            const categoryPath = config.animations.alfabeto;
            if (categoryPath) {
                // Los archivos de alfabeto usan solo la letra: Luis_resultado_a.glb
                const fullPath = `${this.BASE_URL}${categoryPath}${avatarName}_resultado_${letter}.glb`;
                console.log(`🔤 Alfabeto "${letter}" -> ${fullPath}`);
                return fullPath;
            }
        }
        
        // Detectar si es número
        if (fileName.startsWith('numero_')) {
            const number = fileName.replace('numero_', '');
            const categoryPath = config.animations.numero || config.animations.numeros;
            if (categoryPath) {
                const fullPath = `${this.BASE_URL}${categoryPath}${avatarName}_resultado_${number}.glb`;
                console.log(`🔢 Número "${number}" -> ${fullPath}`);
                return fullPath;
            }
        }
        
        // Buscar categoría en el mapeo
        const category = AvatarLoader.ANIMATION_CATEGORIES[fileName];
        
        if (category && config.animations[category]) {
            // Los archivos usan ESPACIOS, no underscores
            // Convertir underscores a espacios para el nombre del archivo
            const fileNameWithSpaces = fileName.replace(/_/g, ' ');
            
            const categoryPath = config.animations[category];
            const fullPath = `${this.BASE_URL}${categoryPath}${avatarName}_resultado_${fileNameWithSpaces}.glb`;
            
            console.log(`🎯 Animación "${animName}" -> Categoría "${category}" -> ${fullPath}`);
            return fullPath;
        }
        
        // Si no se encuentra en el mapeo, intentar buscar en todas las categorías
        // (fallback para palabras no mapeadas)
        console.warn(`⚠️ Animación "${animName}" no encontrada en mapeo, buscando en todas las categorías...`);
        
        const fileNameWithSpaces = fileName.replace(/_/g, ' ');
        
        // Intentar primero en expresiones (categoría más grande)
        for (const categoryName of ['expresiones', 'saludos', 'verbos', 'cortesia']) {
            const categoryPath = config.animations[categoryName];
            if (categoryPath) {
                const fullPath = `${this.BASE_URL}${categoryPath}${avatarName}_resultado_${fileNameWithSpaces}.glb`;
                console.log(`🔍 Intentando en "${categoryName}": ${fullPath}`);
                return fullPath;
            }
        }
        
        // Si todo falla, retornar null
        console.error(`❌ No se pudo construir ruta para "${animName}"`);
        return null;
    }
}

// Exportar para uso en diferentes entornos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AvatarLoader; // Node.js/React Native
} else {
    window.AvatarLoader = AvatarLoader; // Browser
}
