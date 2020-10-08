from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank = False)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()