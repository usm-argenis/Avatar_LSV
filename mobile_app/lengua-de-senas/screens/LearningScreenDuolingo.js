import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  StatusBar,
  Dimensions,
  Alert,
  Modal,
  TouchableWithoutFeedback,
  Image
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { saveStarsToAPI } from '../services/authService';
import { useFocusEffect } from '@react-navigation/native';

const { width } = Dimensions.get('window');

// Mapeo de insignias a imágenes (temporalmente deshabilitado para pruebas)
// Las imágenes se cargarán dinámicamente cuando sea necesario
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

const LearningScreenDuolingo = ({ navigation }) => {
  const [userId, setUserId] = useState(null);
  const [stars, setStars] = useState(0); 
  const [currentLevel, setCurrentLevel] = useState(1);
  const [showBadges, setShowBadges] = useState(false); // Estado para el dropdown
  const [zoomedBadge, setZoomedBadge] = useState(null); // Estado para la insignia con zoom
  const [lastUnlockedBadge, setLastUnlockedBadge] = useState(null); // Última insignia desbloqueada
  const [unlockedBadgesCount, setUnlockedBadgesCount] = useState(0); // Número de insignias desbloqueadas

  // Lista de Insignias Venezolanas y sus requisitos de estrellas
  const insignias = [
    { id: 1, name: 'Salto Ángel', tipo: 'salto', req: 500 },
    { id: 2, name: 'El Ávila', tipo: 'avila', req: 1000 },
    { id: 3, name: 'Los Roques', tipo: 'roques', req: 2000 },
    { id: 4, name: 'Los Médanos de Coro', tipo: 'medanos', req: 2500 },
    { id: 5, name: 'El Turpial', tipo: 'turpial', req: 3000 },
    { id: 6, name: 'Pico Bolívar', tipo: 'pico', req: 4000 },
    { id: 7, name: 'Roraima', tipo: 'roraima', req: 5000 },
    { id: 8, name: 'Relámpago del Catatumbo', tipo: 'catatumbo', req: 6000 },
  ];

  // Cargar datos guardados al montar
  useEffect(() => {
    loadProgress();
  }, []);

  // Recargar progreso cada vez que la pantalla gana foco
  useFocusEffect(
    React.useCallback(() => {
      console.log('🔄 [LearningScreen] Pantalla ganó foco, recargando progreso...');
      loadProgress();
    }, [])
  );

  // Actualizar última insignia desbloqueada cuando cambien las estrellas
  useEffect(() => {
    const unlockedBadges = insignias.filter(badge => stars >= badge.req);
    setUnlockedBadgesCount(unlockedBadges.length);
    if (unlockedBadges.length > 0) {
      const lastBadge = unlockedBadges[unlockedBadges.length - 1];
      setLastUnlockedBadge(lastBadge);
    } else {
      setLastUnlockedBadge(null);
    }
  }, [stars]);

  const loadProgress = async () => {
    try {
      console.log('🔍 [LearningScreen] Iniciando carga de progreso...');
      
      // Cargar userId primero
      const id = await AsyncStorage.getItem('userId');
      console.log('🔑 [LearningScreen] userId obtenido:', id);
      
      if (!id) {
        console.warn('⚠️ [LearningScreen] No hay userId, redirigiendo al login');
        navigation.replace('Login');
        return;
      }
      
      setUserId(id);
      console.log('✅ [LearningScreen] userId establecido:', id);
      
      // Cargar estrellas y nivel específicos de este usuario
      let savedStars = await AsyncStorage.getItem(`stars_${id}`);
      let savedLevel = await AsyncStorage.getItem(`currentLevel_${id}`);
      
      console.log(`🌟 [LearningScreen] Estrellas cargadas de stars_${id}:`, savedStars);
      console.log(`🏆 [LearningScreen] Nivel cargado de currentLevel_${id}:`, savedLevel);
      
      // MIGRACIÓN: Si no existen en el nuevo formato, cargar del formato antiguo
      if (!savedStars) {
        console.log('🔄 [LearningScreen] No hay datos en formato nuevo, buscando en formato antiguo...');
        const oldStars = await AsyncStorage.getItem('userStars');
        const oldLevel = await AsyncStorage.getItem('userLevel');
        
        console.log('📦 [LearningScreen] Datos antiguos encontrados:', { userStars: oldStars, userLevel: oldLevel });
        
        if (oldStars) {
          savedStars = oldStars;
          // Migrar al nuevo formato
          await AsyncStorage.setItem(`stars_${id}`, oldStars);
          console.log(`✅ [LearningScreen] Estrellas migradas a stars_${id}: ${oldStars}`);
        }
        
        if (oldLevel) {
          savedLevel = oldLevel;
          // Migrar al nuevo formato
          await AsyncStorage.setItem(`currentLevel_${id}`, oldLevel);
          console.log(`✅ [LearningScreen] Nivel migrado a currentLevel_${id}: ${oldLevel}`);
        }
      }
      
      if (savedStars) {
        const starsValue = parseInt(savedStars);
        console.log(`⭐ [LearningScreen] Estableciendo estrellas a:`, starsValue);
        setStars(starsValue);
      } else {
        console.log('⚠️ [LearningScreen] No se encontraron estrellas guardadas, manteniendo en 0');
      }
      
      if (savedLevel) {
        const levelValue = parseInt(savedLevel);
        console.log(`📊 [LearningScreen] Estableciendo nivel a:`, levelValue);
        setCurrentLevel(levelValue);
      } else {
        console.log('⚠️ [LearningScreen] No se encontró nivel guardado, manteniendo en 1');
      }
      
      console.log('✅ [LearningScreen] Carga de progreso completada');
    } catch (error) {
      console.error('❌ [LearningScreen] Error cargando progreso:', error);
    }
  };

  const saveProgress = async (forceUserId = null) => {
    try {
      const userIdToUse = forceUserId || userId;
      
      if (!userIdToUse) {
        console.log('⚠️ [LearningScreen] No se puede guardar progreso: userId no disponible');
        return;
      }
      
      console.log(`💾 [LearningScreen] Guardando progreso para usuario ${userIdToUse}:`, { stars, currentLevel });
      
      // 1. Guardar localmente en ambos formatos para compatibilidad
      await AsyncStorage.setItem(`stars_${userIdToUse}`, stars.toString());
      await AsyncStorage.setItem(`currentLevel_${userIdToUse}`, currentLevel.toString());
      await AsyncStorage.setItem('userStars', stars.toString());
      await AsyncStorage.setItem('userLevel', currentLevel.toString());
      
      console.log('✅ [LearningScreen] Progreso guardado localmente en ambos formatos');
      
      // 2. Guardar en el backend (solo las estrellas nuevas)
      // No enviamos el total, el backend ya suma automáticamente
      console.log(`🌐 [LearningScreen] Sincronizando con el backend...`);
      
    } catch (error) {
      console.error('❌ [LearningScreen] Error guardando progreso:', error);
    }
  };

  useEffect(() => {
    if (userId) {
      saveProgress(userId);
    }
    const newLevel = Math.floor(stars / 2000) + 1;
    if (newLevel > currentLevel) {
      setCurrentLevel(newLevel);
    }
  }, [stars, userId]);

  // TUS MÓDULOS (Sin modificaciones)
  const modules = [
    {
      id: 1,
      title: 'Fundamentos Culturales',
      description: 'Cultura Sorda y Mitos',
      icon: '🏛️',
      color: '#8B4789',
      completed: 0,
      total: 15,
      unlocked: true,
      category: 'cultura_mitos',
      cost: 0,
      rewardClassic: 150,
      rewardFalling: 200,
      rewardAvatar: 200,
      subtitle: 'Módulo 1: Aprende sobre la Cultura Sorda',
      sections: [
        {
          type: 'narrativa',
          title: '📖 El Origen',
          content: 'Historia de la LSV',
          datos: [
            { year: 1935, text: 'Se funda el Instituto Venezolano de Ciegos y Sordomudos (IVCyS)', icon: '🏫' },
            { year: 1950, text: 'Se crea la Asociación de Sordomudos de Caracas, liderada por José Arquero Urbano', icon: '👥' },
            { year: 1950, text: 'La LSV nace de la mezcla de señas caseras y señas españolas', icon: '🤝' }
          ]
        },
        {
          type: 'minijuego',
          title: '🎮 Verdadero o Falso',
          gameType: 'trivia',
          questions: [
            { statement: 'El término correcto es Sordomudo.', answer: false, explanation: 'Falso. El término "sordomudo" debe borrarse de nuestra mente.' },
            { statement: 'La Lengua de Señas es universal (igual en todo el mundo).', answer: false, explanation: 'Falso. La LSV tiene su propia gramática.' },
            { statement: 'Debo gritar para que me entiendan mejor.', answer: false, explanation: 'Falso. Se debe hablar con naturalidad.' },
            { statement: 'Las personas Sordas tienen su propia cultura.', answer: true, explanation: 'Verdadero. Existe una Cultura Sorda.' },
            { statement: 'Si uso audífonos, escucho el 100% como un oyente.', answer: false, explanation: 'Falso. Los audífonos son una ayuda.' },
            { statement: 'La LSV tiene variantes dialectales.', answer: true, explanation: 'Verdadero. Al igual que el español, la LSV puede usar diferentes señas.' }
          ]
        },
        {
          type: 'mision',
          title: '🕵️ Llamada de Atención',
          gameType: 'interaccion_3d',
          scenario: 'Avatar de espaldas mirando estantería',
          options: [
            { id: 'A', action: 'Gritarle "¡Oye tú!"', correct: false, feedback: '❌ Fallo.', lesson: 'No hables de espaldas.' },
            { id: 'B', action: 'Tocarle el hombro suavemente', correct: true, feedback: '✅ Éxito.', lesson: 'Es necesario llamar su atención con un toque.' },
            { id: 'C', action: 'Apagar y encender la luz', correct: true, feedback: '✅ Éxito.', lesson: 'Forma válida visual.' },
            { id: 'D', action: 'Golpear el piso o la mesa fuerte', correct: true, feedback: '✅ Éxito.', lesson: 'Las vibraciones se notan.' }
          ]
        },
        {
          type: 'resumen',
          title: '📝 Tarjeta del Aliado',
          normas: [
            { icon: '👁️', title: 'Norma de Oro', text: 'Hablar siempre de frente' },
            { icon: '🗣️', title: 'Claridad', text: 'No exagerar la vocalización' },
            { icon: '👀', title: 'Visual', text: 'La atención es visual' }
          ],
          quote: '"Una persona sorda puede hacer cualquier cosa igual que un oyente, excepto oír"'
        }
      ]
    },
    { id: 2, title: 'Alfabeto LSV', description: 'Aprende las letras A-Z', icon: '🔤', color: '#58CC02', completed: 0, total: 27, unlocked: stars >= 0, category: 'alfabeto', cost: 0, rewardClassic: 100, rewardFalling: 150, rewardAvatar: 150 },
    { id: 3, title: 'Números', description: 'Números del 1 al 10', icon: '🔢', color: '#00B5E2', completed: 0, total: 20, unlocked: stars >= 100, category: 'numeros', cost: 100, rewardClassic: 100, rewardFalling: 150, rewardAvatar: 150 },
    { id: 4, title: 'Saludos', description: 'Hola, adiós, buenos días', icon: '👋', color: '#FF9600', completed: 0, total: 15, unlocked: stars >= 4000, category: 'saludos', cost: 4000, rewardClassic: 100, rewardFalling: 150, rewardAvatar: 150 },
    { id: 5, title: 'Pronombres', description: 'Yo, tú, él, ella', icon: '👤', color: '#CE82FF', completed: 0, total: 12, unlocked: stars >= 6000, category: 'pronombres', cost: 6000, rewardClassic: 100, rewardFalling: 150, rewardAvatar: 150 },
    { id: 6, title: 'Días de la Semana', description: 'Lunes a domingo', icon: '📅', color: '#FF4B4B', completed: 0, total: 10, unlocked: stars >= 8000, category: 'dias_semana', cost: 8000, rewardClassic: 100, rewardFalling: 150, rewardAvatar: 150 },
    { id: 7, title: 'Tiempo', description: 'Hoy, ayer, mañana', icon: '⏰', color: '#1CB0F6', completed: 0, total: 7, unlocked: stars >= 10000, category: 'tiempo', cost: 10000, rewardClassic: 100, rewardFalling: 150, rewardAvatar: 150 },
    { id: 8, title: 'Cortesía', description: 'Gracias, por favor', icon: '🙏', color: '#FFC800', completed: 0, total: 8, unlocked: stars >= 12000, category: 'cortesia', cost: 12000, rewardClassic: 100, rewardFalling: 150, rewardAvatar: 150 },
    { id: 9, title: 'Preguntas', description: '¿Cómo?, ¿Qué?, ¿Cuál?', icon: '❓', color: '#FF66B3', completed: 0, total: 6, unlocked: stars >= 14000, category: 'preguntas', cost: 14000, rewardClassic: 100, rewardFalling: 150, rewardAvatar: 150 }
  ];

  const startLesson = async (module) => {
    if (!module.unlocked) {
      Alert.alert('Módulo Bloqueado', `Necesitas ${module.cost} estrellas.`);
      return;
    }
    
    const handleComplete = async (earnedStars) => {
      console.log(`🌟 [LearningScreen] Lección completada! Estrellas ganadas: ${earnedStars}`);
      
      // Actualizar estrellas localmente
      const newStars = stars + earnedStars;
      setStars(newStars);
      
      // Guardar INMEDIATAMENTE en AsyncStorage
      if (userId) {
        try {
          await AsyncStorage.setItem(`stars_${userId}`, newStars.toString());
          await AsyncStorage.setItem('userStars', newStars.toString());
          console.log(`💾 [LearningScreen] Estrellas guardadas inmediatamente en AsyncStorage: ${newStars}`);
          
          // Guardar en el backend
          console.log(`🌐 [LearningScreen] Enviando ${earnedStars} estrellas al backend...`);
          const result = await saveStarsToAPI(userId, earnedStars, 1);
          if (result.success) {
            console.log('✅ [LearningScreen] Estrellas guardadas en el backend exitosamente');
          } else {
            console.error('❌ [LearningScreen] Error al guardar en backend:', result.mensaje);
          }
        } catch (error) {
          console.error('❌ [LearningScreen] Error al guardar estrellas:', error);
        }
      }
    };
    
    if (module.category === 'cultura_mitos') {
      navigation.navigate('CulturalModule', { moduleId: module.id, moduleData: module, title: module.title, onComplete: handleComplete });
    } else if (module.category === 'alfabeto' || module.category === 'numeros') {
      navigation.navigate('AlphabetModeSelector', { moduleId: module.id, category: module.category, title: module.title, onComplete: handleComplete });
    } else {
      navigation.navigate('Lesson', { moduleId: module.id, category: module.category, title: module.title, starReward: module.rewardClassic, onComplete: handleComplete });
    }
  };

  const renderModule = (module, index) => {
    const isLocked = !module.unlocked;
    const isLeft = index % 2 === 0;
    const pathColor = module.unlocked ? '#000000c5' : '#cac7c7';
    
    return (
      <View key={module.id} style={styles.moduleWrapper}>
        {/* Línea punteada en S conectando módulos */}
        {index > 0 && (
          <View style={styles.pathContainer}>
            {/* Puntos que forman la línea curva en S */}
            {Array.from({ length: 18 }).map((_, i) => {
              const progress = i / 17;
              
              // Posición vertical (de arriba hacia abajo)
              const topPosition = progress * 100;
              
              // Posición horizontal (forma de S suave)
              let leftPosition;
              if (isLeft) {
                // Viene de derecha (85%) a izquierda (15%)
                const curveProgress = Math.sin(progress * Math.PI / 2);
                leftPosition = 85 - (curveProgress * 70);
              } else {
                // Viene de izquierda (15%) a derecha (85%)
                const curveProgress = Math.sin(progress * Math.PI / 2);
                leftPosition = 15 + (curveProgress * 70);
              }
              
              return (
                <View
                  key={i}
                  style={[
                    styles.pathDot,
                    {
                      backgroundColor: pathColor,
                      top: `${topPosition}%`,
                      left: `${leftPosition}%`,
                    }
                  ]}
                />
              );
            })}
          </View>
        )}
        
        {/* Módulo con texto al lado */}
        <View style={[
          styles.moduleRow, 
          { 
            justifyContent: isLeft ? 'flex-start' : 'flex-end',
            flexDirection: isLeft ? 'row' : 'row-reverse'
          }
        ]}>
          {/* Círculo del módulo */}
          <TouchableOpacity
            style={[
              styles.circleButton,
              { backgroundColor: module.color }
            ]}
            onPress={() => !isLocked && startLesson(module)}
            disabled={isLocked}
            activeOpacity={0.8}
          >
            <Text style={styles.circleIcon}>{module.icon}</Text>
            
            {!isLocked && module.completed === module.total && (
              <View style={styles.completeBadge}>
                <Ionicons name="checkmark-circle" size={35} color="#58CC02" />
              </View>
            )}
            
            {isLocked && (
              <View style={styles.lockOverlay}>
                <Ionicons name="lock-closed" size={40} color="#fff" />
              </View>
            )}
          </TouchableOpacity>
          
          {/* Información del módulo al lado del círculo */}
          <View style={[
            styles.moduleInfo,
            isLeft ? styles.moduleInfoRight : styles.moduleInfoLeft
          ]}>
            <Text style={styles.moduleName}>{module.title}</Text>
            
            {!isLocked && module.completed < module.total && (
              <View style={styles.progressContainer}>
                <View style={[styles.progressBarModule, { backgroundColor: module.color }]}>
                  <View 
                    style={[
                      styles.progressFill,
                      { width: `${(module.completed / module.total) * 100}%` }
                    ]}
                  />
                </View>
              </View>
            )}
            
            {!isLocked && module.completed === module.total && (
              <Text style={styles.completedText}>¡Desblocado!</Text>
            )}
            
            {isLocked && (
              <Text style={styles.lockedText}>Bloqueado</Text>
            )}
          </View>
        </View>
      </View>
    );
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

      <ScrollView 
        style={styles.scrollView}
        contentContainerStyle={styles.newPathContainer}
        showsVerticalScrollIndicator={false}
      >
        {/* Título Aprendizaje con estrellas decorativas */}
        <View style={styles.titleSection}>
          {/*<Text style={styles.starDecor}>⭐</Text>*/}
          <Text style={styles.mainTitle}>Aprendizaje</Text>
          {/*<Text style={styles.starDecor}>⭐</Text>*/}
        </View>

        {/* Barra de EXP con círculo de insignias a la derecha */}
        <View style={styles.expSection}>
          <View style={styles.expContent}>
            <View style={styles.expLeft}>
              {(() => {
                // Encontrar la insignia actual (última desbloqueada) y la siguiente
                const unlockedBadges = insignias.filter(badge => stars >= badge.req);
                const currentBadge = unlockedBadges.length > 0 
                  ? unlockedBadges[unlockedBadges.length - 1] 
                  : null;
                const nextBadge = insignias.find(badge => stars < badge.req);
                
                // Calcular min y max
                const minStars = currentBadge ? currentBadge.req : 0;
                const maxStars = nextBadge ? nextBadge.req : (currentBadge ? currentBadge.req : 1000);
                
                // Calcular progreso
                const progress = maxStars > minStars 
                  ? ((stars - minStars) / (maxStars - minStars)) * 100
                  : 0;
                
                return (
                  <>
                    <Text style={styles.expText}>{stars} / {maxStars} EXP</Text>
                    <View style={styles.expBarContainer}>
                      <View 
                        style={[
                          styles.expBarFill, 
                          { width: `${Math.min(progress, 100)}%` }
                        ]} 
                      />
                    </View>
                  </>
                );
              })()}
            </View>

            {/* Círculo azul con insignias */}
            <TouchableOpacity 
              style={styles.badgeCircle}
              onPress={() => setShowBadges(true)}
            >
              {lastUnlockedBadge ? (
                <Image 
                  source={badgeImages[lastUnlockedBadge.tipo]} 
                  style={styles.badgeCircleImage}
                  resizeMode="cover"
                />
              ) : (
                <Ionicons name="person" size={40} color="#fff" />
              )}
              {unlockedBadgesCount > 0 && (
                <View style={styles.badgeCountBadge}>
                  <Text style={styles.badgeCountText}>{unlockedBadgesCount}</Text>
                </View>
              )}
            </TouchableOpacity>
          </View>
        </View>

        {/* Estrellas decorativas flotantes */}
        <View style={styles.starsDecorContainer}>
          <Text style={[styles.floatingStar, { top: 200, left: 300 }]}>⭐</Text>
          <Text style={[styles.floatingStar, { top: 1150, right: 0 }]}>⭐</Text>
          <Text style={[styles.floatingStar, { top: 380, left: 40 }]}>⭐</Text>
          <Text style={[styles.floatingStar, { top: 680, right: 50 }]}>⭐</Text>
          <Text style={[styles.floatingStar, { top: 850, left: 105 }]}>⭐</Text>
          <Text style={[styles.floatingStar, { top: 1350, right: 150 }]}>⭐</Text>
          <Text style={[styles.floatingStar, { top: 1850, left: 105 }]}>⭐</Text>
          <Text style={[styles.floatingStar, { top: 1650, right: 10 }]}>⭐</Text>
            <Text style={[styles.floatingStar, { top: 2270, left: 95 }]}>⭐</Text>
            <Text style={[styles.floatingStar, { top: 2270, left: 120 }]}>⭐</Text>
            <Text style={[styles.floatingStar, { top: 2270, left: 145 }]}>⭐</Text>
            <Text style={[styles.floatingStar, { top: 2270, left: 170 }]}>⭐</Text>
            <Text style={[styles.floatingStar, { top: 2270, left: 195 }]}>⭐</Text>
            <Text style={[styles.floatingStar, { top: 2270, left: 220 }]}>⭐</Text>
            <Text style={[styles.floatingStar, { top: 2270, left: 245 }]}>⭐</Text>
            <Text style={[styles.floatingStar, { top: 2270, left: 270 }]}>⭐</Text>
          <Text style={[styles.floatingStar, { top: 2040, right: 10 }]}>⭐</Text>
        </View>

        {/* MODAL DEL DROPDOWN DE INSIGNIAS */}
        <Modal
          visible={showBadges}
          transparent={true}
          animationType="fade"
          onRequestClose={() => setShowBadges(false)}
        >
          <TouchableWithoutFeedback onPress={() => { setShowBadges(false); setZoomedBadge(null); }}>
            <View style={styles.modalOverlay}>
              <TouchableWithoutFeedback onPress={(e) => e.stopPropagation()}>
                <View style={styles.badgeDropdown}>
                <Text style={styles.dropdownTitle}>🇻🇪 Insignias Nacionales</Text>
                {insignias.map((item) => {
                  const isUnlocked = stars >= item.req;
                  const isZoomed = zoomedBadge === item.id;
                  
                  return (
                    <View key={item.id} style={styles.badgeRow}>
                      <TouchableOpacity
                        disabled={!isUnlocked}
                        onPress={() => setZoomedBadge(isZoomed ? null : item.id)}
                        activeOpacity={0.7}
                      >
                        <View style={[styles.badgeBase, { 
                          opacity: isUnlocked ? 1 : 0.3, 
                          backgroundColor: '#4FC3F7', 
                          justifyContent: 'center', 
                          alignItems: 'center',
                          transform: [{ scale: isZoomed ? 1.5 : 1 }],
                          zIndex: isZoomed ? 1000 : 1
                        }]}>
                          <Image 
                            source={badgeImages[item.tipo]} 
                            style={styles.badgeImage}
                            resizeMode="cover"
                          />
                        </View>
                      </TouchableOpacity>
                      <View>
                        <Text style={[styles.badgeName, { color: isUnlocked ? 'rgb(11, 80, 253)' : '#6e6e6e' }]}>
                          {item.name}
                        </Text>
                        {!isUnlocked && (
                          <Text style={styles.badgeReq}>Faltan {item.req - stars} ⭐</Text>
                        )}
                      </View>
                    </View>
                  );
                })}
                </View>
              </TouchableWithoutFeedback>
            </View>
          </TouchableWithoutFeedback>
        </Modal>

        {/* Camino de módulos estilo Duolingo */}
        <View style={styles.modulesPath}>
          {modules.map((module, index) => renderModule(module, index))}
        </View>

        <View style={{ height: 150 }} />
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: { 
    flex: 1, 
    backgroundColor: '#ffffff' 
  },
  
  // HEADER CON GRADIENT Y LOGOS
  header: {
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

  // TÍTULO APRENDIZAJE
  titleSection: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 25,
  },
  mainTitle: {
    fontSize: 32,
    fontWeight: '900',
    color: '#000000c5',
    marginHorizontal: 12,
  },
  starDecor: {
    fontSize: 26,
  },

  // SECCIÓN DE EXP CON CÍRCULO AZUL
  expSection: {
    marginBottom: 30,
    paddingHorizontal: 10,
  },
  expContent: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  expLeft: {
    flex: 1,
    marginRight: 15,
  },
  expText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#777',
    marginBottom: 8,
    textAlign: 'center',
  },
  expBarContainer: {
    width: '100%',
    height: 10,
    backgroundColor: '#E5E5E5',
    borderRadius: 5,
    overflow: 'hidden',
  },
  expBarFill: {
    height: '100%',
    backgroundColor: '#FFD700',
    borderRadius: 5,
  },

  // CÍRCULO AZUL CON INSIGNIAS
  badgeCircle: {
    width: 80,
    height: 80,
    borderRadius: 40,
    backgroundColor: '#1E90FF',
    alignItems: 'center',
    justifyContent: 'center',
    elevation: 6,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.3,
    shadowRadius: 5,
    position: 'relative',
  },
  badgeCircleImage: {
    width: '100%',
    height: '100%',
    borderRadius: 40,
  },
  badgeCountBadge: {
    position: 'absolute',
    top: -5,
    right: -5,
    backgroundColor: '#FF4444',
    width: 26,
    height: 26,
    borderRadius: 13,
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 2,
    borderColor: '#fff',
  },
  badgeCountText: {
    color: '#fff',
    fontSize: 13,
    fontWeight: 'bold',
  },

  // ESTRELLAS DECORATIVAS FLOTANTES
  starsDecorContainer: {
    position: 'absolute',
    width: '100%',
    height: '100%',
    pointerEvents: 'none',
  },
  floatingStar: {
    position: 'absolute',
    fontSize: 20,
    opacity: 0.5,
  },

  // MODAL DROPDOWN INSIGNIAS
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  badgeDropdown: {
    width: '90%',
    maxWidth: 400,
    backgroundColor: '#FFF',
    borderRadius: 20,
    padding: 20,
    elevation: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    borderWidth: 3,
    borderColor: '#000000',
  },
  dropdownTitle: {
    fontSize: 20,
    fontWeight: '900',
    color: '#00247D',
    marginBottom: 15,
    textAlign: 'center',
    borderBottomWidth: 2,
    borderBottomColor: '#EEE',
    paddingBottom: 10,
  },
  badgeRow: { 
    flexDirection: 'row', 
    alignItems: 'center', 
    marginBottom: 15, 
    gap: 12 
  },
  badgeBase: { 
    width: 50, 
    height: 50, 
    borderRadius: 25, 
    justifyContent: 'center', 
    alignItems: 'center', 
    borderWidth: 2, 
    borderColor: '#DDD', 
    overflow: 'hidden' 
  },
  badgeImage: { 
    width: '100%', 
    height: '100%', 
    borderRadius: 25 
  },
  badgeName: { 
    fontSize: 15, 
    fontWeight: '700', 
    flex: 1, 
    flexShrink: 1 
  },
  badgeReq: { 
    fontSize: 11, 
    color: '#FF4B4B', 
    fontWeight: 'bold' 
  },

  // CAMINO DE MÓDULOS (ESTILO DUOLINGO)
  modulesPath: {
    paddingVertical: 20,
  },
  moduleWrapper: {
    marginBottom: 0,
  },
  
  // CONTENEDOR DE CAMINO PUNTEADO
  pathContainer: {
    width: '100%',
    height: 110,
    position: 'relative',
    marginBottom: 5,
  },
  
  // PUNTOS DE LA LÍNEA
  pathDot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    position: 'absolute',
    marginLeft: -4,
    marginTop: -4,
  },
  
  moduleRow: {
    flexDirection: 'row',
    width: '100%',
    paddingHorizontal: 20,
    alignItems: 'center',
    marginBottom: 10,
  },
  circleButton: {
    width: 110,
    height: 110,
    borderRadius: 55,
    alignItems: 'center',
    justifyContent: 'center',
    elevation: 8,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 6,
    borderWidth: 5,
    borderColor: '#fff',
    position: 'relative',
  },
  circleIcon: {
    fontSize: 50,
  },
  completeBadge: {
    position: 'absolute',
    bottom: -8,
    right: -8,
    backgroundColor: '#fff',
    borderRadius: 20,
    elevation: 4,
  },
  lockOverlay: {
    position: 'absolute',
    width: '100%',
    height: '100%',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    borderRadius: 55,
    alignItems: 'center',
    justifyContent: 'center',
  },
  
  // INFORMACIÓN DEL MÓDULO AL LADO
  moduleInfo: {
    flex: 1,
    justifyContent: 'center',
  },
  moduleInfoRight: {
    marginLeft: 15,
    alignItems: 'flex-start',
  },
  moduleInfoLeft: {
    marginRight: 15,
    alignItems: 'flex-end',
  },
  moduleName: {
    fontSize: 16,
    fontWeight: '800',
    color: '#333',
    marginBottom: 6,
  },
  progressContainer: {
    width: 120,
  },
  progressBarModule: {
    width: '100%',
    height: 8,
    borderRadius: 4,
    overflow: 'hidden',
    backgroundColor: 'rgba(0,0,0,0.1)',
  },
  progressFill: {
    height: '100%',
    backgroundColor: '#fff',
    borderRadius: 4,
  },
  completedText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#58CC02',
    marginTop: 4,
  },
  lockedText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#999',
    marginTop: 4,
  },
});

export default LearningScreenDuolingo;