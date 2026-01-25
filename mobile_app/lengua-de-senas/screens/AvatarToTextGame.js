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

// Palabras para el juego del alfabeto (usar solo 8 por ronda)
const ALPHABET_WORDS = [
  'hola', 'adios', 'yo', 'tu', 'casa', 'mesa', 'sol', 'luna',
  'agua', 'pan', 'vida', 'amor', 'todo', 'nada', 'bien', 'mal',
  'gato', 'perro', 'libro', 'flor', 'auto', 'tren', 'avion', 'barco'
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
  const webViewRef = useRef(null); // Ref para comunicarse con el WebView SIN recargarlo
  const [failedWords, setFailedWords] = useState([]); // Palabras fallidas
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [availableWords, setAvailableWords] = useState([]);
  const [roundWords, setRoundWords] = useState([]); // Palabras para esta ronda
  const [currentWordIndex, setCurrentWordIndex] = useState(0); // Índice en la ronda actual
  const [selectedAvatar, setSelectedAvatar] = useState('luis'); // Avatar seleccionado
  const [webViewKey, setWebViewKey] = useState(0); // Key para forzar recarga solo cuando sea necesario

  useEffect(() => {
    loadSelectedAvatar();
    startNewRound();
  }, []);

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

  const startNewRound = () => {
    // Seleccionar 3 palabras aleatorias (reducido de 8)
    const shuffled = [...ALPHABET_WORDS].sort(() => Math.random() - 0.5);
    const selected = shuffled.slice(0, 3);
    setRoundWords(selected);
    setCurrentWordIndex(0);
    setFailedWords([]);
    startNewWord(selected[0]);
  };

  const startNewWord = (word = null) => {
    const wordToUse = word || (roundWords[currentWordIndex] || ALPHABET_WORDS[Math.floor(Math.random() * ALPHABET_WORDS.length)]);
    setTargetWord(wordToUse);
    setUserInput('');
    setCurrentLetter(0);
    setIsAnimating(true);
    
    // Enviar nueva palabra al HTML sin recargar el avatar
    if (webViewRef.current) {
      webViewRef.current.postMessage(JSON.stringify({
        type: 'startNewWord',
        word: wordToUse
      }));
    }
  };

  const handleSubmit = () => {
    const userAnswer = userInput.toLowerCase().trim();
    const correctAnswer = targetWord.toLowerCase().trim();

    if (userAnswer === correctAnswer) {
      // ¡Correcto! Dar 50 estrellas inmediatamente
      const starsForWord = 50;
      setTotalStarsEarned(totalStarsEarned + starsForWord);
      setWordsCompleted(wordsCompleted + 1);
      
      // Dar estrellas a AsyncStorage inmediatamente
      if (onComplete) {
        onComplete(starsForWord);
      }
      
      // Verificar si completamos la ronda
      if (currentWordIndex + 1 >= roundWords.length) {
        // Ronda completada
        if (failedWords.length > 0 && !isReviewMode) {
          // Hay palabras fallidas, ofrecer repaso
          Alert.alert(
            '📚 Repaso de palabras fallidas',
            `Tuviste errores en ${failedWords.length} palabra(s). ¿Quieres repasarlas?\n\nPalabras: ${failedWords.join(', ').toUpperCase()}`,
            [
              {
                text: 'Repasar',
                onPress: () => startReviewMode()
              },
              {
                text: 'Nueva Ronda',
                onPress: () => {
                  setLevel(level + 1);
                  startNewRound();
                }
              }
            ]
          );
        } else {
          // Ronda perfecta o ya estábamos en modo repaso
          Alert.alert(
            '🎉 ¡Ronda completada!',
            `¡Excelente trabajo!\nPalabras completadas: ${wordsCompleted}\n\n⭐ Total estrellas ganadas: ${totalStarsEarned}`,
            [
              {
                text: 'Siguiente Ronda',
                onPress: () => {
                  setLevel(level + 1);
                  startNewRound();
                }
              }
            ]
          );
        }
      } else {
        // Continuar con la siguiente palabra
        Alert.alert(
          '🎉 ¡Correcto!',
          `¡Excelente! La palabra era "${correctAnswer.toUpperCase()}"\n\n⭐ +50 estrellas ganadas`,
          [
            {
              text: 'Continuar',
              onPress: () => {
                const nextIndex = currentWordIndex + 1;
                setCurrentWordIndex(nextIndex);
                startNewWord(roundWords[nextIndex]);
              }
            }
          ]
        );
      }
    } else {
      // Incorrecto - guardar palabra fallida
      if (!failedWords.includes(targetWord)) {
        setFailedWords([...failedWords, targetWord]);
      }
      setLives(lives - 1);
      
      if (lives - 1 === 0) {
        setGameOver(true);
        Alert.alert(
          '💔 Game Over',
          `La palabra era: "${correctAnswer.toUpperCase()}"\n\nPalabras completadas: ${wordsCompleted}\n⭐ Estrellas ganadas: ${totalStarsEarned}`,
          [
            {
              text: 'Reintentar',
              onPress: () => restartGame()
            },
            {
              text: 'Salir',
              onPress: () => navigation.goBack()
            }
          ]
        );
      } else {
        Alert.alert(
          '❌ Incorrecto',
          `La palabra era: "${correctAnswer.toUpperCase()}"\nInténtalo con la siguiente`,
          [
            {
              text: 'Continuar',
              onPress: () => {
                if (currentWordIndex + 1 < roundWords.length) {
                  const nextIndex = currentWordIndex + 1;
                  setCurrentWordIndex(nextIndex);
                  startNewWord(roundWords[nextIndex]);
                } else {
                  // Fin de ronda con error
                  startNewRound();
                }
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
    setTotalStarsEarned(0);
    setLives(3); // 3 vidas con guacamaya 🦜 - REINICIAR VIDAS AQUÍ
    setLevel(1);
    setGameOver(false);
    setWordsCompleted(0);
    setIsReviewMode(false);
    setFailedWords([]);
    setCurrentWordIndex(0);
    startNewRound();
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
    
    // Solicitar repetición sin recargar el avatar
    if (webViewRef.current && targetWord) {
      webViewRef.current.postMessage(JSON.stringify({
        type: 'replayWord',
        word: targetWord
      }));
    }
  };

  // Construir URL para el avatar con deletreo letra por letra
  const getAnimationUrl = () => {
    // Removido &v=${Date.now()} para evitar recargas constantes
    return `http://192.168.10.93:8000/avatar_spelling_optimized.html?word=${encodeURIComponent(targetWord)}&avatar=${selectedAvatar}&autoplay=true`;
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
        <TouchableOpacity onPress={() => navigation.goBack()}>
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
        <View style={styles.roundProgressContainer}>
          <Text style={styles.roundProgressText}>
            Palabra {currentWordIndex + 1} de {roundWords.length}
          </Text>
        </View>
      </View>

      {/* Avatar Animation Area */}
      <View style={styles.animationContainer}>
        {targetWord ? (
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
            startInLoadingState={false}
            useWebKit={true}
            sharedCookiesEnabled={true}
            thirdPartyCookiesEnabled={true}
          />
        ) : (
          <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="#667eea" />
          </View>
        )}

        {/* Replay Button */}
        <TouchableOpacity 
          style={styles.replayButton}
          onPress={replayAnimation}
        >
          <Ionicons name="refresh" size={24} color="#fff" />
          <Text style={styles.replayButtonText}>Repetir</Text>
        </TouchableOpacity>

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
