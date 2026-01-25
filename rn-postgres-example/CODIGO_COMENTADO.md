# ============================================
# BACKEND - Node.js + Express + PostgreSQL
# ============================================
# API REST para gestionar usuarios en PostgreSQL
# Base de datos: VeneSeñas
# Operaciones: CREATE, READ, UPDATE, DELETE (CRUD)

# ============================================
# MÓDULOS REQUERIDOS
# ============================================
const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');

# ============================================
# CONFIGURACIÓN DE EXPRESS
# ============================================
const app = express();
const PORT = 3000;

# ============================================
# CONFIGURACIÓN DE LA BASE DE DATOS
# ============================================
# Configuración de la conexión a PostgreSQL
# Pool mantiene múltiples conexiones para mejor rendimiento

const pool = new Pool({
  user: 'postgres',           # Usuario de PostgreSQL
  host: 'localhost',          # Host donde corre PostgreSQL
  database: 'VeneSeñas',      # Nombre de la base de datos
  password: 'dosmastres5A',   # Contraseña del usuario postgres
  port: 5432,                 # Puerto por defecto de PostgreSQL
});

# ============================================
# MIDDLEWARES
# ============================================
# cors(): Permite peticiones desde React Native (diferentes orígenes)
app.use(cors());

# express.json(): Parsea el body de las peticiones como JSON
app.use(express.json());

# ============================================
# VERIFICAR CONEXIÓN A LA BASE DE DATOS
# ============================================
pool.connect((err, client, release) => {
  if (err) {
    return console.error('❌ Error al conectar con PostgreSQL:', err.stack);
  }
  console.log('✅ Conexión exitosa a la base de datos PostgreSQL');
  console.log('   Base de datos:', pool.options.database);
  release();
});

# ============================================
# ENDPOINT 1: GET /usuarios
# ============================================
# Obtiene todos los usuarios de la base de datos
# Response: JSON con array de usuarios

app.get('/usuarios', async (req, res) => {
  try {
    # Ejecutar query SQL
    const result = await pool.query(
      'SELECT id, nombre, email, fecha_creacion FROM usuarios ORDER BY id ASC'
    );

    # Enviar respuesta exitosa
    res.status(200).json({
      success: true,
      count: result.rows.length,
      data: result.rows
    });

  } catch (error) {
    console.error('❌ Error en GET /usuarios:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al obtener usuarios',
      error: error.message
    });
  }
});

# ============================================
# ENDPOINT 2: POST /usuarios
# ============================================
# Crea un nuevo usuario
# Body esperado: { "nombre": "Juan", "email": "juan@example.com" }
# Response: Usuario creado con su ID

app.post('/usuarios', async (req, res) => {
  try {
    const { nombre, email } = req.body;

    # Validar que los campos requeridos estén presentes
    if (!nombre || !email) {
      return res.status(400).json({
        success: false,
        mensaje: 'Faltan campos requeridos: nombre y email'
      });
    }

    # Validar formato de email básico
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      return res.status(400).json({
        success: false,
        mensaje: 'Formato de email inválido'
      });
    }

    # Insertar usuario en la base de datos
    const result = await pool.query(
      'INSERT INTO usuarios (nombre, email) VALUES ($1, $2) RETURNING *',
      [nombre, email]
    );

    # Enviar respuesta con el usuario creado
    res.status(201).json({
      success: true,
      mensaje: 'Usuario creado exitosamente',
      data: result.rows[0]
    });

  } catch (error) {
    console.error('❌ Error en POST /usuarios:', error);

    # Si es error de duplicado de email (constraint unique)
    if (error.code === '23505') {
      return res.status(409).json({
        success: false,
        mensaje: 'El email ya está registrado'
      });
    }

    res.status(500).json({
      success: false,
      mensaje: 'Error al crear usuario',
      error: error.message
    });
  }
});

# ============================================
# ENDPOINT 3: PUT /usuarios/:id
# ============================================
# Actualiza un usuario existente
# Params: id del usuario (ej: /usuarios/1)
# Body: { "nombre": "Nuevo Nombre", "email": "nuevo@email.com" }

