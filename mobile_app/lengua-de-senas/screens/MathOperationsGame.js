import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  StatusBar,
  Alert,
  ScrollView,
  Modal,
  Image
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import AsyncStorage from '@react-native-async-storage/async-storage';

const MathOperationsGame = ({ route, navigation }) => {
  const { starReward = 150, onComplete } = route.params;
  
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [lives, setLives] = useState(3);
  const [showResult, setShowResult] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [timer, setTimer] = useState(180); // Empezar en 180 segundos (3 minutos)
  const [timerInterval, setTimerInterval] = useState(null);

  // Mapeo de imágenes base
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

  const getNumberImages = (number) => {
    const num = parseInt(number);
    console.log(`🔢 getNumberImages llamado para: ${num}`);
    
    // 0-5: Usar imágenes _D y el 0
    if (num === 0) {
      console.log('  ✅ Retornando imagen de 0');
      return [[numberImages['0']]];
    }
    if (num >= 1 && num <= 5) {
      console.log(`  ✅ Retornando imagen ${num}_D`);
      return [[numberImages[`${num}_D`]]];
    }
    
    // 6-10: Combinaciones con 5_I (como un solo grupo)
    if (num === 6) {
      console.log('  ✅ Retornando 6: [1_D, 5_I]');
      return [[numberImages['1_D'], numberImages['5_I']]];
    }
    if (num === 7) {
      console.log('  ✅ Retornando 7: [2_D, 5_I]');
      return [[numberImages['2_D'], numberImages['5_I']]];
    }
    if (num === 8) {
      console.log('  ✅ Retornando 8: [3_D, 5_I]');
      return [[numberImages['3_D'], numberImages['5_I']]];
    }
    if (num === 9) {
      console.log('  ✅ Retornando 9: [4_D, 5_I]');
      return [[numberImages['4_D'], numberImages['5_I']]];
    }
    if (num === 10) {
      console.log('  ✅ Retornando 10: [5_D, 5_I]');
      return [[numberImages['5_D'], numberImages['5_I']]];
    }
    
    // 11-15: Grupo del 10 + grupo de la unidad
    if (num >= 11 && num <= 15) {
      const unidad = num - 10;
      console.log(`  ✅ Retornando ${num}: [[5_D, 5_I], [${unidad}_D]]`);
      return [
        [numberImages['5_D'], numberImages['5_I']], // Grupo 10
        [numberImages[`${unidad}_D`]] // Grupo unidad
      ];
    }
    
    // 16-19: Grupo del 10 + grupo del 5 + unidad
    if (num >= 16 && num <= 19) {
      const unidad = num - 15;
      console.log(`  ✅ Retornando ${num}: [[5_D, 5_I], [1_D, ${unidad}_I]]`);
      return [
        [numberImages['5_D'], numberImages['5_I']], // Grupo 10
        [numberImages['1_D'], numberImages[`${unidad}_I`]] // Grupo 5+unidad
      ];
    }
    
    // 20+: Separar dígitos (23 = 2_D + 3_D)
    if (num >= 20) {
      const digits = number.toString().split('');
      const groups = [];
      console.log(`  📊 Procesando dígitos de ${num}: ${digits.join(', ')}`);
      digits.forEach(digit => {
        const d = parseInt(digit);
        if (d === 0) {
          groups.push([numberImages['0']]);
          console.log(`    - Dígito ${d}: agregando imagen 0`);
        } else if (d >= 1 && d <= 5) {
          groups.push([numberImages[`${d}_D`]]);
          console.log(`    - Dígito ${d}: agregando imagen ${d}_D`);
        } else if (d >= 6 && d <= 9) {
          // Para 6-9, agregar la combinación como un grupo
          const base = d - 5;
          groups.push([numberImages[`${base}_D`], numberImages['5_I']]);
          console.log(`    - Dígito ${d}: agregando imágenes ${base}_D + 5_I`);
        }
      });
      console.log(`  ✅ Retornando ${groups.length} grupos para número ${num}`);
      // Asegurar que siempre retorne algo válido
      return groups.length > 0 ? groups : [[numberImages['0']]];
    }
    
    // Por defecto, retornar 0
    console.log('  ⚠️ Caso por defecto - retornando imagen 0');
    return [[numberImages['0']]];
  };

  useEffect(() => {
    generateQuestions();
    startTimer();
    return () => {
      if (timerInterval) clearInterval(timerInterval);
    };
  }, []);

  useEffect(() => {
    // Verificar si se acabó el tiempo
    if (timer <= 0) {
      gameOver();
    }
  }, [timer]);

  const startTimer = () => {
    const interval = setInterval(() => {
      setTimer(prev => prev - 1); // Decrementar en vez de incrementar
    }, 1000);
    setTimerInterval(interval);
  };

  const stopTimer = () => {
    if (timerInterval) {
      clearInterval(timerInterval);
      setTimerInterval(null);
    }
  };

  const gameOver = () => {
    stopTimer();
    Alert.alert(
      '⏱️ Tiempo Agotado',
      '¡Se acabó el tiempo! Perdiste automáticamente.',
      [
        {
          text: 'Reintentar',
          onPress: () => {
            setLives(3);
            setScore(0);
            setCurrentQuestion(0);
            setShowResult(false);
            setSelectedAnswer(null);
            setTimer(180);
            generateQuestions();
            startTimer();
          }
        },
        {
          text: 'Salir',
          onPress: () => navigation.goBack()
        }
      ]
    );
  };

  const generateQuestions = () => {
    const operations = ['+', '-', '×'];
    const generatedQuestions = [];

    for (let i = 0; i < 10; i++) {
      const operation = operations[Math.floor(Math.random() * operations.length)];
      let num1, num2, correctAnswer;

      if (operation === '+') {
        num1 = Math.floor(Math.random() * 10);
        num2 = Math.floor(Math.random() * 10);
        correctAnswer = num1 + num2;
      } else if (operation === '-') {
        num1 = Math.floor(Math.random() * 10) + 5;
        num2 = Math.floor(Math.random() * num1);
        correctAnswer = num1 - num2;
      } else { // multiplicación
        num1 = Math.floor(Math.random() * 5) + 1;
        num2 = Math.floor(Math.random() * 5) + 1;
        correctAnswer = num1 * num2;
      }

      // Generar opciones incorrectas
      const wrongOptions = [];
      while (wrongOptions.length < 3) {
        const wrongAnswer = correctAnswer + Math.floor(Math.random() * 10) - 5;
        if (wrongAnswer !== correctAnswer && wrongAnswer >= 0 && !wrongOptions.includes(wrongAnswer)) {
          wrongOptions.push(wrongAnswer);
        }
      }

      const allOptions = [correctAnswer, ...wrongOptions];
      const shuffledOptions = allOptions.sort(() => Math.random() - 0.5);

      generatedQuestions.push({
        num1,
        num2,
        operation,
        correctAnswer,
        options: shuffledOptions,
        question: `${num1} ${operation} ${num2} = ?`
      });
    }

    setQuestions(generatedQuestions);
  };

  const handleAnswer = (answer) => {
    if (selectedAnswer !== null) return;
    
    setSelectedAnswer(answer);
    const correct = answer === questions[currentQuestion].correctAnswer;
    setIsCorrect(correct);
    setShowResult(true);

    if (correct) {
      setScore(score + 150);
    } else {
      setLives(lives - 1);
      if (lives - 1 === 0) {
        setTimeout(() => {
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
                  setTimer(180);
                  generateQuestions();
                  startTimer();
                }
              },
              {
                text: 'Salir',
                onPress: () => navigation.goBack()
              }
            ]
          );
        }, 500);
      }
    }
  };

  const nextQuestion = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
      setShowResult(false);
      setSelectedAnswer(null);
      setIsCorrect(false);
    } else {
      showCompletionMessage();
    }
  };

  const showCompletionMessage = () => {
    stopTimer();
    
    const tiempoUsado = 180 - timer; // Calcular tiempo usado (lo que falta del temporizador)
    let finalStars = 0;
    let timeMessage = '';
    
    if (tiempoUsado <= 60) {
      finalStars = 150;
      timeMessage = '¡Increíble! Terminaste en menos de 1 minuto';
    } else if (tiempoUsado <= 120) {
      finalStars = 100;
      timeMessage = '¡Buen trabajo! Terminaste entre 1-2 minutos';
    } else if (tiempoUsado <= 180) {
      finalStars = 50;
      timeMessage = 'Terminaste entre 2-3 minutos';
    }
    
    if (onComplete) {
      onComplete(finalStars);
    }
    
    const minutos = Math.floor(tiempoUsado / 60);
    const segundos = tiempoUsado % 60;
    
    Alert.alert(
      '🎉 ¡Juego Completado!',
      `${timeMessage}\nTiempo usado: ${minutos}:${segundos.toString().padStart(2, '0')}\nPuntuación: ${score}\nVidas restantes: ${lives}\n\n⭐ +${finalStars} estrellas ganadas!`,
      [
        {
          text: 'Volver al menú',
          onPress: () => navigation.goBack()
        }
      ]
    );
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
    <SafeAreaView style={styles.container} edges={['top', 'bottom']}>
      <StatusBar barStyle="light-content" backgroundColor="#f093fb" />

      {/* Header */}
      <LinearGradient
        colors={['#f093fb', '#f5576c']}
        style={styles.header}
        start={{ x: 0, y: 0 }}
        end={{ x: 1, y: 1 }}
      >
        <TouchableOpacity onPress={() => navigation.goBack()}>
          <Ionicons name="close" size={28} color="#fff" />
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

        {/* Lives */}
        <View style={styles.livesContainer}>
          {[...Array(3)].map((_, i) => (
            <Text key={i} style={styles.heart}>
              {i < lives ? '🦜' : '💀'}
            </Text>
          ))}
        </View>
      </LinearGradient>

      {/* Question */}
      <View style={styles.questionContainer}>
        <View style={styles.timerContainer}>
          <Ionicons name="time-outline" size={20} color={timer <= 60 ? '#F44336' : timer <= 120 ? '#FF9800' : '#4CAF50'} />
          <Text style={[
            styles.timerText,
            { color: timer <= 60 ? '#F44336' : timer <= 120 ? '#FF9800' : '#4CAF50' }
          ]}>
            {Math.floor(timer / 60)}:{(timer % 60).toString().padStart(2, '0')}
          </Text>
        </View>
        <Text style={styles.questionTitle}>Resuelve la operación:</Text>
        <Text style={styles.operationText}>{question.question}</Text>
        <Text style={styles.scoreText}>Puntos: {score}</Text>
      </View>

      {/* Options Grid - Números en señas */}
      <ScrollView 
        style={styles.scrollView}
        contentContainerStyle={styles.optionsContainer}
      >
        {question.options.map((option, index) => {
          const isSelected = selectedAnswer === option;
          const isCorrectOption = option === question.correctAnswer;
          const imageGroups = getNumberImages(option);
          const numGroups = imageGroups.length;
          
          // Calcular aspectRatio dinámico basado en grupos
          // 1 grupo = ratio 1:1, 2 grupos = ratio 1:1.3, 3+ grupos = ratio 1:1.5
          let aspectRatio = 1;
          if (numGroups === 2) {
            aspectRatio = 0.77; // Más alto (1:1.3)
          } else if (numGroups >= 3) {
            aspectRatio = 0.67; // Aún más alto (1:1.5)
          }
          
          let backgroundColor = '#fff';
          let borderColor = '#ddd';
          let borderWidth = 2;
          
          if (showResult && isSelected) {
            backgroundColor = isCorrect ? '#4CAF50' : '#F44336';
            borderColor = isCorrect ? '#4CAF50' : '#F44336';
            borderWidth = 4;
          } else if (showResult && isCorrectOption) {
            backgroundColor = '#4CAF50';
            borderColor = '#4CAF50';
            borderWidth = 4;
          }

          return (
            <TouchableOpacity
              key={index}
              style={[
                styles.optionCard,
                { 
                  backgroundColor, 
                  borderColor,
                  borderWidth,
                  aspectRatio // Aplicar ratio dinámico
                }
              ]}
              onPress={() => handleAnswer(option)}
              disabled={showResult}
              activeOpacity={0.7}
            >
              <View style={[
                styles.signContainer,
                imageGroups.length === 1 && imageGroups[0].length === 1 && styles.signContainerSingle,
                imageGroups.length === 1 && imageGroups[0].length === 2 && styles.signContainerPair
              ]}>
                {imageGroups.map((group, groupIdx) => (
                  <View key={groupIdx} style={[
                    styles.groupContainer,
                    imageGroups.length === 1 && imageGroups[0].length === 1 && styles.groupContainerSingle,
                    imageGroups.length === 1 && imageGroups[0].length === 2 && styles.groupContainerPair,
                    numGroups > 1 && { marginVertical: 2 } // Más espacio entre grupos
                  ]}>
                    {group.map((img, imgIdx) => (
                      <Image
                        key={`${groupIdx}-${imgIdx}`}
                        source={img}
                        style={[
                          styles.numberImage,
                          imageGroups.length === 1 && imageGroups[0].length === 1 && styles.numberImageSingle,
                          group.length === 2 && styles.numberImagePair
                        ]}
                        resizeMode="contain"
                      />
                    ))}
                  </View>
                ))}
              </View>
              <Text style={[
                styles.optionNumber,
                { color: showResult && (isSelected || isCorrectOption) ? '#fff' : '#333' }
              ]}>
                {option}
              </Text>
            </TouchableOpacity>
          );
        })}
      </ScrollView>

      {/* Next Button */}
      {showResult && (
        <View style={styles.resultContainer}>
          <Text style={[styles.resultText, { color: isCorrect ? '#4CAF50' : '#F44336' }]}>
            {isCorrect ? '✅ ¡Correcto!' : `❌ Incorrecto. La respuesta era ${question.correctAnswer}`}
          </Text>
          <TouchableOpacity style={styles.nextButton} onPress={nextQuestion}>
            <LinearGradient
              colors={['#667eea', '#764ba2']}
              style={styles.nextButtonGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 1 }}
            >
              <Text style={styles.nextButtonText}>
                {currentQuestion < questions.length - 1 ? 'Siguiente' : 'Finalizar'}
              </Text>
            </LinearGradient>
          </TouchableOpacity>
        </View>
      )}
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff5f7',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
    paddingVertical: 15,
    elevation: 8,
  },
  progressContainer: {
    flex: 1,
    height: 8,
    backgroundColor: 'rgba(255,255,255,0.3)',
    borderRadius: 4,
    marginHorizontal: 15,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    backgroundColor: '#fff',
    borderRadius: 4,
  },
  livesContainer: {
    flexDirection: 'row',
    gap: 5,
  },
  heart: {
    fontSize: 20,
  },
  questionContainer: {
    padding: 25,
    alignItems: 'center',
    backgroundColor: '#fff',
    borderBottomWidth: 1,
    borderBottomColor: '#f0f0f0',
  },
  timerContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    marginBottom: 10,
    paddingHorizontal: 15,
    paddingVertical: 8,
    backgroundColor: '#f5f5f5',
    borderRadius: 20,
  },
  timerText: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  questionTitle: {
    fontSize: 18,
    color: '#666',
    marginBottom: 10,
  },
  operationText: {
    fontSize: 48,
    fontWeight: 'bold',
    color: '#000000',
    marginBottom: 10,
  },
  scoreText: {
    fontSize: 16,
    color: '#667eea',
    fontWeight: '600',
  },
  scrollView: {
    flex: 1,
  },
  optionsContainer: {
    padding: 20,
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  optionCard: {
    width: '48%',
    // aspectRatio eliminado - ahora es dinámico en el componente
    marginBottom: 15,
    borderRadius: 16,
    overflow: 'hidden',
    elevation: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
  },
  signContainer: {
    flex: 1,
    backgroundColor: '#fff',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 5,
    flexDirection: 'column',
  },
  signContainerSingle: {
    padding: 15,
  },
  signContainerPair: {
    padding: 10,
  },
  groupContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    width: '100%',
    height: 'auto',
    flex: 1, // Cambiado: permitir que cada grupo tome espacio flexible
    marginVertical: 1,
  },
  groupContainerSingle: {
    maxHeight: '100%',
    height: '100%',
  },
  groupContainerPair: {
    maxHeight: '100%',
    height: '80%',
  },
  numberImage: {
    width: '100%',
    height: '100%',
    flex: 1,
  },
  numberImageSingle: {
    width: '100%',
    height: '100%',
  },
  numberImagePair: {
    width: '48%',
    flex: 0,
    margin: 1,
  },
  optionNumber: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    paddingVertical: 12,
    backgroundColor: 'rgba(255,255,255,0.9)',
  },
  resultContainer: {
    padding: 20,
    backgroundColor: '#fff',
    borderTopWidth: 1,
    borderTopColor: '#f0f0f0',
  },
  resultText: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 15,
  },
  nextButton: {
    borderRadius: 12,
    overflow: 'hidden',
    elevation: 4,
  },
  nextButtonGradient: {
    paddingVertical: 16,
    alignItems: 'center',
  },
  nextButtonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
});

export default MathOperationsGame;
