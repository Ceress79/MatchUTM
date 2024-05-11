#miapp
from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.Perfil)
admin.site.register(models.Facultad)
admin.site.register(models.Foto_extras)
admin.site.register(models.Interes)
admin.site.register(models.Matches)
admin.site.register(models.Mensaje)
admin.site.register(models.Carrera)

