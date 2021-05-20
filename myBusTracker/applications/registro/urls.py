from django.urls import path

from .views import registro, inicio

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('inicio/', inicio, name='inicio')
]