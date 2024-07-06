from django.urls import path
from speedwagon import views


urlpatterns = [
    path("index", views.index, name="index"),
    path("cata2", views.cata2, name="cata2"),
    path("catalogo", views.catalogo, name="catalogo"),
    path("oferton", views.oferton, name="oferton"),
    path("peluches", views.peluches, name="peluches"),
    path("registro", views.registro, name="registro"),
    path("ropa", views.ropa, name="ropa"),
    path("seinen", views.seinen, name="seinen"),
    path("shonen", views.shonen, name="shonen"),
    path("crud", views.crud, name="crud"),
    path("carrito", views.carrito, name="carrito"),
    path("usuarioAdd", views.usuarioAdd, name="usuarioAdd")
    
]
