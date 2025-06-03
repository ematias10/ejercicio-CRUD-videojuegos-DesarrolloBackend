from django import forms
from .models import Videojuego
from datetime import date

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el título del videojuego'}),
            'plataforma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe la plataforma'}),
            'fecha_lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'jugado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe una descripción del videojuego'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el género del videojuego'}),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 3:
            raise forms.ValidationError("El título debe tener al menos 3 caracteres.")
        return titulo
    
    def clean_fecha_lanzamiento(self):
        fecha_lanzamiento = self.cleaned_data.get('fecha_lanzamiento')
        if fecha_lanzamiento > date.today():
            raise forms.ValidationError("La fecha de lanzamiento no puede ser futura.")
        return fecha_lanzamiento