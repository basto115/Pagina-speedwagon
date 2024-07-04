from django.urls import path
from speedwagon import views


urlpatterns = [
    path("index", views.index, name="index")
]
