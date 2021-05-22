from django.urls import path
from .views import buscadorBuses, detallePost

urlpatterns = [
    path('inicio/', buscadorBuses, name='inicio'),
    path('ayuda/', detallePost, name='detalle_post'),
]