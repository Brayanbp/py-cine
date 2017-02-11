from django.db import models
from pelicula.models import Pelicula


class Cine(models.Model):

    nombre = models.CharField(verbose_name='Cine', max_length= 100)
    imagen = models.ImageField(verbose_name='Imagen', upload_to='cines/', blank=True, null=True)
    direccion = models.CharField(verbose_name='Dirección', max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name= 'Cine'
        verbose_name_plural= 'Cines'


class Cartelera(models.Model):

    pelicula = models.ForeignKey(Pelicula)
    cine = models.ForeignKey(Cine)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.pelicula.nombre

    class Meta:
        verbose_name= 'Cartelera'
        verbose_name_plural= 'Carteleras'