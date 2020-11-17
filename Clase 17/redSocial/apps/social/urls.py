from django.urls import path
from .views import ingresar, perfil
urlpatterns = [
    path('ingresar/',ingresar,name='ingreso'),
    path('',perfil, name='perfil')
]