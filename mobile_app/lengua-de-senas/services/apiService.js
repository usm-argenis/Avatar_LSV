/**
 * Servicio de API para conexión con backend IA LSV
 */

const API_BASE_URL = 'http://192.168.10.93:5000'; // Backend Flask en puerto 5000

class LSVAPIService {
  /**
   * Optimiza texto usando la IA del backend
   * @param {string} texto - Texto a optimizar
   * @returns {Promise<Object>} Resultado de la optimización
   */
  async optimizarTexto(texto) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/optimizar`, {
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
        data: {
          textoOriginal: data.texto_original,
          textoCorregido: data.texto_corregido,
          textoLSV: data.texto_lsv,
          palabrasLSV: data.palabras_lsv,
          palabrasDisponibles: data.palabras_disponibles || [],
          palabrasFaltantes: data.palabras_faltantes || [],
          porcentajeCobertura: data.porcentaje_cobertura || 0,
          sugerencias: data.sugerencias || {}
        }
      };
    } catch (error) {
      console.error('Error al optimizar texto:', error);
      return {
        success: false,
        error: error.message
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
      const response = await fetch(`${API_BASE_URL}/`, {
        method: 'GET',
      });

      return response.ok;
    } catch (error) {
      console.error('No hay conexión con el backend:', error);
      return false;
    }
  }
}

export default new LSVAPIService();
