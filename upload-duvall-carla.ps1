# Script PowerShell para subir Duvall y Carla a GitHub Releases
# Requiere GitHub CLI instalado y autenticado

$ErrorActionPreference = "Continue"

$REPO = "usm-argenis/Avatar_LSV"
$RELEASE_TAG = "models-v1"

# Crear release único para todos los modelos
Write-Host "📦 Creando release models-v1..."
gh release create $RELEASE_TAG --repo $REPO --title "Modelos GLB - Duvall y Carla" --notes "Archivos GLB para avatares Duvall y Carla con todas las categorías"

Write-Host "📤 Subiendo archivos en lotes..."
$totalGroups = 40
$currentGroup = 0


# Duvall - adverbios lugares (9 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - adverbios lugares..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/adverbios lugares/Duvall_resultado_adverbios.glb" `
  "test/output/glb/Duvall/adverbios lugares/Duvall_resultado_al lado.glb" `
  "test/output/glb/Duvall/adverbios lugares/Duvall_resultado_atras.glb" `
  "test/output/glb/Duvall/adverbios lugares/Duvall_resultado_cerca.glb" `
  "test/output/glb/Duvall/adverbios lugares/Duvall_resultado_derecha.glb" `
  "test/output/glb/Duvall/adverbios lugares/Duvall_resultado_frente.glb" `
  "test/output/glb/Duvall/adverbios lugares/Duvall_resultado_izquierda.glb" `
  "test/output/glb/Duvall/adverbios lugares/Duvall_resultado_lejos.glb" `
  "test/output/glb/Duvall/adverbios lugares/Duvall_resultado_lugares.glb" `
  --repo $REPO --clobber


# Duvall - alfabeto (27 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - alfabeto..."

Write-Host "  Lote 1/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_a.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_b.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_c.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_d.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_e.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_f.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_g.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_h.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_i.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_j.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_k.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_l.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_m.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_n.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_o.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_p.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_q.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_r.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_s.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_t.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 2/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_u.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_v.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_w.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_x.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_y.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_z.glb" `
  "test/output/glb/Duvall/alfabeto/Duvall_resultado_ñ.glb" `
  --repo $REPO --clobber


# Duvall - cortesia (7 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - cortesia..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/cortesia/Duvall_resultado_a la orden.glb" `
  "test/output/glb/Duvall/cortesia/Duvall_resultado_buen provecho.glb" `
  "test/output/glb/Duvall/cortesia/Duvall_resultado_cortesia.glb" `
  "test/output/glb/Duvall/cortesia/Duvall_resultado_gracias.glb" `
  "test/output/glb/Duvall/cortesia/Duvall_resultado_muchas gracias.glb" `
  "test/output/glb/Duvall/cortesia/Duvall_resultado_mucho gusto.glb" `
  "test/output/glb/Duvall/cortesia/Duvall_resultado_permiso.glb" `
  --repo $REPO --clobber


# Duvall - dias_semana (7 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - dias_semana..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/dias_semana/Duvall_resultado_domingo.glb" `
  "test/output/glb/Duvall/dias_semana/Duvall_resultado_jueves.glb" `
  "test/output/glb/Duvall/dias_semana/Duvall_resultado_lunes.glb" `
  "test/output/glb/Duvall/dias_semana/Duvall_resultado_martes.glb" `
  "test/output/glb/Duvall/dias_semana/Duvall_resultado_miercoles.glb" `
  "test/output/glb/Duvall/dias_semana/Duvall_resultado_sabado.glb" `
  "test/output/glb/Duvall/dias_semana/Duvall_resultado_viernes.glb" `
  --repo $REPO --clobber


# Duvall - base (1 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - base..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/Duvall.glb" `
  --repo $REPO --clobber


