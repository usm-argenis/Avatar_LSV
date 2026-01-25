# 🎯 GUÍA DE CONEXIÓN COMPLETA - VeneSeñas

## ✅ PASO 1: Crear las Tablas en PostgreSQL

### Opción A: Usando pgAdmin
1. Abre **pgAdmin**
2. Conecta al servidor PostgreSQL
3. Verifica que la base de datos **"VeneSeñas"** existe (si no, créala)
4. Click derecho en **"VeneSeñas"** → Query Tool
5. Copia y pega TODO el contenido del archivo: `database_complete.sql`
6. Presiona F5 o el botón ▶️ "Execute"

### Opción B: Usando psql en Terminal
```powershell
# Conectar a PostgreSQL
psql -U postgres

# Cambiar a la base de datos
\c "VeneSeñas"

# Ejecutar el script
\i C:/Users/andre/OneDrive/Documentos/tesis/rn-postgres-example/backend/database_complete.sql

# Verificar que se crearon las tablas
\dt
```

Deberías ver 4 tablas:
- `users`
- `user_progress`
- `user_settings`
- `user_word_history`

---

## ✅ PASO 2: Backend Node.js (YA ESTÁ CORRIENDO ✓)

El servidor ya está corriendo en el puerto **3000** con estos endpoints:

```
🔐 Autenticación:
   POST /api/register - Registrar usuario
   POST /api/login - Iniciar sesión

📊 Progreso:
   GET  /api/user/:id/progress
   PUT  /api/user/:id/progress
   POST /api/user/:id/add-stars

📝 Historial:
   GET  /api/user/:id/word-history
   POST /api/user/:id/word-history

⚙️  Configuraciones:
   GET  /api/user/:id/settings
   PUT  /api/user/:id/settings
```

---

## ✅ PASO 3: Probar la API (Antes de React Native)

### Probar Registro:
```powershell
curl -X POST http://localhost:3000/api/register `
  -H "Content-Type: application/json" `
  -d '{\"full_name\":\"Juan Pérez\",\"email\":\"juan@test.com\",\"password\":\"test123\"}'
```

### Probar Login:
```powershell
curl -X POST http://localhost:3000/api/login `
  -H "Content-Type: application/json" `
  -d '{\"email\":\"juan@test.com\",\"password\":\"test123\"}'
```

Si ves respuestas JSON con `"success": true`, ¡todo funciona! ✅

---

## ✅ PASO 4: React Native - Pantallas de Login y Registro

He creado dos componentes listos para usar:

### Archivos creados:
- `frontend/screens/LoginScreen.js` - Pantalla de inicio de sesión
- `frontend/screens/RegisterScreen.js` - Pantalla de registro
- `frontend/services/authAPI.js` - Servicio de autenticación

### Integración con tu app:

Si usas **React Navigation**, edita tu `App.js`:

```javascript
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';
import HomeScreen from './screens/HomeScreen'; // Tu pantalla principal

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen 
          name="Login" 
          component={LoginScreen}
          options={{ headerShown: false }}
        />
        <Stack.Screen 
          name="Register" 
          component={RegisterScreen}
          options={{ title: 'Registrarse' }}
        />
        <Stack.Screen 
          name="Home" 
          component={HomeScreen}
          options={{ headerLeft: null }} // No permitir volver atrás
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

---

## ✅ PASO 5: Instalar Dependencias de React Native

```powershell
cd C:\Users\andre\OneDrive\Documentos\tesis\rn-postgres-example\frontend
npm install @react-navigation/native @react-navigation/stack axios
npm install react-native-screens react-native-safe-area-context
npm install @react-native-async-storage/async-storage
```

---

## ✅ PASO 6: Configurar IP del Backend

Edita `frontend/services/authAPI.js` línea 10:

```javascript
// Para Android Emulator:
const API_URL = 'http://10.0.2.2:3000';

// Para iOS Emulator:
// const API_URL = 'http://localhost:3000';

// Para dispositivo físico (usa tu IP):
// const API_URL = 'http://192.168.1.100:3000';
```

---

## ✅ PASO 7: Ejecutar la App

```powershell
cd C:\Users\andre\OneDrive\Documentos\tesis\rn-postgres-example\frontend
npx react-native run-android
```

---

## 🎯 Flujo de la Aplicación

```
1. Usuario abre la app
   ↓
2. Ve LoginScreen
   ↓
3. Opciones:
   - Ingresar email/password → Login → HomeScreen
   - Presionar "Registrarse" → RegisterScreen
   ↓
4. Después del login exitoso:
   - Se guarda userId en AsyncStorage
   - Se navega a HomeScreen
   - Puede actualizar progreso con POST /api/user/:id/add-stars
```

---

## 🔗 Conectar con tu Juego de Palabras

En tu pantalla `FallingSignsGame.js`, cuando el usuario complete una palabra:

```javascript
import { saveStarsToAPI } from '../services/authAPI';

// Cuando complete 3 palabras:
const onGameComplete = async (starsEarned) => {
  try {
    const userId = await AsyncStorage.getItem('userId');
    if (userId) {
      await saveStarsToAPI(userId, starsEarned, 3); // 3 palabras completadas
    }
  } catch (error) {
    console.error('Error guardando progreso:', error);
  }
};
```

---

## 📊 Tu Base de Datos Ahora Almacena:

- **users**: Información del usuario (nombre, email, contraseña)
- **user_progress**: Nivel, estrellas, puntaje total, palabras completadas
- **user_word_history**: Historial de cada palabra practicada
- **user_settings**: Preferencias (tema, sonido, notificaciones)

---

## 🐛 Solución de Problemas

### Error: "ECONNREFUSED"
- Verifica que el backend esté corriendo: `npm start` en `backend/`
- Verifica la IP en `authAPI.js`

### Error: "password authentication failed"
- Cambia la contraseña en `backend/server.js` línea 18

### Error: "relation users does not exist"
- Ejecuta el script SQL: `database_complete.sql`

### Error al hacer login:
- Verifica que el usuario esté registrado
- Verifica que la contraseña tenga al menos 6 caracteres

---

## ✅ Checklist Final

- [ ] PostgreSQL instalado y corriendo
- [ ] Base de datos "VeneSeñas" creada
- [ ] Tablas creadas (ejecutar database_complete.sql)
- [ ] Backend corriendo (npm start en backend/)
- [ ] Dependencias instaladas en frontend
- [ ] IP configurada correctamente en authAPI.js
- [ ] React Native app corriendo
- [ ] Puedes registrar un usuario
- [ ] Puedes hacer login
- [ ] El progreso se guarda correctamente

---

¡Todo listo! 🎉 Ahora tienes una app completa con:
- ✅ Autenticación de usuarios
- ✅ Base de datos PostgreSQL
- ✅ Sistema de progreso y estrellas
- ✅ Historial de palabras
- ✅ Configuraciones personalizadas
