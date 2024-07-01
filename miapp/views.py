# views.py
from django.shortcuts import render, redirect 
from .models import Perfil
from django.contrib.auth.models import User
from .forms import UserForm, PerfilForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    correo = ""
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
    
        usuario = authenticate(request, username=correo, password=contrasena)

        if usuario is not None:
            login(request, usuario)
            # Mensaje en consola
            print(f"El usuario {usuario.username} ha iniciado sesión correctamente.")
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('./home')
        else:
            # Mensaje en consola para el caso de inicio de sesión fallido
            print("Inicio de sesión fallido. Credenciales incorrectas.")

    data = {
        'titulo': "MatchUTM"
    }
    
    return render(request, 'miapp/index.html', data)

# home 
def home(request):
    data = {
        'titulo': 'Habitacion'
    }
    return render(request, 'miapp/home.html', data)

# PERFIL

@login_required
def profile(request):
    if request.method == 'POST':
        perfil_form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if perfil_form.is_valid():
            perfil_form.save()
            return redirect('miapp:profile')
    else:
        perfil_form = PerfilForm(instance=request.user.perfil)
    
    context = {
        'perfil_form': perfil_form
    }
    return render(request, 'miapp/profile.html', context)

