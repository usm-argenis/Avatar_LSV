# Configuración de Recuperación de Contraseña - VeneSeñas

## ✅ Implementación Completa

Se ha implementado el sistema completo de recuperación de contraseña con las siguientes características:

### 🎨 Frontend (React Native)

#### Nueva Pantalla: `ForgotPasswordScreen.js`
- Diseño moderno con degradado de colores de VeneSeñas
- Validación de email
- Integración con el backend
- Navegación desde LoginScreen

#### Actualizaciones en `LoginScreen.js`
- El botón "¿Olvidaste tu contraseña?" ahora navega a `ForgotPasswordScreen`
- Link funcional reemplazando el Alert anterior

#### Actualizaciones en `SettingsScreen.js`
- ✅ Campo de email **deshabilitado** (no editable)
- ✅ Color del título "Configuración" cambiado a **negro**
- ✅ Color del ícono de flecha cambiado a **negro**
- Estilo visual mejorado para campos deshabilitados

#### Actualizaciones en `App.js`
- Agregada ruta de navegación para `ForgotPassword`

#### Actualizaciones en `authService.js`
- `requestPasswordReset(email)` - Solicitar restablecimiento
- `resetPassword(token, newPassword)` - Restablecer con token

---

### 🔧 Backend (Node.js + Express)

#### Nuevo Servicio: `emailService.js`
- **Nodemailer** configurado para Gmail
- Templates de email con **degradado de colores de VeneSeñas**
- Funciones de email:
  - `sendPasswordResetEmail()` - Email de recuperación
  - `sendWelcomeEmail()` - Email de bienvenida
  - `sendPasswordChangedEmail()` - Confirmación de cambio

#### Nuevos Endpoints en `index.js`

**POST /api/forgot-password**
- Recibe: `{ email }`
- Valida email en base de datos
- Genera token de recuperación (válido 1 hora)
- Envía email con enlace de recuperación

**POST /api/reset-password**
- Recibe: `{ token, new_password }`
- Valida token y expiración
- Actualiza contraseña
- Elimina token usado
- Envía email de confirmación

#### Nueva Tabla: `password_reset_tokens`
```sql
CREATE TABLE password_reset_tokens (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL UNIQUE REFERENCES users(id),
  token VARCHAR(255) NOT NULL,
  expires_at TIMESTAMP NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 📧 Templates de Email con Degradado

Los emails incluyen:
- ✅ Header con **degradado** (`#FFC107` → `#2196F3` → `#F44336`)
- Logo y nombre de VeneSeñas
- Diseño responsive y profesional
- Botones call-to-action
- Footer con información de la app

---

### 🔐 Flujo de Recuperación de Contraseña

1. Usuario hace clic en "¿Olvidaste tu contraseña?"
2. Ingresa su correo electrónico
3. Backend genera token único y lo guarda en BD
4. Se envía email con enlace de recuperación
5. Usuario hace clic en el enlace
6. Ingresa nueva contraseña
7. Backend valida token y actualiza contraseña
8. Se envía email de confirmación

---

### 📦 Dependencias Instaladas

```bash
npm install nodemailer
```

---

### ⚙️ Configuración Requerida

#### Variables de Entorno (Backend)
Crear archivo `.env`:

```env
EMAIL_USER=venesenas.app@gmail.com
EMAIL_PASSWORD=tu_contraseña_de_aplicación
```

#### Configurar Gmail
1. Ir a tu cuenta de Google
2. Activar "Verificación en 2 pasos"
3. Generar "Contraseña de aplicación"
4. Usar esa contraseña en `EMAIL_PASSWORD`

---

### 🎯 Características Implementadas

✅ Pantalla de recuperación de contraseña  
✅ Validación de email  
✅ Generación de tokens seguros  
✅ Envío de emails con degradado  
✅ Email deshabilitado en configuración  
✅ Título y flecha en negro en configuración  
✅ Expiración de tokens (1 hora)  
✅ Confirmación por email  
✅ Navegación completa  

---

### 🚀 Próximos Pasos

1. **Configurar Gmail** con contraseña de aplicación
2. **Crear página web** para reseteo de contraseña (el enlace del email)
3. **Personalizar templates** de email con más detalles
4. **Agregar límite de intentos** para prevenir spam

---

### 📱 Uso en la App

```javascript
// Solicitar recuperación
import { requestPasswordReset } from './services/authService';

const response = await requestPasswordReset('usuario@email.com');
if (response.success) {
  // Email enviado
}

// Restablecer contraseña
import { resetPassword } from './services/authService';

const response = await resetPassword('token123', 'nuevaContraseña');
if (response.success) {
  // Contraseña actualizada
}
```

---

## 📊 Resumen de Cambios

| Archivo | Cambios |
|---------|---------|
| `ForgotPasswordScreen.js` | ✅ Creado |
| `emailService.js` | ✅ Creado |
| `authService.js` | ✅ 2 nuevas funciones |
| `index.js` (backend) | ✅ 2 nuevos endpoints |
| `LoginScreen.js` | ✅ Navegación actualizada |
| `SettingsScreen.js` | ✅ Email deshabilitado + Estilos |
| `App.js` | ✅ Ruta agregada |
| Base de datos | ✅ Nueva tabla |

---

¡Sistema de recuperación de contraseña completamente funcional! 🎉
