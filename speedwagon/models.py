from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    user = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=30)
    
def __str__(self):
    return (
        str(self.nombre) 
        + " "
        + str(self.apellido)
        + " "
        + str(self.user)
    )

