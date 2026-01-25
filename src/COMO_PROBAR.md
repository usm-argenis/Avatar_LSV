# 🚀 GUÍA RÁPIDA - Cómo Probar el Sistema

## ✅ El Sistema YA ESTÁ FUNCIONANDO

Las pruebas automáticas se ejecutaron exitosamente y generaron:
- ✅ `output_hola.json` (4 frames)
- ✅ `output_gracias.json` (4 frames)
- ✅ `output_hola_gracias.json` (18 frames con interpolación)

---

## 🎮 3 Formas de Probar

### 1️⃣ FORMA MÁS FÁCIL - Menú Interactivo

Haz doble clic en:
```
📁 probar_sistema.bat
```

Te mostrará un menú con opciones:
1. Prueba automática
2. Modo interactivo
3. Ver archivos generados

### 2️⃣ Modo Automático desde Terminal

```powershell
cd c:\Users\andre\OneDrive\Documentos\tesis\src
python main.py
```

Esto ejecuta 3 pruebas:
- ✅ "hola" → genera `output_hola.json`
- ✅ "gracias" → genera `output_gracias.json`
- ✅ "hola gracias" → genera `output_hola_gracias.json` (con interpolación)

### 3️⃣ Modo Interactivo - Prueba Tu Propio Texto

```powershell
cd c:\Users\andre\OneDrive\Documentos\tesis\src
python main.py --mode interactive
```

Luego escribe cualquier texto:
```
📝 Ingresa texto: hola buenos dias
📝 Ingresa texto: gracias mama
📝 Ingresa texto: salir
```

---

## 📊 Qué Puedes Probar

### ✅ Palabras que Funcionan (39 en total)

**Saludos:**
- hola, buenos, dias, tardes, noches, adios

**Cortesía:**
- gracias, favor, por, perdon, disculpa

**Pronombres:**
- yo, tu, el, ella, nosotros, ustedes

**Familia:**
- mama, papa, hermano, hermana, hijo, hija, abuelo, abuela

**Verbos:**
- ir, venir, hacer, ver, comer, beber, dormir, trabajar

**Números:**
- cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez

### 🎯 Ejemplos de Prueba

```
hola                    → 1 seña
gracias                 → 1 seña
hola gracias            → 2 señas + interpolación
buenos dias             → 2 señas
yo ir a casa            → 4 señas (deletrea "a" y "casa")
mama y papa             → 3 señas (deletrea "y")
uno dos tres            → 3 señas
```

---

## 📁 Ver los Resultados

### Opción 1: Explorador de Windows
```
1. Abre el explorador
2. Navega a: c:\Users\andre\OneDrive\Documentos\tesis\src
3. Busca archivos .json (output_*.json)
```

### Opción 2: Desde PowerShell
```powershell
cd c:\Users\andre\OneDrive\Documentos\tesis\src
dir *.json
```

### Opción 3: Abrir con VS Code
```powershell
code output_hola_gracias.json
```

---

## 🔍 Entender los Archivos JSON

Cada archivo contiene:

```json
{
  "frames": [              // Array de frames
    {
      "frame": 0,          // Número de frame
      "time": 0.0,         // Tiempo en segundos
      "sign": "hola",      // Nombre de la seña
      "keypoints": {
        "pose": {
          "right_hand": {  // Posición de la mano
            "x": 0.5,
            "y": 1.2,
            "z": 0.3,
            "rotation_x": 0,
            "rotation_y": 0,
            "rotation_z": 0
          },
          "right_arm": {   // Ángulos del brazo
            "elbow_angle": 90,
            "shoulder_angle": 45
          },
          "head": {        // Rotación de cabeza
            "rotation_x": 0,
            "rotation_y": 0,
            "rotation_z": 0
          }
        }
      }
    }
  ],
  "duration": 0.13,        // Duración total
  "fps": 30                // Frames por segundo
}
```

---

## 🎯 Prueba Paso a Paso

### Paso 1: Ejecuta la prueba automática
```powershell
cd src
python main.py
```

**Resultado esperado:**
```
✅ ÉXITO: Animación generada para 'hola'
✅ ÉXITO: Animación generada para 'gracias'
✅ ÉXITO: Animación generada para 'hola gracias'
```

### Paso 2: Verifica los archivos
```powershell
dir *.json
```

**Deberías ver:**
```
output_hola.json
output_gracias.json
output_hola_gracias.json
```

### Paso 3: Abre uno de los archivos
```powershell
code output_hola_gracias.json
```

**Deberías ver:**
- 18 frames en total
- Primera seña: "hola" (4 frames)
- Transición: "hola_to_gracias" (10 frames)
- Segunda seña: "gracias" (4 frames)

---

## 🔧 Solución de Problemas

### ❌ Error: "No module named 'numpy'"
```powershell
pip install numpy scipy pandas matplotlib tqdm
```

### ❌ Error: "Seña no encontrada"
- El sistema usa coincidencia difusa
- Si una palabra no existe, la deletreará letra por letra
- Esto es normal para palabras no en el diccionario

### ❌ Error: "UnicodeEncodeError"
- Usa `probar_sistema.bat` en vez de `demo.py`
- O ejecuta: `python main.py` en vez de `python demo.py`

---

## 📈 Próximos Pasos

Una vez que hayas probado el sistema:

1. **Agregar más señas:** Crea archivos JSON en `data/keypoints/`
2. **Integrar con app móvil:** Llamar API desde React Native
3. **Exportar a GLB:** Instalar pygltflib para archivos 3D
4. **Visualizar en navegador:** Crear renderizador Three.js

---

## 🎓 Resumen

| Comando | Qué hace |
|---------|----------|
| `python main.py` | Prueba automática (3 ejemplos) |
| `python main.py --mode interactive` | Modo interactivo (escribe texto) |
| `probar_sistema.bat` | Menú con todas las opciones |
| `dir *.json` | Ver archivos generados |
| `code output_hola.json` | Abrir archivo en VS Code |

---

**¡El sistema está 100% funcional y listo para usar!** 🚀
