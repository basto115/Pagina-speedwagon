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
    usuarios = Usuario.objects.all()
    context ={
        "Usuarios": Usuario,
    }
    return render(request, "speedwagon/crud.html", context)

def carrito(request):
    context={}
    return render(request, "speedwagon/carrito.html", context)


def usuarioAdd(request):
    if request == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        email = request.POST["email"]
        user = request.POST["user"]
        password = request.POST["password"]
        
    obj = Usuario.objects.create(
        
        nombre = nombre,
        apellido = apellido,
        email = email,
        user = user,
        password = password
    )
    obj.save()
    context = {
        "mensaje": "Registro exitoso",
    }
    return render(request, "speedwagon/usuarioAdd.html", context)
        
def usuarioUpdate(request):
    if request.method=="POST":
        user = request.POST["user"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    email = request.POST["email"]

    
    password = request.POST["password"]
    
    obj = Usuario(
        nombre = nombre,
        apellido = apellido,
        email = email,
        user = user,
        password = password
    )
    obj.save()
