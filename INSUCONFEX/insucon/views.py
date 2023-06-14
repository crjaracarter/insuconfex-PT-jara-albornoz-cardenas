from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, ProductoForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Producto
# Create your views here.

def index(request):
    return render(request,"home.html")

def home(request):
    return render(request,"home.html")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


def quienes_somos(request):
    return render(request,"quienes_somos.html")

def catalogo(request):
    return render(request,"catalogo.html")

def pagina_1(request):
    return render(request,"catalogo/pagina_1.html")

def pagina_2(request):
    productos = Producto.objects.all()
    data={
        'productos': productos
    }
    return render(request,"catalogo/pagina_2.html", data)

def pagina_3(request):
    return render(request,"catalogo/pagina_3.html")

def desinfectantes(request):
    return render(request,"categorias/desinfectantes.html")

def guantes(request):
    return render(request,"categorias/guantes.html")

def material_quirurgico(request):
    return render(request,"categorias/material_quirurgico.html")

def tratamiento_heridas(request):
    return render(request,"categorias/tratamiento_heridas.html")

def via_aerea(request):
    return render(request,"categorias/via_aerea.html")

def via_venosa(request):
    return render(request,"categorias/via_venosa.html")


def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    formulario = None 
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, "crud/agregar.html", data)



def listar_productos(request):
    productos = Producto.objects.all()
    data={
        'productos': productos
    }
    return render(request, 'crud/listar.html', data)


def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data ={
        'form': ProductoForm(instance=producto)

    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_productos")
        data["form"] = formulario
    return render(request, "crud/modificar.html", data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "el producto a sido eliminado")
    return redirect(to="listar_productos")

def cuenta(request):
    return render(request,"cuenta.html")

