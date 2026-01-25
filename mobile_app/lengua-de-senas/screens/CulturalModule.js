import React, { useState, useRef, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  StatusBar,
  Dimensions,
  Alert,
  Animated
} from 'react-native';
import { WebView } from 'react-native-webview';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import AsyncStorage from '@react-native-async-storage/async-storage';

const { width, height } = Dimensions.get('window');

const CulturalModule = ({ navigation, route }) => {
  const { moduleData, title, onComplete } = route.params;
  const [currentSection, setCurrentSection] = useState(0);
  const [quizAnswers, setQuizAnswers] = useState({});
  const [missionCompleted, setMissionCompleted] = useState(false);
  const [selectedOption, setSelectedOption] = useState(null);
  const [score, setScore] = useState(0);
  const [starsEarned, setStarsEarned] = useState(0); // Total de estrellas ganadas
  const [fadeAnim] = useState(new Animated.Value(0));
  const [selectedAvatar, setSelectedAvatar] = useState('Carla'); // Avatar por defecto
  const [answeredQuestions, setAnsweredQuestions] = useState({}); // Preguntas ya respondidas (desactivadas)
  const [missionAnswered, setMissionAnswered] = useState(false); // Si ya contestó la misión
  const webViewRef = useRef(null);

  // Datos de las secciones del módulo
  const sections = moduleData.sections || [];

  // Cargar avatar seleccionado desde AsyncStorage
  useEffect(() => {
    loadSelectedAvatar();
  }, []);

  const loadSelectedAvatar = async () => {
    try {
      const avatar = await AsyncStorage.getItem('selectedAvatar');
      if (avatar) {
        setSelectedAvatar(avatar);
        console.log(`Avatar cargado para módulo cultural: ${avatar}`);
      }
    } catch (error) {
      console.error('Error cargando avatar:', error);
    }
  };

  React.useEffect(() => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 500,
      useNativeDriver: true,
    }).start();
  }, [currentSection]);
  
  // Ejecutar acción en la escena 3D cuando se selecciona una opción
  useEffect(() => {
    if (selectedOption && webViewRef.current) {
      const script = `
        console.log('React Native enviando comando: ${selectedOption.id}');
        if (window.ejecutarAccion) {
          window.ejecutarAccion('${selectedOption.id}');
        } else {
          console.error('window.ejecutarAccion no está definida');
        }
        true;
      `;
      console.log('Ejecutando JavaScript en WebView:', selectedOption.id);
      webViewRef.current.injectJavaScript(script);
    }
  }, [selectedOption]);

  // Renderizar sección narrativa (historia)
  const renderNarrativeSection = (section) => {
    return (
      <ScrollView style={styles.sectionContent}>
        <View style={styles.narrativeHeader}>
          <Text style={styles.sectionTitle}>{section.title}</Text>
          <Text style={styles.narrativeSubtitle}>Historia de la Lengua de Señas Venezolana</Text>
        </View>

        {section.datos.map((dato, index) => (
          <View key={index} style={styles.historicalCard}>
            <View style={styles.historicalYear}>
              <Text style={styles.yearText}>{dato.year}</Text>
            </View>
            <View style={styles.historicalContent}>
              <Text style={styles.historicalIcon}>{dato.icon}</Text>
              <Text style={styles.historicalText}>{dato.text}</Text>
            </View>
          </View>
        ))}

        <View style={styles.contextBox}>
          <Text style={styles.contextIcon}>💡</Text>
          <Text style={styles.contextText}>
            La LSV es una lengua viva y única que representa la identidad y cultura de la comunidad Sorda venezolana.
          </Text>
        </View>

        <TouchableOpacity 
          style={styles.continueButton} 
          onPress={() => goToNextSection()}
        >
          <Text style={styles.continueButtonText}>Continuar</Text>
          <Ionicons name="arrow-forward" size={24} color="#fff" />
        </TouchableOpacity>
      </ScrollView>
    );
  };

  // Renderizar minijuego de trivia
  const renderTriviaSection = (section) => {
    const questions = section.questions || [];
    const answeredQuestions = Object.keys(quizAnswers).length;

    return (
      <ScrollView style={styles.sectionContent}>
        <View style={styles.triviaHeader}>
          <Text style={styles.sectionTitle}>{section.title}</Text>
          <Text style={styles.triviaSubtitle}>
            Desliza las tarjetas: Verdadero ➡️ | ❌ ⬅️ Falso
          </Text>
          <View style={styles.progressContainer}>
            <Text style={styles.progressText}>
              {answeredQuestions} / {questions.length}
            </Text>
          </View>
        </View>

        {questions.map((question, index) => {
          const isAnswered = quizAnswers[index] !== undefined;
          const wasCorrect = quizAnswers[index] === question.answer;

          return (
            <View key={index} style={styles.questionCard}>
              <View style={styles.questionHeader}>
                <Text style={styles.questionNumber}>Pregunta {index + 1}</Text>
                {isAnswered && (
                  <Text style={styles.resultIcon}>
                    {wasCorrect ? '✅' : '❌'}
                  </Text>
                )}
              </View>

              <Text style={styles.statementText}>{question.statement}</Text>

              {!isAnswered ? (
                <View style={styles.answerButtons}>
                  <TouchableOpacity
                    style={[styles.answerButton, styles.truthButton]}
                    onPress={() => handleAnswer(index, true, question)}
                    disabled={answeredQuestions[index]} // Desactivar si ya se respondió
                  >
                    <Text style={styles.answerButtonText}>✅VERDADERO</Text>
                  </TouchableOpacity>

                  <TouchableOpacity
                    style={[styles.answerButton, styles.mythButton]}
                    onPress={() => handleAnswer(index, false, question)}
                    disabled={answeredQuestions[index]} // Desactivar si ya se respondió
                  >
                    <Text style={styles.answerButtonText}>❌ FALSO</Text>
                  </TouchableOpacity>
                </View>
              ) : (
                <View style={[
                  styles.feedbackBox,
                  wasCorrect ? styles.correctFeedback : styles.incorrectFeedback
                ]}>
                  <Text style={styles.feedbackTitle}>
                    {wasCorrect ? '¡Correcto! 🎉' : 'Incorrecto 😔'}
                  </Text>
                  <Text style={styles.feedbackText}>{question.explanation}</Text>
                </View>
              )}
            </View>
          );
        })}

        {answeredQuestions === questions.length && (
          <TouchableOpacity 
            style={styles.continueButton} 
            onPress={() => goToNextSection()}
          >
            <Text style={styles.continueButtonText}>Siguiente Misión</Text>
            <Ionicons name="arrow-forward" size={24} color="#fff" />
          </TouchableOpacity>
        )}
      </ScrollView>
    );
  };

  // Renderizar misión especial de interacción 3D
  const renderMissionSection = (section) => {
    const options = section.options || [];

    const handleOptionSelect = (option) => {
      setSelectedOption(option);
      setMissionAnswered(true); // Marcar misión como respondida (desactivar todas las opciones)
      
      if (option.correct) {
        // Dar 20 estrellas por opción correcta (B o C)
        setStarsEarned(prev => prev + 20);
        setScore(prevScore => prevScore + 20);
        console.log('⭐ +20 estrellas por opción correcta en misión');
        
        setTimeout(() => {
          Alert.alert(
            option.feedback,
            option.lesson,
            [
              {
                text: 'Entendido',
                onPress: () => {
                  // Si ya seleccionó todas las opciones correctas
                  if (!missionCompleted) {
                    setMissionCompleted(true);
                  }
                }
              }
            ]
          );
        }, 300);
      } else {
        Alert.alert(
          option.feedback,
          option.lesson + '\n\nNo se otorgan estrellas por esta opción.',
          [{ text: 'Entendido' }]
        );
      }
    };

    return (
      <ScrollView style={styles.sectionContent}>
        <View style={styles.missionHeader}>
          <Text style={styles.sectionTitle}>{section.title}</Text>
          <Text style={styles.missionSubtitle}>Interacción con Avatar 3D</Text>
        </View>

        <View style={styles.scenarioBox}>
          <Text style={styles.scenarioIcon}>🚶‍♀️</Text>
          <Text style={styles.scenarioTitle}>Escenario</Text>
          <Text style={styles.scenarioText}>{section.scenario}</Text>
          <Text style={styles.scenarioQuestion}>
            ¿Cómo llamarías la atención del avatar?
          </Text>
        </View>

        <View style={styles.avatarContainer}>
          <WebView
            ref={webViewRef}
            source={{ uri: `http://192.168.10.93:8000/escena_simple.html?avatar=${selectedAvatar}` }}
            style={styles.webViewAvatar}
            javaScriptEnabled={true}
            domStorageEnabled={true}
            startInLoadingState={true}
            onMessage={(event) => {
              console.log('Mensaje desde WebView:', event.nativeEvent.data);
            }}
            onLoad={() => {
              console.log(`WebView cargado correctamente con avatar: ${selectedAvatar}`);
            }}
            onError={(syntheticEvent) => {
              const { nativeEvent } = syntheticEvent;
              console.error('Error en WebView:', nativeEvent);
            }}
          />
        </View>

        <Text style={styles.optionsTitle}>Selecciona una opción:</Text>

        {options.map((option, index) => (
          <TouchableOpacity
            key={option.id}
            style={[
              styles.optionCard,
              selectedOption?.id === option.id && (
                option.correct ? styles.optionCorrect : styles.optionIncorrect
              )
            ]}
            onPress={() => handleOptionSelect(option)}
            disabled={missionAnswered} // Desactivar todas las opciones después de responder
          >
            <View style={styles.optionHeader}>
              <View style={styles.optionBadge}>
                <Text style={styles.optionBadgeText}>Opción {option.id}</Text>
              </View>
              {selectedOption?.id === option.id && (
                <Text style={styles.optionResultIcon}>
                  {option.correct ? '✅' : '❌'}
                </Text>
              )}
            </View>
            <Text style={styles.optionText}>{option.action}</Text>
          </TouchableOpacity>
        ))}

        {missionCompleted && (
          <TouchableOpacity 
            style={styles.continueButton} 
            onPress={() => goToNextSection()}
          >
            <Text style={styles.continueButtonText}>Ver Resumen Final</Text>
            <Ionicons name="arrow-forward" size={24} color="#fff" />
          </TouchableOpacity>
        )}
      </ScrollView>
    );
  };

  // Renderizar resumen final
  const renderSummarySection = (section) => {
    const normas = section.normas || [];
    // Usar starsEarned en lugar de cálculo incorrecto
    const totalScore = starsEarned;

    return (
      <ScrollView style={styles.sectionContent}>
        <View style={styles.summaryHeader}>
          <Text style={styles.congratsIcon}>🎊</Text>
          <Text style={styles.congratsTitle}>¡Felicitaciones!</Text>
          <Text style={styles.congratsSubtitle}>
            Has completado el Módulo de Cultura Sorda
          </Text>
        </View>

        <View style={styles.scoreCard}>
          <Text style={styles.scoreTitle}>Tu Puntuación</Text>
          <Text style={styles.scoreValue}>⭐ {totalScore} puntos</Text>
        </View>

        <View style={styles.cardIdentity}>
          <Text style={styles.cardTitle}>{section.title}</Text>
          <Text style={styles.cardSubtitle}>Normas del Aliado de la Comunidad Sorda</Text>

          {normas.map((norma, index) => (
            <View key={index} style={styles.normaItem}>
              <Text style={styles.normaIcon}>{norma.icon}</Text>
              <View style={styles.normaContent}>
                <Text style={styles.normaTitle}>{norma.title}</Text>
                <Text style={styles.normaText}>{norma.text}</Text>
              </View>
            </View>
          ))}
        </View>

        <View style={styles.quoteBox}>
          <Text style={styles.quoteIcon}>💬</Text>
          <Text style={styles.quoteText}>{section.quote}</Text>
        </View>

        <TouchableOpacity 
          style={styles.finishButton} 
          onPress={() => finishModule(totalScore)}
        >
          <Text style={styles.finishButtonText}>Finalizar Módulo</Text>
          <Ionicons name="checkmark-circle" size={28} color="#fff" />
        </TouchableOpacity>
      </ScrollView>
    );
  };

  // Manejar respuestas de trivia
  const handleAnswer = (questionIndex, userAnswer, question) => {
    const isCorrect = userAnswer === question.answer;
    setQuizAnswers(prev => ({
      ...prev,
      [questionIndex]: userAnswer
    }));

    // Marcar pregunta como respondida (desactivada)
    setAnsweredQuestions(prev => ({
      ...prev,
      [questionIndex]: true
    }));

    if (isCorrect) {
      // Dar 5 estrellas por respuesta correcta
      setStarsEarned(prev => prev + 5);
      setScore(prevScore => prevScore + 5);
      console.log('⭐ +5 estrellas por respuesta correcta');
    }
  };

  // Ir a la siguiente sección
  const goToNextSection = () => {
    if (currentSection < sections.length - 1) {
      setCurrentSection(currentSection + 1);
      setSelectedOption(null); // Resetear la opción seleccionada
      fadeAnim.setValue(0);
      Animated.timing(fadeAnim, {
        toValue: 1,
        duration: 500,
        useNativeDriver: true,
      }).start();
    }
  };

  // Finalizar módulo
  const finishModule = (finalScore) => {
    // Usar starsEarned directamente (no calcular desde finalScore)
    const stars = starsEarned;
    
    Alert.alert(
      '🏆 ¡Módulo Completado!',
      `Has ganado ${stars} estrellas ⭐\n\nAhora entiendes mejor la cultura Sorda y cómo interactuar respetuosamente.`,
      [
        {
          text: 'Continuar',
          onPress: () => {
            if (onComplete) {
              onComplete(stars); // Pasar estrellas ganadas a la experiencia
            }
            navigation.goBack();
          }
        }
      ]
    );
  };

  // Renderizar sección actual
  const renderCurrentSection = () => {
    if (sections.length === 0) {
      return (
        <View style={styles.emptyState}>
          <Text style={styles.emptyText}>No hay secciones disponibles</Text>
        </View>
      );
    }

    const section = sections[currentSection];

    switch (section.type) {
      case 'narrativa':
        return renderNarrativeSection(section);
      case 'minijuego':
        return renderTriviaSection(section);
      case 'mision':
        return renderMissionSection(section);
      case 'resumen':
        return renderSummarySection(section);
      default:
        return null;
    }
  };

  return (
    <SafeAreaView style={styles.container} edges={['top', 'bottom']}>
      <StatusBar barStyle="light-content" backgroundColor="#8B4789" />

      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity onPress={() => navigation.goBack()} style={styles.backButton}>
          <Ionicons name="arrow-back" size={24} color="#fff" />
        </TouchableOpacity>

        <View style={styles.headerTitleContainer}>
          <Text style={styles.headerTitle}>{title}</Text>
          <Text style={styles.headerSubtitle}>
            Sección {currentSection + 1} de {sections.length}
          </Text>
        </View>

        <View style={styles.scoreContainer}>
          <Text style={styles.scoreIcon}>⭐</Text>
          <Text style={styles.scoreText}>{starsEarned}</Text>
        </View>
      </View>

      {/* Progress Bar */}
      <View style={styles.progressBar}>
        <View 
          style={[
            styles.progressBarFill, 
            { width: `${((currentSection + 1) / sections.length) * 100}%` }
          ]} 
        />
      </View>

      {/* Contenido principal */}
      <Animated.View style={[styles.content, { opacity: fadeAnim }]}>
        {renderCurrentSection()}
      </Animated.View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F3FF',
  },
  header: {
    backgroundColor: '#8B4789',
    paddingHorizontal: 16,
    paddingVertical: 14,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    elevation: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
  },
  backButton: {
    padding: 5,
  },
  headerTitleContainer: {
    flex: 1,
    marginLeft: 12,
  },
  headerTitle: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '700',
  },
  headerSubtitle: {
    color: 'rgba(255, 255, 255, 0.8)',
    fontSize: 13,
    marginTop: 2,
  },
  scoreContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 20,
  },
  scoreIcon: {
    fontSize: 18,
    marginRight: 4,
  },
  scoreText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '700',
  },
  progressBar: {
    height: 6,
    backgroundColor: '#E0E0E0',
  },
  progressBarFill: {
    height: '100%',
    backgroundColor: '#FFD700',
  },
  content: {
    flex: 1,
  },
  sectionContent: {
    flex: 1,
    paddingHorizontal: 20,
    paddingTop: 20,
  },

  // Sección Narrativa
  narrativeHeader: {
    alignItems: 'center',
    marginBottom: 30,
    paddingBottom: 20,
    borderBottomWidth: 2,
    borderBottomColor: '#8B4789',
  },
  sectionTitle: {
    fontSize: 28,
    fontWeight: '900',
    color: '#8B4789',
    textAlign: 'center',
    marginBottom: 8,
  },
  narrativeSubtitle: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
  },
  historicalCard: {
    backgroundColor: '#fff',
    borderRadius: 16,
    padding: 20,
    marginBottom: 20,
    elevation: 3,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    borderLeftWidth: 6,
    borderLeftColor: '#8B4789',
  },
  historicalYear: {
    backgroundColor: '#8B4789',
    alignSelf: 'flex-start',
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
    marginBottom: 12,
  },
  yearText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '700',
  },
  historicalContent: {
    flexDirection: 'row',
    alignItems: 'flex-start',
  },
  historicalIcon: {
    fontSize: 28,
    marginRight: 12,
  },
  historicalText: {
    flex: 1,
    fontSize: 16,
    color: '#333',
    lineHeight: 24,
  },
  contextBox: {
    backgroundColor: '#FFF9E6',
    borderRadius: 12,
    padding: 16,
    marginTop: 10,
    marginBottom: 30,
    flexDirection: 'row',
    alignItems: 'flex-start',
    borderWidth: 2,
    borderColor: '#FFD700',
  },
  contextIcon: {
    fontSize: 24,
    marginRight: 12,
  },
  contextText: {
    flex: 1,
    fontSize: 15,
    color: '#555',
    fontStyle: 'italic',
    lineHeight: 22,
  },

  // Sección Trivia
  triviaHeader: {
    alignItems: 'center',
    marginBottom: 25,
  },
  triviaSubtitle: {
    fontSize: 14,
    color: '#666',
    textAlign: 'center',
    marginTop: 8,
  },
  progressContainer: {
    backgroundColor: '#8B4789',
    paddingHorizontal: 20,
    paddingVertical: 8,
    borderRadius: 20,
    marginTop: 12,
  },
  progressText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '700',
  },
  questionCard: {
    backgroundColor: '#fff',
    borderRadius: 16,
    padding: 20,
    marginBottom: 20,
    elevation: 3,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  questionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  questionNumber: {
    fontSize: 14,
    color: '#8B4789',
    fontWeight: '700',
  },
  resultIcon: {
    fontSize: 24,
  },
  statementText: {
    fontSize: 18,
    color: '#333',
    fontWeight: '600',
    lineHeight: 26,
    marginBottom: 20,
  },
  answerButtons: {
    flexDirection: 'row',
    gap: 12,
  },
  answerButton: {
    flex: 1,
    paddingVertical: 16,
    borderRadius: 12,
    alignItems: 'center',
    elevation: 2,
  },
  truthButton: {
    backgroundColor: '#4CAF50',
  },
  mythButton: {
    backgroundColor: '#FF5252',
  },
  answerButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '700',
  },
  feedbackBox: {
    borderRadius: 12,
    padding: 16,
    marginTop: 10,
  },
  correctFeedback: {
    backgroundColor: '#E8F5E9',
    borderWidth: 2,
    borderColor: '#4CAF50',
  },
  incorrectFeedback: {
    backgroundColor: '#FFEBEE',
    borderWidth: 2,
    borderColor: '#FF5252',
  },
  feedbackTitle: {
    fontSize: 16,
    fontWeight: '700',
    marginBottom: 8,
    color: '#333',
  },
  feedbackText: {
    fontSize: 15,
    color: '#555',
    lineHeight: 22,
  },

  // Sección Misión
  missionHeader: {
    alignItems: 'center',
    marginBottom: 25,
  },
  missionSubtitle: {
    fontSize: 14,
    color: '#666',
    marginTop: 8,
  },
  scenarioBox: {
    backgroundColor: '#fff',
    borderRadius: 16,
    padding: 20,
    marginBottom: 20,
    alignItems: 'center',
    elevation: 3,
    borderWidth: 3,
    borderColor: '#8B4789',
  },
  scenarioIcon: {
    fontSize: 48,
    marginBottom: 12,
  },
  scenarioTitle: {
    fontSize: 20,
    fontWeight: '700',
    color: '#8B4789',
    marginBottom: 8,
  },
  scenarioText: {
    fontSize: 15,
    color: '#666',
    textAlign: 'center',
    marginBottom: 12,
  },
  scenarioQuestion: {
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
    textAlign: 'center',
  },
  avatarContainer: {
    alignItems: 'center',
    marginBottom: 30,
    width: '100%',
  },
  webViewAvatar: {
    width: width - 40,
    height: 250,
    borderRadius: 16,
    overflow: 'hidden',
    backgroundColor: '#fff',
    borderWidth: 3,
    borderColor: '#8B4789',
  },
  avatarPlaceholder: {
    width: 180,
    height: 180,
    backgroundColor: '#E8E0F5',
    borderRadius: 90,
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 4,
    borderColor: '#8B4789',
    elevation: 4,
  },
  avatarIcon: {
    fontSize: 80,
  },
  avatarStatus: {
    fontSize: 16,
    marginTop: 10,
    fontWeight: '600',
    color: '#555',
  },
  optionsTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: '#333',
    marginBottom: 16,
  },
  optionCard: {
    backgroundColor: '#fff',
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
    borderWidth: 2,
    borderColor: '#E0E0E0',
    elevation: 2,
  },
  optionCorrect: {
    borderColor: '#4CAF50',
    backgroundColor: '#E8F5E9',
  },
  optionIncorrect: {
    borderColor: '#FF5252',
    backgroundColor: '#FFEBEE',
  },
  optionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  optionBadge: {
    backgroundColor: '#8B4789',
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 12,
  },
  optionBadgeText: {
    color: '#fff',
    fontSize: 12,
    fontWeight: '700',
  },
  optionResultIcon: {
    fontSize: 24,
  },
  optionText: {
    fontSize: 16,
    color: '#333',
    fontWeight: '500',
  },

  // Sección Resumen
  summaryHeader: {
    alignItems: 'center',
    marginBottom: 30,
  },
  congratsIcon: {
    fontSize: 60,
    marginBottom: 12,
  },
  congratsTitle: {
    fontSize: 32,
    fontWeight: '900',
    color: '#8B4789',
    marginBottom: 8,
  },
  congratsSubtitle: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
  },
  scoreCard: {
    backgroundColor: '#FFD700',
    borderRadius: 16,
    padding: 20,
    alignItems: 'center',
    marginBottom: 25,
    elevation: 4,
    borderWidth: 3,
    borderColor: '#8B4789',
  },
  scoreTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: '#333',
    marginBottom: 8,
  },
  scoreValue: {
    fontSize: 36,
    fontWeight: '900',
    color: '#8B4789',
  },
  cardIdentity: {
    backgroundColor: '#fff',
    borderRadius: 16,
    padding: 20,
    marginBottom: 25,
    elevation: 3,
    borderWidth: 2,
    borderColor: '#8B4789',
  },
  cardTitle: {
    fontSize: 22,
    fontWeight: '800',
    color: '#8B4789',
    textAlign: 'center',
    marginBottom: 6,
  },
  cardSubtitle: {
    fontSize: 14,
    color: '#666',
    textAlign: 'center',
    marginBottom: 20,
  },
  normaItem: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 20,
    paddingBottom: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#E0E0E0',
  },
  normaIcon: {
    fontSize: 32,
    marginRight: 12,
  },
  normaContent: {
    flex: 1,
  },
  normaTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: '#8B4789',
    marginBottom: 4,
  },
  normaText: {
    fontSize: 15,
    color: '#555',
    lineHeight: 22,
  },
  quoteBox: {
    backgroundColor: '#E8F5E9',
    borderRadius: 12,
    padding: 20,
    marginBottom: 30,
    flexDirection: 'row',
    alignItems: 'flex-start',
    borderLeftWidth: 6,
    borderLeftColor: '#4CAF50',
  },
  quoteIcon: {
    fontSize: 28,
    marginRight: 12,
  },
  quoteText: {
    flex: 1,
    fontSize: 16,
    color: '#333',
    fontStyle: 'italic',
    lineHeight: 24,
    fontWeight: '500',
  },

  // Botones
  continueButton: {
    backgroundColor: '#8B4789',
    borderRadius: 12,
    paddingVertical: 16,
    paddingHorizontal: 24,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 20,
    marginBottom: 30,
    elevation: 4,
  },
  continueButtonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '700',
    marginRight: 8,
  },
  finishButton: {
    backgroundColor: '#4CAF50',
    borderRadius: 12,
    paddingVertical: 16,
    paddingHorizontal: 24,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 10,
    marginBottom: 40,
    elevation: 4,
  },
  finishButtonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '700',
    marginRight: 8,
  },

  // Estado vacío
  emptyState: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 40,
  },
  emptyText: {
    fontSize: 18,
    color: '#999',
    textAlign: 'center',
  },
});

export default CulturalModule;