# Duvall - estado civil (6 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - estado civil..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/estado civil/Duvall_resultado_casado.glb" `
  "test/output/glb/Duvall/estado civil/Duvall_resultado_concubino.glb" `
  "test/output/glb/Duvall/estado civil/Duvall_resultado_divorciado.glb" `
  "test/output/glb/Duvall/estado civil/Duvall_resultado_separado.glb" `
  "test/output/glb/Duvall/estado civil/Duvall_resultado_soltero.glb" `
  "test/output/glb/Duvall/estado civil/Duvall_resultado_viudo.glb" `
  --repo $REPO --clobber


# Duvall - expresiones (30 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - expresiones..."

Write-Host "  Lote 1/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_abril.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_agosto.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_bien.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_como.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_cual.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_cuando.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_cuantos.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_de nada.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_diciembre.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_donde (especifico).glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_donde.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_enero.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_expresiones.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_febrero.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_interrogantes.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_julio.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_junio.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_mal.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_marzo.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_mayo.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 2/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_no.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_noviembre.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_octubre.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_porque.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_que.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_quien.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_regular.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_saludas a.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_septiembre.glb" `
  "test/output/glb/Duvall/expresiones/Duvall_resultado_si.glb" `
  --repo $REPO --clobber


# Duvall - horario (8 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - horario..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/horario/Duvall_resultado_en punto.glb" `
  "test/output/glb/Duvall/horario/Duvall_resultado_hora.glb" `
  "test/output/glb/Duvall/horario/Duvall_resultado_horario.glb" `
  "test/output/glb/Duvall/horario/Duvall_resultado_media hora.glb" `
  "test/output/glb/Duvall/horario/Duvall_resultado_un cuarto.glb" `
  "test/output/glb/Duvall/horario/Duvall_resultado_un minuto.glb" `
  "test/output/glb/Duvall/horario/Duvall_resultado_un segundo.glb" `
  "test/output/glb/Duvall/horario/Duvall_resultado_una hora.glb" `
  --repo $REPO --clobber


# Duvall - medios transporte (0 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - medios transporte..."


# Duvall - numero (12 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - numero..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/numero/Duvall_resultado_0.glb" `
  "test/output/glb/Duvall/numero/Duvall_resultado_1.glb" `
  "test/output/glb/Duvall/numero/Duvall_resultado_10.glb" `
  "test/output/glb/Duvall/numero/Duvall_resultado_1M.glb" `
  "test/output/glb/Duvall/numero/Duvall_resultado_2.glb" `
  "test/output/glb/Duvall/numero/Duvall_resultado_3.glb" `
  "test/output/glb/Duvall/numero/Duvall_resultado_4.glb" `
  "test/output/glb/Duvall/numero/Duvall_resultado_5.glb" `
  "test/output/glb/Duvall/numero/Duvall_resultado_6.glb" `
  "test/output/glb/Duvall/numero/Duvall_resultado_7.glb" `
  "test/output/glb/Duvall/numero/Duvall_resultado_8.glb" `
  "test/output/glb/Duvall/numero/Duvall_resultado_9.glb" `
  --repo $REPO --clobber


# Duvall - numeros ordinales (10 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - numeros ordinales..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/numeros ordinales/Duvall_resultado_10_o.glb" `
  "test/output/glb/Duvall/numeros ordinales/Duvall_resultado_1_o.glb" `
  "test/output/glb/Duvall/numeros ordinales/Duvall_resultado_2_o.glb" `
  "test/output/glb/Duvall/numeros ordinales/Duvall_resultado_3_o.glb" `
  "test/output/glb/Duvall/numeros ordinales/Duvall_resultado_4_o.glb" `
  "test/output/glb/Duvall/numeros ordinales/Duvall_resultado_5_o.glb" `
  "test/output/glb/Duvall/numeros ordinales/Duvall_resultado_6_o.glb" `
  "test/output/glb/Duvall/numeros ordinales/Duvall_resultado_7_o.glb" `
  "test/output/glb/Duvall/numeros ordinales/Duvall_resultado_8_o.glb" `
  "test/output/glb/Duvall/numeros ordinales/Duvall_resultado_9_o.glb" `
  --repo $REPO --clobber


# Duvall - personas (22 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - personas..."

Write-Host "  Lote 1/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/personas/Duvall_resultado_adulto.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_amigo.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_anciano.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_bebe.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_ciego.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_compañero.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_hombre.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_joven.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_mayor de edad.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_mayor.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_menor de edad.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_mujer.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_niño.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_novio.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_oyente.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_persona.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_personas.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_señor.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_señorita.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_sordo.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 2/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/personas/Duvall_resultado_sordociego.glb" `
  "test/output/glb/Duvall/personas/Duvall_resultado_viejo.glb" `
  --repo $REPO --clobber


# Duvall - preguntas (4 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - preguntas..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/preguntas/Duvall_resultado_como estas.glb" `
  "test/output/glb/Duvall/preguntas/Duvall_resultado_cual es tu nombre.glb" `
  "test/output/glb/Duvall/preguntas/Duvall_resultado_cual es tu seña.glb" `
  "test/output/glb/Duvall/preguntas/Duvall_resultado_que tal.glb" `
  --repo $REPO --clobber


# Duvall - preposicion (15 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - preposicion..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_algo.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_alguien.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_algun.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_bastante.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_cualquier.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_demasiado.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_mas.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_mucho.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_nada.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_nadie.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_ningun.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_otro.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_poco.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_quienquiera.glb" `
  "test/output/glb/Duvall/preposicion/Duvall_resultado_todo.glb" `
  --repo $REPO --clobber


# Duvall - profesion (47 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - profesion..."

Write-Host "  Lote 1/3..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/profesion/Duvall_resultado_abogado.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_administrador.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_albañil.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_analista.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_auxiliar.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_barbero.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_carrera.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_chef.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_cocinero.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_conductor.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_constructor.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_contador.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_dentista.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_detective.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_dibujante tecnico.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_dibujante.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_director.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_economista.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_enfermera.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_escritor.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 2/3..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/profesion/Duvall_resultado_fotografo.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_gerente.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_informatica.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_ingeniero.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_inspector.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_instructor.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_interprete.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_jefe.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_licenciado.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_maestro.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_medico.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_mensajero.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_mesonero.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_pasante.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_peluquera.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_pintor.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_policia.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_profesion.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_profesor.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_psicologo.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 3/3..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/profesion/Duvall_resultado_secretaria.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_sistema.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_supervisor.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_tecnico.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_traductor.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_vendedor.glb" `
  "test/output/glb/Duvall/profesion/Duvall_resultado_vigilante.glb" `
  --repo $REPO --clobber


# Duvall - pronombres (12 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - pronombres..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_el.glb" `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_ella.glb" `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_ellas.glb" `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_ellos.glb" `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_mio.glb" `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_nosotros.glb" `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_nuestro.glb" `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_suyo.glb" `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_tu.glb" `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_tuyo.glb" `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_ustedes.glb" `
  "test/output/glb/Duvall/pronombres/Duvall_resultado_yo.glb" `
  --repo $REPO --clobber


# Duvall - saludos (7 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - saludos..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/saludos/Duvall_resultado_adios.glb" `
  "test/output/glb/Duvall/saludos/Duvall_resultado_bienvenido.glb" `
  "test/output/glb/Duvall/saludos/Duvall_resultado_buenas noches.glb" `
  "test/output/glb/Duvall/saludos/Duvall_resultado_buenas tardes.glb" `
  "test/output/glb/Duvall/saludos/Duvall_resultado_buenos dias.glb" `
  "test/output/glb/Duvall/saludos/Duvall_resultado_chao.glb" `
  "test/output/glb/Duvall/saludos/Duvall_resultado_hola.glb" `
  --repo $REPO --clobber


