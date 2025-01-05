# encoding: utf-8
from django import forms
from django.forms import ModelForm
from principal.models import Alumno, Profesor, Curso, Matricula

# Formulario para Alumno
class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'direccion', 'telefono', 'correo']  # Especifica los campos que quieres usar


# Formulario para Curso
class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'num_creditos']  # Especifica los campos


# Formulario para Profesor
class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'direccion', 'telefono', 'correo']  # Especifica los campos


# Formulario de contacto
class ContactoForm(forms.Form):
    correo = forms.EmailField(label='Tu correo electrónico', widget=forms.EmailInput(attrs={
        'placeholder': 'example@correo.com',
        'class': 'form-control'
    }))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Escribe tu mensaje aquí',
        'class': 'form-control',
        'rows': 4
    }))


# Formulario para Matricula
class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['fecha', 'tipo', 'alumno', 'curso']  # Especifica los campos


# Formulario para editar Alumno
class EditarAlumno(ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'direccion', 'telefono', 'correo']  # Especifica los campos
