
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("oferton", views.oferton, name="oferton"),
    path("peluches", views.peluches, name="peluches"),
]

