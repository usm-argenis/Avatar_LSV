# REPORTE: Palabras sin Archivos GLB

**Fecha:** 2026-02-06  
**Total palabras en data.json:** 445  
**✅ Palabras CON archivo GLB:** 369 (82.9%)  
**❌ Palabras SIN archivo GLB:** 76 (17.1%)

---

## ❌ Categorías SIN Carpeta Física (4 palabras)

### 1. EDUCACION (1 palabra)
- objetivo

### 2. SUSTANTIVOS (1 palabra)
- proyecto

### 3. TECNOLOGIA (2 palabras)
- computadora, computadoras

---

## ⚠️ Palabras Faltantes en Categorías CON Carpeta (72 palabras)

### 1. FAMILIA (1 palabra - carpeta: nuevo)
- cuñado (problema de codificación)

### 2. GENERAL (27 palabras - carpetas: horario, nuevo)
- aporte, comunidad, defensa, edad, en punto, especial, esta, este
- grado, hora, horario, importante, integracion, junto, jurado, lengua
- lsv, media hora, miembro, miembros, presentacion, senas, señas
- social, tecnologia, tecnologico, teg, trabajo, traduccion
- un cuarto, un minuto, un segundo, una hora, venezolano

### 3. LUGARES (2 palabras - carpeta: adverbios lugares)
- universidad, venezuela

### 4. EXPRESIONES (1 palabra - carpeta: expresiones)
- mejor

### 5. INTERROGANTES (1 palabra - carpeta: preguntas)
- cual es tu sena

### 6. TIEMPO (3 palabras - carpetas: tiempo, nuevo)
- año, años, hace rato

### 7. VERBOS (37 palabras - carpetas: verbos, nuevo)
- busca, buscamos, buscan, buscar, buscas
- comunicacion, crear, enganar, entender, entiende
- entiendes, entiendo, evaluar, existir, facilita
- facilitamos, facilitan, facilitar, facilitas, facilite
- integrar, ir, llamar, llamo, mejora
- mejorar, participar, tener, tengo, tiene
- tienes, traducir, va, vamos, van
- vas, voy

---

## ✅ Carpetas Físicas Disponibles

Carpetas existentes en `test/output/glb/Duvall/`:
- adverbios lugares ✓
- alfabeto ✓
- cortesia ✓
- dias_semana ✓
- estado civil ✓
- expresiones ✓
- horario ✓
- medios transporte ✓
- **nuevo ✓✓✓** (familia completa + algunos verbos/tiempo/general)
- numero ✓
- numeros ordinales ✓
- personas ✓
- preguntas ✓
- preposicion ✓
- profesion ✓
- pronombres ✓
- saludos ✓
- tiempo ✓
- tipos de vivienda ✓
- verbos ✓

---

## 📊 Resumen

**MAPEO_CATEGORIAS actualizado:**
- ✅ 19 categorías CON carpeta física y archivos GLB
- ❌ 3 categorías SIN carpeta física (educacion, sustantivos, tecnologia)
- 🔄 Categorías con archivos en MÚLTIPLES carpetas:
  - **familia** → nuevo (15/16 palabras)
  - **verbos** → verbos + nuevo (47/84 palabras)
  - **tiempo** → tiempo + nuevo (14/17 palabras)
  - **general** → horario + nuevo (10/37 palabras)

**Estado del diccionario:**
- ✅ 369 palabras (82.9%) tienen archivo GLB y funcionan correctamente
- ⚠️ 72 palabras (16.2%) en categorías con carpeta pero faltan GLB específicos
- ❌ 4 palabras (0.9%) en categorías sin carpeta física

**Mejora con carpeta "nuevo":**
- Antes: 331 palabras (74.4%) con GLB
- Ahora: 369 palabras (82.9%) con GLB
- **+38 palabras recuperadas (+8.5%)**

---

## 🎯 Recomendación

### PRIORIDAD 1: Generar GLB para palabras críticas de TEG (12 palabras)

**TEG (4):** defensa, presentacion, proyecto, objetivo  
**Tecnología (2):** computadora, computadoras  
**General (6):** importante, trabajo, lengua, lsv, edad, grado

### PRIORIDAD 2: Verbos faltantes comunes (15 palabras)

buscar, crear, entender, existir, ir, tener, mejorar, participar, traducir, llamar, evaluar, integrar, va, vas, voy

### PRIORIDAD 3: Completar categorías parciales

- **GENERAL:** 27 palabras faltantes (TEG/universidad)
- **VERBOS:** 37 palabras faltantes (conjugaciones)
- **TIEMPO:** 3 palabras (año, años, hace rato)

---

### OPCIÓN ALTERNATIVA: 

Eliminar las 76 palabras sin GLB del diccionario hasta que se generen las animaciones.
- Ventaja: Diccionario 100% funcional con 369 palabras
- Desventaja: Perder palabras importantes para TEG y familia
