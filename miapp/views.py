#miapp
from django.shortcuts import render, redirect # type: ignore

from django.contrib.auth.models import *


from django.http import HttpResponse # type: ignore

def index(request):
    correo = ""
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
    
        usuario = User.objects.filter(email=correo).first()
        if usuario is not None and usuario.check_password(contrasena):
            
            return redirect('home')

    data = {
        
        'titulo' : "MathUTM"
    }
    
    return render(request, 'miapp/index.html', data)

def home(request):
    return render(request, 'miapp/home.html')