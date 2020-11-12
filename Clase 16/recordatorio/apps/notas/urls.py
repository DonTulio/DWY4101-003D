from django.urls import path
from .views import saludar, buscarModificarCambiarEstado,listarAgregarYQuizasEliminarxD

""" 
    /api/notas/
    Tengo diferentes ventanas
    GET    = Listar
    POST   = Agregar
    # DELETE = Eliminar / borrar todos los elemenos
    /api/notas/id_elemento/
    GET    = Buscar por id / listar un elemento por ID
    PUT    = Modificar_por_id
    DELETE = Eliminar_por_id
"""

urlpatterns = [
    path('saludar/',saludar, name='saludar'),
    path('',listarAgregarYQuizasEliminarxD),
    path('<int:uid>/',buscarModificarCambiarEstado)
]