# Duvall - tiempo (10 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - tiempo..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/tiempo/Duvall_resultado_anteayer.glb" `
  "test/output/glb/Duvall/tiempo/Duvall_resultado_ayer.glb" `
  "test/output/glb/Duvall/tiempo/Duvall_resultado_calendario.glb" `
  "test/output/glb/Duvall/tiempo/Duvall_resultado_dia.glb" `
  "test/output/glb/Duvall/tiempo/Duvall_resultado_fin de semana.glb" `
  "test/output/glb/Duvall/tiempo/Duvall_resultado_hoy.glb" `
  "test/output/glb/Duvall/tiempo/Duvall_resultado_mañana.glb" `
  "test/output/glb/Duvall/tiempo/Duvall_resultado_mes.glb" `
  "test/output/glb/Duvall/tiempo/Duvall_resultado_pasado mañana.glb" `
  "test/output/glb/Duvall/tiempo/Duvall_resultado_semana.glb" `
  --repo $REPO --clobber


# Duvall - tipos de vivienda (10 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - tipos de vivienda..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/tipos de vivienda/Duvall_resultado_apartamento.glb" `
  "test/output/glb/Duvall/tipos de vivienda/Duvall_resultado_baño.glb" `
  "test/output/glb/Duvall/tipos de vivienda/Duvall_resultado_casa.glb" `
  "test/output/glb/Duvall/tipos de vivienda/Duvall_resultado_cocina.glb" `
  "test/output/glb/Duvall/tipos de vivienda/Duvall_resultado_comedor.glb" `
  "test/output/glb/Duvall/tipos de vivienda/Duvall_resultado_cuarto.glb" `
  "test/output/glb/Duvall/tipos de vivienda/Duvall_resultado_edificio.glb" `
  "test/output/glb/Duvall/tipos de vivienda/Duvall_resultado_piso.glb" `
  "test/output/glb/Duvall/tipos de vivienda/Duvall_resultado_rancho.glb" `
  "test/output/glb/Duvall/tipos de vivienda/Duvall_resultado_sala.glb" `
  --repo $REPO --clobber


# Duvall - verbos (35 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Duvall - verbos..."

Write-Host "  Lote 1/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/verbos/Duvall_resultado_agarrar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_amar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_atraer.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_ayudar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_burlar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_calmar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_cansar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_comer.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_conocer.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_decir.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_deletrear.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_dormir.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_engañar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_estar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_estudiar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_guardar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_invitar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_llevar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_pelear.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_preguntar.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 2/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Duvall/verbos/Duvall_resultado_presentar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_querer.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_regalar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_responder.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_saludar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_sentir.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_ser.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_sufrir.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_trabajar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_traer.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_usar.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_ver.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_verbo.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_vestir.glb" `
  "test/output/glb/Duvall/verbos/Duvall_resultado_vivir.glb" `
  --repo $REPO --clobber


# Carla - adverbios lugares (9 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - adverbios lugares..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/adverbios lugares/Carla_resultado_adverbios.glb" `
  "test/output/glb/Carla/adverbios lugares/Carla_resultado_al lado.glb" `
  "test/output/glb/Carla/adverbios lugares/Carla_resultado_atras.glb" `
  "test/output/glb/Carla/adverbios lugares/Carla_resultado_cerca.glb" `
  "test/output/glb/Carla/adverbios lugares/Carla_resultado_derecha.glb" `
  "test/output/glb/Carla/adverbios lugares/Carla_resultado_frente.glb" `
  "test/output/glb/Carla/adverbios lugares/Carla_resultado_izquierda.glb" `
  "test/output/glb/Carla/adverbios lugares/Carla_resultado_lejos.glb" `
  "test/output/glb/Carla/adverbios lugares/Carla_resultado_lugares.glb" `
  --repo $REPO --clobber


