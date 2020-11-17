from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def ingresar(request):
    return render(
        request,
        'ingresar/index.html'
    )

@login_required
def perfil(request):
    return render(
        request,
        'ingresar/perfil.html'
    )