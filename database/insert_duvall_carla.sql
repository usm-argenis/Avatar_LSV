-- Inserción de modelos GLB para Duvall y Carla
-- Generado: 2026-02-05T17:28:18.208Z

BEGIN;

-- Duvall - adverbios lugares (9 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'adverbios', 'Duvall_resultado_adverbios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/adverbios lugares/Duvall_resultado_adverbios.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'al lado', 'Duvall_resultado_al lado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/adverbios lugares/Duvall_resultado_al%20lado.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'atras', 'Duvall_resultado_atras.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/adverbios lugares/Duvall_resultado_atras.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'cerca', 'Duvall_resultado_cerca.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/adverbios lugares/Duvall_resultado_cerca.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'derecha', 'Duvall_resultado_derecha.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/adverbios lugares/Duvall_resultado_derecha.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'frente', 'Duvall_resultado_frente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/adverbios lugares/Duvall_resultado_frente.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'izquierda', 'Duvall_resultado_izquierda.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/adverbios lugares/Duvall_resultado_izquierda.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'lejos', 'Duvall_resultado_lejos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/adverbios lugares/Duvall_resultado_lejos.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'adverbios lugares', 'lugares', 'Duvall_resultado_lugares.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/adverbios lugares/Duvall_resultado_lugares.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - alfabeto (27 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'a', 'Duvall_resultado_a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_a.glb', 2.83, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'b', 'Duvall_resultado_b.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_b.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'c', 'Duvall_resultado_c.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_c.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'd', 'Duvall_resultado_d.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_d.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'e', 'Duvall_resultado_e.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_e.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'f', 'Duvall_resultado_f.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_f.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'g', 'Duvall_resultado_g.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_g.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'h', 'Duvall_resultado_h.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_h.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'i', 'Duvall_resultado_i.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_i.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'j', 'Duvall_resultado_j.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_j.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'k', 'Duvall_resultado_k.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_k.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'l', 'Duvall_resultado_l.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_l.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'm', 'Duvall_resultado_m.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_m.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'n', 'Duvall_resultado_n.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_n.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'o', 'Duvall_resultado_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_o.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'p', 'Duvall_resultado_p.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_p.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'q', 'Duvall_resultado_q.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_q.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'r', 'Duvall_resultado_r.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_r.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 's', 'Duvall_resultado_s.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_s.glb', 3.00, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 't', 'Duvall_resultado_t.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_t.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'u', 'Duvall_resultado_u.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_u.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'v', 'Duvall_resultado_v.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_v.glb', 2.80, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'w', 'Duvall_resultado_w.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_w.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'x', 'Duvall_resultado_x.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_x.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'y', 'Duvall_resultado_y.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_y.glb', 2.82, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'z', 'Duvall_resultado_z.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_z.glb', 2.81, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'alfabeto', 'ñ', 'Duvall_resultado_ñ.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/alfabeto/Duvall_resultado_%C3%B1.glb', 2.79, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - cortesia (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'a la orden', 'Duvall_resultado_a la orden.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/cortesia/Duvall_resultado_a%20la%20orden.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'buen provecho', 'Duvall_resultado_buen provecho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/cortesia/Duvall_resultado_buen%20provecho.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'cortesia', 'Duvall_resultado_cortesia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/cortesia/Duvall_resultado_cortesia.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'gracias', 'Duvall_resultado_gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/cortesia/Duvall_resultado_gracias.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'muchas gracias', 'Duvall_resultado_muchas gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/cortesia/Duvall_resultado_muchas%20gracias.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'mucho gusto', 'Duvall_resultado_mucho gusto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/cortesia/Duvall_resultado_mucho%20gusto.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'cortesia', 'permiso', 'Duvall_resultado_permiso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/cortesia/Duvall_resultado_permiso.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - dias_semana (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'domingo', 'Duvall_resultado_domingo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/dias_semana/Duvall_resultado_domingo.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'jueves', 'Duvall_resultado_jueves.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/dias_semana/Duvall_resultado_jueves.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'lunes', 'Duvall_resultado_lunes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/dias_semana/Duvall_resultado_lunes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'martes', 'Duvall_resultado_martes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/dias_semana/Duvall_resultado_martes.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'miercoles', 'Duvall_resultado_miercoles.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/dias_semana/Duvall_resultado_miercoles.glb', 2.91, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'sabado', 'Duvall_resultado_sabado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/dias_semana/Duvall_resultado_sabado.glb', 2.88, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'dias_semana', 'viernes', 'Duvall_resultado_viernes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/dias_semana/Duvall_resultado_viernes.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - base (1 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'base', 'base', 'Duvall.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/base/Duvall.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - estado civil (6 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'casado', 'Duvall_resultado_casado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/estado civil/Duvall_resultado_casado.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'concubino', 'Duvall_resultado_concubino.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/estado civil/Duvall_resultado_concubino.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'divorciado', 'Duvall_resultado_divorciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/estado civil/Duvall_resultado_divorciado.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'separado', 'Duvall_resultado_separado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/estado civil/Duvall_resultado_separado.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'soltero', 'Duvall_resultado_soltero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/estado civil/Duvall_resultado_soltero.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'estado civil', 'viudo', 'Duvall_resultado_viudo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/estado civil/Duvall_resultado_viudo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - expresiones (30 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'abril', 'Duvall_resultado_abril.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_abril.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'agosto', 'Duvall_resultado_agosto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_agosto.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'bien', 'Duvall_resultado_bien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_bien.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'como', 'Duvall_resultado_como.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_como.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'cual', 'Duvall_resultado_cual.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_cual.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'cuando', 'Duvall_resultado_cuando.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_cuando.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'cuantos', 'Duvall_resultado_cuantos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_cuantos.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'de nada', 'Duvall_resultado_de nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_de%20nada.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'diciembre', 'Duvall_resultado_diciembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_diciembre.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'donde (especifico)', 'Duvall_resultado_donde (especifico).glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_donde%20(especifico).glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'donde', 'Duvall_resultado_donde.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_donde.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'enero', 'Duvall_resultado_enero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_enero.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'expresiones', 'Duvall_resultado_expresiones.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_expresiones.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'febrero', 'Duvall_resultado_febrero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_febrero.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'interrogantes', 'Duvall_resultado_interrogantes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_interrogantes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'julio', 'Duvall_resultado_julio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_julio.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'junio', 'Duvall_resultado_junio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_junio.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'mal', 'Duvall_resultado_mal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_mal.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'marzo', 'Duvall_resultado_marzo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_marzo.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'mayo', 'Duvall_resultado_mayo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_mayo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'no', 'Duvall_resultado_no.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_no.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'noviembre', 'Duvall_resultado_noviembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_noviembre.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'octubre', 'Duvall_resultado_octubre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_octubre.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'porque', 'Duvall_resultado_porque.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_porque.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'que', 'Duvall_resultado_que.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_que.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'quien', 'Duvall_resultado_quien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_quien.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'regular', 'Duvall_resultado_regular.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_regular.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'saludas a', 'Duvall_resultado_saludas a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_saludas%20a.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'septiembre', 'Duvall_resultado_septiembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_septiembre.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'expresiones', 'si', 'Duvall_resultado_si.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/expresiones/Duvall_resultado_si.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - horario (8 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'en punto', 'Duvall_resultado_en punto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/horario/Duvall_resultado_en%20punto.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'hora', 'Duvall_resultado_hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/horario/Duvall_resultado_hora.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'horario', 'Duvall_resultado_horario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/horario/Duvall_resultado_horario.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'media hora', 'Duvall_resultado_media hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/horario/Duvall_resultado_media%20hora.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'un cuarto', 'Duvall_resultado_un cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/horario/Duvall_resultado_un%20cuarto.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'un minuto', 'Duvall_resultado_un minuto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/horario/Duvall_resultado_un%20minuto.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'un segundo', 'Duvall_resultado_un segundo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/horario/Duvall_resultado_un%20segundo.glb', 3.04, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'horario', 'una hora', 'Duvall_resultado_una hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/horario/Duvall_resultado_una%20hora.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - medios transporte (0 archivos)
-- Duvall - numero (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '0', 'Duvall_resultado_0.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_0.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '1', 'Duvall_resultado_1.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_1.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '10', 'Duvall_resultado_10.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_10.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '1M', 'Duvall_resultado_1M.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_1M.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '2', 'Duvall_resultado_2.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_2.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '3', 'Duvall_resultado_3.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_3.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '4', 'Duvall_resultado_4.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_4.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '5', 'Duvall_resultado_5.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_5.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '6', 'Duvall_resultado_6.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_6.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '7', 'Duvall_resultado_7.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_7.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '8', 'Duvall_resultado_8.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_8.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numero', '9', 'Duvall_resultado_9.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numero/Duvall_resultado_9.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - numeros ordinales (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '10_o', 'Duvall_resultado_10_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numeros ordinales/Duvall_resultado_10_o.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '1_o', 'Duvall_resultado_1_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numeros ordinales/Duvall_resultado_1_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '2_o', 'Duvall_resultado_2_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numeros ordinales/Duvall_resultado_2_o.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '3_o', 'Duvall_resultado_3_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numeros ordinales/Duvall_resultado_3_o.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '4_o', 'Duvall_resultado_4_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numeros ordinales/Duvall_resultado_4_o.glb', 11.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '5_o', 'Duvall_resultado_5_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numeros ordinales/Duvall_resultado_5_o.glb', 11.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '6_o', 'Duvall_resultado_6_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numeros ordinales/Duvall_resultado_6_o.glb', 11.98, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '7_o', 'Duvall_resultado_7_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numeros ordinales/Duvall_resultado_7_o.glb', 12.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '8_o', 'Duvall_resultado_8_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numeros ordinales/Duvall_resultado_8_o.glb', 12.17, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'numeros ordinales', '9_o', 'Duvall_resultado_9_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/numeros ordinales/Duvall_resultado_9_o.glb', 12.28, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - personas (22 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'adulto', 'Duvall_resultado_adulto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_adulto.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'amigo', 'Duvall_resultado_amigo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_amigo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'anciano', 'Duvall_resultado_anciano.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_anciano.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'bebe', 'Duvall_resultado_bebe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_bebe.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'ciego', 'Duvall_resultado_ciego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_ciego.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'compañero', 'Duvall_resultado_compañero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_compa%C3%B1ero.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'hombre', 'Duvall_resultado_hombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_hombre.glb', 2.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'joven', 'Duvall_resultado_joven.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_joven.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'mayor de edad', 'Duvall_resultado_mayor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_mayor%20de%20edad.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'mayor', 'Duvall_resultado_mayor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_mayor.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'menor de edad', 'Duvall_resultado_menor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_menor%20de%20edad.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'mujer', 'Duvall_resultado_mujer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_mujer.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'niño', 'Duvall_resultado_niño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_ni%C3%B1o.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'novio', 'Duvall_resultado_novio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_novio.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'oyente', 'Duvall_resultado_oyente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_oyente.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'persona', 'Duvall_resultado_persona.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_persona.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'personas', 'Duvall_resultado_personas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_personas.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'señor', 'Duvall_resultado_señor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_se%C3%B1or.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'señorita', 'Duvall_resultado_señorita.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_se%C3%B1orita.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'sordo', 'Duvall_resultado_sordo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_sordo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'sordociego', 'Duvall_resultado_sordociego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_sordociego.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'personas', 'viejo', 'Duvall_resultado_viejo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/personas/Duvall_resultado_viejo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - preguntas (4 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preguntas', 'como estas', 'Duvall_resultado_como estas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preguntas/Duvall_resultado_como%20estas.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preguntas', 'cual es tu nombre', 'Duvall_resultado_cual es tu nombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preguntas/Duvall_resultado_cual%20es%20tu%20nombre.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preguntas', 'cual es tu seña', 'Duvall_resultado_cual es tu seña.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preguntas/Duvall_resultado_cual%20es%20tu%20se%C3%B1a.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preguntas', 'que tal', 'Duvall_resultado_que tal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preguntas/Duvall_resultado_que%20tal.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - preposicion (15 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'algo', 'Duvall_resultado_algo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_algo.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'alguien', 'Duvall_resultado_alguien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_alguien.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'algun', 'Duvall_resultado_algun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_algun.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'bastante', 'Duvall_resultado_bastante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_bastante.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'cualquier', 'Duvall_resultado_cualquier.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_cualquier.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'demasiado', 'Duvall_resultado_demasiado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_demasiado.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'mas', 'Duvall_resultado_mas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_mas.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'mucho', 'Duvall_resultado_mucho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_mucho.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'nada', 'Duvall_resultado_nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_nada.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'nadie', 'Duvall_resultado_nadie.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_nadie.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'ningun', 'Duvall_resultado_ningun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_ningun.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'otro', 'Duvall_resultado_otro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_otro.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'poco', 'Duvall_resultado_poco.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_poco.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'quienquiera', 'Duvall_resultado_quienquiera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_quienquiera.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'preposicion', 'todo', 'Duvall_resultado_todo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/preposicion/Duvall_resultado_todo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - profesion (47 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'abogado', 'Duvall_resultado_abogado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_abogado.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'administrador', 'Duvall_resultado_administrador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_administrador.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'albañil', 'Duvall_resultado_albañil.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_alba%C3%B1il.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'analista', 'Duvall_resultado_analista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_analista.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'auxiliar', 'Duvall_resultado_auxiliar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_auxiliar.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'barbero', 'Duvall_resultado_barbero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_barbero.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'carrera', 'Duvall_resultado_carrera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_carrera.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'chef', 'Duvall_resultado_chef.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_chef.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'cocinero', 'Duvall_resultado_cocinero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_cocinero.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'conductor', 'Duvall_resultado_conductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_conductor.glb', 2.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'constructor', 'Duvall_resultado_constructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_constructor.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'contador', 'Duvall_resultado_contador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_contador.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'dentista', 'Duvall_resultado_dentista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_dentista.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'detective', 'Duvall_resultado_detective.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_detective.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'dibujante tecnico', 'Duvall_resultado_dibujante tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_dibujante%20tecnico.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'dibujante', 'Duvall_resultado_dibujante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_dibujante.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'director', 'Duvall_resultado_director.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_director.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'economista', 'Duvall_resultado_economista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_economista.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'enfermera', 'Duvall_resultado_enfermera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_enfermera.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'escritor', 'Duvall_resultado_escritor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_escritor.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'fotografo', 'Duvall_resultado_fotografo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_fotografo.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'gerente', 'Duvall_resultado_gerente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_gerente.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'informatica', 'Duvall_resultado_informatica.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_informatica.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'ingeniero', 'Duvall_resultado_ingeniero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_ingeniero.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'inspector', 'Duvall_resultado_inspector.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_inspector.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'instructor', 'Duvall_resultado_instructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_instructor.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'interprete', 'Duvall_resultado_interprete.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_interprete.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'jefe', 'Duvall_resultado_jefe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_jefe.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'licenciado', 'Duvall_resultado_licenciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_licenciado.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'maestro', 'Duvall_resultado_maestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_maestro.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'medico', 'Duvall_resultado_medico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_medico.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'mensajero', 'Duvall_resultado_mensajero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_mensajero.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'mesonero', 'Duvall_resultado_mesonero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_mesonero.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'pasante', 'Duvall_resultado_pasante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_pasante.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'peluquera', 'Duvall_resultado_peluquera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_peluquera.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'pintor', 'Duvall_resultado_pintor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_pintor.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'policia', 'Duvall_resultado_policia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_policia.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'profesion', 'Duvall_resultado_profesion.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_profesion.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'profesor', 'Duvall_resultado_profesor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_profesor.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'psicologo', 'Duvall_resultado_psicologo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_psicologo.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'secretaria', 'Duvall_resultado_secretaria.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_secretaria.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'sistema', 'Duvall_resultado_sistema.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_sistema.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'supervisor', 'Duvall_resultado_supervisor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_supervisor.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'tecnico', 'Duvall_resultado_tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_tecnico.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'traductor', 'Duvall_resultado_traductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_traductor.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'vendedor', 'Duvall_resultado_vendedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_vendedor.glb', 2.86, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'profesion', 'vigilante', 'Duvall_resultado_vigilante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/profesion/Duvall_resultado_vigilante.glb', 2.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - pronombres (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'el', 'Duvall_resultado_el.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_el.glb', 2.78, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'ella', 'Duvall_resultado_ella.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_ella.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'ellas', 'Duvall_resultado_ellas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_ellas.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'ellos', 'Duvall_resultado_ellos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_ellos.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'mio', 'Duvall_resultado_mio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_mio.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'nosotros', 'Duvall_resultado_nosotros.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_nosotros.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'nuestro', 'Duvall_resultado_nuestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_nuestro.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'suyo', 'Duvall_resultado_suyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_suyo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'tu', 'Duvall_resultado_tu.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_tu.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'tuyo', 'Duvall_resultado_tuyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_tuyo.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'ustedes', 'Duvall_resultado_ustedes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_ustedes.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'pronombres', 'yo', 'Duvall_resultado_yo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/pronombres/Duvall_resultado_yo.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - saludos (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'adios', 'Duvall_resultado_adios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/saludos/Duvall_resultado_adios.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'bienvenido', 'Duvall_resultado_bienvenido.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/saludos/Duvall_resultado_bienvenido.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'buenas noches', 'Duvall_resultado_buenas noches.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/saludos/Duvall_resultado_buenas%20noches.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'buenas tardes', 'Duvall_resultado_buenas tardes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/saludos/Duvall_resultado_buenas%20tardes.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'buenos dias', 'Duvall_resultado_buenos dias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/saludos/Duvall_resultado_buenos%20dias.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'chao', 'Duvall_resultado_chao.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/saludos/Duvall_resultado_chao.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'saludos', 'hola', 'Duvall_resultado_hola.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/saludos/Duvall_resultado_hola.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - tiempo (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'anteayer', 'Duvall_resultado_anteayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tiempo/Duvall_resultado_anteayer.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'ayer', 'Duvall_resultado_ayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tiempo/Duvall_resultado_ayer.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'calendario', 'Duvall_resultado_calendario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tiempo/Duvall_resultado_calendario.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'dia', 'Duvall_resultado_dia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tiempo/Duvall_resultado_dia.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'fin de semana', 'Duvall_resultado_fin de semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tiempo/Duvall_resultado_fin%20de%20semana.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'hoy', 'Duvall_resultado_hoy.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tiempo/Duvall_resultado_hoy.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'mañana', 'Duvall_resultado_mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tiempo/Duvall_resultado_ma%C3%B1ana.glb', 2.80, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'mes', 'Duvall_resultado_mes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tiempo/Duvall_resultado_mes.glb', 2.79, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'pasado mañana', 'Duvall_resultado_pasado mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tiempo/Duvall_resultado_pasado%20ma%C3%B1ana.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tiempo', 'semana', 'Duvall_resultado_semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tiempo/Duvall_resultado_semana.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - tipos de vivienda (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'apartamento', 'Duvall_resultado_apartamento.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tipos de vivienda/Duvall_resultado_apartamento.glb', 2.85, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'baño', 'Duvall_resultado_baño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tipos de vivienda/Duvall_resultado_ba%C3%B1o.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'casa', 'Duvall_resultado_casa.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tipos de vivienda/Duvall_resultado_casa.glb', 2.83, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'cocina', 'Duvall_resultado_cocina.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tipos de vivienda/Duvall_resultado_cocina.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'comedor', 'Duvall_resultado_comedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tipos de vivienda/Duvall_resultado_comedor.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'cuarto', 'Duvall_resultado_cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tipos de vivienda/Duvall_resultado_cuarto.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'edificio', 'Duvall_resultado_edificio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tipos de vivienda/Duvall_resultado_edificio.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'piso', 'Duvall_resultado_piso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tipos de vivienda/Duvall_resultado_piso.glb', 2.82, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'rancho', 'Duvall_resultado_rancho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tipos de vivienda/Duvall_resultado_rancho.glb', 2.84, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'tipos de vivienda', 'sala', 'Duvall_resultado_sala.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/tipos de vivienda/Duvall_resultado_sala.glb', 2.87, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Duvall - verbos (35 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'agarrar', 'Duvall_resultado_agarrar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_agarrar.glb', 4.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'amar', 'Duvall_resultado_amar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_amar.glb', 3.00, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'atraer', 'Duvall_resultado_atraer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_atraer.glb', 4.34, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'ayudar', 'Duvall_resultado_ayudar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_ayudar.glb', 2.94, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'burlar', 'Duvall_resultado_burlar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_burlar.glb', 4.40, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'calmar', 'Duvall_resultado_calmar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_calmar.glb', 4.49, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'cansar', 'Duvall_resultado_cansar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_cansar.glb', 2.97, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'comer', 'Duvall_resultado_comer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_comer.glb', 3.00, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'conocer', 'Duvall_resultado_conocer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_conocer.glb', 2.95, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'decir', 'Duvall_resultado_decir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_decir.glb', 2.96, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'deletrear', 'Duvall_resultado_deletrear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_deletrear.glb', 2.93, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'dormir', 'Duvall_resultado_dormir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_dormir.glb', 2.95, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'engañar', 'Duvall_resultado_engañar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_enga%C3%B1ar.glb', 4.30, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'estar', 'Duvall_resultado_estar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_estar.glb', 2.94, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'estudiar', 'Duvall_resultado_estudiar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_estudiar.glb', 2.94, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'guardar', 'Duvall_resultado_guardar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_guardar.glb', 4.39, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'invitar', 'Duvall_resultado_invitar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_invitar.glb', 2.97, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'llevar', 'Duvall_resultado_llevar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_llevar.glb', 4.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'pelear', 'Duvall_resultado_pelear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_pelear.glb', 4.38, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'preguntar', 'Duvall_resultado_preguntar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_preguntar.glb', 2.95, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'presentar', 'Duvall_resultado_presentar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_presentar.glb', 2.94, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'querer', 'Duvall_resultado_querer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_querer.glb', 2.96, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'regalar', 'Duvall_resultado_regalar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_regalar.glb', 4.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'responder', 'Duvall_resultado_responder.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_responder.glb', 2.97, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'saludar', 'Duvall_resultado_saludar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_saludar.glb', 2.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'sentir', 'Duvall_resultado_sentir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_sentir.glb', 2.99, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'ser', 'Duvall_resultado_ser.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_ser.glb', 4.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'sufrir', 'Duvall_resultado_sufrir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_sufrir.glb', 4.44, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'trabajar', 'Duvall_resultado_trabajar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_trabajar.glb', 2.95, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'traer', 'Duvall_resultado_traer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_traer.glb', 4.35, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'usar', 'Duvall_resultado_usar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_usar.glb', 4.43, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'ver', 'Duvall_resultado_ver.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_ver.glb', 2.97, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'verbo', 'Duvall_resultado_verbo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_verbo.glb', 4.37, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'vestir', 'Duvall_resultado_vestir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_vestir.glb', 4.42, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Duvall', 'verbos', 'vivir', 'Duvall_resultado_vivir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Duvall/verbos/Duvall_resultado_vivir.glb', 2.93, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - adverbios lugares (9 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'adverbios', 'Carla_resultado_adverbios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/adverbios lugares/Carla_resultado_adverbios.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'al lado', 'Carla_resultado_al lado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/adverbios lugares/Carla_resultado_al%20lado.glb', 3.40, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'atras', 'Carla_resultado_atras.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/adverbios lugares/Carla_resultado_atras.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'cerca', 'Carla_resultado_cerca.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/adverbios lugares/Carla_resultado_cerca.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'derecha', 'Carla_resultado_derecha.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/adverbios lugares/Carla_resultado_derecha.glb', 3.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'frente', 'Carla_resultado_frente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/adverbios lugares/Carla_resultado_frente.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'izquierda', 'Carla_resultado_izquierda.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/adverbios lugares/Carla_resultado_izquierda.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'lejos', 'Carla_resultado_lejos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/adverbios lugares/Carla_resultado_lejos.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'adverbios lugares', 'lugares', 'Carla_resultado_lugares.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/adverbios lugares/Carla_resultado_lugares.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - alfabeto (27 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'a', 'Carla_resultado_a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_a.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'b', 'Carla_resultado_b.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_b.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'c', 'Carla_resultado_c.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_c.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'd', 'Carla_resultado_d.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_d.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'e', 'Carla_resultado_e.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_e.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'f', 'Carla_resultado_f.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_f.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'g', 'Carla_resultado_g.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_g.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'h', 'Carla_resultado_h.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_h.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'i', 'Carla_resultado_i.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_i.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'j', 'Carla_resultado_j.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_j.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'k', 'Carla_resultado_k.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_k.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'l', 'Carla_resultado_l.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_l.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'm', 'Carla_resultado_m.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_m.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'n', 'Carla_resultado_n.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_n.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'o', 'Carla_resultado_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_o.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'p', 'Carla_resultado_p.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_p.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'q', 'Carla_resultado_q.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_q.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'r', 'Carla_resultado_r.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_r.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 's', 'Carla_resultado_s.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_s.glb', 3.35, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 't', 'Carla_resultado_t.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_t.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'u', 'Carla_resultado_u.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_u.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'v', 'Carla_resultado_v.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_v.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'w', 'Carla_resultado_w.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_w.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'x', 'Carla_resultado_x.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_x.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'y', 'Carla_resultado_y.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_y.glb', 3.07, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'z', 'Carla_resultado_z.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_z.glb', 3.06, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'alfabeto', 'ñ', 'Carla_resultado_ñ.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/alfabeto/Carla_resultado_%C3%B1.glb', 3.05, true)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - base (1 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'base', 'base', 'Carla.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/base/Carla.glb', 3.01, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - cortesia (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'a la orden', 'Carla_resultado_a la orden.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/cortesia/Carla_resultado_a%20la%20orden.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'buen provecho', 'Carla_resultado_buen provecho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/cortesia/Carla_resultado_buen%20provecho.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'cortesia', 'Carla_resultado_cortesia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/cortesia/Carla_resultado_cortesia.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'gracias', 'Carla_resultado_gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/cortesia/Carla_resultado_gracias.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'muchas gracias', 'Carla_resultado_muchas gracias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/cortesia/Carla_resultado_muchas%20gracias.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'mucho gusto', 'Carla_resultado_mucho gusto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/cortesia/Carla_resultado_mucho%20gusto.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'cortesia', 'permiso', 'Carla_resultado_permiso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/cortesia/Carla_resultado_permiso.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - dias_semana (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'domingo', 'Carla_resultado_domingo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/dias_semana/Carla_resultado_domingo.glb', 3.40, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'jueves', 'Carla_resultado_jueves.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/dias_semana/Carla_resultado_jueves.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'lunes', 'Carla_resultado_lunes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/dias_semana/Carla_resultado_lunes.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'martes', 'Carla_resultado_martes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/dias_semana/Carla_resultado_martes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'miercoles', 'Carla_resultado_miercoles.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/dias_semana/Carla_resultado_miercoles.glb', 3.47, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'sabado', 'Carla_resultado_sabado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/dias_semana/Carla_resultado_sabado.glb', 3.41, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'dias_semana', 'viernes', 'Carla_resultado_viernes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/dias_semana/Carla_resultado_viernes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - estado civil (6 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'casado', 'Carla_resultado_casado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/estado civil/Carla_resultado_casado.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'concubino', 'Carla_resultado_concubino.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/estado civil/Carla_resultado_concubino.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'divorciado', 'Carla_resultado_divorciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/estado civil/Carla_resultado_divorciado.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'separado', 'Carla_resultado_separado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/estado civil/Carla_resultado_separado.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'soltero', 'Carla_resultado_soltero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/estado civil/Carla_resultado_soltero.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'estado civil', 'viudo', 'Carla_resultado_viudo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/estado civil/Carla_resultado_viudo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - expresiones (30 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'abril', 'Carla_resultado_abril.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_abril.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'agosto', 'Carla_resultado_agosto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_agosto.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'bien', 'Carla_resultado_bien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_bien.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'como', 'Carla_resultado_como.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_como.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'cual', 'Carla_resultado_cual.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_cual.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'cuando', 'Carla_resultado_cuando.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_cuando.glb', 3.41, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'cuantos', 'Carla_resultado_cuantos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_cuantos.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'de nada', 'Carla_resultado_de nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_de%20nada.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'diciembre', 'Carla_resultado_diciembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_diciembre.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'donde (especifico)', 'Carla_resultado_donde (especifico).glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_donde%20(especifico).glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'donde', 'Carla_resultado_donde.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_donde.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'enero', 'Carla_resultado_enero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_enero.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'expresiones', 'Carla_resultado_expresiones.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_expresiones.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'febrero', 'Carla_resultado_febrero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_febrero.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'interrogantes', 'Carla_resultado_interrogantes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_interrogantes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'julio', 'Carla_resultado_julio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_julio.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'junio', 'Carla_resultado_junio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_junio.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'mal', 'Carla_resultado_mal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_mal.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'marzo', 'Carla_resultado_marzo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_marzo.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'mayo', 'Carla_resultado_mayo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_mayo.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'no', 'Carla_resultado_no.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_no.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'noviembre', 'Carla_resultado_noviembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_noviembre.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'octubre', 'Carla_resultado_octubre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_octubre.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'porque', 'Carla_resultado_porque.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_porque.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'que', 'Carla_resultado_que.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_que.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'quien', 'Carla_resultado_quien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_quien.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'regular', 'Carla_resultado_regular.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_regular.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'saludas a', 'Carla_resultado_saludas a.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_saludas%20a.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'septiembre', 'Carla_resultado_septiembre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_septiembre.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'expresiones', 'si', 'Carla_resultado_si.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/expresiones/Carla_resultado_si.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - horario (8 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'en punto', 'Carla_resultado_en punto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/horario/Carla_resultado_en%20punto.glb', 3.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'hora', 'Carla_resultado_hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/horario/Carla_resultado_hora.glb', 3.35, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'horario', 'Carla_resultado_horario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/horario/Carla_resultado_horario.glb', 3.41, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'media hora', 'Carla_resultado_media hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/horario/Carla_resultado_media%20hora.glb', 3.38, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'un cuarto', 'Carla_resultado_un cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/horario/Carla_resultado_un%20cuarto.glb', 3.34, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'un minuto', 'Carla_resultado_un minuto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/horario/Carla_resultado_un%20minuto.glb', 3.37, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'un segundo', 'Carla_resultado_un segundo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/horario/Carla_resultado_un%20segundo.glb', 3.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'horario', 'una hora', 'Carla_resultado_una hora.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/horario/Carla_resultado_una%20hora.glb', 3.40, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - medios transporte (0 archivos)
-- Carla - numero (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '0', 'Carla_resultado_0.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_0.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '1', 'Carla_resultado_1.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_1.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '10', 'Carla_resultado_10.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_10.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '1M', 'Carla_resultado_1M.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_1M.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '2', 'Carla_resultado_2.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_2.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '3', 'Carla_resultado_3.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_3.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '4', 'Carla_resultado_4.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_4.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '5', 'Carla_resultado_5.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_5.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '6', 'Carla_resultado_6.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_6.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '7', 'Carla_resultado_7.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_7.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '8', 'Carla_resultado_8.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_8.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numero', '9', 'Carla_resultado_9.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numero/Carla_resultado_9.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - numeros ordinales (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '10_o', 'Carla_resultado_10_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numeros ordinales/Carla_resultado_10_o.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '1_o', 'Carla_resultado_1_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numeros ordinales/Carla_resultado_1_o.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '2_o', 'Carla_resultado_2_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numeros ordinales/Carla_resultado_2_o.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '3_o', 'Carla_resultado_3_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numeros ordinales/Carla_resultado_3_o.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '4_o', 'Carla_resultado_4_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numeros ordinales/Carla_resultado_4_o.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '5_o', 'Carla_resultado_5_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numeros ordinales/Carla_resultado_5_o.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '6_o', 'Carla_resultado_6_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numeros ordinales/Carla_resultado_6_o.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '7_o', 'Carla_resultado_7_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numeros ordinales/Carla_resultado_7_o.glb', 12.44, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '8_o', 'Carla_resultado_8_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numeros ordinales/Carla_resultado_8_o.glb', 12.54, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'numeros ordinales', '9_o', 'Carla_resultado_9_o.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/numeros ordinales/Carla_resultado_9_o.glb', 12.64, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - personas (22 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'adulto', 'Carla_resultado_adulto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_adulto.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'amigo', 'Carla_resultado_amigo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_amigo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'anciano', 'Carla_resultado_anciano.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_anciano.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'bebe', 'Carla_resultado_bebe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_bebe.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'ciego', 'Carla_resultado_ciego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_ciego.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'compañero', 'Carla_resultado_compañero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_compa%C3%B1ero.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'hombre', 'Carla_resultado_hombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_hombre.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'joven', 'Carla_resultado_joven.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_joven.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'mayor de edad', 'Carla_resultado_mayor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_mayor%20de%20edad.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'mayor', 'Carla_resultado_mayor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_mayor.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'menor de edad', 'Carla_resultado_menor de edad.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_menor%20de%20edad.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'mujer', 'Carla_resultado_mujer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_mujer.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'niño', 'Carla_resultado_niño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_ni%C3%B1o.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'novio', 'Carla_resultado_novio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_novio.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'oyente', 'Carla_resultado_oyente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_oyente.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'persona', 'Carla_resultado_persona.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_persona.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'personas', 'Carla_resultado_personas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_personas.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'señor', 'Carla_resultado_señor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_se%C3%B1or.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'señorita', 'Carla_resultado_señorita.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_se%C3%B1orita.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'sordo', 'Carla_resultado_sordo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_sordo.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'sordociego', 'Carla_resultado_sordociego.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_sordociego.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'personas', 'viejo', 'Carla_resultado_viejo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/personas/Carla_resultado_viejo.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - preguntas (4 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preguntas', 'como estas', 'Carla_resultado_como estas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preguntas/Carla_resultado_como%20estas.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preguntas', 'cual es tu nombre', 'Carla_resultado_cual es tu nombre.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preguntas/Carla_resultado_cual%20es%20tu%20nombre.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preguntas', 'cual es tu seña', 'Carla_resultado_cual es tu seña.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preguntas/Carla_resultado_cual%20es%20tu%20se%C3%B1a.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preguntas', 'que tal', 'Carla_resultado_que tal.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preguntas/Carla_resultado_que%20tal.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - preposicion (15 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'algo', 'Carla_resultado_algo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_algo.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'alguien', 'Carla_resultado_alguien.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_alguien.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'algun', 'Carla_resultado_algun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_algun.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'bastante', 'Carla_resultado_bastante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_bastante.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'cualquier', 'Carla_resultado_cualquier.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_cualquier.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'demasiado', 'Carla_resultado_demasiado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_demasiado.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'mas', 'Carla_resultado_mas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_mas.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'mucho', 'Carla_resultado_mucho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_mucho.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'nada', 'Carla_resultado_nada.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_nada.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'nadie', 'Carla_resultado_nadie.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_nadie.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'ningun', 'Carla_resultado_ningun.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_ningun.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'otro', 'Carla_resultado_otro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_otro.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'poco', 'Carla_resultado_poco.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_poco.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'quienquiera', 'Carla_resultado_quienquiera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_quienquiera.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'preposicion', 'todo', 'Carla_resultado_todo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/preposicion/Carla_resultado_todo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - profesion (47 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'abogado', 'Carla_resultado_abogado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_abogado.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'administrador', 'Carla_resultado_administrador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_administrador.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'albañil', 'Carla_resultado_albañil.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_alba%C3%B1il.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'analista', 'Carla_resultado_analista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_analista.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'auxiliar', 'Carla_resultado_auxiliar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_auxiliar.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'barbero', 'Carla_resultado_barbero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_barbero.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'carrera', 'Carla_resultado_carrera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_carrera.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'chef', 'Carla_resultado_chef.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_chef.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'cocinero', 'Carla_resultado_cocinero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_cocinero.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'conductor', 'Carla_resultado_conductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_conductor.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'constructor', 'Carla_resultado_constructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_constructor.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'contador', 'Carla_resultado_contador.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_contador.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'dentista', 'Carla_resultado_dentista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_dentista.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'detective', 'Carla_resultado_detective.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_detective.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'dibujante tecnico', 'Carla_resultado_dibujante tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_dibujante%20tecnico.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'dibujante', 'Carla_resultado_dibujante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_dibujante.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'director', 'Carla_resultado_director.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_director.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'economista', 'Carla_resultado_economista.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_economista.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'enfermera', 'Carla_resultado_enfermera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_enfermera.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'escritor', 'Carla_resultado_escritor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_escritor.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'fotografo', 'Carla_resultado_fotografo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_fotografo.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'gerente', 'Carla_resultado_gerente.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_gerente.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'informatica', 'Carla_resultado_informatica.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_informatica.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'ingeniero', 'Carla_resultado_ingeniero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_ingeniero.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'inspector', 'Carla_resultado_inspector.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_inspector.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'instructor', 'Carla_resultado_instructor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_instructor.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'interprete', 'Carla_resultado_interprete.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_interprete.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'jefe', 'Carla_resultado_jefe.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_jefe.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'licenciado', 'Carla_resultado_licenciado.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_licenciado.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'maestro', 'Carla_resultado_maestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_maestro.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'medico', 'Carla_resultado_medico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_medico.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'mensajero', 'Carla_resultado_mensajero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_mensajero.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'mesonero', 'Carla_resultado_mesonero.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_mesonero.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'pasante', 'Carla_resultado_pasante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_pasante.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'peluquera', 'Carla_resultado_peluquera.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_peluquera.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'pintor', 'Carla_resultado_pintor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_pintor.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'policia', 'Carla_resultado_policia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_policia.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'profesion', 'Carla_resultado_profesion.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_profesion.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'profesor', 'Carla_resultado_profesor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_profesor.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'psicologo', 'Carla_resultado_psicologo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_psicologo.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'secretaria', 'Carla_resultado_secretaria.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_secretaria.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'sistema', 'Carla_resultado_sistema.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_sistema.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'supervisor', 'Carla_resultado_supervisor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_supervisor.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'tecnico', 'Carla_resultado_tecnico.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_tecnico.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'traductor', 'Carla_resultado_traductor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_traductor.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'vendedor', 'Carla_resultado_vendedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_vendedor.glb', 3.13, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'profesion', 'vigilante', 'Carla_resultado_vigilante.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/profesion/Carla_resultado_vigilante.glb', 3.14, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - pronombres (12 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'el', 'Carla_resultado_el.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_el.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'ella', 'Carla_resultado_ella.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_ella.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'ellas', 'Carla_resultado_ellas.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_ellas.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'ellos', 'Carla_resultado_ellos.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_ellos.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'mio', 'Carla_resultado_mio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_mio.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'nosotros', 'Carla_resultado_nosotros.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_nosotros.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'nuestro', 'Carla_resultado_nuestro.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_nuestro.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'suyo', 'Carla_resultado_suyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_suyo.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'tu', 'Carla_resultado_tu.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_tu.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'tuyo', 'Carla_resultado_tuyo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_tuyo.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'ustedes', 'Carla_resultado_ustedes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_ustedes.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'pronombres', 'yo', 'Carla_resultado_yo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/pronombres/Carla_resultado_yo.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - saludos (7 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'adios', 'Carla_resultado_adios.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/saludos/Carla_resultado_adios.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'bienvenido', 'Carla_resultado_bienvenido.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/saludos/Carla_resultado_bienvenido.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'buenas noches', 'Carla_resultado_buenas noches.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/saludos/Carla_resultado_buenas%20noches.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'buenas tardes', 'Carla_resultado_buenas tardes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/saludos/Carla_resultado_buenas%20tardes.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'buenos dias', 'Carla_resultado_buenos dias.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/saludos/Carla_resultado_buenos%20dias.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'chao', 'Carla_resultado_chao.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/saludos/Carla_resultado_chao.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'saludos', 'hola', 'Carla_resultado_hola.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/saludos/Carla_resultado_hola.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - tiempo (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'anteayer', 'Carla_resultado_anteayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tiempo/Carla_resultado_anteayer.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'ayer', 'Carla_resultado_ayer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tiempo/Carla_resultado_ayer.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'calendario', 'Carla_resultado_calendario.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tiempo/Carla_resultado_calendario.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'dia', 'Carla_resultado_dia.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tiempo/Carla_resultado_dia.glb', 3.35, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'fin de semana', 'Carla_resultado_fin de semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tiempo/Carla_resultado_fin%20de%20semana.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'hoy', 'Carla_resultado_hoy.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tiempo/Carla_resultado_hoy.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'mañana', 'Carla_resultado_mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tiempo/Carla_resultado_ma%C3%B1ana.glb', 3.06, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'mes', 'Carla_resultado_mes.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tiempo/Carla_resultado_mes.glb', 3.05, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'pasado mañana', 'Carla_resultado_pasado mañana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tiempo/Carla_resultado_pasado%20ma%C3%B1ana.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tiempo', 'semana', 'Carla_resultado_semana.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tiempo/Carla_resultado_semana.glb', 3.07, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - tipos de vivienda (10 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'apartamento', 'Carla_resultado_apartamento.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tipos de vivienda/Carla_resultado_apartamento.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'baño', 'Carla_resultado_baño.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tipos de vivienda/Carla_resultado_ba%C3%B1o.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'casa', 'Carla_resultado_casa.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tipos de vivienda/Carla_resultado_casa.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'cocina', 'Carla_resultado_cocina.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tipos de vivienda/Carla_resultado_cocina.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'comedor', 'Carla_resultado_comedor.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tipos de vivienda/Carla_resultado_comedor.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'cuarto', 'Carla_resultado_cuarto.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tipos de vivienda/Carla_resultado_cuarto.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'edificio', 'Carla_resultado_edificio.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tipos de vivienda/Carla_resultado_edificio.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'piso', 'Carla_resultado_piso.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tipos de vivienda/Carla_resultado_piso.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'rancho', 'Carla_resultado_rancho.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tipos de vivienda/Carla_resultado_rancho.glb', 3.11, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'tipos de vivienda', 'sala', 'Carla_resultado_sala.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/tipos de vivienda/Carla_resultado_sala.glb', 3.15, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

-- Carla - verbos (35 archivos)
INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'agarrar', 'Carla_resultado_agarrar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_agarrar.glb', 3.36, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'amar', 'Carla_resultado_amar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_amar.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'atraer', 'Carla_resultado_atraer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_atraer.glb', 3.23, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'ayudar', 'Carla_resultado_ayudar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_ayudar.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'burlar', 'Carla_resultado_burlar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_burlar.glb', 3.29, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'calmar', 'Carla_resultado_calmar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_calmar.glb', 4.00, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'cansar', 'Carla_resultado_cansar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_cansar.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'comer', 'Carla_resultado_comer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_comer.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'conocer', 'Carla_resultado_conocer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_conocer.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'decir', 'Carla_resultado_decir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_decir.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'deletrear', 'Carla_resultado_deletrear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_deletrear.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'dormir', 'Carla_resultado_dormir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_dormir.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'engañar', 'Carla_resultado_engañar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_enga%C3%B1ar.glb', 3.20, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'estar', 'Carla_resultado_estar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_estar.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'estudiar', 'Carla_resultado_estudiar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_estudiar.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'guardar', 'Carla_resultado_guardar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_guardar.glb', 3.28, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'invitar', 'Carla_resultado_invitar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_invitar.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'llevar', 'Carla_resultado_llevar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_llevar.glb', 3.26, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'pelear', 'Carla_resultado_pelear.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_pelear.glb', 3.27, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'preguntar', 'Carla_resultado_preguntar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_preguntar.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'presentar', 'Carla_resultado_presentar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_presentar.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'querer', 'Carla_resultado_querer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_querer.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'regalar', 'Carla_resultado_regalar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_regalar.glb', 3.26, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'responder', 'Carla_resultado_responder.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_responder.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'saludar', 'Carla_resultado_saludar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_saludar.glb', 3.08, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'sentir', 'Carla_resultado_sentir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_sentir.glb', 3.12, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'ser', 'Carla_resultado_ser.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_ser.glb', 3.22, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'sufrir', 'Carla_resultado_sufrir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_sufrir.glb', 3.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'trabajar', 'Carla_resultado_trabajar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_trabajar.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'traer', 'Carla_resultado_traer.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_traer.glb', 3.25, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'usar', 'Carla_resultado_usar.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_usar.glb', 3.32, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'ver', 'Carla_resultado_ver.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_ver.glb', 3.10, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'verbo', 'Carla_resultado_verbo.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_verbo.glb', 4.81, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'vestir', 'Carla_resultado_vestir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_vestir.glb', 3.30, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO glb_models (avatar, categoria, nombre_palabra, nombre_archivo, url_github, peso_mb, es_deletreo)
VALUES ('Carla', 'verbos', 'vivir', 'Carla_resultado_vivir.glb', 'https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/Carla/verbos/Carla_resultado_vivir.glb', 3.09, false)
ON CONFLICT (avatar, categoria, nombre_palabra) DO UPDATE SET
  url_github = EXCLUDED.url_github,
  peso_mb = EXCLUDED.peso_mb,
  updated_at = CURRENT_TIMESTAMP;

COMMIT;
