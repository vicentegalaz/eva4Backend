from rest_framework import serializers
from AdministradorDePeliculas.models import Actor
from AdministradorDePeliculas.models import Director
from AdministradorDePeliculas.models import Pelicula

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'