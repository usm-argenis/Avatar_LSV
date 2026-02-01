# Instrucciones para Limpiar Caché y Verificar Versión

## Problema
Expo puede cachear versiones antiguas del código, causando que los cambios no se reflejen inmediatamente.

## Solución 1: Limpiar Caché de Expo (RECOMENDADO)

1. **Detener el servidor de Expo** (Ctrl+C en la terminal donde corre `npx expo start`)

2. **Ejecutar comando de limpieza:**
```bash
cd mobile_app/lengua-de-senas
npx expo start -c
```

El flag `-c` limpia la caché antes de iniciar.

## Solución 2: Limpieza Manual Completa

```bash
cd mobile_app/lengua-de-senas

# Limpiar caché de Metro
npx react-native start --reset-cache

# O limpiar TODO
rm -rf node_modules
rm -rf .expo
npm install
npx expo start -c
```

## Solución 3: Reiniciar App en el Dispositivo

1. En la app de Expo Go, **sacudir el dispositivo** para abrir el menú de desarrollo
2. Seleccionar **"Reload"** o **"Refresh"**
3. Si no funciona, cerrar completamente la app de Expo Go y volver a abrirla

## Verificar que Estás Usando la Versión Correcta

Abre la consola de desarrollo (sacude el dispositivo → "Toggle Developer Menu" → "Debug Remote JS") y busca:

```
🚀 Avatar Spelling v2.1 - Iniciando...
```

Si ves esto, estás usando la versión actualizada.

## Logs para Diagnosticar el Problema

Cuando juegues, deberías ver estos logs en la consola:

### React Native (cuando envía la palabra):
```
📤 Enviando a HTML: palabra="casa", speed=2.5s, level=2
```

### HTML (cuando recibe la palabra):
```
📩 Mensaje recibido desde React Native: {type: "startNewWord", word: "casa", speed: 2.5, level: 2}
🎯 Configurado: palabra="casa", speed=2.5s, level=2
🔡 Deletreando: "casa" (4 letras) - Velocidad: 2.5s - Nivel: 2
```

### Para cada letra:
```
⚡ Instantánea desde caché: c - Velocidad: 2.5s
🎬 Reproduciendo animación: duración objetivo=2.5s, duración original=1.50s
✅ Letra 1/4 completada: c (velocidad usada: 2.5s)
```

Si ves velocidades diferentes o valores incorrectos, significa que hay caché.

## Verificar Nivel 2 - Palabras

Todas las palabras del Nivel 2 tienen **exactamente 4 letras**:
- casa, mesa, hola, luna, agua
- vida, amor, todo, nada, gato
- rosa, cafe, pelo, mano, pies
- ojos, boca, cara, ropa, sopa

Si ves una palabra de 3 letras en nivel 2, **definitivamente es caché antiguo**.

## Último Recurso: Desinstalar y Reinstalar

Si nada funciona:
1. Desinstala Expo Go del dispositivo
2. Reinstala Expo Go desde la tienda
3. Vuelve a escanear el QR code

---

**Fecha de última actualización del código: 2026-01-26**
**Versión HTML: v2.1**
