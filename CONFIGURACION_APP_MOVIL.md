# 📱 CONFIGURACIÓN APP MÓVIL - Conexión Backend

## ✅ PROBLEMAS RESUELTOS

### 1. ❌ Endpoint /api/optimizar no existía
**Síntoma:** App móvil no funcionaba, mostraba errores de red
**Causa:** La app llamaba a `/api/optimizar` pero el backend solo tenía `/api/translate`
**Solución:** ✅ Se creó el endpoint `/api/optimizar` en el backend

### 2. ❌ Acentos no se detectaban
**Síntoma:** Palabras con acentos (días, médico, etc.) no se reconocían
**Causa:** La normalización eliminaba TODO lo no-ASCII, incluyendo la ñ
**Solución:** ✅ Nueva función `normalizar_texto_espanol()` que:
- Quita acentos: á→a, é→e, í→i, ó→o, ú→u
- MANTIENE la ñ: mañana→mañana, niño→niño

### 3. ❌ "nombre" se corregía a "hombre"
**Síntoma:** "mi nombre es X" → "mi hombre es X"
**Causa:** Algoritmo de corrección ortográfica con distancia Levenshtein
**Solución:** ✅ Se agregó "nombre" a palabras omitidas (LSV estándar)

---

## 🔍 Diagnóstico
La app móvil está configurada para usar la IP: `192.168.10.93:5000`
Tu IP actual es: **192.168.10.93** ✅ (IP correcta)

Para que funcione en tu teléfono, necesitas:
1. ✅ Backend corriendo en tu PC
2. ✅ Teléfono y PC en la MISMA red WiFi
3. ✅ IP correcta de tu PC en el código (ya está bien configurada)

---

## 🚀 SOLUCIÓN PASO A PASO

### 1️⃣ Verificar tu IP (opcional)

**En Windows (PowerShell):**
```powershell
ipconfig | Select-String 'IPv4'
```

Deberías ver: `192.168.10.93`

---

### 2️⃣ Iniciar el backend

En PowerShell:
```powershell
cd backend
python main.py
```

Deberías ver:
```
🚀 Iniciando LSV Translator API...
📡 Servidor corriendo en http://localhost:5000
📚 Documentación en http://localhost:5000/docs
```

**IMPORTANTE:** Deja este terminal abierto mientras usas la app.

---

### 3️⃣ Probar el endpoint /api/optimizar

Ejecuta el test:
```powershell
python test_endpoint_optimizar.py
```

Deberías ver:
```
✅ RESPUESTA EXITOSA:
  • Texto original: buenos días mi nombre es argenis
  • Texto corregido: buenos dias mio argenis
  • Cobertura: XX%
```

---

### 4️⃣ Reiniciar la app móvil

Si la app ya estaba corriendo:
1. Ciérrala completamente en el teléfono
2. Presiona `r` en el terminal de Expo para recargar
3. O escanea de nuevo el QR

---

## 🧪 VERIFICAR CONEXIÓN

### Desde tu navegador en el teléfono:
Abre el navegador y ve a:
```
http://192.168.10.93:5000
```

Si ves el mensaje JSON:
```json
{
  "message": "LSV Translator API funcionando! 🚀",
  "version": "2.0.0",
  "endpoints": {
    "translate": "/api/translate",
    "optimizar": "/api/optimizar",
    "corregir": "/api/corregir"
  }
}
```

✅ **La conexión funciona correctamente**

---

## 🔧 PROBLEMAS COMUNES

### ❌ "Network request failed"
- Verifica que el backend esté corriendo
- Asegúrate de que teléfono y PC están en la misma WiFi
- Verifica que la IP es correcta (192.168.10.93)

### ❌ Firewall bloqueando
Windows puede bloquear el puerto 5000. Si esto pasa:
1. Abre "Firewall de Windows Defender"
2. "Permitir una aplicación..."
3. Busca Python y habilita redes privadas

### ❌ "Connection timeout"
- Desactiva temporalmente el firewall para probar
- Verifica que no hay VPN activa
- Prueba con otra red WiFi

---

## 📝 RESUMEN DE CAMBIOS REALIZADOS

### ✅ Backend (api_optimizer.py)
1. **Nueva función normalizar_texto_espanol()**: Quita acentos pero mantiene ñ
2. **Agregada "nombre" a palabras omitidas**: Para evitar corrección incorrecta
3. **Aumentado umbral de corrección**: De 50% a 80% de confianza
4. **Verificación de frases compuestas**: No corrige palabras parte de frases

### ✅ Backend (main.py)
1. **Nuevo endpoint /api/optimizar**: Para compatibilidad con app móvil
2. **Retorna información completa**: texto_lsv, cobertura, palabras disponibles/faltantes

### ✅ Tests validados
- ✅ "buenos días" → BUENOS DIAS (1 animación)
- ✅ "mañana" → MAÑANA (mantiene ñ)
- ✅ "niño" → NIÑO (mantiene ñ)
- ✅ "mi nombre es X" → MIO + deletreado de X
- ✅ "cual es tu nombre" → CUAL ES TU NOMBRE (frase completa)

---

## 🎯 COMANDOS RÁPIDOS

### Iniciar backend:
```powershell
cd backend
python main.py
```

### Probar endpoint:
```powershell
cd backend
python test_endpoint_optimizar.py
```

### Ver tu IP WiFi:
```powershell
ipconfig | Select-String 'IPv4'
```

---

## 📞 SI AÚN HAY PROBLEMAS

1. Reinicia el backend (Ctrl+C y ejecuta de nuevo `python main.py`)
2. Revisa el terminal del backend para ver errores
3. Verifica que el test `python test_endpoint_optimizar.py` funcione
4. Asegúrate de que el teléfono esté en WiFi (no datos móviles)

