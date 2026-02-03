# LSV Avatar - Lengua de Señas Venezolana

## 🎯 Descripción

Sistema de traducción de texto a Lengua de Señas Venezolana (LSV) con avatares 3D animados. El sistema incluye:

- ✅ **311 palabras** del diccionario LSV
- ✅ **18 categorías** (profesiones, tiempo, verbos, números, etc.)
- ✅ **Reglas lingüísticas LSV completas** (orden temporal, género, verbos infinitivos, omisión de artículos)
- ✅ **Corrección ortográfica** con variantes venezolanas
- ✅ **Deletreo automático** para palabras desconocidas
- ✅ **Avatares 3D** (Nancy, Nina, Argenis, Duvall)

## 🌐 GitHub Pages

Este proyecto funciona directamente en GitHub Pages **sin necesidad de backend**. Toda la lógica de traducción LSV está implementada en JavaScript.

### Versión GitHub Pages:
- **URL**: https://usm-argenis.github.io/Avatar_LSV/test/animation_mobile.html
- **Traductor**: Incluido en `lsv-translator.js` (standalone)
- **GLB Files**: Almacenados localmente (no en repositorio)

### Versión con Backend API:
- **URL Local**: http://localhost:5000
- **Backend**: FastAPI con Python (puerto 5000)
- **API Endpoints**: `/api/translate`, `/api/corregir`

## 📚 Diccionario LSV

El sistema incluye 311 palabras organizadas en 18 categorías:

| Categoría | Palabras | Ejemplos |
|-----------|----------|----------|
| Alfabeto | 26 | a, b, c, d, ... |
| Profesiones | 98 | ingeniero, médico, profesor, ... |
| Expresiones | 30 | hola, gracias, bien, mal, ... |
| Personas | 22 | hombre, mujer, niño, amigo, ... |
| Verbos | 20 | trabajar, estudiar, comer, vivir, ... |
| Tiempo | 18 | ayer, hoy, mañana, lunes, ... |
| Preposiciones | 15 | mucho, poco, todo, nada, ... |
| Pronombres | 12 | yo, tú, él, ella, nosotros, ... |
| Saludos | 12 | hola, adiós, buenos días, ... |
| Números | 12 | 0, 1, 2, 3, ... 10, 1M |
| Ordinales | 10 | primero, segundo, tercero, ... |
| Viviendas | 10 | casa, apartamento, sala, ... |
| Adverbios | 9 | cerca, lejos, derecha, ... |
| Cortesía | 7 | gracias, permiso, de nada, ... |
| Estado Civil | 6 | casado, soltero, divorciado, ... |
| Interrogantes | 4 | cómo estás, qué tal, ... |

## 🧠 Reglas Lingüísticas LSV

### 1. Orden Temporal
Las palabras de **TIEMPO** van al **inicio** de la frase:

```
"trabajo mañana" → MAÑANA TRABAJAR
"ayer estudié" → AYER ESTUDIAR
```

### 2. Sistema de Género
Las palabras **femeninas** se convierten a **masculino + MUJER**:

```
"ingeniera" → INGENIERO + MUJER
"doctora" → MÉDICO + MUJER
"profesora" → PROFESOR + MUJER
```

### 3. Verbos en Infinitivo
Todos los verbos se normalizan al **infinitivo**:

```
"trabajo" → TRABAJAR
"estudié" → ESTUDIAR
"como" → COMER
```

### 4. Omisión de Artículos
Se omiten: el, la, los, las, un, una, de, del, y, o

```
"el niño y la niña" → NIÑO NIÑA
"trabajo de ingeniero" → TRABAJAR INGENIERO
```

### 5. Plurales a Singular
Los plurales se convierten a singular con cuantificadores:

```
"muchos amigos" → MUCHO AMIGO
"todos los días" → TODO DÍA
```

### 6. Frases Compuestas
Algunas frases son **una sola seña**:

```
"buenos días" = 1 seña
"buenas tardes" = 1 seña
"muchas gracias" = 1 seña
"fin de semana" = 1 seña
```

## 🔧 Uso del Traductor

### En el navegador (GitHub Pages):

```javascript
// El traductor LSV_TRANSLATOR está disponible globalmente
const resultado = LSV_TRANSLATOR.translate("hola, ¿cómo estás?", {
    deletrearDesconocidas: true,
    velocidadDeletreo: 1.2
});

console.log(resultado.animaciones);
// [
//   { nombre: "hola", categoria: "saludos", archivo: "hola" },
//   { nombre: "comer", categoria: "verbos", archivo: "comer" },
//   { nombre: "estar", categoria: "verbos", archivo: "estar" }
// ]
```

