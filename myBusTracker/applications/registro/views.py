from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistroFormulario
# Create your views here.

def inicio(request):
    context = {
        'bienvenido': 'Binevenido'
    }
    return render(request, 'inicio/inicio.html', context)

def registro(request):
    titulo='Crear una cuenta'
    form = RegistroFormulario(request.POST)
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            return  redirect('inicio')
        else:
            form = RegistroFormulario()
    context = {
        'formulario':form,
        'titulo':titulo
    }
    return render(request, 'Usuario/registro.html', context)