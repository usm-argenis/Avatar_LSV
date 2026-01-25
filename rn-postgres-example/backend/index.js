// ============================================
// BACKEND - Node.js + Express + PostgreSQL
// ============================================
// API REST para VeneSeñas - App de Lengua de Señas Venezolana
// Maneja autenticación, progreso de usuarios, historial y configuraciones

const express = require('express');
const cors = require('cors');
const { Pool } = require('pg');
const bcrypt = require('bcrypt');

// ============================================
// CONFIGURACIÓN DEL SERVIDOR
// ============================================
const app = express();
const PORT = 3000;

// Middleware para parsear JSON en las peticiones
app.use(express.json());

// Middleware CORS para permitir conexiones desde React Native
app.use(cors());

// ============================================
// CONFIGURACIÓN DE POSTGRESQL
// ============================================
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'VeneSeñas',
  password: 'dosmastres5A',
  port: 5432,
});

// Probar conexión
pool.connect((err, client, release) => {
  if (err) {
    return console.error('❌ Error conectando a PostgreSQL:', err.stack);
  }
  console.log('✅ Conectado a PostgreSQL - Base de datos: VeneSeñas');
  release();
});

// ============================================
// ENDPOINT RAÍZ
// ============================================
app.get('/', (req, res) => {
  res.json({
    mensaje: '🎉 Backend VeneSeñas API funcionando',
    version: '1.0.0',
    endpoints: {
      registro: 'POST /api/register',
      login: 'POST /api/login',
      progreso: 'GET/PUT /api/user/:id/progress',
      historial: 'GET/POST /api/user/:id/word-history',
      configuraciones: 'GET/PUT /api/user/:id/settings'
    }
  });
});

// ============================================
// 🔐 AUTENTICACIÓN
// ============================================

// REGISTRO DE USUARIO
// POST /api/register
app.post('/api/register', async (req, res) => {
  const client = await pool.connect();
  try {
    const { full_name, email, password } = req.body;
    
    // Validaciones
    if (!full_name || !email || !password) {
      return res.status(400).json({
        success: false,
        mensaje: 'Todos los campos son requeridos'
      });
    }

    if (password.length < 6) {
      return res.status(400).json({
        success: false,
        mensaje: 'La contraseña debe tener al menos 6 caracteres'
      });
    }

    await client.query('BEGIN');

    // Verificar si el email ya existe
    const emailCheck = await client.query(
      'SELECT id FROM users WHERE email = $1',
      [email]
    );

    if (emailCheck.rows.length > 0) {
      await client.query('ROLLBACK');
      return res.status(409).json({
        success: false,
        mensaje: 'El email ya está registrado'
      });
    }

    // Hashear la contraseña
    const hashedPassword = await bcrypt.hash(password, 10);

    // Crear usuario
    const userResult = await client.query(
      `INSERT INTO users (full_name, email, password) 
       VALUES ($1, $2, $3) 
       RETURNING id, full_name, email, created_at`,
      [full_name, email, hashedPassword]
    );

    const userId = userResult.rows[0].id;

    // Crear progreso inicial
    await client.query(
      `INSERT INTO user_progress (user_id, level, stars, total_score, words_completed) 
       VALUES ($1, 1, 0, 0, 0)`,
      [userId]
    );

    // Crear configuraciones por defecto
    await client.query(
      `INSERT INTO user_settings (user_id, theme, sound_enabled, notifications_enabled) 
       VALUES ($1, 'light', true, true)`,
      [userId]
    );

    await client.query('COMMIT');

    res.status(201).json({
      success: true,
      mensaje: 'Usuario registrado exitosamente',
      data: {
        id: userResult.rows[0].id,
        full_name: userResult.rows[0].full_name,
        email: userResult.rows[0].email,
        created_at: userResult.rows[0].created_at
      }
    });

  } catch (error) {
    await client.query('ROLLBACK');
    console.error('❌ Error en registro:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al registrar usuario',
      error: error.message
    });
  } finally {
    client.release();
  }
});

// LOGIN DE USUARIO
// POST /api/login
app.post('/api/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    
    // Validaciones
    if (!email || !password) {
      return res.status(400).json({
        success: false,
        mensaje: 'Email y contraseña son requeridos'
      });
    }

    // Buscar usuario por email
    const userResult = await pool.query(
      'SELECT * FROM users WHERE email = $1',
      [email]
    );

    if (userResult.rows.length === 0) {
      return res.status(401).json({
        success: false,
        mensaje: 'Email o contraseña incorrectos'
      });
    }

    const user = userResult.rows[0];

    // Verificar contraseña
    const passwordMatch = await bcrypt.compare(password, user.password);

    if (!passwordMatch) {
      return res.status(401).json({
        success: false,
        mensaje: 'Email o contraseña incorrectos'
      });
    }

    // Obtener progreso del usuario
    const progressResult = await pool.query(
      'SELECT * FROM user_progress WHERE user_id = $1',
      [user.id]
    );

    // Obtener configuraciones
    const settingsResult = await pool.query(
      'SELECT * FROM user_settings WHERE user_id = $1',
      [user.id]
    );

    // Actualizar last_played
    await pool.query(
      'UPDATE user_progress SET last_played = CURRENT_TIMESTAMP WHERE user_id = $1',
      [user.id]
    );

    res.json({
      success: true,
      mensaje: 'Login exitoso',
      data: {
        user: {
          id: user.id,
          full_name: user.full_name,
          email: user.email,
          profile_picture: user.profile_picture,
          created_at: user.created_at
        },
        progress: progressResult.rows[0] || null,
        settings: settingsResult.rows[0] || null
      }
    });

  } catch (error) {
    console.error('❌ Error en login:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error en el servidor',
      error: error.message
    });
  }
});

