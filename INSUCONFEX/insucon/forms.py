from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto, Proveedor, UserProfile


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = '__all__'

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'
