import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  StatusBar,
  Dimensions,
  Alert,
  Animated,
  Modal,
  Image
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { WebView } from 'react-native-webview';
import AsyncStorage from '@react-native-async-storage/async-storage';

const { width, height } = Dimensions.get('window');

// Datos de cada categoría (vocabulario expandido)
const lessonData = {
  alfabeto: [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
  ],
  numeros: [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
    '20', '30', '40', '50', '60', '70', '80', '90', '100'
  ],
  saludos: [
    'hola', 'adios', 'buenos dias', 'buenas tardes', 'buenas noches', 
    'chao', 'bienvenido', 'hasta luego', 'nos vemos', 'que tengas buen dia',
    'feliz dia', 'saludos', 'mucho gusto', 'encantado', 'bienvenida'
  ],
  pronombres: [
    'yo', 'tu', 'el', 'ella', 'nosotros', 'ustedes', 'ellos', 'ellas',
    'mi', 'tuyo', 'suyo'
  ],
  dias_semana: [
    'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'
  ],
  tiempo: [
    'hoy', 'ayer', 'mañana', 'anteayer', 'pasado mañana', 
    'semana', 'mes', 'año', 'dia', 'hora', 'minuto',
    'fin de semana', 'ahora', 'despues', 'antes'
  ],
  cortesia: [
    'gracias', 'permiso', 'por favor', 'disculpe', 'de nada', 
    'mucho gusto', 'perdon', 'lo siento', 'con permiso', 'buen provecho'
  ],
  preguntas: [
    'como', 'que', 'quien', 'donde', 'cuando', 'por que', 'cual', 'cuanto'
  ]
};

// Mapeo de imágenes del alfabeto
const letterImages = {
  'a': require('../assets/alfabeto/A.png'),
  'b': require('../assets/alfabeto/B.png'),
  'c': require('../assets/alfabeto/C.png'),
  'd': require('../assets/alfabeto/D.png'),
  'e': require('../assets/alfabeto/E.png'),
  'f': require('../assets/alfabeto/F.png'),
  'g': require('../assets/alfabeto/G.png'),
  'h': require('../assets/alfabeto/H.png'),
  'i': require('../assets/alfabeto/I.png'),
  'j': require('../assets/alfabeto/J.png'),
  'k': require('../assets/alfabeto/K.png'),
  'l': require('../assets/alfabeto/L.png'),
  'm': require('../assets/alfabeto/M.png'),
  'n': require('../assets/alfabeto/N.png'),
  'ñ': require('../assets/alfabeto/Ñ.png'),
  'o': require('../assets/alfabeto/O.png'),
  'p': require('../assets/alfabeto/P.png'),
  'q': require('../assets/alfabeto/Q.png'),
  'r': require('../assets/alfabeto/R.png'),
  's': require('../assets/alfabeto/S.png'),
  't': require('../assets/alfabeto/T.png'),
  'u': require('../assets/alfabeto/U.png'),
  'v': require('../assets/alfabeto/V.png'),
  'w': require('../assets/alfabeto/W.png'),
  'x': require('../assets/alfabeto/X.png'),
  'y': require('../assets/alfabeto/Y.png'),
  'z': require('../assets/alfabeto/Z.png'),
};

