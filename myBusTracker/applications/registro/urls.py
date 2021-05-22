from django.urls import path

from .views import registro, inicio, loginView, logout_vista

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('inicio/', inicio, name='inicio'),
    path('logout_vista/', logout_vista, name='logout_vista'),
    path('login/', loginView, name='login'),
]