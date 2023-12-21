from django.contrib import admin
from AdministradorDePeliculas.models import Actor, Director, Pelicula
# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'genero', 'nacionalidad', 'premios', 'anio_debut']

admin.site.register(Actor,ActorAdmin)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'genero', 'nacionalidad', 'premios', 'cantidad_peliculas']

admin.site.register(Director, DirectorAdmin)


class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'minutos_duracion','genero','fecha_de_estreno','presupuesto','recaudacion','director','actor_protagonista']

admin.site.register(Pelicula, PeliculaAdmin)