### Con la API (Backend Python):

```bash
# Activar API (puerto 5000)
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 5000

# Traducir texto
curl -X POST http://localhost:5000/api/translate \
  -H "Content-Type: application/json" \
  -d '{
    "texto": "hola, ¿cómo estás?",
    "deletrear_desconocidas": true
  }'
```

## 📝 Ejemplos de Traducción

### Ejemplo 1: Saludo simple
```
Entrada: "hola, ¿cómo estás?"
Salida: HOLA COMER ESTAR
```

### Ejemplo 2: Género y tiempo
```
Entrada: "ayer la ingeniera trabajó"
Salida: AYER INGENIERO MUJER TRABAJAR
```

### Ejemplo 3: Omisión de artículos
```
Entrada: "el niño y la niña comen"
Salida: NIÑO NIÑA COMER
```

### Ejemplo 4: Frase compuesta
```
Entrada: "buenos días, muchas gracias"
Salida: BUENOS DÍAS MUCHAS GRACIAS
```

### Ejemplo 5: Deletreo
```
Entrada: "mi nombre es Pedro"
Salida: MÍO DELETREAR P-E-D-R-O
```

## 🛠️ Estructura del Proyecto

```
tesis/
├── backend/
│   ├── main.py                    # FastAPI server (puerto 5000)
│   ├── api_optimizer.py           # Motor LSV completo (627 líneas)
│   ├── actualizar_diccionario.py  # Auto-genera diccionario desde Duvall
│   ├── scripts/
│   │   └── data.json              # 311 palabras LSV
│   └── test_lsv_completo.py       # 23 tests LSV
├── test/
│   ├── animation_mobile.html      # Visor móvil (GitHub Pages)
│   ├── lsv-translator.js          # Traductor standalone (JavaScript)
│   └── output/glb/                # Archivos GLB de animaciones
│       ├── Duvall/
│       ├── Nancy/
│       ├── Nina/
│       └── Argenis/
└── SISTEMA_LSV_COMPLETO.md        # Documentación completa
```

## ⚙️ Configuración

### Modo GitHub Pages (actual)
```javascript
// en animation_mobile.html
let useBackendAPI = false;  // Usar traductor local
```

### Modo Backend API
```javascript
// en animation_mobile.html
let useBackendAPI = true;   // Usar API Python
const BACKEND_URL = 'http://localhost:5000';
```

## 🧪 Tests

El sistema incluye 39 tests automatizados:

- **23 tests LSV**: Reglas lingüísticas completas
- **16 tests puntuación**: Limpieza de signos (.,¿?¡!;:)

```bash
# Ejecutar tests LSV
cd backend
python test_lsv_completo.py

# Ejecutar tests de puntuación
python test_signos_puntuacion.py
```

## 📊 Estadísticas

- **Diccionario**: 311 palabras (253 base + 58 expansiones)
- **Categorías**: 18 categorías temáticas
- **Avatares**: 4 avatares 3D (Nancy, Nina, Argenis, Duvall)
- **Animaciones GLB**: 280+ archivos (.glb)
- **Precisión**: 100% en palabras del diccionario
- **Corrección**: Levenshtein distance max 2, confianza min 50%

## 🚀 Despliegue

### GitHub Pages (Automático)
```bash
# Hacer push a main
git add .
git commit -m "feat: Actualizar sistema LSV"
git push origin main

# GitHub Pages se actualiza automáticamente en 2-3 minutos
# URL: https://usm-argenis.github.io/Avatar_LSV/test/animation_mobile.html
```

### API Backend (Manual)
```bash
# Instalar dependencias
cd backend
pip install -r requirements.txt

# Ejecutar servidor
python -m uvicorn main:app --host 0.0.0.0 --port 5000

# API disponible en http://localhost:5000
# Docs en http://localhost:5000/docs
```

## 📖 Documentación Completa

- [SISTEMA_LSV_COMPLETO.md](SISTEMA_LSV_COMPLETO.md) - Reglas y diccionario completo
- [OPTIMIZACION_SIGNOS.md](backend/OPTIMIZACION_SIGNOS.md) - Sistema de puntuación
- [HAND_QUATERNION_DOCS.md](HAND_QUATERNION_DOCS.md) - Animaciones de manos
- [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md) - Configuración GitHub Pages

## 👥 Créditos

- **Desarrollador**: Argenis Useche
- **Universidad**: Universidad Santa María (USM)
- **Proyecto**: Tesis - Sistema LSV con Avatares 3D
- **Año**: 2024

## 📄 Licencia

Este proyecto es parte de una tesis universitaria.
