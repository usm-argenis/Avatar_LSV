import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  StatusBar,
  ScrollView,
  Image
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
const badgeImages = {
   'salto': require('../assets/images/salto.jpeg'),
   'avila': require('../assets/images/avila.jpeg'),
   'roques': require('../assets/images/los roques.png'),
   'turpial': require('../assets/images/turpial.png'),
   'medanos': require('../assets/images/medanos.png'),
   'pico': require('../assets/images/pico.png'),
   'roraima': require('../assets/images/roraima.png'),
   'catatumbo': require('../assets/images/catatumbo.png'),
};
const AlphabetModeSelector = ({ route, navigation }) => {
  console.log('🎨 AlphabetModeSelector RENDERIZADO');
  console.log('📦 Params recibidos:', route.params);
  
  const { moduleId, category, title } = route.params;

  const modes = [
    {
      id: 'lesson',
      title: 'Modo Clásico',
      description: 'Aprende viendo señas y respondiendo preguntas',
      icon: 'school',
      color: ['#667eea', '#764ba2'],
      screen: 'Lesson',
      reward: 100
    },
    {
      id: 'falling',
      title: 'Lluvia de Señas',
      description: 'Atrapa las letras que caen para formar palabras',
      icon: 'game-controller',
      color: ['#f093fb', '#f5576c'],
      screen: 'FallingSignsGame',
      reward: 150
    },
    {
      id: 'avatar-to-text',
      title: 'Avatar a Texto',
      description: 'Mira el avatar y escribe lo que deletrea',
      icon: 'create',
      color: ['#4facfe', '#00f2fe'],
      screen: 'AvatarToTextGame',
      reward: 150
    },
    {
      id: 'math-operations',
      title: 'Operaciones Matemáticas',
      description: 'Resuelve operaciones y responde en señas',
      icon: 'calculator',
      color: ['#f093fb', '#f5576c'],
      screen: 'MathOperations',
      reward: 150
    }
  ];

  // Filtrar modos según la categoría
  const availableModes = category === 'numeros' 
    ? modes.filter(mode => mode.id === 'lesson' || mode.id === 'math-operations') // Modo clásico + Calculadora para números
    : modes.filter(mode => mode.id !== 'math-operations'); // Todos menos calculadora para alfabeto

  const selectMode = (mode) => {
    navigation.navigate(mode.screen, {
      moduleId,
      category,
      title,
      onComplete: route.params.onComplete // Pasar el callback de onComplete
    });
  };

  const goToIntroduction = () => {
    if (category === 'alfabeto') {
      navigation.navigate('AlphabetIntroduction');
    } else if (category === 'numeros') {
      navigation.navigate('NumbersIntroduction');
    }
  };

  const goToMathOperations = () => {
    if (category === 'numeros') {
      navigation.navigate('MathOperations', {
        moduleId,
        category,
        title,
        onComplete: route.params.onComplete
      });
    }
  };

  return (
    <SafeAreaView style={styles.container} edges={['bottom']}>
          <StatusBar barStyle="light-content" backgroundColor="#04309e" translucent={true} />
          
          {/* HEADER CON GRADIENT Y LOGOS A LA DERECHA */}
          <LinearGradient
            colors={['#04309e', '#0056b3', '#34a3fd', '#77c1fd', '#cfe8fa', '#ffffff']}
            style={styles.header}
            start={{ x: 0.5, y: 0 }}
            end={{ x: 0.5, y: 1 }}
          >
            {/* Botón Exit (izquierda) */}
            <TouchableOpacity 
              onPress={() => navigation.goBack()} 
              style={styles.exitButton}
            >
              <Ionicons name="arrow-back-outline" size={40} color="#000000" />
            </TouchableOpacity>
    
            <View style={styles.headerContent}>
              {/* Logos del lado derecho */}
              <View style={styles.rightLogos}>
                {/* Guacamaya */}
                <View style={styles.imageContainer}>
                  <Image 
                    source={require('../assets/images/guacamaya.png')}
                    style={styles.guacamayaImage}
                    resizeMode="contain"
                  />
                </View>
    
                {/* Logo VeneSeñas (centro) */}
                <View style={styles.brandImageContainer}>
                  <Image 
                    source={require('../assets/images/venesenas-logo.png')}
                    style={styles.brandImage}
                    resizeMode="contain"
                  />
                </View>
    
                {/* Seña/Mano */}
                <View style={styles.imageContainer}>
                  <Image 
                    source={require('../assets/images/sena-hand.png')}
                    style={styles.senaImage}
                    resizeMode="contain"
                  />
                </View>
              </View>
            </View>
          </LinearGradient>
      {/* Module Info */}
      <View style={styles.moduleInfo}>
        <Text style={styles.moduleIcon}>🔤</Text>
        <Text style={styles.moduleTitle}>{title}</Text>
        <Text style={styles.moduleSubtitle}>
          Elige cómo quieres aprender
        </Text>
      </View>

      {/* Modes */}
      <ScrollView 
        style={styles.scrollView}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {/* Botón de Introducción */}
        <TouchableOpacity
          style={styles.introButton}
          onPress={goToIntroduction}
          activeOpacity={0.8}
        >
          <LinearGradient
            colors={['#30cfd0', '#330867']}
            style={styles.introButtonGradient}
            start={{ x: 0, y: 0 }}
            end={{ x: 1, y: 1 }}
          >
            <View style={styles.introIconContainer}>
              <Ionicons name="book" size={32} color="#fff" />
            </View>
            <View style={styles.introContent}>
              <Text style={styles.introTitle}>
                {category === 'alfabeto' ? '📖 Ver Alfabeto Completo' : '🔢 Ver Números Completos'}
              </Text>
              <Text style={styles.introDescription}>
                Explora todas las {category === 'alfabeto' ? 'letras' : 'números'} antes de empezar
              </Text>
            </View>
            <Ionicons name="eye" size={28} color="#fff" />
          </LinearGradient>
        </TouchableOpacity>

        {/* Separador */}
        <View style={styles.separator}>
          <View style={styles.separatorLine} />
          <Text style={styles.separatorText}>Modos de Juego</Text>
          <View style={styles.separatorLine} />
        </View>
        {availableModes.map((mode, index) => (
          <TouchableOpacity
            key={mode.id}
            style={styles.modeCard}
            onPress={() => selectMode(mode)}
            activeOpacity={0.8}
          >
            <LinearGradient
              colors={mode.color}
              style={styles.modeGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 1 }}
            >
              <View style={styles.modeIconContainer}>
                <Ionicons name={mode.icon} size={40} color="#fff" />
              </View>
              
              <View style={styles.modeContent}>
                <Text style={styles.modeTitle}>{mode.title}</Text>
                <Text style={styles.modeDescription}>{mode.description}</Text>
                <View style={styles.rewardBadge}>
                  <Text style={styles.rewardStar}>⭐</Text>
                  <Text style={styles.rewardText}>+{mode.reward} al completar</Text>
                </View>
              </View>

              <Ionicons name="chevron-forward" size={28} color="#fff" />
            </LinearGradient>

            {/* Badge para nuevo/recomendado */}
            {index === 0 && (
              <View style={styles.recommendedBadge}>
                <Text style={styles.badgeText}>⭐ Recomendado</Text>
              </View>
            )}
          </TouchableOpacity>
        ))}

        {/* Info Box */}
        <View style={styles.infoBox}>
          <Ionicons name="information-circle" size={24} color="#667eea" />
          <Text style={styles.infoText}>
            Cada modo ofrece una forma diferente de practicar. ¡Prueba todos para mejorar tu aprendizaje!
          </Text>
        </View>

        {/* Stats Preview */}
        

        <View style={{ height: 30 }} />
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F8F9FA',
  },
  
  headerTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
  },
  moduleInfo: {
    backgroundColor: '#fff',
    alignItems: 'center',
    paddingVertical: 25,
    borderBottomWidth: 1,
    borderBottomColor: '#E0E0E0',
  },
  moduleIcon: {
    fontSize: 50,
    marginBottom: 10,
  },
  moduleTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 5,
  },
  moduleSubtitle: {
    fontSize: 14,
    color: '#666',
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    padding: 20,
  },
  modeCard: {
    marginBottom: 20,
    borderRadius: 20,
    overflow: 'hidden',
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
  },
  modeGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 20,
  },
  modeIconContainer: {
    width: 70,
    height: 70,
    borderRadius: 35,
    backgroundColor: 'rgba(255,255,255,0.2)',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 15,
  },
  modeContent: {
    flex: 1,
  },
  modeTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 5,
  },
  modeDescription: {
    fontSize: 14,
    color: '#fff',
    opacity: 0.9,
  },
  rewardBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 8,
    backgroundColor: '#FFCD00', // Amarillo Venezuela
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 15,
    alignSelf: 'flex-start',
    borderWidth: 2,
    borderColor: '#CF142B', // Rojo Venezuela
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 3,
    elevation: 3,
  },
  rewardStar: {
    fontSize: 15,
    marginRight: 4,
  },
  rewardText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#093ec5ff', // Azul Venezuela
  },
  recommendedBadge: {
    position: 'absolute',
    top: 10,
    right: 10,
    backgroundColor: '#FFD700',
    paddingHorizontal: 12,
    paddingVertical: 5,
    borderRadius: 15,
  },
  badgeText: {
    fontSize: 12,
    fontWeight: 'bold',
    color: '#333',
  },
  infoBox: {
    flexDirection: 'row',
    backgroundColor: '#E3F2FD',
    padding: 15,
    borderRadius: 15,
    marginTop: 10,
    marginBottom: 20,
  },
  infoText: {
    flex: 1,
    marginLeft: 10,
    fontSize: 14,
    color: '#1976D2',
    lineHeight: 20,
  },
  statsContainer: {
    backgroundColor: '#fff',
    borderRadius: 15,
    padding: 20,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  statsTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 15,
    textAlign: 'center',
  },
  statsRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
  },
  statItem: {
    alignItems: 'center',
  },
  statValue: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#667eea',
  },
  statLabel: {
    fontSize: 12,
    color: '#666',
    marginTop: 5,
  },
  introButton: {
    marginBottom: 15,
    borderRadius: 20,
    overflow: 'hidden',
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
  },
  mathButton: {
    marginBottom: 15,
    borderRadius: 20,
    overflow: 'hidden',
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
  },
  introButtonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 20,
  },
  introIconContainer: {
    width: 60,
    height: 60,
    borderRadius: 30,
    backgroundColor: 'rgba(255,255,255,0.2)',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 15,
  },
  introContent: {
    flex: 1,
  },
  introTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 5,
  },
  introDescription: {
    fontSize: 13,
    color: '#fff',
    opacity: 0.9,
  },
  separator: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: 20,
  },
  separatorLine: {
    flex: 1,
    height: 2,
    backgroundColor: '#E0E0E0',
  },
  separatorText: {
    marginHorizontal: 15,
    fontSize: 14,
    fontWeight: '600',
    color: '#666',
  },header: {
    height: 100,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 15,
    paddingTop: StatusBar.currentHeight || 30,
    paddingBottom: 10,
  },
  exitButton: {
    width: 50,
    height: 50,
    alignItems: 'center',
    justifyContent: 'center',
  },
  headerContent: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'flex-end',
  },
  rightLogos: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  imageContainer: {
    width: 30,
    height: 50,
  },
  brandImageContainer: {
    width: 110,
    height: 45,
  },
  guacamayaImage: {
    width: '100%',
    height: '100%',
  },
  brandImage: {
    width: '100%',
    height: '100%',
  },
  senaImage: {
    width: '100%',
    height: '100%',
  },

  scrollView: { 
    flex: 1,
    backgroundColor: '#F7F7F7',
  },
  
  newPathContainer: { 
    paddingHorizontal: 20,
    paddingTop: 20,
  },
});

export default AlphabetModeSelector;