app.put('/usuarios/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { nombre, email } = req.body;

    # Validar que al menos un campo esté presente
    if (!nombre && !email) {
      return res.status(400).json({
        success: false,
        mensaje: 'Debes proporcionar al menos nombre o email'
      });
    }

    # Construir query dinámicamente según los campos presentes
    let query = 'UPDATE usuarios SET ';
    const values = [];
    let valueIndex = 1;

    if (nombre) {
      query += `nombre = $${valueIndex}, `;
      values.push(nombre);
      valueIndex++;
    }

    if (email) {
      # Validar formato de email
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        return res.status(400).json({
          success: false,
          mensaje: 'Formato de email inválido'
        });
      }

      query += `email = $${valueIndex}, `;
      values.push(email);
      valueIndex++;
    }

    # Remover última coma y agregar WHERE
    query = query.slice(0, -2);
    query += ` WHERE id = $${valueIndex} RETURNING *`;
    values.push(id);

    # Ejecutar actualización
    const result = await pool.query(query, values);

    # Verificar si el usuario existe
    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        mensaje: `Usuario con ID ${id} no encontrado`
      });
    }

    res.status(200).json({
      success: true,
      mensaje: 'Usuario actualizado exitosamente',
      data: result.rows[0]
    });

  } catch (error) {
    console.error('❌ Error en PUT /usuarios/:id:', error);

    # Si es error de duplicado de email
    if (error.code === '23505') {
      return res.status(409).json({
        success: false,
        mensaje: 'El email ya está registrado'
      });
    }

    res.status(500).json({
      success: false,
      mensaje: 'Error al actualizar usuario',
      error: error.message
    });
  }
});

# ============================================
# ENDPOINT 4: DELETE /usuarios/:id
# ============================================
# Elimina un usuario por su ID
# Params: id del usuario (ej: /usuarios/1)

app.delete('/usuarios/:id', async (req, res) => {
  try {
    const { id } = req.params;

    # Eliminar usuario
    const result = await pool.query(
      'DELETE FROM usuarios WHERE id = $1 RETURNING *',
      [id]
    );

    # Verificar si el usuario existía
    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        mensaje: `Usuario con ID ${id} no encontrado`
      });
    }

    res.status(200).json({
      success: true,
      mensaje: 'Usuario eliminado exitosamente',
      data: result.rows[0]
    });

  } catch (error) {
    console.error('❌ Error en DELETE /usuarios/:id:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al eliminar usuario',
      error: error.message
    });
  }
});

# ============================================
# ENDPOINT DE HEALTH CHECK
# ============================================
# Verifica que el servidor esté funcionando

app.get('/', (req, res) => {
  res.json({
    success: true,
    mensaje: 'API funcionando correctamente',
    endpoints: {
      'GET /usuarios': 'Obtener todos los usuarios',
      'POST /usuarios': 'Crear un nuevo usuario',
      'PUT /usuarios/:id': 'Actualizar un usuario',
      'DELETE /usuarios/:id': 'Eliminar un usuario'
    }
  });
});

# ============================================
# INICIAR SERVIDOR
# ============================================
app.listen(PORT, () => {
  console.log(`🚀 Servidor escuchando en http://localhost:${PORT}`);
  console.log(`📍 Endpoints disponibles:`);
  console.log(`   GET    http://localhost:${PORT}/usuarios`);
  console.log(`   POST   http://localhost:${PORT}/usuarios`);
  console.log(`   PUT    http://localhost:${PORT}/usuarios/:id`);
  console.log(`   DELETE http://localhost:${PORT}/usuarios/:id`);
});

# ============================================
# MANEJO DE CIERRE GRACEFUL
# ============================================
# Cierra el pool de conexiones cuando se detiene el servidor
process.on('SIGINT', async () => {
  console.log('\n🛑 Cerrando servidor...');
  await pool.end();
  console.log('✅ Conexiones cerradas');
  process.exit(0);
});
