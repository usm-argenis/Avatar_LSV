import React, { useState, useEffect } from 'react';
import {
  StyleSheet,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
  KeyboardAvoidingView,
  Platform,
  ScrollView,
  Image,
  Dimensions,
  ImageBackground,
  StatusBar,
} from 'react-native';
import { Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';
import AsyncStorage from '@react-native-async-storage/async-storage';
import * as LocalAuthentication from 'expo-local-authentication';
import { SafeAreaView } from 'react-native-safe-area-context';
import { login } from '../services/authService';

const { width, height } = Dimensions.get('window');

export default function LoginScreen({ navigation }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [isBiometricSupported, setIsBiometricSupported] = useState(false);
  const [hasSavedCredentials, setHasSavedCredentials] = useState(false);

  useEffect(() => {
    checkBiometricSupport();
    checkSavedCredentials();
  }, []);

  const checkBiometricSupport = async () => {
    const compatible = await LocalAuthentication.hasHardwareAsync();
    const enrolled = await LocalAuthentication.isEnrolledAsync();
    setIsBiometricSupported(compatible && enrolled);
  };

  const checkSavedCredentials = async () => {
    try {
      const savedEmail = await AsyncStorage.getItem('userEmail');
      setHasSavedCredentials(!!savedEmail);
      if (savedEmail) {
        setEmail(savedEmail);
      }
    } catch (error) {
      console.error('Error checking saved credentials:', error);
    }
  };

  const handleFingerprintLogin = async () => {
    if (!hasSavedCredentials) {
      Alert.alert(
        'Configuración requerida',
        'Primero debes iniciar sesión con tu usuario y contraseña para guardar tus credenciales.'
      );
      return;
    }

    try {
      setLoading(true);
      const result = await LocalAuthentication.authenticateAsync({
        promptMessage: 'Inicia sesión con tu huella',
        fallbackLabel: 'Usar contraseña',
        disableDeviceFallback: false,
      });

      if (result.success) {
        setTimeout(() => {
          setLoading(false);
          navigation.replace('Main');
        }, 300);
      } else {
        setLoading(false);
        Alert.alert('Error', 'Autenticación fallida');
      }
    } catch (error) {
      setLoading(false);
      Alert.alert('Error', 'No se pudo autenticar con huella');
    }
  };

  const handleLogin = async () => {
    if (!email || email.trim().length === 0) {
      Alert.alert('Error', 'Por favor ingresa tu correo electrónico');
      return;
    }

    if (!password || password.trim().length === 0) {
      Alert.alert('Error', 'Por favor ingresa tu contraseña');
      return;
    }

    setLoading(true);

    try {
      const response = await login(email.trim(), password);

      if (response.success) {
        // Login exitoso - Guardar credenciales para biometría
        console.log('✅ Login exitoso:', response.data);
        
        // Guardar email para futuras autenticaciones biométricas
        await AsyncStorage.setItem('userEmail', email.trim());
        await AsyncStorage.setItem('hasLoggedInBefore', 'true');
        setHasSavedCredentials(true);
        
        Alert.alert('¡Bienvenido!', `Hola ${response.data.user.full_name}`, [
          {
            text: 'Continuar',
            onPress: () => navigation.replace('Main')
          }
        ]);
      } else {
        Alert.alert('Error', response.mensaje || 'Credenciales incorrectas');
      }
    } catch (error) {
      console.error('❌ Error en login:', error);
      Alert.alert('Error', 'Error de conexión. Verifica que el servidor esté corriendo.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
      <StatusBar barStyle="dark-content" translucent={false} />
      <View style={styles.container}>
        <KeyboardAvoidingView
          behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
          style={styles.keyboardView}
        >
          <View style={styles.scrollContent}>
            {/* Logo VeneSeñas - Fuera del card */}
            <View style={styles.logoContainer}>
              <Image
                source={require('../assets/logo-venesenas.png')}
                style={styles.logoImage}
                resizeMode="contain"
              />
            </View>

            {/* Título y subtítulo - Fuera del card */}
            <Text style={styles.welcomeTitle}>¡Bienvenido!</Text>
            <Text style={styles.subtitle}>Inicia sesión para ver tu perfil</Text>

            {/* Estrellas decorativas - Fuera del card */}
            <View style={styles.starsContainer}>
              <Ionicons name="star" size={22} color="#f3e521" />
              <Ionicons name="star" size={22} color="#2196F3" />
              <Ionicons name="star" size={22} color="#f32121" />
            </View>

          <View style={styles.card}>
            {/* Formulario */}
            <View style={styles.form}>
              {/* Label Correo Electrónico */}
              <View style={styles.labelContainer}>
                <Ionicons name="person-outline" size={18} color="#2196F3" />
                <Text style={styles.label}>Correo Electrónico</Text>
              </View>

              {/* Input Correo */}
              <View style={styles.inputContainer}>
                <TextInput
                  style={styles.input}
                  placeholder="tucorreo@ejemplo.com"
                  placeholderTextColor="#999"
                  value={email}
                  onChangeText={setEmail}
                  autoCapitalize="none"
                  keyboardType="email-address"
                />
              </View>

              {/* Label Contraseña */}
              <View style={styles.labelContainer}>
                <Ionicons name="lock-closed-outline" size={18} color="#2196F3" />
                <Text style={styles.label}>Contraseña</Text>
              </View>

              {/* Input Contraseña */}
              <View style={styles.inputContainer}>
                <TextInput
                  style={styles.input}
                  placeholder="••••••••"
                  placeholderTextColor="#999"
                  value={password}
                  onChangeText={setPassword}
                  secureTextEntry={!showPassword}
                />
                <TouchableOpacity onPress={() => setShowPassword(!showPassword)} style={styles.eyeButton}>
                  <Ionicons
                    name={showPassword ? 'eye-off-outline' : 'eye-outline'}
                    size={20}
                    color="#999"
                  />
                </TouchableOpacity>
              </View>

              {/* Link Olvidaste contraseña */}
              <TouchableOpacity 
                style={styles.forgotPasswordButton}
                onPress={() => Alert.alert('Recuperar contraseña', 'Esta función estará disponible próximamente')}
              >
                <Text style={styles.forgotPasswordText}>¿Olvidaste tu contraseña?</Text>
              </TouchableOpacity>

              {/* Botones Iniciar Sesión */}
              <View style={styles.loginButtonsContainer}>
                {/* Botón Iniciar Sesión Normal */}
                <TouchableOpacity
                  style={[styles.loginButton, loading && styles.buttonDisabled]}
                  onPress={handleLogin}
                  disabled={loading}
                >
                  {loading ? (
                    <ActivityIndicator color="#FFFFFF" />
                  ) : (
                    <>
                      <Ionicons name="arrow-forward" size={20} color="#FFFFFF" style={styles.buttonIcon} />
                      <Text style={styles.loginButtonText}>Iniciar Sesión</Text>
                    </>
                  )}
                </TouchableOpacity>

                {/* Botón Huella Digital */}
                {isBiometricSupported && (
                  <TouchableOpacity
                    style={[styles.fingerprintButton, loading && styles.buttonDisabled]}
                    onPress={handleFingerprintLogin}
                    disabled={loading}
                  >
                    {loading ? (
                      <ActivityIndicator color="#2196F3" />
                    ) : (
                      <MaterialCommunityIcons name="fingerprint" size={32} color="#2196F3" />
                    )}
                  </TouchableOpacity>
                )}
              </View>

              {/* Separador con punto 
              <View style={styles.dividerContainer}>
                <View style={styles.dotSeparator} />
              </View>*/}

              {/* Texto ¿No tienes una cuenta? */}
              <View style={styles.registerContainer}>
                <Text style={styles.registerText}>¿No tienes una cuenta?</Text>
              </View>

              {/* Botón Crear Cuenta */}
              <TouchableOpacity
                style={styles.registerButton}
                onPress={() => navigation.navigate('Register')}
              >
                <Text style={styles.registerButtonText}>Crear Cuenta</Text>
              </TouchableOpacity>
            </View>
          </View>

          {/* Footer con líneas venezolanas - Fuera del card */}
          <View style={styles.footerContainer}>
            <Text style={styles.footerText}>Hecho con </Text>
            <Ionicons name="heart" size={14} color="#DC143C" />
            <Text style={styles.footerText}> para tod@s los venezolanos</Text>
          </View>
          <View style={styles.flagContainer}>
            <View style={styles.blueLine} />
            <View style={styles.starsFooter}>
              <Ionicons name="star" size={12} color="#f3e521" />
              <Ionicons name="star" size={12} color="#2196F3" />
              <Ionicons name="star" size={12} color="#f32121" />
            </View>
            <View style={styles.redLine} />
          </View>

          {/* Estrellas decorativas de fondo */}
          <Ionicons name="star" size={30} color="rgba(255, 217, 0, 0.32)" style={styles.starBg1} />
          <Ionicons name="star" size={25} color="rgba(255, 217, 0, 0.32)" style={styles.starBg2} />
          <Ionicons name="star" size={35} color="rgba(255, 217, 0, 0.32)" style={styles.starBg3} />
          <Ionicons name="star" size={20} color="rgba(255, 217, 0, 0.32)" style={styles.starBg4} />
          <Ionicons name="star" size={28} color="rgba(255, 217, 0, 0.32)" style={styles.starBg5} />
        </View>
      </KeyboardAvoidingView>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  container: {
    flex: 1,
  },
  keyboardView: {
    flex: 1,
  },
  scrollContent: {
    flex: 1,
    justifyContent: 'flex-start',
    padding: 20,
    paddingTop: 30,
    paddingBottom: 10,
  },
  logoContainer: {
    alignItems: 'center',
    marginBottom: 5,
  },
  card: {
    backgroundColor: 'rgba(255, 255, 255, 0.95)',
    borderRadius: 24,
    padding: 30,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.15,
    shadowRadius: 16,
    elevation: 8,
  },
  logoImage: {
    width: 120,
    height: 120,
  },
  welcomeTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#2196F3',
    textAlign: 'center',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 15,
    color: '#666',
    textAlign: 'center',
    marginBottom: 12,
  },
  starsContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: 8,
    marginBottom: 24,
  },
  form: {
    width: '100%',
  },
  labelContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 7,
    marginLeft: 4,
    gap: 6,
  },
  label: {
    fontSize: 15,
    color: '#2196F3',
    fontWeight: '600',
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F5F5F5',
    borderRadius: 12,
    paddingHorizontal: 16,
    height: 40,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#E0E0E0',
  },
  inputIcon: {
    marginRight: 10,
  },
  input: {
    flex: 1,
    fontSize: 15,
    color: '#333',
  },
  eyeButton: {
    padding: 4,
  },
  forgotPasswordText: {
    color: '#DC143C',
    fontSize: 13,
    textAlign: 'right',
    fontWeight: '500',
  },
  forgotPasswordButton: {
    marginBottom: 20,
    alignItems: 'flex-end',
  },
  loginButtonsContainer: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 16,
  },
  loginButton: {
    flex: 1,
    backgroundColor: '#2196F3',
    borderRadius: 12,
    height: 45,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 8,
    elevation: 6,
  },
  fingerprintButton: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    width: 60,
    height: 45,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 2,
    borderColor: '#2196F3',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 8,
    elevation: 6,
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  buttonIcon: {
    marginRight: 8,
  },
  loginButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
  dividerContainer: {
    alignItems: 'center',
    marginVertical: 5,
  },
  dotSeparator: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: '#000000',
  },
  registerContainer: {
    alignItems: 'center',
    marginBottom: 19,
    marginTop: 5,
  },
  registerText: {
    fontSize: 14,
    color: '#666',
  },
  registerButton: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    height: 45,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 2,
    borderColor: '#DC143C',
  },
  registerButtonText: {
    color: '#DC143C',
    fontSize: 16,
    fontWeight: 'bold',
  },
  footerContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 19,
    flexWrap: 'wrap',
  },
  footerText: {
    fontSize: 11,
    color: '#666',
    textAlign: 'center',
  },
  flagContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 8,
    marginBottom: 10,
    gap: 6,
  },
  blueLine: {
    flex: 1,
    height: 3,
    backgroundColor: '#000000',
  },
  redLine: {
    flex: 1,
    height: 3,
    backgroundColor: '#000000',
  },
  starsFooter: {
    flexDirection: 'row',
    gap: 3,
  },
starBg1: {
    position: 'absolute',
    top: 100,
    left: 30,
  },
  starBg2: {
    position: 'absolute',
    top: 230,
    right: 40,
  },
  starBg3: {
    position: 'absolute',
    bottom: 27,
    left: 10,
  },
  starBg4: {
    position: 'absolute',
    top: 40,
    right: 60,
  },
  starBg5: {
    position: 'absolute',
    bottom: 30,
    right: 10,
  },
});
