# 🎯 SISTEMA EXPERTO EN LENGUA DE SEÑAS VENEZOLANA (LSV)

## 📚 Fundamentos del Sistema

Este sistema de traducción Español → LSV está basado exclusivamente en información **documental, educativa y comunitaria** proveniente de:
- **FEVENSOR** (Federación Venezolana de Sordos)
- **Consorven** (Consorcio Venezuela de Organizaciones de Sordos)
- **Aportes validados** de la comunidad sorda venezolana

---

## ⚠️ PRINCIPIOS FUNDAMENTALES (NO MODIFICABLES)

### 🚫 LO QUE NO HACE EL SISTEMA
1. ❌ **NO traduce literalmente** el español
2. ❌ **NO impone estructuras** del español en LSV
3. ❌ **NO inventa señas** inexistentes
4. ❌ **NO usa "español señado"** (palabra por palabra)

### ✅ LO QUE SÍ HACE EL SISTEMA
1. ✅ **Respeta el orden natural LSV**: CONTEXTO → TIEMPO → LUGAR → SUJETO → ACCIÓN → COMPLEMENTO
2. ✅ **Elimina elementos innecesarios**: artículos, preposiciones, conectores
3. ✅ **Reformula conceptos abstractos** usando señas existentes
4. ✅ **Respeta la iconicidad** y la intención comunicativa
5. ✅ **Deletrea solo cuando es necesario**: nombres propios, siglas, términos sin seña
6. ✅ **Usa glosas en MAYÚSCULAS** (estándar de notación LSV)

---

## 🎯 LOS 5 PATRONES LINGÜÍSTICOS LSV

### 1️⃣ PATRÓN TEMPORAL
**El tiempo se indica al INICIO de la oración**

```
Español: "Mañana presentaré el proyecto"
LSV:     MAÑANA PROYECTO PRESENTAR
         ⬆️
       TIEMPO primero + omisión de artículos + orden natural
```

**Implementación en el código:**
```python
# Las palabras de tiempo van SIEMPRE al inicio
palabras_tiempo = [p for p in palabras_procesadas if p.get('es_tiempo')]
secuencia_final = palabras_tiempo + ...
```

---

### 2️⃣ PATRÓN DE CONTEXTO
**Primero se establece el CONTEXTO antes de la acción**

```
Español: "En la universidad necesitamos un sistema de traducción"
LSV:     UNIVERSIDAD SISTEMA TRADUCIR NECESITAR
         ⬆️
       LUGAR establece contexto + omisión de artículos/preposiciones
```

**Implementación:**
```python
# Palabras de lugar van después del tiempo
palabras_lugar = [p for p in palabras_procesadas if p.get('es_lugar')]
secuencia_final = palabras_tiempo + palabras_lugar + ...
```

---

### 3️⃣ PATRÓN DE ÉNFASIS VISUAL
**Lo importante va PRIMERO**

```
Español: "Es muy importante la comunicación"
LSV:     COMUNICACIÓN IMPORTANTE MUCHO
         ⬆️
       Lo relevante primero + intensificador al final
```

**Implementación:**
```python
# Reformulación que prioriza el concepto principal
'muy importante': ['importante', 'mucho']
```

---

### 4️⃣ PATRÓN DE NEGACIÓN
**La negación va al FINAL o se refuerza con expresión facial**

```
Español: "No existe un sistema accesible"
LSV:     SISTEMA ACCESIBLE EXISTIR NO
         ⬆️
       Afirmación primero + negación al final
```

**Implementación:**
```python
# Reformulaciones que ponen la negación al final
'no existe': ['existir', 'no']
'no hay': ['tener', 'no']
```

---

### 5️⃣ PATRÓN DE CONCEPTOS ABSTRACTOS
**Los conceptos abstractos se REFORMULAN usando señas existentes**

```
Español: "Integración social"
LSV:     PERSONAS JUNTOS PARTICIPAR
         ⬆️
       No hay seña para "integración social" → se reformula conceptualmente
```

**Implementación:**
```python
# Diccionario de reformulaciones conceptuales
self.reformulaciones_conceptuales = {
    'integración social': ['personas', 'juntos', 'participar'],
    'aporte tecnológico': ['tecnologia', 'aporte'],
    'comunicación': ['comunicacion'],  # existe en diccionario
    ...
}
```

---

