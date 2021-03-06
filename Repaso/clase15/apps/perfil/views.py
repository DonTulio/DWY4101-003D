from django.shortcuts import render, redirect
from .forms import FormularioCreacion, FormularioPerfil,FormIniciarSesion
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
## importando el modelo desde publicaciones.....
from apps.imagen.models import Publicacion
# Create your views here.
def mostarFormularioRegistro(request):
    formulario1 = FormularioCreacion()
    formulario2 = FormularioPerfil()
    context = {
        'formulario1':formulario1,
        'formulario2':formulario2
    }
    return render(
        request,
        'perfil/registro.html',
        context
    )

def registroUsuario(request):
    if request.method == 'POST':
        formulario1 = FormularioCreacion(request.POST)
        formulario2 = FormularioPerfil(request.POST)
        if formulario1.is_valid() and formulario2.is_valid():
            usuarioGuardado = formulario1.save()
            perfilGuardado = formulario2.save(commit=False)
            perfilGuardado.usuario = usuarioGuardado
            perfilGuardado.save()
            messages.add_message(request,
                messages.SUCCESS,
                'Usuario registrado con éxito :D'
            )
            return redirect('/inicio/')
        context = {
        'formulario1':formulario1,
        'formulario2':formulario2
        }
        return render(
            request,
            'perfil/registro.html',
            context
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'No puedes estar aquí'
        )
        return redirect('/registro/')

def iniciarSesion(request):
    formulario = FormIniciarSesion()
    if request.method == 'POST':
        formulario = FormIniciarSesion(data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            usuarioLogeado = authenticate(username=username,password=password)
            if usuarioLogeado is not None:
                login(request,usuarioLogeado)
                return redirect('/inicio/')
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    'Usuario o contraseña son incorrectos'
                )
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'perfil/iniciarSesion.html',
        context)

def salir(request):
    logout(request)
    return redirect('/inicio/')

def perfil(request):
    publicaciones = Publicacion.objects.all()
    context = {
        'publicaciones':publicaciones
    }
    return render(
        request,
        'perfil/perfil.html',
        context
    )