# Carla - alfabeto (27 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - alfabeto..."

Write-Host "  Lote 1/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/alfabeto/Carla_resultado_a.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_b.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_c.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_d.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_e.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_f.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_g.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_h.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_i.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_j.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_k.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_l.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_m.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_n.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_o.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_p.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_q.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_r.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_s.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_t.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 2/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/alfabeto/Carla_resultado_u.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_v.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_w.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_x.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_y.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_z.glb" `
  "test/output/glb/Carla/alfabeto/Carla_resultado_ñ.glb" `
  --repo $REPO --clobber


# Carla - base (1 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - base..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/Carla.glb" `
  --repo $REPO --clobber


# Carla - cortesia (7 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - cortesia..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/cortesia/Carla_resultado_a la orden.glb" `
  "test/output/glb/Carla/cortesia/Carla_resultado_buen provecho.glb" `
  "test/output/glb/Carla/cortesia/Carla_resultado_cortesia.glb" `
  "test/output/glb/Carla/cortesia/Carla_resultado_gracias.glb" `
  "test/output/glb/Carla/cortesia/Carla_resultado_muchas gracias.glb" `
  "test/output/glb/Carla/cortesia/Carla_resultado_mucho gusto.glb" `
  "test/output/glb/Carla/cortesia/Carla_resultado_permiso.glb" `
  --repo $REPO --clobber


