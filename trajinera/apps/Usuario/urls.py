from django.urls import path
from apps.Usuario.views import *

urlpatterns = [
    path('index_administrador/', indexAdministrador, name = 'index_menu'),
    path('menu_Alimentos_Administrador/', menu_Alimentos_Administrador.as_view() , name = 'menu_alimentos'),
    path('menu_Alimentos_Editar/', menu_Alimentos_Editar.as_view() , name = 'menu_editar_alimentos'),
    path('menu_Alimentos_Eliminar/', menu_Alimentos_Eliminar.as_view() , name = 'menu_eliminar_alimentos'),
    path('menu_Alimentos_crear/', Crear_Alimento.as_view() , name = 'crear_alimento'),
    path('editar_Alimento/<pk>', Editar_Alimento.as_view() , name = 'editar_alimento'),
    path('eliminar_Alimento/<pk>', Eliminar_Alimento.as_view() , name = 'eliminar_alimento'),
]

