from django.contrib.auth.forms import UserCreationForm #Usado no admin para usuarios
from django import forms
from .models import User

class UserAdminCreatForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email']

class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name','is_active', 'is_staff']
