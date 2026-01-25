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
    constructor(THREE, GLTFLoader) {
        this.THREE = THREE;
        this.GLTFLoader = GLTFLoader;
        this.avatars = new Map(); // { name: { model, animations, mixer, skeleton } }
        this.loadingCallbacks = new Map();
        this.errorCallbacks = new Map();
    }

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
                preguntas: 'output/glb/Nancy/preguntas/'
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
                preguntas: 'output/glb/Duvall/preguntas/'
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
                preguntas: 'output/glb/Luis/preguntas/'
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
                preguntas: 'output/glb/Carlos/preguntas/'
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
                preguntas: 'output/glb/Carla/preguntas/'
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
            loader.load(
                config.base,
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
     * Busca automáticamente en las categorías
     * @private
     */
    _buildAnimationPath(config, animName, avatarName) {
        // Normalizar nombre (mantener espacios para la mayoría, underscores para Remy)
        let fileName = animName.toLowerCase();
        
        // Remy usa underscores, los demás usan espacios
        if (avatarName === 'Remy') {
            fileName = fileName.replace(/\s+/g, '_');
        }
        
        // Buscar en cada categoría y construir el path con el nombre del avatar
        for (const [category, path] of Object.entries(config.animations)) {
            // Formato: {Avatar}_resultado_{palabra}.glb
            const possiblePath = `${path}${avatarName}_resultado_${fileName}.glb`;
            // En producción, deberías verificar si el archivo existe
            // Por ahora, retornamos la primera coincidencia
            return possiblePath;
        }
        
        // Si no se encuentra, intentar ruta directa
        return `${config.animations.saludos}${avatarName}_resultado_${fileName}.glb`;
    }
}

// Exportar para uso en diferentes entornos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = AvatarLoader; // Node.js/React Native
} else {
    window.AvatarLoader = AvatarLoader; // Browser
}
