# En el archivo models.py de tu aplicación miapp

from django.db import models
from django.contrib.auth.models import User

# Definir el modelo Facultad
class Facultad(models.Model):
    nombre = models.CharField(max_length=50)

# Definir el modelo Carrera
class Carrera(models.Model):
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

# Definir el modelo Perfil
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=250)
    altura = models.CharField(max_length=45)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

# Definir el modelo Foto_extras
class Foto_extras(models.Model):
    foto = models.CharField(max_length=300)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

# Definir el modelo Interes
class Interes(models.Model):
    nombre = models.CharField(max_length=45)

# Definir el modelo PersonaInteres
class PersonaInteres(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    interes = models.ForeignKey(Interes, on_delete=models.CASCADE)

# Definir el modelo Matches
class Matches(models.Model):
    usuario1 = models.ForeignKey(Perfil, related_name='matches_usuario1', on_delete=models.CASCADE)
    usuario2 = models.ForeignKey(Perfil, related_name='matches_usuario2', on_delete=models.CASCADE, null=True)
    fecha = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

# Definir el modelo Mensaje
class Mensaje(models.Model):
    matches = models.ForeignKey(Matches, on_delete=models.CASCADE)
    chat = models.CharField(max_length=300)
    mensaje = models.TextField(default="")
    foto = models.CharField(max_length=300, null=True)
    video = models.CharField(max_length=300, null=True)
    leido = models.BooleanField(default=False)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    usuario = models.CharField(choices=[("1", "1"), ("2", "2")], max_length=1)
