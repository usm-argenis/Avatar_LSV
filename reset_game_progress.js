#!/usr/bin/env node

/**
 * Script para limpiar el progreso del juego Avatar a Texto
 * 
 * CÓMO USAR:
 * 1. Abre la consola de React Native Debugger
 * 2. Copia y pega este código en la consola
 * 3. Presiona Enter
 * 
 * O simplemente usa el botón de reset en la app
 */

const resetGameProgress = async () => {
  try {
    const AsyncStorage = require('@react-native-async-storage/async-storage').default;
    
    // Obtener userId
    const userId = await AsyncStorage.getItem('userId');
    console.log(`🔍 Usuario encontrado: ${userId}`);
    
    if (userId) {
      // Limpiar nivel
      const levelKey = `currentLevel_${userId}`;
      const currentLevel = await AsyncStorage.getItem(levelKey);
      console.log(`📊 Nivel actual: ${currentLevel}`);
      
      await AsyncStorage.setItem(levelKey, '1');
      console.log('✅ Nivel reseteado a 1');
      
      // Mostrar todas las claves guardadas para este usuario
      const allKeys = await AsyncStorage.getAllKeys();
      const userKeys = allKeys.filter(key => key.includes(userId));
      console.log('🔑 Claves del usuario:', userKeys);
      
      for (const key of userKeys) {
        const value = await AsyncStorage.getItem(key);
        console.log(`  ${key}: ${value}`);
      }
      
      console.log('✅ Progreso reseteado exitosamente');
      console.log('⚠️ Cierra y vuelve a abrir el juego para ver los cambios');
    } else {
      console.error('❌ No se encontró userId');
    }
  } catch (error) {
    console.error('❌ Error:', error);
  }
};

// Ejecutar
resetGameProgress();
