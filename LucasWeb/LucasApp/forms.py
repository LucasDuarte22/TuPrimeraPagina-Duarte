from django import forms

class LibroFormulario(forms.Form):
    titulolibro = forms.CharField()
    autor = forms.CharField()
    
class PeliculaFormulario(forms.Form):
    titulo = forms.CharField()
    director= forms.CharField()
    
class MusicaFormulario(forms.Form):
    nombre = forms.CharField()
    cantante = forms.CharField()