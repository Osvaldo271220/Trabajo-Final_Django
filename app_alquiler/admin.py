from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Plataforma, Genero, Videojuego, Alquiler

class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'plataforma', 'genero', 'stock')

class AlquilerAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'videojuego', 'fecha_alquiler', 'fecha_devolucion')

admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Videojuego, VideojuegoAdmin)
admin.site.register(Alquiler, AlquilerAdmin)