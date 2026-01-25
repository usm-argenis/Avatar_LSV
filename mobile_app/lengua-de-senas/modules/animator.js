/**
 * SignAnimator - Sistema de reproducción de animaciones de señas
 * Compatible con Three.js y React Native
 * 
 * Características:
 * - Reproducción secuencial de animaciones
 * - Transiciones suaves (crossfade)
 * - Control de velocidad
 * - Sistema de colas
 * - Eventos de reproducción
 */

class SignAnimator {
    constructor(avatar, THREE) {
        this.THREE = THREE;
        this.avatar = avatar; // Datos del avatar desde AvatarLoader
        this.mixer = avatar.mixer;
        this.currentAction = null;
        this.queue = []; // Cola de animaciones pendientes
        this.isPlaying = false;
        this.isPaused = false;
        this.playbackSpeed = 1.0;
        this.defaultTransitionDuration = 0.3; // Segundos
        
        // Callbacks
        this.callbacks = {
            onAnimationStart: null,
            onAnimationEnd: null,
            onQueueComplete: null,
            onAnimationChange: null,
            onError: null
        };
    }

    /**
     * Reproducir una animación específica
     * @param {string} animationName - Nombre de la animación
     * @param {Object} options - Opciones de reproducción
     * @returns {boolean} true si se reprodujo correctamente
     */
    playAnimation(animationName, options = {}) {
        const {
            loop = false,
            transitionDuration = this.defaultTransitionDuration,
            speed = this.playbackSpeed,
            onComplete = null
        } = options;

        // Buscar el clip de animación
        const clip = this.avatar.animations.get(animationName);
        if (!clip) {
            console.error(`❌ Animación "${animationName}" no encontrada`);
            if (this.callbacks.onError) {
                this.callbacks.onError(`Animación "${animationName}" no existe`);
            }
            return false;
        }

        console.log(`▶️ Reproduciendo: ${animationName}`);

        // Crear acción desde el clip
        const action = this.mixer.clipAction(clip);
        action.setLoop(loop ? this.THREE.LoopRepeat : this.THREE.LoopOnce, loop ? Infinity : 1);
        action.clampWhenFinished = true; // Mantener último frame
        action.timeScale = speed;

        // Transición suave desde la animación anterior
        if (this.currentAction && this.currentAction !== action) {
            this.currentAction.fadeOut(transitionDuration);
        }

        // Iniciar nueva animación
        action.reset();
        action.fadeIn(transitionDuration);
        action.play();

        // Guardar como acción actual
        this.currentAction = action;
        this.isPlaying = true;
        this.isPaused = false;

        // Callback de inicio
        if (this.callbacks.onAnimationStart) {
            this.callbacks.onAnimationStart(animationName, clip.duration);
        }

        // Listener de finalización (solo para animaciones no-loop)
        if (!loop) {
            const onFinished = (e) => {
                if (e.action === action) {
                    console.log(`✅ Animación "${animationName}" completada`);
                    
                    if (this.callbacks.onAnimationEnd) {
                        this.callbacks.onAnimationEnd(animationName);
                    }
                    
                    if (onComplete) {
                        onComplete();
                    }
                    
                    // Procesar siguiente en cola
                    this.processQueue();
                    
                    this.mixer.removeEventListener('finished', onFinished);
                }
            };
            this.mixer.addEventListener('finished', onFinished);
        }

        return true;
    }

    /**
     * Reproducir secuencia de animaciones
     * @param {Array<string>} animationNames - Lista de nombres de animaciones
     * @param {Object} options - Opciones globales
     */
    playSequence(animationNames, options = {}) {
        const {
            pauseBetween = 0.5, // Pausa entre animaciones (segundos)
            speed = this.playbackSpeed,
            onComplete = null
        } = options;

        console.log(`🎬 Iniciando secuencia: ${animationNames.join(' → ')}`);

        // Agregar animaciones a la cola
        this.queue = animationNames.map(name => ({
            name,
            speed,
            pauseBetween
        }));

        // Callback cuando termine toda la secuencia
        if (onComplete) {
            const originalCallback = this.callbacks.onQueueComplete;
            this.callbacks.onQueueComplete = () => {
                if (originalCallback) originalCallback();
                onComplete();
                this.callbacks.onQueueComplete = originalCallback;
            };
        }

        // Iniciar primera animación
        this.processQueue();
    }

    /**
     * Procesar siguiente animación en la cola
     * @private
     */
    processQueue() {
        if (this.queue.length === 0) {
            console.log(`🏁 Secuencia completada`);
            this.isPlaying = false;
            
            if (this.callbacks.onQueueComplete) {
                this.callbacks.onQueueComplete();
            }
            return;
        }

        // Obtener siguiente animación
        const next = this.queue.shift();
        
        // Pausa opcional antes de siguiente animación
        if (next.pauseBetween > 0) {
            setTimeout(() => {
                this.playAnimation(next.name, { speed: next.speed });
            }, next.pauseBetween * 1000);
        } else {
            this.playAnimation(next.name, { speed: next.speed });
        }
    }

