import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

// ============================================
// CONFIGURACIÓN DE LA API
// ============================================
// ⚠️ IMPORTANTE: Cambia según tu entorno

// Android Emulator: usa 10.0.2.2 (es el localhost del emulador)
const API_URL = 'http://10.0.2.2:3000';

// iOS Emulator: usa localhost
// const API_URL = 'http://localhost:3000';

// Dispositivo Físico: usa tu IP local
// const API_URL = 'http://192.168.1.100:3000';

// ============================================
// REGISTRO DE USUARIO
// ============================================
export const register = async (full_name, email, password) => {
  try {
    const response = await axios.post(`${API_URL}/api/register`, {
      full_name,
      email,
      password
    });

    if (response.data.success) {
      // Guardar ID del usuario
      await AsyncStorage.setItem('userId', response.data.data.id.toString());
      await AsyncStorage.setItem('userEmail', response.data.data.email);
      await AsyncStorage.setItem('userName', response.data.data.full_name);
    }

    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return {
      success: false,
      mensaje: 'Error de conexión. Verifica que el servidor esté corriendo.'
    };
  }
};

// ============================================
// LOGIN DE USUARIO
// ============================================
export const login = async (email, password) => {
  try {
    const response = await axios.post(`${API_URL}/api/login`, {
      email,
      password
    });

    if (response.data.success) {
      // Guardar datos del usuario
      const { user, progress, settings } = response.data.data;
      
      await AsyncStorage.setItem('userId', user.id.toString());
      await AsyncStorage.setItem('userEmail', user.email);
      await AsyncStorage.setItem('userName', user.full_name);
      
      // Guardar progreso
      if (progress) {
        await AsyncStorage.setItem('userStars', progress.stars.toString());
        await AsyncStorage.setItem('userLevel', progress.level.toString());
      }
    }

    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return {
      success: false,
      mensaje: 'Error de conexión. Verifica que el servidor esté corriendo.'
    };
  }
};

// ============================================
// CERRAR SESIÓN
// ============================================
export const logout = async () => {
  try {
    await AsyncStorage.multiRemove([
      'userId',
      'userEmail',
      'userName',
      'userStars',
      'userLevel'
    ]);
    return { success: true };
  } catch (error) {
    return { success: false, mensaje: error.message };
  }
};

// ============================================
// OBTENER PROGRESO DEL USUARIO
// ============================================
export const getUserProgress = async (userId) => {
  try {
    const response = await axios.get(`${API_URL}/api/user/${userId}/progress`);
    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return { success: false, mensaje: 'Error al obtener progreso' };
  }
};

// ============================================
// GUARDAR ESTRELLAS (Cuando completan palabras)
// ============================================
export const saveStarsToAPI = async (userId, stars, wordsCompleted = 0) => {
  try {
    const response = await axios.post(`${API_URL}/api/user/${userId}/add-stars`, {
      stars,
      words_completed: wordsCompleted
    });

    if (response.data.success) {
      // Actualizar AsyncStorage local
      const currentStars = await AsyncStorage.getItem('userStars');
      const newStars = parseInt(currentStars || '0') + stars;
      await AsyncStorage.setItem('userStars', newStars.toString());
    }

    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return { success: false, mensaje: 'Error al guardar estrellas' };
  }
};

// ============================================
// AGREGAR PALABRA AL HISTORIAL
// ============================================
export const addWordToHistory = async (userId, word, completed, mistakes = 0) => {
  try {
    const response = await axios.post(`${API_URL}/api/user/${userId}/word-history`, {
      word,
      completed,
      mistakes
    });
    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return { success: false, mensaje: 'Error al guardar historial' };
  }
};

// ============================================
// OBTENER HISTORIAL DE PALABRAS
// ============================================
export const getWordHistory = async (userId, limit = 50) => {
  try {
    const response = await axios.get(`${API_URL}/api/user/${userId}/word-history?limit=${limit}`);
    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return { success: false, mensaje: 'Error al obtener historial' };
  }
};

// ============================================
// OBTENER CONFIGURACIONES
// ============================================
export const getUserSettings = async (userId) => {
  try {
    const response = await axios.get(`${API_URL}/api/user/${userId}/settings`);
    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return { success: false, mensaje: 'Error al obtener configuraciones' };
  }
};

// ============================================
// ACTUALIZAR CONFIGURACIONES
// ============================================
export const updateUserSettings = async (userId, settings) => {
  try {
    const response = await axios.put(`${API_URL}/api/user/${userId}/settings`, settings);
    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return { success: false, mensaje: 'Error al actualizar configuraciones' };
  }
};

// ============================================
// VERIFICAR SI EL USUARIO ESTÁ LOGUEADO
// ============================================
export const isUserLoggedIn = async () => {
  try {
    const userId = await AsyncStorage.getItem('userId');
    return userId !== null;
  } catch (error) {
    return false;
  }
};

// ============================================
// OBTENER DATOS DEL USUARIO ACTUAL
// ============================================
export const getCurrentUser = async () => {
  try {
    const userId = await AsyncStorage.getItem('userId');
    const userEmail = await AsyncStorage.getItem('userEmail');
    const userName = await AsyncStorage.getItem('userName');
    const userStars = await AsyncStorage.getItem('userStars');
    const userLevel = await AsyncStorage.getItem('userLevel');

    if (userId) {
      return {
        id: parseInt(userId),
        email: userEmail,
        name: userName,
        stars: parseInt(userStars || '0'),
        level: parseInt(userLevel || '1')
      };
    }
    return null;
  } catch (error) {
    return null;
  }
};
