
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("oferton", views.oferton, name="oferton"),
    path("peluches", views.peluches, name="peluches"),
    path("catalogo", views.catalogo, name="catalogo"),
    path("cata2", views.cata2, name="cata2"),
    path("registro", views.registro, name="registro"),
    path("ropa", views.ropa, name="ropa"),
    path("seinen", views.seinen, name="seinen"),
    path("shonen", views.shonen, name="shonen"),
]

