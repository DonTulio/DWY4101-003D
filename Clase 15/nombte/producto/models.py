from django.db import models
from perfil.models import Perfil
# Create your models here.
class Producto(models.Model):
    precio = models.PositiveIntegerField()

class Venta(models.Model):
    vendedor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()

class DetalleVenta(models.Model):
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Venta, on_delete=models.CASCADE)
    total_individual = models.PositiveIntegerField()
