// Script para actualizar las estrellas del usuario 1 a 700
const { Pool } = require('pg');

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'VeneSeñas',
  password: 'dosmastres5A',
  port: 5432,
});

async function updateStars() {
  try {
    // Actualizar las estrellas del usuario 1
    const updateResult = await pool.query(
      'UPDATE user_progress SET stars = $1 WHERE user_id = $2',
      [700, 1]
    );
    
    console.log(`✅ Actualización exitosa. Filas afectadas: ${updateResult.rowCount}`);
    
    // Verificar el cambio
    const verifyResult = await pool.query(
      `SELECT users.id, users.full_name, user_progress.stars, user_progress.level
       FROM users 
       INNER JOIN user_progress ON users.id = user_progress.user_id 
       WHERE users.id = 1`
    );
    
    if (verifyResult.rows.length > 0) {
      const user = verifyResult.rows[0];
      console.log('\n📊 Datos del usuario 1:');
      console.log(`   ID: ${user.id}`);
      console.log(`   Nombre: ${user.full_name}`);
      console.log(`   Estrellas: ⭐ ${user.stars}`);
      console.log(`   Nivel: ${user.level}`);
    } else {
      console.log('⚠️  No se encontró el usuario con ID 1');
    }
    
  } catch (error) {
    console.error('❌ Error:', error.message);
  } finally {
    await pool.end();
  }
}

updateStars();
