from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'SIMULADOR PARA FABRICACIÓN DE PRODUCTOS FARMACÉUTICOS'
admin.site.index_title = 'Panel de control simulador fabricación'
admin.site.site_title = 'Administrador Django'


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    ordering = ('nombre',)
    search_fields = ('id', 'nombre')

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id','laboratorio', 'nombre')
    ordering = ('laboratorio','nombre')
    search_fields = ('laboratorio', 'nombre')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','laboratorio', 'year', 'p_costo', 'p_venta')
    ordering = ('laboratorio','nombre')
    search_fields = ('laboratorio', 'nombre')
    list_filter = ('laboratorio', 'nombre')

    def year(self, obj):
        return obj.f_fabricacion.strftime('%Y')