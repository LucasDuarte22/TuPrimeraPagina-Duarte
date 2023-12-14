from django.shortcuts import render
from django.http import HttpResponse
from LucasApp.models import Pelicula,Libro,Musica
from LucasApp.forms import PeliculaFormulario,LibroFormulario,MusicaFormulario

# Create your views here.


def inicio(request):
    return render(request, 'LucasApp/inicio.html')

def libros(request):
    if request.method == "POST":
        miFormulario = LibroFormulario(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            libro = Libro(titulolibro=informacion["titulolibro"], autor=informacion["autor"])
            libro.save()
            return render(request, "LucasApp/inicio.html")
    else:
        miFormulario = LibroFormulario()
        return render(request, "LucasApp/Libro.html", {"miFormulario": miFormulario})





def pelicula(request):
    if request.method == "POST":
        miFormulario = PeliculaFormulario(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            pelicula = Pelicula(titulo=informacion["titulo"], director=informacion["director"])
            pelicula.save()
            return render(request, "LucasApp/inicio.html")
    else:
        miFormulario = PeliculaFormulario()
        return render(request, "LucasApp/Pelicula.html", {"miFormulario": miFormulario})
  


def musica(request):
    if request.method == "POST":
        miFormulario = MusicaFormulario(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            musica = Musica(nombre=informacion["nombre"], cantante=informacion["cantante"])
            musica.save()
            return render(request, "LucasApp/inicio.html")
    else:
        miFormulario = MusicaFormulario()
        return render(request, "LucasApp/Musica.html", {"miFormulario": miFormulario})

  
  
  
def buscar_pelicula(request):
    return render(request, 'LucasApp/buscar_pelicula.html')

def buscar_libro(request):
    return render(request, 'LucasApp/buscar_libro.html')

def buscar_musica(request):
    return render(request, 'LucasApp/buscar_musica.html')

def buscarlibro(request):
    if request.GET['autor']:

        autor = request.GET['autor']
        libros = Libro.objects.filter(autor__icontains=autor)
       
        return render(request, 'LucasApp/resultadosBusquedaLibro.html', {'libros': libros, 'autor': autor})
    else:
        respuesta = 'No enviaste datos.'
   

    return HttpResponse(respuesta)

def buscar(request):
    if request.GET['director']:

        director = request.GET['director']
        peliculas = Pelicula.objects.filter(director__icontains=director)
       
        return render(request, 'LucasApp/resultadosBusqueda.html', {'peliculas': peliculas, 'director': director})
    else:
        respuesta = 'No enviaste datos.'
   

    return HttpResponse(respuesta)

