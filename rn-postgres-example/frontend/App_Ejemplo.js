// ============================================
// EJEMPLO DE App.js CON AUTENTICACIÓN
// ============================================
// Este archivo muestra cómo integrar las pantallas de Login/Register
// con tu app existente de VeneSeñas

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

// Pantallas de autenticación
import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';

// TUS PANTALLAS EXISTENTES (reemplaza con tus rutas reales)
// import LearningScreenDuolingo from './screens/LearningScreenDuolingo';
// import AlphabetModeSelector from './screens/AlphabetModeSelector';
// import FallingSignsGame from './screens/FallingSignsGame';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator 
        initialRouteName="Login"
        screenOptions={{
          headerStyle: {
            backgroundColor: '#007AFF',
          },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}
      >
        {/* ===== AUTENTICACIÓN ===== */}
        <Stack.Screen 
          name="Login" 
          component={LoginScreen}
          options={{ headerShown: false }}
        />
        
        <Stack.Screen 
          name="Register" 
          component={RegisterScreen}
          options={{ 
            title: 'Crear Cuenta',
            headerBackTitle: 'Volver'
          }}
        />

        {/* ===== PANTALLAS PRINCIPALES ===== */}
        {/* Descomenta y reemplaza con tus pantallas reales */}
        {/*
        <Stack.Screen 
          name="Home" 
          component={LearningScreenDuolingo}
          options={{ 
            headerLeft: null, // No permitir volver a login
            title: 'Aprender LSV',
            headerRight: () => <LogoutButton />
          }}
        />

        <Stack.Screen 
          name="AlphabetMode" 
          component={AlphabetModeSelector}
          options={{ title: 'Modo de Aprendizaje' }}
        />

        <Stack.Screen 
          name="FallingSignsGame" 
          component={FallingSignsGame}
          options={{ title: 'Juego de Palabras' }}
        />
        */}
      </Stack.Navigator>
    </NavigationContainer>
  );
}

// ============================================
// BOTÓN DE LOGOUT (Opcional)
// ============================================
/*
import { TouchableOpacity, Text, Alert } from 'react-native';
import { logout } from './services/authAPI';

function LogoutButton() {
  const handleLogout = () => {
    Alert.alert(
      'Cerrar Sesión',
      '¿Estás seguro que deseas salir?',
      [
        { text: 'Cancelar', style: 'cancel' },
        {
          text: 'Salir',
          style: 'destructive',
          onPress: async () => {
            await logout();
            // Navegar a Login (requiere useNavigation hook)
          }
        }
      ]
    );
  };

  return (
    <TouchableOpacity onPress={handleLogout} style={{ marginRight: 15 }}>
      <Text style={{ color: '#fff', fontSize: 16 }}>Salir</Text>
    </TouchableOpacity>
  );
}
*/
