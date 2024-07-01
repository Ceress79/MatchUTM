# En el archivo models.py de tu aplicación miapp

from django.db import models
from django.contrib.auth.models import User

class Facultad(models.Model):
    nombre = models.CharField(max_length=50)

class Carrera(models.Model):
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)
    foto_banner = models.ImageField(upload_to='banner/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Foto_extras(models.Model):
    foto = models.ImageField(upload_to='extras/')
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

class Interes(models.Model):
    nombre = models.CharField(max_length=45)

class PersonaInteres(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    interes = models.ForeignKey(Interes, on_delete=models.CASCADE)

class Matches(models.Model):
    usuario1 = models.ForeignKey(Perfil, related_name='matches_usuario1', on_delete=models.CASCADE)
    usuario2 = models.ForeignKey(Perfil, related_name='matches_usuario2', on_delete=models.CASCADE, null=True)
    fecha = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

class Mensaje(models.Model):
    matches = models.ForeignKey(Matches, on_delete=models.CASCADE)
    chat = models.CharField(max_length=300)
    mensaje = models.TextField(default="")
    foto = models.ImageField(upload_to='mensajes/', null=True, blank=True)
    video = models.CharField(max_length=300, null=True, blank=True)
    leido = models.BooleanField(default=False)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    usuario = models.CharField(choices=[("1", "1"), ("2", "2")], max_length=1)