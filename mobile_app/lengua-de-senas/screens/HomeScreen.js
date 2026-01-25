import React, { useState, useEffect } from 'react';
import {
  StyleSheet,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  Alert,
  Modal,
  ActivityIndicator,
  Platform,
  Image,
  StatusBar,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { WebView } from 'react-native-webview';
import AsyncStorage from '@react-native-async-storage/async-storage';
import AvatarSelector from '../components/AvatarSelector';
import apiService from '../services/apiService';
import { getCurrentUser, getUserProgress } from '../services/authService';

// URL del visualizador 3D
// En desarrollo:
// - Emulador Android: usar 10.0.2.2 (alias de localhost de la PC)
// - Expo Go en dispositivo físico: usar la IP local de la PC
// En producción: usar GitHub Pages
const getWebUrl = () => {
  if (__DEV__) {
    // Para Expo Go en tu teléfono, usar la IP de tu PC en el puerto 8000
    // Servidor corriendo desde /test/, entonces la URL es directa
    return 'http://192.168.10.93:8000/prueba.html';
  }
  return 'https://usm-argenis.github.io/STT_LSV/';
};

const WEB_3D_URL = getWebUrl();

const AVATARES = {
  nancy: 'Nancy',
  carla: 'Carla',
  luis: 'luis',
  duvall: 'Duvall',
  argenis: 'Argenis'
};

export default function HomeScreen({ navigation }) {
  const [activeTab, setActiveTab] = useState('traduccion');
  const [progress] = useState(0); // 0 de 6 lecciones completadas
  const [userStars, setUserStars] = useState(0);
  const [userLevel, setUserLevel] = useState(1);
  const [userName, setUserName] = useState('');
  const [avatarSeleccionado, setAvatarSeleccionado] = useState('luis');
  const [showWebView, setShowWebView] = useState(false);
  const [webViewUrl, setWebViewUrl] = useState(WEB_3D_URL);
  const [webViewLoading, setWebViewLoading] = useState(true);
  const [showAvatarSelector, setShowAvatarSelector] = useState(false);
  const [textoTraducir, setTextoTraducir] = useState('');
  const [isOptimizing, setIsOptimizing] = useState(false);
  const [optimizationResult, setOptimizationResult] = useState(null);

  // Cargar datos del usuario al montar
  useEffect(() => {
    loadUserData();
  }, []);

  // Recargar datos cuando vuelven a esta pantalla
  useEffect(() => {
    const unsubscribe = navigation.addListener('focus', () => {
      loadUserData();
    });
    return unsubscribe;
  }, [navigation]);

  const loadUserData = async () => {
    try {
      const user = await getCurrentUser();
      if (user) {
        setUserName(user.name);
        setUserStars(user.stars);
        setUserLevel(user.level);
        
        // Actualizar progreso desde el servidor
        const progressData = await getUserProgress(user.id);
        if (progressData.success) {
          setUserStars(progressData.data.stars);
          setUserLevel(progressData.data.level);
          console.log('✅ Progreso cargado:', progressData.data);
        }
      }
    } catch (error) {
      console.error('❌ Error cargando datos de usuario:', error);
    }
  };

  const lecciones = [
    {
      id: 1,
      titulo: 'Alfabeto en Lengua de Señas',
      descripcion: 'Aprende las letras del alfabeto',
      nivel: 'Básico',
      duracion: '15 min',
      icono: '📚',
      completado: false,
    },
    {
      id: 2,
      titulo: 'Números del 1 al 10',
      descripcion: 'Números básicos en señas',
      nivel: 'Básico',
      duracion: '10 min',
      icono: '🔢',
      completado: false,
    },
    {
      id: 3,
      titulo: 'Saludos y Presentaciones',
      descripcion: 'Frases comunes de saludo',
      nivel: 'Básico',
      duracion: '20 min',
      icono: '👋',
      completado: false,
    },
    {
      id: 4,
      titulo: 'Familia y Relaciones',
      descripcion: 'Vocabulario sobre familia',
      nivel: 'Intermedio',
      duracion: '25 min',
      icono: '👨‍👩‍👧‍👦',
      completado: false,
    },
    {
      id: 5,
      titulo: 'Colores y Formas',
      descripcion: 'Señas de colores y formas',
      nivel: 'Básico',
      duracion: '15 min',
      icono: '🎨',
      completado: false,
    },
  ];

  const abrirTraductor = async (palabra = '') => {
    const avatarName = AVATARES[avatarSeleccionado] || 'Nancy';
    
    let textoFinal = palabra;
    
    // Si hay texto, intentar optimizar con IA
    if (palabra && palabra.length > 0) {
      setIsOptimizing(true);
      
      try {
        const result = await apiService.optimizarTexto(palabra);
        
        if (result.success) {
          setOptimizationResult(result.data);
          textoFinal = result.data.textoLSV || result.data.textoCorregido || palabra;
          console.log('✨ Optimizado por IA:', textoFinal);
          console.log('📊 Cobertura:', result.data.porcentajeCobertura + '%');
          
          // Mostrar info de optimización
          if (result.data.textoCorregido !== palabra) {
            Alert.alert(
              '🤖 Texto Optimizado por IA',
              `Original: "${palabra}"\nOptimizado: "${textoFinal}"\nCobertura: ${(result.data.porcentajeCobertura || 0).toFixed(1)}%`,
              [{ text: 'OK' }]
            );
          }
        } else {
          console.warn('⚠️ API no disponible, usando texto original');
        }
      } catch (error) {
        console.error('Error al optimizar:', error);
      } finally {
        setIsOptimizing(false);
      }
    }
    
    // ============================================
    // CONFIGURACIÓN DE URL
    // ============================================
    let url = 'http://192.168.10.93:8000/animation_mobile.html';
    
    // Construir URL con parámetros de avatar y palabra optimizada
    const params = new URLSearchParams();
    params.append('avatar', avatarName);
    
    if (textoFinal) {
      params.append('text', textoFinal);
      params.append('autoload', 'true');
    }
    
    url = `${url}?${params.toString()}`;
    
    console.log('🌐 Abriendo URL:', url);
    console.log('👤 Avatar seleccionado:', avatarName);
    
    setWebViewUrl(url);
    setWebViewLoading(true);
    setShowWebView(true);
  };

  const handleSelectAvatar = async (avatarId, avatarName) => {
    setAvatarSeleccionado(avatarId);
    setShowAvatarSelector(false);
    
    // Guardar avatar seleccionado en AsyncStorage
    try {
      await AsyncStorage.setItem('selectedAvatar', avatarId);
      console.log('✅ Avatar guardado en HomeScreen:', avatarId);
      
      Alert.alert(
        'Avatar seleccionado',
        `Has seleccionado a ${avatarName}. El avatar se usará en el traductor 3D.`,
        [{ text: 'OK' }]
      );
    } catch (error) {
      console.error('Error guardando avatar:', error);
    }
  };

  const cerrarTraductor = () => {
    setShowWebView(false);
    setWebViewUrl(WEB_3D_URL);
  };

  const renderTraduccion = () => (
    <View style={styles.tabContent}>
      {/* Info del Avatar Actual */}
      <View style={styles.infoCard}>
        <Ionicons name="person-circle" size={32} color="#4A90E2" />
        <Text style={styles.infoText}>
          Usando avatar: <Text style={styles.infoBold}>{AVATARES[avatarSeleccionado]}</Text>
        </Text>
        <TouchableOpacity onPress={() => setShowAvatarSelector(true)}>
          <Ionicons name="settings-outline" size={20} color="#4A90E2" />
        </TouchableOpacity>
      </View>

      {/* Traductor Principal */}
      <View style={styles.card}>
        <View style={styles.cardHeader}>
          <View style={styles.iconContainer}>
            <Ionicons name="language" size={24} color="#4A90E2" />
          </View>
          <View style={styles.cardHeaderText}>
            <Text style={styles.cardTitle}>Traductor de Lengua de Señas</Text>
            <Text style={styles.cardSubtitle}>Escribe una frase para traducir</Text>
          </View>
        </View>
        
        {/* Botón de traducir con IA */}
        <TouchableOpacity
          style={styles.translateButton}
          onPress={() => abrirTraductor('')}
          disabled={isOptimizing}
        >
          <LinearGradient
            colors={['#4A90E2', '#357ABD']}
            start={{ x: 0, y: 0 }}
            end={{ x: 1, y: 0 }}
            style={styles.buttonGradient}
          >
            <Ionicons name="hand-left" size={24} color="white" style={{ marginRight: 8 }} />
            <Text style={styles.translateButtonText}>
              Abrir Traductor 3D con IA
            </Text>
          </LinearGradient>
        </TouchableOpacity>
      </View>

      {/* Accesos rápidos a letras */}
      <Text style={styles.sectionTitle}>Acceso Rápido</Text>
      <View style={styles.quickAccessGrid}>
        {['b', 'c', 'd', 'e'].map((letra) => (
          <TouchableOpacity
            key={letra}
            style={styles.quickAccessButton}
            onPress={() => abrirTraductor(letra)}
          >
            <Text style={styles.quickAccessLetter}>{letra.toUpperCase()}</Text>
          </TouchableOpacity>
        ))}
      </View>
    </View>
  );

  const renderAprendizaje = () => {
    const modules = [
      { id: 1, title: 'Alfabeto', icon: '🔤', color: '#58CC02', total: 27, completed: 0, category: 'alfabeto', emoji: '🅰️' },
      { id: 2, title: 'Números', icon: '🔢', color: '#00B5E2', total: 20, completed: 0, category: 'numeros', emoji: '🔢' },
      { id: 3, title: 'Saludos', icon: '👋', color: '#FF9600', total: 15, completed: 0, category: 'saludos', emoji: '👋' },
      { id: 4, title: 'Pronombres', icon: '👤', color: '#CE82FF', total: 10, completed: 0, category: 'pronombres', emoji: '👥' },
      { id: 5, title: 'Días', icon: '📅', color: '#FF4B4B', total: 7, completed: 0, category: 'dias_semana', emoji: '📅' },
      { id: 6, title: 'Tiempo', icon: '⏰', color: '#1CB0F6', total: 15, completed: 0, category: 'tiempo', emoji: '⏰' },
      { id: 7, title: 'Cortesía', icon: '🙏', color: '#FFC800', total: 10, completed: 0, category: 'cortesia', emoji: '🙏' },
      { id: 8, title: 'Preguntas', icon: '❓', color: '#FF66B3', total: 8, completed: 0, category: 'preguntas', emoji: '❓' }
    ];

    return (
      <View style={styles.tabContent}>
        {/* Header con mascota */}
        <View style={styles.learningHeader}>
          <View style={styles.mascotContainer}>
            <Text style={styles.mascotEmoji}>🐵</Text>
            <View style={styles.streakBadge}>
              <Text style={styles.streakNumber}>1</Text>
              <Text style={styles.streakFire}>🔥</Text>
            </View>
          </View>
          <View style={styles.headerTextContainer}>
            <Text style={styles.learningTitle}>Aprende LSV</Text>
            <Text style={styles.learningSubtitle}>Lengua de Señas Venezolana</Text>
          </View>
        </View>

        {/* Stats compacto */}
        <View style={styles.compactStats}>
          <View style={styles.compactStatItem}>
            <Text style={styles.compactStatValue}>414</Text>
            <Text style={styles.compactStatLabel}>XP total</Text>
          </View>
          <View style={styles.statDivider} />
          <View style={styles.compactStatItem}>
            <Text style={styles.compactStatValue}>5</Text>
            <Text style={styles.compactStatLabel}>Vidas</Text>
          </View>
        </View>

        {/* Módulos estilo Duolingo */}
        <View style={styles.modulesContainer}>
          {modules.map((module, index) => {
            const isLocked = index > 0 && modules[index - 1].completed === 0;
            return (
              <TouchableOpacity
                key={module.id}
                style={[
                  styles.duolingoModule,
                  { opacity: isLocked ? 0.5 : 1 }
                ]}
                onPress={() => {
                  if (!isLocked) {
                    navigation.navigate('Lesson', {
                      moduleId: module.id,
                      category: module.category,
                      title: module.title
                    });
                  }
                }}
                disabled={isLocked}
              >
                <View style={[styles.duolingoCircle, { backgroundColor: module.color }]}>
                  <Text style={styles.duolingoEmoji}>{module.emoji}</Text>
                  {isLocked && (
                    <View style={styles.lockOverlay}>
                      <Ionicons name="lock-closed" size={24} color="white" />
                    </View>
                  )}
                </View>
                <Text style={styles.duolingoTitle}>{module.title}</Text>
                <View style={styles.duolingoProgress}>
                  <View style={[styles.duolingoProgressBar, { width: `${(module.completed / module.total) * 100}%`, backgroundColor: module.color }]} />
                </View>
                <Text style={styles.duolingoProgressText}>
                  {module.completed}/{module.total}
                </Text>
              </TouchableOpacity>
            );
          })}
        </View>
      </View>
    );
  };

  const renderAvatar = () => {
    const avatars = [
      { id: 'luis', name: 'Luis', img: require('../assets/avatar/Luis.png'), color: '#3498DB', description: 'Avatar masculino - Completo' },
      { id: 'duvall', name: 'Duvall', img: require('../assets/avatar/Duvall.png'), color: '#E67E22', description: 'Avatar masculino - Completo' },
      { id: 'nancy', name: 'Nancy', img: require('../assets/avatar/Nancy.png'), color: '#9B59B6', description: 'Avatar femenino - Completo' },
      { id: 'carla', name: 'Carla', img: require('../assets/avatar/Carla.png'), color: '#FF6B9D', description: 'Avatar femenino - Completo' },
      { id: 'argenis', name: 'Argenis', img: require('../assets/avatar/Argenis.png'), color: '#2ECC71', description: 'Avatar masculino - Completo' }
    ];

    return (
      <View style={styles.tabContent}>
        <Text style={styles.sectionTitle}>Selecciona tu Avatar</Text>
        <Text style={styles.sectionSubtitle}>
          El avatar seleccionado se usará en todas las traducciones de lengua de señas
        </Text>

        <View style={styles.avatarGrid}>
          {avatars.map((avatar) => {
            const isSelected = avatarSeleccionado === avatar.id;
            return (
              <TouchableOpacity
                key={avatar.id}
                style={[
                  styles.avatarCardNew,
                  isSelected && styles.avatarCardSelected
                ]}
                onPress={() => handleSelectAvatar(avatar.id, avatar.name)}
              >
                <View style={styles.avatarImageContainer}>
                  <Image 
                    source={avatar.img}
                    style={styles.avatarImage}
                    resizeMode="cover"
                  />
                  {isSelected && (
                    <View style={styles.selectedBadgeNew}>
                      <Ionicons name="checkmark-circle" size={24} color="#4CAF50" />
                    </View>
                  )}
                </View>
                
                <View style={styles.avatarCardContent}>
                  <Text style={styles.avatarNameNew}>{avatar.name}</Text>
                  <Text style={styles.avatarDescriptionNew}>{avatar.description}</Text>
                  
                  {isSelected && (
                    <View style={styles.currentBadge}>
                      <Ionicons name="checkmark-circle" size={16} color="#4CAF50" />
                      <Text style={styles.currentText}>En uso</Text>
                    </View>
                  )}
                </View>
              </TouchableOpacity>
            );
          })}
        </View>

        {/* Info adicional */}
        <View style={styles.avatarInfo}>
          <Ionicons name="information-circle" size={24} color="#4A90E2" />
          <Text style={styles.avatarInfoText}>
            Los avatares animan las señas en 3D. Más avatares próximamente.
          </Text>
        </View>
      </View>
    );
  };

  const renderAprendizajeOLD = () => (
    <View style={styles.tabContent}>
      {/* Barra de Progreso */}
      <View style={styles.progressCard}>
        <Text style={styles.progressTitle}>Tu Progreso</Text>
        <Text style={styles.progressText}>⭐ {userStars} estrellas - Nivel {userLevel}</Text>
        <View style={styles.progressBarContainer}>
          <View style={[styles.progressBar, { width: `${(progress / lecciones.length) * 100}%` }]} />
        </View>
      </View>

      {/* Lista de Lecciones */}
      {lecciones.map((leccion) => (
        <TouchableOpacity
          key={leccion.id}
          style={styles.lessonCard}
          onPress={() => Alert.alert(leccion.titulo, 'Funcionalidad en desarrollo')}
        >
          <View style={styles.lessonIcon}>
            <Text style={styles.lessonEmoji}>{leccion.icono}</Text>
          </View>
          
          <View style={styles.lessonContent}>
            <Text style={styles.lessonTitle}>{leccion.titulo}</Text>
            <Text style={styles.lessonDescription}>{leccion.descripcion}</Text>
            
            <View style={styles.lessonMeta}>
              <View style={[
                styles.levelBadge,
                leccion.nivel === 'Básico' ? styles.levelBasico : styles.levelIntermedio
              ]}>
                <Text style={styles.levelText}>{leccion.nivel}</Text>
              </View>
              <Text style={styles.durationText}>{leccion.duracion}</Text>
            </View>
          </View>

          <View style={styles.lessonAction}>
            {leccion.completado ? (
              <Ionicons name="checkmark-circle" size={24} color="#27ae60" />
            ) : (
              <Ionicons name="play-circle-outline" size={24} color="#4A90E2" />
            )}
          </View>
        </TouchableOpacity>
      ))}
    </View>
  );



  return (
    <SafeAreaView style={styles.container} edges={['top', 'bottom']}>
      <StatusBar barStyle="light-content" backgroundColor="#667eea" />
      {/* Header */}
      <LinearGradient
        colors={['#667eea', '#764ba2']}
        style={styles.header}
      >
        <View style={styles.headerTop}>
          <View>
            <Text style={styles.headerTitle}>Traductor de Lengua de Señas</Text>
            <Text style={styles.headerSubtitle}>Bienvenido de vuelta</Text>
          </View>
          <TouchableOpacity onPress={() => navigation.replace('Login')}>
            <Ionicons name="log-out-outline" size={24} color="white" />
          </TouchableOpacity>
        </View>

        {/* Tabs */}
        <View style={styles.tabsContainer}>
          <TouchableOpacity
            style={[styles.tab, activeTab === 'traduccion' && styles.tabActive]}
            onPress={() => setActiveTab('traduccion')}
          >
            <Ionicons
              name="language"
              size={20}
              color={activeTab === 'traduccion' ? '#4A90E2' : 'white'}
            />
            <Text style={[styles.tabText, activeTab === 'traduccion' && styles.tabTextActive]}>
              Traducción
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.tab, activeTab === 'aprendizaje' && styles.tabActive]}
            onPress={() => {
              setActiveTab('aprendizaje');
              navigation.navigate('Learning');
            }}
          >
            <Ionicons
              name="school"
              size={20}
              color={activeTab === 'aprendizaje' ? '#4A90E2' : 'white'}
            />
            <Text style={[styles.tabText, activeTab === 'aprendizaje' && styles.tabTextActive]}>
              Aprendizaje
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.tab, activeTab === 'avatar' && styles.tabActive]}
            onPress={() => setActiveTab('avatar')}
          >
            <Ionicons
              name="person"
              size={20}
              color={activeTab === 'avatar' ? '#4A90E2' : 'white'}
            />
            <Text style={[styles.tabText, activeTab === 'avatar' && styles.tabTextActive]}>
              Avatar
            </Text>
          </TouchableOpacity>
        </View>
      </LinearGradient>

      {/* Content */}
      <ScrollView style={styles.content} showsVerticalScrollIndicator={false}>
        {activeTab === 'traduccion' && renderTraduccion()}
        {activeTab === 'avatar' && renderAvatar()}
      </ScrollView>

      {/* Modal Selector de Avatares */}
      <Modal
        visible={showAvatarSelector}
        animationType="slide"
        transparent={true}
        onRequestClose={() => setShowAvatarSelector(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            <View style={styles.modalHeader}>
              <Text style={styles.modalTitle}>Selecciona tu Avatar</Text>
              <TouchableOpacity
                onPress={() => setShowAvatarSelector(false)}
                style={styles.modalCloseButton}
              >
                <Ionicons name="close" size={24} color="#333" />
              </TouchableOpacity>
            </View>
            
            <AvatarSelector
              selectedAvatar={avatarSeleccionado}
              onSelectAvatar={handleSelectAvatar}
            />
          </View>
        </View>
      </Modal>

      {/* Modal WebView para Traductor 3D */}
      <Modal
        visible={showWebView}
        animationType="slide"
        onRequestClose={cerrarTraductor}
      >
        <View style={styles.webViewContainer}>
          {/* Header del WebView */}
          <View style={styles.webViewHeader}>
            <Text style={styles.webViewTitle}>Traductor 3D</Text>
            <TouchableOpacity
              style={styles.closeButton}
              onPress={cerrarTraductor}
            >
              <Ionicons name="close" size={28} color="#fff" />
            </TouchableOpacity>
          </View>

          {/* WebView */}
          {webViewLoading && (
            <View style={styles.loadingContainer}>
              <ActivityIndicator size="large" color="#4A90E2" />
              <Text style={styles.loadingText}>Cargando visualizador 3D...</Text>
              <Text style={styles.urlDebug}>{webViewUrl}</Text>
            </View>
          )}
          
          <WebView
            source={{ uri: webViewUrl }}
            style={styles.webView}
            onLoadStart={() => {
              console.log('📱 WebView iniciando carga...');
              setWebViewLoading(true);
            }}
            onLoadEnd={() => {
              console.log('✅ WebView carga completa');
              setWebViewLoading(false);
            }}
            onError={(syntheticEvent) => {
              const { nativeEvent } = syntheticEvent;
              console.error('❌ Error en WebView:', nativeEvent);
            }}
            onMessage={(event) => {
              console.log('📩 WebView message:', event.nativeEvent.data);
            }}
            javaScriptEnabled={true}
            domStorageEnabled={true}
            startInLoadingState={true}
            allowsFullscreenVideo={true}
            allowsInlineMediaPlayback={true}
            mediaPlaybackRequiresUserAction={false}
            keyboardDisplayRequiresUserAction={false}
            scrollEnabled={true}
            scalesPageToFit={true}
            bounces={false}
            originWhitelist={['*']}
            useWebKit={true}
            sharedCookiesEnabled={true}
            thirdPartyCookiesEnabled={true}
            setSupportMultipleWindows={false}
            textZoom={100}
          />
        </View>
      </Modal>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    paddingTop: 50,
    paddingBottom: 0,
    paddingHorizontal: 20,
  },
  headerTop: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 24,
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: '700',
    color: 'white',
  },
  headerSubtitle: {
    fontSize: 14,
    color: 'rgba(255, 255, 255, 0.8)',
    marginTop: 4,
  },
  tabsContainer: {
    flexDirection: 'row',
    gap: 8,
  },
  tab: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 12,
    paddingHorizontal: 16,
    borderTopLeftRadius: 12,
    borderTopRightRadius: 12,
    gap: 6,
  },
  tabActive: {
    backgroundColor: 'white',
  },
  tabText: {
    color: 'white',
    fontSize: 13,
    fontWeight: '600',
  },
  tabTextActive: {
    color: '#4A90E2',
  },
  content: {
    flex: 1,
    backgroundColor: 'white',
  },
  tabContent: {
    padding: 20,
  },
  card: {
    backgroundColor: 'white',
    borderRadius: 16,
    padding: 20,
    marginBottom: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  cardHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  iconContainer: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#EBF5FF',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  cardHeaderText: {
    flex: 1,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: '#2c3e50',
  },
  cardSubtitle: {
    fontSize: 14,
    color: '#7f8c8d',
    marginTop: 2,
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F5F5F5',
    borderRadius: 12,
    paddingHorizontal: 16,
    paddingVertical: 4,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#E0E0E0',
  },
  textInput: {
    flex: 1,
    fontSize: 16,
    color: '#2c3e50',
    paddingVertical: 12,
  },
  clearButton: {
    padding: 4,
    marginLeft: 8,
  },
  optimizationInfo: {
    marginTop: 12,
    marginBottom: 8,
    padding: 12,
    backgroundColor: 'rgba(74, 144, 226, 0.1)',
    borderRadius: 8,
    borderLeftWidth: 3,
    borderLeftColor: '#4A90E2',
  },
  optimizationLabel: {
    color: '#4A90E2',
    fontSize: 12,
    fontWeight: 'bold',
    marginBottom: 6,
  },
  optimizationText: {
    color: '#333',
    fontSize: 13,
    marginBottom: 4,
  },
  coverageText: {
    color: '#E24A90',
    fontSize: 12,
    fontWeight: '600',
    marginTop: 4,
  },
  translateButton: {
    borderRadius: 12,
    overflow: 'hidden',
  },
  buttonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 16,
  },
  translateButtonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: '600',
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: '#2c3e50',
    marginBottom: 4,
  },
  sectionSubtitle: {
    fontSize: 14,
    color: '#7f8c8d',
    marginBottom: 16,
    lineHeight: 20,
  },
  quickAccessGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 12,
    marginTop: 16,
  },
  quickAccessButton: {
    width: '22%',
    aspectRatio: 1,
    backgroundColor: 'white',
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  quickAccessLetter: {
    fontSize: 32,
    fontWeight: '700',
    color: '#4A90E2',
  },
  progressCard: {
    backgroundColor: '#EBF5FF',
    borderRadius: 16,
    padding: 20,
    marginBottom: 20,
  },
  progressTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#2c3e50',
    marginBottom: 4,
  },
  progressText: {
    fontSize: 14,
    color: '#7f8c8d',
    marginBottom: 12,
  },
  progressBarContainer: {
    height: 8,
    backgroundColor: 'rgba(74, 144, 226, 0.2)',
    borderRadius: 4,
    overflow: 'hidden',
  },
  progressBar: {
    height: '100%',
    backgroundColor: '#4A90E2',
    borderRadius: 4,
  },
  lessonCard: {
    flexDirection: 'row',
    backgroundColor: 'white',
    borderRadius: 16,
    padding: 16,
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  lessonIcon: {
    width: 56,
    height: 56,
    borderRadius: 28,
    backgroundColor: '#FFF5E6',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 12,
  },
  lessonEmoji: {
    fontSize: 28,
  },
  lessonContent: {
    flex: 1,
  },
  lessonTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#2c3e50',
    marginBottom: 4,
  },
  lessonDescription: {
    fontSize: 13,
    color: '#7f8c8d',
    marginBottom: 8,
  },
  lessonMeta: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  levelBadge: {
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
  },
  levelBasico: {
    backgroundColor: '#FF6B35',
  },
  levelIntermedio: {
    backgroundColor: '#FFA500',
  },
  levelText: {
    fontSize: 11,
    fontWeight: '600',
    color: 'white',
  },
  durationText: {
    fontSize: 12,
    color: '#7f8c8d',
  },
  lessonAction: {
    justifyContent: 'center',
    marginLeft: 8,
  },
  avatarCard: {
    flexDirection: 'row',
    backgroundColor: 'white',
    borderRadius: 16,
    padding: 16,
    marginBottom: 12,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  avatarCircle: {
    width: 72,
    height: 72,
    borderRadius: 36,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  avatarEmoji: {
    fontSize: 36,
  },
  avatarInfo: {
    flex: 1,
  },
  avatarName: {
    fontSize: 16,
    fontWeight: '600',
    color: '#2c3e50',
    marginBottom: 4,
  },
  avatarDescription: {
    fontSize: 13,
    color: '#7f8c8d',
  },
  selectedBadge: {
    alignItems: 'center',
  },
  selectedText: {
    fontSize: 11,
    color: '#4A90E2',
    fontWeight: '600',
    marginTop: 4,
  },
  selectButton: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 8,
    borderWidth: 2,
    borderColor: '#4A90E2',
  },
  selectButtonText: {
    color: '#4A90E2',
    fontSize: 13,
    fontWeight: '600',
  },
  // Info Card de Avatar en Traducción
  infoCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F0F8FF',
    borderRadius: 12,
    padding: 12,
    marginBottom: 16,
    gap: 12,
  },
  infoText: {
    flex: 1,
    fontSize: 14,
    color: '#666',
  },
  infoBold: {
    fontWeight: '700',
    color: '#4A90E2',
  },
  // Avatar Grid
  avatarGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginBottom: 20,
  },
  avatarCardNew: {
    width: '48%',
    backgroundColor: 'white',
    borderRadius: 16,
    marginBottom: 15,
    overflow: 'hidden',
    borderWidth: 3,
    borderColor: '#E0E0E0',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  avatarImageContainer: {
    width: '100%',
    height: 150,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#f0f0f0',
    position: 'relative',
  },
  avatarImage: {
    width: '100%',
    height: '100%',
  },
  avatarGradient: {
    padding: 30,
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: 150,
  },
  avatarCardContent: {
    padding: 12,
    backgroundColor: '#f5f5f5',
  },
  avatarCardSelected: {
    borderColor: '#4CAF50',
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 6,
    transform: [{ scale: 1.02 }],
  },
  selectedBadgeNew: {
    position: 'absolute',
    top: 10,
    right: 10,
  },
  avatarNameNew: {
    fontSize: 16,
    fontWeight: '700',
    color: '#2c3e50',
    marginBottom: 4,
    textAlign: 'center',
  },
  avatarDescriptionNew: {
    fontSize: 11,
    color: '#7f8c8d',
    textAlign: 'center',
    marginBottom: 4,
  },
  currentBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 10,
    paddingHorizontal: 12,
    paddingVertical: 6,
    backgroundColor: '#E8F5E9',
    borderRadius: 12,
    gap: 4,
  },
  currentText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#4CAF50',
  },
  avatarInfo: {
    flexDirection: 'row',
    backgroundColor: '#F0F8FF',
    borderRadius: 12,
    padding: 16,
    gap: 12,
    alignItems: 'center',
  },
  avatarInfoText: {
    flex: 1,
    fontSize: 13,
    color: '#666',
    lineHeight: 20,
  },
  // Estilos Header con Mascota
  learningHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'white',
    borderRadius: 20,
    padding: 20,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 4,
  },
  mascotContainer: {
    position: 'relative',
    marginRight: 16,
  },
  mascotEmoji: {
    fontSize: 72,
  },
  streakBadge: {
    position: 'absolute',
    bottom: -5,
    right: -5,
    backgroundColor: '#FF9600',
    borderRadius: 20,
    paddingHorizontal: 8,
    paddingVertical: 4,
    flexDirection: 'row',
    alignItems: 'center',
    borderWidth: 3,
    borderColor: 'white',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
    elevation: 3,
  },
  streakNumber: {
    fontSize: 16,
    fontWeight: '900',
    color: 'white',
    marginRight: 2,
  },
  streakFire: {
    fontSize: 14,
  },
  headerTextContainer: {
    flex: 1,
  },
  learningTitle: {
    fontSize: 26,
    fontWeight: '800',
    color: '#58CC02',
    marginBottom: 4,
    letterSpacing: 0.5,
  },
  learningSubtitle: {
    fontSize: 14,
    color: '#777',
    fontWeight: '600',
  },
  // Stats compacto
  compactStats: {
    flexDirection: 'row',
    backgroundColor: 'white',
    borderRadius: 16,
    padding: 16,
    marginBottom: 20,
    alignItems: 'center',
    justifyContent: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  compactStatItem: {
    alignItems: 'center',
    flex: 1,
  },
  compactStatValue: {
    fontSize: 24,
    fontWeight: '800',
    color: '#1CB0F6',
    marginBottom: 4,
  },
  compactStatLabel: {
    fontSize: 12,
    color: '#777',
    fontWeight: '600',
  },
  statDivider: {
    width: 1,
    height: 40,
    backgroundColor: '#E5E5E5',
    marginHorizontal: 20,
  },
  // Módulos estilo Duolingo
  modulesContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  duolingoModule: {
    width: '48%',
    backgroundColor: 'white',
    borderRadius: 20,
    padding: 16,
    marginBottom: 12,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 4,
  },
  duolingoCircle: {
    width: 70,
    height: 70,
    borderRadius: 35,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.2,
    shadowRadius: 5,
    elevation: 5,
  },
  duolingoEmoji: {
    fontSize: 36,
  },
  lockOverlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    borderRadius: 35,
    justifyContent: 'center',
    alignItems: 'center',
  },
  duolingoTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#2c3e50',
    marginBottom: 8,
    textAlign: 'center',
  },
  duolingoProgress: {
    width: '100%',
    height: 8,
    backgroundColor: '#E5E5E5',
    borderRadius: 4,
    overflow: 'hidden',
    marginBottom: 6,
  },
  duolingoProgressBar: {
    height: '100%',
    borderRadius: 4,
  },
  duolingoProgressText: {
    fontSize: 12,
    color: '#777',
    fontWeight: '600',
  },
  // Estilos del Modal de Avatares
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modalContent: {
    backgroundColor: 'white',
    borderRadius: 20,
    width: '90%',
    maxHeight: '80%',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 4,
    elevation: 5,
  },
  modalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  modalTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
  },
  modalCloseButton: {
    padding: 5,
  },
  // Estilos del WebView Modal
  webViewContainer: {
    flex: 1,
    backgroundColor: '#000',
  },
  webViewHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingTop: 50,
    paddingBottom: 15,
    paddingHorizontal: 20,
    backgroundColor: '#667eea',
  },
  webViewTitle: {
    fontSize: 20,
    fontWeight: '700',
    color: '#fff',
  },
  closeButton: {
    padding: 8,
  },
  webView: {
    flex: 1,
    backgroundColor: '#fff',
  },
  loadingContainer: {
    position: 'absolute',
    top: '50%',
    left: 0,
    right: 0,
    alignItems: 'center',
    justifyContent: 'center',
    zIndex: 10,
  },
  loadingText: {
    marginTop: 12,
    fontSize: 16,
    color: '#4A90E2',
    fontWeight: '600',
  },
  urlDebug: {
    marginTop: 8,
    fontSize: 12,
    color: '#666',
    textAlign: 'center',
    paddingHorizontal: 20,
  },
});
