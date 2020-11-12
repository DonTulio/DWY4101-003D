from django.db import models

# Create your models here.
class Nota(models.Model):
    titulo = models.CharField(max_length=45,blank=False)
    detalle = models.TextField(blank=False)
    creacion = models.DateTimeField(auto_now=True)
    activa = models.SmallIntegerField(blank=False, default=1)