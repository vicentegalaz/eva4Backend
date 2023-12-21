"""
URL configuration for Eva4_BackEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AdministradorDePeliculas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('actores/', views.ListaActores.as_view()),
    path('actores/<int:pk>', views.DetalleActor.as_view()),
    path('directores/', views.ListaDirectores.as_view()),
    path('directores/<int:pk>', views.DetalleDirector.as_view()),
    path('peliculas/', views.ListaPeliculas.as_view()),
    path('peliculas/<int:pk>',views.DetallesPeliculas.as_view())
]
