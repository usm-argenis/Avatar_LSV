/**
 * Sistema de Gestos Faciales para Animaciones LSV
 * Maneja la aplicación de expresiones faciales usando morph targets (shape keys)
 * en tiempo real durante la reproducción de animaciones.
 */

class FacialExpressionSystem {
    constructor() {
        this.config = null;
        this.currentExpression = 'neutral';
        this.targetExpression = 'neutral';
        this.transitionProgress = 1.0;
        this.transitionDuration = 0.5;
        this.meshesWithMorphTargets = [];
        this.morphTargetIndices = {};
        this.isTransitioning = false;
        this.isEnabled = true; // Control para activar/desactivar el sistema
    }

    /**
     * Carga la configuración de expresiones desde JSON
     */
    async loadConfig(configPath = 'facial_expressions_config.json') {
        try {
            const response = await fetch(configPath);
            this.config = await response.json();
            console.log('✅ Configuración de expresiones faciales cargada');
            return true;
        } catch (error) {
            console.error('❌ Error cargando configuración de expresiones:', error);
            return false;
        }
    }

    /**
     * Inicializa el sistema con un modelo 3D cargado
     * @param {THREE.Object3D} model - Modelo 3D con meshes que contienen morph targets
     */
    initializeWithModel(model) {
        this.meshesWithMorphTargets = [];
        this.morphTargetIndices = {};

        // Buscar todos los meshes con morph targets
        model.traverse((child) => {
            if (child.isMesh && child.morphTargetInfluences && child.morphTargetInfluences.length > 0) {
                this.meshesWithMorphTargets.push(child);
                
                // Mapear nombres de morph targets a índices
                if (child.morphTargetDictionary) {
                    console.log(`📦 Mesh encontrado: ${child.name} con ${child.morphTargetInfluences.length} morph targets`);
                    
                    // Solo necesitamos mapear una vez (todos los meshes tienen los mismos targets)
                    if (Object.keys(this.morphTargetIndices).length === 0) {
                        this.morphTargetIndices = { ...child.morphTargetDictionary };
                        console.log('📋 Morph targets disponibles:', Object.keys(this.morphTargetIndices));
                    }
                }
            }
        });

        console.log(`✅ Inicializado con ${this.meshesWithMorphTargets.length} meshes`);
        
        // Resetear a expresión neutral
        this.setExpression('neutral', 0);
    }

    /**
     * Establece una expresión facial
     * @param {string} expressionName - Nombre de la expresión ('angry', 'happy', etc.)
     * @param {number} transitionDuration - Duración de la transición en segundos (0 = inmediato)
     */
    setExpression(expressionName, transitionDuration = null) {
        if (!this.config) {
            console.warn('⚠️ Configuración no cargada');
            return;
        }

        if (!this.config.expressions[expressionName]) {
            console.warn(`⚠️ Expresión no encontrada: ${expressionName}`);
            console.log('   Expresiones disponibles:', Object.keys(this.config.expressions));
            return;
        }

        this.targetExpression = expressionName;
        this.transitionDuration = transitionDuration !== null ? 
            transitionDuration : this.config.transitionSettings.duration;
        this.transitionProgress = 0;
        this.isTransitioning = this.transitionDuration > 0;

        console.log(`😊 Transición a: ${expressionName} (${this.transitionDuration}s)`);

        // Si no hay transición, aplicar inmediatamente
        if (!this.isTransitioning) {
            this.applyExpression(expressionName, 1.0);
            this.currentExpression = expressionName;
        }
    }

    /**
     * Obtiene la expresión apropiada para una palabra
     * @param {string} word - Palabra a evaluar
     * @returns {string} - Nombre de la expresión
     */
    getExpressionForWord(word) {
        if (!this.config) return 'neutral';

        const wordLower = word.toLowerCase().trim();
        
        // Buscar coincidencia exacta
        if (this.config.wordExpressionMapping[wordLower]) {
            return this.config.wordExpressionMapping[wordLower];
        }

        // Buscar coincidencia parcial
        for (const [key, expression] of Object.entries(this.config.wordExpressionMapping)) {
            if (wordLower.includes(key) || key.includes(wordLower)) {
                return expression;
            }
        }

        return 'neutral';
    }

