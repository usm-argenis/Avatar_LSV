/**
 * Optimizaciones de rendimiento para la app VeneSeñas
 * Implementa lazy loading, caché, y mejoras de performance
 */

import { InteractionManager } from 'react-native';

// ============================================
// UTILIDADES DE OPTIMIZACIÓN
// ============================================

/**
 * Ejecuta una función después de que las animaciones terminen
 * Evita bloquear la UI durante operaciones pesadas
 */
export const executeAfterInteractions = (callback) => {
  return new Promise((resolve) => {
    InteractionManager.runAfterInteractions(() => {
      const result = callback();
      resolve(result);
    });
  });
};

/**
 * Debounce para evitar ejecuciones múltiples
 */
export const debounce = (func, wait) => {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
};

/**
 * Throttle para limitar frecuencia de ejecución
 */
export const throttle = (func, limit) => {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
};

// ============================================
// CACHÉ DE AVATARES Y ANIMACIONES
// ============================================

class ResourceCache {
  constructor(maxSize = 50) {
    this.cache = new Map();
    this.maxSize = maxSize;
    this.accessOrder = [];
  }

  set(key, value) {
    // Si ya existe, actualizar orden de acceso
    if (this.cache.has(key)) {
      this.accessOrder = this.accessOrder.filter(k => k !== key);
    }

    // Si el caché está lleno, eliminar el menos usado
    if (this.cache.size >= this.maxSize) {
      const oldestKey = this.accessOrder.shift();
      this.cache.delete(oldestKey);
    }

    this.cache.set(key, value);
    this.accessOrder.push(key);
  }

  get(key) {
    if (!this.cache.has(key)) {
      return null;
    }

    // Actualizar orden de acceso
    this.accessOrder = this.accessOrder.filter(k => k !== key);
    this.accessOrder.push(key);

    return this.cache.get(key);
  }

  has(key) {
    return this.cache.has(key);
  }

  clear() {
    this.cache.clear();
    this.accessOrder = [];
  }

  size() {
    return this.cache.size;
  }
}

export const avatarCache = new ResourceCache(10); // Máximo 10 avatares en caché
export const animationCache = new ResourceCache(100); // Máximo 100 animaciones

// ============================================
// LAZY LOADER DE ANIMACIONES
// ============================================

class LazyAnimationLoader {
  constructor() {
    this.loadingQueue = [];
    this.isProcessing = false;
    this.loadedAnimations = new Set();
    this.preloadedAnimations = new Set();
  }

  /**
   * Animaciones esenciales que se cargan primero
   */
  getEssentialAnimations() {
    return [
      'hola', 'adios', 'gracias', 'por_favor',
      'si', 'no', 'buenos_dias', 'buenas_tardes'
    ];
  }

  /**
   * Marca una animación como cargada
   */
  markAsLoaded(animationName) {
    this.loadedAnimations.add(animationName);
  }

  /**
   * Verifica si una animación está cargada
   */
  isLoaded(animationName) {
    return this.loadedAnimations.has(animationName);
  }

  /**
   * Precarga animaciones en segundo plano
   */
  async preloadAnimations(avatarName, animations, loader) {
    for (const anim of animations) {
      if (!this.isLoaded(anim) && !this.preloadedAnimations.has(anim)) {
        this.preloadedAnimations.add(anim);
        try {
          await loader.loadSingleAnimation(avatarName, anim);
          this.markAsLoaded(anim);
        } catch (error) {
          console.warn(`⚠️ No se pudo precargar ${anim}:`, error.message);
        }
      }
    }
  }

  /**
   * Limpia el caché de animaciones cargadas
   */
  clear() {
    this.loadedAnimations.clear();
    this.preloadedAnimations.clear();
  }
}

export const lazyAnimationLoader = new LazyAnimationLoader();

// ============================================
// OPTIMIZADOR DE RENDERIZADO 3D
// ============================================

export class RenderOptimizer {
  constructor() {
    this.targetFPS = 60;
    this.frameTime = 1000 / this.targetFPS;
    this.lastFrameTime = 0;
    this.skipFrames = 0;
    this.performanceMode = 'auto'; // 'auto', 'quality', 'performance'
  }

  /**
   * Determina si se debe renderizar este frame
   */
  shouldRender(currentTime) {
    const deltaTime = currentTime - this.lastFrameTime;

    if (deltaTime < this.frameTime) {
      return false;
    }

    this.lastFrameTime = currentTime;
    return true;
  }

  /**
   * Ajusta calidad según rendimiento
   */
  adjustQuality(fps) {
    if (this.performanceMode !== 'auto') return;

    if (fps < 30) {
      // Rendimiento bajo: reducir calidad
      return {
        shadows: false,
        antialias: false,
        pixelRatio: 1
      };
    } else if (fps < 50) {
      // Rendimiento medio
      return {
        shadows: false,
        antialias: true,
        pixelRatio: 1.5
      };
    } else {
      // Buen rendimiento
      return {
        shadows: true,
        antialias: true,
        pixelRatio: 2
      };
    }
  }

