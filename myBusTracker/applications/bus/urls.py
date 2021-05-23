from django.urls import path
from .views import buscadorBuses, detallePost,busesPrueba, inicio

urlpatterns = [
    path('listadoBuses/', busesPrueba, name='listado'),
    path('ayuda/', detallePost, name='detalle_post'),
    path('inicio/', inicio, name='inicio'),
]