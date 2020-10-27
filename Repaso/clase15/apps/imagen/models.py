from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=45,blank=False)
    detalle = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='imagens')
    fechaSubida = models.DateField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)