    /**
     * Pausar animación actual
     */
    pause() {
        if (this.currentAction && this.isPlaying && !this.isPaused) {
            this.currentAction.paused = true;
            this.isPaused = true;
            console.log(`⏸️ Animación pausada`);
        }
    }

    /**
     * Reanudar animación pausada
     */
    resume() {
        if (this.currentAction && this.isPaused) {
            this.currentAction.paused = false;
            this.isPaused = false;
            console.log(`▶️ Animación reanudada`);
        }
    }

    /**
     * Detener animación actual y limpiar cola
     */
    stop() {
        if (this.currentAction) {
            this.currentAction.stop();
            this.currentAction = null;
        }
        
        this.queue = [];
        this.isPlaying = false;
        this.isPaused = false;
        
        console.log(`⏹️ Reproducción detenida`);
    }

    /**
     * Cambiar velocidad de reproducción
     * @param {number} speed - Velocidad (0.5 = mitad, 2.0 = doble)
     */
    setSpeed(speed) {
        this.playbackSpeed = Math.max(0.1, Math.min(5.0, speed)); // Límites razonables
        
        if (this.currentAction) {
            this.currentAction.timeScale = this.playbackSpeed;
        }
        
        console.log(`⚡ Velocidad ajustada: ${this.playbackSpeed.toFixed(2)}x`);
    }

    /**
     * Saltar a tiempo específico en animación actual
     * @param {number} time - Tiempo en segundos
     */
    seekTo(time) {
        if (this.currentAction) {
            this.currentAction.time = Math.max(0, Math.min(time, this.currentAction.getClip().duration));
        }
    }

    /**
     * Obtener tiempo actual de reproducción
     * @returns {number} Tiempo en segundos
     */
    getCurrentTime() {
        return this.currentAction ? this.currentAction.time : 0;
    }

    /**
     * Obtener duración de animación actual
     * @returns {number} Duración en segundos
     */
    getCurrentDuration() {
        return this.currentAction ? this.currentAction.getClip().duration : 0;
    }

    /**
     * Obtener nombre de animación actual
     * @returns {string|null}
     */
    getCurrentAnimationName() {
        return this.currentAction ? this.currentAction.getClip().name : null;
    }

    /**
     * Verificar si hay reproducción activa
     * @returns {boolean}
     */
    isCurrentlyPlaying() {
        return this.isPlaying && !this.isPaused;
    }

    /**
     * Obtener cantidad de animaciones en cola
     * @returns {number}
     */
    getQueueLength() {
        return this.queue.length;
    }

    /**
     * Limpiar cola sin detener animación actual
     */
    clearQueue() {
        this.queue = [];
        console.log(`🗑️ Cola limpiada`);
    }

    /**
     * Actualizar mixer (debe llamarse en cada frame)
     * @param {number} deltaTime - Tiempo transcurrido desde último frame
     */
    update(deltaTime) {
        if (this.mixer) {
            this.mixer.update(deltaTime);
        }
    }

    /**
     * Registrar callback de evento
     * @param {string} eventName - Nombre del evento
     * @param {function} callback - Función a ejecutar
     */
    on(eventName, callback) {
        if (this.callbacks.hasOwnProperty(`on${eventName}`)) {
            this.callbacks[`on${eventName}`] = callback;
        } else {
            console.warn(`⚠️ Evento "${eventName}" no reconocido`);
        }
    }

    /**
     * Remover callback de evento
     * @param {string} eventName - Nombre del evento
     */
    off(eventName) {
        if (this.callbacks.hasOwnProperty(`on${eventName}`)) {
            this.callbacks[`on${eventName}`] = null;
        }
    }

    /**
     * Obtener información de estado
     * @returns {Object} Estado actual del animator
     */
    getState() {
        return {
            isPlaying: this.isPlaying,
            isPaused: this.isPaused,
            currentAnimation: this.getCurrentAnimationName(),
            currentTime: this.getCurrentTime(),
            duration: this.getCurrentDuration(),
            queueLength: this.getQueueLength(),
            speed: this.playbackSpeed
        };
    }

    /**
     * Reproducir animación idle (posición neutral)
     * @param {boolean} loop - Si debe repetirse
     */
    playIdle(loop = true) {
        // Buscar animación "idle" o "neutral"
        const idleNames = ['idle', 'neutral', 'reposo', 'espera'];
        
        for (const name of idleNames) {
            if (this.avatar.animations.has(name)) {
                this.playAnimation(name, { loop });
                return true;
            }
        }
        
        console.warn(`⚠️ No se encontró animación idle`);
        return false;
    }

    /**
     * Transición suave a idle después de secuencia
     * @param {number} delay - Retraso en segundos
     */
    returnToIdle(delay = 1.0) {
        setTimeout(() => {
            if (!this.isPlaying) {
                this.playIdle(true);
            }
        }, delay * 1000);
    }
}

// Exportar para uso en diferentes entornos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SignAnimator; // Node.js/React Native
} else {
    window.SignAnimator = SignAnimator; // Browser
}
