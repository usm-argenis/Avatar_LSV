// Service Worker para cache persistente de modelos 3D
// Versión: 1.0.0

const CACHE_NAME = 'lsv-models-v1';
const MODEL_CACHE_NAME = 'lsv-glb-models-v1';

// Archivos estáticos a cachear
const STATIC_ASSETS = [
  '/test/prueba.html',
  '/test/index.html'
];

// Instalar Service Worker
self.addEventListener('install', (event) => {
  console.log('🔧 Service Worker instalando...');
  
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('✅ Cache abierto');
      return cache.addAll(STATIC_ASSETS);
    }).catch(err => {
      console.error('❌ Error en instalación:', err);
    })
  );
  
  // Activar inmediatamente
  self.skipWaiting();
});

// Activar Service Worker
self.addEventListener('activate', (event) => {
  console.log('✅ Service Worker activado');
  
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          // Eliminar caches antiguas
          if (cacheName !== CACHE_NAME && cacheName !== MODEL_CACHE_NAME) {
            console.log('🗑️ Eliminando cache antigua:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  
  return self.clients.claim();
});

// Interceptar peticiones
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  
  // Solo cachear archivos GLB (modelos 3D)
  if (url.pathname.endsWith('.glb')) {
    event.respondWith(
      caches.open(MODEL_CACHE_NAME).then((cache) => {
        // Intentar obtener del cache primero
        return cache.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            console.log('⚡ Modelo desde cache:', url.pathname);
            return cachedResponse;
          }
          
          // Si no está en cache, descargarlo y guardarlo
          console.log('📥 Descargando modelo:', url.pathname);
          return fetch(event.request).then((networkResponse) => {
            // Clonar la respuesta porque solo se puede usar una vez
            const responseToCache = networkResponse.clone();
            
            cache.put(event.request, responseToCache).then(() => {
              console.log('💾 Modelo guardado en cache:', url.pathname);
            });
            
            return networkResponse;
          }).catch((error) => {
            console.error('❌ Error descargando modelo:', error);
            throw error;
          });
        });
      })
    );
  } else {
    // Para otros recursos, estrategia network-first
    event.respondWith(
      fetch(event.request).catch(() => {
        return caches.match(event.request);
      })
    );
  }
});

// Mensajes desde la página
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'CLEAR_CACHE') {
    console.log('🗑️ Limpiando cache de modelos...');
    event.waitUntil(
      caches.delete(MODEL_CACHE_NAME).then(() => {
        console.log('✅ Cache de modelos limpiado');
        event.ports[0].postMessage({ success: true });
      })
    );
  }
  
  if (event.data && event.data.type === 'GET_CACHE_SIZE') {
    console.log('📊 Calculando tamaño del cache...');
    event.waitUntil(
      caches.open(MODEL_CACHE_NAME).then((cache) => {
        return cache.keys().then((keys) => {
          console.log(`📦 Modelos en cache: ${keys.length}`);
          event.ports[0].postMessage({ 
            count: keys.length,
            models: keys.map(req => new URL(req.url).pathname)
          });
        });
      })
    );
  }
});
