from django.contrib import admin
from pelicula.models import Pelicula, Genero, Pais

admin.site.register(Pelicula)
admin.site.register(Genero)
admin.site.register(Pais)