## 📋 PROCESO DE TRADUCCIÓN (Orden de Aplicación)

### 1️⃣ CORRECCIÓN ORTOGRÁFICA
- Detecta y corrige errores de escritura automáticamente
- Normaliza variantes venezolanas
- Usa **distancia de Levenshtein** con umbral de 80% confianza

**Ejemplo:**
```
"tecnologico" (sin tilde) → "tecnologico" (normalizado)
```

---

### 2️⃣ REFORMULACIÓN CONCEPTUAL (PRIORITARIA)
**Si una palabra NO tiene seña documentada:**
- ❌ **NO inventa** señas
- ✅ **Reformula** usando señas existentes
- ✅ Usa **conceptos equivalentes**

**Ejemplos:**
```
"aporte tecnológico" → TECNOLOGÍA APORTE
"integración"        → INCLUSIÓN (seña existente)
"estudiantes"        → ESTUDIAR PERSONAS
"accesibilidad"      → ESPECIAL
"importante"         → ESPECIAL
"defensa de tesis"   → TRABAJO GRADO DEFENSA
```

---

### 3️⃣ VERBOS BASE para Construcción Conceptual
**Cuando no hay seña directa, usa verbos base existentes:**

```python
verbos_base = {
    'ayudar', 'usar', 'trabajar', 'presentar',
    'estudiar', 'integrar', 'traducir', 'ver',
    'querer', 'conocer', 'decir', 'llevar'
}
```

**Ejemplo:**
```
"implementación" → TRABAJAR USAR (verbos base)
```

---

### 4️⃣ OMISIÓN LINGÜÍSTICA
**Elimina elementos que NO existen en LSV:**

```python
palabras_omitidas = {
    # Artículos
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas',
    
    # Preposiciones contextuales
    'de', 'del', 'al', 'a', 'para', 'por', 'con', 'en',
    
    # Conjunciones
    'y', 'e', 'o', 'u',
    
    # Verbos ser/estar (se infieren por contexto)
    'es', 'son', 'esta', 'están'
}
```

**Ejemplo:**
```
Español: "El sistema de traducción para la comunidad"
LSV:     SISTEMA TRADUCIR COMUNIDAD
         (omite: el, de, para, la)
```

---

### 5️⃣ NORMALIZACIÓN AUTOMÁTICA

**Plurales → Singular:**
```
"estudiantes" → "estudiante" → ESTUDIAR PERSONA
```

**Verbos → Infinitivo:**
```
"trabajó" → "trabajar" → TRABAJAR
"estudian" → "estudiar" → ESTUDIAR
```

**Género Femenino → Masculino + MUJER:**
```
"ingeniera" → INGENIERO MUJER
"doctora"   → MÉDICO MUJER
"maestra"   → MAESTRO MUJER
```

---

### 6️⃣ ORDEN GRAMATICAL LSV
**Estructura visual-espacial:**

```
TIEMPO → LUGAR → SUJETO → OBJETO → VERBO → COMPLEMENTO
```

**Ejemplo completo:**
```
Español: "Ayer la ingeniera trabajó en la universidad con un proyecto"
LSV:     AYER UNIVERSIDAD INGENIERO MUJER PROYECTO TRABAJAR
         ⬆️    ⬆️           ⬆️                       ⬆️
       TIEMPO LUGAR       SUJETO                  VERBO
```

---

### 7️⃣ NÚMEROS

**Sistema de numeración LSV:**
- **0-10**: señas directas
- **11-19**: `10` + dígito (ej: `15` → `10 5`)
- **20+**: dígitos separados (ej: `25` → `2 5`)

---

### 8️⃣ DELETREO (ÚLTIMO RECURSO)

**Solo se deletrea cuando:**
- ✅ Es **nombre propio** (ej: "María", "Pedro", "Venezuela")
- ✅ Es **sigla** o término técnico sin equivalente (ej: "LSV", "USB")
- ✅ Ya se intentó reformulación sin éxito

**NO se deletrea:**
- ❌ Palabras que se pueden reformular
- ❌ Conceptos con señas existentes
- ❌ Palabras que se pueden construir con verbos base

**Ejemplo de deletreo:**
```
Español: "Mi nombre es José"
LSV:     MIO J-O-S-E (cada letra se señala individualmente)
```

---

## 📚 EJEMPLOS COMPLETOS DE TRADUCCIÓN

