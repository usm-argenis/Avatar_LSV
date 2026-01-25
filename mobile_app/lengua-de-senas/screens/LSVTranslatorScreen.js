/**
 * LSVTranslatorScreen - Componente React Native para traducción de texto a LSV
 * Avatar por defecto: Luis
 * Compatible con Expo + expo-three
 */

import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
  Dimensions,
  ActivityIndicator,
  Alert
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { ExpoWebGLRenderingContext, GLView } from 'expo-gl';
import { Renderer } from 'expo-three';
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';

// Importar módulos del sistema
import AvatarLoader from '../modules/loader';
import SignAnimator from '../modules/animator';
import LSVTranslator from '../modules/translator';
import apiService from '../services/apiService';

const { width, height } = Dimensions.get('window');

const LSVTranslatorScreen = () => {
  // ============= ESTADOS =============
  const [selectedAvatar, setSelectedAvatar] = useState('Luis'); // AVATAR POR DEFECTO
  const [isLoading, setIsLoading] = useState(true);
  const [loadingProgress, setLoadingProgress] = useState(0);
  const [inputText, setInputText] = useState('');
  const [translationResult, setTranslationResult] = useState([]);
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentAnimIndex, setCurrentAnimIndex] = useState(-1);
  const [playbackSpeed, setPlaybackSpeed] = useState(1.0);
  const [isOptimizing, setIsOptimizing] = useState(false);
  const [optimizationResult, setOptimizationResult] = useState(null);

  // ============= REFS =============
  const loaderRef = useRef(null);
  const animatorRef = useRef(null);
  const translatorRef = useRef(null);
  const sceneRef = useRef(null);
  const cameraRef = useRef(null);
  const rendererRef = useRef(null);
  const animationFrameRef = useRef(null);
  const clockRef = useRef(new THREE.Clock());
  const avatarCacheRef = useRef({}); // Caché de avatares cargados

  // ============= INICIALIZACIÓN =============
  useEffect(() => {
    // Inicializar traductor (no depende de 3D)
    translatorRef.current = new LSVTranslator();
    console.log('✅ Traductor LSV inicializado');

    return () => {
      // Cleanup
      if (animationFrameRef.current) {
        cancelAnimationFrame(animationFrameRef.current);
      }
    };
  }, []);

  // ============= CONFIGURACIÓN DE ESCENA 3D =============
  const onContextCreate = async (gl) => {
    try {
      // Configurar renderer
      const renderer = new Renderer({ gl });
      renderer.setSize(width, height * 0.6);
      renderer.setClearColor(0x1a1a2e);
      rendererRef.current = renderer;

      // Crear escena
      const scene = new THREE.Scene();
      scene.background = new THREE.Color(0x1a1a2e);
      sceneRef.current = scene;

      // Crear cámara
      const camera = new THREE.PerspectiveCamera(
        50,
        width / (height * 0.6),
        0.1,
        1000
      );
      camera.position.set(0, 1.6, 3);
      camera.lookAt(0, 1.2, 0);
      cameraRef.current = camera;

      // Luces
      const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
      scene.add(ambientLight);

      const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
      directionalLight.position.set(5, 10, 5);
      scene.add(directionalLight);

      const backLight = new THREE.DirectionalLight(0x4fc3f7, 0.4);
      backLight.position.set(-5, 5, -5);
      scene.add(backLight);

      // Inicializar loader
      loaderRef.current = new AvatarLoader(THREE, GLTFLoader);

      // Cargar avatar por defecto (Luis)
      await loadAvatar(selectedAvatar);

      // Iniciar loop de renderizado
      startRenderLoop();

      setIsLoading(false);
      console.log('✅ Escena 3D inicializada');

    } catch (error) {
      console.error('❌ Error en onContextCreate:', error);
      Alert.alert('Error', 'No se pudo inicializar el visor 3D');
      setIsLoading(false);
    }
  };

  // ============= CARGA DE AVATAR =============
  const loadAvatar = async (avatarName) => {
    try {
      // Verificar si el avatar ya está en caché
      if (avatarCacheRef.current[avatarName]) {
        console.log(`⚡ Usando avatar en caché: ${avatarName}`);
        
        // Remover avatar actual de la escena
        const previousAvatar = sceneRef.current.getObjectByName('currentAvatar');
        if (previousAvatar) {
          sceneRef.current.remove(previousAvatar);
        }
        
        // Añadir avatar desde caché
        const cachedAvatarData = avatarCacheRef.current[avatarName];
        cachedAvatarData.model.name = 'currentAvatar';
        sceneRef.current.add(cachedAvatarData.model);
        
        // Crear nuevo animator con los datos en caché
        animatorRef.current = new SignAnimator(cachedAvatarData, THREE);
        
        // Configurar callbacks
        animatorRef.current.on('AnimationStart', (name) => {
          console.log(`▶️ Reproduciendo: ${name}`);
          const index = translationResult.findIndex(anim => anim === name);
          setCurrentAnimIndex(index);
        });

        animatorRef.current.on('AnimationEnd', (name) => {
          console.log(`✅ Completado: ${name}`);
        });

        animatorRef.current.on('QueueComplete', () => {
          console.log('🏁 Secuencia completada');
          setIsPlaying(false);
          setCurrentAnimIndex(-1);
        });
        
        console.log(`✅ Avatar ${avatarName} cargado desde caché`);
        return;
      }
      
      setIsLoading(true);
      setLoadingProgress(0);
      console.log(`🔄 Cargando avatar: ${avatarName}`);

      // Cargar modelo base
      const avatarData = await loaderRef.current.loadAvatar(
        avatarName,
        (progress) => {
          setLoadingProgress(Math.round(progress));
        }
      );

      // Guardar en caché
      avatarCacheRef.current[avatarName] = avatarData;
      console.log(`💾 Avatar ${avatarName} guardado en caché`);

      // Agregar a escena
      if (sceneRef.current) {
        // Remover avatar anterior si existe
        const previousAvatar = sceneRef.current.getObjectByName('currentAvatar');
        if (previousAvatar) {
          sceneRef.current.remove(previousAvatar);
        }

        // Agregar nuevo avatar
        avatarData.model.name = 'currentAvatar';
        sceneRef.current.add(avatarData.model);

        // Centrar modelo
        const box = new THREE.Box3().setFromObject(avatarData.model);
        const center = box.getCenter(new THREE.Vector3());
        avatarData.model.position.sub(center);
        avatarData.model.position.y = 0;
      }

      // Crear animator
      animatorRef.current = new SignAnimator(avatarData, THREE);

      // Configurar callbacks
      animatorRef.current.on('AnimationStart', (name) => {
        console.log(`▶️ Reproduciendo: ${name}`);
        const index = translationResult.findIndex(anim => anim === name);
        setCurrentAnimIndex(index);
      });

      animatorRef.current.on('AnimationEnd', (name) => {
        console.log(`✅ Completado: ${name}`);
      });

      animatorRef.current.on('QueueComplete', () => {
        console.log('🏁 Secuencia completada');
        setIsPlaying(false);
        setCurrentAnimIndex(-1);
      });

      // Cargar animaciones comunes
      await loadCommonAnimations(avatarName);

      console.log(`✅ Avatar ${avatarName} cargado exitosamente`);

    } catch (error) {
      console.error('❌ Error cargando avatar:', error);
      Alert.alert('Error', `No se pudo cargar el avatar ${avatarName}`);
    } finally {
      setIsLoading(false);
    }
  };

  const loadCommonAnimations = async (avatarName) => {
    const commonAnimations = [
      'hola', 'adios', 'gracias', 'buenos_dias', 'buenas_tardes',
      'como_estas', 'mi', 'nombre', 'yo', 'tu', 'el', 'ella',
      'hoy', 'ayer', 'manana', 'lunes', 'martes', 'miercoles',
      // Alfabeto
      ...Array.from('abcdefghijklmnopqrstuvwxyz').map(l => `alfabeto_${l}`)
    ];

    await loaderRef.current.loadAnimations(
      avatarName,
      commonAnimations,
      (progress, animName) => {
        setLoadingProgress(Math.round(progress));
      }
    );

    console.log(`✅ Animaciones cargadas para ${avatarName}`);
  };

  // ============= LOOP DE RENDERIZADO =============
  const startRenderLoop = () => {
    const render = () => {
      animationFrameRef.current = requestAnimationFrame(render);

      const delta = clockRef.current.getDelta();

      // Actualizar animator
      if (animatorRef.current) {
        animatorRef.current.update(delta);
      }

      // Renderizar escena
      if (rendererRef.current && sceneRef.current && cameraRef.current) {
        rendererRef.current.render(sceneRef.current, cameraRef.current);
      }

      // Flush GL context (requerido para expo-gl)
      if (rendererRef.current) {
        rendererRef.current.gl.endFrameEXP();
      }
    };

    render();
  };

  // ============= TRADUCCIÓN Y REPRODUCCIÓN =============
  const handleTranslate = async () => {
    if (!inputText.trim()) {
      Alert.alert('Atención', 'Por favor ingresa un texto para traducir');
      return;
    }

    console.log(`📝 Traduciendo: "${inputText}"`);

    setIsOptimizing(true);
    
    try {
      // Optimizar con IA
      const result = await apiService.optimizarTexto(inputText);
      
      if (result.success) {
        setOptimizationResult(result.data);
        
        // Usar texto LSV optimizado
        const textoAUsar = result.data.textoLSV || result.data.textoCorregido;
        console.log(`✨ Optimizado por IA: "${textoAUsar}"`);
        
        // Traducir a animaciones
        const animations = translatorRef.current.translate(textoAUsar, {
          spellUnknownWords: true,
          includeIdle: false,
          maxSpellingLength: 10
        });

        if (animations.length === 0) {
          Alert.alert('Error', 'No se pudo traducir el texto');
          setIsOptimizing(false);
          return;
        }

        setTranslationResult(animations);
        console.log(`✅ Traducción: ${animations.length} animaciones`);
        
        // Mostrar info de optimización
        if (result.data.textoCorregido && result.data.textoCorregido !== inputText) {
          Alert.alert(
            'Texto Optimizado',
            `Original: "${inputText}"\nOptimizado: "${textoAUsar}"\nCobertura: ${(result.data.porcentajeCobertura || 0).toFixed(1)}%`,
            [{ text: 'OK' }]
          );
        }
      } else {
        // Fallback: traducir sin optimización
        console.warn('⚠️ API no disponible, traduciendo sin optimización');
        const animations = translatorRef.current.translate(inputText, {
          spellUnknownWords: true,
          includeIdle: false,
          maxSpellingLength: 10
        });

        if (animations.length === 0) {
          Alert.alert('Error', 'No se pudo traducir el texto');
          setIsOptimizing(false);
          return;
        }

        setTranslationResult(animations);
        console.log(`✅ Traducción (sin IA): ${animations.length} animaciones`);
        setIsOptimizing(false);
      }
    } catch (error) {
      console.error('Error en traducción:', error);
      Alert.alert('Error', 'Hubo un problema al traducir');
      setIsOptimizing(false);
    }
  };

  const handlePlay = () => {
    if (!animatorRef.current || translationResult.length === 0) {
      Alert.alert('Error', 'Primero debes traducir un texto');
      return;
    }

    setIsPlaying(true);
    
    animatorRef.current.playSequence(translationResult, {
      pauseBetween: 0.3,
      speed: playbackSpeed
    });
  };

  const handlePause = () => {
    if (animatorRef.current) {
      animatorRef.current.pause();
      setIsPlaying(false);
    }
  };

  const handleStop = () => {
    if (animatorRef.current) {
      animatorRef.current.stop();
      setIsPlaying(false);
      setCurrentAnimIndex(-1);
    }
  };

  const handleSpeedChange = (speed) => {
    setPlaybackSpeed(speed);
    if (animatorRef.current) {
      animatorRef.current.setSpeed(speed);
    }
  };

  const handleAvatarChange = async (avatarName) => {
    if (avatarName === selectedAvatar) return;
    
    setSelectedAvatar(avatarName);
    await loadAvatar(avatarName);
  };

  // ============= RENDER =============
  return (
    <View style={styles.container}>
      {/* Header */}
      <LinearGradient
        colors={['#1E3A8A', '#7C3AED', '#EC4899']}
        style={styles.header}
        start={{ x: 0, y: 0 }}
        end={{ x: 1, y: 0 }}
      >
        <Text style={styles.headerTitle}>🤟 Traductor LSV</Text>
      </LinearGradient>

      {/* Selector de Avatar */}
      <View style={styles.avatarSelector}>
        {['Nancy', 'Duvall', 'Luis', 'Carla', 'Argenis'].map(avatar => (
          <TouchableOpacity
            key={avatar}
            style={[
              styles.avatarBtn,
              selectedAvatar === avatar && styles.avatarBtnActive
            ]}
            onPress={() => handleAvatarChange(avatar)}
          >
            <Text style={[
              styles.avatarBtnText,
              selectedAvatar === avatar && styles.avatarBtnTextActive
            ]}>
              {avatar}
            </Text>
          </TouchableOpacity>
        ))}
      </View>

      {/* Visor 3D */}
      <View style={styles.viewerContainer}>
        {isLoading ? (
          <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="#4fc3f7" />
            <Text style={styles.loadingText}>
              Cargando {selectedAvatar}... {loadingProgress}%
            </Text>
          </View>
        ) : (
          <GLView style={styles.glView} onContextCreate={onContextCreate} />
        )}
      </View>

      {/* Panel de Controles */}
      <View style={styles.controlPanel}>
        {/* Input con botón integrado */}
        <View style={styles.inputRow}>
          <TextInput
            style={styles.textInput}
            placeholder="Escribe tu mensaje..."
            placeholderTextColor="rgba(255,255,255,0.4)"
            value={inputText}
            onChangeText={setInputText}
            editable={!isOptimizing}
          />
          <TouchableOpacity
            style={styles.translateBtn}
            onPress={handleTranslate}
            disabled={isOptimizing || !inputText.trim()}
          >
            <LinearGradient
              colors={isOptimizing ? ['#666', '#888'] : ['#f093fb', '#f5576c']}
              style={styles.gradientBtn}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              {isOptimizing ? (
                <ActivityIndicator color="white" />
              ) : (
                <Text style={styles.translateBtnText}>🤖 Traducir con IA</Text>
              )}
            </LinearGradient>
          </TouchableOpacity>
        </View>

        {/* Info de optimización */}
        {optimizationResult && (
          <View style={styles.optimizationInfo}>
            <Text style={styles.optimizationLabel}>✨ Optimizado por IA</Text>
            {optimizationResult.textoCorregido && optimizationResult.textoCorregido !== inputText && (
              <Text style={styles.optimizationText}>
                Corrección: "{optimizationResult.textoCorregido}"
              </Text>
            )}
            {optimizationResult.textoLSV && (
              <Text style={styles.optimizationText}>
                LSV: "{optimizationResult.textoLSV}"
              </Text>
            )}
            {optimizationResult.porcentajeCobertura !== undefined && (
              <Text style={styles.coverageText}>
                Cobertura: {optimizationResult.porcentajeCobertura.toFixed(1)}%
              </Text>
            )}
          </View>
        )}
      </View>

      {/* Panel de Resultado */}
      <ScrollView style={styles.translationPanel}>

        {/* Resultado */}
        {translationResult.length > 0 && (
          <View style={styles.resultContainer}>
            <Text style={styles.resultLabel}>Secuencia de Señas:</Text>
            <View style={styles.signChipsContainer}>
              {translationResult.map((anim, index) => (
                <View
                  key={`${anim}-${index}`}
                  style={[
                    styles.signChip,
                    currentAnimIndex === index && styles.signChipActive
                  ]}
                >
                  <Text style={styles.signChipText}>
                    {anim.replace(/_/g, ' ')}
                  </Text>
                </View>
              ))}
            </View>
          </View>
        )}

        {/* Controles de Reproducción */}
        {translationResult.length > 0 && (
          <View style={styles.playbackControls}>
            <TouchableOpacity
              style={styles.controlBtn}
              onPress={handlePlay}
              disabled={isPlaying}
            >
              <Text style={styles.controlBtnText}>▶</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.controlBtn}
              onPress={handlePause}
              disabled={!isPlaying}
            >
              <Text style={styles.controlBtnText}>⏸</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.controlBtn}
              onPress={handleStop}
            >
              <Text style={styles.controlBtnText}>⏹</Text>
            </TouchableOpacity>

            {/* Speed Control */}
            <View style={styles.speedControl}>
              <Text style={styles.speedLabel}>Velocidad:</Text>
              <View style={styles.speedButtons}>
                {[0.5, 1.0, 1.5, 2.0].map(speed => (
                  <TouchableOpacity
                    key={speed}
                    style={[
                      styles.speedBtn,
                      playbackSpeed === speed && styles.speedBtnActive
                    ]}
                    onPress={() => handleSpeedChange(speed)}
                  >
                    <Text style={styles.speedBtnText}>{speed}x</Text>
                  </TouchableOpacity>
                ))}
              </View>
            </View>
          </View>
        )}
      </ScrollView>
    </View>
  );
};

