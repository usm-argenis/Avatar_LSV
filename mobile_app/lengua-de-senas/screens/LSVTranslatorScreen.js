/**
 * LSVTranslatorScreen - Componente React Native para traducción de texto a LSV
 * Avatar por defecto: Luis
 * Compatible con Expo + expo-three
 * OPTIMIZADO para mejor rendimiento en dispositivos móviles
 */

import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
  Dimensions,
  ActivityIndicator,
  Alert,
  InteractionManager
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
import { GLB_SERVER_URL } from '../config/serverConfig';

// Importar utilidades de optimización
import {
  executeAfterInteractions,
  debounce,
  throttle,
  avatarCache,
  lazyAnimationLoader,
  RenderOptimizer,
  memoryOptimizer,
  batchAnimationLoader
} from '../utils/performanceOptimizations';

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
  const [animationsReady, setAnimationsReady] = useState(false);
  const [loadingAnimations, setLoadingAnimations] = useState(false);

  // ============= REFS =============
  const loaderRef = useRef(null);
  const animatorRef = useRef(null);
  const translatorRef = useRef(null);
  const sceneRef = useRef(null);
  const cameraRef = useRef(null);
  const rendererRef = useRef(null);
  const animationFrameRef = useRef(null);
  const clockRef = useRef(new THREE.Clock());
  const renderOptimizerRef = useRef(new RenderOptimizer());
  const isChangingAvatarRef = useRef(false);

  // ============= INICIALIZACIÓN =============
  useEffect(() => {
    // Inicializar traductor (no depende de 3D)
    translatorRef.current = new LSVTranslator();
    console.log('✅ Traductor LSV inicializado');

    return () => {
      // Cleanup mejorado con gestión de memoria
      console.log('🧹 Limpiando recursos...');
      
      // Detener loop de renderizado
      if (animationFrameRef.current) {
        cancelAnimationFrame(animationFrameRef.current);
      }

      // Limpiar avatar actual
      if (sceneRef.current) {
        const avatar = sceneRef.current.getObjectByName('currentAvatar');
        if (avatar) {
          memoryOptimizer.disposeAvatar(avatar);
          sceneRef.current.remove(avatar);
        }
      }

      // Detener animator
      if (animatorRef.current) {
        animatorRef.current.stop();
        animatorRef.current = null;
      }

      // Limpiar escena
      if (sceneRef.current) {
        sceneRef.current.clear();
      }

      // Disponer renderer
      if (rendererRef.current) {
        rendererRef.current.dispose();
      }

      console.log('✅ Recursos liberados correctamente');
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

      // Inicializar loader con URL del servidor
      console.log(`🌐 Configurando AvatarLoader con servidor: ${GLB_SERVER_URL}`);
      loaderRef.current = new AvatarLoader(THREE, GLTFLoader, GLB_SERVER_URL);

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

  // ============= CARGA DE AVATAR (OPTIMIZADA) =============
  const loadAvatar = useCallback(async (avatarName) => {
    // Prevenir cargas múltiples simultáneas
    if (isChangingAvatarRef.current) {
      console.log('⚠️ Ya hay un cambio de avatar en proceso');
      return;
    }

    isChangingAvatarRef.current = true;

    try {
      // Verificar caché global primero
      if (avatarCache.has(avatarName)) {
        console.log(`⚡ Usando avatar en caché: ${avatarName}`);
        
        await executeAfterInteractions(() => {
          // Remover avatar actual de la escena
          const previousAvatar = sceneRef.current.getObjectByName('currentAvatar');
          if (previousAvatar && previousAvatar.userData.avatarName !== avatarName) {
            sceneRef.current.remove(previousAvatar);
          }
          
          // Añadir avatar desde caché
          const cachedAvatarData = avatarCache.get(avatarName);
          cachedAvatarData.model.name = 'currentAvatar';
          cachedAvatarData.model.userData.avatarName = avatarName;
          sceneRef.current.add(cachedAvatarData.model);
          
          // Crear nuevo animator con los datos en caché
          animatorRef.current = new SignAnimator(cachedAvatarData, THREE);
          setupAnimatorCallbacks();
        });
        
        console.log(`✅ Avatar ${avatarName} cargado desde caché`);
        isChangingAvatarRef.current = false;
        return;
      }
      
      setIsLoading(true);
      setLoadingProgress(0);
      console.log(`🔄 Cargando avatar: ${avatarName}`);

      // Cargar modelo base (sin bloquear UI)
      const avatarData = await loaderRef.current.loadAvatar(
        avatarName,
        (progress) => {
          setLoadingProgress(Math.round(progress));
        }
      );

      // Guardar en caché global
      avatarCache.set(avatarName, avatarData);
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

      // Añadir metadata al modelo
      avatarData.model.userData.avatarName = avatarName;

      // Cargar animaciones esenciales de forma no bloqueante
      executeAfterInteractions(() => {
        loadCommonAnimations(avatarName);
      });

      console.log(`✅ Avatar ${avatarName} cargado exitosamente`);

    } catch (error) {
      console.error('❌ Error cargando avatar:', error);
      Alert.alert('Error', `No se pudo cargar el avatar ${avatarName}`);
    } finally {
      setIsLoading(false);
      isChangingAvatarRef.current = false;
    }
  }, [translationResult]);

  // Configurar callbacks del animator (extraído para reutilizar)
  const setupAnimatorCallbacks = useCallback(() => {
    if (!animatorRef.current) return;

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
  }, [translationResult]);

  // Cargar animaciones comunes con lazy loading
  const loadCommonAnimations = useCallback(async (avatarName) => {
    const essentialAnimations = [
      'hola', 'adios', 'gracias', 'buenos_dias', 'buenas_tardes'
    ];
    
    const secondaryAnimations = [
      'como_estas', 'mi', 'nombre', 'yo', 'tu', 'el', 'ella',
      'hoy', 'ayer', 'manana', 'lunes', 'martes', 'miercoles'
    ];

    try {
      // Cargar esenciales primero (rápido)
      console.log(`⚡ Cargando animaciones esenciales para ${avatarName}`);
      await batchAnimationLoader.loadBatch(
        avatarName,
        essentialAnimations,
        loaderRef.current,
        (progress) => setLoadingProgress(Math.round(progress * 50))
      );

      // Cargar secundarias en background (lazy)
      lazyAnimationLoader.preloadAnimations(
        avatarName,
        secondaryAnimations,
        loaderRef.current,
        (progress) => setLoadingProgress(50 + Math.round(progress * 30))
      );

      // Alfabeto se cargará bajo demanda (no precarga)
      console.log(`✅ Sistema de carga configurado para ${avatarName}`);
    } catch (error) {
      console.warn('⚠️ Error precargando animaciones:', error);
    }
  }, []);

  // ============= LOOP DE RENDERIZADO (OPTIMIZADO) =============
  const startRenderLoop = () => {
    const render = () => {
      animationFrameRef.current = requestAnimationFrame(render);

      // Control de FPS optimizado
      if (!renderOptimizerRef.current.shouldRender()) {
        return;
      }

      const delta = clockRef.current.getDelta();

      // Actualizar animator solo si hay animaciones activas
      if (animatorRef.current && isPlaying) {
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
  // ============= TRADUCCIÓN (OPTIMIZADA) =============
  const handleTranslate = useCallback(
    debounce(async () => {
      if (!inputText.trim()) {
        Alert.alert('Atención', 'Por favor ingresa un texto para traducir');
        return;
      }

      console.log(`📝 Traduciendo: "${inputText}"`);

      setIsOptimizing(true);
      setOptimizationResult(null);
      
      // Ejecutar traducción sin bloquear UI
      await executeAfterInteractions(async () => {
        try {
          // OPTIMIZACIÓN: Procesar traducción local INMEDIATAMENTE (no esperar API)
          const animationsLocal = translatorRef.current.translate(inputText, {
            spellUnknownWords: true,
            includeIdle: false,
            maxSpellingLength: 10
          });

          if (animationsLocal.length === 0) {
            Alert.alert('Error', 'No se pudo traducir el texto');
            setIsOptimizing(false);
            return;
          }

          // Mostrar resultado local INMEDIATAMENTE
          setTranslationResult(animationsLocal);
          console.log(`⚡ Traducción local rápida: ${animationsLocal.length} animaciones`);
          
          // Cargar las animaciones necesarias
          await loadAnimationsForTranslation(animationsLocal);
          
          // Intentar optimizar con IA en paralelo (con timeout de 3 segundos)
          const result = await apiService.optimizarTexto(inputText, 3000);
          
          if (result.success) {
            setOptimizationResult(result.data);
            
            // Usar texto LSV optimizado si es diferente
            const textoAUsar = result.data.textoLSV || result.data.textoCorregido;
            console.log(`✨ Optimizado por IA: "${textoAUsar}"`);
            
            // Si el texto optimizado es diferente, re-traducir
            if (textoAUsar.toLowerCase() !== inputText.toLowerCase()) {
              const animationsOptimized = translatorRef.current.translate(textoAUsar, {
                spellUnknownWords: true,
                includeIdle: false,
                maxSpellingLength: 10
              });

              if (animationsOptimized.length > 0) {
                setTranslationResult(animationsOptimized);
                console.log(`✅ Traducción optimizada: ${animationsOptimized.length} animaciones`);
                
                // Recargar animaciones si el texto cambió
                await loadAnimationsForTranslation(animationsOptimized);
              }
            }
            
            // Mostrar info si hubo corrección (solo si no viene de caché)
            if (result.data.textoCorregido && result.data.textoCorregido !== inputText && !result.fromCache) {
              setTimeout(() => {
                Alert.alert(
                  '✨ Texto Optimizado por IA',
                  `Original: "${inputText}"\nOptimizado: "${textoAUsar}"\nCobertura: ${(result.data.porcentajeCobertura || 0).toFixed(1)}%`,
                  [{ text: 'OK' }]
                );
              }, 300);
            }
          } else {
            // API no disponible o timeout - ya tenemos la traducción local
            if (result.isTimeout) {
              console.log('⏱️ API timeout - usando traducción local (ya mostrada)');
            } else {
              console.warn('⚠️ API no disponible - usando traducción local');
            }
          }
        } catch (error) {
          console.error('❌ Error en traducción:', error);
          
          // Intentar traducción de emergencia si no hay resultado
          if (translationResult.length === 0) {
            const emergencyTranslation = translatorRef.current.translate(inputText, {
              spellUnknownWords: true,
              includeIdle: false,
              maxSpellingLength: 10
            });
            
            if (emergencyTranslation.length > 0) {
              setTranslationResult(emergencyTranslation);
            } else {
              Alert.alert('Error', 'Hubo un problema al traducir');
            }
          }
        } finally {
          setIsOptimizing(false);
        }
      });
    }, 300), // Debounce de 300ms
    [inputText, translationResult]
  );

  // Cargar animaciones necesarias para la traducción
  const loadAnimationsForTranslation = useCallback(async (animationNames) => {
    if (!loaderRef.current || animationNames.length === 0) return;
    
    setLoadingAnimations(true);
    setAnimationsReady(false);
    
    try {
      console.log(`🎬 Cargando ${animationNames.length} animaciones...`);
      
      // Filtrar animaciones ya cargadas
      const loadedAnims = loaderRef.current.getLoadedAnimations(selectedAvatar);
      const animsToLoad = animationNames.filter(name => !loadedAnims.includes(name));
      
      if (animsToLoad.length > 0) {
        console.log(`📥 Faltan ${animsToLoad.length} animaciones por cargar`);
        await loaderRef.current.loadAnimations(
          selectedAvatar,
          animsToLoad,
          (progress) => {
            console.log(`📊 Progreso carga: ${progress.toFixed(0)}%`);
          }
        );
      } else {
        console.log(`✅ Todas las animaciones ya están en caché`);
      }
      
      setAnimationsReady(true);
      console.log(`✅ Animaciones listas para reproducir`);
    } catch (error) {
      console.error('❌ Error cargando animaciones:', error);
      Alert.alert('Error', 'Algunas animaciones no se pudieron cargar');
      setAnimationsReady(true); // Permitir reproducir las que sí cargaron
    } finally {
      setLoadingAnimations(false);
    }
  }, [selectedAvatar]);

  const handlePlay = () => {
    if (!animatorRef.current || translationResult.length === 0) {
      Alert.alert('Error', 'Primero debes traducir un texto');
      return;
    }
    
    if (!animationsReady) {
      Alert.alert('Espera', 'Las animaciones aún se están cargando...');
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
    setAnimationsReady(false);
    await loadAvatar(avatarName);
    
    // Recargar animaciones si hay una traducción activa
    if (translationResult.length > 0) {
      await loadAnimationsForTranslation(translationResult);
    }
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
                <>
                  <ActivityIndicator color="white" size="small" />
                  <Text style={[styles.translateBtnText, { marginLeft: 8 }]}>Traduciendo...</Text>
                </>
              ) : (
                <Text style={styles.translateBtnText}>🚀 Traducir</Text>
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
              style={[
                styles.controlBtn,
                (!animationsReady || isPlaying || loadingAnimations) && styles.controlBtnDisabled
              ]}
              onPress={handlePlay}
              disabled={!animationsReady || isPlaying || loadingAnimations}
            >
              <Text style={styles.controlBtnText}>
                {loadingAnimations ? '⏳' : '▶'}
              </Text>
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
    flexDirection: 'row',
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
  controlBtnDisabled: {
    backgroundColor: 'rgba(100, 100, 100, 0.2)',
    borderColor: 'rgba(100, 100, 100, 0.3)',
    opacity: 0.5,
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
