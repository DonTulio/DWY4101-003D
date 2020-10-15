from django.urls import path

from .views import login, registro,perfil,salir
# cuenta:login
# cuenta:registro
# cuenta:perfil
urlpatterns = [
    path('login/',login, name='login'),
    path('registro/',registro, name='registro'),
    path('perfil/',perfil, name='perfil'),
    path('salir/',salir,name='salir')
]