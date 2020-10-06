# importamos path para trabajar con las URLS
from django.urls import path
# importamos Views para enlazarlo con una URLs
from .views import login,registro,recuperarContrasena

urlpatterns = [
    path('',login),
    path('registro/',registro),
    path('recuperar-contrasena/',recuperarContrasena)
]