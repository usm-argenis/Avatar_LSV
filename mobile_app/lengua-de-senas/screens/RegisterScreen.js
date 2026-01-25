import React, { useState } from 'react';
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
  ImageBackground,
  StatusBar,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { SafeAreaView } from 'react-native-safe-area-context';
import { register } from '../services/authService';

export default function RegisterScreen({ navigation }) {
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  const handleRegister = async () => {
    // Validaciones
    if (!fullName || !email || !password || !confirmPassword) {
      Alert.alert('Error', 'Por favor completa todos los campos');
      return;
    }

    if (!validateEmail(email)) {
      Alert.alert('Error', 'Por favor ingresa un correo electrónico válido');
      return;
    }

    if (password.length < 6) {
      Alert.alert('Error', 'La contraseña debe tener al menos 6 caracteres');
      return;
    }

    if (password !== confirmPassword) {
      Alert.alert('Error', 'Las contraseñas no coinciden');
      return;
    }

    setLoading(true);

    try {
      const response = await register(fullName.trim(), email.trim(), password);

      if (response.success) {
        // Registro exitoso
        console.log('✅ Registro exitoso:', response.data);
        Alert.alert(
          '¡Bienvenido a VeneSeñas!',
          `Cuenta creada exitosamente. ¡Comienza a aprender LSV!`,
          [
            {
              text: 'Continuar',
              onPress: () => navigation.replace('Main'),
            },
          ]
        );
      } else {
        Alert.alert('Error', response.mensaje || 'No se pudo crear la cuenta');
      }
    } catch (error) {
      console.error('❌ Error en registro:', error);
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
            {/* Botón Volver - Fuera del card */}
            <TouchableOpacity style={styles.backButton} onPress={() => navigation.goBack()}>
              <Ionicons name="arrow-back" size={24} color="#2196F3" />
              <Text style={styles.backText}>Volver</Text>
            </TouchableOpacity>

            {/* Logo VeneSeñas - Fuera del card */}
            <View style={styles.logoContainer}>
              <Image
                source={require('../assets/logo-venesenas.png')}
                style={styles.logoImage}
                resizeMode="contain"
              />
            </View>

            {/* Título - Fuera del card */}
            <Text style={styles.title}>¡Únete a VeneSeñas!</Text>
            
            {/* Estrellas decorativas - Fuera del card */}
            <View style={styles.starsContainer}>
              <Ionicons name="star" size={24} color="#f3e521"/>
              <Ionicons name="star" size={24} color="#2196F3" />
              <Ionicons name="star" size={24} color="#f32121" />
            </View>

          <View style={styles.card}>
            {/* Formulario */}
            <View style={styles.form}>
              {/* Nombre completo */}
              <View style={styles.labelContainer}>
                <Ionicons name="person-outline" size={18} color="#2196F3" />
                <Text style={styles.label}>Nombre Completo</Text>
              </View>
              <View style={styles.inputContainer}>
                <TextInput
                  style={styles.input}
                  placeholder="Tu nombre completo"
                  placeholderTextColor="#999"
                  value={fullName}
                  onChangeText={setFullName}
                  autoComplete="name"
                />
              </View>

              {/* Email */}
              <View style={styles.labelContainer}>
                <Ionicons name="mail-outline" size={18} color="#2196F3" />
                <Text style={styles.label}>Correo Electrónico</Text>
              </View>
              <View style={styles.inputContainer}>
                <TextInput
                  style={styles.input}
                  placeholder="tucorreo@ejemplo.com"
                  placeholderTextColor="#999"
                  value={email}
                  onChangeText={setEmail}
                  keyboardType="email-address"
                  autoCapitalize="none"
                  autoComplete="email"
                />
              </View>

              {/* Contraseña */}
              <View style={styles.labelContainer}>
                <Ionicons name="lock-closed-outline" size={18} color="#2196F3" />
                <Text style={styles.label}>Contraseña</Text>
              </View>
              <View style={styles.inputContainer}>
                <TextInput
                  style={styles.input}
                  placeholder="Mínimo 6 caracteres"
                  placeholderTextColor="#999"
                  value={password}
                  onChangeText={setPassword}
                  secureTextEntry={!showPassword}
                  autoComplete="password-new"
                />
                <TouchableOpacity
                  onPress={() => setShowPassword(!showPassword)}
                  style={styles.eyeButton}
                >
                  <Ionicons
                    name={showPassword ? 'eye-off-outline' : 'eye-outline'}
                    size={20}
                    color="#999"
                  />
                </TouchableOpacity>
              </View>

              {/* Confirmar Contraseña */}
              <View style={styles.labelContainer}>
                <Ionicons name="lock-closed-outline" size={18} color="#2196F3" />
                <Text style={styles.label}>Confirmar Contraseña</Text>
              </View>
              <View style={styles.inputContainer}>
                <TextInput
                  style={styles.input}
                  placeholder="Confirma tu contraseña"
                  placeholderTextColor="#999"
                  value={confirmPassword}
                  onChangeText={setConfirmPassword}
                  secureTextEntry={!showConfirmPassword}
                  autoComplete="password-new"
                />
                <TouchableOpacity
                  onPress={() => setShowConfirmPassword(!showConfirmPassword)}
                  style={styles.eyeButton}
                >
                  <Ionicons
                    name={showConfirmPassword ? 'eye-off-outline' : 'eye-outline'}
                    size={20}
                    color="#999"
                  />
                </TouchableOpacity>
              </View>

              {/* Botón Registrarse */}
              <TouchableOpacity
                style={[styles.button, loading && styles.buttonDisabled]}
                onPress={handleRegister}
                disabled={loading}
              >
                {loading ? (
                  <ActivityIndicator color="#FFFFFF" />
                ) : (
                  <>
                    <Ionicons name="person-add" size={20} color="#FFFFFF" style={styles.buttonIcon} />
                    <Text style={styles.buttonText}>Crear Cuenta</Text>
                  </>
                )}
              </TouchableOpacity>
            </View>
          </View>

          {/* Footer con corazón venezolano - Fuera del card */}
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
    padding: 20,
    paddingTop: 20,
    paddingBottom: 10,
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
  backButton: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 0,
    gap: 8,
  },
  backText: {
    fontSize: 16,
    color: '#2196F3',
    fontWeight: '600',
  },
  logoContainer: {
    alignItems: 'center',
    marginBottom: 4,
  },
  logoImage: {
    width: 120,
    height: 120,
  },
  title: {
    fontSize: 26,
    fontWeight: 'bold',
    color: '#DC143C',
    textAlign: 'center',
    marginBottom: 6,
  },
  subtitle: {
    fontSize: 14,
    color: '#666',
    textAlign: 'center',
    marginBottom: 12,
  },
  starsContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: 8,
    marginBottom: 20,
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
    backgroundColor: '#f5f5f5',
    borderRadius: 12,
    paddingHorizontal: 16,
    height: 40,
    marginBottom: 14,
    borderWidth: 1,
    borderColor: '#E0E0E0',
  },
  inputIcon: {
    marginRight: 10,
  },
  input: {
    flex: 1,
    fontSize: 15,
    color: 'z#333',
  },
  eyeButton: {
    padding: 4,
  },
  button: {
    backgroundColor: '#DC143C',
    borderRadius: 12,
    height: 52,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 8,
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
  buttonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
  footerContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 16,
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
    top: 200,
    right: 40,
  },
  starBg3: {
    position: 'absolute',
    bottom: 30,
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
