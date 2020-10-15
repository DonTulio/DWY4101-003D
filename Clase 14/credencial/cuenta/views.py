from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login as iniciarSesion, logout, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
def login(request):
    formulario = None
    if request.method == 'POST':
        formulario = AuthenticationForm(data = request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contra = formulario.cleaned_data['password']

            usuarioLogeado = authenticate(username = usuario, password = contra)

            if usuarioLogeado is not None:
                iniciarSesion(request,usuarioLogeado)
                return redirect('/usuario/perfil/')
    else:
        formulario = AuthenticationForm()
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'cuenta/login.html',
        context
    )

def registro(request):
    formulario = None
    if request.method == 'POST':
        formulario = UserCreationForm( data = request.POST)
        if formulario.is_valid():
            usuarioGuardado = formulario.save()
            if usuarioGuardado is not None:
                iniciarSesion(request,usuarioGuardado)
                return redirect('/usuario/perfil/')
    else:
        formulario = UserCreationForm()
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'cuenta/registro.html',
        context
    )

def perfil(request):
    return render(
        request,
        'cuenta/perfil.html'
    )
def salir(request):
    logout(request)
    return redirect('/usuario/login')