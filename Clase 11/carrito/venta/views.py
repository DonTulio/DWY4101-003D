from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Usuario
from django.shortcuts import get_object_or_404

# Create your views here.
def usuarios(request):
    template = loader.get_template('usuario/index.html')
    usuarios = Usuario.objects.all()
    context = {
        'usuarios':usuarios
    }
    return HttpResponse(template.render(context,request))

def buscarUsuario(request,usuario_id):
    usuario = get_object_or_404(Usuario, pk = usuario_id)
    return HttpResponse("Usuario encontrado {}".format(usuario))

def holaMundo(request):
    retorno = """
        <h1>Hola mundo!</h1>
        <p>Esto es una p</p>
        <a href="/usuarios">Ir a usuarios</a>
    """
    return HttpResponse(retorno)