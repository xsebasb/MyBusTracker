from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistroFormulario, UsuarioLoginFormulario
# Create your views here.

def inicio(request):
    context = {
        'bienvenido': 'Binevenido'
    }
    return render(request, 'inicio/inicio.html', context)


def loginView(request):
    titulo = 'login'
    form = UsuarioLoginFormulario(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        passsword = form.cleaned_data.get("passsword")
        usuario = authenticate(username=username, password=passsword)
        login(request, usuario)
        return redirect('inicio')
    context={
        'form':form,
        'titulo': titulo
    }
    return render(request, 'Usuario/login.html', context)

def registro(request):
    titulo='Crear una cuenta'
    form = RegistroFormulario(request.POST)
    if request.method == 'POST':
        if form.is_valid():

            form.save()
            return  redirect('login')
        else:
            form = RegistroFormulario()
    context = {
        'formulario':form,
        'titulo':titulo
    }
    return render(request, 'Usuario/registro.html', context)


def logout_vista(request):
    logout(request)
    return redirect('/')