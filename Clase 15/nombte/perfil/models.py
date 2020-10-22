from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Genero(models.Model):
    detalleGenero = models.CharField(max_length=45,blank=True)

class Perfil(models.Model):
    foto = models.FileField()
    genero = models.ForeignKey(Genero, on_delete= models.CASCADE)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    

    