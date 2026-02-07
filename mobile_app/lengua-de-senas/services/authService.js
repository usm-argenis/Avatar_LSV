import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

// ============================================
// CONFIGURACIÓN DE LA API
// ============================================
// ⚠️ IMPORTANTE: Cambia según tu entorno

// Para Expo Go en dispositivo físico (ambos en la misma WiFi):
const API_URL = 'http://192.168.86.27:3000';

// Android Emulator: usa 'http://10.0.2.2:3000'
// iOS Simulator: usa 'http://localhost:3000'

// iOS Emulator: usa localhost
// const API_URL = 'http://localhost:3000';

// Dispositivo Físico: usa tu IP local
// const API_URL = 'http://192.168.1.100:3000';

// ============================================
// REGISTRO DE USUARIO
// ============================================
export const register = async (full_name, email, password) => {
  try {
    console.log('[AuthService][register] Enviando datos de registro:', { full_name, email });
    const response = await axios.post(`${API_URL}/api/register`, {
      full_name,
      email,
      password
    });

    console.log('[AuthService][register] Respuesta del backend:', response.data);
    if (response.data.success) {
      // IMPORTANTE: Limpiar PRIMERO todo el AsyncStorage
      await AsyncStorage.multiRemove([
        'userId',
        'userEmail',
        'userName',
        'userStars',
        'userLevel',
        'totalScore',
        'wordsCompleted',
        'theme',
        'soundEnabled',
        'notificationsEnabled'
      ]);
      console.log('[AuthService][register] AsyncStorage limpiado');

      // Guardar datos del nuevo usuario
      const newUserId = response.data.data.id.toString();
      await AsyncStorage.setItem('userId', newUserId);
      await AsyncStorage.setItem('userEmail', response.data.data.email);
      await AsyncStorage.setItem('userName', response.data.data.full_name);
      console.log('[AuthService][register] Usuario guardado:', { id: newUserId, email: response.data.data.email });
      
      // Inicializar progreso en 0 para nuevo usuario
      await AsyncStorage.setItem('userStars', '0');
      await AsyncStorage.setItem('userLevel', '1');
      await AsyncStorage.setItem('totalScore', '0');
      await AsyncStorage.setItem('wordsCompleted', '0');
      console.log('[AuthService][register] Progreso inicializado en 0');
      
      // TAMBIÉN guardar con el formato específico por usuario para LearningScreen
      await AsyncStorage.setItem(`stars_${newUserId}`, '0');
      await AsyncStorage.setItem(`currentLevel_${newUserId}`, '1');
      console.log('[AuthService][register] Progreso guardado en formato específico:', { [`stars_${newUserId}`]: '0', [`currentLevel_${newUserId}`]: '1' });
    }

    return response.data;
  } catch (error) {
    console.log('[AuthService][register] Error:', error);
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
    console.log('[AuthService][login] Iniciando login para:', email);
    let response;
    try {
      response = await axios.post(`${API_URL}/api/login`, {
        email,
        password
      }, {
        timeout: 10000 // 10 segundos
      });
      console.log('[AuthService][login] Respuesta del backend:', response.data);
    } catch (axiosError) {
      console.log('[AuthService][login][AXIOS ERROR]', axiosError);
      if (axiosError.response) {
        console.log('[AuthService][login][AXIOS ERROR] response:', axiosError.response.data);
        return axiosError.response.data;
      }
      if (axiosError.request) {
        console.log('[AuthService][login][AXIOS ERROR] request:', axiosError.request);
      }
      if (axiosError.message) {
        console.log('[AuthService][login][AXIOS ERROR] message:', axiosError.message);
      }
      // Intentar con fetch si axios falla por red
      try {
        console.log('[AuthService][login][FETCH] Intentando login con fetch...');
        const fetchResponse = await fetch(`${API_URL}/api/login`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password })
        });
        const fetchData = await fetchResponse.json();
        console.log('[AuthService][login][FETCH] Respuesta:', fetchData);

        // Si el login fue exitoso con fetch, guardar en AsyncStorage igual que con axios
        if (fetchData && fetchData.success && fetchData.data) {
          await AsyncStorage.multiRemove([
            'userId',
            'userEmail',
            'userName',
            'userStars',
            'userLevel',
            'totalScore',
            'wordsCompleted',
            'theme',
            'soundEnabled',
            'notificationsEnabled'
          ]);
          console.log('[AuthService][login][FETCH] AsyncStorage limpiado');

          const { user, progress, settings } = fetchData.data;
          await AsyncStorage.setItem('userId', user.id.toString());
          await AsyncStorage.setItem('userEmail', user.email);
          await AsyncStorage.setItem('userName', user.full_name);
          console.log('[AuthService][login][FETCH] Usuario guardado:', { id: user.id, email: user.email });

          const userId = user.id.toString();
          if (progress) {
            console.log('[AuthService][login][FETCH] Progreso recibido del backend:', progress);
            await AsyncStorage.setItem('userStars', progress.stars.toString());
            await AsyncStorage.setItem('userLevel', progress.level.toString());
            await AsyncStorage.setItem('totalScore', progress.total_score.toString());
            await AsyncStorage.setItem('wordsCompleted', progress.words_completed.toString());
            await AsyncStorage.setItem(`stars_${userId}`, progress.stars.toString());
            await AsyncStorage.setItem(`currentLevel_${userId}`, progress.level.toString());
            console.log('[AuthService][login][FETCH] Progreso guardado:', {
              userStars: progress.stars,
              [`stars_${userId}`]: progress.stars,
              userLevel: progress.level,
              [`currentLevel_${userId}`]: progress.level
            });
          } else {
            console.log('[AuthService][login][FETCH] No hay progreso en el backend, inicializando con 0');
            await AsyncStorage.setItem('userStars', '0');
            await AsyncStorage.setItem('userLevel', '1');
            await AsyncStorage.setItem('totalScore', '0');
            await AsyncStorage.setItem('wordsCompleted', '0');
            await AsyncStorage.setItem(`stars_${userId}`, '0');
            await AsyncStorage.setItem(`currentLevel_${userId}`, '1');
            console.log('[AuthService][login][FETCH] Progreso inicial guardado con valores en 0');
          }

          if (settings) {
            await AsyncStorage.setItem('theme', settings.theme || 'light');
            await AsyncStorage.setItem('soundEnabled', settings.sound_enabled?.toString() || 'true');
            await AsyncStorage.setItem('notificationsEnabled', settings.notifications_enabled?.toString() || 'true');
            console.log('[AuthService][login][FETCH] Configuraciones guardadas:', settings);
          }
        }
        return fetchData;
      } catch (fetchError) {
        console.log('[AuthService][login][FETCH ERROR]', fetchError);
        return {
          success: false,
          mensaje: 'Error de red/fetch: ' + (fetchError.message || fetchError.toString())
        };
      }
    }
    if (response && response.data && response.data.success) {
      // IMPORTANTE: Limpiar PRIMERO todo el AsyncStorage del usuario anterior
      await AsyncStorage.multiRemove([
        'userId',
        'userEmail',
        'userName',
        'userStars',
        'userLevel',
        'totalScore',
        'wordsCompleted',
        'theme',
        'soundEnabled',
        'notificationsEnabled'
      ]);
      console.log('[AuthService][login] AsyncStorage limpiado');

      // Ahora guardar datos del nuevo usuario
      const { user, progress, settings } = response.data.data;
      await AsyncStorage.setItem('userId', user.id.toString());
      await AsyncStorage.setItem('userEmail', user.email);
      await AsyncStorage.setItem('userName', user.full_name);
      console.log('[AuthService][login] Usuario guardado:', { id: user.id, email: user.email });

      // Guardar progreso (esto asegura que cada usuario tenga sus propias estrellas)
      const userId = user.id.toString();
      if (progress) {
        console.log('[AuthService][login] Progreso recibido del backend:', progress);
        await AsyncStorage.setItem('userStars', progress.stars.toString());
        await AsyncStorage.setItem('userLevel', progress.level.toString());
        await AsyncStorage.setItem('totalScore', progress.total_score.toString());
        await AsyncStorage.setItem('wordsCompleted', progress.words_completed.toString());
        // TAMBIÉN guardar con el formato específico por usuario para LearningScreen
        await AsyncStorage.setItem(`stars_${userId}`, progress.stars.toString());
        await AsyncStorage.setItem(`currentLevel_${userId}`, progress.level.toString());
        console.log('[AuthService][login] Progreso guardado:', {
          userStars: progress.stars,
          [`stars_${userId}`]: progress.stars,
          userLevel: progress.level,
          [`currentLevel_${userId}`]: progress.level
        });
      } else {
        console.log('[AuthService][login] No hay progreso en el backend, inicializando con 0');
        // Si no hay progreso, inicializar con 0
        await AsyncStorage.setItem('userStars', '0');
        await AsyncStorage.setItem('userLevel', '1');
        await AsyncStorage.setItem('totalScore', '0');
        await AsyncStorage.setItem('wordsCompleted', '0');
        // TAMBIÉN guardar con el formato específico por usuario para LearningScreen
        await AsyncStorage.setItem(`stars_${userId}`, '0');
        await AsyncStorage.setItem(`currentLevel_${userId}`, '1');
        console.log('[AuthService][login] Progreso inicial guardado con valores en 0');
      }

      // Guardar configuraciones
      if (settings) {
        await AsyncStorage.setItem('theme', settings.theme || 'light');
        await AsyncStorage.setItem('soundEnabled', settings.sound_enabled?.toString() || 'true');
        await AsyncStorage.setItem('notificationsEnabled', settings.notifications_enabled?.toString() || 'true');
        console.log('[AuthService][login] Configuraciones guardadas:', settings);
      }
    }
    return response && response.data ? response.data : { success: false, mensaje: 'Respuesta inesperada del backend.' };
  } catch (error) {
    console.log('[AuthService][login] Error FINAL:', error);
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
    // Limpiar TODAS las estrellas y progreso del usuario anterior
    await AsyncStorage.multiRemove([
      'userId',
      'userEmail',
      'userName',
      'userStars',
      'userLevel',
      'totalScore',
      'wordsCompleted',
      'theme',
      'soundEnabled',
      'notificationsEnabled'
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

      const currentWords = await AsyncStorage.getItem('wordsCompleted');
      const newWords = parseInt(currentWords || '0') + wordsCompleted;
      await AsyncStorage.setItem('wordsCompleted', newWords.toString());
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

// ============================================
// ACTUALIZAR PERFIL DE USUARIO
// ============================================
export const updateUserProfile = async (userId, { full_name, email }) => {
  try {
    const response = await axios.put(`${API_URL}/api/user/${userId}/profile`, {
      full_name,
      email
    });

    if (response.data.success) {
      // Actualizar AsyncStorage con los nuevos datos
      await AsyncStorage.setItem('userName', full_name);
      await AsyncStorage.setItem('userEmail', email);
    }

    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return { 
      success: false, 
      mensaje: 'Error de conexión al actualizar perfil' 
    };
  }
};

// ============================================
// ACTUALIZAR CONTRASEÑA DE USUARIO
// ============================================
export const updateUserPassword = async (userId, { current_password, new_password }) => {
  try {
    const response = await axios.put(`${API_URL}/api/user/${userId}/password`, {
      current_password,
      new_password
    });

    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return { 
      success: false, 
      mensaje: 'Error de conexión al actualizar contraseña' 
    };
  }
};

// ============================================
// SOLICITAR RESTABLECIMIENTO DE CONTRASEÑA
// ============================================
export const requestPasswordReset = async (email) => {
  try {
    const response = await axios.post(`${API_URL}/api/forgot-password`, {
      email
    });

    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return { 
      success: false, 
      mensaje: 'Error de conexión al solicitar restablecimiento' 
    };
  }
};

// ============================================
// RESTABLECER CONTRASEÑA CON TOKEN
// ============================================
export const resetPassword = async (token, newPassword) => {
  try {
    const response = await axios.post(`${API_URL}/api/reset-password`, {
      token,
      new_password: newPassword
    });

    return response.data;
  } catch (error) {
    if (error.response) {
      return error.response.data;
    }
    return { 
      success: false, 
      mensaje: 'Error de conexión al restablecer contraseña' 
    };
  }
};
