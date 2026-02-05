import React, { useState, useEffect, useMemo, useCallback, useRef } from 'react';
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

// Mapeo de imágenes de números
const numberImages = {
  '0': require('../assets/numeros/0.png'),
  '1_D': require('../assets/numeros/1_D.png'),
  '2_D': require('../assets/numeros/2_D.png'),
  '3_D': require('../assets/numeros/3_D.png'),
  '4_D': require('../assets/numeros/4_D.png'),
  '5_D': require('../assets/numeros/5_D.png'),
  '1_I': require('../assets/numeros/1_I.png'),
  '2_I': require('../assets/numeros/2_I.png'),
  '3_I': require('../assets/numeros/3_I.png'),
  '4_I': require('../assets/numeros/4_I.png'),
  '5_I': require('../assets/numeros/5_I.png'),
};

// Función para obtener las imágenes correspondientes a un número
const getNumberImages = (number) => {
  const num = parseInt(number);
  
  // 0-5: Usar imágenes _D y el 0
  if (num === 0) return [[numberImages['0']]];
  if (num >= 1 && num <= 5) return [[numberImages[`${num}_D`]]];
  
  // 6-10: Combinaciones con 5_I (como un solo grupo)
  if (num === 6) return [[numberImages['1_D'], numberImages['5_I']]];
  if (num === 7) return [[numberImages['2_D'], numberImages['5_I']]];
  if (num === 8) return [[numberImages['3_D'], numberImages['5_I']]];
  if (num === 9) return [[numberImages['4_D'], numberImages['5_I']]];
  if (num === 10) return [[numberImages['5_D'], numberImages['5_I']]];
  
  // 11-15: Grupo del 10 + grupo de la unidad
  if (num >= 11 && num <= 15) {
    const unidad = num - 10;
    return [
      [numberImages['5_D'], numberImages['5_I']], // Grupo 10
      [numberImages[`${unidad}_D`]] // Grupo unidad
    ];
  }
  
  // 16-19: Grupo del 10 + grupo del 5 + unidad
  if (num >= 16 && num <= 19) {
    const unidad = num - 15;
    return [
      [numberImages['5_D'], numberImages['5_I']], // Grupo 10
      [numberImages['1_D'], numberImages[`${unidad}_I`]] // Grupo 5+unidad
    ];
  }
  
  // 20+: Separar dígitos (23 = 2_D + 3_D)
  if (num >= 20) {
    const digits = number.toString().split('');
    const groups = [];
    digits.forEach(digit => {
      const d = parseInt(digit);
      if (d === 0) {
        groups.push([numberImages['0']]);
      } else if (d >= 1 && d <= 5) {
        groups.push([numberImages[`${d}_D`]]);
      } else if (d >= 6 && d <= 9) {
        // Para 6-9, agregar la combinación como un grupo
        const base = d - 5;
        groups.push([numberImages[`${base}_D`], numberImages['5_I']]);
      }
    });
    // Asegurar que siempre retorne algo válido
    return groups.length > 0 ? groups : [[numberImages['0']]];
  }
  
  // Por defecto, retornar 0
  return [[numberImages['0']]];
};

