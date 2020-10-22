from django.urls import path
from .views import mostarFormularioRegistro,registroUsuario, iniciarSesion,salir

urlpatterns = [
    path('registro/',mostarFormularioRegistro, name="registro"),
    path('crearUsuario/',registroUsuario, name="crear"),
    path('inicio/',iniciarSesion, name='iniciar'),
    path('salir/',salir, name='salir')
]