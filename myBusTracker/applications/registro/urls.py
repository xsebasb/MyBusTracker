from django.urls import path

from .views import registro, inicioRegistro, logout_vista

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('inicioRegistro/', inicioRegistro, name='inicioRegistro'),
    path('logout_vista/', logout_vista, name='logout_vista'),

]