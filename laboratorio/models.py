from django.db import models
# Create your models here.
from django_countries.fields import CountryField

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    pais = CountryField(blank_label='(Seleccione el pais)', blank=True)

    def __str__(self):
        return f"{self.nombre}"
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.PROTECT)
    especialidad = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.PROTECT)
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre}"