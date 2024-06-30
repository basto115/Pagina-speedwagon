from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, "speedwagon/index.html", context)

def oferton(request):
    context={}
    return render(request, "speedwagon/oferton", context)

def peluches(request):
    context={}
    return render(request, "speedwagon/peluches", context)