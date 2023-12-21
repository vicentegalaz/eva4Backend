from django.shortcuts import render
from .serializers import ActorSerializer, DirectorSerializer, PeliculaSerializer
from .models import Actor, Director, Pelicula
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

class ListaActores(APIView):

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




class DetalleActor(APIView):
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