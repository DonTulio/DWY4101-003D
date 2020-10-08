from django.urls import path

from .views import listarProductos,agregarProducto,editarProducto,eliminarProducto

urlpatterns = [
    # Muchos path
    path('',listarProductos,name = 'listar_producto'),
    path('agregar/',agregarProducto,name='agregar_producto'),
    path('editar/<int:id_producto>',editarProducto, name='editar_producto'),
    path('eliminar/<int:id_producto>',eliminarProducto, name='eliminar_producto')
]