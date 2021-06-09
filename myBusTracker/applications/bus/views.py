from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Bus

def inicio(request):
    return render(request, 'inicio/inicio.html')

def infoRutas(request):
    return render(request, 'inicio/info_rutas.html')

def infoCovid(request):
    return render(request, 'inicio/info_covid.html')

def infoPerfil(request):
    return render(request, 'inicio/info_perfil.html')

def inicioPrueba(request):
    queryset = request.GET.get('buscar')
    bus = Bus.objects.filter(estado=True)
    if queryset:
        bus = Bus.objects.filter(
            Q(buses__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    paginator = Paginator(bus, 100)
    page = request.GET.get('page')
    bus = paginator.get_page(page)

    return render(request, 'inicio/post.html', {'Bus': bus})