-- ============================================
-- SCRIPT DE INICIALIZACIÓN DE BASE DE DATOS
-- Base de datos: VeneSeñas
-- ============================================

-- Crear la base de datos (ejecutar como superusuario)
-- CREATE DATABASE "VeneSeñas";

-- Conectarse a la base de datos
-- \c "VeneSeñas"

-- ============================================
-- TABLA: users (Usuarios del sistema)
-- ============================================
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    profile_picture VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- TABLA: user_word_history (Historial de palabras practicadas)
-- ============================================
CREATE TABLE IF NOT EXISTS user_word_history (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    word VARCHAR(50) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    mistakes INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- TABLA: user_progress (Progreso del usuario en el juego)
-- ============================================
CREATE TABLE IF NOT EXISTS user_progress (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    level INTEGER DEFAULT 1,
    stars INTEGER DEFAULT 0,
    total_score INTEGER DEFAULT 0,
    words_completed INTEGER DEFAULT 0,
    last_played TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- TABLA: user_settings (Configuraciones del usuario)
-- ============================================
CREATE TABLE IF NOT EXISTS user_settings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    theme VARCHAR(50) DEFAULT 'light',
    sound_enabled BOOLEAN DEFAULT TRUE,
    notifications_enabled BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- ÍNDICES PARA MEJORAR RENDIMIENTO
-- ============================================
CREATE INDEX IF NOT EXISTS idx_user_word_history_user_id ON user_word_history(user_id);
CREATE INDEX IF NOT EXISTS idx_user_word_history_word ON user_word_history(word);
CREATE INDEX IF NOT EXISTS idx_user_progress_user_id ON user_progress(user_id);
CREATE INDEX IF NOT EXISTS idx_user_settings_user_id ON user_settings(user_id);

-- ============================================
-- FUNCIÓN: Actualizar updated_at automáticamente
-- ============================================
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ============================================
-- TRIGGERS: Actualizar updated_at en users y user_settings
-- ============================================
DROP TRIGGER IF EXISTS update_users_updated_at ON users;
CREATE TRIGGER update_users_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_user_settings_updated_at ON user_settings;
CREATE TRIGGER update_user_settings_updated_at
BEFORE UPDATE ON user_settings
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- ============================================
-- DATOS DE PRUEBA
-- ============================================
-- Usuario de prueba (contraseña: test123)
INSERT INTO users (full_name, email, password) VALUES
('Usuario Prueba', 'test@example.com', 'test123')
ON CONFLICT (email) DO NOTHING;

-- Obtener el ID del usuario de prueba
DO $$
DECLARE
    test_user_id INTEGER;
BEGIN
    SELECT id INTO test_user_id FROM users WHERE email = 'test@example.com';
    
    -- Progreso inicial
    INSERT INTO user_progress (user_id, level, stars, total_score, words_completed)
    VALUES (test_user_id, 1, 0, 0, 0)
    ON CONFLICT (user_id) DO NOTHING;
    
    -- Configuraciones por defecto
    INSERT INTO user_settings (user_id, theme, sound_enabled, notifications_enabled)
    VALUES (test_user_id, 'light', TRUE, TRUE)
    ON CONFLICT (user_id) DO NOTHING;
END $$;

-- ============================================
-- VERIFICACIÓN
-- ============================================
SELECT 'Tablas creadas exitosamente' AS status;
SELECT * FROM users;
SELECT * FROM user_progress;
SELECT * FROM user_settings;
