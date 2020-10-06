from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        "titulo":"Iniciar sesión",
        "mensaje":"Bienvenido :D"
    }
    return render(
        request,
        'login/login.html',
        context
    )
def registro(request):
    context = {
        "titulo":"Registro"
    }
    return render(
        request,
        'login/registro.html',
        context
    )
def recuperarContrasena(request):
    context = {
        "titulo":"Recupera contraseña"
    }
    return render(
        request,
        'login/contrasena.html',
        context
    )