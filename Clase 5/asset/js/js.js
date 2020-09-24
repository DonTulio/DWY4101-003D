// uso de callback
// console.log("Hola Mundo! 1");
// console.log("Hola Mundo! 2");

// function nombre(parametro,parametro2){
//     setTimeout(function(){
//         console.log("Hola Mundo! 3");
//         parametro(parametro2);
//     },2000)
// }

// let variable = function callback(parametro){
//     setTimeout(function(){
//         console.log("Hola Mundo! 4");
//         parametro();
//     },1000)
// }

// let imprimir5 = ()=>{
//     console.log("Hola Mundo! 5");
// }
// nombre(variable,imprimir5);
// uso de Promesas

// async function ejecutar() {
//     console.log("Hola mundo! 1");
//     console.log("Hola mundo! 2");
//     let esperar = new Promise((res,ref)=>{
//         setTimeout(function () {
//             console.log("Hola mundo! 3");
//             res();
//         }, 2000);
//     });
//     await esperar;
//     console.log("Hola mundo! 4");
//     console.log("Hola mundo! 5");
// }
// ejecutar();
let numero = 0;
function apretarBoton(){
    numero = numero + 1;
    console.log("has apretado el boton una cantidad de : ",numero);
    let a = document.createElement("a");
    a.href = "https://google.cl";
    a.text = "Link a google";
    // Ir a buscar el padre
    let boton = document.getElementsByTagName("body")[0];
    boton.appendChild(a);
}

// document.onreadystatechange = function(){
//     console.log(document.readyState);
// }