// ============================================
// 📊 PROGRESO DEL USUARIO
// ============================================

// OBTENER PROGRESO
// GET /api/user/:id/progress
app.get('/api/user/:id/progress', async (req, res) => {
  try {
    const { id } = req.params;

    const result = await pool.query(
      'SELECT * FROM user_progress WHERE user_id = $1',
      [id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        mensaje: 'Progreso no encontrado'
      });
    }

    res.json({
      success: true,
      data: result.rows[0]
    });

  } catch (error) {
    console.error('❌ Error al obtener progreso:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al obtener progreso',
      error: error.message
    });
  }
});

// ACTUALIZAR PROGRESO
// PUT /api/user/:id/progress
app.put('/api/user/:id/progress', async (req, res) => {
  try {
    const { id } = req.params;
    const { level, stars, total_score, words_completed } = req.body;

    const result = await pool.query(
      `UPDATE user_progress 
       SET level = COALESCE($1, level),
           stars = COALESCE($2, stars),
           total_score = COALESCE($3, total_score),
           words_completed = COALESCE($4, words_completed),
           last_played = CURRENT_TIMESTAMP
       WHERE user_id = $5
       RETURNING *`,
      [level, stars, total_score, words_completed, id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        mensaje: 'Progreso no encontrado'
      });
    }

    res.json({
      success: true,
      mensaje: 'Progreso actualizado',
      data: result.rows[0]
    });

  } catch (error) {
    console.error('❌ Error al actualizar progreso:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al actualizar progreso',
      error: error.message
    });
  }
});

// AGREGAR ESTRELLAS (útil para cuando completan palabras)
// POST /api/user/:id/add-stars
app.post('/api/user/:id/add-stars', async (req, res) => {
  try {
    const { id } = req.params;
    const { stars, words_completed } = req.body;

    const result = await pool.query(
      `UPDATE user_progress 
       SET stars = stars + $1,
           total_score = total_score + ($1 * 10),
           words_completed = words_completed + $2,
           last_played = CURRENT_TIMESTAMP
       WHERE user_id = $3
       RETURNING *`,
      [stars || 0, words_completed || 0, id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        mensaje: 'Usuario no encontrado'
      });
    }

    res.json({
      success: true,
      mensaje: `¡+${stars} estrellas ganadas!`,
      data: result.rows[0]
    });

  } catch (error) {
    console.error('❌ Error al agregar estrellas:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al agregar estrellas',
      error: error.message
    });
  }
});

// ============================================
// 📝 HISTORIAL DE PALABRAS
// ============================================

// OBTENER HISTORIAL
// GET /api/user/:id/word-history
app.get('/api/user/:id/word-history', async (req, res) => {
  try {
    const { id } = req.params;
    const { limit = 50 } = req.query;

    const result = await pool.query(
      `SELECT * FROM user_word_history 
       WHERE user_id = $1 
       ORDER BY created_at DESC 
       LIMIT $2`,
      [id, limit]
    );

    res.json({
      success: true,
      count: result.rows.length,
      data: result.rows
    });

  } catch (error) {
    console.error('❌ Error al obtener historial:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al obtener historial',
      error: error.message
    });
  }
});

// AGREGAR PALABRA AL HISTORIAL
// POST /api/user/:id/word-history
app.post('/api/user/:id/word-history', async (req, res) => {
  try {
    const { id } = req.params;
    const { word, completed, mistakes } = req.body;

    if (!word) {
      return res.status(400).json({
        success: false,
        mensaje: 'La palabra es requerida'
      });
    }

    const result = await pool.query(
      `INSERT INTO user_word_history (user_id, word, completed, mistakes) 
       VALUES ($1, $2, $3, $4) 
       RETURNING *`,
      [id, word, completed || false, mistakes || 0]
    );

    res.status(201).json({
      success: true,
      mensaje: 'Historial actualizado',
      data: result.rows[0]
    });

  } catch (error) {
    console.error('❌ Error al agregar historial:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al agregar historial',
      error: error.message
    });
  }
});

// ============================================
// ⚙️ CONFIGURACIONES
// ============================================

