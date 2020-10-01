from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    apellido = models.CharField(max_length= 50, blank= False)
    edad = models.IntegerField()
    generos = (
        ('M','Masculino'),
        ('F','Femenino')
    )
    genero = models.CharField(max_length=1,choices=generos, default='M')

    def obtenerNombreCompleto(self):
        return "{} {} {}".format(self.nombre, self.apellido, self.edad)

    def __str__(self):
        return self.obtenerNombreCompleto()

