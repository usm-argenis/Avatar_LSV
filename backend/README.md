# API LSV - Backend con Reglas Lingüísticas Completas + Corrección Ortográfica

## ✅ Reglas LSV Implementadas

### 1. **🔧 Corrección Ortográfica Automática (NUEVO)**
- Detecta errores de escritura usando distancia de Levenshtein
- Corrige automáticamente con nivel de confianza
- Ejemplos:
  - "ola" → "hola" (70% confianza)
  - "traajo" → "trabajo" (70% confianza)
  - "estuido" → "estudio" (70% confianza)

### 2. **Omisión de Palabras**
- Artículos: el, la, los, las, un, una
- Preposiciones: de, del, al, a
- Conectores: y, e, o, u

### 2. **Género Femenino**
- Sustantivos neutros por defecto
- Palabras femeninas → masculino + MUJER
- Ejemplo: "maestra" → MAESTRO MUJER

### 3. **Normalización de Verbos**
- Todas las conjugaciones → infinitivo
- Ejemplo: "trabajo" → TRABAJAR, "estudio" → ESTUDIAR

### 4. **Números**
- 0-10: glosa directa
- 11-19: 10 + segundo dígito (12 → 10 2)
- 20+: separar dígitos (25 → 2 5)

### 5. **Posesivos**
- mi/mis → MIO
- tu/tus → TUYO
- su/sus → SUYO

### 6. **Plurales**
- todos/todas → TODO
- muchos/muchas → MUCHO
- días → DIA

### 7. **Tiempo al Inicio**
- Palabras de tiempo se mueven al inicio
- Ejemplo: "viajo mañana" → MAÑANA VIAJAR

### 8. **Deletreo Automático**
- Palabras desconocidas se deletrean
- Ejemplo: "pizza" → DELETREAR P I Z Z A

## 🚀 Uso del Backend

### Iniciar servidor:
```bash
cd backend
python main.py
```

### Endpoints:

#### POST /api/corregir (NUEVO)
Corrige ortografía sin traducir:
```json
{ermana traaja en la univercidad",
  "deletrear_desconocidas": true,
  "corregir_ortografia": true
}
```

**Respuesta:**
```json
{
  "texto_original": "mi ermana traaja en la univercidad",
  "texto_corregido": "mio hermana trabajar universidad",
  "correcciones": [
    {
      "original": "mi",
      "corregida": "mio",
      "tipo": "normalización",
      "confianza": 100
    },
    {
      "original": "ermana",
      "corregida": "hermana",
      "tipo": "ortografía",
      "distancia": 1,
      "confianza": 70
    },
    {
      "original": "traaja",
      "corregida": "trabajar",
      "tipo": "ortografía",
      "distancia": 2,
      "confianza": 40
    },
    {
      "original": "univercidad",
      "corregida": "universidad",
      "tipo": "ortografía",
      "distancia": 1,
      "confianza": 70
    }
  ]
  "texto_corregido": "hola como estar",
  "correcciones": [
    {
      "original": "ola",
      "corregida": "hola",
      "tipo": "ortografía",
      "distancia": 1,
      "confianza": 70
    },
    {
      "original": "cmo",
      "corregida": "como",
      "tipo": "ortografía",
      "distancia": 1,
      "confianza": 70
    },
    {
      "original": "estas",
      "corregida": "estar",
      "tipo": "normalización",
      "confianza": 100 con Corrección

```
❌ "ola yo traajo en gogle"
✅ "hola yo trabajar en google"
→ HOLA → YO → TRABAJAR → DELETREAR → G → O → O → G → L → E

❌ "tengo 15 aÑos"
✅ "tener 10 5 año"
→ TENER → 10 → 5 → AÑO

❌ "mi maedtra es vuena"
✅ "mio maestro mujer bueno"
→ MIO → MAESTRO → MUJER → (omite "es") → DELETREAR → B → U → E → N → O

❌ "mañna voi a estuiar"
✅ "mañana estudiar"
→ MAÑANA → ESTUDIAR

❌ "cmo ests?"
✅ "como estar"
→ COMO → ESTAR
```

## 🎯 Niveles de Confianza

La corrección ortográfica tiene diferentes niveles:

- **100%**: Normalización exacta (mi→mio, trabajo→trabajar)
- **70%**: 1 carácter de diferencia (ola→hola, cmo→como)
- **40%**: 2 caracteres de diferencia (traajo→trabajar, estuido→estudio)

Si la distancia es mayor a 2 caracteres, la palabra se deletrea.
  "texto_original": "mi hermana trabaja en la universidad",
  "animaciones": [
    {"nombre": "mio", "categoria": "pronombres", "archivo": "mio"},
    {"nombre": "hermano", "categoria": "familia", "archivo": "hermano"},
    {"nombre": "mujer", "categoria": "personas", "archivo": "mujer"},
    {"nombre": "universidad", "categoria": "lugares", "archivo": "universidad"},
    {"nombre": "trabajar", "categoria": "verbos", "archivo": "trabajar"}
  ],
  "total_animaciones": 5,
  "palabras_deletreadas": []
}
```

## 📝 Ejemplos de Traducción

```
"yo trabajo en google"
→ YO → TRABAJAR → DELETREAR → G → O → O → G → L → E

"tengo 15 años"
→ TENER → 10 → 5 → AÑO

"mi maestra es buena"
→ MIO → MAESTRO → MUJER → (omite "es") → DELETREAR → B → U → E → N → A

"mañana voy a estudiar"
→ MAÑANA → (omite "voy") → (omite "a") → ESTUDIAR

"¿cómo estás?"
→ COMO → ESTAR (signos de interrogación omitidos)
```

## 🔧 Actualizar Diccionario

Para agregar más palabras al diccionario:
**Corrección ortográfica automática** (distancia de Levenshtein)
- ✅ Normalización completa de verbos (140+ conjugaciones)
- ✅ Manejo de género femenino
- ✅ Reordenamiento según estructura LSV
- ✅ Omisión de palabras innecesarias
- ✅ Deletreo automático de palabras desconocidas
- ✅ Manejo correcto de números
- ✅ Limpieza automática de signos de puntuación
- ✅ **Retorna texto original Y corregido**
- ✅ **Lista detallada de correcciones con niveles de confianza**
## 📦 Dependencias

```bash
pip install fastapi uvicorn pydantic
```

## ✨ Características

- ✅ Normalización completa de verbos (140+ conjugaciones)
- ✅ Manejo de género femenino
- ✅ Reordenamiento según estructura LSV
- ✅ Omisión de palabras innecesarias
- ✅ Deletreo automático de palabras desconocidas
- ✅ Manejo correcto de números
- ✅ Limpieza automática de signos de puntuación