// OBTENER CONFIGURACIONES
// GET /api/user/:id/settings
app.get('/api/user/:id/settings', async (req, res) => {
  try {
    const { id } = req.params;

    const result = await pool.query(
      'SELECT * FROM user_settings WHERE user_id = $1',
      [id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        mensaje: 'Configuraciones no encontradas'
      });
    }

    res.json({
      success: true,
      data: result.rows[0]
    });

  } catch (error) {
    console.error('❌ Error al obtener configuraciones:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al obtener configuraciones',
      error: error.message
    });
  }
});

// ACTUALIZAR CONFIGURACIONES
// PUT /api/user/:id/settings
app.put('/api/user/:id/settings', async (req, res) => {
  try {
    const { id } = req.params;
    const { theme, sound_enabled, notifications_enabled } = req.body;

    const result = await pool.query(
      `UPDATE user_settings 
       SET theme = COALESCE($1, theme),
           sound_enabled = COALESCE($2, sound_enabled),
           notifications_enabled = COALESCE($3, notifications_enabled),
           updated_at = CURRENT_TIMESTAMP
       WHERE user_id = $4
       RETURNING *`,
      [theme, sound_enabled, notifications_enabled, id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        mensaje: 'Configuraciones no encontradas'
      });
    }

    res.json({
      success: true,
      mensaje: 'Configuraciones actualizadas',
      data: result.rows[0]
    });

  } catch (error) {
    console.error('❌ Error al actualizar configuraciones:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al actualizar configuraciones',
      error: error.message
    });
  }
});

// ============================================
// ENDPOINT 3: ACTUALIZAR UN USUARIO
// ============================================
// PUT /usuarios/:id
// Body: { "nombre": "Juan Actualizado", "email": "juan_nuevo@example.com" }
app.put('/usuarios/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const { nombre, email } = req.body;
    
    // Validar que se reciban los datos necesarios
    if (!nombre || !email) {
      return res.status(400).json({
        success: false,
        mensaje: 'Nombre y email son obligatorios'
      });
    }
    
    // Actualizar usuario en la base de datos
    const result = await pool.query(
      'UPDATE usuarios SET nombre = $1, email = $2 WHERE id = $3 RETURNING *',
      [nombre, email, id]
    );
    
    // Verificar si se encontró el usuario
    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        mensaje: 'Usuario no encontrado'
      });
    }
    
    // Devolver el usuario actualizado
    res.json({
      success: true,
      mensaje: 'Usuario actualizado exitosamente',
      data: result.rows[0]
    });
  } catch (error) {
    console.error('❌ Error al actualizar usuario:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al actualizar usuario',
      error: error.message
    });
  }
});

// ============================================
// ENDPOINT 4: ELIMINAR UN USUARIO
// ============================================
// DELETE /usuarios/:id
app.delete('/usuarios/:id', async (req, res) => {
  try {
    const { id } = req.params;
    
    // Eliminar usuario de la base de datos
    const result = await pool.query(
      'DELETE FROM usuarios WHERE id = $1 RETURNING *',
      [id]
    );
    
    // Verificar si se encontró el usuario
    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        mensaje: 'Usuario no encontrado'
      });
    }
    
    // Devolver confirmación
    res.json({
      success: true,
      mensaje: 'Usuario eliminado exitosamente',
      data: result.rows[0]
    });
  } catch (error) {
    console.error('❌ Error al eliminar usuario:', error);
    res.status(500).json({
      success: false,
      mensaje: 'Error al eliminar usuario',
      error: error.message
    });
  }
});


// ============================================
// INICIAR SERVIDOR
// ============================================
app.listen(PORT, () => {
  console.log('========================================');
  console.log(`🚀 Servidor VeneSeñas API en http://localhost:${PORT}`);
  console.log('========================================');
  console.log('🔐 Autenticación:');
  console.log(`   POST /api/register - Registrar usuario`);
  console.log(`   POST /api/login - Iniciar sesión`);
  console.log('');
  console.log('📊 Progreso:');
  console.log(`   GET  /api/user/:id/progress - Ver progreso`);
  console.log(`   PUT  /api/user/:id/progress - Actualizar progreso`);
  console.log(`   POST /api/user/:id/add-stars - Agregar estrellas`);
  console.log('');
  console.log('📝 Historial:');
  console.log(`   GET  /api/user/:id/word-history - Ver historial`);
  console.log(`   POST /api/user/:id/word-history - Agregar palabra`);
  console.log('');
  console.log('⚙️  Configuraciones:');
  console.log(`   GET  /api/user/:id/settings - Ver configuración`);
  console.log(`   PUT  /api/user/:id/settings - Actualizar configuración`);
  console.log('========================================');
});

// Manejo de cierre graceful
process.on('SIGINT', async () => {
  console.log('\n🛑 Cerrando servidor...');
  await pool.end();
  console.log('✅ Conexiones cerradas');
  process.exit(0);
});

