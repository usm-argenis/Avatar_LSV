import React, { useState, useEffect, useRef } from 'react';
import {
  StyleSheet,
  View,
  Text,
  TouchableOpacity,
  StatusBar,
  Modal,
  Dimensions,
  Animated,
  TouchableWithoutFeedback,
  Image,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';
import { WebView } from 'react-native-webview';
import { LinearGradient } from 'expo-linear-gradient';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { getCurrentUser, logout } from '../services/authService';
import AvatarSelector from '../components/AvatarSelector';

const { width, height } = Dimensions.get('window');

export default function MainScreen({ navigation }) {
  const [userName, setUserName] = useState('');
  const [showAvatarSelector, setShowAvatarSelector] = useState(false);
  const [avatarSeleccionado, setAvatarSeleccionado] = useState('luis');
  const [showMenu, setShowMenu] = useState(false);
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const slideAnim = useRef(new Animated.Value(-10)).current;

  useEffect(() => {
    loadUserData();
    loadSelectedAvatar();
  }, []);

  useEffect(() => {
    const unsubscribe = navigation.addListener('focus', () => {
      loadSelectedAvatar();
      loadUserData();
    });
    return unsubscribe;
  }, [navigation]);

  useEffect(() => {
    if (showMenu) {
      Animated.parallel([
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration: 200,
          useNativeDriver: true,
        }),
        Animated.timing(slideAnim, {
          toValue: 0,
          duration: 200,
          useNativeDriver: true,
        }),
      ]).start();
    } else {
      Animated.parallel([
        Animated.timing(fadeAnim, {
          toValue: 0,
          duration: 150,
          useNativeDriver: true,
        }),
        Animated.timing(slideAnim, {
          toValue: -10,
          duration: 150,
          useNativeDriver: true,
        }),
      ]).start();
    }
  }, [showMenu]);

  const loadUserData = async () => {
    try {
      const user = await getCurrentUser();
      if (user) {
        setUserName(user.name);
      }
    } catch (error) {
      console.error('Error cargando datos de usuario:', error);
    }
  };

  const loadSelectedAvatar = async () => {
    try {
      const savedAvatar = await AsyncStorage.getItem('selectedAvatar');
      if (savedAvatar) {
        setAvatarSeleccionado(savedAvatar);
        console.log('✅ Avatar cargado:', savedAvatar);
      }
    } catch (error) {
      console.error('Error cargando avatar:', error);
    }
  };

  const handleLogout = async () => {
    setShowMenu(false);
    await logout();
    navigation.replace('Login');
  };

  const handleSettings = () => {
    setShowMenu(false);
    navigation.navigate('Settings');
  };

  const handleSelectAvatar = async (avatarId) => {
    setAvatarSeleccionado(avatarId);
    setShowAvatarSelector(false);
    
    try {
      await AsyncStorage.setItem('selectedAvatar', avatarId);
      console.log('✅ Avatar guardado:', avatarId);
    } catch (error) {
      console.error('Error guardando avatar:', error);
    }
  };

  // URL del visualizador 3D estático con el avatar seleccionado
  const avatarViewerUrl = `http://192.168.10.93:8000/avatar_static.html?avatar=${avatarSeleccionado.charAt(0).toUpperCase() + avatarSeleccionado.slice(1)}`;

  return (
    <SafeAreaView style={styles.container} edges={['bottom']}>
      <StatusBar barStyle="light-content" backgroundColor="#1dffa1" // Aquí pones tu color exacto (Hexadecimal)
  translucent={true} />
      
      {/* Header con imágenes: Guacamaya + Logo VeneSeñas + Seña */}
      <LinearGradient //'#008afc', '#6abcff', '#50b0ff', '#81c3f8', '#cce8ff', '#ffffff'
        colors={['#04309e', '#0056b3', '#34a3fd', '#77c1fd', '#cfe8fa', '#ffffff']}
  style={styles.header}
  // Start en (0.5, 0) es el centro superior
  start={{ x: 0.5, y: 0 }}
  // End en (0.5, 1) es el centro inferior (degradado vertical)
  end={{ x: 0.5, y: 1 }}
      >
        <View style={styles.headerContent} >
          {/* Guacamaya (izquierda) */}
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

          {/* Seña/Mano (derecha) */}
          <View style={styles.imageContainer}>
            <Image 
              source={require('../assets/images/sena-hand.png')}
              style={styles.senaImage}
              resizeMode="contain"
            />
          </View>
        </View>

        {/* Botón de menú flotante */}
        <TouchableOpacity 
          onPress={() => setShowMenu(!showMenu)} 
          style={styles.menuButtonFloating}
        >
          <Ionicons name="menu" size={35} color="black" />
        </TouchableOpacity>

        {/* Menú desplegable */}
        {showMenu && (
          <TouchableWithoutFeedback onPress={() => setShowMenu(false)}>
            <View style={styles.menuOverlay}>
              <TouchableWithoutFeedback>
                <Animated.View
                  style={[
                    styles.menuDropdown,
                    {
                      opacity: fadeAnim,
                      transform: [{ translateY: slideAnim }],
                    },
                  ]}
                >
                  <TouchableOpacity style={styles.menuItem} onPress={handleSettings}>
                    <Ionicons name="settings" size={22} color="#2196F3" />
                    <Text style={styles.menuItemText}>Configuración</Text>
                  </TouchableOpacity>
                  
                  <View style={styles.menuDivider} />
                  
                  <TouchableOpacity style={styles.menuItem} onPress={handleLogout}>
                    <Ionicons name="log-out" size={22} color="#F44336" />
                    <Text style={styles.menuItemText}>Cerrar Sesión</Text>
                  </TouchableOpacity>
                </Animated.View>
              </TouchableWithoutFeedback>
            </View>
          </TouchableWithoutFeedback>
        )}
      </LinearGradient>

      {/* Avatar 3D en el centro */}
      <View style={styles.avatarContainer}>
        <WebView
          source={{ uri: avatarViewerUrl }}
          style={styles.avatarWebView}
          opaque={false}
          javaScriptEnabled={true}
          domStorageEnabled={true}
          scrollEnabled={false}
          bounces={false}
          showsVerticalScrollIndicator={false}
          showsHorizontalScrollIndicator={false}
        />
      </View>

      {/* Botones circulares con colores de bandera */}
      <View style={styles.buttonsContainer}>

        <TouchableOpacity 
          style={[styles.circleButton, styles.learningButton]}
          onPress={() => navigation.navigate('Learning')}
        >
          <Ionicons name="school" size={40} color="black" />
          <Text style={styles.buttonLabel}>Aprendizaje</Text>
        </TouchableOpacity>

        <TouchableOpacity 
          style={[styles.circleButton1, styles.translatorButton]}
          onPress={() => navigation.navigate('Translator')}
        >
          <Ionicons name="language" size={40} color="black" />
          <Text style={styles.buttonLabel1}>Traductor</Text>
        </TouchableOpacity>

        <TouchableOpacity 
          style={[styles.circleButton, styles.avatarButton]}
          onPress={() => setShowAvatarSelector(true)}
        >
          <MaterialCommunityIcons name="account-switch" size={40} color="black" />
          <Text style={styles.buttonLabel}>Avatar</Text>
        </TouchableOpacity>
      </View>

      {/* Modal de Selector de Avatares */}
      <Modal
        visible={showAvatarSelector}
        animationType="slide"
        transparent={false}
        onRequestClose={() => setShowAvatarSelector(false)}
      >
        <SafeAreaView style={styles.modalContainer} edges={['top', 'bottom']}>
          <AvatarSelector
            selectedAvatar={avatarSeleccionado}
            onSelectAvatar={handleSelectAvatar}
            onClose={() => setShowAvatarSelector(false)}
          />
        </SafeAreaView>
      </Modal>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#ffffff',
  },
  header: {
    
    paddingVertical: 20,
    paddingHorizontal: 15,
    position: 'relative',
   
  },
  headerContent: {
    top: 20,
    flexDirection: 'row',
    alignItems: 'center',
  },
  imageContainer: {
    
    height: 60,
    
  },
  guacamayaImage:{
    width: 35,
    height: 55,
    
  },
  brandImageContainer: {
    
    width: 150,
    height: 60,
    justifyContent: 'center',
    alignItems: 'center',
    
  },
  brandImage: {
 
    width: '100%',
    height: 80,
  },
  senaImage: {
    width: 40,
    height: 50,
  },
  menuButtonFloating: {
    position: 'absolute',
    top: 40,
    right: 10,
    //backgroundColor: 'rgb(0, 0, 0)',
    borderRadius: 20,
    padding: 8,
    zIndex: 100,
  },
  menuOverlay: {
    position: 'absolute',
    top: 70,
    right: 15,
    zIndex: 1000,
  },
  menuDropdown: {
    backgroundColor: 'white',
    borderRadius: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 8,
    minWidth: 200,
    overflow: 'hidden',
  },
  menuItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 15,
    paddingHorizontal: 20,
    gap: 12,
  },
  menuItemText: {
    fontSize: 16,
    color: '#000000',
    fontWeight: '600',
  },
  menuDivider: {
    height: 1,
    backgroundColor: '#ffffff',
  },
  avatarContainer: {
    flex: 0.99,
    marginTop: -1,
    backgroundColor: '#ffffff',
  },
  avatarWebView: {
    flex: 1,
  },
  buttonsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingBottom: 25,
    paddingTop: 10,
  },
  circleButton: {
    width: 95,
    height: 90,
    borderRadius: 35,
    borderWidth: 3,
    borderColor: '#ffffff',
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.4,
    shadowRadius: 10,
    elevation: 8,
  },
  circleButton1: {
    width:120,
    height: 120,
    borderRadius: 40,
    borderWidth: 4,
    borderColor: '#ffffff',
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.4,
    shadowRadius: 10,
    elevation: 8,
  },
  translatorButton: {
    backgroundColor: '#2196F3',
  },
  learningButton: {
    backgroundColor: '#FFC107',
  },
  avatarButton: {
    backgroundColor: '#F44336',
  },
  buttonLabel: {
    color: 'black',
    fontSize: 12,
    fontWeight: '700',
    marginTop: 5,
    textAlign: 'center',
  },
  buttonLabel1: {
    color: 'black',
    fontSize: 17,
    fontWeight: '700',
    marginTop: 5,
    textAlign: 'center',
  },
  modalContainer: {
    flex: 1,
    backgroundColor: '#ffffff',
  },
});
