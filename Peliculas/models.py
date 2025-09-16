from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    anio_lanzamiento = models.IntegerField()
    duracion_minutos = models.IntegerField()

    def __str__(self):
        return self.titulo