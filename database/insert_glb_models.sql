-- Inserción automática de modelos GLB
-- Generado: 2026-02-05T17:25:18.545Z

BEGIN;

-- Argenis - adverbios lugares (9 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'adverbios lugares', 'adverbios', 'Argenis_resultado_adverbios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-adverbios lugares/Argenis_resultado_adverbios.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'adverbios lugares', 'al lado', 'Argenis_resultado_al lado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-adverbios lugares/Argenis_resultado_al%20lado.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'adverbios lugares', 'atras', 'Argenis_resultado_atras.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-adverbios lugares/Argenis_resultado_atras.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'adverbios lugares', 'cerca', 'Argenis_resultado_cerca.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-adverbios lugares/Argenis_resultado_cerca.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'adverbios lugares', 'derecha', 'Argenis_resultado_derecha.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-adverbios lugares/Argenis_resultado_derecha.glb', 2.68, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'adverbios lugares', 'frente', 'Argenis_resultado_frente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-adverbios lugares/Argenis_resultado_frente.glb', 2.70, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'adverbios lugares', 'izquierda', 'Argenis_resultado_izquierda.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-adverbios lugares/Argenis_resultado_izquierda.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'adverbios lugares', 'lejos', 'Argenis_resultado_lejos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-adverbios lugares/Argenis_resultado_lejos.glb', 2.68, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'adverbios lugares', 'lugares', 'Argenis_resultado_lugares.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-adverbios lugares/Argenis_resultado_lugares.glb', 2.68, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - alfabeto (28 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'a', 'Argenis_resultado_a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_a.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'b', 'Argenis_resultado_b.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_b.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'c', 'Argenis_resultado_c.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_c.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'd', 'Argenis_resultado_d.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_d.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'e', 'Argenis_resultado_e.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_e.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'f', 'Argenis_resultado_f.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_f.glb', 2.63, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'g', 'Argenis_resultado_g.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_g.glb', 2.63, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'h', 'Argenis_resultado_h.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_h.glb', 2.63, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'i', 'Argenis_resultado_i.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_i.glb', 2.61, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'j', 'Argenis_resultado_j.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_j.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'k', 'Argenis_resultado_k.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_k.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'l', 'Argenis_resultado_l.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_l.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'm', 'Argenis_resultado_m.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_m.glb', 2.61, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'n', 'Argenis_resultado_n.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_n.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'o', 'Argenis_resultado_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_o.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'p', 'Argenis_resultado_p.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_p.glb', 2.61, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'q', 'Argenis_resultado_q.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_q.glb', 2.63, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'r', 'Argenis_resultado_r.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_r.glb', 2.63, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 's1', 'Argenis_resultado_s1.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_s1.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 's2', 'Argenis_resultado_s2.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_s2.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 't', 'Argenis_resultado_t.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_t.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'u', 'Argenis_resultado_u.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_u.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'v', 'Argenis_resultado_v.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_v.glb', 2.62, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'w', 'Argenis_resultado_w.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_w.glb', 2.64, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'x', 'Argenis_resultado_x.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_x.glb', 2.63, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'y', 'Argenis_resultado_y.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_y.glb', 2.63, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'z', 'Argenis_resultado_z.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_z.glb', 2.63, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'alfabeto', 'ñ', 'Argenis_resultado_ñ.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-alfabeto/Argenis_resultado_%C3%B1.glb', 2.61, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - base (1 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'base', 'base', 'Argenis.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-base/Argenis.glb', 2.60, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - cortesia (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'cortesia', 'a la orden', 'Argenis_resultado_a la orden.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-cortesia/Argenis_resultado_a%20la%20orden.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'cortesia', 'buen provecho', 'Argenis_resultado_buen provecho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-cortesia/Argenis_resultado_buen%20provecho.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'cortesia', 'cortesia', 'Argenis_resultado_cortesia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-cortesia/Argenis_resultado_cortesia.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'cortesia', 'gracias', 'Argenis_resultado_gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-cortesia/Argenis_resultado_gracias.glb', 2.61, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'cortesia', 'muchas gracias', 'Argenis_resultado_muchas gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-cortesia/Argenis_resultado_muchas%20gracias.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'cortesia', 'mucho gusto', 'Argenis_resultado_mucho gusto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-cortesia/Argenis_resultado_mucho%20gusto.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'cortesia', 'permiso', 'Argenis_resultado_permiso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-cortesia/Argenis_resultado_permiso.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - dias_semana (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'dias_semana', 'domingo', 'Argenis_resultado_domingo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-dias_semana/Argenis_resultado_domingo.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'dias_semana', 'jueves', 'Argenis_resultado_jueves.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-dias_semana/Argenis_resultado_jueves.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'dias_semana', 'lunes', 'Argenis_resultado_lunes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-dias_semana/Argenis_resultado_lunes.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'dias_semana', 'martes', 'Argenis_resultado_martes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-dias_semana/Argenis_resultado_martes.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'dias_semana', 'miercoles', 'Argenis_resultado_miercoles.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-dias_semana/Argenis_resultado_miercoles.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'dias_semana', 'sabado', 'Argenis_resultado_sabado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-dias_semana/Argenis_resultado_sabado.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'dias_semana', 'viernes', 'Argenis_resultado_viernes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-dias_semana/Argenis_resultado_viernes.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - estado civil (6 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'estado civil', 'casado', 'Argenis_resultado_casado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-estado civil/Argenis_resultado_casado.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'estado civil', 'concubino', 'Argenis_resultado_concubino.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-estado civil/Argenis_resultado_concubino.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'estado civil', 'divorciado', 'Argenis_resultado_divorciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-estado civil/Argenis_resultado_divorciado.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'estado civil', 'separado', 'Argenis_resultado_separado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-estado civil/Argenis_resultado_separado.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'estado civil', 'soltero', 'Argenis_resultado_soltero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-estado civil/Argenis_resultado_soltero.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'estado civil', 'viudo', 'Argenis_resultado_viudo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-estado civil/Argenis_resultado_viudo.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - expresiones (30 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'abril', 'Argenis_resultado_abril.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_abril.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'agosto', 'Argenis_resultado_agosto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_agosto.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'bien', 'Argenis_resultado_bien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_bien.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'como', 'Argenis_resultado_como.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_como.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'cual', 'Argenis_resultado_cual.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_cual.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'cuando', 'Argenis_resultado_cuando.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_cuando.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'cuantos', 'Argenis_resultado_cuantos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_cuantos.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'de nada', 'Argenis_resultado_de nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_de%20nada.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'diciembre', 'Argenis_resultado_diciembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_diciembre.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'donde (especifico)', 'Argenis_resultado_donde (especifico).glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_donde%20(especifico).glb', 2.61, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'donde', 'Argenis_resultado_donde.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_donde.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'enero', 'Argenis_resultado_enero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_enero.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'expresiones', 'Argenis_resultado_expresiones.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_expresiones.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'febrero', 'Argenis_resultado_febrero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_febrero.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'interrogantes', 'Argenis_resultado_interrogantes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_interrogantes.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'julio', 'Argenis_resultado_julio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_julio.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'junio', 'Argenis_resultado_junio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_junio.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'mal', 'Argenis_resultado_mal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_mal.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'marzo', 'Argenis_resultado_marzo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_marzo.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'mayo', 'Argenis_resultado_mayo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_mayo.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'no', 'Argenis_resultado_no.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_no.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'noviembre', 'Argenis_resultado_noviembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_noviembre.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'octubre', 'Argenis_resultado_octubre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_octubre.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'porque', 'Argenis_resultado_porque.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_porque.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'que', 'Argenis_resultado_que.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_que.glb', 2.61, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'quien', 'Argenis_resultado_quien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_quien.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'regular', 'Argenis_resultado_regular.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_regular.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'saludas a', 'Argenis_resultado_saludas a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_saludas%20a.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'septiembre', 'Argenis_resultado_septiembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_septiembre.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'expresiones', 'si', 'Argenis_resultado_si.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-expresiones/Argenis_resultado_si.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - medios transporte (0 archivos)
-- Argenis - numero (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '0', 'Argenis_resultado_0.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_0.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '1', 'Argenis_resultado_1.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_1.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '10', 'Argenis_resultado_10.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_10.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '1M', 'Argenis_resultado_1M.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_1M.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '2', 'Argenis_resultado_2.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_2.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '3', 'Argenis_resultado_3.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_3.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '4', 'Argenis_resultado_4.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_4.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '5', 'Argenis_resultado_5.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_5.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '6', 'Argenis_resultado_6.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_6.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '7', 'Argenis_resultado_7.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_7.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '8', 'Argenis_resultado_8.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_8.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numero', '9', 'Argenis_resultado_9.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numero/Argenis_resultado_9.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - numeros ordinales (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numeros ordinales', '10_o', 'Argenis_resultado_10_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numeros ordinales/Argenis_resultado_10_o.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numeros ordinales', '1_o', 'Argenis_resultado_1_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numeros ordinales/Argenis_resultado_1_o.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numeros ordinales', '2_o', 'Argenis_resultado_2_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numeros ordinales/Argenis_resultado_2_o.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numeros ordinales', '3_o', 'Argenis_resultado_3_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numeros ordinales/Argenis_resultado_3_o.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numeros ordinales', '4_o', 'Argenis_resultado_4_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numeros ordinales/Argenis_resultado_4_o.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numeros ordinales', '5_o', 'Argenis_resultado_5_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numeros ordinales/Argenis_resultado_5_o.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numeros ordinales', '6_o', 'Argenis_resultado_6_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numeros ordinales/Argenis_resultado_6_o.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numeros ordinales', '7_o', 'Argenis_resultado_7_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numeros ordinales/Argenis_resultado_7_o.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numeros ordinales', '8_o', 'Argenis_resultado_8_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numeros ordinales/Argenis_resultado_8_o.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'numeros ordinales', '9_o', 'Argenis_resultado_9_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-numeros ordinales/Argenis_resultado_9_o.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - personas (22 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'adulto', 'Argenis_resultado_adulto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_adulto.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'amigo', 'Argenis_resultado_amigo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_amigo.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'anciano', 'Argenis_resultado_anciano.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_anciano.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'bebe', 'Argenis_resultado_bebe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_bebe.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'ciego', 'Argenis_resultado_ciego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_ciego.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'compañero', 'Argenis_resultado_compañero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_compa%C3%B1ero.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'hombre', 'Argenis_resultado_hombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_hombre.glb', 2.70, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'joven', 'Argenis_resultado_joven.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_joven.glb', 2.69, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'mayor de edad', 'Argenis_resultado_mayor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_mayor%20de%20edad.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'mayor', 'Argenis_resultado_mayor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_mayor.glb', 2.69, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'menor de edad', 'Argenis_resultado_menor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_menor%20de%20edad.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'mujer', 'Argenis_resultado_mujer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_mujer.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'niño', 'Argenis_resultado_niño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_ni%C3%B1o.glb', 2.70, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'novio', 'Argenis_resultado_novio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_novio.glb', 2.69, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'oyente', 'Argenis_resultado_oyente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_oyente.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'persona', 'Argenis_resultado_persona.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_persona.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'personas', 'Argenis_resultado_personas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_personas.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'señor', 'Argenis_resultado_señor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_se%C3%B1or.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'señorita', 'Argenis_resultado_señorita.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_se%C3%B1orita.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'sordo', 'Argenis_resultado_sordo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_sordo.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'sordociego', 'Argenis_resultado_sordociego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_sordociego.glb', 2.69, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'personas', 'viejo', 'Argenis_resultado_viejo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-personas/Argenis_resultado_viejo.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - preguntas (4 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preguntas', 'como estas', 'Argenis_resultado_como estas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preguntas/Argenis_resultado_como%20estas.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preguntas', 'cual es tu nombre', 'Argenis_resultado_cual es tu nombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preguntas/Argenis_resultado_cual%20es%20tu%20nombre.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preguntas', 'cual es tu sena', 'Argenis_resultado_cual es tu sena.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preguntas/Argenis_resultado_cual%20es%20tu%20sena.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preguntas', 'que tal', 'Argenis_resultado_que tal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preguntas/Argenis_resultado_que%20tal.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - preposicion (15 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'algo', 'Argenis_resultado_algo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_algo.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'alguien', 'Argenis_resultado_alguien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_alguien.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'algun', 'Argenis_resultado_algun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_algun.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'bastante', 'Argenis_resultado_bastante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_bastante.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'cualquier', 'Argenis_resultado_cualquier.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_cualquier.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'demasiado', 'Argenis_resultado_demasiado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_demasiado.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'mas', 'Argenis_resultado_mas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_mas.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'mucho', 'Argenis_resultado_mucho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_mucho.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'nada', 'Argenis_resultado_nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_nada.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'nadie', 'Argenis_resultado_nadie.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_nadie.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'ningun', 'Argenis_resultado_ningun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_ningun.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'otro', 'Argenis_resultado_otro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_otro.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'poco', 'Argenis_resultado_poco.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_poco.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'quienquiera', 'Argenis_resultado_quienquiera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_quienquiera.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'preposicion', 'todo', 'Argenis_resultado_todo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-preposicion/Argenis_resultado_todo.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - profesion (48 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'abogado', 'Argenis_resultado_abogado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_abogado.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'administrador', 'Argenis_resultado_administrador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_administrador.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'albañil', 'Argenis_resultado_albañil.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_alba%C3%B1il.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'analista', 'Argenis_resultado_analista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_analista.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'auxiliar', 'Argenis_resultado_auxiliar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_auxiliar.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'barbero', 'Argenis_resultado_barbero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_barbero.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'carrera', 'Argenis_resultado_carrera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_carrera.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'chef', 'Argenis_resultado_chef.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_chef.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'cocinero', 'Argenis_resultado_cocinero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_cocinero.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'conductor', 'Argenis_resultado_conductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_conductor.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'constructor', 'Argenis_resultado_constructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_constructor.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'contador', 'Argenis_resultado_contador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_contador.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'dentista', 'Argenis_resultado_dentista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_dentista.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'detective', 'Argenis_resultado_detective.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_detective.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'dibujante tecnico', 'Argenis_resultado_dibujante tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_dibujante%20tecnico.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'dibujante', 'Argenis_resultado_dibujante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_dibujante.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'director', 'Argenis_resultado_director.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_director.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'economista', 'Argenis_resultado_economista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_economista.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'enfermera', 'Argenis_resultado_enfermera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_enfermera.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'escritor', 'Argenis_resultado_escritor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_escritor.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'fotografo', 'Argenis_resultado_fotografo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_fotografo.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'gerente', 'Argenis_resultado_gerente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_gerente.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'informatica', 'Argenis_resultado_informatica.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_informatica.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'ingenieria', 'Argenis_resultado_ingenieria.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_ingenieria.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'ingeniero', 'Argenis_resultado_ingeniero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_ingeniero.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'inspector', 'Argenis_resultado_inspector.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_inspector.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'instructor', 'Argenis_resultado_instructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_instructor.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'interprete', 'Argenis_resultado_interprete.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_interprete.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'jefe', 'Argenis_resultado_jefe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_jefe.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'licenciado', 'Argenis_resultado_licenciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_licenciado.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'maestro', 'Argenis_resultado_maestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_maestro.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'medico', 'Argenis_resultado_medico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_medico.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'mensajero', 'Argenis_resultado_mensajero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_mensajero.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'mesonero', 'Argenis_resultado_mesonero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_mesonero.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'pasante', 'Argenis_resultado_pasante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_pasante.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'peluquera', 'Argenis_resultado_peluquera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_peluquera.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'pintor', 'Argenis_resultado_pintor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_pintor.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'policia', 'Argenis_resultado_policia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_policia.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'profesion', 'Argenis_resultado_profesion.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_profesion.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'profesor', 'Argenis_resultado_profesor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_profesor.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'psicologo', 'Argenis_resultado_psicologo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_psicologo.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'secretaria', 'Argenis_resultado_secretaria.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_secretaria.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'sistema', 'Argenis_resultado_sistema.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_sistema.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'supervisor', 'Argenis_resultado_supervisor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_supervisor.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'tecnico', 'Argenis_resultado_tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_tecnico.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'traductor', 'Argenis_resultado_traductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_traductor.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'vendedor', 'Argenis_resultado_vendedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_vendedor.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'profesion', 'vigilante', 'Argenis_resultado_vigilante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-profesion/Argenis_resultado_vigilante.glb', 2.68, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - pronombres (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'el', 'Argenis_resultado_el.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_el.glb', 2.61, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'ella', 'Argenis_resultado_ella.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_ella.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'ellas', 'Argenis_resultado_ellas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_ellas.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'ellos', 'Argenis_resultado_ellos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_ellos.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'mio', 'Argenis_resultado_mio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_mio.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'nosotros', 'Argenis_resultado_nosotros.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_nosotros.glb', 2.61, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'nuestro', 'Argenis_resultado_nuestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_nuestro.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'suyo', 'Argenis_resultado_suyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_suyo.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'tu', 'Argenis_resultado_tu.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_tu.glb', 2.61, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'tuyo', 'Argenis_resultado_tuyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_tuyo.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'ustedes', 'Argenis_resultado_ustedes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_ustedes.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'pronombres', 'yo', 'Argenis_resultado_yo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-pronombres/Argenis_resultado_yo.glb', 2.61, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - saludos (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'saludos', 'adios', 'Argenis_resultado_adios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-saludos/Argenis_resultado_adios.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'saludos', 'bienvenido', 'Argenis_resultado_bienvenido.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-saludos/Argenis_resultado_bienvenido.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'saludos', 'buenas noches', 'Argenis_resultado_buenas noches.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-saludos/Argenis_resultado_buenas%20noches.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'saludos', 'buenas tardes', 'Argenis_resultado_buenas tardes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-saludos/Argenis_resultado_buenas%20tardes.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'saludos', 'buenos dias', 'Argenis_resultado_buenos dias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-saludos/Argenis_resultado_buenos%20dias.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'saludos', 'chao', 'Argenis_resultado_chao.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-saludos/Argenis_resultado_chao.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'saludos', 'hola', 'Argenis_resultado_hola.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-saludos/Argenis_resultado_hola.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - tiempo (9 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tiempo', 'anteayer', 'Argenis_resultado_anteayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tiempo/Argenis_resultado_anteayer.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tiempo', 'ayer', 'Argenis_resultado_ayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tiempo/Argenis_resultado_ayer.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tiempo', 'calendario', 'Argenis_resultado_calendario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tiempo/Argenis_resultado_calendario.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tiempo', 'fin de semana', 'Argenis_resultado_fin de semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tiempo/Argenis_resultado_fin%20de%20semana.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tiempo', 'hoy', 'Argenis_resultado_hoy.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tiempo/Argenis_resultado_hoy.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tiempo', 'manana', 'Argenis_resultado_manana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tiempo/Argenis_resultado_manana.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tiempo', 'mes', 'Argenis_resultado_mes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tiempo/Argenis_resultado_mes.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tiempo', 'pasado manana', 'Argenis_resultado_pasado manana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tiempo/Argenis_resultado_pasado%20manana.glb', 2.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tiempo', 'semana', 'Argenis_resultado_semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tiempo/Argenis_resultado_semana.glb', 2.62, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - tipos de vivienda (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tipos de vivienda', 'apartamento', 'Argenis_resultado_apartamento.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tipos de vivienda/Argenis_resultado_apartamento.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tipos de vivienda', 'baño', 'Argenis_resultado_baño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tipos de vivienda/Argenis_resultado_ba%C3%B1o.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tipos de vivienda', 'casa', 'Argenis_resultado_casa.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tipos de vivienda/Argenis_resultado_casa.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tipos de vivienda', 'cocina', 'Argenis_resultado_cocina.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tipos de vivienda/Argenis_resultado_cocina.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tipos de vivienda', 'comedor', 'Argenis_resultado_comedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tipos de vivienda/Argenis_resultado_comedor.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tipos de vivienda', 'cuarto', 'Argenis_resultado_cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tipos de vivienda/Argenis_resultado_cuarto.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tipos de vivienda', 'edificio', 'Argenis_resultado_edificio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tipos de vivienda/Argenis_resultado_edificio.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tipos de vivienda', 'piso', 'Argenis_resultado_piso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tipos de vivienda/Argenis_resultado_piso.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tipos de vivienda', 'rancho', 'Argenis_resultado_rancho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tipos de vivienda/Argenis_resultado_rancho.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'tipos de vivienda', 'sala', 'Argenis_resultado_sala.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-tipos de vivienda/Argenis_resultado_sala.glb', 2.68, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Argenis - verbos (20 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'amar', 'Argenis_resultado_amar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_amar.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'ayudar', 'Argenis_resultado_ayudar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_ayudar.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'cansar', 'Argenis_resultado_cansar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_cansar.glb', 2.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'comer', 'Argenis_resultado_comer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_comer.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'conocer', 'Argenis_resultado_conocer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_conocer.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'decir', 'Argenis_resultado_decir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_decir.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'deletrear', 'Argenis_resultado_deletrear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_deletrear.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'dormir', 'Argenis_resultado_dormir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_dormir.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'estar', 'Argenis_resultado_estar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_estar.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'estudiar', 'Argenis_resultado_estudiar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_estudiar.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'invitar', 'Argenis_resultado_invitar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_invitar.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'preguntar', 'Argenis_resultado_preguntar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_preguntar.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'presentar', 'Argenis_resultado_presentar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_presentar.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'querer', 'Argenis_resultado_querer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_querer.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'responder', 'Argenis_resultado_responder.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_responder.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'saludar', 'Argenis_resultado_saludar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_saludar.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'sentir', 'Argenis_resultado_sentir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_sentir.glb', 2.67, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'trabajar', 'Argenis_resultado_trabajar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_trabajar.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'ver', 'Argenis_resultado_ver.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_ver.glb', 2.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Argenis', 'verbos', 'vivir', 'Argenis_resultado_vivir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-argenis-verbos/Argenis_resultado_vivir.glb', 2.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - adverbios lugares (9 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'adverbios', 'Carla_resultado_adverbios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-adverbios lugares/Carla_resultado_adverbios.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'al lado', 'Carla_resultado_al lado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-adverbios lugares/Carla_resultado_al%20lado.glb', 3.40, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'atras', 'Carla_resultado_atras.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-adverbios lugares/Carla_resultado_atras.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'cerca', 'Carla_resultado_cerca.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-adverbios lugares/Carla_resultado_cerca.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'derecha', 'Carla_resultado_derecha.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-adverbios lugares/Carla_resultado_derecha.glb', 3.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'frente', 'Carla_resultado_frente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-adverbios lugares/Carla_resultado_frente.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'izquierda', 'Carla_resultado_izquierda.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-adverbios lugares/Carla_resultado_izquierda.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'lejos', 'Carla_resultado_lejos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-adverbios lugares/Carla_resultado_lejos.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'lugares', 'Carla_resultado_lugares.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-adverbios lugares/Carla_resultado_lugares.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - alfabeto (27 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'a', 'Carla_resultado_a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_a.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'b', 'Carla_resultado_b.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_b.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'c', 'Carla_resultado_c.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_c.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'd', 'Carla_resultado_d.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_d.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'e', 'Carla_resultado_e.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_e.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'f', 'Carla_resultado_f.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_f.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'g', 'Carla_resultado_g.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_g.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'h', 'Carla_resultado_h.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_h.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'i', 'Carla_resultado_i.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_i.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'j', 'Carla_resultado_j.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_j.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'k', 'Carla_resultado_k.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_k.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'l', 'Carla_resultado_l.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_l.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'm', 'Carla_resultado_m.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_m.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'n', 'Carla_resultado_n.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_n.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'o', 'Carla_resultado_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_o.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'p', 'Carla_resultado_p.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_p.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'q', 'Carla_resultado_q.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_q.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'r', 'Carla_resultado_r.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_r.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 's', 'Carla_resultado_s.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_s.glb', 3.35, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 't', 'Carla_resultado_t.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_t.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'u', 'Carla_resultado_u.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_u.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'v', 'Carla_resultado_v.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_v.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'w', 'Carla_resultado_w.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_w.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'x', 'Carla_resultado_x.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_x.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'y', 'Carla_resultado_y.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_y.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'z', 'Carla_resultado_z.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_z.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'ñ', 'Carla_resultado_ñ.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-alfabeto/Carla_resultado_%C3%B1.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - base (1 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'base', 'base', 'Carla.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-base/Carla.glb', 3.01, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - cortesia (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'a la orden', 'Carla_resultado_a la orden.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-cortesia/Carla_resultado_a%20la%20orden.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'buen provecho', 'Carla_resultado_buen provecho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-cortesia/Carla_resultado_buen%20provecho.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'cortesia', 'Carla_resultado_cortesia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-cortesia/Carla_resultado_cortesia.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'gracias', 'Carla_resultado_gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-cortesia/Carla_resultado_gracias.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'muchas gracias', 'Carla_resultado_muchas gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-cortesia/Carla_resultado_muchas%20gracias.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'mucho gusto', 'Carla_resultado_mucho gusto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-cortesia/Carla_resultado_mucho%20gusto.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'permiso', 'Carla_resultado_permiso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-cortesia/Carla_resultado_permiso.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - dias_semana (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'domingo', 'Carla_resultado_domingo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-dias_semana/Carla_resultado_domingo.glb', 3.40, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'jueves', 'Carla_resultado_jueves.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-dias_semana/Carla_resultado_jueves.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'lunes', 'Carla_resultado_lunes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-dias_semana/Carla_resultado_lunes.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'martes', 'Carla_resultado_martes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-dias_semana/Carla_resultado_martes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'miercoles', 'Carla_resultado_miercoles.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-dias_semana/Carla_resultado_miercoles.glb', 3.47, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'sabado', 'Carla_resultado_sabado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-dias_semana/Carla_resultado_sabado.glb', 3.41, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'viernes', 'Carla_resultado_viernes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-dias_semana/Carla_resultado_viernes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - estado civil (6 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'casado', 'Carla_resultado_casado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-estado civil/Carla_resultado_casado.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'concubino', 'Carla_resultado_concubino.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-estado civil/Carla_resultado_concubino.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'divorciado', 'Carla_resultado_divorciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-estado civil/Carla_resultado_divorciado.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'separado', 'Carla_resultado_separado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-estado civil/Carla_resultado_separado.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'soltero', 'Carla_resultado_soltero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-estado civil/Carla_resultado_soltero.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'viudo', 'Carla_resultado_viudo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-estado civil/Carla_resultado_viudo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - expresiones (30 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'abril', 'Carla_resultado_abril.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_abril.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'agosto', 'Carla_resultado_agosto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_agosto.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'bien', 'Carla_resultado_bien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_bien.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'como', 'Carla_resultado_como.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_como.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'cual', 'Carla_resultado_cual.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_cual.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'cuando', 'Carla_resultado_cuando.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_cuando.glb', 3.41, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'cuantos', 'Carla_resultado_cuantos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_cuantos.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'de nada', 'Carla_resultado_de nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_de%20nada.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'diciembre', 'Carla_resultado_diciembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_diciembre.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'donde (especifico)', 'Carla_resultado_donde (especifico).glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_donde%20(especifico).glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'donde', 'Carla_resultado_donde.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_donde.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'enero', 'Carla_resultado_enero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_enero.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'expresiones', 'Carla_resultado_expresiones.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_expresiones.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'febrero', 'Carla_resultado_febrero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_febrero.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'interrogantes', 'Carla_resultado_interrogantes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_interrogantes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'julio', 'Carla_resultado_julio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_julio.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'junio', 'Carla_resultado_junio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_junio.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'mal', 'Carla_resultado_mal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_mal.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'marzo', 'Carla_resultado_marzo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_marzo.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'mayo', 'Carla_resultado_mayo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_mayo.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'no', 'Carla_resultado_no.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_no.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'noviembre', 'Carla_resultado_noviembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_noviembre.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'octubre', 'Carla_resultado_octubre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_octubre.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'porque', 'Carla_resultado_porque.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_porque.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'que', 'Carla_resultado_que.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_que.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'quien', 'Carla_resultado_quien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_quien.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'regular', 'Carla_resultado_regular.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_regular.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'saludas a', 'Carla_resultado_saludas a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_saludas%20a.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'septiembre', 'Carla_resultado_septiembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_septiembre.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'si', 'Carla_resultado_si.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-expresiones/Carla_resultado_si.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - horario (8 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'en punto', 'Carla_resultado_en punto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-horario/Carla_resultado_en%20punto.glb', 3.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'hora', 'Carla_resultado_hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-horario/Carla_resultado_hora.glb', 3.35, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'horario', 'Carla_resultado_horario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-horario/Carla_resultado_horario.glb', 3.41, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'media hora', 'Carla_resultado_media hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-horario/Carla_resultado_media%20hora.glb', 3.38, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'un cuarto', 'Carla_resultado_un cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-horario/Carla_resultado_un%20cuarto.glb', 3.34, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'un minuto', 'Carla_resultado_un minuto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-horario/Carla_resultado_un%20minuto.glb', 3.37, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'un segundo', 'Carla_resultado_un segundo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-horario/Carla_resultado_un%20segundo.glb', 3.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'una hora', 'Carla_resultado_una hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-horario/Carla_resultado_una%20hora.glb', 3.40, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - medios transporte (0 archivos)
-- Carla - numero (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '0', 'Carla_resultado_0.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_0.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '1', 'Carla_resultado_1.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_1.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '10', 'Carla_resultado_10.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_10.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '1M', 'Carla_resultado_1M.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_1M.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '2', 'Carla_resultado_2.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_2.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '3', 'Carla_resultado_3.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_3.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '4', 'Carla_resultado_4.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_4.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '5', 'Carla_resultado_5.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_5.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '6', 'Carla_resultado_6.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_6.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '7', 'Carla_resultado_7.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_7.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '8', 'Carla_resultado_8.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_8.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '9', 'Carla_resultado_9.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numero/Carla_resultado_9.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - numeros ordinales (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '10_o', 'Carla_resultado_10_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numeros ordinales/Carla_resultado_10_o.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '1_o', 'Carla_resultado_1_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numeros ordinales/Carla_resultado_1_o.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '2_o', 'Carla_resultado_2_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numeros ordinales/Carla_resultado_2_o.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '3_o', 'Carla_resultado_3_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numeros ordinales/Carla_resultado_3_o.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '4_o', 'Carla_resultado_4_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numeros ordinales/Carla_resultado_4_o.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '5_o', 'Carla_resultado_5_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numeros ordinales/Carla_resultado_5_o.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '6_o', 'Carla_resultado_6_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numeros ordinales/Carla_resultado_6_o.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '7_o', 'Carla_resultado_7_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numeros ordinales/Carla_resultado_7_o.glb', 12.44, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '8_o', 'Carla_resultado_8_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numeros ordinales/Carla_resultado_8_o.glb', 12.54, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '9_o', 'Carla_resultado_9_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-numeros ordinales/Carla_resultado_9_o.glb', 12.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - personas (22 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'adulto', 'Carla_resultado_adulto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_adulto.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'amigo', 'Carla_resultado_amigo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_amigo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'anciano', 'Carla_resultado_anciano.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_anciano.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'bebe', 'Carla_resultado_bebe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_bebe.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'ciego', 'Carla_resultado_ciego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_ciego.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'compañero', 'Carla_resultado_compañero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_compa%C3%B1ero.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'hombre', 'Carla_resultado_hombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_hombre.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'joven', 'Carla_resultado_joven.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_joven.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'mayor de edad', 'Carla_resultado_mayor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_mayor%20de%20edad.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'mayor', 'Carla_resultado_mayor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_mayor.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'menor de edad', 'Carla_resultado_menor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_menor%20de%20edad.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'mujer', 'Carla_resultado_mujer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_mujer.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'niño', 'Carla_resultado_niño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_ni%C3%B1o.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'novio', 'Carla_resultado_novio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_novio.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'oyente', 'Carla_resultado_oyente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_oyente.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'persona', 'Carla_resultado_persona.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_persona.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'personas', 'Carla_resultado_personas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_personas.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'señor', 'Carla_resultado_señor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_se%C3%B1or.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'señorita', 'Carla_resultado_señorita.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_se%C3%B1orita.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'sordo', 'Carla_resultado_sordo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_sordo.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'sordociego', 'Carla_resultado_sordociego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_sordociego.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'viejo', 'Carla_resultado_viejo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-personas/Carla_resultado_viejo.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - preguntas (4 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preguntas', 'como estas', 'Carla_resultado_como estas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preguntas/Carla_resultado_como%20estas.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preguntas', 'cual es tu nombre', 'Carla_resultado_cual es tu nombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preguntas/Carla_resultado_cual%20es%20tu%20nombre.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preguntas', 'cual es tu seña', 'Carla_resultado_cual es tu seña.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preguntas/Carla_resultado_cual%20es%20tu%20se%C3%B1a.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preguntas', 'que tal', 'Carla_resultado_que tal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preguntas/Carla_resultado_que%20tal.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - preposicion (15 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'algo', 'Carla_resultado_algo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_algo.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'alguien', 'Carla_resultado_alguien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_alguien.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'algun', 'Carla_resultado_algun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_algun.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'bastante', 'Carla_resultado_bastante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_bastante.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'cualquier', 'Carla_resultado_cualquier.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_cualquier.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'demasiado', 'Carla_resultado_demasiado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_demasiado.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'mas', 'Carla_resultado_mas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_mas.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'mucho', 'Carla_resultado_mucho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_mucho.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'nada', 'Carla_resultado_nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_nada.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'nadie', 'Carla_resultado_nadie.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_nadie.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'ningun', 'Carla_resultado_ningun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_ningun.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'otro', 'Carla_resultado_otro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_otro.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'poco', 'Carla_resultado_poco.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_poco.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'quienquiera', 'Carla_resultado_quienquiera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_quienquiera.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'todo', 'Carla_resultado_todo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-preposicion/Carla_resultado_todo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - profesion (47 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'abogado', 'Carla_resultado_abogado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_abogado.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'administrador', 'Carla_resultado_administrador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_administrador.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'albañil', 'Carla_resultado_albañil.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_alba%C3%B1il.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'analista', 'Carla_resultado_analista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_analista.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'auxiliar', 'Carla_resultado_auxiliar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_auxiliar.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'barbero', 'Carla_resultado_barbero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_barbero.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'carrera', 'Carla_resultado_carrera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_carrera.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'chef', 'Carla_resultado_chef.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_chef.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'cocinero', 'Carla_resultado_cocinero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_cocinero.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'conductor', 'Carla_resultado_conductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_conductor.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'constructor', 'Carla_resultado_constructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_constructor.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'contador', 'Carla_resultado_contador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_contador.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'dentista', 'Carla_resultado_dentista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_dentista.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'detective', 'Carla_resultado_detective.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_detective.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'dibujante tecnico', 'Carla_resultado_dibujante tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_dibujante%20tecnico.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'dibujante', 'Carla_resultado_dibujante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_dibujante.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'director', 'Carla_resultado_director.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_director.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'economista', 'Carla_resultado_economista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_economista.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'enfermera', 'Carla_resultado_enfermera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_enfermera.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'escritor', 'Carla_resultado_escritor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_escritor.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'fotografo', 'Carla_resultado_fotografo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_fotografo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'gerente', 'Carla_resultado_gerente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_gerente.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'informatica', 'Carla_resultado_informatica.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_informatica.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'ingeniero', 'Carla_resultado_ingeniero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_ingeniero.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'inspector', 'Carla_resultado_inspector.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_inspector.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'instructor', 'Carla_resultado_instructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_instructor.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'interprete', 'Carla_resultado_interprete.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_interprete.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'jefe', 'Carla_resultado_jefe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_jefe.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'licenciado', 'Carla_resultado_licenciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_licenciado.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'maestro', 'Carla_resultado_maestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_maestro.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'medico', 'Carla_resultado_medico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_medico.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'mensajero', 'Carla_resultado_mensajero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_mensajero.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'mesonero', 'Carla_resultado_mesonero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_mesonero.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'pasante', 'Carla_resultado_pasante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_pasante.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'peluquera', 'Carla_resultado_peluquera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_peluquera.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'pintor', 'Carla_resultado_pintor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_pintor.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'policia', 'Carla_resultado_policia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_policia.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'profesion', 'Carla_resultado_profesion.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_profesion.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'profesor', 'Carla_resultado_profesor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_profesor.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'psicologo', 'Carla_resultado_psicologo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_psicologo.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'secretaria', 'Carla_resultado_secretaria.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_secretaria.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'sistema', 'Carla_resultado_sistema.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_sistema.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'supervisor', 'Carla_resultado_supervisor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_supervisor.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'tecnico', 'Carla_resultado_tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_tecnico.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'traductor', 'Carla_resultado_traductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_traductor.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'vendedor', 'Carla_resultado_vendedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_vendedor.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'vigilante', 'Carla_resultado_vigilante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-profesion/Carla_resultado_vigilante.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - pronombres (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'el', 'Carla_resultado_el.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_el.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'ella', 'Carla_resultado_ella.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_ella.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'ellas', 'Carla_resultado_ellas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_ellas.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'ellos', 'Carla_resultado_ellos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_ellos.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'mio', 'Carla_resultado_mio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_mio.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'nosotros', 'Carla_resultado_nosotros.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_nosotros.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'nuestro', 'Carla_resultado_nuestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_nuestro.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'suyo', 'Carla_resultado_suyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_suyo.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'tu', 'Carla_resultado_tu.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_tu.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'tuyo', 'Carla_resultado_tuyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_tuyo.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'ustedes', 'Carla_resultado_ustedes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_ustedes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'yo', 'Carla_resultado_yo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-pronombres/Carla_resultado_yo.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - saludos (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'adios', 'Carla_resultado_adios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-saludos/Carla_resultado_adios.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'bienvenido', 'Carla_resultado_bienvenido.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-saludos/Carla_resultado_bienvenido.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'buenas noches', 'Carla_resultado_buenas noches.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-saludos/Carla_resultado_buenas%20noches.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'buenas tardes', 'Carla_resultado_buenas tardes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-saludos/Carla_resultado_buenas%20tardes.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'buenos dias', 'Carla_resultado_buenos dias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-saludos/Carla_resultado_buenos%20dias.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'chao', 'Carla_resultado_chao.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-saludos/Carla_resultado_chao.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'hola', 'Carla_resultado_hola.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-saludos/Carla_resultado_hola.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - tiempo (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'anteayer', 'Carla_resultado_anteayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tiempo/Carla_resultado_anteayer.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'ayer', 'Carla_resultado_ayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tiempo/Carla_resultado_ayer.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'calendario', 'Carla_resultado_calendario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tiempo/Carla_resultado_calendario.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'dia', 'Carla_resultado_dia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tiempo/Carla_resultado_dia.glb', 3.35, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'fin de semana', 'Carla_resultado_fin de semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tiempo/Carla_resultado_fin%20de%20semana.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'hoy', 'Carla_resultado_hoy.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tiempo/Carla_resultado_hoy.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'mañana', 'Carla_resultado_mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tiempo/Carla_resultado_ma%C3%B1ana.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'mes', 'Carla_resultado_mes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tiempo/Carla_resultado_mes.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'pasado mañana', 'Carla_resultado_pasado mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tiempo/Carla_resultado_pasado%20ma%C3%B1ana.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'semana', 'Carla_resultado_semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tiempo/Carla_resultado_semana.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - tipos de vivienda (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'apartamento', 'Carla_resultado_apartamento.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tipos de vivienda/Carla_resultado_apartamento.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'baño', 'Carla_resultado_baño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tipos de vivienda/Carla_resultado_ba%C3%B1o.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'casa', 'Carla_resultado_casa.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tipos de vivienda/Carla_resultado_casa.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'cocina', 'Carla_resultado_cocina.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tipos de vivienda/Carla_resultado_cocina.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'comedor', 'Carla_resultado_comedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tipos de vivienda/Carla_resultado_comedor.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'cuarto', 'Carla_resultado_cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tipos de vivienda/Carla_resultado_cuarto.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'edificio', 'Carla_resultado_edificio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tipos de vivienda/Carla_resultado_edificio.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'piso', 'Carla_resultado_piso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tipos de vivienda/Carla_resultado_piso.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'rancho', 'Carla_resultado_rancho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tipos de vivienda/Carla_resultado_rancho.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'sala', 'Carla_resultado_sala.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-tipos de vivienda/Carla_resultado_sala.glb', 3.15, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - verbos (35 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'agarrar', 'Carla_resultado_agarrar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_agarrar.glb', 3.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'amar', 'Carla_resultado_amar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_amar.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'atraer', 'Carla_resultado_atraer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_atraer.glb', 3.23, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'ayudar', 'Carla_resultado_ayudar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_ayudar.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'burlar', 'Carla_resultado_burlar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_burlar.glb', 3.29, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'calmar', 'Carla_resultado_calmar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_calmar.glb', 4.00, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'cansar', 'Carla_resultado_cansar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_cansar.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'comer', 'Carla_resultado_comer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_comer.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'conocer', 'Carla_resultado_conocer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_conocer.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'decir', 'Carla_resultado_decir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_decir.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'deletrear', 'Carla_resultado_deletrear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_deletrear.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'dormir', 'Carla_resultado_dormir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_dormir.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'engañar', 'Carla_resultado_engañar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_enga%C3%B1ar.glb', 3.20, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'estar', 'Carla_resultado_estar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_estar.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'estudiar', 'Carla_resultado_estudiar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_estudiar.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'guardar', 'Carla_resultado_guardar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_guardar.glb', 3.28, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'invitar', 'Carla_resultado_invitar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_invitar.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'llevar', 'Carla_resultado_llevar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_llevar.glb', 3.26, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'pelear', 'Carla_resultado_pelear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_pelear.glb', 3.27, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'preguntar', 'Carla_resultado_preguntar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_preguntar.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'presentar', 'Carla_resultado_presentar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_presentar.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'querer', 'Carla_resultado_querer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_querer.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'regalar', 'Carla_resultado_regalar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_regalar.glb', 3.26, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'responder', 'Carla_resultado_responder.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_responder.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'saludar', 'Carla_resultado_saludar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_saludar.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'sentir', 'Carla_resultado_sentir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_sentir.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'ser', 'Carla_resultado_ser.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_ser.glb', 3.22, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'sufrir', 'Carla_resultado_sufrir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_sufrir.glb', 3.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'trabajar', 'Carla_resultado_trabajar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_trabajar.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'traer', 'Carla_resultado_traer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_traer.glb', 3.25, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'usar', 'Carla_resultado_usar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_usar.glb', 3.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'ver', 'Carla_resultado_ver.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_ver.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'verbo', 'Carla_resultado_verbo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_verbo.glb', 4.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'vestir', 'Carla_resultado_vestir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_vestir.glb', 3.30, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'vivir', 'Carla_resultado_vivir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-carla-verbos/Carla_resultado_vivir.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Cultura - base (6 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Cultura', 'base', 'luz', 'Argenis_luz.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-cultura-base/Argenis_luz.glb', 2.90, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Cultura', 'base', 'luz', 'Carla_luz.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-cultura-base/Carla_luz.glb', 3.97, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Cultura', 'base', 'luz', 'Duvall_luz.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-cultura-base/Duvall_luz.glb', 2.99, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Cultura', 'base', 'escena', 'escena.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-cultura-base/escena.glb', 1.57, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Cultura', 'base', 'luz', 'Luis_luz.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-cultura-base/Luis_luz.glb', 3.00, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Cultura', 'base', 'luz', 'Nancy_luz.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-cultura-base/Nancy_luz.glb', 3.02, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - adverbios lugares (9 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'adverbios', 'Duvall_resultado_adverbios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-adverbios lugares/Duvall_resultado_adverbios.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'al lado', 'Duvall_resultado_al lado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-adverbios lugares/Duvall_resultado_al%20lado.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'atras', 'Duvall_resultado_atras.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-adverbios lugares/Duvall_resultado_atras.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'cerca', 'Duvall_resultado_cerca.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-adverbios lugares/Duvall_resultado_cerca.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'derecha', 'Duvall_resultado_derecha.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-adverbios lugares/Duvall_resultado_derecha.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'frente', 'Duvall_resultado_frente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-adverbios lugares/Duvall_resultado_frente.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'izquierda', 'Duvall_resultado_izquierda.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-adverbios lugares/Duvall_resultado_izquierda.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'lejos', 'Duvall_resultado_lejos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-adverbios lugares/Duvall_resultado_lejos.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'lugares', 'Duvall_resultado_lugares.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-adverbios lugares/Duvall_resultado_lugares.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - alfabeto (27 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'a', 'Duvall_resultado_a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_a.glb', 2.83, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'b', 'Duvall_resultado_b.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_b.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'c', 'Duvall_resultado_c.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_c.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'd', 'Duvall_resultado_d.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_d.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'e', 'Duvall_resultado_e.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_e.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'f', 'Duvall_resultado_f.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_f.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'g', 'Duvall_resultado_g.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_g.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'h', 'Duvall_resultado_h.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_h.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'i', 'Duvall_resultado_i.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_i.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'j', 'Duvall_resultado_j.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_j.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'k', 'Duvall_resultado_k.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_k.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'l', 'Duvall_resultado_l.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_l.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'm', 'Duvall_resultado_m.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_m.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'n', 'Duvall_resultado_n.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_n.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'o', 'Duvall_resultado_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_o.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'p', 'Duvall_resultado_p.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_p.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'q', 'Duvall_resultado_q.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_q.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'r', 'Duvall_resultado_r.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_r.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 's', 'Duvall_resultado_s.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_s.glb', 3.00, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 't', 'Duvall_resultado_t.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_t.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'u', 'Duvall_resultado_u.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_u.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'v', 'Duvall_resultado_v.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_v.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'w', 'Duvall_resultado_w.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_w.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'x', 'Duvall_resultado_x.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_x.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'y', 'Duvall_resultado_y.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_y.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'z', 'Duvall_resultado_z.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_z.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'ñ', 'Duvall_resultado_ñ.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-alfabeto/Duvall_resultado_%C3%B1.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - cortesia (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'a la orden', 'Duvall_resultado_a la orden.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-cortesia/Duvall_resultado_a%20la%20orden.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'buen provecho', 'Duvall_resultado_buen provecho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-cortesia/Duvall_resultado_buen%20provecho.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'cortesia', 'Duvall_resultado_cortesia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-cortesia/Duvall_resultado_cortesia.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'gracias', 'Duvall_resultado_gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-cortesia/Duvall_resultado_gracias.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'muchas gracias', 'Duvall_resultado_muchas gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-cortesia/Duvall_resultado_muchas%20gracias.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'mucho gusto', 'Duvall_resultado_mucho gusto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-cortesia/Duvall_resultado_mucho%20gusto.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'permiso', 'Duvall_resultado_permiso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-cortesia/Duvall_resultado_permiso.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - dias_semana (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'domingo', 'Duvall_resultado_domingo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-dias_semana/Duvall_resultado_domingo.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'jueves', 'Duvall_resultado_jueves.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-dias_semana/Duvall_resultado_jueves.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'lunes', 'Duvall_resultado_lunes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-dias_semana/Duvall_resultado_lunes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'martes', 'Duvall_resultado_martes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-dias_semana/Duvall_resultado_martes.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'miercoles', 'Duvall_resultado_miercoles.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-dias_semana/Duvall_resultado_miercoles.glb', 2.91, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'sabado', 'Duvall_resultado_sabado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-dias_semana/Duvall_resultado_sabado.glb', 2.88, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'viernes', 'Duvall_resultado_viernes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-dias_semana/Duvall_resultado_viernes.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - base (1 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'base', 'base', 'Duvall.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-base/Duvall.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - estado civil (6 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'casado', 'Duvall_resultado_casado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-estado civil/Duvall_resultado_casado.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'concubino', 'Duvall_resultado_concubino.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-estado civil/Duvall_resultado_concubino.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'divorciado', 'Duvall_resultado_divorciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-estado civil/Duvall_resultado_divorciado.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'separado', 'Duvall_resultado_separado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-estado civil/Duvall_resultado_separado.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'soltero', 'Duvall_resultado_soltero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-estado civil/Duvall_resultado_soltero.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'viudo', 'Duvall_resultado_viudo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-estado civil/Duvall_resultado_viudo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - expresiones (30 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'abril', 'Duvall_resultado_abril.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_abril.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'agosto', 'Duvall_resultado_agosto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_agosto.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'bien', 'Duvall_resultado_bien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_bien.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'como', 'Duvall_resultado_como.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_como.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'cual', 'Duvall_resultado_cual.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_cual.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'cuando', 'Duvall_resultado_cuando.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_cuando.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'cuantos', 'Duvall_resultado_cuantos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_cuantos.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'de nada', 'Duvall_resultado_de nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_de%20nada.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'diciembre', 'Duvall_resultado_diciembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_diciembre.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'donde (especifico)', 'Duvall_resultado_donde (especifico).glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_donde%20(especifico).glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'donde', 'Duvall_resultado_donde.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_donde.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'enero', 'Duvall_resultado_enero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_enero.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'expresiones', 'Duvall_resultado_expresiones.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_expresiones.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'febrero', 'Duvall_resultado_febrero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_febrero.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'interrogantes', 'Duvall_resultado_interrogantes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_interrogantes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'julio', 'Duvall_resultado_julio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_julio.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'junio', 'Duvall_resultado_junio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_junio.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'mal', 'Duvall_resultado_mal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_mal.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'marzo', 'Duvall_resultado_marzo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_marzo.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'mayo', 'Duvall_resultado_mayo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_mayo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'no', 'Duvall_resultado_no.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_no.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'noviembre', 'Duvall_resultado_noviembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_noviembre.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'octubre', 'Duvall_resultado_octubre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_octubre.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'porque', 'Duvall_resultado_porque.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_porque.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'que', 'Duvall_resultado_que.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_que.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'quien', 'Duvall_resultado_quien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_quien.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'regular', 'Duvall_resultado_regular.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_regular.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'saludas a', 'Duvall_resultado_saludas a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_saludas%20a.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'septiembre', 'Duvall_resultado_septiembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_septiembre.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'si', 'Duvall_resultado_si.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-expresiones/Duvall_resultado_si.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - horario (8 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'en punto', 'Duvall_resultado_en punto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-horario/Duvall_resultado_en%20punto.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'hora', 'Duvall_resultado_hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-horario/Duvall_resultado_hora.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'horario', 'Duvall_resultado_horario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-horario/Duvall_resultado_horario.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'media hora', 'Duvall_resultado_media hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-horario/Duvall_resultado_media%20hora.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'un cuarto', 'Duvall_resultado_un cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-horario/Duvall_resultado_un%20cuarto.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'un minuto', 'Duvall_resultado_un minuto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-horario/Duvall_resultado_un%20minuto.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'un segundo', 'Duvall_resultado_un segundo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-horario/Duvall_resultado_un%20segundo.glb', 3.04, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'una hora', 'Duvall_resultado_una hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-horario/Duvall_resultado_una%20hora.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - medios transporte (0 archivos)
-- Duvall - numero (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '0', 'Duvall_resultado_0.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_0.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '1', 'Duvall_resultado_1.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_1.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '10', 'Duvall_resultado_10.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_10.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '1M', 'Duvall_resultado_1M.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_1M.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '2', 'Duvall_resultado_2.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_2.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '3', 'Duvall_resultado_3.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_3.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '4', 'Duvall_resultado_4.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_4.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '5', 'Duvall_resultado_5.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_5.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '6', 'Duvall_resultado_6.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_6.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '7', 'Duvall_resultado_7.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_7.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '8', 'Duvall_resultado_8.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_8.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '9', 'Duvall_resultado_9.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numero/Duvall_resultado_9.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - numeros ordinales (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '10_o', 'Duvall_resultado_10_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numeros ordinales/Duvall_resultado_10_o.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '1_o', 'Duvall_resultado_1_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numeros ordinales/Duvall_resultado_1_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '2_o', 'Duvall_resultado_2_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numeros ordinales/Duvall_resultado_2_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '3_o', 'Duvall_resultado_3_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numeros ordinales/Duvall_resultado_3_o.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '4_o', 'Duvall_resultado_4_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numeros ordinales/Duvall_resultado_4_o.glb', 11.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '5_o', 'Duvall_resultado_5_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numeros ordinales/Duvall_resultado_5_o.glb', 11.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '6_o', 'Duvall_resultado_6_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numeros ordinales/Duvall_resultado_6_o.glb', 11.98, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '7_o', 'Duvall_resultado_7_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numeros ordinales/Duvall_resultado_7_o.glb', 12.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '8_o', 'Duvall_resultado_8_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numeros ordinales/Duvall_resultado_8_o.glb', 12.17, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '9_o', 'Duvall_resultado_9_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-numeros ordinales/Duvall_resultado_9_o.glb', 12.28, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - personas (22 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'adulto', 'Duvall_resultado_adulto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_adulto.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'amigo', 'Duvall_resultado_amigo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_amigo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'anciano', 'Duvall_resultado_anciano.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_anciano.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'bebe', 'Duvall_resultado_bebe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_bebe.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'ciego', 'Duvall_resultado_ciego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_ciego.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'compañero', 'Duvall_resultado_compañero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_compa%C3%B1ero.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'hombre', 'Duvall_resultado_hombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_hombre.glb', 2.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'joven', 'Duvall_resultado_joven.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_joven.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'mayor de edad', 'Duvall_resultado_mayor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_mayor%20de%20edad.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'mayor', 'Duvall_resultado_mayor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_mayor.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'menor de edad', 'Duvall_resultado_menor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_menor%20de%20edad.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'mujer', 'Duvall_resultado_mujer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_mujer.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'niño', 'Duvall_resultado_niño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_ni%C3%B1o.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'novio', 'Duvall_resultado_novio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_novio.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'oyente', 'Duvall_resultado_oyente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_oyente.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'persona', 'Duvall_resultado_persona.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_persona.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'personas', 'Duvall_resultado_personas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_personas.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'señor', 'Duvall_resultado_señor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_se%C3%B1or.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'señorita', 'Duvall_resultado_señorita.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_se%C3%B1orita.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'sordo', 'Duvall_resultado_sordo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_sordo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'sordociego', 'Duvall_resultado_sordociego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_sordociego.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'viejo', 'Duvall_resultado_viejo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-personas/Duvall_resultado_viejo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - preguntas (4 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preguntas', 'como estas', 'Duvall_resultado_como estas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preguntas/Duvall_resultado_como%20estas.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preguntas', 'cual es tu nombre', 'Duvall_resultado_cual es tu nombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preguntas/Duvall_resultado_cual%20es%20tu%20nombre.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preguntas', 'cual es tu seña', 'Duvall_resultado_cual es tu seña.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preguntas/Duvall_resultado_cual%20es%20tu%20se%C3%B1a.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preguntas', 'que tal', 'Duvall_resultado_que tal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preguntas/Duvall_resultado_que%20tal.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - preposicion (15 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'algo', 'Duvall_resultado_algo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_algo.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'alguien', 'Duvall_resultado_alguien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_alguien.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'algun', 'Duvall_resultado_algun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_algun.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'bastante', 'Duvall_resultado_bastante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_bastante.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'cualquier', 'Duvall_resultado_cualquier.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_cualquier.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'demasiado', 'Duvall_resultado_demasiado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_demasiado.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'mas', 'Duvall_resultado_mas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_mas.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'mucho', 'Duvall_resultado_mucho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_mucho.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'nada', 'Duvall_resultado_nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_nada.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'nadie', 'Duvall_resultado_nadie.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_nadie.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'ningun', 'Duvall_resultado_ningun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_ningun.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'otro', 'Duvall_resultado_otro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_otro.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'poco', 'Duvall_resultado_poco.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_poco.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'quienquiera', 'Duvall_resultado_quienquiera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_quienquiera.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'todo', 'Duvall_resultado_todo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-preposicion/Duvall_resultado_todo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - profesion (47 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'abogado', 'Duvall_resultado_abogado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_abogado.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'administrador', 'Duvall_resultado_administrador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_administrador.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'albañil', 'Duvall_resultado_albañil.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_alba%C3%B1il.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'analista', 'Duvall_resultado_analista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_analista.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'auxiliar', 'Duvall_resultado_auxiliar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_auxiliar.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'barbero', 'Duvall_resultado_barbero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_barbero.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'carrera', 'Duvall_resultado_carrera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_carrera.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'chef', 'Duvall_resultado_chef.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_chef.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'cocinero', 'Duvall_resultado_cocinero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_cocinero.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'conductor', 'Duvall_resultado_conductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_conductor.glb', 2.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'constructor', 'Duvall_resultado_constructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_constructor.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'contador', 'Duvall_resultado_contador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_contador.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'dentista', 'Duvall_resultado_dentista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_dentista.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'detective', 'Duvall_resultado_detective.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_detective.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'dibujante tecnico', 'Duvall_resultado_dibujante tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_dibujante%20tecnico.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'dibujante', 'Duvall_resultado_dibujante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_dibujante.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'director', 'Duvall_resultado_director.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_director.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'economista', 'Duvall_resultado_economista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_economista.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'enfermera', 'Duvall_resultado_enfermera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_enfermera.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'escritor', 'Duvall_resultado_escritor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_escritor.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'fotografo', 'Duvall_resultado_fotografo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_fotografo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'gerente', 'Duvall_resultado_gerente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_gerente.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'informatica', 'Duvall_resultado_informatica.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_informatica.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'ingeniero', 'Duvall_resultado_ingeniero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_ingeniero.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'inspector', 'Duvall_resultado_inspector.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_inspector.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'instructor', 'Duvall_resultado_instructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_instructor.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'interprete', 'Duvall_resultado_interprete.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_interprete.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'jefe', 'Duvall_resultado_jefe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_jefe.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'licenciado', 'Duvall_resultado_licenciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_licenciado.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'maestro', 'Duvall_resultado_maestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_maestro.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'medico', 'Duvall_resultado_medico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_medico.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'mensajero', 'Duvall_resultado_mensajero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_mensajero.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'mesonero', 'Duvall_resultado_mesonero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_mesonero.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'pasante', 'Duvall_resultado_pasante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_pasante.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'peluquera', 'Duvall_resultado_peluquera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_peluquera.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'pintor', 'Duvall_resultado_pintor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_pintor.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'policia', 'Duvall_resultado_policia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_policia.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'profesion', 'Duvall_resultado_profesion.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_profesion.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'profesor', 'Duvall_resultado_profesor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_profesor.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'psicologo', 'Duvall_resultado_psicologo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_psicologo.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'secretaria', 'Duvall_resultado_secretaria.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_secretaria.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'sistema', 'Duvall_resultado_sistema.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_sistema.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'supervisor', 'Duvall_resultado_supervisor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_supervisor.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'tecnico', 'Duvall_resultado_tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_tecnico.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'traductor', 'Duvall_resultado_traductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_traductor.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'vendedor', 'Duvall_resultado_vendedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_vendedor.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'vigilante', 'Duvall_resultado_vigilante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-profesion/Duvall_resultado_vigilante.glb', 2.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - pronombres (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'el', 'Duvall_resultado_el.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_el.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'ella', 'Duvall_resultado_ella.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_ella.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'ellas', 'Duvall_resultado_ellas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_ellas.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'ellos', 'Duvall_resultado_ellos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_ellos.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'mio', 'Duvall_resultado_mio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_mio.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'nosotros', 'Duvall_resultado_nosotros.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_nosotros.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'nuestro', 'Duvall_resultado_nuestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_nuestro.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'suyo', 'Duvall_resultado_suyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_suyo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'tu', 'Duvall_resultado_tu.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_tu.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'tuyo', 'Duvall_resultado_tuyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_tuyo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'ustedes', 'Duvall_resultado_ustedes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_ustedes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'yo', 'Duvall_resultado_yo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-pronombres/Duvall_resultado_yo.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - saludos (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'adios', 'Duvall_resultado_adios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-saludos/Duvall_resultado_adios.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'bienvenido', 'Duvall_resultado_bienvenido.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-saludos/Duvall_resultado_bienvenido.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'buenas noches', 'Duvall_resultado_buenas noches.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-saludos/Duvall_resultado_buenas%20noches.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'buenas tardes', 'Duvall_resultado_buenas tardes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-saludos/Duvall_resultado_buenas%20tardes.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'buenos dias', 'Duvall_resultado_buenos dias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-saludos/Duvall_resultado_buenos%20dias.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'chao', 'Duvall_resultado_chao.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-saludos/Duvall_resultado_chao.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'hola', 'Duvall_resultado_hola.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-saludos/Duvall_resultado_hola.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - tiempo (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'anteayer', 'Duvall_resultado_anteayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tiempo/Duvall_resultado_anteayer.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'ayer', 'Duvall_resultado_ayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tiempo/Duvall_resultado_ayer.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'calendario', 'Duvall_resultado_calendario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tiempo/Duvall_resultado_calendario.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'dia', 'Duvall_resultado_dia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tiempo/Duvall_resultado_dia.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'fin de semana', 'Duvall_resultado_fin de semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tiempo/Duvall_resultado_fin%20de%20semana.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'hoy', 'Duvall_resultado_hoy.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tiempo/Duvall_resultado_hoy.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'mañana', 'Duvall_resultado_mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tiempo/Duvall_resultado_ma%C3%B1ana.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'mes', 'Duvall_resultado_mes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tiempo/Duvall_resultado_mes.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'pasado mañana', 'Duvall_resultado_pasado mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tiempo/Duvall_resultado_pasado%20ma%C3%B1ana.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'semana', 'Duvall_resultado_semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tiempo/Duvall_resultado_semana.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - tipos de vivienda (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'apartamento', 'Duvall_resultado_apartamento.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tipos de vivienda/Duvall_resultado_apartamento.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'baño', 'Duvall_resultado_baño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tipos de vivienda/Duvall_resultado_ba%C3%B1o.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'casa', 'Duvall_resultado_casa.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tipos de vivienda/Duvall_resultado_casa.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'cocina', 'Duvall_resultado_cocina.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tipos de vivienda/Duvall_resultado_cocina.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'comedor', 'Duvall_resultado_comedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tipos de vivienda/Duvall_resultado_comedor.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'cuarto', 'Duvall_resultado_cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tipos de vivienda/Duvall_resultado_cuarto.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'edificio', 'Duvall_resultado_edificio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tipos de vivienda/Duvall_resultado_edificio.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'piso', 'Duvall_resultado_piso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tipos de vivienda/Duvall_resultado_piso.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'rancho', 'Duvall_resultado_rancho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tipos de vivienda/Duvall_resultado_rancho.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'sala', 'Duvall_resultado_sala.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-tipos de vivienda/Duvall_resultado_sala.glb', 2.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - verbos (35 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'agarrar', 'Duvall_resultado_agarrar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_agarrar.glb', 4.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'amar', 'Duvall_resultado_amar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_amar.glb', 3.00, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'atraer', 'Duvall_resultado_atraer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_atraer.glb', 4.34, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'ayudar', 'Duvall_resultado_ayudar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_ayudar.glb', 2.94, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'burlar', 'Duvall_resultado_burlar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_burlar.glb', 4.40, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'calmar', 'Duvall_resultado_calmar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_calmar.glb', 4.49, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'cansar', 'Duvall_resultado_cansar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_cansar.glb', 2.97, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'comer', 'Duvall_resultado_comer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_comer.glb', 3.00, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'conocer', 'Duvall_resultado_conocer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_conocer.glb', 2.95, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'decir', 'Duvall_resultado_decir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_decir.glb', 2.96, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'deletrear', 'Duvall_resultado_deletrear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_deletrear.glb', 2.93, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'dormir', 'Duvall_resultado_dormir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_dormir.glb', 2.95, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'engañar', 'Duvall_resultado_engañar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_enga%C3%B1ar.glb', 4.30, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'estar', 'Duvall_resultado_estar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_estar.glb', 2.94, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'estudiar', 'Duvall_resultado_estudiar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_estudiar.glb', 2.94, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'guardar', 'Duvall_resultado_guardar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_guardar.glb', 4.39, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'invitar', 'Duvall_resultado_invitar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_invitar.glb', 2.97, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'llevar', 'Duvall_resultado_llevar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_llevar.glb', 4.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'pelear', 'Duvall_resultado_pelear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_pelear.glb', 4.38, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'preguntar', 'Duvall_resultado_preguntar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_preguntar.glb', 2.95, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'presentar', 'Duvall_resultado_presentar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_presentar.glb', 2.94, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'querer', 'Duvall_resultado_querer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_querer.glb', 2.96, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'regalar', 'Duvall_resultado_regalar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_regalar.glb', 4.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'responder', 'Duvall_resultado_responder.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_responder.glb', 2.97, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'saludar', 'Duvall_resultado_saludar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_saludar.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'sentir', 'Duvall_resultado_sentir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_sentir.glb', 2.99, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'ser', 'Duvall_resultado_ser.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_ser.glb', 4.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'sufrir', 'Duvall_resultado_sufrir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_sufrir.glb', 4.44, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'trabajar', 'Duvall_resultado_trabajar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_trabajar.glb', 2.95, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'traer', 'Duvall_resultado_traer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_traer.glb', 4.35, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'usar', 'Duvall_resultado_usar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_usar.glb', 4.43, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'ver', 'Duvall_resultado_ver.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_ver.glb', 2.97, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'verbo', 'Duvall_resultado_verbo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_verbo.glb', 4.37, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'vestir', 'Duvall_resultado_vestir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_vestir.glb', 4.42, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'vivir', 'Duvall_resultado_vivir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-duvall-verbos/Duvall_resultado_vivir.glb', 2.93, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - adverbios lugares (9 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'adverbios lugares', 'adverbios', 'Luis_resultado_adverbios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-adverbios lugares/Luis_resultado_adverbios.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'adverbios lugares', 'al lado', 'Luis_resultado_al lado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-adverbios lugares/Luis_resultado_al%20lado.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'adverbios lugares', 'atras', 'Luis_resultado_atras.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-adverbios lugares/Luis_resultado_atras.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'adverbios lugares', 'cerca', 'Luis_resultado_cerca.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-adverbios lugares/Luis_resultado_cerca.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'adverbios lugares', 'derecha', 'Luis_resultado_derecha.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-adverbios lugares/Luis_resultado_derecha.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'adverbios lugares', 'frente', 'Luis_resultado_frente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-adverbios lugares/Luis_resultado_frente.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'adverbios lugares', 'izquierda', 'Luis_resultado_izquierda.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-adverbios lugares/Luis_resultado_izquierda.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'adverbios lugares', 'lejos', 'Luis_resultado_lejos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-adverbios lugares/Luis_resultado_lejos.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'adverbios lugares', 'lugares', 'Luis_resultado_lugares.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-adverbios lugares/Luis_resultado_lugares.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - alfabeto (31 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'a', 'Luis_resultado_a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_a.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'b', 'Luis_resultado_b.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_b.glb', 2.72, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'c', 'Luis_resultado_c.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_c.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'd', 'Luis_resultado_d.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_d.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'e', 'Luis_resultado_e.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_e.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'f', 'Luis_resultado_f.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_f.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'g', 'Luis_resultado_g.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_g.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'h', 'Luis_resultado_h.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_h.glb', 2.74, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'i', 'Luis_resultado_i.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_i.glb', 2.72, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'j', 'Luis_resultado_j.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_j.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'k', 'Luis_resultado_k.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_k.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'modif', 'Luis_resultado_k_modif.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_k_modif.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'l', 'Luis_resultado_l.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_l.glb', 2.72, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'm', 'Luis_resultado_m.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_m.glb', 2.72, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'n', 'Luis_resultado_n.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_n.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'o', 'Luis_resultado_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_o.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'p', 'Luis_resultado_p.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_p.glb', 2.72, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'q', 'Luis_resultado_q.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_q.glb', 2.74, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'r', 'Luis_resultado_r.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_r.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'modif', 'Luis_resultado_r_modif.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_r_modif.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 's', 'Luis_resultado_s.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_s.glb', 2.74, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 's1', 'Luis_resultado_s1.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_s1.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 's2', 'Luis_resultado_s2.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_s2.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 't', 'Luis_resultado_t.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_t.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'u', 'Luis_resultado_u.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_u.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'v', 'Luis_resultado_v.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_v.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'w', 'Luis_resultado_w.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_w.glb', 2.74, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'x', 'Luis_resultado_x.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_x.glb', 2.74, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'y', 'Luis_resultado_y.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_y.glb', 2.74, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'z', 'Luis_resultado_z.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_z.glb', 2.73, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'alfabeto', 'ñ', 'Luis_resultado_ñ.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-alfabeto/Luis_resultado_%C3%B1.glb', 2.72, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - cortesia (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'cortesia', 'a la orden', 'Luis_resultado_a la orden.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-cortesia/Luis_resultado_a%20la%20orden.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'cortesia', 'buen provecho', 'Luis_resultado_buen provecho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-cortesia/Luis_resultado_buen%20provecho.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'cortesia', 'cortesia', 'Luis_resultado_cortesia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-cortesia/Luis_resultado_cortesia.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'cortesia', 'gracias', 'Luis_resultado_gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-cortesia/Luis_resultado_gracias.glb', 2.72, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'cortesia', 'muchas gracias', 'Luis_resultado_muchas gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-cortesia/Luis_resultado_muchas%20gracias.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'cortesia', 'mucho gusto', 'Luis_resultado_mucho gusto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-cortesia/Luis_resultado_mucho%20gusto.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'cortesia', 'permiso', 'Luis_resultado_permiso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-cortesia/Luis_resultado_permiso.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - dias_semana (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'dias_semana', 'domingo', 'Luis_resultado_domingo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-dias_semana/Luis_resultado_domingo.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'dias_semana', 'jueves', 'Luis_resultado_jueves.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-dias_semana/Luis_resultado_jueves.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'dias_semana', 'lunes', 'Luis_resultado_lunes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-dias_semana/Luis_resultado_lunes.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'dias_semana', 'martes', 'Luis_resultado_martes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-dias_semana/Luis_resultado_martes.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'dias_semana', 'miercoles', 'Luis_resultado_miercoles.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-dias_semana/Luis_resultado_miercoles.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'dias_semana', 'sabado', 'Luis_resultado_sabado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-dias_semana/Luis_resultado_sabado.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'dias_semana', 'viernes', 'Luis_resultado_viernes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-dias_semana/Luis_resultado_viernes.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - estado civil (6 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'estado civil', 'casado', 'Luis_resultado_casado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-estado civil/Luis_resultado_casado.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'estado civil', 'concubino', 'Luis_resultado_concubino.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-estado civil/Luis_resultado_concubino.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'estado civil', 'divorciado', 'Luis_resultado_divorciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-estado civil/Luis_resultado_divorciado.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'estado civil', 'separado', 'Luis_resultado_separado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-estado civil/Luis_resultado_separado.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'estado civil', 'soltero', 'Luis_resultado_soltero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-estado civil/Luis_resultado_soltero.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'estado civil', 'viudo', 'Luis_resultado_viudo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-estado civil/Luis_resultado_viudo.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - expresiones (30 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'abril', 'Luis_resultado_abril.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_abril.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'agosto', 'Luis_resultado_agosto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_agosto.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'bien', 'Luis_resultado_bien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_bien.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'como', 'Luis_resultado_como.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_como.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'cual', 'Luis_resultado_cual.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_cual.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'cuando', 'Luis_resultado_cuando.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_cuando.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'cuantos', 'Luis_resultado_cuantos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_cuantos.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'de nada', 'Luis_resultado_de nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_de%20nada.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'diciembre', 'Luis_resultado_diciembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_diciembre.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'donde (especifico)', 'Luis_resultado_donde (especifico).glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_donde%20(especifico).glb', 2.72, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'donde', 'Luis_resultado_donde.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_donde.glb', 2.72, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'enero', 'Luis_resultado_enero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_enero.glb', 2.72, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'expresiones', 'Luis_resultado_expresiones.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_expresiones.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'febrero', 'Luis_resultado_febrero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_febrero.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'interrogantes', 'Luis_resultado_interrogantes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_interrogantes.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'julio', 'Luis_resultado_julio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_julio.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'junio', 'Luis_resultado_junio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_junio.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'mal', 'Luis_resultado_mal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_mal.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'marzo', 'Luis_resultado_marzo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_marzo.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'mayo', 'Luis_resultado_mayo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_mayo.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'no', 'Luis_resultado_no.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_no.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'noviembre', 'Luis_resultado_noviembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_noviembre.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'octubre', 'Luis_resultado_octubre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_octubre.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'porque', 'Luis_resultado_porque.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_porque.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'que', 'Luis_resultado_que.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_que.glb', 2.72, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'quien', 'Luis_resultado_quien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_quien.glb', 2.72, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'regular', 'Luis_resultado_regular.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_regular.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'saludas a', 'Luis_resultado_saludas a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_saludas%20a.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'septiembre', 'Luis_resultado_septiembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_septiembre.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'expresiones', 'si', 'Luis_resultado_si.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-expresiones/Luis_resultado_si.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - base (1 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'base', 'base', 'Luis.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-base/Luis.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - medios transporte (0 archivos)
-- Luis - numero (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '0', 'Luis_resultado_0.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_0.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '1', 'Luis_resultado_1.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_1.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '10', 'Luis_resultado_10.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_10.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '1M', 'Luis_resultado_1M.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_1M.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '2', 'Luis_resultado_2.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_2.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '3', 'Luis_resultado_3.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_3.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '4', 'Luis_resultado_4.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_4.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '5', 'Luis_resultado_5.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_5.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '6', 'Luis_resultado_6.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_6.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '7', 'Luis_resultado_7.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_7.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '8', 'Luis_resultado_8.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_8.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numero', '9', 'Luis_resultado_9.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numero/Luis_resultado_9.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - numeros ordinales (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numeros ordinales', '10_o', 'Luis_resultado_10_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numeros ordinales/Luis_resultado_10_o.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numeros ordinales', '1_o', 'Luis_resultado_1_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numeros ordinales/Luis_resultado_1_o.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numeros ordinales', '2_o', 'Luis_resultado_2_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numeros ordinales/Luis_resultado_2_o.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numeros ordinales', '3_o', 'Luis_resultado_3_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numeros ordinales/Luis_resultado_3_o.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numeros ordinales', '4_o', 'Luis_resultado_4_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numeros ordinales/Luis_resultado_4_o.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numeros ordinales', '5_o', 'Luis_resultado_5_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numeros ordinales/Luis_resultado_5_o.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numeros ordinales', '6_o', 'Luis_resultado_6_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numeros ordinales/Luis_resultado_6_o.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numeros ordinales', '7_o', 'Luis_resultado_7_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numeros ordinales/Luis_resultado_7_o.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numeros ordinales', '8_o', 'Luis_resultado_8_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numeros ordinales/Luis_resultado_8_o.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'numeros ordinales', '9_o', 'Luis_resultado_9_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-numeros ordinales/Luis_resultado_9_o.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - personas (22 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'adulto', 'Luis_resultado_adulto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_adulto.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'amigo', 'Luis_resultado_amigo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_amigo.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'anciano', 'Luis_resultado_anciano.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_anciano.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'bebe', 'Luis_resultado_bebe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_bebe.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'ciego', 'Luis_resultado_ciego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_ciego.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'compañero', 'Luis_resultado_compañero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_compa%C3%B1ero.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'hombre', 'Luis_resultado_hombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_hombre.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'joven', 'Luis_resultado_joven.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_joven.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'mayor de edad', 'Luis_resultado_mayor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_mayor%20de%20edad.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'mayor', 'Luis_resultado_mayor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_mayor.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'menor de edad', 'Luis_resultado_menor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_menor%20de%20edad.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'mujer', 'Luis_resultado_mujer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_mujer.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'niño', 'Luis_resultado_niño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_ni%C3%B1o.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'novio', 'Luis_resultado_novio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_novio.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'oyente', 'Luis_resultado_oyente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_oyente.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'persona', 'Luis_resultado_persona.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_persona.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'personas', 'Luis_resultado_personas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_personas.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'señor', 'Luis_resultado_señor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_se%C3%B1or.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'señorita', 'Luis_resultado_señorita.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_se%C3%B1orita.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'sordo', 'Luis_resultado_sordo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_sordo.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'sordociego', 'Luis_resultado_sordociego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_sordociego.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'personas', 'viejo', 'Luis_resultado_viejo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-personas/Luis_resultado_viejo.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - preguntas (6 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preguntas', 'como estas', 'Luis_resultado_como estas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preguntas/Luis_resultado_como%20estas.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preguntas', 'como estas_CONGELADO', 'Luis_resultado_como estas_CONGELADO.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preguntas/Luis_resultado_como%20estas_CONGELADO.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preguntas', 'cual es tu nombre', 'Luis_resultado_cual es tu nombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preguntas/Luis_resultado_cual%20es%20tu%20nombre.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preguntas', 'cual es tu nombre_CONGELADO', 'Luis_resultado_cual es tu nombre_CONGELADO.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preguntas/Luis_resultado_cual%20es%20tu%20nombre_CONGELADO.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preguntas', 'cual es tu sena', 'Luis_resultado_cual es tu sena.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preguntas/Luis_resultado_cual%20es%20tu%20sena.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preguntas', 'que tal', 'Luis_resultado_que tal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preguntas/Luis_resultado_que%20tal.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - preposicion (14 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'algo', 'Luis_resultado_algo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_algo.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'alguien', 'Luis_resultado_alguien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_alguien.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'algun', 'Luis_resultado_algun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_algun.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'bastante', 'Luis_resultado_bastante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_bastante.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'cualquier', 'Luis_resultado_cualquier.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_cualquier.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'demasiado', 'Luis_resultado_demasiado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_demasiado.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'mucho', 'Luis_resultado_mucho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_mucho.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'nada', 'Luis_resultado_nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_nada.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'nadie', 'Luis_resultado_nadie.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_nadie.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'ningun', 'Luis_resultado_ningun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_ningun.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'otro', 'Luis_resultado_otro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_otro.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'poco', 'Luis_resultado_poco.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_poco.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'quienquiera', 'Luis_resultado_quienquiera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_quienquiera.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'preposicion', 'todo', 'Luis_resultado_todo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-preposicion/Luis_resultado_todo.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - profesion (47 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'abogado', 'Luis_resultado_abogado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_abogado.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'administrador', 'Luis_resultado_administrador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_administrador.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'albañil', 'Luis_resultado_albañil.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_alba%C3%B1il.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'analista', 'Luis_resultado_analista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_analista.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'auxiliar', 'Luis_resultado_auxiliar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_auxiliar.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'barbero', 'Luis_resultado_barbero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_barbero.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'carrera', 'Luis_resultado_carrera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_carrera.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'chef', 'Luis_resultado_chef.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_chef.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'cocinero', 'Luis_resultado_cocinero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_cocinero.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'conductor', 'Luis_resultado_conductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_conductor.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'constructor', 'Luis_resultado_constructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_constructor.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'contador', 'Luis_resultado_contador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_contador.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'dentista', 'Luis_resultado_dentista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_dentista.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'detective', 'Luis_resultado_detective.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_detective.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'dibujante tecnico', 'Luis_resultado_dibujante tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_dibujante%20tecnico.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'dibujante', 'Luis_resultado_dibujante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_dibujante.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'director', 'Luis_resultado_director.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_director.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'economista', 'Luis_resultado_economista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_economista.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'enfermera', 'Luis_resultado_enfermera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_enfermera.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'escritor', 'Luis_resultado_escritor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_escritor.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'fotografo', 'Luis_resultado_fotografo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_fotografo.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'gerente', 'Luis_resultado_gerente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_gerente.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'informatica', 'Luis_resultado_informatica.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_informatica.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'ingeniero', 'Luis_resultado_ingeniero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_ingeniero.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'inspector', 'Luis_resultado_inspector.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_inspector.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'instructor', 'Luis_resultado_instructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_instructor.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'interprete', 'Luis_resultado_interprete.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_interprete.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'jefe', 'Luis_resultado_jefe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_jefe.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'licenciado', 'Luis_resultado_licenciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_licenciado.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'maestro', 'Luis_resultado_maestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_maestro.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'medico', 'Luis_resultado_medico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_medico.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'mensajero', 'Luis_resultado_mensajero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_mensajero.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'mesonero', 'Luis_resultado_mesonero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_mesonero.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'pasante', 'Luis_resultado_pasante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_pasante.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'peluquera', 'Luis_resultado_peluquera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_peluquera.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'pintor', 'Luis_resultado_pintor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_pintor.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'policia', 'Luis_resultado_policia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_policia.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'profesion', 'Luis_resultado_profesion.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_profesion.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'profesor', 'Luis_resultado_profesor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_profesor.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'psicologo', 'Luis_resultado_psicologo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_psicologo.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'secretaria', 'Luis_resultado_secretaria.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_secretaria.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'sistema', 'Luis_resultado_sistema.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_sistema.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'supervisor', 'Luis_resultado_supervisor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_supervisor.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'tecnico', 'Luis_resultado_tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_tecnico.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'traductor', 'Luis_resultado_traductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_traductor.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'vendedor', 'Luis_resultado_vendedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_vendedor.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'profesion', 'vigilante', 'Luis_resultado_vigilante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-profesion/Luis_resultado_vigilante.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - pronombres (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'el', 'Luis_resultado_el.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_el.glb', 2.72, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'ella', 'Luis_resultado_ella.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_ella.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'ellas', 'Luis_resultado_ellas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_ellas.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'ellos', 'Luis_resultado_ellos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_ellos.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'mio', 'Luis_resultado_mio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_mio.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'nosotros', 'Luis_resultado_nosotros.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_nosotros.glb', 2.72, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'nuestro', 'Luis_resultado_nuestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_nuestro.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'suyo', 'Luis_resultado_suyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_suyo.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'tu', 'Luis_resultado_tu.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_tu.glb', 2.72, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'tuyo', 'Luis_resultado_tuyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_tuyo.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'ustedes', 'Luis_resultado_ustedes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_ustedes.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'pronombres', 'yo', 'Luis_resultado_yo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-pronombres/Luis_resultado_yo.glb', 2.72, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - saludos (8 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'saludos', 'adios', 'Luis_resultado_adios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-saludos/Luis_resultado_adios.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'saludos', 'bienvenido', 'Luis_resultado_bienvenido.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-saludos/Luis_resultado_bienvenido.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'saludos', 'buenas noches', 'Luis_resultado_buenas noches.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-saludos/Luis_resultado_buenas%20noches.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'saludos', 'buenas tardes', 'Luis_resultado_buenas tardes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-saludos/Luis_resultado_buenas%20tardes.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'saludos', 'buenos dias', 'Luis_resultado_buenos dias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-saludos/Luis_resultado_buenos%20dias.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'saludos', 'chao', 'Luis_resultado_chao.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-saludos/Luis_resultado_chao.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'saludos', 'hola', 'Luis_resultado_hola.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-saludos/Luis_resultado_hola.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'saludos', '_temp_Luis_resultado_bienvenido', '_temp_Luis_resultado_bienvenido.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-saludos/_temp_Luis_resultado_bienvenido.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - tiempo (9 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tiempo', 'anteayer', 'Luis_resultado_anteayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tiempo/Luis_resultado_anteayer.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tiempo', 'ayer', 'Luis_resultado_ayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tiempo/Luis_resultado_ayer.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tiempo', 'calendario', 'Luis_resultado_calendario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tiempo/Luis_resultado_calendario.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tiempo', 'fin de semana', 'Luis_resultado_fin de semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tiempo/Luis_resultado_fin%20de%20semana.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tiempo', 'hoy', 'Luis_resultado_hoy.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tiempo/Luis_resultado_hoy.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tiempo', 'manana', 'Luis_resultado_manana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tiempo/Luis_resultado_manana.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tiempo', 'mes', 'Luis_resultado_mes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tiempo/Luis_resultado_mes.glb', 2.72, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tiempo', 'pasado manana', 'Luis_resultado_pasado manana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tiempo/Luis_resultado_pasado%20manana.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tiempo', 'semana', 'Luis_resultado_semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tiempo/Luis_resultado_semana.glb', 2.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - tipos de vivienda (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tipos de vivienda', 'apartamento', 'Luis_resultado_apartamento.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tipos de vivienda/Luis_resultado_apartamento.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tipos de vivienda', 'baño', 'Luis_resultado_baño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tipos de vivienda/Luis_resultado_ba%C3%B1o.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tipos de vivienda', 'casa', 'Luis_resultado_casa.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tipos de vivienda/Luis_resultado_casa.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tipos de vivienda', 'cocina', 'Luis_resultado_cocina.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tipos de vivienda/Luis_resultado_cocina.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tipos de vivienda', 'comedor', 'Luis_resultado_comedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tipos de vivienda/Luis_resultado_comedor.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tipos de vivienda', 'cuarto', 'Luis_resultado_cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tipos de vivienda/Luis_resultado_cuarto.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tipos de vivienda', 'edificio', 'Luis_resultado_edificio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tipos de vivienda/Luis_resultado_edificio.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tipos de vivienda', 'piso', 'Luis_resultado_piso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tipos de vivienda/Luis_resultado_piso.glb', 2.74, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tipos de vivienda', 'rancho', 'Luis_resultado_rancho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tipos de vivienda/Luis_resultado_rancho.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'tipos de vivienda', 'sala', 'Luis_resultado_sala.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-tipos de vivienda/Luis_resultado_sala.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Luis - verbos (20 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'amar', 'Luis_resultado_amar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_amar.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'ayudar', 'Luis_resultado_ayudar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_ayudar.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'cansar', 'Luis_resultado_cansar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_cansar.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'comer', 'Luis_resultado_comer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_comer.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'conocer', 'Luis_resultado_conocer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_conocer.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'decir', 'Luis_resultado_decir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_decir.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'deletrear', 'Luis_resultado_deletrear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_deletrear.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'dormir', 'Luis_resultado_dormir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_dormir.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'estar', 'Luis_resultado_estar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_estar.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'estudiar', 'Luis_resultado_estudiar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_estudiar.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'invitar', 'Luis_resultado_invitar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_invitar.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'preguntar', 'Luis_resultado_preguntar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_preguntar.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'presentar', 'Luis_resultado_presentar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_presentar.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'querer', 'Luis_resultado_querer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_querer.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'responder', 'Luis_resultado_responder.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_responder.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'saludar', 'Luis_resultado_saludar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_saludar.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'sentir', 'Luis_resultado_sentir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_sentir.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'trabajar', 'Luis_resultado_trabajar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_trabajar.glb', 2.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'ver', 'Luis_resultado_ver.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_ver.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Luis', 'verbos', 'vivir', 'Luis_resultado_vivir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-luis-verbos/Luis_resultado_vivir.glb', 2.75, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Modif - personas (20 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'anciano', 'Duvall_resultado_anciano.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_anciano.glb', 12.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'bebe', 'Duvall_resultado_bebe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_bebe.glb', 12.73, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'ciego', 'Duvall_resultado_ciego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_ciego.glb', 12.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'compañero', 'Duvall_resultado_compañero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_compa%C3%B1ero.glb', 12.93, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'hombre', 'Duvall_resultado_hombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_hombre.glb', 13.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'joven', 'Duvall_resultado_joven.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_joven.glb', 13.22, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'mayor de edad', 'Duvall_resultado_mayor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_mayor%20de%20edad.glb', 13.34, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'mayor', 'Duvall_resultado_mayor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_mayor.glb', 13.47, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'menor de edad', 'Duvall_resultado_menor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_menor%20de%20edad.glb', 13.58, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'mujer', 'Duvall_resultado_mujer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_mujer.glb', 13.70, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'niño', 'Duvall_resultado_niño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_ni%C3%B1o.glb', 13.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'novio', 'Duvall_resultado_novio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_novio.glb', 13.98, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'oyente', 'Duvall_resultado_oyente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_oyente.glb', 14.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'persona', 'Duvall_resultado_persona.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_persona.glb', 14.18, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'personas', 'Duvall_resultado_personas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_personas.glb', 14.28, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'señor', 'Duvall_resultado_señor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_se%C3%B1or.glb', 14.41, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'señorita', 'Duvall_resultado_señorita.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_se%C3%B1orita.glb', 14.52, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'sordo', 'Duvall_resultado_sordo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_sordo.glb', 14.63, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'sordociego', 'Duvall_resultado_sordociego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_sordociego.glb', 14.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'personas', 'viejo', 'Duvall_resultado_viejo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-personas/Duvall_resultado_viejo.glb', 14.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Modif - preguntas (4 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preguntas', 'como estas', 'Duvall_resultado_como estas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preguntas/Duvall_resultado_como%20estas.glb', 14.96, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preguntas', 'cual es tu nombre', 'Duvall_resultado_cual es tu nombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preguntas/Duvall_resultado_cual%20es%20tu%20nombre.glb', 15.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preguntas', 'cual es tu sena', 'Duvall_resultado_cual es tu sena.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preguntas/Duvall_resultado_cual%20es%20tu%20sena.glb', 15.23, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preguntas', 'que tal', 'Duvall_resultado_que tal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preguntas/Duvall_resultado_que%20tal.glb', 15.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Modif - preposicion (15 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'algo', 'Duvall_resultado_algo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_algo.glb', 15.40, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'alguien', 'Duvall_resultado_alguien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_alguien.glb', 15.53, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'algun', 'Duvall_resultado_algun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_algun.glb', 15.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'bastante', 'Duvall_resultado_bastante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_bastante.glb', 15.76, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'cualquier', 'Duvall_resultado_cualquier.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_cualquier.glb', 15.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'demasiado', 'Duvall_resultado_demasiado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_demasiado.glb', 15.98, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'mas', 'Duvall_resultado_mas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_mas.glb', 16.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'mucho', 'Duvall_resultado_mucho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_mucho.glb', 16.23, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'nada', 'Duvall_resultado_nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_nada.glb', 16.35, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'nadie', 'Duvall_resultado_nadie.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_nadie.glb', 16.45, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'ningun', 'Duvall_resultado_ningun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_ningun.glb', 16.56, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'otro', 'Duvall_resultado_otro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_otro.glb', 16.66, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'poco', 'Duvall_resultado_poco.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_poco.glb', 16.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'quienquiera', 'Duvall_resultado_quienquiera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_quienquiera.glb', 16.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'preposicion', 'todo', 'Duvall_resultado_todo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-preposicion/Duvall_resultado_todo.glb', 16.98, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Modif - profesion (29 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'abogado', 'Duvall_resultado_abogado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_abogado.glb', 17.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'administrador', 'Duvall_resultado_administrador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_administrador.glb', 17.25, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'albañil', 'Duvall_resultado_albañil.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_alba%C3%B1il.glb', 17.38, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'analista', 'Duvall_resultado_analista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_analista.glb', 17.52, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'auxiliar', 'Duvall_resultado_auxiliar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_auxiliar.glb', 17.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'barbero', 'Duvall_resultado_barbero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_barbero.glb', 17.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'carrera', 'Duvall_resultado_carrera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_carrera.glb', 17.90, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'chef', 'Duvall_resultado_chef.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_chef.glb', 18.02, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'cocinero', 'Duvall_resultado_cocinero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_cocinero.glb', 18.16, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'conductor', 'Duvall_resultado_conductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_conductor.glb', 18.30, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'constructor', 'Duvall_resultado_constructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_constructor.glb', 18.44, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'contador', 'Duvall_resultado_contador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_contador.glb', 18.56, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'dentista', 'Duvall_resultado_dentista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_dentista.glb', 18.68, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'detective', 'Duvall_resultado_detective.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_detective.glb', 18.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'dibujante tecnico', 'Duvall_resultado_dibujante tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_dibujante%20tecnico.glb', 18.93, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'dibujante', 'Duvall_resultado_dibujante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_dibujante.glb', 19.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'director', 'Duvall_resultado_director.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_director.glb', 19.17, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'economista', 'Duvall_resultado_economista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_economista.glb', 19.31, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'enfermera', 'Duvall_resultado_enfermera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_enfermera.glb', 19.43, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'escritor', 'Duvall_resultado_escritor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_escritor.glb', 19.54, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'fotografo', 'Duvall_resultado_fotografo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_fotografo.glb', 19.65, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'gerente', 'Duvall_resultado_gerente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_gerente.glb', 19.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'informatica', 'Duvall_resultado_informatica.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_informatica.glb', 19.92, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'ingeniero', 'Duvall_resultado_ingeniero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_ingeniero.glb', 20.04, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'inspector', 'Duvall_resultado_inspector.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_inspector.glb', 20.19, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'instructor', 'Duvall_resultado_instructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_instructor.glb', 20.29, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'interprete', 'Duvall_resultado_interprete.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_interprete.glb', 20.42, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'jefe', 'Duvall_resultado_jefe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_jefe.glb', 20.53, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Modif', 'profesion', 'licenciado', 'Duvall_resultado_licenciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-modif-profesion/Duvall_resultado_licenciado.glb', 20.68, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - adverbios lugares (9 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'adverbios lugares', 'adverbios', 'Nancy_resultado_adverbios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-adverbios lugares/Nancy_resultado_adverbios.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'adverbios lugares', 'al lado', 'Nancy_resultado_al lado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-adverbios lugares/Nancy_resultado_al%20lado.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'adverbios lugares', 'atras', 'Nancy_resultado_atras.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-adverbios lugares/Nancy_resultado_atras.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'adverbios lugares', 'cerca', 'Nancy_resultado_cerca.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-adverbios lugares/Nancy_resultado_cerca.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'adverbios lugares', 'derecha', 'Nancy_resultado_derecha.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-adverbios lugares/Nancy_resultado_derecha.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'adverbios lugares', 'frente', 'Nancy_resultado_frente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-adverbios lugares/Nancy_resultado_frente.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'adverbios lugares', 'izquierda', 'Nancy_resultado_izquierda.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-adverbios lugares/Nancy_resultado_izquierda.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'adverbios lugares', 'lejos', 'Nancy_resultado_lejos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-adverbios lugares/Nancy_resultado_lejos.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'adverbios lugares', 'lugares', 'Nancy_resultado_lugares.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-adverbios lugares/Nancy_resultado_lugares.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - alfabeto (27 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'a', 'Nancy_resultado_a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_a.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'b', 'Nancy_resultado_b.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_b.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'c', 'Nancy_resultado_c.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_c.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'd', 'Nancy_resultado_d.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_d.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'e', 'Nancy_resultado_e.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_e.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'f', 'Nancy_resultado_f.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_f.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'g', 'Nancy_resultado_g.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_g.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'h', 'Nancy_resultado_h.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_h.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'i', 'Nancy_resultado_i.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_i.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'j', 'Nancy_resultado_j.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_j.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'k', 'Nancy_resultado_k.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_k.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'l', 'Nancy_resultado_l.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_l.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'm', 'Nancy_resultado_m.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_m.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'n', 'Nancy_resultado_n.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_n.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'o', 'Nancy_resultado_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_o.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'p', 'Nancy_resultado_p.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_p.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'q', 'Nancy_resultado_q.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_q.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'r', 'Nancy_resultado_r.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_r.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 's', 'Nancy_resultado_s.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_s.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 't', 'Nancy_resultado_t.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_t.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'u', 'Nancy_resultado_u.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_u.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'v', 'Nancy_resultado_v.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_v.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'w', 'Nancy_resultado_w.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_w.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'x', 'Nancy_resultado_x.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_x.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'y', 'Nancy_resultado_y.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_y.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'z', 'Nancy_resultado_z.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_z.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'alfabeto', 'ñ', 'Nancy_resultado_ñ.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-alfabeto/Nancy_resultado_%C3%B1.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - cortesia (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'cortesia', 'a la orden', 'Nancy_resultado_a la orden.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-cortesia/Nancy_resultado_a%20la%20orden.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'cortesia', 'buen provecho', 'Nancy_resultado_buen provecho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-cortesia/Nancy_resultado_buen%20provecho.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'cortesia', 'cortesia', 'Nancy_resultado_cortesia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-cortesia/Nancy_resultado_cortesia.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'cortesia', 'gracias', 'Nancy_resultado_gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-cortesia/Nancy_resultado_gracias.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'cortesia', 'muchas gracias', 'Nancy_resultado_muchas gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-cortesia/Nancy_resultado_muchas%20gracias.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'cortesia', 'mucho gusto', 'Nancy_resultado_mucho gusto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-cortesia/Nancy_resultado_mucho%20gusto.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'cortesia', 'permiso', 'Nancy_resultado_permiso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-cortesia/Nancy_resultado_permiso.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - dias_semana (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'dias_semana', 'domingo', 'Nancy_resultado_domingo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-dias_semana/Nancy_resultado_domingo.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'dias_semana', 'jueves', 'Nancy_resultado_jueves.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-dias_semana/Nancy_resultado_jueves.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'dias_semana', 'lunes', 'Nancy_resultado_lunes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-dias_semana/Nancy_resultado_lunes.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'dias_semana', 'martes', 'Nancy_resultado_martes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-dias_semana/Nancy_resultado_martes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'dias_semana', 'miercoles', 'Nancy_resultado_miercoles.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-dias_semana/Nancy_resultado_miercoles.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'dias_semana', 'sabado', 'Nancy_resultado_sabado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-dias_semana/Nancy_resultado_sabado.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'dias_semana', 'viernes', 'Nancy_resultado_viernes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-dias_semana/Nancy_resultado_viernes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - estado civil (6 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'estado civil', 'casado', 'Nancy_resultado_casado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-estado civil/Nancy_resultado_casado.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'estado civil', 'concubino', 'Nancy_resultado_concubino.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-estado civil/Nancy_resultado_concubino.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'estado civil', 'divorciado', 'Nancy_resultado_divorciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-estado civil/Nancy_resultado_divorciado.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'estado civil', 'separado', 'Nancy_resultado_separado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-estado civil/Nancy_resultado_separado.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'estado civil', 'soltero', 'Nancy_resultado_soltero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-estado civil/Nancy_resultado_soltero.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'estado civil', 'viudo', 'Nancy_resultado_viudo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-estado civil/Nancy_resultado_viudo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - expresiones (30 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'abril', 'Nancy_resultado_abril.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_abril.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'agosto', 'Nancy_resultado_agosto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_agosto.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'bien', 'Nancy_resultado_bien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_bien.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'como', 'Nancy_resultado_como.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_como.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'cual', 'Nancy_resultado_cual.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_cual.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'cuando', 'Nancy_resultado_cuando.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_cuando.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'cuantos', 'Nancy_resultado_cuantos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_cuantos.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'de nada', 'Nancy_resultado_de nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_de%20nada.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'diciembre', 'Nancy_resultado_diciembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_diciembre.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'donde (especifico)', 'Nancy_resultado_donde (especifico).glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_donde%20(especifico).glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'donde', 'Nancy_resultado_donde.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_donde.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'enero', 'Nancy_resultado_enero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_enero.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'expresiones', 'Nancy_resultado_expresiones.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_expresiones.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'febrero', 'Nancy_resultado_febrero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_febrero.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'interrogantes', 'Nancy_resultado_interrogantes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_interrogantes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'julio', 'Nancy_resultado_julio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_julio.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'junio', 'Nancy_resultado_junio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_junio.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'mal', 'Nancy_resultado_mal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_mal.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'marzo', 'Nancy_resultado_marzo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_marzo.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'mayo', 'Nancy_resultado_mayo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_mayo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'no', 'Nancy_resultado_no.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_no.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'noviembre', 'Nancy_resultado_noviembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_noviembre.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'octubre', 'Nancy_resultado_octubre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_octubre.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'porque', 'Nancy_resultado_porque.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_porque.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'que', 'Nancy_resultado_que.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_que.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'quien', 'Nancy_resultado_quien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_quien.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'regular', 'Nancy_resultado_regular.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_regular.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'saludas a', 'Nancy_resultado_saludas a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_saludas%20a.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'septiembre', 'Nancy_resultado_septiembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_septiembre.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'expresiones', 'si', 'Nancy_resultado_si.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-expresiones/Nancy_resultado_si.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - medios transporte (0 archivos)
-- Nancy - base (1 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'base', 'base', 'Nancy.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-base/Nancy.glb', 2.77, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - numero (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '0', 'Nancy_resultado_0.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_0.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '1', 'Nancy_resultado_1.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_1.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '10', 'Nancy_resultado_10.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_10.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '1M', 'Nancy_resultado_1M.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_1M.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '2', 'Nancy_resultado_2.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_2.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '3', 'Nancy_resultado_3.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_3.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '4', 'Nancy_resultado_4.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_4.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '5', 'Nancy_resultado_5.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_5.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '6', 'Nancy_resultado_6.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_6.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '7', 'Nancy_resultado_7.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_7.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '8', 'Nancy_resultado_8.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_8.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numero', '9', 'Nancy_resultado_9.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numero/Nancy_resultado_9.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - numeros ordinales (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numeros ordinales', '10_o', 'Nancy_resultado_10_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numeros ordinales/Nancy_resultado_10_o.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numeros ordinales', '1_o', 'Nancy_resultado_1_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numeros ordinales/Nancy_resultado_1_o.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numeros ordinales', '2_o', 'Nancy_resultado_2_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numeros ordinales/Nancy_resultado_2_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numeros ordinales', '3_o', 'Nancy_resultado_3_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numeros ordinales/Nancy_resultado_3_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numeros ordinales', '4_o', 'Nancy_resultado_4_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numeros ordinales/Nancy_resultado_4_o.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numeros ordinales', '5_o', 'Nancy_resultado_5_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numeros ordinales/Nancy_resultado_5_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numeros ordinales', '6_o', 'Nancy_resultado_6_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numeros ordinales/Nancy_resultado_6_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numeros ordinales', '7_o', 'Nancy_resultado_7_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numeros ordinales/Nancy_resultado_7_o.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numeros ordinales', '8_o', 'Nancy_resultado_8_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numeros ordinales/Nancy_resultado_8_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'numeros ordinales', '9_o', 'Nancy_resultado_9_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-numeros ordinales/Nancy_resultado_9_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - personas (22 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'adulto', 'Nancy_resultado_adulto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_adulto.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'amigo', 'Nancy_resultado_amigo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_amigo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'anciano', 'Nancy_resultado_anciano.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_anciano.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'bebe', 'Nancy_resultado_bebe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_bebe.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'ciego', 'Nancy_resultado_ciego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_ciego.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'compañero', 'Nancy_resultado_compañero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_compa%C3%B1ero.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'hombre', 'Nancy_resultado_hombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_hombre.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'joven', 'Nancy_resultado_joven.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_joven.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'mayor de edad', 'Nancy_resultado_mayor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_mayor%20de%20edad.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'mayor', 'Nancy_resultado_mayor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_mayor.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'menor de edad', 'Nancy_resultado_menor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_menor%20de%20edad.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'mujer', 'Nancy_resultado_mujer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_mujer.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'niño', 'Nancy_resultado_niño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_ni%C3%B1o.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'novio', 'Nancy_resultado_novio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_novio.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'oyente', 'Nancy_resultado_oyente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_oyente.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'persona', 'Nancy_resultado_persona.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_persona.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'personas', 'Nancy_resultado_personas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_personas.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'señor', 'Nancy_resultado_señor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_se%C3%B1or.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'señorita', 'Nancy_resultado_señorita.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_se%C3%B1orita.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'sordo', 'Nancy_resultado_sordo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_sordo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'sordociego', 'Nancy_resultado_sordociego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_sordociego.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'personas', 'viejo', 'Nancy_resultado_viejo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-personas/Nancy_resultado_viejo.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - preguntas (4 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preguntas', 'como estas', 'Nancy_resultado_como estas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preguntas/Nancy_resultado_como%20estas.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preguntas', 'cual es tu nombre', 'Nancy_resultado_cual es tu nombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preguntas/Nancy_resultado_cual%20es%20tu%20nombre.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preguntas', 'cual es tu sena', 'Nancy_resultado_cual es tu sena.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preguntas/Nancy_resultado_cual%20es%20tu%20sena.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preguntas', 'que tal', 'Nancy_resultado_que tal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preguntas/Nancy_resultado_que%20tal.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - preposicion (14 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'algo', 'Nancy_resultado_algo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_algo.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'alguien', 'Nancy_resultado_alguien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_alguien.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'algun', 'Nancy_resultado_algun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_algun.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'bastante', 'Nancy_resultado_bastante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_bastante.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'cualquier', 'Nancy_resultado_cualquier.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_cualquier.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'demasiado', 'Nancy_resultado_demasiado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_demasiado.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'mucho', 'Nancy_resultado_mucho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_mucho.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'nada', 'Nancy_resultado_nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_nada.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'nadie', 'Nancy_resultado_nadie.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_nadie.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'ningun', 'Nancy_resultado_ningun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_ningun.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'otro', 'Nancy_resultado_otro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_otro.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'poco', 'Nancy_resultado_poco.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_poco.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'quienquiera', 'Nancy_resultado_quienquiera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_quienquiera.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'preposicion', 'todo', 'Nancy_resultado_todo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-preposicion/Nancy_resultado_todo.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - profesion (48 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'abogado', 'Nancy_resultado_abogado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_abogado.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'administrador', 'Nancy_resultado_administrador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_administrador.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'albañil', 'Nancy_resultado_albañil.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_alba%C3%B1il.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'analista', 'Nancy_resultado_analista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_analista.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'auxiliar', 'Nancy_resultado_auxiliar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_auxiliar.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'barbero', 'Nancy_resultado_barbero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_barbero.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'cansar', 'Nancy_resultado_cansar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_cansar.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'carrera', 'Nancy_resultado_carrera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_carrera.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'chef', 'Nancy_resultado_chef.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_chef.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'cocinero', 'Nancy_resultado_cocinero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_cocinero.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'conductor', 'Nancy_resultado_conductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_conductor.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'constructor', 'Nancy_resultado_constructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_constructor.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'contador', 'Nancy_resultado_contador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_contador.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'dentista', 'Nancy_resultado_dentista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_dentista.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'detective', 'Nancy_resultado_detective.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_detective.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'dibujante tecnico', 'Nancy_resultado_dibujante tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_dibujante%20tecnico.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'dibujante', 'Nancy_resultado_dibujante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_dibujante.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'director', 'Nancy_resultado_director.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_director.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'economista', 'Nancy_resultado_economista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_economista.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'enfermera', 'Nancy_resultado_enfermera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_enfermera.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'escritor', 'Nancy_resultado_escritor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_escritor.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'fotografo', 'Nancy_resultado_fotografo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_fotografo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'gerente', 'Nancy_resultado_gerente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_gerente.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'informatica', 'Nancy_resultado_informatica.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_informatica.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'ingeniero', 'Nancy_resultado_ingeniero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_ingeniero.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'inspector', 'Nancy_resultado_inspector.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_inspector.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'instructor', 'Nancy_resultado_instructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_instructor.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'interprete', 'Nancy_resultado_interprete.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_interprete.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'jefe', 'Nancy_resultado_jefe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_jefe.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'licenciado', 'Nancy_resultado_licenciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_licenciado.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'maestro', 'Nancy_resultado_maestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_maestro.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'medico', 'Nancy_resultado_medico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_medico.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'mensajero', 'Nancy_resultado_mensajero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_mensajero.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'mesonero', 'Nancy_resultado_mesonero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_mesonero.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'pasante', 'Nancy_resultado_pasante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_pasante.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'peluquera', 'Nancy_resultado_peluquera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_peluquera.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'pintor', 'Nancy_resultado_pintor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_pintor.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'policia', 'Nancy_resultado_policia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_policia.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'profesion', 'Nancy_resultado_profesion.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_profesion.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'profesor', 'Nancy_resultado_profesor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_profesor.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'psicologo', 'Nancy_resultado_psicologo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_psicologo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'secretaria', 'Nancy_resultado_secretaria.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_secretaria.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'sistema', 'Nancy_resultado_sistema.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_sistema.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'supervisor', 'Nancy_resultado_supervisor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_supervisor.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'tecnico', 'Nancy_resultado_tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_tecnico.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'traductor', 'Nancy_resultado_traductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_traductor.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'vendedor', 'Nancy_resultado_vendedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_vendedor.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'profesion', 'vigilante', 'Nancy_resultado_vigilante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-profesion/Nancy_resultado_vigilante.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - pronombres (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'el', 'Nancy_resultado_el.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_el.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'ella', 'Nancy_resultado_ella.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_ella.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'ellas', 'Nancy_resultado_ellas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_ellas.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'ellos', 'Nancy_resultado_ellos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_ellos.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'mio', 'Nancy_resultado_mio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_mio.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'nosotros', 'Nancy_resultado_nosotros.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_nosotros.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'nuestro', 'Nancy_resultado_nuestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_nuestro.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'suyo', 'Nancy_resultado_suyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_suyo.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'tu', 'Nancy_resultado_tu.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_tu.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'tuyo', 'Nancy_resultado_tuyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_tuyo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'ustedes', 'Nancy_resultado_ustedes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_ustedes.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'pronombres', 'yo', 'Nancy_resultado_yo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-pronombres/Nancy_resultado_yo.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - saludos (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'saludos', 'adios', 'Nancy_resultado_adios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-saludos/Nancy_resultado_adios.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'saludos', 'bienvenido', 'Nancy_resultado_bienvenido.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-saludos/Nancy_resultado_bienvenido.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'saludos', 'buenas noches', 'Nancy_resultado_buenas noches.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-saludos/Nancy_resultado_buenas%20noches.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'saludos', 'buenas tardes', 'Nancy_resultado_buenas tardes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-saludos/Nancy_resultado_buenas%20tardes.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'saludos', 'buenos dias', 'Nancy_resultado_buenos dias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-saludos/Nancy_resultado_buenos%20dias.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'saludos', 'chao', 'Nancy_resultado_chao.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-saludos/Nancy_resultado_chao.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'saludos', 'hola', 'Nancy_resultado_hola.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-saludos/Nancy_resultado_hola.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - tiempo (9 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tiempo', 'anteayer', 'Nancy_resultado_anteayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tiempo/Nancy_resultado_anteayer.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tiempo', 'ayer', 'Nancy_resultado_ayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tiempo/Nancy_resultado_ayer.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tiempo', 'calendario', 'Nancy_resultado_calendario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tiempo/Nancy_resultado_calendario.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tiempo', 'fin de semana', 'Nancy_resultado_fin de semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tiempo/Nancy_resultado_fin%20de%20semana.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tiempo', 'hoy', 'Nancy_resultado_hoy.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tiempo/Nancy_resultado_hoy.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tiempo', 'manana', 'Nancy_resultado_manana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tiempo/Nancy_resultado_manana.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tiempo', 'mes', 'Nancy_resultado_mes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tiempo/Nancy_resultado_mes.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tiempo', 'pasado manana', 'Nancy_resultado_pasado manana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tiempo/Nancy_resultado_pasado%20manana.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tiempo', 'semana', 'Nancy_resultado_semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tiempo/Nancy_resultado_semana.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - tipos de vivienda (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tipos de vivienda', 'apartamento', 'Nancy_resultado_apartamento.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tipos de vivienda/Nancy_resultado_apartamento.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tipos de vivienda', 'baño', 'Nancy_resultado_baño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tipos de vivienda/Nancy_resultado_ba%C3%B1o.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tipos de vivienda', 'casa', 'Nancy_resultado_casa.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tipos de vivienda/Nancy_resultado_casa.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tipos de vivienda', 'cocina', 'Nancy_resultado_cocina.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tipos de vivienda/Nancy_resultado_cocina.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tipos de vivienda', 'comedor', 'Nancy_resultado_comedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tipos de vivienda/Nancy_resultado_comedor.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tipos de vivienda', 'cuarto', 'Nancy_resultado_cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tipos de vivienda/Nancy_resultado_cuarto.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tipos de vivienda', 'edificio', 'Nancy_resultado_edificio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tipos de vivienda/Nancy_resultado_edificio.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tipos de vivienda', 'piso', 'Nancy_resultado_piso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tipos de vivienda/Nancy_resultado_piso.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tipos de vivienda', 'rancho', 'Nancy_resultado_rancho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tipos de vivienda/Nancy_resultado_rancho.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'tipos de vivienda', 'sala', 'Nancy_resultado_sala.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-tipos de vivienda/Nancy_resultado_sala.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Nancy - verbos (19 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'amar', 'Nancy_resultado_amar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_amar.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'ayudar', 'Nancy_resultado_ayudar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_ayudar.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'comer', 'Nancy_resultado_comer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_comer.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'conocer', 'Nancy_resultado_conocer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_conocer.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'decir', 'Nancy_resultado_decir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_decir.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'deletrear', 'Nancy_resultado_deletrear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_deletrear.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'dormir', 'Nancy_resultado_dormir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_dormir.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'estar', 'Nancy_resultado_estar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_estar.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'estudiar', 'Nancy_resultado_estudiar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_estudiar.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'invitar', 'Nancy_resultado_invitar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_invitar.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'preguntar', 'Nancy_resultado_preguntar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_preguntar.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'presentar', 'Nancy_resultado_presentar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_presentar.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'querer', 'Nancy_resultado_querer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_querer.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'responder', 'Nancy_resultado_responder.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_responder.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'saludar', 'Nancy_resultado_saludar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_saludar.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'sentir', 'Nancy_resultado_sentir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_sentir.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'trabajar', 'Nancy_resultado_trabajar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_trabajar.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'ver', 'Nancy_resultado_ver.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_ver.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Nancy', 'verbos', 'vivir', 'Nancy_resultado_vivir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-nancy-verbos/Nancy_resultado_vivir.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - adverbios lugares (18 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'adverbios', 'Carla_resultado_adverbios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Carla_resultado_adverbios.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'al lado', 'Carla_resultado_al lado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Carla_resultado_al%20lado.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'atras', 'Carla_resultado_atras.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Carla_resultado_atras.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'cerca', 'Carla_resultado_cerca.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Carla_resultado_cerca.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'derecha', 'Carla_resultado_derecha.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Carla_resultado_derecha.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'frente', 'Carla_resultado_frente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Carla_resultado_frente.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'izquierda', 'Carla_resultado_izquierda.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Carla_resultado_izquierda.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'lejos', 'Carla_resultado_lejos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Carla_resultado_lejos.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'lugares', 'Carla_resultado_lugares.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Carla_resultado_lugares.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'adverbios', 'Duvall_resultado_adverbios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Duvall_resultado_adverbios.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'al lado', 'Duvall_resultado_al lado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Duvall_resultado_al%20lado.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'atras', 'Duvall_resultado_atras.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Duvall_resultado_atras.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'cerca', 'Duvall_resultado_cerca.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Duvall_resultado_cerca.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'derecha', 'Duvall_resultado_derecha.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Duvall_resultado_derecha.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'frente', 'Duvall_resultado_frente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Duvall_resultado_frente.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'izquierda', 'Duvall_resultado_izquierda.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Duvall_resultado_izquierda.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'lejos', 'Duvall_resultado_lejos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Duvall_resultado_lejos.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'adverbios lugares', 'lugares', 'Duvall_resultado_lugares.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-adverbios lugares/Duvall_resultado_lugares.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - alfabeto (52 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'a', 'Carla_resultado_a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_a.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'b', 'Carla_resultado_b.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_b.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'c', 'Carla_resultado_c.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_c.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'd', 'Carla_resultado_d.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_d.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'e', 'Carla_resultado_e.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_e.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'f', 'Carla_resultado_f.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_f.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'g', 'Carla_resultado_g.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_g.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'h', 'Carla_resultado_h.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_h.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'i', 'Carla_resultado_i.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_i.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'j', 'Carla_resultado_j.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_j.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'k', 'Carla_resultado_k.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_k.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'l', 'Carla_resultado_l.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_l.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'm', 'Carla_resultado_m.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_m.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'n', 'Carla_resultado_n.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_n.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'o', 'Carla_resultado_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_o.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'p', 'Carla_resultado_p.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_p.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'q', 'Carla_resultado_q.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_q.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'r', 'Carla_resultado_r.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_r.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 't', 'Carla_resultado_t.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_t.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'u', 'Carla_resultado_u.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_u.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'v', 'Carla_resultado_v.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_v.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'w', 'Carla_resultado_w.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_w.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'x', 'Carla_resultado_x.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_x.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'y', 'Carla_resultado_y.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_y.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'z', 'Carla_resultado_z.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_z.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'ñ', 'Carla_resultado_ñ.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Carla_resultado_%C3%B1.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'a', 'Duvall_resultado_a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_a.glb', 2.83, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'b', 'Duvall_resultado_b.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_b.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'c', 'Duvall_resultado_c.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_c.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'd', 'Duvall_resultado_d.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_d.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'e', 'Duvall_resultado_e.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_e.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'f', 'Duvall_resultado_f.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_f.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'g', 'Duvall_resultado_g.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_g.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'h', 'Duvall_resultado_h.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_h.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'i', 'Duvall_resultado_i.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_i.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'j', 'Duvall_resultado_j.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_j.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'k', 'Duvall_resultado_k.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_k.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'l', 'Duvall_resultado_l.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_l.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'm', 'Duvall_resultado_m.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_m.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'n', 'Duvall_resultado_n.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_n.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'o', 'Duvall_resultado_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_o.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'p', 'Duvall_resultado_p.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_p.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'q', 'Duvall_resultado_q.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_q.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'r', 'Duvall_resultado_r.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_r.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 't', 'Duvall_resultado_t.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_t.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'u', 'Duvall_resultado_u.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_u.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'v', 'Duvall_resultado_v.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_v.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'w', 'Duvall_resultado_w.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_w.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'x', 'Duvall_resultado_x.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_x.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'y', 'Duvall_resultado_y.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_y.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'z', 'Duvall_resultado_z.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_z.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'alfabeto', 'ñ', 'Duvall_resultado_ñ.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-alfabeto/Duvall_resultado_%C3%B1.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - cortesia (15 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'a la orden', 'Carla_resultado_a la orden.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Carla_resultado_a%20la%20orden.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'buen provecho', 'Carla_resultado_buen provecho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Carla_resultado_buen%20provecho.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'cortesia', 'Carla_resultado_cortesia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Carla_resultado_cortesia.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'gracias', 'Carla_resultado_gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Carla_resultado_gracias.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'muchas gracias', 'Carla_resultado_muchas gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Carla_resultado_muchas%20gracias.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'mucho gusto', 'Carla_resultado_mucho gusto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Carla_resultado_mucho%20gusto.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'permiso', 'Carla_resultado_permiso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Carla_resultado_permiso.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'modif', 'Carla_resultado_permiso_modif.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Carla_resultado_permiso_modif.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'a la orden', 'Duvall_resultado_a la orden.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Duvall_resultado_a%20la%20orden.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'buen provecho', 'Duvall_resultado_buen provecho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Duvall_resultado_buen%20provecho.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'cortesia', 'Duvall_resultado_cortesia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Duvall_resultado_cortesia.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'gracias', 'Duvall_resultado_gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Duvall_resultado_gracias.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'muchas gracias', 'Duvall_resultado_muchas gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Duvall_resultado_muchas%20gracias.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'mucho gusto', 'Duvall_resultado_mucho gusto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Duvall_resultado_mucho%20gusto.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'cortesia', 'permiso', 'Duvall_resultado_permiso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-cortesia/Duvall_resultado_permiso.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - dias_semana (14 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'domingo', 'Carla_resultado_domingo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Carla_resultado_domingo.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'jueves', 'Carla_resultado_jueves.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Carla_resultado_jueves.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'lunes', 'Carla_resultado_lunes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Carla_resultado_lunes.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'martes', 'Carla_resultado_martes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Carla_resultado_martes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'miercoles', 'Carla_resultado_miercoles.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Carla_resultado_miercoles.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'sabado', 'Carla_resultado_sabado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Carla_resultado_sabado.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'viernes', 'Carla_resultado_viernes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Carla_resultado_viernes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'domingo', 'Duvall_resultado_domingo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Duvall_resultado_domingo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'jueves', 'Duvall_resultado_jueves.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Duvall_resultado_jueves.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'lunes', 'Duvall_resultado_lunes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Duvall_resultado_lunes.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'martes', 'Duvall_resultado_martes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Duvall_resultado_martes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'miercoles', 'Duvall_resultado_miercoles.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Duvall_resultado_miercoles.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'sabado', 'Duvall_resultado_sabado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Duvall_resultado_sabado.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'dias_semana', 'viernes', 'Duvall_resultado_viernes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-dias_semana/Duvall_resultado_viernes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - estado civil (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'casado', 'Carla_resultado_casado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Carla_resultado_casado.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'concubino', 'Carla_resultado_concubino.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Carla_resultado_concubino.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'divorciado', 'Carla_resultado_divorciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Carla_resultado_divorciado.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'separado', 'Carla_resultado_separado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Carla_resultado_separado.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'soltero', 'Carla_resultado_soltero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Carla_resultado_soltero.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'viudo', 'Carla_resultado_viudo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Carla_resultado_viudo.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'casado', 'Duvall_resultado_casado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Duvall_resultado_casado.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'concubino', 'Duvall_resultado_concubino.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Duvall_resultado_concubino.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'divorciado', 'Duvall_resultado_divorciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Duvall_resultado_divorciado.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'separado', 'Duvall_resultado_separado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Duvall_resultado_separado.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'soltero', 'Duvall_resultado_soltero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Duvall_resultado_soltero.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'estado civil', 'viudo', 'Duvall_resultado_viudo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-estado civil/Duvall_resultado_viudo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - expresiones (62 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'abril', 'Carla_resultado_abril.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_abril.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'agosto', 'Carla_resultado_agosto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_agosto.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'bien', 'Carla_resultado_bien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_bien.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'como', 'Carla_resultado_como.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_como.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'cual', 'Carla_resultado_cual.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_cual.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'cuando', 'Carla_resultado_cuando.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_cuando.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'cuantos', 'Carla_resultado_cuantos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_cuantos.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'de nada', 'Carla_resultado_de nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_de%20nada.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'diciembre', 'Carla_resultado_diciembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_diciembre.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'donde (especifico)', 'Carla_resultado_donde (especifico).glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_donde%20(especifico).glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'donde', 'Carla_resultado_donde.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_donde.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'enero', 'Carla_resultado_enero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_enero.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'expresiones', 'Carla_resultado_expresiones.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_expresiones.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'febrero', 'Carla_resultado_febrero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_febrero.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'interrogantes', 'Carla_resultado_interrogantes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_interrogantes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'julio', 'Carla_resultado_julio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_julio.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'junio', 'Carla_resultado_junio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_junio.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'mal', 'Carla_resultado_mal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_mal.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'modif', 'Carla_resultado_mal_modif.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_mal_modif.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'marzo', 'Carla_resultado_marzo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_marzo.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'mayo', 'Carla_resultado_mayo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_mayo.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'no', 'Carla_resultado_no.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_no.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'noviembre', 'Carla_resultado_noviembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_noviembre.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'octubre', 'Carla_resultado_octubre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_octubre.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'porque', 'Carla_resultado_porque.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_porque.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'que', 'Carla_resultado_que.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_que.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'quien', 'Carla_resultado_quien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_quien.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'regular', 'Carla_resultado_regular.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_regular.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'saludas a', 'Carla_resultado_saludas a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_saludas%20a.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'septiembre', 'Carla_resultado_septiembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_septiembre.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'si', 'Carla_resultado_si.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Carla_resultado_si.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'abril', 'Duvall_resultado_abril.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_abril.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'agosto', 'Duvall_resultado_agosto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_agosto.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'bien', 'Duvall_resultado_bien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_bien.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'como', 'Duvall_resultado_como.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_como.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'cual', 'Duvall_resultado_cual.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_cual.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'cuando', 'Duvall_resultado_cuando.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_cuando.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'cuantos', 'Duvall_resultado_cuantos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_cuantos.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'de nada', 'Duvall_resultado_de nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_de%20nada.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'diciembre', 'Duvall_resultado_diciembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_diciembre.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'donde (especifico)', 'Duvall_resultado_donde (especifico).glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_donde%20(especifico).glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'donde', 'Duvall_resultado_donde.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_donde.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'enero', 'Duvall_resultado_enero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_enero.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'expresiones', 'Duvall_resultado_expresiones.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_expresiones.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'febrero', 'Duvall_resultado_febrero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_febrero.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'interrogantes', 'Duvall_resultado_interrogantes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_interrogantes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'julio', 'Duvall_resultado_julio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_julio.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'junio', 'Duvall_resultado_junio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_junio.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'mal', 'Duvall_resultado_mal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_mal.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'modif', 'Duvall_resultado_mal_modif.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_mal_modif.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'marzo', 'Duvall_resultado_marzo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_marzo.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'mayo', 'Duvall_resultado_mayo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_mayo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'no', 'Duvall_resultado_no.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_no.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'noviembre', 'Duvall_resultado_noviembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_noviembre.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'octubre', 'Duvall_resultado_octubre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_octubre.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'porque', 'Duvall_resultado_porque.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_porque.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'que', 'Duvall_resultado_que.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_que.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'quien', 'Duvall_resultado_quien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_quien.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'regular', 'Duvall_resultado_regular.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_regular.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'saludas a', 'Duvall_resultado_saludas a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_saludas%20a.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'septiembre', 'Duvall_resultado_septiembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_septiembre.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'expresiones', 'si', 'Duvall_resultado_si.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-expresiones/Duvall_resultado_si.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - medios transporte (0 archivos)
-- original - numero (24 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '0', 'Carla_resultado_0.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_0.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '1', 'Carla_resultado_1.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_1.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '10', 'Carla_resultado_10.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_10.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '1M', 'Carla_resultado_1M.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_1M.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '2', 'Carla_resultado_2.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_2.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '3', 'Carla_resultado_3.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_3.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '4', 'Carla_resultado_4.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_4.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '5', 'Carla_resultado_5.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_5.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '6', 'Carla_resultado_6.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_6.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '7', 'Carla_resultado_7.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_7.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '8', 'Carla_resultado_8.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_8.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '9', 'Carla_resultado_9.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Carla_resultado_9.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '0', 'Duvall_resultado_0.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_0.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '1', 'Duvall_resultado_1.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_1.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '10', 'Duvall_resultado_10.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_10.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '1M', 'Duvall_resultado_1M.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_1M.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '2', 'Duvall_resultado_2.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_2.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '3', 'Duvall_resultado_3.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_3.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '4', 'Duvall_resultado_4.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_4.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '5', 'Duvall_resultado_5.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_5.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '6', 'Duvall_resultado_6.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_6.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '7', 'Duvall_resultado_7.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_7.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '8', 'Duvall_resultado_8.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_8.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numero', '9', 'Duvall_resultado_9.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numero/Duvall_resultado_9.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - numeros ordinales (20 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '10_o', 'Carla_resultado_10_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Carla_resultado_10_o.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '1_o', 'Carla_resultado_1_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Carla_resultado_1_o.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '2_o', 'Carla_resultado_2_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Carla_resultado_2_o.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '3_o', 'Carla_resultado_3_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Carla_resultado_3_o.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '4_o', 'Carla_resultado_4_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Carla_resultado_4_o.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '5_o', 'Carla_resultado_5_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Carla_resultado_5_o.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '6_o', 'Carla_resultado_6_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Carla_resultado_6_o.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '7_o', 'Carla_resultado_7_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Carla_resultado_7_o.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '8_o', 'Carla_resultado_8_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Carla_resultado_8_o.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '9_o', 'Carla_resultado_9_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Carla_resultado_9_o.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '10_o', 'Duvall_resultado_10_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Duvall_resultado_10_o.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '1_o', 'Duvall_resultado_1_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Duvall_resultado_1_o.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '2_o', 'Duvall_resultado_2_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Duvall_resultado_2_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '3_o', 'Duvall_resultado_3_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Duvall_resultado_3_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '4_o', 'Duvall_resultado_4_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Duvall_resultado_4_o.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '5_o', 'Duvall_resultado_5_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Duvall_resultado_5_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '6_o', 'Duvall_resultado_6_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Duvall_resultado_6_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '7_o', 'Duvall_resultado_7_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Duvall_resultado_7_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '8_o', 'Duvall_resultado_8_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Duvall_resultado_8_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'numeros ordinales', '9_o', 'Duvall_resultado_9_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-numeros ordinales/Duvall_resultado_9_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - personas (44 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'adulto', 'Carla_resultado_adulto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_adulto.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'amigo', 'Carla_resultado_amigo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_amigo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'anciano', 'Carla_resultado_anciano.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_anciano.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'bebe', 'Carla_resultado_bebe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_bebe.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'ciego', 'Carla_resultado_ciego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_ciego.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'compañero', 'Carla_resultado_compañero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_compa%C3%B1ero.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'hombre', 'Carla_resultado_hombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_hombre.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'joven', 'Carla_resultado_joven.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_joven.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'mayor de edad', 'Carla_resultado_mayor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_mayor%20de%20edad.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'mayor', 'Carla_resultado_mayor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_mayor.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'menor de edad', 'Carla_resultado_menor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_menor%20de%20edad.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'mujer', 'Carla_resultado_mujer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_mujer.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'niño', 'Carla_resultado_niño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_ni%C3%B1o.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'novio', 'Carla_resultado_novio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_novio.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'oyente', 'Carla_resultado_oyente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_oyente.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'persona', 'Carla_resultado_persona.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_persona.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'personas', 'Carla_resultado_personas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_personas.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'señor', 'Carla_resultado_señor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_se%C3%B1or.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'señorita', 'Carla_resultado_señorita.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_se%C3%B1orita.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'sordo', 'Carla_resultado_sordo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_sordo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'sordociego', 'Carla_resultado_sordociego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_sordociego.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'viejo', 'Carla_resultado_viejo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Carla_resultado_viejo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'adulto', 'Duvall_resultado_adulto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_adulto.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'amigo', 'Duvall_resultado_amigo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_amigo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'anciano', 'Duvall_resultado_anciano.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_anciano.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'bebe', 'Duvall_resultado_bebe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_bebe.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'ciego', 'Duvall_resultado_ciego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_ciego.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'compañero', 'Duvall_resultado_compañero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_compa%C3%B1ero.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'hombre', 'Duvall_resultado_hombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_hombre.glb', 2.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'joven', 'Duvall_resultado_joven.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_joven.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'mayor de edad', 'Duvall_resultado_mayor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_mayor%20de%20edad.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'mayor', 'Duvall_resultado_mayor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_mayor.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'menor de edad', 'Duvall_resultado_menor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_menor%20de%20edad.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'mujer', 'Duvall_resultado_mujer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_mujer.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'niño', 'Duvall_resultado_niño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_ni%C3%B1o.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'novio', 'Duvall_resultado_novio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_novio.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'oyente', 'Duvall_resultado_oyente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_oyente.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'persona', 'Duvall_resultado_persona.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_persona.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'personas', 'Duvall_resultado_personas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_personas.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'señor', 'Duvall_resultado_señor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_se%C3%B1or.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'señorita', 'Duvall_resultado_señorita.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_se%C3%B1orita.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'sordo', 'Duvall_resultado_sordo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_sordo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'sordociego', 'Duvall_resultado_sordociego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_sordociego.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'personas', 'viejo', 'Duvall_resultado_viejo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-personas/Duvall_resultado_viejo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - preguntas (8 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preguntas', 'como estas', 'Carla_resultado_como estas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preguntas/Carla_resultado_como%20estas.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preguntas', 'cual es tu nombre', 'Carla_resultado_cual es tu nombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preguntas/Carla_resultado_cual%20es%20tu%20nombre.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preguntas', 'cual es tu sena', 'Carla_resultado_cual es tu sena.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preguntas/Carla_resultado_cual%20es%20tu%20sena.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preguntas', 'que tal', 'Carla_resultado_que tal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preguntas/Carla_resultado_que%20tal.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preguntas', 'como estas', 'Duvall_resultado_como estas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preguntas/Duvall_resultado_como%20estas.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preguntas', 'cual es tu nombre', 'Duvall_resultado_cual es tu nombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preguntas/Duvall_resultado_cual%20es%20tu%20nombre.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preguntas', 'cual es tu sena', 'Duvall_resultado_cual es tu sena.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preguntas/Duvall_resultado_cual%20es%20tu%20sena.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preguntas', 'que tal', 'Duvall_resultado_que tal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preguntas/Duvall_resultado_que%20tal.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - preposicion (30 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'algo', 'Carla_resultado_algo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_algo.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'alguien', 'Carla_resultado_alguien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_alguien.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'algun', 'Carla_resultado_algun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_algun.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'bastante', 'Carla_resultado_bastante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_bastante.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'cualquier', 'Carla_resultado_cualquier.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_cualquier.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'demasiado', 'Carla_resultado_demasiado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_demasiado.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'mas', 'Carla_resultado_mas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_mas.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'mucho', 'Carla_resultado_mucho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_mucho.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'nada', 'Carla_resultado_nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_nada.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'nadie', 'Carla_resultado_nadie.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_nadie.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'ningun', 'Carla_resultado_ningun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_ningun.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'otro', 'Carla_resultado_otro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_otro.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'poco', 'Carla_resultado_poco.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_poco.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'quienquiera', 'Carla_resultado_quienquiera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_quienquiera.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'todo', 'Carla_resultado_todo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Carla_resultado_todo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'algo', 'Duvall_resultado_algo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_algo.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'alguien', 'Duvall_resultado_alguien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_alguien.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'algun', 'Duvall_resultado_algun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_algun.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'bastante', 'Duvall_resultado_bastante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_bastante.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'cualquier', 'Duvall_resultado_cualquier.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_cualquier.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'demasiado', 'Duvall_resultado_demasiado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_demasiado.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'mas', 'Duvall_resultado_mas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_mas.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'mucho', 'Duvall_resultado_mucho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_mucho.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'nada', 'Duvall_resultado_nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_nada.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'nadie', 'Duvall_resultado_nadie.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_nadie.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'ningun', 'Duvall_resultado_ningun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_ningun.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'otro', 'Duvall_resultado_otro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_otro.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'poco', 'Duvall_resultado_poco.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_poco.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'quienquiera', 'Duvall_resultado_quienquiera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_quienquiera.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'preposicion', 'todo', 'Duvall_resultado_todo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-preposicion/Duvall_resultado_todo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - profesion (94 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'abogado', 'Carla_resultado_abogado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_abogado.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'administrador', 'Carla_resultado_administrador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_administrador.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'albañil', 'Carla_resultado_albañil.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_alba%C3%B1il.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'analista', 'Carla_resultado_analista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_analista.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'auxiliar', 'Carla_resultado_auxiliar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_auxiliar.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'barbero', 'Carla_resultado_barbero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_barbero.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'carrera', 'Carla_resultado_carrera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_carrera.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'chef', 'Carla_resultado_chef.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_chef.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'cocinero', 'Carla_resultado_cocinero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_cocinero.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'conductor', 'Carla_resultado_conductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_conductor.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'constructor', 'Carla_resultado_constructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_constructor.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'contador', 'Carla_resultado_contador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_contador.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'dentista', 'Carla_resultado_dentista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_dentista.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'detective', 'Carla_resultado_detective.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_detective.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'dibujante tecnico', 'Carla_resultado_dibujante tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_dibujante%20tecnico.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'dibujante', 'Carla_resultado_dibujante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_dibujante.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'director', 'Carla_resultado_director.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_director.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'economista', 'Carla_resultado_economista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_economista.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'enfermera', 'Carla_resultado_enfermera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_enfermera.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'escritor', 'Carla_resultado_escritor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_escritor.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'fotografo', 'Carla_resultado_fotografo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_fotografo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'gerente', 'Carla_resultado_gerente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_gerente.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'informatica', 'Carla_resultado_informatica.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_informatica.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'ingeniero', 'Carla_resultado_ingeniero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_ingeniero.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'inspector', 'Carla_resultado_inspector.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_inspector.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'instructor', 'Carla_resultado_instructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_instructor.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'interprete', 'Carla_resultado_interprete.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_interprete.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'jefe', 'Carla_resultado_jefe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_jefe.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'licenciado', 'Carla_resultado_licenciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_licenciado.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'maestro', 'Carla_resultado_maestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_maestro.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'medico', 'Carla_resultado_medico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_medico.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'mensajero', 'Carla_resultado_mensajero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_mensajero.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'mesonero', 'Carla_resultado_mesonero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_mesonero.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'pasante', 'Carla_resultado_pasante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_pasante.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'peluquera', 'Carla_resultado_peluquera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_peluquera.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'pintor', 'Carla_resultado_pintor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_pintor.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'policia', 'Carla_resultado_policia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_policia.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'profesion', 'Carla_resultado_profesion.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_profesion.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'profesor', 'Carla_resultado_profesor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_profesor.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'psicologo', 'Carla_resultado_psicologo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_psicologo.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'secretaria', 'Carla_resultado_secretaria.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_secretaria.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'sistema', 'Carla_resultado_sistema.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_sistema.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'supervisor', 'Carla_resultado_supervisor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_supervisor.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'tecnico', 'Carla_resultado_tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_tecnico.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'traductor', 'Carla_resultado_traductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_traductor.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'vendedor', 'Carla_resultado_vendedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_vendedor.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'vigilante', 'Carla_resultado_vigilante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Carla_resultado_vigilante.glb', 3.15, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'abogado', 'Duvall_resultado_abogado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_abogado.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'administrador', 'Duvall_resultado_administrador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_administrador.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'albañil', 'Duvall_resultado_albañil.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_alba%C3%B1il.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'analista', 'Duvall_resultado_analista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_analista.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'auxiliar', 'Duvall_resultado_auxiliar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_auxiliar.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'barbero', 'Duvall_resultado_barbero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_barbero.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'carrera', 'Duvall_resultado_carrera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_carrera.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'chef', 'Duvall_resultado_chef.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_chef.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'cocinero', 'Duvall_resultado_cocinero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_cocinero.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'conductor', 'Duvall_resultado_conductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_conductor.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'constructor', 'Duvall_resultado_constructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_constructor.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'contador', 'Duvall_resultado_contador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_contador.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'dentista', 'Duvall_resultado_dentista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_dentista.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'detective', 'Duvall_resultado_detective.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_detective.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'dibujante tecnico', 'Duvall_resultado_dibujante tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_dibujante%20tecnico.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'dibujante', 'Duvall_resultado_dibujante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_dibujante.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'director', 'Duvall_resultado_director.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_director.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'economista', 'Duvall_resultado_economista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_economista.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'enfermera', 'Duvall_resultado_enfermera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_enfermera.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'escritor', 'Duvall_resultado_escritor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_escritor.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'fotografo', 'Duvall_resultado_fotografo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_fotografo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'gerente', 'Duvall_resultado_gerente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_gerente.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'informatica', 'Duvall_resultado_informatica.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_informatica.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'ingeniero', 'Duvall_resultado_ingeniero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_ingeniero.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'inspector', 'Duvall_resultado_inspector.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_inspector.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'instructor', 'Duvall_resultado_instructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_instructor.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'interprete', 'Duvall_resultado_interprete.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_interprete.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'jefe', 'Duvall_resultado_jefe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_jefe.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'licenciado', 'Duvall_resultado_licenciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_licenciado.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'maestro', 'Duvall_resultado_maestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_maestro.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'medico', 'Duvall_resultado_medico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_medico.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'mensajero', 'Duvall_resultado_mensajero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_mensajero.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'mesonero', 'Duvall_resultado_mesonero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_mesonero.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'pasante', 'Duvall_resultado_pasante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_pasante.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'peluquera', 'Duvall_resultado_peluquera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_peluquera.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'pintor', 'Duvall_resultado_pintor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_pintor.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'policia', 'Duvall_resultado_policia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_policia.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'profesion', 'Duvall_resultado_profesion.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_profesion.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'profesor', 'Duvall_resultado_profesor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_profesor.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'psicologo', 'Duvall_resultado_psicologo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_psicologo.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'secretaria', 'Duvall_resultado_secretaria.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_secretaria.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'sistema', 'Duvall_resultado_sistema.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_sistema.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'supervisor', 'Duvall_resultado_supervisor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_supervisor.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'tecnico', 'Duvall_resultado_tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_tecnico.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'traductor', 'Duvall_resultado_traductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_traductor.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'vendedor', 'Duvall_resultado_vendedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_vendedor.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'profesion', 'vigilante', 'Duvall_resultado_vigilante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-profesion/Duvall_resultado_vigilante.glb', 2.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - pronombres (24 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'el', 'Carla_resultado_el.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_el.glb', 3.04, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'ella', 'Carla_resultado_ella.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_ella.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'ellas', 'Carla_resultado_ellas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_ellas.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'ellos', 'Carla_resultado_ellos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_ellos.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'mio', 'Carla_resultado_mio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_mio.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'nosotros', 'Carla_resultado_nosotros.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_nosotros.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'nuestro', 'Carla_resultado_nuestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_nuestro.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'suyo', 'Carla_resultado_suyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_suyo.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'tu', 'Carla_resultado_tu.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_tu.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'tuyo', 'Carla_resultado_tuyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_tuyo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'ustedes', 'Carla_resultado_ustedes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_ustedes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'yo', 'Carla_resultado_yo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Carla_resultado_yo.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'el', 'Duvall_resultado_el.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_el.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'ella', 'Duvall_resultado_ella.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_ella.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'ellas', 'Duvall_resultado_ellas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_ellas.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'ellos', 'Duvall_resultado_ellos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_ellos.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'mio', 'Duvall_resultado_mio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_mio.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'nosotros', 'Duvall_resultado_nosotros.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_nosotros.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'nuestro', 'Duvall_resultado_nuestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_nuestro.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'suyo', 'Duvall_resultado_suyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_suyo.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'tu', 'Duvall_resultado_tu.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_tu.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'tuyo', 'Duvall_resultado_tuyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_tuyo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'ustedes', 'Duvall_resultado_ustedes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_ustedes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'pronombres', 'yo', 'Duvall_resultado_yo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-pronombres/Duvall_resultado_yo.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - saludos (14 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'adios', 'Carla_resultado_adios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Carla_resultado_adios.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'bienvenido', 'Carla_resultado_bienvenido.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Carla_resultado_bienvenido.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'buenas noches', 'Carla_resultado_buenas noches.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Carla_resultado_buenas%20noches.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'buenas tardes', 'Carla_resultado_buenas tardes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Carla_resultado_buenas%20tardes.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'buenos dias', 'Carla_resultado_buenos dias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Carla_resultado_buenos%20dias.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'chao', 'Carla_resultado_chao.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Carla_resultado_chao.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'hola', 'Carla_resultado_hola.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Carla_resultado_hola.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'adios', 'Duvall_resultado_adios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Duvall_resultado_adios.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'bienvenido', 'Duvall_resultado_bienvenido.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Duvall_resultado_bienvenido.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'buenas noches', 'Duvall_resultado_buenas noches.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Duvall_resultado_buenas%20noches.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'buenas tardes', 'Duvall_resultado_buenas tardes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Duvall_resultado_buenas%20tardes.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'buenos dias', 'Duvall_resultado_buenos dias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Duvall_resultado_buenos%20dias.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'chao', 'Duvall_resultado_chao.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Duvall_resultado_chao.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'saludos', 'hola', 'Duvall_resultado_hola.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-saludos/Duvall_resultado_hola.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - tiempo (18 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'anteayer', 'Carla_resultado_anteayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Carla_resultado_anteayer.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'ayer', 'Carla_resultado_ayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Carla_resultado_ayer.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'calendario', 'Carla_resultado_calendario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Carla_resultado_calendario.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'fin de semana', 'Carla_resultado_fin de semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Carla_resultado_fin%20de%20semana.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'hoy', 'Carla_resultado_hoy.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Carla_resultado_hoy.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'mañana', 'Carla_resultado_mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Carla_resultado_ma%C3%B1ana.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'mes', 'Carla_resultado_mes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Carla_resultado_mes.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'pasado mañana', 'Carla_resultado_pasado mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Carla_resultado_pasado%20ma%C3%B1ana.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'semana', 'Carla_resultado_semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Carla_resultado_semana.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'anteayer', 'Duvall_resultado_anteayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Duvall_resultado_anteayer.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'ayer', 'Duvall_resultado_ayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Duvall_resultado_ayer.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'calendario', 'Duvall_resultado_calendario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Duvall_resultado_calendario.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'fin de semana', 'Duvall_resultado_fin de semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Duvall_resultado_fin%20de%20semana.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'hoy', 'Duvall_resultado_hoy.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Duvall_resultado_hoy.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'mañana', 'Duvall_resultado_mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Duvall_resultado_ma%C3%B1ana.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'mes', 'Duvall_resultado_mes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Duvall_resultado_mes.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'pasado mañana', 'Duvall_resultado_pasado mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Duvall_resultado_pasado%20ma%C3%B1ana.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tiempo', 'semana', 'Duvall_resultado_semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tiempo/Duvall_resultado_semana.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - tipos de vivienda (20 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'apartamento', 'Carla_resultado_apartamento.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Carla_resultado_apartamento.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'baño', 'Carla_resultado_baño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Carla_resultado_ba%C3%B1o.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'casa', 'Carla_resultado_casa.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Carla_resultado_casa.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'cocina', 'Carla_resultado_cocina.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Carla_resultado_cocina.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'comedor', 'Carla_resultado_comedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Carla_resultado_comedor.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'cuarto', 'Carla_resultado_cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Carla_resultado_cuarto.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'edificio', 'Carla_resultado_edificio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Carla_resultado_edificio.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'piso', 'Carla_resultado_piso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Carla_resultado_piso.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'rancho', 'Carla_resultado_rancho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Carla_resultado_rancho.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'sala', 'Carla_resultado_sala.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Carla_resultado_sala.glb', 3.15, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'apartamento', 'Duvall_resultado_apartamento.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Duvall_resultado_apartamento.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'baño', 'Duvall_resultado_baño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Duvall_resultado_ba%C3%B1o.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'casa', 'Duvall_resultado_casa.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Duvall_resultado_casa.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'cocina', 'Duvall_resultado_cocina.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Duvall_resultado_cocina.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'comedor', 'Duvall_resultado_comedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Duvall_resultado_comedor.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'cuarto', 'Duvall_resultado_cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Duvall_resultado_cuarto.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'edificio', 'Duvall_resultado_edificio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Duvall_resultado_edificio.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'piso', 'Duvall_resultado_piso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Duvall_resultado_piso.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'rancho', 'Duvall_resultado_rancho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Duvall_resultado_rancho.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'tipos de vivienda', 'sala', 'Duvall_resultado_sala.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-tipos de vivienda/Duvall_resultado_sala.glb', 2.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- original - verbos (40 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'amar', 'Carla_resultado_amar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_amar.glb', 3.38, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'ayudar', 'Carla_resultado_ayudar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_ayudar.glb', 3.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'cansar', 'Carla_resultado_cansar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_cansar.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'comer', 'Carla_resultado_comer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_comer.glb', 3.38, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'conocer', 'Carla_resultado_conocer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_conocer.glb', 3.33, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'decir', 'Carla_resultado_decir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_decir.glb', 3.34, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'deletrear', 'Carla_resultado_deletrear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_deletrear.glb', 3.31, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'dormir', 'Carla_resultado_dormir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_dormir.glb', 3.33, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'estar', 'Carla_resultado_estar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_estar.glb', 3.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'estudiar', 'Carla_resultado_estudiar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_estudiar.glb', 3.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'invitar', 'Carla_resultado_invitar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_invitar.glb', 3.34, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'preguntar', 'Carla_resultado_preguntar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_preguntar.glb', 3.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'presentar', 'Carla_resultado_presentar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_presentar.glb', 3.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'querer', 'Carla_resultado_querer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_querer.glb', 3.34, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'responder', 'Carla_resultado_responder.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_responder.glb', 3.30, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'saludar', 'Carla_resultado_saludar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_saludar.glb', 3.31, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'sentir', 'Carla_resultado_sentir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_sentir.glb', 3.37, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'trabajar', 'Carla_resultado_trabajar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_trabajar.glb', 3.29, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'ver', 'Carla_resultado_ver.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_ver.glb', 3.35, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'vivir', 'Carla_resultado_vivir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Carla_resultado_vivir.glb', 3.27, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'amar', 'Duvall_resultado_amar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_amar.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'ayudar', 'Duvall_resultado_ayudar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_ayudar.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'cansar', 'Duvall_resultado_cansar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_cansar.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'comer', 'Duvall_resultado_comer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_comer.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'conocer', 'Duvall_resultado_conocer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_conocer.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'decir', 'Duvall_resultado_decir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_decir.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'deletrear', 'Duvall_resultado_deletrear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_deletrear.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'dormir', 'Duvall_resultado_dormir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_dormir.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'estar', 'Duvall_resultado_estar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_estar.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'estudiar', 'Duvall_resultado_estudiar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_estudiar.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'invitar', 'Duvall_resultado_invitar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_invitar.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'preguntar', 'Duvall_resultado_preguntar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_preguntar.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'presentar', 'Duvall_resultado_presentar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_presentar.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'querer', 'Duvall_resultado_querer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_querer.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'responder', 'Duvall_resultado_responder.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_responder.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'saludar', 'Duvall_resultado_saludar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_saludar.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'sentir', 'Duvall_resultado_sentir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_sentir.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'trabajar', 'Duvall_resultado_trabajar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_trabajar.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'ver', 'Duvall_resultado_ver.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_ver.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('original', 'verbos', 'vivir', 'Duvall_resultado_vivir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-original-verbos/Duvall_resultado_vivir.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

COMMIT;
