from django.urls import path

from .views import registro, inicio, loginView

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('inicio/', inicio, name='inicio'),
    path('login/', loginView, name='login'),
]