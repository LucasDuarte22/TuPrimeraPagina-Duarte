from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    titulolibro = models.CharField(max_length=200)
    autor= models.CharField(max_length=200)

    

class Pelicula(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    titulo = models.CharField(max_length=200)
    director = models.CharField(max_length=200)


class Musica(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=200)
    cantante = models.CharField(max_length=200)


