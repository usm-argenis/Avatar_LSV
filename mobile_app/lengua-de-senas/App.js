import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';

// Importar pantallas
import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';
import MainScreen from './screens/MainScreen';
import HomeScreen from './screens/HomeScreen';
import LearningScreen from './screens/LearningScreen';
import LearningScreenDuolingo from './screens/LearningScreenDuolingo';
import LessonScreen from './screens/LessonScreen';
import TranslatorScreen from './screens/TranslatorScreen';
import LSVTranslatorScreen from './screens/LSVTranslatorScreen';
import SettingsScreen from './screens/SettingsScreen';
import AlphabetIntroductionScreen from './screens/AlphabetIntroductionScreen';
import NumbersIntroductionScreen from './screens/NumbersIntroductionScreen';
import AlphabetModeSelector from './screens/AlphabetModeSelector';
import FallingSignsGame from './screens/FallingSignsGame';
import AvatarToTextGame from './screens/AvatarToTextGame';
import MathOperationsGame from './screens/MathOperationsGame';
import CulturalModule from './screens/CulturalModule';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <SafeAreaProvider>
      <NavigationContainer>
        <StatusBar style="light" />
        <Stack.Navigator
          initialRouteName="Login"
          screenOptions={{
            headerShown: false,
            animation: 'slide_from_right',
          }}
        >
          {/* Autenticación */}
          <Stack.Screen name="Login" component={LoginScreen} />
          <Stack.Screen name="Register" component={RegisterScreen} />
          
          {/* Pantallas principales */}
          <Stack.Screen name="Main" component={MainScreen} />
          <Stack.Screen name="Home" component={HomeScreen} />
          
          {/* Aprendizaje */}
          <Stack.Screen name="Learning" component={LearningScreen} />
          <Stack.Screen name="LearningDuolingo" component={LearningScreenDuolingo} />
          <Stack.Screen name="Lesson" component={LessonScreen} />
          
          {/* Traducción */}
          <Stack.Screen name="Translator" component={TranslatorScreen} />
          <Stack.Screen name="LSVTranslator" component={LSVTranslatorScreen} />
          
          {/* Configuración */}
          <Stack.Screen name="Settings" component={SettingsScreen} />
          
          {/* Lecciones específicas */}
          <Stack.Screen name="AlphabetIntroduction" component={AlphabetIntroductionScreen} />
          <Stack.Screen name="NumbersIntroduction" component={NumbersIntroductionScreen} />
          <Stack.Screen name="AlphabetModeSelector" component={AlphabetModeSelector} />
          
          {/* Juegos */}
          <Stack.Screen name="FallingSignsGame" component={FallingSignsGame} />
          <Stack.Screen name="AvatarToTextGame" component={AvatarToTextGame} />
          <Stack.Screen name="MathOperationsGame" component={MathOperationsGame} />
          {/* Alias para compatibilidad con navegaciones antiguas */}
          <Stack.Screen name="MathOperations" component={MathOperationsGame} />
          
          {/* Módulos adicionales */}
          <Stack.Screen name="CulturalModule" component={CulturalModule} />
        </Stack.Navigator>
      </NavigationContainer>
    </SafeAreaProvider>
  );
}
