var nombreCache = 'login-v1';

self.addEventListener("install", function(event){
    console.log("Instalado");
    event.waitUntil(
        caches.open(nombreCache)
        .then(function(cacheEncontrada){
            return cacheEncontrada.addAll([
                '/'
            ]);
        })
    );
});

self.addEventListener('fetch', function(event){
    const peticionURL = new URL(event.request.url);
    if((peticionURL.origin === location.origin)){
        console.log(peticionURL.pathname)
        if(peticionURL.pathname === '/'){
            event.respondWith(caches.match('/'))
            return;
        }
    }
    event.respondWith(
        caches.match(event.request)
        .then(function(respuesta){
            return respuesta || fetch(event.request)
        })
    )
})