# Carla - dias_semana (7 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - dias_semana..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/dias_semana/Carla_resultado_domingo.glb" `
  "test/output/glb/Carla/dias_semana/Carla_resultado_jueves.glb" `
  "test/output/glb/Carla/dias_semana/Carla_resultado_lunes.glb" `
  "test/output/glb/Carla/dias_semana/Carla_resultado_martes.glb" `
  "test/output/glb/Carla/dias_semana/Carla_resultado_miercoles.glb" `
  "test/output/glb/Carla/dias_semana/Carla_resultado_sabado.glb" `
  "test/output/glb/Carla/dias_semana/Carla_resultado_viernes.glb" `
  --repo $REPO --clobber


# Carla - estado civil (6 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - estado civil..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/estado civil/Carla_resultado_casado.glb" `
  "test/output/glb/Carla/estado civil/Carla_resultado_concubino.glb" `
  "test/output/glb/Carla/estado civil/Carla_resultado_divorciado.glb" `
  "test/output/glb/Carla/estado civil/Carla_resultado_separado.glb" `
  "test/output/glb/Carla/estado civil/Carla_resultado_soltero.glb" `
  "test/output/glb/Carla/estado civil/Carla_resultado_viudo.glb" `
  --repo $REPO --clobber


# Carla - expresiones (30 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - expresiones..."

Write-Host "  Lote 1/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/expresiones/Carla_resultado_abril.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_agosto.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_bien.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_como.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_cual.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_cuando.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_cuantos.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_de nada.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_diciembre.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_donde (especifico).glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_donde.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_enero.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_expresiones.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_febrero.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_interrogantes.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_julio.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_junio.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_mal.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_marzo.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_mayo.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 2/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/expresiones/Carla_resultado_no.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_noviembre.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_octubre.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_porque.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_que.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_quien.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_regular.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_saludas a.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_septiembre.glb" `
  "test/output/glb/Carla/expresiones/Carla_resultado_si.glb" `
  --repo $REPO --clobber


# Carla - horario (8 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - horario..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/horario/Carla_resultado_en punto.glb" `
  "test/output/glb/Carla/horario/Carla_resultado_hora.glb" `
  "test/output/glb/Carla/horario/Carla_resultado_horario.glb" `
  "test/output/glb/Carla/horario/Carla_resultado_media hora.glb" `
  "test/output/glb/Carla/horario/Carla_resultado_un cuarto.glb" `
  "test/output/glb/Carla/horario/Carla_resultado_un minuto.glb" `
  "test/output/glb/Carla/horario/Carla_resultado_un segundo.glb" `
  "test/output/glb/Carla/horario/Carla_resultado_una hora.glb" `
  --repo $REPO --clobber


# Carla - medios transporte (0 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - medios transporte..."


# Carla - numero (12 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - numero..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/numero/Carla_resultado_0.glb" `
  "test/output/glb/Carla/numero/Carla_resultado_1.glb" `
  "test/output/glb/Carla/numero/Carla_resultado_10.glb" `
  "test/output/glb/Carla/numero/Carla_resultado_1M.glb" `
  "test/output/glb/Carla/numero/Carla_resultado_2.glb" `
  "test/output/glb/Carla/numero/Carla_resultado_3.glb" `
  "test/output/glb/Carla/numero/Carla_resultado_4.glb" `
  "test/output/glb/Carla/numero/Carla_resultado_5.glb" `
  "test/output/glb/Carla/numero/Carla_resultado_6.glb" `
  "test/output/glb/Carla/numero/Carla_resultado_7.glb" `
  "test/output/glb/Carla/numero/Carla_resultado_8.glb" `
  "test/output/glb/Carla/numero/Carla_resultado_9.glb" `
  --repo $REPO --clobber


# Carla - numeros ordinales (10 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - numeros ordinales..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/numeros ordinales/Carla_resultado_10_o.glb" `
  "test/output/glb/Carla/numeros ordinales/Carla_resultado_1_o.glb" `
  "test/output/glb/Carla/numeros ordinales/Carla_resultado_2_o.glb" `
  "test/output/glb/Carla/numeros ordinales/Carla_resultado_3_o.glb" `
  "test/output/glb/Carla/numeros ordinales/Carla_resultado_4_o.glb" `
  "test/output/glb/Carla/numeros ordinales/Carla_resultado_5_o.glb" `
  "test/output/glb/Carla/numeros ordinales/Carla_resultado_6_o.glb" `
  "test/output/glb/Carla/numeros ordinales/Carla_resultado_7_o.glb" `
  "test/output/glb/Carla/numeros ordinales/Carla_resultado_8_o.glb" `
  "test/output/glb/Carla/numeros ordinales/Carla_resultado_9_o.glb" `
  --repo $REPO --clobber


# Carla - personas (22 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - personas..."

Write-Host "  Lote 1/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/personas/Carla_resultado_adulto.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_amigo.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_anciano.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_bebe.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_ciego.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_compañero.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_hombre.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_joven.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_mayor de edad.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_mayor.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_menor de edad.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_mujer.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_niño.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_novio.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_oyente.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_persona.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_personas.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_señor.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_señorita.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_sordo.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 2/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/personas/Carla_resultado_sordociego.glb" `
  "test/output/glb/Carla/personas/Carla_resultado_viejo.glb" `
  --repo $REPO --clobber


# Carla - preguntas (4 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - preguntas..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/preguntas/Carla_resultado_como estas.glb" `
  "test/output/glb/Carla/preguntas/Carla_resultado_cual es tu nombre.glb" `
  "test/output/glb/Carla/preguntas/Carla_resultado_cual es tu seña.glb" `
  "test/output/glb/Carla/preguntas/Carla_resultado_que tal.glb" `
  --repo $REPO --clobber


# Carla - preposicion (15 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - preposicion..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/preposicion/Carla_resultado_algo.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_alguien.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_algun.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_bastante.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_cualquier.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_demasiado.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_mas.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_mucho.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_nada.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_nadie.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_ningun.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_otro.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_poco.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_quienquiera.glb" `
  "test/output/glb/Carla/preposicion/Carla_resultado_todo.glb" `
  --repo $REPO --clobber


# Carla - profesion (47 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - profesion..."

Write-Host "  Lote 1/3..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/profesion/Carla_resultado_abogado.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_administrador.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_albañil.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_analista.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_auxiliar.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_barbero.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_carrera.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_chef.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_cocinero.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_conductor.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_constructor.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_contador.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_dentista.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_detective.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_dibujante tecnico.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_dibujante.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_director.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_economista.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_enfermera.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_escritor.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 2/3..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/profesion/Carla_resultado_fotografo.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_gerente.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_informatica.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_ingeniero.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_inspector.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_instructor.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_interprete.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_jefe.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_licenciado.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_maestro.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_medico.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_mensajero.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_mesonero.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_pasante.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_peluquera.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_pintor.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_policia.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_profesion.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_profesor.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_psicologo.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 3/3..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/profesion/Carla_resultado_secretaria.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_sistema.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_supervisor.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_tecnico.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_traductor.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_vendedor.glb" `
  "test/output/glb/Carla/profesion/Carla_resultado_vigilante.glb" `
  --repo $REPO --clobber


# Carla - pronombres (12 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - pronombres..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/pronombres/Carla_resultado_el.glb" `
  "test/output/glb/Carla/pronombres/Carla_resultado_ella.glb" `
  "test/output/glb/Carla/pronombres/Carla_resultado_ellas.glb" `
  "test/output/glb/Carla/pronombres/Carla_resultado_ellos.glb" `
  "test/output/glb/Carla/pronombres/Carla_resultado_mio.glb" `
  "test/output/glb/Carla/pronombres/Carla_resultado_nosotros.glb" `
  "test/output/glb/Carla/pronombres/Carla_resultado_nuestro.glb" `
  "test/output/glb/Carla/pronombres/Carla_resultado_suyo.glb" `
  "test/output/glb/Carla/pronombres/Carla_resultado_tu.glb" `
  "test/output/glb/Carla/pronombres/Carla_resultado_tuyo.glb" `
  "test/output/glb/Carla/pronombres/Carla_resultado_ustedes.glb" `
  "test/output/glb/Carla/pronombres/Carla_resultado_yo.glb" `
  --repo $REPO --clobber


# Carla - saludos (7 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - saludos..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/saludos/Carla_resultado_adios.glb" `
  "test/output/glb/Carla/saludos/Carla_resultado_bienvenido.glb" `
  "test/output/glb/Carla/saludos/Carla_resultado_buenas noches.glb" `
  "test/output/glb/Carla/saludos/Carla_resultado_buenas tardes.glb" `
  "test/output/glb/Carla/saludos/Carla_resultado_buenos dias.glb" `
  "test/output/glb/Carla/saludos/Carla_resultado_chao.glb" `
  "test/output/glb/Carla/saludos/Carla_resultado_hola.glb" `
  --repo $REPO --clobber


