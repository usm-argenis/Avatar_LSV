-- ============================================
-- SCRIPT SQL PARA CREAR LA BASE DE DATOS Y TABLA
-- ============================================

-- 1. Crear la base de datos (ejecutar desde psql o pgAdmin)
-- Si ya existe la base de datos VeneSeñas, puedes omitir este paso
CREATE DATABASE "VeneSeñas"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Venezuela.1252'
    LC_CTYPE = 'Spanish_Venezuela.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- 2. Conectarse a la base de datos VeneSeñas
-- \c VeneSeñas

-- 3. Crear la tabla usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,          -- ID autoincremental
    nombre TEXT NOT NULL,            -- Nombre del usuario
    email TEXT NOT NULL UNIQUE,      -- Email del usuario (único)
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Fecha de creación
);

-- 4. Insertar datos de prueba
INSERT INTO usuarios (nombre, email) VALUES
    ('Juan Pérez', 'juan@example.com'),
    ('María García', 'maria@example.com'),
    ('Carlos López', 'carlos@example.com');

-- 5. Verificar que los datos se insertaron correctamente
SELECT * FROM usuarios;

-- ============================================
-- COMANDOS ÚTILES PARA POSTGRESQL
-- ============================================

-- Ver todas las tablas
-- \dt

-- Describir estructura de tabla usuarios
-- \d usuarios

-- Eliminar la tabla (¡CUIDADO! Esto borra todos los datos)
-- DROP TABLE usuarios;

-- Eliminar todos los datos de la tabla pero mantener la estructura
-- TRUNCATE TABLE usuarios RESTART IDENTITY;
