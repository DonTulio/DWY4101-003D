(function (d, w) {
    // verificar si el navegador esta listo para los cambios del DOM
    const token = "12d889927a2ab0508477527474cd4699";
    d.onreadystatechange = function (e) {
        if (d.readyState === "complete") {
            iniciar();
        }
    }
    // se crea la función inicial
    function iniciar() {
        const ciudad = "san bernardo";
        fetch(`https://api.openweathermap.org/data/2.5/weather?q=${ciudad}
        &appid=${token}&units=metric`)
        .then(r=>r.json())
        .then(({weather,main:{temp,temp_max,temp_min},wind,sys,name})=>{
            console.log(weather,temp,temp_max,temp_min,temp,wind,sys);
            cargarTiempo(weather[0].icon,name,temp,temp_min,temp_max,"Tiem");
        })
        .catch(e=>{
            console.error(e);
        });

    }
    function cargarTiempo(icono,ciudad,temperatura,min,max,descripcion){
        console.log({
            icono,ciudad,temperatura,min,max,descripcion
        })
        const img = d.querySelector(".card-image img");
        const titulo = d.getElementsByClassName("card-title")[0];
        const spanCiudad = d.getElementsByClassName("ciudad")[0];
        const pMin = d.querySelector("p.min");
        const pActual = d.querySelector("p.actual");
        const pMax = d.querySelector("p.max");
        img.src = ` http://openweathermap.org/img/wn/${icono}@2x.png`;
        titulo.innerHTML = `${temperatura}°`;
        spanCiudad.innerHTML = ciudad;
        pMin.textContent = `${parseFloat(min).toFixed(1)}°`;
        pActual.textContent = `${parseFloat(temperatura).toFixed(1)}°`;
        pMax.textContent = `${parseFloat(max).toFixed(1)}°`;
    }
})(document, window);