from django.shortcuts import render, redirect
# importando el modelo
from .models import Producto
# Importando los formularios
from .forms import FormProducto

# Create your views here.
def listarProductos(request):
    productos = Producto.objects.all()
    context = {
        'titulo':'Listar productos',
        'productos':productos
    }
    return render(
        request,
        'producto/listar_producto.html',
        context
    )

def agregarProducto(request):

    formulario = None
    if request.method == 'POST':
        formulario = FormProducto(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/producto')
    else:
        formulario = FormProducto()
    context = {
        'titulo':'Agregar producto',
        'formulario':formulario
    }
    return render(
        request,
        'producto/agregar_producto.html',
        context
    )

def editarProducto(request,id_producto):
    productoEncontrado = Producto.objects.get(pk = id_producto)
    formulario = None

    if request.method == 'POST':
        formulario = FormProducto(request.POST, instance= productoEncontrado)
        if formulario.is_valid():
            formulario.save()
            return redirect('/producto/')
    else:
        formulario = FormProducto(instance= productoEncontrado)
    context = {
        'titulo':'Modificar producto',
        'formulario':formulario
    }

    return render(
        request,
        'producto/modificar_producto.html',
        context
    )

def eliminarProducto(request, id_producto):
    productoEncontrado = Producto.objects.get(pk=id_producto)
    productoEncontrado.delete()

    return redirect('/producto')