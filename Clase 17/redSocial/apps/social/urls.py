from django.urls import path
from .views import ingresar, perfil
urlpatterns = [
    path('',ingresar,name='ingreso'),
    path('perfil/',perfil, name='perfil')
]