    /**
     * Aplica una expresión con un factor de intensidad
     * @param {string} expressionName - Nombre de la expresión
     * @param {number} intensity - Factor de intensidad (0.0 a 1.0)
     */
    applyExpression(expressionName, intensity = 1.0) {
        if (!this.config) {
            console.warn('⚠️ Config no cargado');
            return;
        }
        
        if (this.meshesWithMorphTargets.length === 0) {
            console.warn('⚠️ No hay meshes con morph targets');
            return;
        }

        const expression = this.config.expressions[expressionName];
        if (!expression) {
            console.warn(`⚠️ Expresión no encontrada: ${expressionName}`);
            return;
        }

        console.log(`🎭 Aplicando expresión: ${expressionName} (intensidad: ${intensity})`);
        let appliedCount = 0;

        // Aplicar valores a todos los meshes
        this.meshesWithMorphTargets.forEach(mesh => {
            // Primero resetear todos los morph targets a 0
            for (let i = 0; i < mesh.morphTargetInfluences.length; i++) {
                mesh.morphTargetInfluences[i] = 0;
            }

            // Luego aplicar los valores de la expresión
            for (const [targetName, targetValue] of Object.entries(expression.morphTargets)) {
                const index = this.morphTargetIndices[targetName];
                if (index !== undefined) {
                    mesh.morphTargetInfluences[index] = targetValue * intensity;
                    appliedCount++;
                    console.log(`   ✓ ${targetName}[${index}] = ${(targetValue * intensity).toFixed(2)}`);
                } else {
                    console.warn(`   ✗ Shape key no encontrado: ${targetName}`);
                }
            }
        });
        
        console.log(`✅ Aplicados ${appliedCount} shape keys en ${this.meshesWithMorphTargets.length} meshes`);
    }

    /**
     * Mezcla entre dos expresiones
     * @param {string} expr1 - Primera expresión
     * @param {string} expr2 - Segunda expresión
     * @param {number} blend - Factor de mezcla (0.0 = expr1, 1.0 = expr2)
     */
    blendExpressions(expr1, expr2, blend) {
        if (!this.config || this.meshesWithMorphTargets.length === 0) return;

        const expression1 = this.config.expressions[expr1];
        const expression2 = this.config.expressions[expr2];
        
        if (!expression1 || !expression2) return;

        // Obtener todos los morph targets usados
        const allTargets = new Set([
            ...Object.keys(expression1.morphTargets),
            ...Object.keys(expression2.morphTargets)
        ]);

        this.meshesWithMorphTargets.forEach(mesh => {
            // Resetear todos
            for (let i = 0; i < mesh.morphTargetInfluences.length; i++) {
                mesh.morphTargetInfluences[i] = 0;
            }

            // Mezclar valores
            allTargets.forEach(targetName => {
                const index = this.morphTargetIndices[targetName];
                if (index !== undefined) {
                    const value1 = expression1.morphTargets[targetName] || 0;
                    const value2 = expression2.morphTargets[targetName] || 0;
                    mesh.morphTargetInfluences[index] = value1 * (1 - blend) + value2 * blend;
                }
            });
        });
    }

    /**
     * Actualiza el sistema (llamar en el loop de animación)
     * @param {number} deltaTime - Tiempo transcurrido en segundos
     */
    update(deltaTime) {
        if (!this.isEnabled || !this.isTransitioning) return;

        this.transitionProgress += deltaTime / this.transitionDuration;

        if (this.transitionProgress >= 1.0) {
            // Transición completa
            this.transitionProgress = 1.0;
            this.isTransitioning = false;
            this.applyExpression(this.targetExpression, 1.0);
            this.currentExpression = this.targetExpression;
        } else {
            // Aplicar easing
            const easedProgress = this.easeInOutQuad(this.transitionProgress);
            this.blendExpressions(this.currentExpression, this.targetExpression, easedProgress);
        }
    }

    /**
     * Desactiva el sistema (para usar animaciones manuales JSON)
     */
    disable() {
        this.isEnabled = false;
    }

    /**
     * Reactiva el sistema
     */
    enable() {
        this.isEnabled = true;
    }

    /**
     * Función de easing suave
     */
    easeInOutQuad(t) {
        return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
    }

    /**
     * Resetea a expresión neutral
     */
    reset() {
        this.setExpression('neutral', 0);
    }

    /**
     * Obtiene información de debug
     */
    getDebugInfo() {
        return {
            meshCount: this.meshesWithMorphTargets.length,
            currentExpression: this.currentExpression,
            targetExpression: this.targetExpression,
            isTransitioning: this.isTransitioning,
            transitionProgress: this.transitionProgress,
            availableMorphTargets: Object.keys(this.morphTargetIndices).length
        };
    }
}

// Exportar para uso en otros scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = FacialExpressionSystem;
}
