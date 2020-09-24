function enviarFormulario(formulario, evento){
    evento.preventDefault();
    const validacion = {
        usuario:{
            maxlength:5,
            minlength:2
        },
        password:{
            maxlength:5,
            minlength:2
        }
    }
    // console.log(formulario.usuario.value);
    // console.log(formulario.usuario.getAttribute("t-maxlength"));
    // console.log(formulario.usuario.getAttribute("t-minlength"));
    // const maximo = formulario.usuario.getAttribute("t-maxlength");
    // const minimo = formulario.usuario.getAttribute("t-minlength");
    // const usuario = formulario.usuario.value;
    // console.log(usuario.length);
    // if(usuario.length < minimo || usuario.length > maximo){
    //     console.log("Entro");
    //     alert("EL nombre de usuario es incorrecto");
    // }
    const inputs = document.querySelectorAll("input");
    for(const elemento of inputs){
        let largo = elemento.value.trim().length;
        let nombreElemento = elemento.getAttribute("name");
        if(nombreElemento !== null){
            if(largo < validacion[nombreElemento].minlength || largo > validacion[nombreElemento].maxlength){
                console.log(`El elemento ${nombreElemento} es invalido XD`);
            }
        }
    }
}