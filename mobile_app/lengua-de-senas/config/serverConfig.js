/**
 * Configuración del servidor para la aplicación móvil
 * 
 * IMPORTANTE: Actualiza estas configuraciones según tu red
 */

// URL del servidor HTTP que sirve los archivos GLB (puerto 8000)
// Este servidor debe estar corriendo con: python -m http.server 8000
export const GLB_SERVER_URL = 'http://192.168.10.93:8000/';

// URL del API backend (Node.js/Express - puerto 3000)
export const API_SERVER_URL = 'http://192.168.10.93:3000';

/**
 * Cómo encontrar tu IP local:
 * 
 * Windows:
 * 1. Abre CMD o PowerShell
 * 2. Ejecuta: ipconfig
 * 3. Busca "IPv4 Address" en tu adaptador de red activo
 * 
 * Mac/Linux:
 * 1. Abre Terminal
 * 2. Ejecuta: ifconfig
 * 3. Busca "inet" en tu conexión activa (wifi/ethernet)
 * 
 * NOTAS:
 * - Tu teléfono y PC deben estar en la misma red WiFi
 * - Si usas Android Emulator, usa: 10.0.2.2 en lugar de tu IP local
 * - Si usas iOS Simulator, puedes usar: localhost
 */

export default {
  GLB_SERVER_URL,
  API_SERVER_URL
};