  setPerformanceMode(mode) {
    this.performanceMode = mode;
  }
}

// ============================================
// OPTIMIZADOR DE MEMORIA
// ============================================

export class MemoryOptimizer {
  constructor() {
    this.disposeQueue = [];
  }

  /**
   * Marca recursos para disposición
   */
  scheduleDisposal(resource) {
    this.disposeQueue.push(resource);
  }

  /**
   * Limpia recursos marcados
   */
  flush() {
    while (this.disposeQueue.length > 0) {
      const resource = this.disposeQueue.pop();
      
      try {
        if (resource.geometry) {
          resource.geometry.dispose();
        }
        if (resource.material) {
          if (Array.isArray(resource.material)) {
            resource.material.forEach(mat => mat.dispose());
          } else {
            resource.material.dispose();
          }
        }
        if (resource.texture) {
          resource.texture.dispose();
        }
        if (resource.dispose) {
          resource.dispose();
        }
      } catch (error) {
        console.warn('⚠️ Error disposing resource:', error);
      }
    }
  }

  /**
   * Limpia un avatar completo de la memoria
   */
  disposeAvatar(avatarData) {
    if (!avatarData) return;

    try {
      // Limpiar animaciones
      if (avatarData.animations) {
        avatarData.animations = [];
      }

      // Limpiar mixer
      if (avatarData.mixer) {
        avatarData.mixer.stopAllAction();
        avatarData.mixer.uncacheRoot(avatarData.mixer.getRoot());
      }

      // Limpiar modelo
      if (avatarData.model) {
        avatarData.model.traverse((child) => {
          if (child.isMesh) {
            this.scheduleDisposal(child);
          }
        });
      }

      this.flush();
    } catch (error) {
      console.warn('⚠️ Error disposing avatar:', error);
    }
  }
}

export const memoryOptimizer = new MemoryOptimizer();

// ============================================
// BATCH LOADER DE ANIMACIONES
// ============================================

export class BatchAnimationLoader {
  constructor(batchSize = 5) {
    this.batchSize = batchSize;
    this.queue = [];
    this.isLoading = false;
  }

  /**
   * Agrega animaciones a la cola de carga
   */
  enqueue(animations) {
    this.queue.push(...animations.filter(anim => 
      !lazyAnimationLoader.isLoaded(anim)
    ));
  }

  /**
   * Procesa la cola en lotes
   */
  async process(avatarName, loader, onProgress) {
    if (this.isLoading || this.queue.length === 0) return;

    this.isLoading = true;

    while (this.queue.length > 0) {
      const batch = this.queue.splice(0, this.batchSize);
      
      await Promise.all(
        batch.map(async (anim) => {
          try {
            await loader.loadSingleAnimation(avatarName, anim);
            lazyAnimationLoader.markAsLoaded(anim);
            if (onProgress) {
              onProgress(anim);
            }
          } catch (error) {
            console.warn(`⚠️ Error cargando ${anim}:`, error.message);
          }
        })
      );

      // Pequeña pausa entre lotes para no bloquear UI
      await new Promise(resolve => setTimeout(resolve, 50));
    }

    this.isLoading = false;
  }

  clear() {
    this.queue = [];
  }
}

export const batchAnimationLoader = new BatchAnimationLoader();

// ============================================
// HELPER FUNCTIONS
// ============================================

/**
 * Optimiza un texto para traducción (elimina caracteres innecesarios)
 */
export const optimizeTextForTranslation = (text) => {
  return text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '') // Eliminar acentos
    .replace(/[^\w\s]/gi, ' ') // Eliminar puntuación
    .replace(/\s+/g, ' ') // Normalizar espacios
    .trim();
};

/**
 * Divide un texto largo en chunks manejables
 */
export const chunkText = (text, maxLength = 50) => {
  const words = text.split(' ');
  const chunks = [];
  let currentChunk = [];
  let currentLength = 0;

  for (const word of words) {
    if (currentLength + word.length > maxLength && currentChunk.length > 0) {
      chunks.push(currentChunk.join(' '));
      currentChunk = [word];
      currentLength = word.length;
    } else {
      currentChunk.push(word);
      currentLength += word.length + 1;
    }
  }

  if (currentChunk.length > 0) {
    chunks.push(currentChunk.join(' '));
  }

  return chunks;
};

export default {
  executeAfterInteractions,
  debounce,
  throttle,
  avatarCache,
  animationCache,
  lazyAnimationLoader,
  RenderOptimizer,
  memoryOptimizer,
  BatchAnimationLoader,
  batchAnimationLoader,
  optimizeTextForTranslation,
  chunkText
};
