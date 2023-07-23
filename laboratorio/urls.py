from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('laboratorio/add', add_laboratorio, name='add_laboratorio'),
    path("laboratorio/mostrar", mostrar_laboratorio, name="mostrar_laboratorio"),
    path("laboratorio/<int:laboratorio_id>/editar", v_laboratorio_edit, name="editar_laboratorio"),
    path("laboratorio/<int:laboratorio_id>/eliminar", v_laboratorio_delete, name="eliminar_laboratorio"),
    path('director/add', add_director, name='add_director'),
    path("director/mostrar", mostrar_directores, name="mostrar_directores"),
    path("director/<int:pk>/editar", v_director_edit, name="editar_director"),
    path("director/<int:pk>/eliminar", v_director_delete, name="eliminar_director"),
    path('producto/add', add_producto, name='add_producto'),
    path("productos/mostrar", mostrar_productos, name="mostrar_productos"),
    path("producto/<int:pk>/editar", v_producto_edit, name="editar_producto"),
    path("producto/<int:pk>/eliminar", v_producto_delete, name="eliminar_producto"),
    ]