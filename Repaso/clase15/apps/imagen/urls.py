from django.urls import path

from .views import agregarPublicacion
urlpatterns = [
    path('agregar/',agregarPublicacion,name='agregarPublicacion')
]