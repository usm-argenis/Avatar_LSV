import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  StatusBar,
  Alert,
  ScrollView,
  Modal
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { WebView } from 'react-native-webview';
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
  const [showAnimation, setShowAnimation] = useState(false);
  const [avatarSeleccionado, setAvatarSeleccionado] = useState('luis');

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
                  generateQuestions();
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
    if (onComplete) {
      onComplete(starReward);
    }
    
    Alert.alert(
      '🎉 ¡Juego Completado!',
      `Puntuación: ${score}\nVidas restantes: ${lives}\n\n⭐ +${starReward} estrellas ganadas!`,
      [
        {
          text: 'Volver al menú',
          onPress: () => navigation.goBack()
        }
      ]
    );
  };

  const getAnimationUrl = (number) => {
    return `http://192.168.10.93:8000/lesson_simple.html?letra=${encodeURIComponent(number.toString())}&avatar=${avatarSeleccionado}&autoplay=true&v=${Date.now()}`;
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
                  borderWidth
                }
              ]}
              onPress={() => handleAnswer(option)}
              disabled={showResult}
              activeOpacity={0.7}
            >
              <View style={styles.signContainer}>
                <WebView
                  source={{ uri: getAnimationUrl(option) }}
                  style={styles.miniWebview}
                  javaScriptEnabled={true}
                  domStorageEnabled={true}
                  pointerEvents="none"
                />
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
    aspectRatio: 1,
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
    backgroundColor: '#000',
  },
  miniWebview: {
    flex: 1,
    backgroundColor: 'transparent',
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
