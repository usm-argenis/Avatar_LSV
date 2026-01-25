# Test API - Instrucciones rápidas

Resumen y pasos para dejar funcionando los dos archivos de prueba:

- `test/test_api.html`
- `test/test_vocabulario_expandido.html`

---

## Hallazgos rápidos

- El backend que expone los endpoints útiles está en `backend/api_optimizer.py` (Flask) y sirve las rutas:
  - `POST /api/optimizar`  (port 5000 por defecto)
  - `GET  /api/senas-disponibles`
  - `POST /api/corregir`, `POST /api/convertir-lsv`, `GET /api/buscar-sena`, `GET /api/health`

- Existe también `backend/main.py` (FastAPI) que escucha por `port 8000` pero actualmente solo tiene una ruta raíz (`GET /`) y NO implementa los endpoints de optimización. Por eso algunos HTML usan 8000 y otros 5000: hay una inconsistencia histórica.

- El motor de palabras/señas está en `backend/lsv_optimizer.py`. Al iniciar `api_optimizer.py` se instancia `LSVTextOptimizer()` que carga internamente:
  - El vocabulario `SENAS_CURSO_BASICO` (lista dentro de `lsv_optimizer.py`).
  - Posibles animaciones desde `animations_library/` si existen.

Por lo tanto, NO hace falta un "main" adicional con las palabras: al ejecutar `backend/api_optimizer.py` el optimizador carga las palabras internas automáticamente.

---

## ¿Cuándo funcionaban los HTML?

- Ambos HTML funcionaron correctamente cuando el servicio que provee `/api/optimizar` estaba corriendo.
  - Si ejecutabas `python backend/api_optimizer.py` (Flask) el servicio escucha en `http://localhost:5000` y ambos archivos funcionan si apuntan a `http://localhost:5000`.
  - `test_vocabulario_expandido.html` ya apunta a `http://localhost:5000/api/optimizar` (correcto).
  - `test_api.html` actualmente apunta a `http://localhost:8000/api/optimizar` (posible causa de error) y además su mensaje de error sugiere `http://localhost:5000` — hay una mezcla de puertos.

---

## Recomendación rápida (la forma más sencilla)

1) Activar el entorno virtual (PowerShell):

```powershell
& .\.venv\Scripts\Activate.ps1
```

2) Instalar dependencias del backend (si no están):

```powershell
pip install -r backend/requirements.txt
```

3) Ejecutar el servidor Flask (este archivo ya inicia la app en puerto 5000):

```powershell
python backend\api_optimizer.py
```

4) Abrir los archivos de prueba en un navegador:

- `test/test_vocabulario_expandido.html` — ya usa `http://localhost:5000`.
- `test/test_api.html` — editar la URL para que apunte a `http://localhost:5000/api/optimizar` (o ejecutar una versión del backend en el puerto 8000; ver alternativas abajo).

Ejemplo de cambio rápido (buscar y reemplazar la URL dentro del HTML):

```html
// en test/test_api.html
- fetch('http://localhost:8000/api/optimizar', {
+ fetch('http://localhost:5000/api/optimizar', {
```

---

## Alternativas y notas técnicas

- Opción A — Ejecutar Flask (recomendada si quieres usar las rutas tal como están):
  - Ventaja: `api_optimizer.py` ya implementa toda la lógica y carga el vocabulario.

- Opción B — Reimplementar/registrar los endpoints en `backend/main.py` (FastAPI) y ejecutar con Uvicorn en el puerto 8000:
  - Comando para arrancar (tras implementar las rutas):

```powershell
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

  - Consideración: ahora `main.py` solo tiene `GET /`. Si quieres que los HTML funcionen en 8000, debes mover o duplicar las rutas de `api_optimizer.py` a `main.py` o crear un adaptador que las importe.

- Opción C — Dejar ambos servidores, pero ajustar los HTML a 5000 o 8000 según corresponda.

---

## Verificaciones y debugging

- Health check: después de arrancar Flask revisa `http://localhost:5000/api/health`.
- Para comprobar las señas cargadas: `GET http://localhost:5000/api/senas-disponibles`.
- Si alguna petición falla desde el HTML, abre la consola del navegador y mira el error (CORS está habilitado en `api_optimizer.py`, por eso frontend debería poder acceder).

---

## ¿Qué puedo hacer por ti ahora?

- Puedo editar `test/test_api.html` ahora para cambiar `8000` → `5000` y dejarlo funcionando inmediatamente.
- O puedo integrar los endpoints de `api_optimizer.py` en `backend/main.py` (FastAPI) si prefieres usar `uvicorn`/8000 y mantener ese puerto.
- También puedo ejecutar una prueba local (si me das permiso para ejecutar comandos) y confirmar que `test/test_api.html` responde.

Dime cuál opción prefieres y la implemento.