// ============= ESTILOS =============
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#1a1a2e',
  },
  header: {
    paddingTop: 50,
    paddingBottom: 15,
    paddingHorizontal: 20,
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
  },
  avatarSelector: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: 15,
    paddingVertical: 15,
    backgroundColor: 'rgba(0,0,0,0.5)',
  },
  avatarBtn: {
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 10,
    borderWidth: 2,
    borderColor: 'rgba(79, 195, 247, 0.5)',
    backgroundColor: 'rgba(255,255,255,0.1)',
  },
  avatarBtnActive: {
    backgroundColor: '#4fc3f7',
    borderColor: '#4fc3f7',
  },
  avatarBtnText: {
    color: 'white',
    fontWeight: '600',
  },
  avatarBtnTextActive: {
    color: '#1a1a2e',
  },
  viewerContainer: {
    height: height * 0.4,
    backgroundColor: '#1a1a2e',
    justifyContent: 'center',
    alignItems: 'center',
  },
  glView: {
    flex: 1,
    width: '100%',
  },
  loadingContainer: {
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    color: '#4fc3f7',
    marginTop: 15,
    fontSize: 16,
  },
  controlPanel: {
    backgroundColor: 'rgba(0,0,0,0.95)',
    paddingHorizontal: 20,
    paddingVertical: 15,
    borderTopWidth: 2,
    borderTopColor: 'rgba(79, 195, 247, 0.3)',
  },
  inputRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  textInput: {
    flex: 1,
    backgroundColor: 'rgba(255,255,255,0.1)',
    borderWidth: 2,
    borderColor: 'rgba(79, 195, 247, 0.5)',
    borderRadius: 12,
    padding: 12,
    color: 'white',
    fontSize: 16,
  },
  translationPanel: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.9)',
    paddingHorizontal: 20,
    paddingTop: 15,
  },
  translateBtn: {
    borderRadius: 12,
    overflow: 'hidden',
    minWidth: 140,
  },
  gradientBtn: {
    paddingVertical: 12,
    paddingHorizontal: 20,
    alignItems: 'center',
    justifyContent: 'center',
  },
  translateBtnText: {
    color: 'white',
    fontSize: 14,
    fontWeight: 'bold',
  },
  optimizationInfo: {
    marginTop: 12,
    padding: 12,
    backgroundColor: 'rgba(79, 195, 247, 0.1)',
    borderRadius: 8,
    borderLeftWidth: 3,
    borderLeftColor: '#4fc3f7',
  },
  optimizationLabel: {
    color: '#4fc3f7',
    fontSize: 12,
    fontWeight: 'bold',
    marginBottom: 6,
  },
  optimizationText: {
    color: 'rgba(255,255,255,0.9)',
    fontSize: 13,
    marginBottom: 4,
  },
  coverageText: {
    color: '#f093fb',
    fontSize: 12,
    fontWeight: '600',
    marginTop: 4,
  },
  resultContainer: {
    marginBottom: 20,
  },
  resultLabel: {
    fontSize: 12,
    color: '#4fc3f7',
    textTransform: 'uppercase',
    letterSpacing: 1,
    marginBottom: 10,
    fontWeight: 'bold',
  },
  signChipsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
  },
  signChip: {
    paddingVertical: 8,
    paddingHorizontal: 15,
    backgroundColor: 'rgba(79, 195, 247, 0.2)',
    borderWidth: 1,
    borderColor: 'rgba(79, 195, 247, 0.5)',
    borderRadius: 20,
  },
  signChipActive: {
    backgroundColor: '#f5576c',
    borderColor: '#f5576c',
  },
  signChipText: {
    color: 'white',
    fontSize: 14,
    fontWeight: '500',
  },
  playbackControls: {
    marginBottom: 30,
  },
  controlBtn: {
    width: 50,
    height: 50,
    borderRadius: 25,
    backgroundColor: 'rgba(79, 195, 247, 0.2)',
    borderWidth: 2,
    borderColor: 'rgba(79, 195, 247, 0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 10,
  },
  controlBtnText: {
    color: 'white',
    fontSize: 20,
  },
  speedControl: {
    marginTop: 15,
  },
  speedLabel: {
    color: '#aaa',
    fontSize: 14,
    marginBottom: 10,
  },
  speedButtons: {
    flexDirection: 'row',
    gap: 10,
  },
  speedBtn: {
    paddingVertical: 8,
    paddingHorizontal: 15,
    borderRadius: 8,
    backgroundColor: 'rgba(255,255,255,0.1)',
    borderWidth: 1,
    borderColor: 'rgba(79, 195, 247, 0.5)',
  },
  speedBtnActive: {
    backgroundColor: '#4fc3f7',
    borderColor: '#4fc3f7',
  },
  speedBtnText: {
    color: 'white',
    fontSize: 14,
    fontWeight: '600',
  },
});

export default LSVTranslatorScreen;
