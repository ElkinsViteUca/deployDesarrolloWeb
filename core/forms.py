from django import forms
from django.forms import ModelForm
from django.forms import ValidationError

from core.models import *
class TelevisorForm(ModelForm):

  class Meta:
    model = Televisor
    fields = '__all__'
    widgets = {
      'nombretv': forms.TextInput(attrs={'placeholder':'Ingrese el Televisor', 'required': False}),
      'marca': forms.Select(attrs={ 'placeholder': 'Ingrese la Marca', 'required': False}),
      'pulgadas': forms.TextInput(attrs={ 'placeholder': 'Ingrese las Pulgadas', 'required': False}),
      'tipoPanel': forms.Select(attrs={ 'placeholder': 'Ingrese la Marca', 'required': False}),
      'resolucion': forms.TextInput(attrs={ 'placeholder': 'Ingrese las Pulgadas', 'required': False}),
      'imagen': forms.FileInput(attrs={ 'required': False}),
      'costo': forms.NumberInput(attrs={ 'required': False}),
      'stock': forms.NumberInput(attrs={ 'required': False}),

    }

class RefrigeradoraForm(ModelForm):

  class Meta:
    model = Refrigeradora
    fields = '__all__'
    widgets = {
      'nombrerefrigeradora': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese la Refrigeradora', 'required': True}),
      'refrigeradoramarcaRefri': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Marca', 'required': True}),
      'refrigeradoramodeloRefri': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Modelo', 'required': True}),
      'capacidadLitros': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese los Litros', 'required': True}),
      'dimensiones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las Dimensiones', 'required': True}),
      'refrigeradoraColor': forms.Select(attrs={'class': 'form-control', 'required': True}),
      'imagen': forms.FileInput(attrs={'class': 'form-control', 'required': False}),
      'costo': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
      'stock': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),

    }


class MicroondasForm(ModelForm):
  class Meta:
    model = Microondas
    fields = '__all__'
    widgets = {
      'nombremicroondas': forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre', 'required': True}),
      'marcaMicroondas': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Marca', 'required': True}),
      'modelo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Modelo', 'required': True}),
      'capacidad': forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingrese los Litros', 'required': True}),
      'dimensiones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las Dimensiones', 'required': True}),
      'microondasColor': forms.Select(attrs={'class': 'form-control', 'required': True}),
      'imagen': forms.FileInput(attrs={'class': 'form-control', 'required': False}),
      'costo': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
      'stock': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
    }

