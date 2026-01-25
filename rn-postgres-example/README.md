# 🚀 Proyecto Full-Stack: React Native + Node.js + PostgreSQL

Ejemplo completo de aplicación móvil conectada a base de datos PostgreSQL mediante API REST.

## 📋 Tabla de Contenidos
- [Arquitectura](#arquitectura)
- [Requisitos Previos](#requisitos-previos)
- [Configuración de PostgreSQL](#configuración-de-postgresql)
- [Configuración del Backend](#configuración-del-backend)
- [Configuración del Frontend](#configuración-del-frontend)
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Endpoints de la API](#endpoints-de-la-api)
- [Solución de Problemas](#solución-de-problemas)

---

## 🏗️ Arquitectura

```
┌─────────────────┐
│  React Native   │  Puerto: Metro Bundler
│   (Frontend)    │  Tecnologías: React Native, Axios
└────────┬────────┘
         │ HTTP Requests (GET, POST, PUT, DELETE)
         ▼
┌─────────────────┐
│    Node.js      │  Puerto: 3000
│    Express      │  Tecnologías: Express, pg, cors
│   (Backend)     │
└────────┬────────┘
         │ SQL Queries
         ▼
┌─────────────────┐
│   PostgreSQL    │  Puerto: 5432
│   (Database)    │  Base de datos: VeneSeñas
└─────────────────┘
```

**Flujo de Datos:**
1. Usuario interactúa con la app React Native
2. App hace peticiones HTTP al backend Node.js
3. Backend procesa y ejecuta queries en PostgreSQL
4. PostgreSQL devuelve datos al backend
5. Backend envía respuesta JSON al frontend
6. Frontend actualiza la interfaz con los datos

---

## 📦 Requisitos Previos

### 1. Node.js y npm
- **Versión requerida:** Node.js v16 o superior
- **Verificar instalación:**
  ```bash
  node --version
  npm --version
  ```
- **Instalar:** https://nodejs.org/

### 2. PostgreSQL
- **Versión requerida:** PostgreSQL 12 o superior
- **Verificar instalación:**
  ```bash
  psql --version
  ```
- **Instalar:** https://www.postgresql.org/download/

### 3. React Native Environment
- **Android:** Android Studio + SDK
- **iOS:** Xcode (solo macOS)
- **Guía oficial:** https://reactnative.dev/docs/environment-setup

---

## 🗄️ Configuración de PostgreSQL

### Paso 1: Crear la Base de Datos

Abre la terminal de PostgreSQL (pgAdmin o psql):

```bash
psql -U postgres
```

Ingresa la contraseña de tu usuario `postgres`.

### Paso 2: Ejecutar el Script SQL

Dentro de `psql`, ejecuta:

```sql
-- Crear la base de datos
CREATE DATABASE "VeneSeñas";

-- Conectar a la base de datos
\c "VeneSeñas"

-- Crear la tabla usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos de prueba
INSERT INTO usuarios (nombre, email) VALUES
('Juan Pérez', 'juan@example.com'),
('María García', 'maria@example.com'),
('Carlos López', 'carlos@example.com');

-- Verificar que se crearon los datos
SELECT * FROM usuarios;
```

**Resultado esperado:**
```
 id |    nombre     |       email        |     fecha_creacion
----+---------------+--------------------+------------------------
  1 | Juan Pérez    | juan@example.com   | 2024-01-15 10:30:00
  2 | María García  | maria@example.com  | 2024-01-15 10:30:00
  3 | Carlos López  | carlos@example.com | 2024-01-15 10:30:00
```

### Paso 3: Configurar Contraseña (IMPORTANTE)

El backend está configurado para usar:
- **Usuario:** `postgres`
- **Contraseña:** `dosmastres5A`

Si tu contraseña es diferente, debes cambiar la contraseña en PostgreSQL:

```sql
ALTER USER postgres WITH PASSWORD 'dosmastres5A';
```

O puedes editar el archivo `backend/index.js` línea 25:

```javascript
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'VeneSeñas',
  password: 'TU_CONTRASEÑA_AQUI',  // ⬅️ Cambia aquí
  port: 5432,
});
```

---

## 🖥️ Configuración del Backend

### Paso 1: Instalar Dependencias

Navega a la carpeta del backend:

```bash
cd backend
npm install
```

Esto instalará:
- `express` - Framework web
- `pg` - Cliente PostgreSQL para Node.js
- `cors` - Permitir peticiones desde React Native
- `dotenv` - Variables de entorno (opcional)

### Paso 2: Verificar Configuración

Abre `backend/index.js` y verifica la configuración del Pool (líneas 18-24):

```javascript
const pool = new Pool({
  user: 'postgres',           // Usuario de PostgreSQL
  host: 'localhost',          // Host de la base de datos
  database: 'VeneSeñas',      // Nombre de la base de datos
  password: 'dosmastres5A',   // Contraseña
  port: 5432,                 // Puerto de PostgreSQL
});
```

### Paso 3: Iniciar el Backend

```bash
npm start
```

**Salida esperada:**
```
🚀 Servidor escuchando en http://localhost:3000
✅ Conexión exitosa a la base de datos PostgreSQL
   Base de datos: VeneSeñas
```

**Probar endpoints manualmente:**

```bash
# Listar usuarios
curl http://localhost:3000/usuarios

# Crear usuario
curl -X POST http://localhost:3000/usuarios \
  -H "Content-Type: application/json" \
  -d "{\"nombre\":\"Test User\",\"email\":\"test@example.com\"}"
```

---

## 📱 Configuración del Frontend

### Paso 1: Instalar Dependencias

Navega a la carpeta del frontend:

```bash
cd frontend
npm install
```

### Paso 2: Configurar URL del Backend

Abre `frontend/App.js` y configura la URL según tu entorno (líneas 20-30):

```javascript
// ⚠️ IMPORTANTE: Elige UNA de estas opciones

// Opción 1: Para EMULADOR ANDROID
const API_URL = 'http://10.0.2.2:3000';

// Opción 2: Para EMULADOR iOS
// const API_URL = 'http://localhost:3000';

// Opción 3: Para DISPOSITIVO FÍSICO
// const API_URL = 'http://192.168.1.100:3000';  // ⬅️ Usa tu IP local
```

**¿Cómo encontrar tu IP local?**

**En Windows:**
```bash
ipconfig
# Busca "Dirección IPv4" en la red activa
```

**En macOS/Linux:**
```bash
ifconfig | grep inet
# Busca la dirección inet de tu red activa
```

### Paso 3: Iniciar la Aplicación

**Para Android:**
```bash
npx react-native run-android
```

**Para iOS (solo macOS):**
```bash
cd ios && pod install && cd ..
npx react-native run-ios
```

**Metro Bundler se iniciará automáticamente:**
```
✔ Metro Bundler running on http://localhost:8081
```

---

## 🎯 Ejecución del Proyecto

### Orden de Inicio

1. **PostgreSQL debe estar corriendo** (generalmente se inicia automáticamente)
2. **Backend:**
   ```bash
   cd backend
   npm start
   ```
3. **Frontend** (en otra terminal):
   ```bash
   cd frontend
   npx react-native run-android
   # o
   npx react-native run-ios
   ```

### Verificar que Todo Funcione

1. **Backend:** http://localhost:3000/usuarios debe devolver JSON
2. **Frontend:** La app debe mostrar la lista de usuarios
3. **Crear usuario:** Completa el formulario y presiona "Guardar"
4. **Editar:** Presiona el botón ✏️ en cualquier usuario
5. **Eliminar:** Presiona el botón 🗑️ y confirma

---

## 🔌 Endpoints de la API

### 1. GET /usuarios
Obtiene todos los usuarios.

**Request:**
```bash
GET http://localhost:3000/usuarios
```

**Response:**
```json
{
  "success": true,
  "count": 3,
  "data": [
    {
      "id": 1,
      "nombre": "Juan Pérez",
      "email": "juan@example.com",
      "fecha_creacion": "2024-01-15T10:30:00.000Z"
    }
  ]
}
```

### 2. POST /usuarios
Crea un nuevo usuario.

**Request:**
```bash
POST http://localhost:3000/usuarios
Content-Type: application/json

{
  "nombre": "Nuevo Usuario",
  "email": "nuevo@example.com"
}
```

**Response:**
```json
{
  "success": true,
  "mensaje": "Usuario creado exitosamente",
  "data": {
    "id": 4,
    "nombre": "Nuevo Usuario",
    "email": "nuevo@example.com",
    "fecha_creacion": "2024-01-15T11:00:00.000Z"
  }
}
```

### 3. PUT /usuarios/:id
Actualiza un usuario existente.

**Request:**
```bash
PUT http://localhost:3000/usuarios/4
Content-Type: application/json

{
  "nombre": "Usuario Actualizado",
  "email": "actualizado@example.com"
}
```

**Response:**
```json
{
  "success": true,
  "mensaje": "Usuario actualizado exitosamente",
  "data": {
    "id": 4,
    "nombre": "Usuario Actualizado",
    "email": "actualizado@example.com"
  }
}
```

### 4. DELETE /usuarios/:id
Elimina un usuario.

**Request:**
```bash
DELETE http://localhost:3000/usuarios/4
```

**Response:**
```json
{
  "success": true,
  "mensaje": "Usuario eliminado exitosamente",
  "data": {
    "id": 4,
    "nombre": "Usuario Actualizado",
    "email": "actualizado@example.com"
  }
}
```

---

## 🐛 Solución de Problemas

### Problema 1: "ECONNREFUSED" en React Native

**Error:**
```
Error: connect ECONNREFUSED 127.0.0.1:3000
```

**Solución:**
- En emulador Android: Usa `http://10.0.2.2:3000`
- En emulador iOS: Usa `http://localhost:3000`
- En dispositivo físico: Usa tu IP local (ej: `http://192.168.1.100:3000`)

### Problema 2: "CORS Policy" Error

**Error:**
```
Access to XMLHttpRequest blocked by CORS policy
```

**Solución:**
Verifica que el backend tenga CORS habilitado (`backend/index.js` línea 31):
```javascript
app.use(cors());
```

### Problema 3: "password authentication failed"

**Error:**
```
error: password authentication failed for user "postgres"
```

**Solución:**
Cambiar contraseña en `backend/index.js` línea 25 o actualizar en PostgreSQL:
```sql
ALTER USER postgres WITH PASSWORD 'dosmastres5A';
```

### Problema 4: Base de datos no existe

**Error:**
```
database "VeneSeñas" does not exist
```

**Solución:**
Crear la base de datos manualmente:
```sql
psql -U postgres
CREATE DATABASE "VeneSeñas";
```

### Problema 5: Puerto 3000 ya en uso

**Error:**
```
Error: listen EADDRINUSE: address already in use :::3000
```

**Solución:**
Matar el proceso que usa el puerto 3000:

**Windows:**
```bash
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

**macOS/Linux:**
```bash
lsof -i :3000
kill -9 <PID>
```

### Problema 6: Metro Bundler no inicia

**Solución:**
```bash
cd frontend
npx react-native start --reset-cache
```

---

## 📚 Recursos Adicionales

- **React Native Docs:** https://reactnative.dev/docs/getting-started
- **Express Docs:** https://expressjs.com/
- **PostgreSQL Docs:** https://www.postgresql.org/docs/
- **node-postgres (pg):** https://node-postgres.com/
- **Axios:** https://axios-http.com/docs/intro

---

## ✅ Checklist de Verificación

- [ ] PostgreSQL instalado y corriendo
- [ ] Base de datos "VeneSeñas" creada
- [ ] Tabla "usuarios" creada con datos de prueba
- [ ] Node.js v16+ instalado
- [ ] Backend: `npm install` ejecutado
- [ ] Backend: `npm start` corriendo sin errores
- [ ] Frontend: `npm install` ejecutado
- [ ] Frontend: API_URL configurada correctamente
- [ ] Frontend: App corriendo en emulador/dispositivo
- [ ] App puede cargar lista de usuarios
- [ ] App puede crear nuevos usuarios
- [ ] App puede editar usuarios existentes
- [ ] App puede eliminar usuarios

---

## 📧 Contacto

Si tienes problemas, verifica:
1. Backend está corriendo (`http://localhost:3000/usuarios` devuelve JSON)
2. PostgreSQL está corriendo (verifica con pgAdmin o psql)
3. URL del backend es correcta en `App.js`
4. Contraseña de PostgreSQL coincide con `backend/index.js`

¡Buena suerte con tu proyecto! 🚀
