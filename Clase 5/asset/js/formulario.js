const datos = [];
function recibirInformacion(formulario,evento){
    evento.preventDefault();
    let nuevaPersona = {
        nombre: formulario.nombre.value,
        apellido: formulario.apellido.value,
        edad: formulario.edad.value,
        fecha_nacimiento: formulario.fecha_nacimiento.value,
        detalle: formulario.detalle.value
    };
    datos.push(nuevaPersona);
    anadirHijo(nuevaPersona.nombre,
        nuevaPersona.apellido,
        nuevaPersona.edad,
        nuevaPersona.fecha_nacimiento);
}

function anadirHijo(nombre,apellido,edad,fecha){
    const tbody = document.querySelector("#tabla tbody");
    // Generando Hijo, creamos la fila
    const nuevoTr = document.createElement("tr");
    // Generando Nietos, las columnas
    const columnaNombre = document.createElement("td");
    const columnaApellido = document.createElement("td");
    const columnaEdad = document.createElement("td");
    const columnaFecha = document.createElement("td");
    columnaNombre.innerText = nombre;
    columnaApellido.innerText = apellido;
    columnaEdad.innerHTML = edad;
    columnaFecha.innerHTML = fecha;
    nuevoTr.appendChild(columnaNombre);
    nuevoTr.appendChild(columnaApellido);
    nuevoTr.appendChild(columnaEdad);
    nuevoTr.appendChild(columnaFecha);
    tbody.appendChild(nuevoTr);
}

function listarInformacion(){
    // Elemento padre
    const tbody = document.querySelector("#tabla tbody");
    //borrar
    tbody.innerHTML = "";
    // inicio del forEach
    for(const dato of datos){
        // Generando Hijo, creamos la fila
        const nuevoTr = document.createElement("tr");
        // Generando Nietos, las columnas
        const columnaNombre = document.createElement("td");
        const columnaApellido = document.createElement("td");
        const columnaEdad = document.createElement("td");
        const columnaFecha = document.createElement("td");
        columnaNombre.innerText = dato.nombre;
        columnaApellido.innerText = dato.apellido;
        columnaEdad.innerHTML = dato.edad;
        columnaFecha.innerHTML = dato.fecha_nacimiento;
        nuevoTr.appendChild(columnaNombre);
        nuevoTr.appendChild(columnaApellido);
        nuevoTr.appendChild(columnaEdad);
        nuevoTr.appendChild(columnaFecha);
        tbody.appendChild(nuevoTr);
    }
}
listarInformacion();