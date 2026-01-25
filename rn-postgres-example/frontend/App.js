// ============================================
// FRONTEND - React Native App
// ============================================
// Aplicación React Native que conecta con backend Node.js/PostgreSQL
// Permite gestionar usuarios: listar, crear, actualizar y eliminar

import React, { useState, useEffect } from 'react';
import {
  SafeAreaView,
  ScrollView,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  Alert,
  ActivityIndicator,
  RefreshControl
} from 'react-native';
import axios from 'axios';

// ============================================
// CONFIGURACIÓN DE LA URL DEL BACKEND
// ============================================
// ⚠️ IMPORTANTE: Cambia esta URL según tu entorno

// Para EMULADOR ANDROID: usa 10.0.2.2 (localhost del emulador)
// const API_URL = 'http://10.0.2.2:3000';

// Para EMULADOR iOS: usa localhost directamente
// const API_URL = 'http://localhost:3000';

// Para DISPOSITIVO FÍSICO: usa la IP de tu computadora en la red local
// Ejemplo: const API_URL = 'http://192.168.1.100:3000';
// Para encontrar tu IP: Windows -> cmd -> ipconfig (buscar IPv4)

const API_URL = 'http://10.0.2.2:3000'; // Por defecto para Android

// ============================================
// COMPONENTE PRINCIPAL
// ============================================
export default function App() {
  // ============================================
  // ESTADOS DE LA APLICACIÓN
  // ============================================
  const [usuarios, setUsuarios] = useState([]); // Lista de usuarios
  const [loading, setLoading] = useState(false); // Estado de carga
  const [refreshing, setRefreshing] = useState(false); // Estado de refresh
  
  // Estados para el formulario de crear/actualizar
  const [nombre, setNombre] = useState('');
  const [email, setEmail] = useState('');
  const [editandoId, setEditandoId] = useState(null); // ID del usuario en edición

  // ============================================
  // useEffect - Cargar usuarios al iniciar
  // ============================================
  useEffect(() => {
    cargarUsuarios();
  }, []);

  // ============================================
  // FUNCIÓN 1: CARGAR TODOS LOS USUARIOS
  // ============================================
  // Hace una petición GET al backend para obtener todos los usuarios
  const cargarUsuarios = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_URL}/usuarios`);
      
      if (response.data.success) {
        setUsuarios(response.data.data);
        console.log('✅ Usuarios cargados:', response.data.count);
      }
    } catch (error) {
      console.error('❌ Error al cargar usuarios:', error);
      Alert.alert(
        'Error',
        'No se pudieron cargar los usuarios. Verifica que el backend esté corriendo.'
      );
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  // ============================================
  // FUNCIÓN 2: CREAR O ACTUALIZAR USUARIO
  // ============================================
  const guardarUsuario = async () => {
    // Validar que los campos no estén vacíos
    if (!nombre.trim() || !email.trim()) {
      Alert.alert('Error', 'Por favor completa todos los campos');
      return;
    }

    // Validar formato de email básico
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      Alert.alert('Error', 'Por favor ingresa un email válido');
      return;
    }

    try {
      if (editandoId) {
        // ACTUALIZAR usuario existente
        const response = await axios.put(
          `${API_URL}/usuarios/${editandoId}`,
          { nombre, email }
        );

        if (response.data.success) {
          Alert.alert('Éxito', 'Usuario actualizado correctamente');
          limpiarFormulario();
          cargarUsuarios();
        }
      } else {
        // CREAR nuevo usuario
        const response = await axios.post(
          `${API_URL}/usuarios`,
          { nombre, email }
        );

        if (response.data.success) {
          Alert.alert('Éxito', 'Usuario creado correctamente');
          limpiarFormulario();
          cargarUsuarios();
        }
      }
    } catch (error) {
      console.error('❌ Error al guardar usuario:', error);
      Alert.alert(
        'Error',
        error.response?.data?.mensaje || 'No se pudo guardar el usuario'
      );
    }
  };

  // ============================================
  // FUNCIÓN 3: EDITAR USUARIO
  // ============================================
  // Prepara el formulario para editar un usuario existente
  const editarUsuario = (usuario) => {
    setNombre(usuario.nombre);
    setEmail(usuario.email);
    setEditandoId(usuario.id);
  };

  // ============================================
  // FUNCIÓN 4: ELIMINAR USUARIO
  // ============================================
  const eliminarUsuario = async (id) => {
    Alert.alert(
      'Confirmar',
      '¿Estás seguro de eliminar este usuario?',
      [
        { text: 'Cancelar', style: 'cancel' },
        {
          text: 'Eliminar',
          style: 'destructive',
          onPress: async () => {
            try {
              const response = await axios.delete(`${API_URL}/usuarios/${id}`);

              if (response.data.success) {
                Alert.alert('Éxito', 'Usuario eliminado correctamente');
                cargarUsuarios();
              }
            } catch (error) {
              console.error('❌ Error al eliminar usuario:', error);
              Alert.alert('Error', 'No se pudo eliminar el usuario');
            }
          }
        }
      ]
    );
  };

  // ============================================
  // FUNCIÓN 5: LIMPIAR FORMULARIO
  // ============================================
  const limpiarFormulario = () => {
    setNombre('');
    setEmail('');
    setEditandoId(null);
  };

  // ============================================
  // FUNCIÓN 6: REFRESH PULL-TO-REFRESH
  // ============================================
  const onRefresh = () => {
    setRefreshing(true);
    cargarUsuarios();
  };

  // ============================================
  // RENDERIZADO DE LA INTERFAZ
  // ============================================
  return (
    <SafeAreaView style={styles.container}>
      {/* HEADER */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>👥 Gestión de Usuarios</Text>
        <Text style={styles.headerSubtitle}>
          PostgreSQL + Node.js + React Native
        </Text>
      </View>

      <ScrollView
        style={styles.scrollView}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
        }
      >
        {/* FORMULARIO DE CREAR/ACTUALIZAR */}
        <View style={styles.formContainer}>
          <Text style={styles.sectionTitle}>
            {editandoId ? '✏️ Editar Usuario' : '➕ Nuevo Usuario'}
          </Text>

          <TextInput
            style={styles.input}
            placeholder="Nombre completo"
            value={nombre}
            onChangeText={setNombre}
            placeholderTextColor="#999"
          />

          <TextInput
            style={styles.input}
            placeholder="Email"
            value={email}
            onChangeText={setEmail}
            keyboardType="email-address"
            autoCapitalize="none"
            placeholderTextColor="#999"
          />

          <View style={styles.buttonRow}>
            <TouchableOpacity
              style={[styles.button, styles.buttonPrimary]}
              onPress={guardarUsuario}
            >
              <Text style={styles.buttonText}>
                {editandoId ? '💾 Actualizar' : '✅ Guardar'}
              </Text>
            </TouchableOpacity>

            {editandoId && (
              <TouchableOpacity
                style={[styles.button, styles.buttonSecondary]}
                onPress={limpiarFormulario}
              >
                <Text style={styles.buttonText}>❌ Cancelar</Text>
              </TouchableOpacity>
            )}
          </View>
        </View>

        {/* LISTA DE USUARIOS */}
        <View style={styles.listContainer}>
          <Text style={styles.sectionTitle}>
            📋 Usuarios ({usuarios.length})
          </Text>

          {loading ? (
            <ActivityIndicator size="large" color="#007AFF" />
          ) : usuarios.length === 0 ? (
            <Text style={styles.emptyText}>
              No hay usuarios. ¡Crea el primero!
            </Text>
          ) : (
            usuarios.map((usuario) => (
              <View key={usuario.id} style={styles.userCard}>
                <View style={styles.userInfo}>
                  <Text style={styles.userName}>{usuario.nombre}</Text>
                  <Text style={styles.userEmail}>{usuario.email}</Text>
                  <Text style={styles.userId}>ID: {usuario.id}</Text>
                </View>

                <View style={styles.userActions}>
                  <TouchableOpacity
                    style={[styles.actionButton, styles.editButton]}
                    onPress={() => editarUsuario(usuario)}
                  >
                    <Text style={styles.actionButtonText}>✏️</Text>
                  </TouchableOpacity>

                  <TouchableOpacity
                    style={[styles.actionButton, styles.deleteButton]}
                    onPress={() => eliminarUsuario(usuario.id)}
                  >
                    <Text style={styles.actionButtonText}>🗑️</Text>
                  </TouchableOpacity>
                </View>
              </View>
            ))
          )}
        </View>

        {/* FOOTER CON INFO */}
        <View style={styles.footer}>
          <Text style={styles.footerText}>
            🔗 Backend: {API_URL}
          </Text>
          <TouchableOpacity onPress={cargarUsuarios}>
            <Text style={styles.refreshText}>🔄 Recargar datos</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

// ============================================
// ESTILOS
// ============================================
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    backgroundColor: '#007AFF',
    padding: 20,
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 5,
  },
  headerSubtitle: {
    fontSize: 12,
    color: '#fff',
    opacity: 0.9,
  },
  scrollView: {
    flex: 1,
  },
  formContainer: {
    backgroundColor: '#fff',
    margin: 15,
    padding: 20,
    borderRadius: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 15,
    color: '#333',
  },
  input: {
    backgroundColor: '#f9f9f9',
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    padding: 12,
    marginBottom: 12,
    fontSize: 16,
    color: '#333',
  },
  buttonRow: {
    flexDirection: 'row',
    gap: 10,
  },
  button: {
    flex: 1,
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
  },
  buttonPrimary: {
    backgroundColor: '#007AFF',
  },
  buttonSecondary: {
    backgroundColor: '#FF3B30',
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  listContainer: {
    backgroundColor: '#fff',
    margin: 15,
    padding: 20,
    borderRadius: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  emptyText: {
    textAlign: 'center',
    color: '#999',
    fontSize: 16,
    marginVertical: 20,
  },
  userCard: {
    flexDirection: 'row',
    backgroundColor: '#f9f9f9',
    padding: 15,
    borderRadius: 8,
    marginBottom: 10,
    borderLeftWidth: 4,
    borderLeftColor: '#007AFF',
  },
  userInfo: {
    flex: 1,
  },
  userName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 5,
  },
  userEmail: {
    fontSize: 14,
    color: '#666',
    marginBottom: 3,
  },
  userId: {
    fontSize: 12,
    color: '#999',
  },
  userActions: {
    flexDirection: 'row',
    gap: 8,
  },
  actionButton: {
    width: 40,
    height: 40,
    borderRadius: 20,
    justifyContent: 'center',
    alignItems: 'center',
  },
  editButton: {
    backgroundColor: '#34C759',
  },
  deleteButton: {
    backgroundColor: '#FF3B30',
  },
  actionButtonText: {
    fontSize: 18,
  },
  footer: {
    padding: 20,
    alignItems: 'center',
  },
  footerText: {
    fontSize: 12,
    color: '#999',
    marginBottom: 10,
  },
  refreshText: {
    fontSize: 14,
    color: '#007AFF',
    fontWeight: 'bold',
  },
});
