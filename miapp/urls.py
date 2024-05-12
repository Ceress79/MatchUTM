from django.urls import path
from . import views


app_name = 'miapp'

urlpatterns = [
    path('', views.index, name='index'),  # Agregar el nombre 'index' a esta URL
    path('home/', views.home, name='home'),  # Agregar el nombre 'home' a esta URL
]