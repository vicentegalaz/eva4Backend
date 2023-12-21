from django.db import models

# Create your models here.

GENERO = [('Masculino','Masculino'), ('Femenino','Femenino'),('No Aplica','Prefiero no decirlo')]

NACIONALIDAD = [('Estadounidense' , 'Estadounidense'), ('Británico','Británico'), ('Canadiense','Canadiense'),('Chileno','Chileno'), ('Peruano','Peruano'),('Otro','Otro')]

OPCIONES_GENERO = [('Accion','Accion'),('Comedia','Comedia'),('Drama','Drama'),('Terror','Terror'),('Otros','Otros')]



class Actor (models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(default='')
    genero = models.CharField(max_length=20, choices=GENERO)
    nacionalidad = models.CharField(max_length=50, choices=NACIONALIDAD)
    premios = models.PositiveIntegerField(default='')
    anio_debut = models.PositiveIntegerField(default='')

    def __str__(self):
        return f'{self.nombre}, {self.edad} años'


class Director (models.Model):
 
    nombre = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(default='')
    genero = models.CharField(max_length=20,choices=GENERO)
    nacionalidad = models.CharField(max_length=50,choices=NACIONALIDAD)
    premios = models.PositiveIntegerField(default='')
    cantidad_peliculas = models.PositiveIntegerField(default='')

    def __str__(self):
        return f'{self.nombre}, {self.edad} años'


class Pelicula (models.Model):

    titulo = models.CharField(max_length=30)
    minutos_duracion = models.PositiveIntegerField(default=0)
    genero = models.CharField(max_length=10,choices=OPCIONES_GENERO)
    fecha_de_estreno = models.CharField(max_length=10,default='dd/mm/aaaa')
    presupuesto = models.PositiveIntegerField(default=0)
    recaudacion = models.PositiveIntegerField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actor_protagonista = models.ForeignKey(Actor,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo}, {self.director}'
