# 🧠 SISTEMA DE TRADUCCIÓN CONCEPTUAL LSV

## ✨ Nuevas Capacidades Implementadas

Tu API ahora incluye un **sistema inteligente de traducción conceptual** que traduce por **significado**, no palabra por palabra, siguiendo las reglas lingüísticas de la Lengua de Señas Venezolana (LSV).

---

## 📋 Reglas de Traducción (Orden de Aplicación)

### 1️⃣ **Corrección Ortográfica**
- Detecta y corrige errores automáticamente
- Normaliza variantes venezolanas
- Ejemplo: "tecnológico" → "tecnologico"

### 2️⃣ **Reformulación Conceptual** (PRIORITARIA)
Si una palabra **NO tiene seña documentada**, el sistema:
- ❌ **NO inventa** señas
- ✅ **Reformula** usando señas existentes
- ✅ Usa **conceptos equivalentes**

**Ejemplos de reformulación:**
```
"aporte tecnológico" → TECNOLOGÍA APORTE
"integración" → INTEGRACION
"inclusión" → INTEGRACION
"proyecto" → TRABAJO
"estudiantes" → ESTUDIAR PERSONAS
"accesibilidad" → ESPECIAL
"importante" → ESPECIAL
"defensa de tesis" → TRABAJO GRADO DEFENSA
```

### 3️⃣ **Verbos Base** para Construcción Conceptual
Cuando no hay seña directa, usa verbos base existentes:
- `AYUDAR`, `USAR`, `TRABAJAR`, `PRESENTAR`
- `ESTUDIAR`, `INTEGRAR`, `TRADUCIR`, `VER`
- `QUERER`, `CONOCER`, `DECIR`, `LLEVAR`

### 4️⃣ **Omisión Lingüística**
Elimina elementos no necesarios en LSV:
- ❌ Artículos: el, la, los, las
- ❌ Preposiciones: de, a, para, con, en
- ✅ Solo mantiene palabras con significado

### 5️⃣ **Normalización Automática**
- **Plurales → Singular**: "estudiantes" → "estudiante"
- **Verbos → Infinitivo**: "trabajó" → "trabajar"
- **Género Femenino → Masculino + MUJER**:
  ```
  "ingeniera" → INGENIERO MUJER
  "doctora" → MEDICO MUJER
  ```

### 6️⃣ **Orden Gramatical LSV**
```
TIEMPO → LUGAR → SUJETO → OBJETO → VERBO → COMPLEMENTO
```

**Ejemplo:**
```
Español: "Ayer la ingeniera trabajó en la universidad"
LSV:     AYER UNIVERSIDAD INGENIERO MUJER TRABAJAR
         ⬆️     ⬆️          ⬆️               ⬆️
       TIEMPO  LUGAR      SUJETO           VERBO
```

### 7️⃣ **Números**
- **0-10**: directos (ej: `5` → `5`)
- **11-19**: `10` + dígito (ej: `15` → `10 5`)
- **20+**: dígitos separados (ej: `25` → `2 5`)

### 8️⃣ **Deletreo** (ÚLTIMO RECURSO)
Solo se deletrea cuando:
- ✅ Es nombre propio (ej: "María", "Pedro")
- ✅ Es sigla o término técnico sin equivalente
- ✅ Ya se intentó reformulación sin éxito

---

## 🎯 Ejemplos Completos

### Ejemplo 1: Traducción Académica
```
Español: "Un aporte tecnológico para la integración de la comunidad sorda venezolana"

LSV: APORTE TECNOLOGICO INTEGRACION COMUNIDAD SORDO VENEZOLANO

Aplicó:
✅ Omisión de artículos (un, la, de)
✅ Palabras del diccionario (todas existen)
✅ Reformulación: "integración" → INTEGRACION
✅ Orden conceptual natural de LSV
```

### Ejemplo 2: Defensa de Grado
```
Español: "Defensa del trabajo de grado"

LSV: DEFENSA TRABAJO GRADO

Aplicó:
✅ Omisión de preposición "del"
✅ Orden conceptual: DEFENSA + TRABAJO + GRADO
```

### Ejemplo 3: Con Tiempo y Lugar
```
Español: "Ayer la ingeniera trabajó en la universidad"

LSV: AYER UNIVERSIDAD INGENIERO MUJER TRABAJAR

Aplicó:
✅ TIEMPO primero (ayer)
✅ LUGAR segundo (universidad)
✅ SUJETO con género (ingeniero + mujer)
✅ VERBO al final (trabajar)
✅ Verbo normalizado a infinitivo (trabajó → trabajar)
```

### Ejemplo 4: Conceptos Abstractos
```
Español: "La accesibilidad es importante para la inclusión"

LSV: ESPECIAL ESPECIAL INTEGRACION

Aplicó:
✅ Reformulación: "accesibilidad" → ESPECIAL
✅ Reformulación: "importante" → ESPECIAL
✅ Reformulación: "inclusión" → INTEGRACION
✅ Omisión de verbos ser/estar
```