// Función para convertir número a secuencia de animación para el HTML
const getNumberAnimationSequence = (number) => {
  const num = parseInt(number);
  console.log(`🔢 Generando secuencia de animación para número: ${num}`);
  
  // 0-10: Usar directamente el número
  if (num >= 0 && num <= 10) {
    console.log(`  → Número simple: ${num}`);
    return [num.toString()];
  }
  
  // 11-19: Primero 10, luego el segundo dígito
  if (num >= 11 && num <= 19) {
    const segundoDigito = num - 10;
    console.log(`  → 11-19: [10, ${segundoDigito}]`);
    return ['10', segundoDigito.toString()];
  }
  
  // 20+: Separar dígitos (24 = 2, luego 4; 40 = 4, luego 0)
  if (num >= 20) {
    const digits = number.toString().split('');
    console.log(`  → 20+: [${digits.join(', ')}]`);
    return digits;
  }
  
  return [num.toString()];
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
  const webViewRef = useRef(null); // Ref para controlar WebView
  const [animationSequenceIndex, setAnimationSequenceIndex] = useState(0);
  const [isPlayingSequence, setIsPlayingSequence] = useState(false);
  const [webViewReady, setWebViewReady] = useState(false); // Estado para saber si WebView está listo
  const hasInitialized = useRef(false); // Evitar múltiples ejecuciones de onLoadEnd

  const [failedLetters, setFailedLetters] = useState([]);
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [showAnimationOption, setShowAnimationOption] = useState(false);
  const [wantsToSeeAnimation, setWantsToSeeAnimation] = useState(false);

  useEffect(() => {
    loadSelectedAvatar();
    generateQuestions();
  }, []);

  // Resetear hasInitialized cuando cambia la pregunta/seña
  useEffect(() => {
    hasInitialized.current = false;
    setWebViewReady(false);
    console.log('🔄 Nueva seña, reseteando hasInitialized y webViewReady');
  }, [currentSign]);

  // Controlar secuencia de animación de números
  useEffect(() => {
    if (!isPlayingSequence || !webViewRef.current || !webViewReady) {
      if (!webViewReady) {
        console.log('⏳ useEffect: WebView no está listo aún, esperando...');
      }
      return;
    }

    const sign = currentSign.toLowerCase();
    const isNumber = /^\d+$/.test(sign);
    
    if (isNumber && category === 'numeros') {
      const sequence = getNumberAnimationSequence(sign);
      
      if (animationSequenceIndex < sequence.length) {
        const currentNum = sequence[animationSequenceIndex];
        console.log(`🎬 Reproduciendo número ${currentNum} (${animationSequenceIndex + 1}/${sequence.length})`);
        
        // Usar siempre carga silenciosa (el avatar ya está cargado)
        if (webViewRef.current) {
          console.log(`📤 Inyectando JavaScript para número: ${currentNum}`);
          const script = `
            console.log('🟢 JS INYECTADO: Ejecutando para número ${currentNum}');
            (async function() {
              try {
                if (typeof window.cargarSiguienteAnimacionSilenciosa === 'function') {
                  console.log('✅ Función cargarSiguienteAnimacionSilenciosa existe, llamando...');
                  await window.cargarSiguienteAnimacionSilenciosa('${currentNum}');
                } else {
                  console.error('❌ Función cargarSiguienteAnimacionSilenciosa NO EXISTE');
                  console.log('window keys:', Object.keys(window).filter(k => k.includes('cargar')));
                }
              } catch (error) {
                console.error('❌ Error en JS inyectado:', error.message);
              }
            })();
            true;
          `;
          webViewRef.current.injectJavaScript(script);
          console.log(`✅ JavaScript inyectado exitosamente`);
        }
        
        // Duración: 2s animación (flujo continuo sin pausa adicional)
        const animationDuration = 2000;
        
        // Después de la animación, pasar al siguiente número directamente
        const timer = setTimeout(() => {
          if (webViewRef.current) {
            setAnimationSequenceIndex(prev => prev + 1);
          }
        }, animationDuration);
        
        return () => clearTimeout(timer);
      } else {
        // Secuencia completada, reiniciar para loop
        console.log('✅ Secuencia completada, reiniciando...');
        const timer = setTimeout(() => {
          if (webViewRef.current) {
            setAnimationSequenceIndex(0);
          }
        }, 2000); // Pausa de 2s antes de reiniciar
        
        return () => clearTimeout(timer);
      }
    }
  }, [isPlayingSequence, animationSequenceIndex, currentSign, category, webViewReady]);

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
      setIsPlayingSequence(false);
      setAnimationSequenceIndex(0);
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

          // Calcular altura dinámica para números según cantidad TOTAL de imágenes
          let cardHeight = 170; // Default
          if (category === 'numeros') {
            const imageGroups = getNumberImages(option);
            const totalImages = imageGroups.reduce((sum, g) => sum + g.length, 0);
            
            if (totalImages === 1) {
              cardHeight = 150; // Una imagen
            } else if (totalImages === 2) {
              cardHeight = 190; // Dos imágenes
            } else if (totalImages === 3) {
              cardHeight = 200; // Tres imágenes
            } else {
              cardHeight = 220; // Cuatro o más imágenes
            }
          }

          return (
            <Animated.View
              key={index}
              style={[
                styles.optionCard,
                { 
                  backgroundColor,
                  borderColor,
                  height: cardHeight, // Altura dinámica
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
                ) : category === 'numeros' ? (
                  (() => {
                    const imageGroups = getNumberImages(option);
                    const totalImages = imageGroups.reduce((sum, g) => sum + g.length, 0);
                    
                    // Aplanar todas las imágenes en un solo array
                    const allImages = imageGroups.flat();
                    
                    if (totalImages === 1) {
                      // 1 imagen: ocupa todo el espacio
                      return (
                        <View style={styles.numberSignContainer}>
                          <Image
                            source={allImages[0]}
                            style={styles.numberImageFull}
                            resizeMode="contain"
                          />
                        </View>
                      );
                    } else if (totalImages === 2) {
                      // 2 imágenes: mitad y mitad horizontalmente
                      return (
                        <View style={styles.numberSignContainer}>
                          <View style={styles.numberRowContainer}>
                            <Image
                              source={allImages[0]}
                              style={styles.numberImageHalf}
                              resizeMode="contain"
                            />
                            <Image
                              source={allImages[1]}
                              style={styles.numberImageHalf}
                              resizeMode="contain"
                            />
                          </View>
                        </View>
                      );
                    } else if (totalImages === 3) {
                      // 3 imágenes: 2 arriba (25% cada una), 1 abajo (50%)
                      return (
                        <View style={styles.numberSignContainer}>
                          <View style={styles.numberRowContainer}>
                            <Image
                              source={allImages[0]}
                              style={styles.numberImageQuarter}
                              resizeMode="contain"
                            />
                            <Image
                              source={allImages[1]}
                              style={styles.numberImageQuarter}
                              resizeMode="contain"
                            />
                          </View>
                          <View style={styles.numberRowContainer}>
                            <Image
                              source={allImages[2]}
                              style={styles.numberImageHalf}
                              resizeMode="contain"
                            />
                          </View>
                        </View>
                      );
                    } else {
                      // 4+ imágenes: cuadrantes de 25% cada uno
                      return (
                        <View style={styles.numberSignContainer}>
                          <View style={styles.numberRowContainer}>
                            <Image
                              source={allImages[0]}
                              style={styles.numberImageQuarter}
                              resizeMode="contain"
                            />
                            <Image
                              source={allImages[1]}
                              style={styles.numberImageQuarter}
                              resizeMode="contain"
                            />
                          </View>
                          <View style={styles.numberRowContainer}>
                            <Image
                              source={allImages[2]}
                              style={styles.numberImageQuarter}
                              resizeMode="contain"
                            />
                            {allImages[3] && (
                              <Image
                                source={allImages[3]}
                                style={styles.numberImageQuarter}
                                resizeMode="contain"
                              />
                            )}
                          </View>
                        </View>
                      );
                    }
                  })()
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
        transparent={false}
        onRequestClose={() => setShowAnimation(false)}
      >
        <View style={styles.modalContainer}>
          <StatusBar barStyle="light-content" backgroundColor="#1a1a20" translucent={true} />

          {/* Header del Modal */}
          <View style={styles.modalHeader}>
            <Text style={styles.modalTitle}>🤟 Seña: {currentSign.toUpperCase()}</Text>
            <TouchableOpacity onPress={() => {
              setShowAnimation(false);
              setIsPlayingSequence(false);
              setAnimationSequenceIndex(0);
              nextQuestion();
            }}>
              <Ionicons name="close" size={40} color="#fff" />
            </TouchableOpacity>
          </View>
          
          <WebView
            ref={webViewRef}
            source={{ 
              uri: (() => {
                const sign = currentSign.toLowerCase();
                const isNumber = /^\d+$/.test(sign);
                
                if (isNumber && category === 'numeros') {
                  // Para números, cargar la primera animación de la secuencia
                  const sequence = getNumberAnimationSequence(sign);
                  const firstNum = sequence[0];
                  console.log(`🎬 Iniciando secuencia de número ${sign}: [${sequence.join(', ')}]`);
                  return `http://192.168.10.93:8000/lesson_simple.html?letra=${encodeURIComponent(firstNum)}&categoria=numero&avatar=${avatarSeleccionado || 'luis'}&autoplay=true`;
                } else {
                  // Para letras y otras categorías, usar el comportamiento normal
                  return `http://192.168.10.93:8000/lesson_simple.html?letra=${encodeURIComponent(sign)}&categoria=${encodeURIComponent(category)}&avatar=${avatarSeleccionado || 'luis'}&autoplay=true`;
                }
              })()
            }}
            originWhitelist={['*']}
            javaScriptEnabled={true}
            domStorageEnabled={true}
            allowsInlineMediaPlayback={true}
            mediaPlaybackRequiresUserAction={false}
            style={styles.webview}
            onLoadEnd={() => {
              // Cuando el WebView carga, iniciar secuencia si es número (solo una vez)
              if (hasInitialized.current) {
                console.log('⚠️ onLoadEnd: Ya inicializado, ignorando');
                return;
              }
              
              console.log('✅ onLoadEnd: WebView cargado, marcando como listo');
              
              // Marcar WebView como listo después de un pequeño delay
              setTimeout(() => {
                setWebViewReady(true);
                
                const sign = currentSign.toLowerCase();
                const isNumber = /^\d+$/.test(sign);
                if (isNumber && category === 'numeros') {
                  console.log('✅ onLoadEnd: Primera vez, iniciando secuencia');
                  hasInitialized.current = true;
                  setAnimationSequenceIndex(0);
                  setIsPlayingSequence(true);
                }
              }, 500); // Esperar 500ms para asegurar que el DOM está listo
            }}
            onError={(syntheticEvent) => {
              const { nativeEvent } = syntheticEvent;
              console.warn('WebView error: ', nativeEvent);
            }}
            useWebKit={true}
            sharedCookiesEnabled={true}
            thirdPartyCookiesEnabled={true}
            cacheEnabled={true}
            cacheMode="LOAD_CACHE_ELSE_NETWORK"
            androidLayerType="hardware"
            androidHardwareAccelerationDisabled={false}
            scalesPageToFit={true}
            nestedScrollEnabled={false}
          />
          
          <TouchableOpacity 
            style={styles.closeModalButton}
            onPress={() => {
              setShowAnimation(false);
              setIsPlayingSequence(false);
              setAnimationSequenceIndex(0);
              nextQuestion();
            }}
          >
            <Text style={styles.closeModalButtonText}>Continuar</Text>
          </TouchableOpacity>
        </View>
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
    // height ahora es dinámica - se asigna en el componente según contenido
    margin: 10,
    borderRadius: 15,
    borderWidth: 4,
    borderColor: '#00247D', // Azul Venezuela
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.25,
    shadowRadius: 5,
    elevation: 5,
    backgroundColor: '#000000',
  },
  optionButton: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 5, // Reducido de 10 a 5 para más espacio para imágenes
  },
  optionImage: {
    width: 120, // Aumentado de 110 a 120
    height: 120,
    marginBottom: 5,
  },
  numberSignContainer: {
    flex: 1,
    width: '100%',
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  numberRowContainer: {
    flexDirection: 'row',
    flex: 1,
    width: '100%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  numberImageFull: {
    width: '90%',
    height: '90%',
  },
  numberImageHalf: {
    width: '45%',
    height: '90%',
    margin: 2,
  },
  numberImageQuarter: {
    width: '45%',
    height: '100%',
    margin: 2,
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
    backgroundColor: '#ffffff00',
    paddingVertical: 15,
    paddingHorizontal: 40,
    borderRadius: 25,
    alignSelf: 'center',
    },
  continueButtonText: {
    fontSize: 18,
    fontWeight: 'bold',
    background: 'linear-gradient(135deg, #2196F3 0%, #53a5f8 100%)',
  boxShadow: '0 4px 15px rgba(33, 150, 243, 0.4)', // camelCase aquí tambié
  
  },
  modalContainer: {
    flex: 1,
    backgroundColor: '#1a1a2e',
  },
  modalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 15,
    paddingTop: 45,
    backgroundColor: '#1a1a2e',
  },
  modalTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
  },
  webview: {
    flex: 0.99,
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
    backgroundColor: 'rgba(102, 126, 234, 0.9)',
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
