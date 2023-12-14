from django.contrib import admin
from django.urls import path
from LucasApp import views



urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
    path('Libros/', views.libros, name= 'Libros'),
    path('Pelicula/', views.pelicula, name='Peliculas'),
    path('Musica/', views.musica, name='Musica'),
    path('buscarPelicula/', views.buscar_pelicula, name= 'Buscar Pelicula'),
    path('buscarPelicula/buscar/', views.buscar),
    path('buscarLibro/', views.buscar_libro, name= 'Buscar Libro'),
    path('buscarLibro/buscarlibro/', views.buscarlibro),
    

]