### Ejemplo 5: Con Reformulación de Estudiantes
```
Español: "Los estudiantes trabajaron ayer"

LSV: AYER ESTUDIAR PERSONAS TRABAJAR

Aplicó:
✅ TIEMPO primero (ayer)
✅ Reformulación: "estudiantes" → ESTUDIAR PERSONAS
✅ Verbo normalizado: "trabajaron" → TRABAJAR
```

---

## 🔧 Uso de la API

### Endpoint: `POST /api/translate`

```json
{
  "texto": "Ayer la ingeniera trabajó en su proyecto de integración",
  "deletrear_desconocidas": true,
  "corregir_ortografia": true,
  "velocidad_deletreo": 1.2
}
```

**Respuesta:**
```json
{
  "texto_original": "Ayer la ingeniera trabajó en su proyecto de integración",
  "texto_corregido": "ayer ingeniera trabajar suyo proyecto integracion",
  "correcciones": [
    {"original": "trabajó", "corregida": "trabajar", "tipo": "normalización"}
  ],
  "animaciones": [
    {"nombre": "ayer", "categoria": "tiempo", "es_deletreo": false},
    {"nombre": "ingeniero", "categoria": "profesiones", "es_deletreo": false},
    {"nombre": "mujer", "categoria": "personas", "es_deletreo": false},
    {"nombre": "trabajar", "categoria": "verbos", "es_deletreo": false},
    {"nombre": "suyo", "categoria": "pronombres", "es_deletreo": false},
    {"nombre": "trabajo", "categoria": "general", "es_deletreo": false},
    {"nombre": "integracion", "categoria": "general", "es_deletreo": false}
  ],
  "total_animaciones": 7,
  "palabras_deletreadas": []
}
```

---

## 📚 Conceptos Reformulados Disponibles

### Académico/Tecnológico
- `aporte tecnológico` → TECNOLOGÍA APORTE
- `integración` → INTEGRACION
- `inclusión` → INTEGRACION
- `proyecto` → TRABAJO
- `tesis` → TRABAJO GRADO
- `investigación` → TRABAJAR
- `implementación` → TRABAJAR USAR
- `aplicación` → USAR
- `evaluación` → VER
- `presentación` → PRESENTAR
- `exposición` → PRESENTAR
- `demostración` → PRESENTAR

### Social/Comunidad
- `comunidad sorda` → COMUNIDAD SORDO
- `accesibilidad` → ESPECIAL
- `herramienta` → AYUDAR
- `apoyo` → AYUDAR
- `asistencia` → AYUDAR

### Abstractos
- `importante` → ESPECIAL
- `diferencia` → OTRO
- `problema` → MALO
- `solución` → AYUDAR
- `oportunidad` → PRESENTAR
- `necesidad` → QUERER
- `objetivo` → QUERER
- `resultado` → TRABAJO
- `beneficio` → AYUDAR BIEN

### Educación
- `estudiante(s)` → ESTUDIAR PERSONA(S)
- `universidad` → UNIVERSIDAD
- `profesor(a)` → PROFESOR (+ MUJER si es femenino)
- `maestro(a)` → MAESTRO (+ MUJER si es femenino)

---

## ⚙️ Configuración

### En tu código Python:
```python
from api_optimizer import LSVOptimizer

optimizer = LSVOptimizer()

resultado = optimizer.translate_to_animations(
    texto="Tu frase aquí",
    deletrear_desconocidas=True,  # Deletrear solo cuando sea necesario
    corregir_ortografia=True,      # Corregir errores automáticamente
    velocidad_deletreo=1.2          # Velocidad del deletreo (segundos/letra)
)
```

---

## ✅ ¿Qué se mantuvo de las reglas anteriores?

**TODAS las reglas existentes se mantuvieron intactas:**

✅ Sistema de deletreo automático para nombres propios
✅ Manejo de números (0-99)
✅ Sistema de género (MUJER/HOMBRE)
✅ Normalización de verbos a infinitivo
✅ Omisión de artículos y preposiciones
✅ Orden temporal (TIEMPO al inicio)
✅ Corrección ortográfica con distancia de Levenshtein
✅ Manejo de frases compuestas (2, 3, 4 palabras)
✅ Plurales → singular automático

---

## 🎓 Principio Fundamental

> **NO traducir palabra por palabra**  
> **Traducir por SIGNIFICADO y CONCEPTO**

El sistema ahora:
1. Intenta **reformular** usando señas existentes
2. Usa **verbos base** para construir significado
3. Solo como **último recurso** deletrea

---

## 🚀 ¿Qué hacer ahora?

1. **Prueba tu API** con frases académicas y conceptuales
2. **Verifica** que las reformulaciones sean naturales
3. **Agrega** más reformulaciones si encuentras conceptos frecuentes en tu dominio

Para agregar nuevas reformulaciones, edita el diccionario `reformulaciones_conceptuales` en [api_optimizer.py](api_optimizer.py#L154).

---

## 📞 Testing

```bash
# Test completo
python test_traduccion_conceptual.py

# Ver palabras disponibles
python ver_diccionario_completo.py

# Verificar palabras específicas
python check_palabras.py
```

---

**¡Tu sistema de traducción LSV ahora es más inteligente y lingüísticamente correcto! 🎉**
