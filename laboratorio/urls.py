from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('laboratorio/add', add_laboratorio, name='add_laboratorio'),
    path("laboratorio/mostrar", mostrar_laboratorio, name="mostrar_laboratorio"),
    path("laboratorio/<int:laboratorio_id>/editar", v_laboratorio_edit, name="editar_laboratorio"),
    path("laboratorio/<int:laboratorio_id>/eliminar", v_laboratorio_delete, name="eliminar_laboratorio"),
    path('director/add', add_director, name='add_director'),
    ]