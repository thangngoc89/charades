const CACHE_NAME = 'headsup-v7';
const ASSETS = [
  './',
  './index.html',
  './style.css',
  './app.js',
  './decks.js',
  './manifest.json'
];

// Install: immediately take over and pre-cache latest assets from network
self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return Promise.all(
        ASSETS.map((url) => {
          // Force network bypass during pre-cache
          return fetch(new Request(url, { cache: 'reload' }))
            .then((res) => {
              if (res.ok) return cache.put(url, res);
            })
            .catch((err) => {
              console.warn('Pre-cache error for:', url, err);
            });
        })
      );
    })
  );
});

// Activate: delete all old caches immediately
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('Deleting outdated cache:', key);
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch: Network-First strategy
// Always fetch fresh version from server when online; fallback to cache if offline
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  event.respondWith(
    fetch(event.request)
      .then((networkResponse) => {
        // If response is valid, update the cache with fresh version
        if (networkResponse && networkResponse.status === 200) {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      })
      .catch(() => {
        // Network failed (offline), try cache
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) {
            return cachedResponse;
          }
          if (event.request.mode === 'navigate') {
            return caches.match('./index.html') || caches.match('./');
          }
        });
      })
  );
});
