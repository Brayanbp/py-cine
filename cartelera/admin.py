from django.contrib import admin

from cartelera.models import Cine, Cartelera


class CineAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion',)
    search_fields = ('nombre',)


class CarteleraAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'cine', 'fecha',)
    list_filter = ('cine',)

admin.site.register(Cine, CineAdmin)
admin.site.register(Cartelera, CarteleraAdmin)