### EJEMPLO 1: Discurso Académico
```
Entrada (español):
"Bienvenidos a la defensa de nuestro trabajo especial de grado"

Salida (LSV):
BIENVENIR DEFENSA TRABAJO GRADO NOSOTROS

Análisis:
✅ "Bienvenidos" → BIENVENIR (plural → singular)
✅ Omisión: "a", "la", "de", "especial"
✅ Orden LSV: contexto primero
✅ "nuestro" → NOSOTROS (posesivo normalizado)
```

---

### EJEMPLO 2: Objetivo del Proyecto
```
Entrada:
"Nuestro objetivo es crear un sistema de traducción de lengua de señas venezolana"

Salida:
OBJETIVO NOSOTROS SISTEMA TRADUCIR LENGUA SEÑAS VENEZUELA CREAR

Análisis:
✅ Énfasis primero: OBJETIVO
✅ Omisión: "es", "un", "de" (x3)
✅ "nuestro" → NOSOTROS
✅ "traducción" → TRADUCIR (infinitivo)
✅ Orden conceptual natural
```

---

### EJEMPLO 3: Palabra sin Seña
```
Entrada:
"Plataforma digital inclusiva"

Salida:
P-L-A-T-A-F-O-R-M-A DIGITAL INCLUIR

Análisis:
✅ "Plataforma" se deletrea (no existe seña estándar)
✅ "digital" → DIGITAL (existe en diccionario)
✅ "inclusiva" → INCLUIR (verbo base)
```

---

### EJEMPLO 4: Justificación Social
```
Entrada:
"Este proyecto busca mejorar la comunicación entre personas sordas y oyentes"

Salida:
PROYECTO ESTE BUSCAR COMUNICACIÓN MEJORAR PERSONA SORDA OYENTE

Análisis:
✅ Énfasis: PROYECTO primero
✅ Omisión: "la", "entre", "y"
✅ "personas sordas" → PERSONA SORDA (singular)
✅ Orden natural LSV respetado
```

---

### EJEMPLO 5: Contexto Temporal
```
Entrada:
"Mañana en la universidad presentaré mi proyecto de grado"

Salida:
MAÑANA UNIVERSIDAD PROYECTO GRADO PRESENTAR MIO

Análisis:
✅ PATRÓN 1: MAÑANA al inicio (tiempo primero)
✅ PATRÓN 2: UNIVERSIDAD después (contexto/lugar)
✅ Omisión: "en", "la", "mi" → MIO
✅ "presentaré" → PRESENTAR (infinitivo)
✅ Orden LSV: TIEMPO → LUGAR → OBJETO → VERBO → POSESIVO
```

---

## 🔬 ARQUITECTURA DEL SISTEMA

### Componentes Principales

