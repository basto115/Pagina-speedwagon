from django.shortcuts import render
from .models import Usuario

# Create your views here.

def index(request):
    context={}
    return render(request, "speedwagon/index.html", context)

def cata2(request):
    context={}
    return render(request, "speedwagon/cata2.html", context)

def catalogo(request):
    context={}
    return render(request, "speedwagon/catalogo.html", context)

def oferton(request):
    context={}
    return render(request, "speedwagon/oferton.html", context)

def peluches(request):
    context={}
    return render(request, "speedwagon/peluches.html", context)

def registro(request):
    context={}
    return render(request, "speedwagon/registro.html", context)

def ropa(request):
    context={}
    return render(request, "speedwagon/ropa.html", context)

def seinen(request):
    context={}
    return render(request, "speedwagon/seinen.html", context)

def shonen(request):
    context={}
    return render(request, "speedwagon/shonen.html", context)

def crud(request):
    usuario = Usuario.objects.all()
    context = {
        "usuario": Usuario,
    }
    return render(request, "speedwagon/crud.html", context)


