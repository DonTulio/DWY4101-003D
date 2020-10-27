from django.shortcuts import render, redirect
from .forms import FormPublicaciones
from django.contrib import messages
# Create your views here.
def agregarPublicacion(request):
    formulario = FormPublicaciones()
    if request.method == 'POST':
        formulario = FormPublicaciones(request.POST,request.FILES)
        if  formulario.is_valid():
            publicacionNueva = formulario.save(commit=False)
            publicacionNueva.usuario = request.user
            publicacionNueva.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Publicaicón creada!!!'
            )
            return redirect('/perfil/')
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'publicacion/agregar.html',
        context
    )