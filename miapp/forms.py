# forms.py
from django import forms 
from .models import Perfil
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto_perfil', 'foto_banner']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']