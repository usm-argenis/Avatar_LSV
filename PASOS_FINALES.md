# 🎯 Pasos Finales - Configuración de Modelos GLB

## ✅ Estado Actual

La subida de archivos GLB a GitHub Releases está en progreso:
- **Release**: https://github.com/usm-argenis/Avatar_LSV/releases/tag/models-v1
- **Progreso**: Monitoreando en tiempo real
- **Avatares**: Duvall y Carla (~558 archivos)

---

## 📋 Cuando termine la subida (20-30 min):

### 1️⃣ Verificar subida completa
```powershell
gh release view models-v1 --repo usm-argenis/Avatar_LSV --json assets --jq '.assets | length'
# Debe mostrar ~558
```

### 2️⃣ Crear tabla en PostgreSQL
Abre **pgAdmin** o la terminal de PostgreSQL y ejecuta:
```sql
-- Conectarse a la base de datos
\c VeneSeñas

-- Ejecutar script
\i C:/Users/andre/OneDrive/Documentos/tesis/database/create_glb_models_table.sql
```

O desde PowerShell (si tienes psql en PATH):
```powershell
& "C:\Program Files\PostgreSQL\[VERSION]\bin\psql.exe" -U postgres -d "VeneSeñas" -f "database\create_glb_models_table.sql"
```

### 3️⃣ Generar e insertar URLs
Ejecuta el script que genera las URLs con base en los archivos subidos:
```powershell
node generate-db-inserts.js
```

Esto creará `database/insert_final.sql` con todas las URLs de GitHub Releases.

Luego ejecuta el SQL:
```powershell
& "C:\Program Files\PostgreSQL\[VERSION]\bin\psql.exe" -U postgres -d "VeneSeñas" -f "database\insert_final.sql"
```

### 4️⃣ Crear endpoint API en el backend
Ya tienes el backend de Node.js en `rn-postgres-example/backend/server.js`

Agrega este endpoint:
```javascript
// Obtener URL de modelo GLB
app.get('/api/models/:avatar/:palabra', async (req, res) => {
  try {
    const { avatar, palabra } = req.params;
    
    const result = await pool.query(
      'SELECT * FROM buscar_modelo($1, $2)',
      [avatar, palabra]
    );
    
    if (result.rows.length > 0) {
      res.json({
        success: true,
        modelo: result.rows[0]
      });
    } else {
      res.status(404).json({
        success: false,
        mensaje: 'Modelo no encontrado'
      });
    }
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});
```

### 5️⃣ Actualizar frontend (GitHub Pages)
Modificar los archivos HTML para obtener URLs de la API:

```javascript
async function obtenerUrlModelo(avatar, palabra) {
    try {
        const response = await fetch(
            `https://tu-backend.com/api/models/${avatar}/${palabra}`
        );
        const data = await response.json();
        return data.modelo.url_github;
    } catch (error) {
        console.error('Error obteniendo modelo:', error);
        return null;
    }
}
```

### 6️⃣ Probar
```javascript
// En la consola del navegador:
const url = await obtenerUrlModelo('Duvall', 'hola');
console.log(url);
// https://github.com/usm-argenis/Avatar_LSV/releases/download/models-v1/...
```

---

## 🔍 Monitorear Progreso Actual

```powershell
# Ver últimas líneas del log
Get-Content upload-log.txt -Tail 20 -Wait

# Ver cantidad de archivos subidos
gh release view models-v1 --repo usm-argenis/Avatar_LSV --json assets --jq '.assets | length'
```

---

## ⏰ Tiempo Estimado

- ⏳ **Subida actual**: ~20-30 minutos
- ⚡ **Configuración DB**: ~5 minutos
- ⚡ **Endpoint API**: ~10 minutos
- ⚡ **Actualizar frontend**: ~15 minutos

**Total**: ~1 hora desde ahora

---

## 🎉 Resultado Final

Tu GitHub Pages podrá cargar modelos GLB desde:
- ✅ GitHub Releases (gratis, ilimitado)
- ✅ PostgreSQL (metadata y búsqueda)
- ✅ API backend (URLs dinámicas)
- ✅ CDN de GitHub (rápido globalmente)

Sin costos adicionales y todos los modelos disponibles! 🚀
