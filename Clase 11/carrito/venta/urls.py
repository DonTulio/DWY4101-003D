from django.urls import path, include
from . import views

urlpatterns = [
    path("usuario/",views.usuarios),
    path("usuario/<int:usuario_id>",views.buscarUsuario),
    path("saludar/",views.holaMundo)
    #path("venta/","views")
    #path("","views")
    #path("producto","views")
]

# www.mipagina.com/venta/venta
# www.mipagina.com/venta/ -> mostrarme
# www.mipagina.com/venta/producto