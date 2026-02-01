import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  StatusBar,
  TextInput,
  Alert,
  Modal,
  ActivityIndicator
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { WebView } from 'react-native-webview';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Palabras organizadas por nivel de dificultad
const NIVEL_1_PALABRAS = [
  'yo', 'tu', 'el', 'si', 'no',
  'sol', 'mar', 'pan', 'luz', 'paz',
  'oso', 'pie', 'rey', 'sed', 'sal'
];

const NIVEL_2_PALABRAS = [
  'casa', 'mesa', 'hola', 'luna', 'agua',
  'vida', 'amor', 'todo', 'nada', 'gato',
  'rosa', 'cafe', 'pelo', 'mano', 'pies',
  'ojos', 'boca', 'cara', 'ropa', 'sopa'
];

const NIVEL_3_PALABRAS = [
  'perro', 'libro', 'flor', 'auto', 'tren',
  'avion', 'barco', 'cielo', 'tierra', 'fuego',
  'viento', 'amigo', 'familia', 'escuela', 'persona',
  'ciudad', 'trabajo', 'tiempo', 'mundo', 'nombre'
];

const AvatarToTextGame = ({ route, navigation }) => {
  const { category, starReward = 150, onComplete } = route.params;
  
  const [targetWord, setTargetWord] = useState('');
  const [userInput, setUserInput] = useState('');
  const [totalStarsEarned, setTotalStarsEarned] = useState(0); // Total de estrellas ganadas
  const [level, setLevel] = useState(1);
  const [lives, setLives] = useState(3); // 3 vidas con guacamaya 🦜
  const [gameOver, setGameOver] = useState(false);
  const [currentLetter, setCurrentLetter] = useState(0);
  const [isAnimating, setIsAnimating] = useState(false);
  const [wordsCompleted, setWordsCompleted] = useState(0);
  const [wordsCompletedInLevel, setWordsCompletedInLevel] = useState(0); // Palabras completadas en nivel actual
  const webViewRef = useRef(null); // Ref para comunicarse con el WebView SIN recargarlo
  const [failedWords, setFailedWords] = useState([]); // Palabras fallidas
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [availableWords, setAvailableWords] = useState([]);
  
  // Configuración de palabras necesarias por nivel
  const WORDS_NEEDED_PER_LEVEL = {
    1: 1, // 1 palabra correcta para pasar de nivel 1 a nivel 2
    2: 1, // 1 palabra correcta para pasar de nivel 2 a nivel 3
    3: 1  // 1 palabra correcta para completar el juego
  };
  const [roundWords, setRoundWords] = useState([]); // Palabras para esta ronda
  const [currentWordIndex, setCurrentWordIndex] = useState(0); // Índice en la ronda actual
  const [selectedAvatar, setSelectedAvatar] = useState('luis'); // Avatar seleccionado
  const [webViewKey, setWebViewKey] = useState(0); // Key para forzar recarga solo cuando sea necesario
  const [webViewReady, setWebViewReady] = useState(false); // Saber cuando WebView está listo
  const [pendingWord, setPendingWord] = useState(null); // Palabra pendiente de enviar
  const [hasFailedCurrentWord, setHasFailedCurrentWord] = useState(false); // Si falló en la palabra actual

  useEffect(() => {
    const init = async () => {
      console.log('🚀 [AvatarToTextGame] Iniciando juego en nivel 1...');
      await loadSelectedAvatar();
      // Siempre iniciar en nivel 1
      setLevel(1);
      setWordsCompletedInLevel(0);
      console.log(`🎮 [AvatarToTextGame] Nivel inicial: 1`);
      
      // Esperar a que el WebView se cargue completamente antes de enviar mensaje
      setTimeout(() => {
        console.log('📤 [AvatarToTextGame] Iniciando primera palabra...');
        startNewRound();
      }, 500); // Optimizado: reducido de 1000ms a 500ms
    };
    init();
  }, []);

  // Enviar mensaje pendiente cuando WebView esté listo
  useEffect(() => {
    if (webViewReady && pendingWord && webViewRef.current) {
      console.log('✅ WebView ahora listo, enviando mensaje pendiente:', pendingWord);
      webViewRef.current.postMessage(JSON.stringify(pendingWord));
      setPendingWord(null);
    }
  }, [webViewReady, pendingWord]);

  // Detectar cambio de avatar desde AsyncStorage (cuando el usuario lo cambia en configuración)
  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const avatar = await AsyncStorage.getItem('selectedAvatar');
        if (avatar && avatar !== selectedAvatar) {
          // Avatar cambió, actualizar y forzar recarga del WebView
          setSelectedAvatar(avatar);
          setWebViewKey(prev => prev + 1); // Forzar recarga del WebView
        }
      } catch (error) {
        console.error('Error verificando avatar:', error);
      }
    }, 2000); // Revisar cada 2 segundos

    return () => clearInterval(interval);
  }, [selectedAvatar]);

  const loadSelectedAvatar = async () => {
    try {
      const avatar = await AsyncStorage.getItem('selectedAvatar');
      if (avatar) {
        setSelectedAvatar(avatar);
      }
    } catch (error) {
      console.error('Error cargando avatar:', error);
    }
  };

  const loadCurrentLevel = async () => {
    try {
      const userId = await AsyncStorage.getItem('userId');
      if (userId) {
        const levelKey = `currentLevel_${userId}`;
        const savedLevel = await AsyncStorage.getItem(levelKey);
        if (savedLevel) {
          const parsedLevel = parseInt(savedLevel, 10);
          console.log(`🎮 [AvatarToTextGame] Nivel cargado: ${parsedLevel}`);
          
          // VALIDACIÓN: Si el nivel es inválido, resetear a 1
          if (parsedLevel < 1 || parsedLevel > 3 || isNaN(parsedLevel)) {
            console.warn(`⚠️ Nivel inválido (${parsedLevel}), reseteando a 1`);
            setLevel(1);
            await AsyncStorage.setItem(levelKey, '1');
          } else {
            setLevel(parsedLevel);
          }
        } else {
          // No hay nivel guardado, usar nivel 1
          console.log(`🎮 [AvatarToTextGame] Sin nivel guardado, iniciando en nivel 1`);
          setLevel(1);
        }
      }
    } catch (error) {
      console.error('Error cargando nivel:', error);
      setLevel(1); // En caso de error, usar nivel 1
    }
  };

  // Función para resetear el progreso (útil para depuración)
  const resetProgress = async () => {
    try {
      const userId = await AsyncStorage.getItem('userId');
      if (userId) {
        await AsyncStorage.setItem(`currentLevel_${userId}`, '1');
        setLevel(1);
        setWordsCompletedInLevel(0);
        setWordsCompleted(0);
        setTotalStarsEarned(0);
        setLives(3);
        console.log(`🔄 [AvatarToTextGame] Progreso reseteado a nivel 1`);
        Alert.alert('✅ Progreso Reseteado', 'Has vuelto al Nivel 1');
        startNewRound();
      }
    } catch (error) {
      console.error('Error reseteando progreso:', error);
    }
  };

  const startNewRound = (currentLevel = null, keepFailedFlag = false) => {
    // Usar nivel pasado como parámetro o el estado actual
    const levelToUse = currentLevel !== null ? currentLevel : level;
    console.log(`🎮 [AvatarToTextGame] startNewRound con nivel: ${levelToUse}, keepFailedFlag: ${keepFailedFlag}`);
    
    // Seleccionar palabras según el nivel
    let levelWords;
    if (levelToUse === 1) {
      levelWords = NIVEL_1_PALABRAS;
    } else if (levelToUse === 2) {
      levelWords = NIVEL_2_PALABRAS;
    } else {
      levelWords = NIVEL_3_PALABRAS;
    }
    
    // Seleccionar 1 palabra aleatoria del nivel
    const shuffled = [...levelWords].sort(() => Math.random() - 0.5);
    const selected = shuffled.slice(0, 1);
    setRoundWords(selected);
    setCurrentWordIndex(0);
    setFailedWords([]);
    startNewWord(selected[0], levelToUse, keepFailedFlag);
  };

  const startNewWord = (word = null, currentLevel = null, keepFailedFlag = false) => {
    // Usar nivel pasado como parámetro o el estado actual
    const levelToUse = currentLevel !== null ? currentLevel : level;
    
    const wordToUse = word || (roundWords[currentWordIndex] || NIVEL_1_PALABRAS[Math.floor(Math.random() * NIVEL_1_PALABRAS.length)]);
    
    console.log(`📝 [startNewWord] Configurando nueva palabra: "${wordToUse}" (nivel ${levelToUse}, keepFailedFlag: ${keepFailedFlag})`);
    console.log(`   ├─ Parámetro 'word': ${word || 'null'}`);
    console.log(`   ├─ roundWords[${currentWordIndex}]: ${roundWords[currentWordIndex] || 'undefined'}`);
    console.log(`   └─ Palabra seleccionada: "${wordToUse}"`);
    
    setTargetWord(wordToUse);
    setUserInput('');
    setCurrentLetter(0);
    setIsAnimating(true);
    
    // Solo resetear flag si NO viene de un fallo
    if (!keepFailedFlag) {
      setHasFailedCurrentWord(false);
      console.log(`   └─ Flag de fallo reseteado`);
    } else {
      console.log(`   └─ Flag de fallo MANTENIDO (usuario falló antes)`);
    }
    
    // Determinar velocidad según nivel (duración en segundos)
    let speed = 3.0; // Nivel 1: 3 segundos (más lento)
    if (levelToUse === 2) speed = 2; // Nivel 2: 1.4 segundos (medio)
    if (levelToUse >= 3) speed = 1.5; // Nivel 3: 1.0 segundo (más rápido)
    
    console.log(`📤 Enviando a HTML: palabra="${wordToUse}", speed=${speed}s, level=${levelToUse}, webViewReady=${webViewReady}`);
    
    // Crear mensaje
    const message = {
      type: 'startNewWord',
      word: wordToUse,
      speed: speed,
      level: levelToUse
    };
    
    // Si el WebView está listo, enviar inmediatamente
    if (webViewReady && webViewRef.current) {
      console.log('✅ WebView listo, enviando mensaje ahora');
      webViewRef.current.postMessage(JSON.stringify(message));
    } else {
      // Si no, guardar para enviar cuando esté listo
      console.log('⏳ WebView no listo, guardando mensaje pendiente');
      setPendingWord(message);
    }
  };

  const handleSubmit = () => {
    const userAnswer = userInput.toLowerCase().trim();
    const correctAnswer = targetWord.toLowerCase().trim();

    if (userAnswer === correctAnswer) {
      // ¡Correcto! Dar 50 estrellas por completar nivel
      const starsForWord = 50; // Siempre 50 estrellas por pasar de nivel
      setTotalStarsEarned(totalStarsEarned + starsForWord);
      setWordsCompleted(wordsCompleted + 1);
      const newWordsInLevel = wordsCompletedInLevel + 1;
      setWordsCompletedInLevel(newWordsInLevel);
      
      if (hasFailedCurrentWord) {
        console.log(`⭐ [AvatarToTextGame] Respuesta correcta (después de fallar)! +${starsForWord} estrellas (Total: ${totalStarsEarned + starsForWord})`);
      } else {
        console.log(`⭐ [AvatarToTextGame] Respuesta correcta (primer intento)! +${starsForWord} estrellas (Total: ${totalStarsEarned + starsForWord})`);
      }
      
      const wordsNeeded = WORDS_NEEDED_PER_LEVEL[level];
      
      // Verificar si completó todas las palabras necesarias en este nivel
      if (newWordsInLevel >= wordsNeeded) {
        // Completó las palabras necesarias en este nivel
        if (level === 3) {
          // ¡Ganó el juego! Completó el nivel 3
          const finalStars = totalStarsEarned + starsForWord;
          Alert.alert(
            '🏆 ¡Felicitaciones!',
            `¡Completaste todos los niveles!\n\nPalabras totales: ${wordsCompleted + 1}\n⭐ Total estrellas: ${finalStars}`,
            [
              {
                text: 'Jugar de Nuevo',
                onPress: () => restartGame()
              },
              {
                text: 'Salir',
                onPress: async () => {
                  // Guardar todas las estrellas ganadas antes de salir
                  console.log(`💾 [AvatarToTextGame] Guardando ${finalStars} estrellas antes de salir`);
                  if (onComplete) {
                    await onComplete(finalStars); // Enviar el total de estrellas ganadas
                  }
                  navigation.goBack();
                }
              }
            ]
          );
        } else {
          // Avanzar al siguiente nivel
          Alert.alert(
            '🎉 ¡Correcto!',
            `¡Excelente! Pasaste al Nivel ${level + 1}\n\n⭐ +${starsForWord} estrellas`,
            [
              {
                text: 'Continuar',
                onPress: async () => {
                  const newLevel = level + 1;
                  console.log(`🎯 [AvatarToTextGame] Pasando de nivel ${level} a ${newLevel}...`);
                  setLevel(newLevel);
                  setWordsCompletedInLevel(0); // Reiniciar contador para nuevo nivel
                  
                  // Guardar nivel en AsyncStorage (sin await para no bloquear)
                  const userId = await AsyncStorage.getItem('userId');
                  if (userId) {
                    AsyncStorage.setItem(`currentLevel_${userId}`, newLevel.toString())
                      .then(() => console.log(`📊 [AvatarToTextGame] Nivel guardado: ${newLevel}`))
                      .catch(error => console.error('Error guardando nivel:', error));
                  }
                  
                  // Delay aumentado para nivel 3 para dar más tiempo de procesamiento
                  const delay = newLevel === 3 ? 500 : 300;
                  console.log(`🔄 [AvatarToTextGame] Iniciando nivel ${newLevel} en ${delay}ms...`);
                  setTimeout(() => {
                    console.log(`▶️ [AvatarToTextGame] Ejecutando startNewRound(${newLevel})...`);
                    startNewRound(newLevel);
                  }, delay);
                }
              }
            ]
          );
        }
      } else {
        // Aún faltan palabras en este nivel (NO DEBERÍA LLEGAR AQUÍ con 1 palabra por nivel)
        const remaining = wordsNeeded - newWordsInLevel;
        Alert.alert(
          '✅ ¡Correcto!',
          `¡Muy bien! Nivel ${level}\nProgreso: ${newWordsInLevel}/${wordsNeeded}\n${remaining} palabra${remaining > 1 ? 's' : ''} más para avanzar\n\n⭐ +${starsForWord} estrellas`,
          [
            {
              text: 'Continuar',
              onPress: () => {
                // Llamar directamente sin setTimeout
                startNewRound();
              }
            }
          ]
        );
      }
    } else {
      // Incorrecto - perder vida y marcar que falló
      setLives(lives - 1);
      setHasFailedCurrentWord(true); // Marcar que falló esta palabra
      
      console.log(`❌ [AvatarToTextGame] Respuesta incorrecta. Vidas restantes: ${lives - 1}`);
      
      if (lives - 1 === 0) {
        setGameOver(true);
        Alert.alert(
          '💔 Game Over',
          `La palabra era: "${correctAnswer.toUpperCase()}"\n\nNivel alcanzado: ${level}\nPalabras completadas: ${wordsCompleted}\n⭐ Estrellas ganadas: ${totalStarsEarned}`,
          [
            {
              text: 'Reintentar',
              onPress: () => restartGame()
            },
            {
              text: 'Salir',
              onPress: async () => {
                // Guardar estrellas antes de salir
                console.log(`💾 [AvatarToTextGame] Guardando ${totalStarsEarned} estrellas al salir (Game Over)`);
                if (onComplete && totalStarsEarned > 0) {
                  await onComplete(totalStarsEarned);
                }
                navigation.goBack();
              }
            }
          ]
        );
      } else {
        Alert.alert(
          '❌ Incorrecto',
          `La palabra era: "${correctAnswer.toUpperCase()}"`,
          [
            {
              text: 'Continuar',
              onPress: () => {
                // Mostrar una palabra NUEVA (no la misma) pero mantener el flag de fallo
                console.log(`🔄 [Incorrecto] Generando nueva palabra (nivel ${level}) manteniendo flag de fallo`);
                // Generar nueva ronda con nueva palabra PERO mantener flag de fallo
                startNewRound(level, true); // keepFailedFlag = true
              }
            }
          ]
        );
      }
    }
  };

  const startReviewMode = () => {
    setIsReviewMode(true);
    setRoundWords(failedWords);
    setCurrentWordIndex(0);
    setFailedWords([]);
    startNewWord(failedWords[0]);
  };

  const restartGame = () => {
    console.log('🔄 [AvatarToTextGame] Reiniciando juego desde nivel 1');
    setTotalStarsEarned(0);
    setLives(3); // 3 vidas con guacamaya 🦜 - REINICIAR VIDAS AQUÍ
    setLevel(1);
    setWordsCompletedInLevel(0); // Reiniciar contador de palabras por nivel
    setGameOver(false);
    setWordsCompleted(0);
    setIsReviewMode(false);
    setFailedWords([]);
    setCurrentWordIndex(0);
    setRoundWords([]); // Limpiar palabras previas
    setHasFailedCurrentWord(false); // Resetear flag de fallo
    // Iniciar nueva ronda explícitamente en nivel 1
    startNewRound(1);
  };

  const handleAnimationProgress = (event) => {
    // Este mensaje vendrá del WebView cuando termine cada letra
    try {
      const data = JSON.parse(event.nativeEvent.data);
      if (data.type === 'letterComplete') {
        setCurrentLetter(data.letterIndex);
      } else if (data.type === 'allComplete') {
        setIsAnimating(false);
      }
    } catch (e) {
      // Ignorar errores de parsing
    }
  };

  const replayAnimation = () => {
    setCurrentLetter(0);
    setIsAnimating(true);
    
    // IMPORTANTE: Usar level del estado actual
    const currentLevel = level;
    
    // Determinar velocidad según nivel (duración en segundos) - IGUAL que startNewWord
    let speed = 3.0; // Nivel 1: 3 segundos (más lento)
    if (currentLevel === 2) speed = 2; // Nivel 2: 2 segundos (medio)
    if (currentLevel >= 3) speed = 1.5; // Nivel 3: 1.5 segundos (más rápido)
    
    console.log(`🔄 [Replay] Repitiendo palabra "${targetWord}" con nivel=${currentLevel}, speed=${speed}s`);
    
    // Solicitar repetición sin recargar el avatar - usar la palabra ACTUAL (targetWord)
    if (webViewRef.current && targetWord) {
      console.log(`🔄 [Replay] Enviando comando de repetición para "${targetWord}"`);
      webViewRef.current.postMessage(JSON.stringify({
        type: 'replayWord',
        word: targetWord, // Siempre usar la palabra que se está mostrando actualmente
        speed: speed,
        level: currentLevel
      }));
    } else {
      console.error('❌ [Replay] No se puede repetir: webViewRef o targetWord no disponible');
    }
  };

  // Función para manejar el cierre del juego guardando las estrellas
  const handleExit = async () => {
    if (totalStarsEarned > 0) {
      console.log(`💾 [AvatarToTextGame] Guardando ${totalStarsEarned} estrellas antes de salir (botón cerrar)`);
      if (onComplete) {
        await onComplete(totalStarsEarned);
      }
    }
    navigation.goBack();
  };

  // Construir URL para el avatar con deletreo letra por letra
  const getAnimationUrl = () => {
    // Agregar timestamp para forzar actualización de caché
    const cacheVersion = '20260126c'; // Actualizar esta fecha cuando cambies el HTML
    // NO incluir autoplay para que espere el mensaje de React Native con la velocidad correcta
    return `http://192.168.10.93:8000/avatar_spelling_optimized.html?avatar=${selectedAvatar}&v=${cacheVersion}`;
  };

  return (
    <SafeAreaView style={styles.container} edges={['bottom']}>
      <StatusBar barStyle="light-content" backgroundColor="#04309e" translucent={true} />

      {/* Header */}
      <LinearGradient
        colors={['#04309e', '#0056b3', '#34a3fd', '#77c1fd', '#cfe8fa', '#ffffff']}
        style={styles.header}
        start={{ x: 0.5, y: 0 }}
        end={{ x: 0.5, y: 1 }}
      >
        <TouchableOpacity onPress={handleExit}>
          <Ionicons name="close" size={28} color="#000000" />
        </TouchableOpacity>
        
        <Text style={styles.headerTitle}>Avatar a Texto</Text>

        <View style={styles.headerStats}>
          <Text style={styles.headerStatText}>⭐ {totalStarsEarned}</Text>
          <Text style={styles.headerStatText}>🦜 {lives}</Text>
          <Text style={styles.headerStatText}>📊 Nivel {level}</Text>
        </View>
      </LinearGradient>

      {/* Instructions */}
      <View style={styles.instructionsContainer}>
        <Text style={styles.instructionsTitle}>
          🎯 Mira el avatar y escribe la palabra
        </Text>
        <Text style={styles.instructionsText}>
          El avatar deletreará una palabra letra por letra. ¡Escribe lo que ves!
        </Text>
        {isReviewMode && (
          <View style={styles.reviewBanner}>
            <Text style={styles.reviewBannerText}>📚 Modo Repaso - Palabras Fallidas</Text>
          </View>
        )}
      </View>

      {/* Avatar Animation Area */}
      <View style={styles.animationContainer}>
        <WebView
          key={`webview-${selectedAvatar}-${webViewKey}`}
          ref={webViewRef}
          source={{ uri: getAnimationUrl() }}
          originWhitelist={['*']}
          javaScriptEnabled={true}
          domStorageEnabled={true}
          allowsInlineMediaPlayback={true}
          mediaPlaybackRequiresUserAction={false}
          style={styles.webview}
          onMessage={handleAnimationProgress}
          onLoad={() => {
            console.log('✅ WebView cargado completamente');
            setWebViewReady(true);
          }}
          startInLoadingState={true}
          renderLoading={() => (
            <View style={styles.loadingContainer}>
              <ActivityIndicator size="large" color="#667eea" />
              <Text style={styles.loadingText}>Cargando avatar...</Text>
            </View>
          )}
          useWebKit={true}
          sharedCookiesEnabled={true}
          thirdPartyCookiesEnabled={true}
        />

        

        {/* Progress Indicator */}
        {isAnimating && (
          <View style={styles.progressIndicator}>
            <Text style={styles.progressText}>
              📝 Letra {currentLetter + 1} de {targetWord.length}
            </Text>
          </View>
        )}
      </View>

      {/* Input Area */}
      <View style={styles.inputContainer}>
        <Text style={styles.inputLabel}>✍️ Escribe la palabra:</Text>
        
        <View style={styles.inputWrapper}>
          <TextInput
            style={styles.input}
            value={userInput}
            onChangeText={setUserInput}
            placeholder="Escribe aquí..."
            placeholderTextColor="#999"
            autoCapitalize="none"
            autoCorrect={false}
            editable={!gameOver && !isAnimating}
          />
          
          {isAnimating ? (
            <View style={styles.loadingButton}>
              <ActivityIndicator size="small" color="#fff" />
              <Text style={styles.loadingButtonText}>Animando...</Text>
            </View>
          ) : (
            <TouchableOpacity
              style={[
                styles.submitButton,
                (!userInput.trim() || gameOver) && styles.submitButtonDisabled
              ]}
              onPress={handleSubmit}
              disabled={!userInput.trim() || gameOver}
            >
              <Text style={styles.submitButtonText}>Enviar</Text>
            </TouchableOpacity>
          )}
        </View>

        <Text style={styles.hintText}>
          💡 Pista: La palabra tiene {targetWord.length} letras
        </Text>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F8F9FA',
  },
  header: {
    height: 100,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
    paddingTop: StatusBar.currentHeight || 30,
    paddingBottom: 10,
  },
  headerTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#000',
  },
  headerStats: {
    flexDirection: 'row',
    gap: 10,
  },
  headerStatText: {
    color: '#000000',
    fontSize: 14,
    fontWeight: 'bold',
  },
  instructionsContainer: {
    backgroundColor: '#fff',
    padding: 15,
    borderBottomWidth: 1,
    borderBottomColor: '#E0E0E0',
  },
  instructionsTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 5,
  },
  instructionsText: {
    fontSize: 14,
    color: '#666',
  },
  reviewBanner: {
    backgroundColor: '#FFA500',
    paddingVertical: 8,
    paddingHorizontal: 15,
    borderRadius: 20,
    marginTop: 10,
    alignSelf: 'center',
  },
  reviewBannerText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 14,
  },
  roundProgressContainer: {
    marginTop: 10,
    alignItems: 'center',
  },
  roundProgressText: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#667eea',
  },
  animationContainer: {
    flex: 1,
    backgroundColor: '#1a1a2e',
    position: 'relative',
  },
  webview: {
    flex: 1,
    backgroundColor: '#1a1a2e',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#1a1a2e',
  },
  loadingText: {
    color: '#fff',
    marginTop: 10,
    fontSize: 14,
  },
  loadingText: {
    marginTop: 10,
    color: '#fff',
    fontSize: 14,
  },
  replayButton: {
    position: 'absolute',
    top: 15,
    right: 15,
    backgroundColor: 'rgba(102, 126, 234, 0.9)',
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 15,
    paddingVertical: 8,
    borderRadius: 20,
    gap: 5,
  },
  replayButtonText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 14,
  },
  progressIndicator: {
    position: 'absolute',
    bottom: 15,
    alignSelf: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.7)',
    paddingHorizontal: 20,
    paddingVertical: 10,
    borderRadius: 20,
  },
  progressText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 14,
  },
  inputContainer: {
    backgroundColor: '#fff',
    padding: 20,
    borderTopWidth: 1,
    borderTopColor: '#E0E0E0',
  },
  inputLabel: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
  },
  inputWrapper: {
    flexDirection: 'row',
    gap: 10,
  },
  input: {
    flex: 1,
    backgroundColor: '#F5F5F5',
    borderRadius: 10,
    paddingHorizontal: 15,
    paddingVertical: 12,
    fontSize: 16,
    color: '#333',
    borderWidth: 2,
    borderColor: '#E0E0E0',
  },
  submitButton: {
    backgroundColor: '#667eea',
    paddingHorizontal: 25,
    paddingVertical: 12,
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
  },
  submitButtonDisabled: {
    backgroundColor: '#ccc',
  },
  submitButtonText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 16,
  },
  loadingButton: {
    backgroundColor: '#667eea',
    paddingHorizontal: 25,
    paddingVertical: 12,
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    flexDirection: 'row',
    gap: 8,
  },
  loadingButtonText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 16,
  },
  hintText: {
    marginTop: 10,
    fontSize: 14,
    color: '#666',
    textAlign: 'center',
  },
});

export default AvatarToTextGame;