const LessonScreen = ({ route, navigation }) => {
  const { category, title, starReward = 100, onComplete } = route.params;
  
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [lives, setLives] = useState(3); // Siempre 3 vidas con guacamaya 🦜
  const [showResult, setShowResult] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [showAnimation, setShowAnimation] = useState(false);
  const [currentSign, setCurrentSign] = useState('');
  const [scaleAnim] = useState(new Animated.Value(1));
  const [avatarSeleccionado, setAvatarSeleccionado] = useState('luis'); // Avatar por defecto

  const [failedLetters, setFailedLetters] = useState([]);
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [showAnimationOption, setShowAnimationOption] = useState(false);
  const [wantsToSeeAnimation, setWantsToSeeAnimation] = useState(false);

  useEffect(() => {
    loadSelectedAvatar();
    generateQuestions();
  }, []);

  const loadSelectedAvatar = async () => {
    try {
      const avatar = await AsyncStorage.getItem('selectedAvatar');
      if (avatar) {
        setAvatarSeleccionado(avatar.toLowerCase());
      }
    } catch (error) {
      console.error('Error cargando avatar:', error);
    }
  };

  const generateQuestions = () => {
    const words = lessonData[category] || [];
    // Aleatorizar todas las palabras primero
    const shuffledWords = [...words].sort(() => Math.random() - 0.5);
    // Seleccionar las primeras 8 palabras aleatorias
    const selectedWords = shuffledWords.slice(0, Math.min(8, words.length));
    const generatedQuestions = selectedWords.map((correctAnswer) => {
      // Generar opciones incorrectas
      const wrongOptions = words.filter(w => w !== correctAnswer).slice(0, 3);
      const allOptions = [correctAnswer, ...wrongOptions];
      // Aleatorizar el orden de las opciones
      const shuffledOptions = allOptions.sort(() => Math.random() - 0.5);
      return {
        question: `¿Cuál es la seña para "${correctAnswer.toUpperCase()}"?`,
        correctAnswer,
        options: shuffledOptions
      };
    });
    setQuestions(generatedQuestions);
  };

  const handleAnswer = (answer) => {
    if (selectedAnswer) return;
    setSelectedAnswer(answer);
    const correct = answer === questions[currentQuestion].correctAnswer;
    setIsCorrect(correct);
    setShowResult(true);
    if (correct) {
      setScore(score + 100);
      setCurrentSign(answer);
      Animated.sequence([
        Animated.timing(scaleAnim, {
          toValue: 1.2,
          duration: 200,
          useNativeDriver: true
        }),
        Animated.timing(scaleAnim, {
          toValue: 1,
          duration: 200,
          useNativeDriver: true
        })
      ]).start();
      // Mostrar opción para ver animación
      setShowAnimationOption(true);
    } else {
      // Guardar letra fallida para repaso posterior
      const failedLetter = questions[currentQuestion].correctAnswer;
      if (!failedLetters.includes(failedLetter)) {
        setFailedLetters([...failedLetters, failedLetter]);
      }
      setLives(lives - 1);
      if (lives - 1 === 0) {
        Alert.alert(
          '❌ Game Over',
          'Te quedaste sin vidas. ¡Inténtalo de nuevo!',
          [
            {
              text: 'Reintentar',
              onPress: () => {
                setLives(3);
                setScore(0);
                setCurrentQuestion(0);
                setShowResult(false);
                setSelectedAnswer(null);
                generateQuestions();
              }
            },
            {
              text: 'Salir',
              onPress: () => navigation.goBack()
            }
          ]
        );
      }
    }
  };

  const nextQuestion = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
      setShowResult(false);
      setSelectedAnswer(null);
      setIsCorrect(false);
      setShowAnimation(false);
      setShowAnimationOption(false);
      setWantsToSeeAnimation(false);
    } else {
      // Verificar si hay letras fallidas para repasar
      if (failedLetters.length > 0 && !isReviewMode) {
        Alert.alert(
          '📚 Repaso de letras fallidas',
          `Tuviste errores en ${failedLetters.length} letra(s). ¿Quieres repasarlas?\n\nLetras: ${failedLetters.join(', ').toUpperCase()}`,
          [
            {
              text: 'Repasar',
              onPress: () => startReviewMode()
            },
            {
              text: 'Finalizar',
              onPress: () => showCompletionMessage()
            }
          ]
        );
      } else {
        showCompletionMessage();
      }
    }
  };

  const startReviewMode = () => {
    setIsReviewMode(true);
    const reviewQuestions = failedLetters.map((failedLetter) => {
      const words = lessonData[category] || [];
      const wrongOptions = words.filter(w => w !== failedLetter).slice(0, 3);
      const allOptions = [failedLetter, ...wrongOptions];
      return {
        question: `¿Cuál es la seña para "${failedLetter.toUpperCase()}"?`,
        correctAnswer: failedLetter,
        options: allOptions
      };
    });
    setQuestions(reviewQuestions);
    setCurrentQuestion(0);
    setShowResult(false);
    setSelectedAnswer(null);
    setFailedLetters([]); // Limpiar para esta ronda de repaso
  };

  const showCompletionMessage = () => {
    // Dar recompensa de estrellas
    if (onComplete) {
      onComplete(starReward);
    }
    
    Alert.alert(
      '🎉 ¡Lección Completada!',
      `Puntuación: ${score}\nVidas restantes: ${lives}\n\n⭐ +${starReward} estrellas ganadas!`,
      [
        {
          text: 'Volver al menú',
          onPress: () => navigation.goBack()
        }
      ]
    );
  };

  const handleAnimationChoice = (choice) => {
    if (choice === 'yes') {
      setWantsToSeeAnimation(true);
      setShowAnimation(true);
      setShowAnimationOption(false);
    } else {
      setShowAnimationOption(false);
      // Continuar directamente
      setTimeout(() => nextQuestion(), 500);
    }
  };

  if (questions.length === 0) {
    return (
      <View style={styles.container}>
        <Text>Cargando...</Text>
      </View>
    );
  }

  const question = questions[currentQuestion];

  return (
    <LinearGradient  
      colors={['#ffffff', '#cfe8fa', '#77c1fd', '#34a3fd', '#0056b3', '#04309e']}
      style={styles.container}
      start={{ x: 0.5, y: 0 }}
      end={{ x: 0.5, y: 1 }}
    >
    <SafeAreaView style={styles.safeArea} edges={['bottom']}>
      <StatusBar barStyle="light-content" backgroundColor="#04309e" translucent={true} />

      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity onPress={() => navigation.goBack()}>
          <Ionicons name="close" size={28} color="#080808" />
        </TouchableOpacity>
        
        {/* Progress Bar */}
        <View style={styles.progressContainer}>
          <View 
            style={[
              styles.progressFill, 
              { width: `${((currentQuestion + 1) / questions.length) * 100}%` }
            ]} 
          />
        </View>

        {/* Lives - Guacamayas */}
        <View style={styles.livesContainer}>
          {[...Array(3)].map((_, i) => (
            <Text key={i} style={styles.heart}>
              {i < lives ? '🦜' : '💀'}
            </Text>
          ))}
        </View>
      </View>

      {/* Question */}
      <View style={styles.questionContainer}>
        {isReviewMode && (
          <View style={styles.reviewBanner}>
            <Text style={styles.reviewBannerText}>📚 Modo Repaso - Letras Fallidas</Text>
          </View>
        )}
        <Text style={styles.questionTitle}>
          {question.question}
        </Text>
        <Text style={styles.scoreText}>Puntos: {score}</Text>
      </View>

      {/* Options Grid */}
      <View style={styles.optionsContainer}>
        {question.options.map((option, index) => {
          const isSelected = selectedAnswer === option;
          const isCorrectOption = option === question.correctAnswer;
          
          let backgroundColor = '#fff';
          let borderColor = '#0e0e0e';
          
          if (showResult && isSelected) {
            backgroundColor = isCorrect ? '#4CAF50' : '#F44336';
            borderColor = isCorrect ? '#4CAF50' : '#F44336';
          } else if (showResult && isCorrectOption) {
            backgroundColor = '#4CAF50';
            borderColor = '#4CAF50';
          }

          return (
            <Animated.View
              key={index}
              style={[
                styles.optionCard,
                { 
                  backgroundColor,
                  borderColor,
                  transform: [{ scale: isSelected && isCorrect ? scaleAnim : 1 }]
                }
              ]}
            >
              <TouchableOpacity
                style={styles.optionButton}
                onPress={() => handleAnswer(option)}
                disabled={showResult}
              >
                {category === 'alfabeto' && letterImages[option.toLowerCase()] ? (
                  <Image
                    source={letterImages[option.toLowerCase()]}
                    style={styles.optionImage}
                    resizeMode="contain"
                  />
                ) : (
                  <>
                    <Text style={[
                      styles.optionEmoji,
                      showResult && (isSelected || isCorrectOption) && styles.optionTextWhite
                    ]}>
                      🤟
                    </Text>
                    <Text style={[
                      styles.optionText,
                      showResult && (isSelected || isCorrectOption) && styles.optionTextWhite
                    ]}>
                      {option.toUpperCase()}
                    </Text>
                  </>
                )}
              </TouchableOpacity>
            </Animated.View>
          );
        })}
      </View>

      {/* Result Message */}
      {showResult && (
        <View style={[
          styles.resultContainer,
          { backgroundColor: isCorrect ? '#4CAF50' : '#F44336' }
        ]}>
          <View style={styles.resultContent}>
            <Text style={styles.resultIcon}>
              {isCorrect ? '✅' : '❌'}
            </Text>
            <Text style={styles.resultText}>
              {isCorrect ? '¡Excelente!' : '¡Incorrecto!'}
            </Text>
            {!isCorrect && (
              <Text style={styles.resultSubtext}>
                La respuesta correcta es: {question.correctAnswer.toUpperCase()}
              </Text>
            )}
          </View>
          
          {/* Opción para ver animación cuando acierta */}
          {isCorrect && showAnimationOption && (
            <View style={styles.animationOptionsContainer}>
              <Text style={styles.animationOptionsTitle}>¿Quieres ver la animación?</Text>
              <View style={styles.animationOptionsButtons}>
                <TouchableOpacity 
                  style={[styles.animationOptionButton, styles.animationOptionYes]}
                  onPress={() => handleAnimationChoice('yes')}
                >
                  <Text style={styles.animationOptionButtonText}>Sí 👍</Text>
                </TouchableOpacity>
                <TouchableOpacity 
                  style={[styles.animationOptionButton, styles.animationOptionNo]}
                  onPress={() => handleAnimationChoice('no')}
                >
                  <Text style={styles.animationOptionButtonText}>No ⏭️</Text>
                </TouchableOpacity>
              </View>
            </View>
          )}
          
          {!showAnimationOption && (
            <TouchableOpacity 
              style={styles.continueButton}
              onPress={nextQuestion}
            >
              <Text style={styles.continueButtonText}>
                Continuar
              </Text>
            </TouchableOpacity>
          )}
        </View>
      )}

      {/* 3D Animation Modal */}
      <Modal
        visible={showAnimation}
        animationType="slide"
        onRequestClose={() => setShowAnimation(false)}
      >
        <SafeAreaView style={styles.modalContainer}>
          <View style={styles.modalHeader}>
            <Text style={styles.modalTitle}>
              🤟 Seña: {currentSign.toUpperCase()}
            </Text>
            <TouchableOpacity onPress={() => {
              setShowAnimation(false);
              nextQuestion();
            }}>
              <Ionicons name="close" size={28} color="#000000" />
            </TouchableOpacity>
          </View>
          
          <WebView
            source={{ 
              uri: `http://192.168.10.93:8000/lesson_simple.html?letra=${encodeURIComponent(currentSign.toLowerCase())}&avatar=${avatarSeleccionado || 'luis'}&autoplay=true&v=${Date.now()}`
            }}
            originWhitelist={['*']}
            javaScriptEnabled={true}
            domStorageEnabled={true}
            allowsInlineMediaPlayback={true}
            mediaPlaybackRequiresUserAction={false}
            style={styles.webview}
            startInLoadingState={true}
            renderLoading={() => (
              <View style={styles.loadingWebview}>
                <Text style={styles.loadingText}>Cargando avatar...</Text>
              </View>
            )}
            onError={(syntheticEvent) => {
              const { nativeEvent } = syntheticEvent;
              console.warn('WebView error: ', nativeEvent);
            }}
            onMessage={(event) => {
              console.log('WebView message:', event.nativeEvent.data);
            }}
            useWebKit={true}
            sharedCookiesEnabled={true}
            thirdPartyCookiesEnabled={true}
          />
          
          <TouchableOpacity 
            style={styles.closeModalButton}
            onPress={() => {
              setShowAnimation(false);
              nextQuestion();
            }}
          >
            <Text style={styles.closeModalButtonText}>Continuar</Text>
          </TouchableOpacity>
        </SafeAreaView>
      </Modal>
    </SafeAreaView>
    </LinearGradient>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  header: {
    height: 100,
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingTop: StatusBar.currentHeight || 30,
    paddingBottom: 10,
  },
  progressContainer: {
    flex: 1,
    height: 10,
    backgroundColor: 'rgba(0, 0, 0, 0.08)',
    borderRadius: 5,
    marginHorizontal: 15,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    backgroundColor: '#000000',
    borderRadius: 5,
  },
  livesContainer: {
    flexDirection: 'row',
  },
  heart: {
    fontSize: 20,
    marginLeft: 5,
  },
  questionContainer: {
    padding: 20,
    alignItems: 'center',
  },
  reviewBanner: {
    backgroundColor: '#FFA500',
    paddingVertical: 8,
    paddingHorizontal: 15,
    borderRadius: 20,
    marginBottom: 15,
  },
  reviewBannerText: {
    color: '#000000',
    fontWeight: 'bold',
    fontSize: 14,
  },
  questionTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    textAlign: 'center',
    marginBottom: 10,
  },
  scoreText: {
    fontSize: 16,
    color: '#667eea',
    fontWeight: 'bold',
  },
  optionsContainer: {
    flex: 1,
    flexDirection: 'row',
    flexWrap: 'wrap',
    padding: 10,
    justifyContent: 'center',
    alignItems: 'center',
  },
  optionCard: {
    width: (width - 60) / 2,
    height: 140,
    margin: 10,
    borderRadius: 15,
    borderWidth: 4,
    borderColor: '#00247D', // Azul Venezuela
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.25,
    shadowRadius: 5,
    elevation: 5,
    backgroundColor: '#fff',
  },
  optionButton: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 15,
  },
  optionImage: {
    width: 110,
    height: 110,
    marginBottom: 5,
  },
  optionText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    textAlign: 'center',
    marginBottom: 10,
  },
  optionTextWhite: {
    color: '#000000',
  },
  optionEmoji: {
    fontSize: 40,
  },
  resultContainer: {
    padding: 20,
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
  },
  resultContent: {
    alignItems: 'center',
    marginBottom: 20,
  },
  resultIcon: {
    fontSize: 60,
    marginBottom: 10,
  },
  resultText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#000000',
    marginBottom: 5,
  },
  resultSubtext: {
    fontSize: 16,
    color: '#000000',
    textAlign: 'center',
  },
  continueButton: {
    backgroundColor: '#fff',
    paddingVertical: 15,
    paddingHorizontal: 40,
    borderRadius: 25,
    alignSelf: 'center',
  },
  continueButtonText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#667eea',
  },
  modalContainer: {
    flex: 1,
    backgroundColor: '#fff',
  },
  modalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#000000',
  },
  modalTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#000000',
  },
  webview: {
    flex: 1,
  },
  loadingWebview: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    fontSize: 16,
    color: '#667eea',
    marginTop: 10,
  },
  closeModalButton: {
    backgroundColor: '#667eea',
    margin: 20,
    padding: 15,
    borderRadius: 25,
    alignItems: 'center',
  },
  closeModalButtonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  animationOptionsContainer: {
    marginTop: 15,
    marginBottom: 10,
    alignItems: 'center',
  },
  animationOptionsTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#030303',
    marginBottom: 15,
  },
  animationOptionsButtons: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: 15,
  },
  animationOptionButton: {
    paddingVertical: 12,
    paddingHorizontal: 30,
    borderRadius: 25,
    minWidth: 120,
    alignItems: 'center',
  },
  animationOptionYes: {
    backgroundColor: '#fff',
  },
  animationOptionNo: {
    backgroundColor: 'rgba(255,255,255,0.3)',
    borderWidth: 2,
    borderColor: '#fff',
  },
  animationOptionButtonText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#667eea',
  },
});

export default LessonScreen;
