const { Pool } = require('pg');

// Configuración de PostgreSQL
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'VeneSeñas',
  password: 'dosmastres5A',
  port: 5432,
});

async function setupPasswordResetTable() {
  const client = await pool.connect();
  
  try {
    console.log('📦 Creando tabla password_reset_tokens...');
    
    await client.query(`
      CREATE TABLE IF NOT EXISTS password_reset_tokens (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
        token VARCHAR(255) NOT NULL,
        expires_at TIMESTAMP NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    `);
    
    console.log('✅ Tabla password_reset_tokens creada');
    
    console.log('📦 Creando índices...');
    
    await client.query(`
      CREATE INDEX IF NOT EXISTS idx_password_reset_token 
      ON password_reset_tokens(token);
    `);
    
    await client.query(`
      CREATE INDEX IF NOT EXISTS idx_password_reset_expires 
      ON password_reset_tokens(expires_at);
    `);
    
    console.log('✅ Índices creados exitosamente');
    console.log('🎉 Setup completado!');
    
  } catch (error) {
    console.error('❌ Error en setup:', error);
  } finally {
    client.release();
    await pool.end();
  }
}

setupPasswordResetTable();
