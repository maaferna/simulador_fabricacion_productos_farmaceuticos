from django import forms
from .models import *
from crispy_forms.layout import Submit, Fieldset, Submit, Field, Layout
from crispy_forms.helper import FormHelper
from django.forms.widgets import NumberInput

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = '__all__'
    
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre del Laboratorio',}),
            'ciudad': forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese ciudad",}),
            'pais': forms.Select(attrs={'class': 'form-control',}),
        }


class DirectorGeneralForm(forms.ModelForm):
    class Meta:
        model = DirectorGeneral
        fields = '__all__'
    
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre Director',}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese especialidad'}),
            'laboratorio': forms.Select(attrs={"class": "form-control", "placeholder": "Ingrese ciudad",}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre Director',}),
            'f_fabricacion': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
            'laboratorio': forms.Select(attrs={"class": "form-control", "placeholder": "Ingrese laboratorio",}),
            'p_costo': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese costo de venta",}),
            'p_venta': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese precio de venta",}),
        }