(function(w,d,$){
    d.addEventListener("readystatechange",function(){
        if(d.readyState === "complete"){
            iniciar();
        }
    });
    let notas = undefined;
    const url = w.location.href+"api/notas/";
    const tbody = d.getElementsByTagName("tbody")[0];
    function irABuscarLasNotas(){
        fetch(url)
        .then(function(respuesta){
            return respuesta.json();
        })
        .then(function(data){
            notas = data;
            llenarTabla();
        })
        .catch(function(error){
            console.error(error)
        })
        .finally(function(){
            console.log("Notas cargadas :D");
        });
    }
    function modificarNota(idNota){
        console.log(idNota);
    }
    function activarDesactivar(idNota,estado){
        console.log(idNota,estado)
    }
    function construirTR(nota){
        // Creación de las columnas
        const tr = d.createElement("tr");
        tr.id = nota.id;
        const tdTitulo = d.createElement("td");
        tdTitulo.innerText = nota.titulo;
        const tdFecha = d.createElement("td");
        tdFecha.innerText = nota.creacion;
        const tdEstado = d.createElement("td");
        tdEstado.innerText = nota.activa === 1 ? "Pendiente":"Finalizado";
        const tdAccion = d.createElement("td");
        const btnModificar = d.createElement("button")
        btnModificar.innerText = "M";
        btnModificar.addEventListener("click",function(){
            modificarNota(nota.id);
        });
        const btnActiva = d.createElement("button");
        if(nota.activa === 1){
            btnActiva.innerText = "D";
            btnActiva.addEventListener("click",function(){
                activarDesactivar(nota.id,1)
            })
        }else{
            btnActiva.innerText = "A";
            btnActiva.addEventListener("click",function(){
                activarDesactivar(nota.id,0)
            })
        }
        //Asingacion los btn estados a la columna estado
        tdAccion.appendChild(btnModificar);
        tdAccion.appendChild(btnActiva);
        //Asingación de las columnas a la fila
        tr.appendChild(tdTitulo);
        tr.appendChild(tdFecha);
        tr.appendChild(tdEstado);
        tr.appendChild(tdAccion);
        tbody.appendChild(tr);
        console.log(nota);
    }

    function escucharForm(){
        const formulario = d.getElementsByTagName("form")[1];
        formulario.addEventListener("submit",function(e){
            e.preventDefault();
            const titulo = d.getElementsByName("titulo")[0].value;
            const detalle = d.getElementsByName("detalle")[0].value;
            const objetoSalida = {
                titulo:titulo,
                detalle:detalle
            }
            fetch(url,{
                method:'POST',
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify(objetoSalida)
            })
            .then(function(peticion){
                return peticion.json();
            })
            .then(function(data){
                construirTR(data);
            })
            .catch(function(error){
                console.error(error)
            })
            .finally(function(){
                console.info("Finalizo la petición de agregar nota...");
                formulario.reset();
            })
        })
    }
    function llenarTabla(){
        tbody.innerText = "";
        for(nota of notas){
            construirTR(nota);
        }
    }
    function iniciar(){
        irABuscarLasNotas();
        escucharForm();
    }

})(window,document,$)