```
┌─────────────────────────────────────────────────────────────┐
│                    API FastAPI (main.py)                    │
│  Endpoints: /api/translate, /api/corregir, /api/optimizar  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              LSVOptimizer (api_optimizer.py)                │
│                                                              │
│  • Diccionario: 311+ palabras LSV documentadas              │
│  • Reglas lingüísticas: 5 patrones implementados            │
│  • Reformulación conceptual automática                      │
│  • Corrección ortográfica (Levenshtein)                     │
│  • Sistema de género (HOMBRE/MUJER)                         │
│  • Deletreo dactilológico                                   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Diccionario LSV (data.json)                    │
│                                                              │
│  • 311+ palabras documentadas                               │
│  • 18 categorías semánticas                                 │
│  • Archivos GLB/GLTF para animaciones 3D                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 📤 FORMATO DE SALIDA DE LA API

```json
{
    "texto_original": "Bienvenidos a la defensa",
    "texto_corregido": "bienvenidos defensa",
    "correcciones": [
        {
            "original": "a",
            "corregida": null,
            "tipo": "omisión",
            "confianza": 100
        }
    ],
    "animaciones": [
        {
            "nombre": "bienvenir",
            "categoria": "saludos",
            "archivo": "bienvenir.glb",
            "es_deletreo": false
        },
        {
            "nombre": "defensa",
            "categoria": "academico",
            "archivo": "defensa.glb",
            "es_deletreo": false
        }
    ],
    "total_animaciones": 2,
    "palabras_deletreadas": []
}
```

---

## 🎯 CAPACIDADES DEL SISTEMA

### ✅ Lo que el sistema PUEDE hacer:
- ✅ Traducir **311+ palabras documentadas** directamente
- ✅ **Reformular conceptos abstractos** usando señas existentes
- ✅ **Corregir ortografía** automáticamente (errores comunes)
- ✅ **Normalizar plurales, verbos y género**
- ✅ **Reordenar según gramática LSV** visual-espacial
- ✅ **Deletrear nombres propios** y términos técnicos
- ✅ **Omitir elementos innecesarios** (artículos, preposiciones)
- ✅ Generar **secuencia de animaciones 3D** (.glb)

### ❌ Lo que el sistema NO puede hacer:
- ❌ **NO inventa señas** inexistentes
- ❌ **NO traduce literalmente** palabra por palabra
- ❌ **NO usa español señado**
- ❌ **NO garantiza cobertura 100%** de palabras técnicas especializadas
- ❌ **NO interpreta expresiones faciales** o movimientos corporales (solo manos)

---

## 🚀 USO DEL SISTEMA

### Endpoint Principal: `/api/translate`

**Request:**
```json
{
    "texto": "Mañana presentaré mi proyecto de grado",
    "deletrear_desconocidas": true,
    "corregir_ortografia": true,
    "velocidad_deletreo": 1.2
}
```

**Response:**
```json
{
    "texto_original": "Mañana presentaré mi proyecto de grado",
    "texto_corregido": "mañana proyecto grado presentar mio",
    "correcciones": [],
    "animaciones": [
        {"nombre": "mañana", "categoria": "tiempo", ...},
        {"nombre": "proyecto", "categoria": "academico", ...},
        {"nombre": "grado", "categoria": "academico", ...},
        {"nombre": "presentar", "categoria": "verbos", ...},
        {"nombre": "mio", "categoria": "pronombres", ...}
    ],
    "total_animaciones": 5,
    "palabras_deletreadas": []
}
```

---

## 📖 GLOSARIO DE TÉRMINOS LSV

### Glosa
**Representación escrita de una seña** en MAYÚSCULAS.
- Ejemplo: `HOLA`, `TRABAJAR`, `UNIVERSIDAD`

### Dactilología
**Deletreo manual** letra por letra usando el alfabeto LSV.
- Ejemplo: J-O-S-E para el nombre "José"

### Iconicidad
**Relación visual** entre la forma de la seña y su significado.
- Ejemplo: COMER simula llevar comida a la boca

### Español Señado
**❌ INCORRECTO**: Traducir palabra por palabra del español.
- Ejemplo incorrecto: EL NIÑO ES FELIZ
- Ejemplo correcto LSV: NIÑO FELIZ

### Orden LSV Natural
**Estructura visual-espacial**: TIEMPO → LUGAR → SUJETO → VERBO
- No es sintaxis española señada

---

## 📚 REFERENCIAS Y FUENTES

### Organizaciones
- **FEVENSOR**: Federación Venezolana de Sordos
- **Consorven**: Consorcio Venezuela de Organizaciones de Sordos

### Validación Comunitaria
- Todas las señas están **documentadas** y **validadas** por la comunidad sorda venezolana
- NO se incluyen señas inventadas o adaptadas de otros países
- Respeta las **variantes regionales** venezolanas

---

## 🎓 PRINCIPIO FUNDAMENTAL

> **"Actúa siempre como intérprete y lingüista, no como traductor automático."**

Prioriza:
1. **Claridad visual** (pensamiento visual-espacial)
2. **Comprensión** (intención comunicativa)
3. **Naturalidad en LSV** (no español señado)

Cada traducción debe ser **comprensible para una persona sorda venezolana** sin conocimiento del español escrito.

---

## ✨ CONCLUSIÓN

Este sistema NO es un traductor automático palabra por palabra. Es un **sistema experto lingüístico** que:

- ✅ Comprende la **estructura visual-espacial** de LSV
- ✅ Respeta los **patrones culturales** de la comunidad sorda venezolana
- ✅ Prioriza **significado sobre literalidad**
- ✅ Usa **SOLO señas documentadas y validadas**
- ✅ Reformula conceptos abstractos de forma **natural e icónica**

**El objetivo es comunicar, no transcribir.**

---

*Última actualización: Febrero 2026*
*Versión del sistema: 2.0.0*