# Carla - tiempo (10 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - tiempo..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/tiempo/Carla_resultado_anteayer.glb" `
  "test/output/glb/Carla/tiempo/Carla_resultado_ayer.glb" `
  "test/output/glb/Carla/tiempo/Carla_resultado_calendario.glb" `
  "test/output/glb/Carla/tiempo/Carla_resultado_dia.glb" `
  "test/output/glb/Carla/tiempo/Carla_resultado_fin de semana.glb" `
  "test/output/glb/Carla/tiempo/Carla_resultado_hoy.glb" `
  "test/output/glb/Carla/tiempo/Carla_resultado_mañana.glb" `
  "test/output/glb/Carla/tiempo/Carla_resultado_mes.glb" `
  "test/output/glb/Carla/tiempo/Carla_resultado_pasado mañana.glb" `
  "test/output/glb/Carla/tiempo/Carla_resultado_semana.glb" `
  --repo $REPO --clobber


# Carla - tipos de vivienda (10 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - tipos de vivienda..."

Write-Host "  Lote 1/1..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/tipos de vivienda/Carla_resultado_apartamento.glb" `
  "test/output/glb/Carla/tipos de vivienda/Carla_resultado_baño.glb" `
  "test/output/glb/Carla/tipos de vivienda/Carla_resultado_casa.glb" `
  "test/output/glb/Carla/tipos de vivienda/Carla_resultado_cocina.glb" `
  "test/output/glb/Carla/tipos de vivienda/Carla_resultado_comedor.glb" `
  "test/output/glb/Carla/tipos de vivienda/Carla_resultado_cuarto.glb" `
  "test/output/glb/Carla/tipos de vivienda/Carla_resultado_edificio.glb" `
  "test/output/glb/Carla/tipos de vivienda/Carla_resultado_piso.glb" `
  "test/output/glb/Carla/tipos de vivienda/Carla_resultado_rancho.glb" `
  "test/output/glb/Carla/tipos de vivienda/Carla_resultado_sala.glb" `
  --repo $REPO --clobber


# Carla - verbos (35 archivos)
$currentGroup++
Write-Host "[$currentGroup/$totalGroups] Subiendo Carla - verbos..."

Write-Host "  Lote 1/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/verbos/Carla_resultado_agarrar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_amar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_atraer.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_ayudar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_burlar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_calmar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_cansar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_comer.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_conocer.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_decir.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_deletrear.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_dormir.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_engañar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_estar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_estudiar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_guardar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_invitar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_llevar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_pelear.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_preguntar.glb" `
  --repo $REPO --clobber

Write-Host "  Lote 2/2..."
gh release upload $RELEASE_TAG `
  "test/output/glb/Carla/verbos/Carla_resultado_presentar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_querer.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_regalar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_responder.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_saludar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_sentir.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_ser.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_sufrir.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_trabajar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_traer.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_usar.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_ver.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_verbo.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_vestir.glb" `
  "test/output/glb/Carla/verbos/Carla_resultado_vivir.glb" `
  --repo $REPO --clobber

Write-Host ""
Write-Host "✅ Subida completa!" -ForegroundColor Green
Write-Host "🔗 Ver release: https://github.com/$REPO/releases/tag/$RELEASE_TAG"
