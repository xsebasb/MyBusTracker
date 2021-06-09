from django.urls import path
from .views import inicio, inicioPrueba, infoRutas, infoCovid, infoPerfil
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #path('listadoBuses/', busesPrueba, name='listado'),
    #path('ayuda/', detallePost, name='detalle_post'),
    path('index/', inicio, name='inicio'),
    path('busqueda/', inicioPrueba, name='busqueda'),
    path('informacion/', infoRutas, name='informacion'),
    path('covid/', infoCovid, name='covid'),
    path('perfil/', infoPerfil, name='perfil')

]