-- ============================================
-- TABLA: glb_models
-- Almacena metadata y URLs de modelos GLB
-- ============================================

CREATE TABLE IF NOT EXISTS glb_models (
    id SERIAL PRIMARY KEY,
    avatar VARCHAR(50) NOT NULL,              -- Nancy, Duvall, Carla, Remy, Argenis
    categoria VARCHAR(100) NOT NULL,          -- alfabeto, verbos, sustantivos, etc.
    nombre_palabra VARCHAR(200) NOT NULL,     -- agarrar, casa, hola, a, b, c, etc.
    nombre_archivo VARCHAR(500) NOT NULL,     -- a.glb, agarrar.glb, etc.
    url_github TEXT NOT NULL,                 -- URL completa del archivo en GitHub Releases
    peso_mb DECIMAL(10,2),                    -- Tamaño del archivo en MB
    duracion_segundos DECIMAL(5,2),           -- Duración de la animación
    es_deletreo BOOLEAN DEFAULT FALSE,        -- Si es una letra del alfabeto
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Índices para búsqueda rápida
    CONSTRAINT unique_model UNIQUE(avatar, categoria, nombre_palabra)
);

-- Índices para optimizar consultas
CREATE INDEX idx_avatar ON glb_models(avatar);
CREATE INDEX idx_categoria ON glb_models(categoria);
CREATE INDEX idx_nombre_palabra ON glb_models(nombre_palabra);
CREATE INDEX idx_avatar_categoria ON glb_models(avatar, categoria);

-- Trigger para actualizar updated_at
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_glb_models_modtime
    BEFORE UPDATE ON glb_models
    FOR EACH ROW
    EXECUTE FUNCTION update_modified_column();

-- Función para buscar modelos
CREATE OR REPLACE FUNCTION buscar_modelo(
    p_avatar VARCHAR,
    p_nombre_palabra VARCHAR
)
RETURNS TABLE (
    url_github TEXT,
    categoria VARCHAR,
    nombre_archivo VARCHAR,
    duracion_segundos DECIMAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        g.url_github,
        g.categoria,
        g.nombre_archivo,
        g.duracion_segundos
    FROM glb_models g
    WHERE LOWER(g.avatar) = LOWER(p_avatar)
      AND LOWER(g.nombre_palabra) = LOWER(p_nombre_palabra)
    LIMIT 1;
END;
$$ LANGUAGE plpgsql;

-- Ejemplos de inserción (se llenará con script automatizado)
-- INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, es_deletreo)
-- VALUES 
--   ('Nancy', 'alfabeto', 'a', 'Nancy_resultado_a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/v1.0/Nancy_resultado_a.glb', TRUE),
--   ('Duvall', 'verbos', 'agarrar', 'Duvall_resultado_agarrar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/v1.0/Duvall_resultado_agarrar.glb', FALSE);

COMMENT ON TABLE glb_models IS 'Almacena referencias a modelos GLB hospedados en GitHub Releases';
COMMENT ON COLUMN glb_models.url_github IS 'URL completa del archivo en GitHub Releases';
COMMENT ON COLUMN glb_models.es_deletreo IS 'TRUE si es una letra del alfabeto para deletreo';
