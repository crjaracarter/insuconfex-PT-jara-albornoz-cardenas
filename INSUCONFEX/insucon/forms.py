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
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    celular = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=100)
    comuna = forms.CharField(max_length=50)

    class Meta:
        model = UserProfile
        fields = [ 'nombre', 'apellido', 'celular', 'direccion', 'comuna']
