/**
 * Servicio de API para conexión con backend IA LSV
 */

const API_BASE_URL = 'http://192.168.86.27:5000'; // Backend Flask en puerto 5000
const API_TIMEOUT = 3000; // Timeout de 3 segundos para evitar esperas largas

class LSVAPIService {
  constructor() {
    // Caché de optimizaciones para evitar llamadas repetidas
    this.cache = new Map();
    this.cacheExpiry = 5 * 60 * 1000; // 5 minutos de expiración
  }

  /**
   * Optimiza texto usando la IA del backend con timeout y caché
   * @param {string} texto - Texto a optimizar
   * @param {number} timeout - Timeout en ms (default: 3000)
   * @returns {Promise<Object>} Resultado de la optimización
   */
  async optimizarTexto(texto, timeout = API_TIMEOUT) {
    // Verificar caché
    const cacheKey = texto.toLowerCase().trim();
    const cached = this.cache.get(cacheKey);
    
    if (cached && Date.now() - cached.timestamp < this.cacheExpiry) {
      console.log('✅ Usando resultado en caché para:', texto);
      return {
        success: true,
        data: cached.data,
        fromCache: true
      };
    }

    try {
      // Crear promesa con timeout
      const fetchPromise = fetch(`${API_BASE_URL}/api/optimizar`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ texto }),
      });

      const timeoutPromise = new Promise((_, reject) => 
        setTimeout(() => reject(new Error('Timeout')), timeout)
      );

      const response = await Promise.race([fetchPromise, timeoutPromise]);

      if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
      }

      const data = await response.json();
      
      const result = {
        textoOriginal: data.texto_original,
        textoCorregido: data.texto_corregido,
        textoLSV: data.texto_lsv,
        palabrasLSV: data.palabras_lsv,
        palabrasDisponibles: data.palabras_disponibles || [],
        palabrasFaltantes: data.palabras_faltantes || [],
        porcentajeCobertura: data.porcentaje_cobertura || 0,
        sugerencias: data.sugerencias || {}
      };

      // Guardar en caché
      this.cache.set(cacheKey, {
        data: result,
        timestamp: Date.now()
      });

      console.log('✅ Optimización obtenida de API y guardada en caché');

      return {
        success: true,
        data: result
      };
    } catch (error) {
      console.error('⚠️ Error al optimizar texto:', error.message);
      
      // Limpiar caché si es un error de timeout recurrente
      if (error.message === 'Timeout') {
        console.log('⏱️ Timeout alcanzado, procesando sin API');
      }
      
      return {
        success: false,
        error: error.message,
        isTimeout: error.message === 'Timeout'
      };
    }
  }

  /**
   * Procesa texto con IA de entrenamiento
   * @param {string} texto - Texto a procesar
   * @returns {Promise<Object>} Resultado del procesamiento
   */
  async procesarConIA(texto) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/entrenar`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ texto }),
      });

      if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
      }

      const data = await response.json();
      return {
        success: true,
        data
      };
    } catch (error) {
      console.error('Error al procesar con IA:', error);
      return {
        success: false,
        error: error.message
      };
    }
  }

  /**
   * Verifica la conexión con el backend
   * @returns {Promise<boolean>} true si hay conexión
   */
  async verificarConexion() {
    try {
      const timeoutPromise = new Promise((_, reject) => 
        setTimeout(() => reject(new Error('Timeout')), 2000)
      );

      const fetchPromise = fetch(`${API_BASE_URL}/`, {
        method: 'GET',
      });

      const response = await Promise.race([fetchPromise, timeoutPromise]);
      return response.ok;
    } catch (error) {
      console.error('⚠️ No hay conexión con el backend:', error.message);
      return false;
    }
  }

  /**
   * Limpia la caché de optimizaciones
   */
  clearCache() {
    this.cache.clear();
    console.log('🧹 Caché limpiada');
  }

  /**
   * Obtiene estadísticas de la caché
   * @returns {Object} Estadísticas
   */
  getCacheStats() {
    return {
      entries: this.cache.size,
      keys: Array.from(this.cache.keys())
    };
  }
}

export default new LSVAPIService();
