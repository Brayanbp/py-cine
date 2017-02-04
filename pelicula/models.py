from django.db import models


class Genero(models.Model):
    nombre = models.CharField(verbose_name='Género', max_length= 50, unique= True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name= 'Género'
        verbose_name_plural= 'Géneros'


class Pais(models.Model):
    nombre = models.CharField(verbose_name='País', max_length= 100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name= 'País'
        verbose_name_plural= 'Países'


class Pelicula(models.Model):

    nombre = models.CharField(verbose_name='Película', max_length= 100)
    genero = models.ForeignKey(Genero)
    imagen = models.ImageField(verbose_name='Imagen', upload_to='peliculas/', blank=True, null=True)
    duracion = models.CharField(verbose_name='Duración', max_length=25)
    director = models.CharField(verbose_name='Director', max_length=50)
    actores = models.TextField(verbose_name='Actores')
    sinopsis = models.TextField(verbose_name='Sinopsis')
    trailer = models.CharField(verbose_name='Trailer',  max_length=100, blank=True, null=True)
    pais = models.ForeignKey(Pais)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name= 'Película'
        verbose_name_plural= 'Películas'