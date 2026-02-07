import React, { useState, useEffect, useMemo, useCallback, useRef } from 'react';
import {
  StyleSheet,
  View,
  TouchableOpacity,
  StatusBar,
  ActivityIndicator,
  Text,
  Modal,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { WebView } from 'react-native-webview';
import AsyncStorage from '@react-native-async-storage/async-storage';

export default function TranslatorScreen({ navigation }) {
  const [loading, setLoading] = useState(true);
  const [avatarSeleccionado, setAvatarSeleccionado] = useState('luis');
  const webViewRef = useRef(null);

  // Cargar avatar solo cuando la pantalla gana foco (evita carga duplicada)
  useEffect(() => {
    const loadAvatar = async () => {
      try {
        const savedAvatar = await AsyncStorage.getItem('selectedAvatar');
        if (savedAvatar && savedAvatar !== avatarSeleccionado) {
          setAvatarSeleccionado(savedAvatar);
          
          // Enviar mensaje al WebView para cambiar avatar sin recargar
          if (webViewRef.current) {
            webViewRef.current.postMessage(JSON.stringify({
              type: 'changeAvatar',
              avatar: savedAvatar.charAt(0).toUpperCase() + savedAvatar.slice(1)
            }));
          }
        }
      } catch (error) {
        console.error('Error cargando avatar:', error);
      }
    };

    const unsubscribe = navigation.addListener('focus', loadAvatar);
    
    // Cargar también al montar
    loadAvatar();
    
    return unsubscribe;
  }, [navigation, avatarSeleccionado]);

  // URL memoizada del visualizador 3D (no cambia con cada render)
  const webViewUrl = useMemo(() => {
    const avatarCapitalized = avatarSeleccionado.charAt(0).toUpperCase() + avatarSeleccionado.slice(1);
    return `http://192.168.86.27:8000/animation_mobile.html?avatar=${avatarCapitalized}`;
  }, [avatarSeleccionado]);

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
        <TouchableOpacity 
          onPress={() => navigation.goBack()} 
          style={styles.backButton}
        >
          <Ionicons name="arrow-back" size={35} color="black" />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>Traductor LSV</Text>
        <View style={styles.placeholder} />
      </LinearGradient>

      {/* Loading indicator */}
      {loading && (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#667eea" />
          <Text style={styles.loadingText}>Cargando traductor...</Text>
        </View>
      )}

      {/* WebView */}
      <WebView
        ref={webViewRef}
        source={{ uri: webViewUrl }}
        style={styles.webView}
        onLoadStart={() => setLoading(true)}
        onLoadEnd={() => setLoading(false)}
        onError={(error) => {
          console.error('❌ [TranslatorWebView] Error:', error.nativeEvent?.description || error);
          setLoading(false);
        }}
        onMessage={(event) => {
          try {
            const msg = JSON.parse(event.nativeEvent.data);
            // Solo loggear errores y eventos importantes, no todo
            if (msg.type === 'ERROR' || msg.type === 'ANIMATION_COMPLETE') {
              console.log(`[TranslatorWebView] ${msg.message}`, msg.data || '');
            }
          } catch (e) {
            // Silenciar logs normales del WebView
          }
        }}
        javaScriptEnabled={true}
        domStorageEnabled={true}
        startInLoadingState={true}
        allowsInlineMediaPlayback={true}
        mediaPlaybackRequiresUserAction={false}
        cacheEnabled={true}
        cacheMode="LOAD_CACHE_ELSE_NETWORK"
        androidLayerType="hardware"
        androidHardwareAccelerationDisabled={false}
        scalesPageToFit={true}
        nestedScrollEnabled={false}
        // Optimizaciones adicionales
        mixedContentMode="always"
        thirdPartyCookiesEnabled={false}
        sharedCookiesEnabled={false}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
  },
  header: {
    height: 100,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingTop: StatusBar.currentHeight || 30,
    paddingBottom: 10,
  },
  backButton: {
    padding: 8,
  },
  headerTitle: {
    fontSize: 25,
    fontWeight: '700',
    color: '#000000',
  },
  placeholder: {
    width: 40,
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
    color: '#667eea',
    fontWeight: '600',
  },
  webView: {
    flex: 1,
    backgroundColor: '#000',
  },
});
