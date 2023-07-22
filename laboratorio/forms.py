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