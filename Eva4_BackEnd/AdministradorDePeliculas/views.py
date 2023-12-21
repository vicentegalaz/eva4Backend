from django.shortcuts import render
from .serializers import ActorSerializer, DirectorSerializer, PeliculaSerializer
from .models import Actor, Director, Pelicula
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins
from rest_framework import generics

# Create your views here.

class ListaActores(generics.ListCreateAPIView,mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request):
        actores = Actor.objects.all()
        serializer = ActorSerializer(actores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetalleActor(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    def get_object(self, pk):
        try: 
            return Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            return Http404
    
    def get(self,request, pk):
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def put(self, request, pk):
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        actor = self.get_object(pk)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ListaDirectores(generics.ListCreateAPIView,mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    def get(self, request):
        directores = Director.objects.all()
        serializer = DirectorSerializer(directores, many=True)
        return Response(serializer.data)
    
class DetalleDirector(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def get_object(self, pk):
        try: 
            return Director.objects.get(pk=pk)
        except Director.DoesNotExist:
            return Http404
    
    def get(self,request, pk):
        director = self.get_object(pk)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)

    def put(self, request, pk):
        director = self.get_object(pk)
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        director = self.get_object(pk)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ListaPeliculas(generics.ListCreateAPIView,mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    def get(self, request):
        pelicula = Pelicula.objects.all()
        serializer = PeliculaSerializer(pelicula, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PeliculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetallesPeliculas(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    def get_object(self, pk):
        try: 
            return Pelicula.objects.get(pk=pk)
        except Pelicula.DoesNotExist:
            return Http404
    
    def get(self,request, pk):
        pelicula = self.get_object(pk)
        serializer = PeliculaSerializer(pelicula)
        return Response(serializer.data)

    def put(self, request, pk):
        pelicula = self.get_object(pk)
        serializer = PeliculaSerializer(pelicula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pelicula = self.get_object(pk)
        pelicula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
