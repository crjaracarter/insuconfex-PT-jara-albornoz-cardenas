from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, ProductoForm, ProveedorForm, UsuarioForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Producto, Proveedor
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from insucon.Carrito import Carrito
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import FormView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail



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
    if request.POST:
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')

        send_mail(
            'Nuevo mensaje de contacto - INSUCONFEX',
            f'Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Tu mensaje ha sido enviado correctamente.')

        return redirect('quienes_somos')

    return render(request, 'quienes_somos.html')

def catalogo(request):
    return render(request,"catalogo.html")

def pagina_1(request):
    busqueda = request.GET.get("buscador")
    productos = Producto.objects.all()

    if busqueda:
        productos= Producto.objects.filter(
            Q(nombre__icontains = busqueda) 
        ).distinct()



    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 9)
        productos = paginator.page(page)
    except:
        raise Http404
    data={
        'entity': productos,
        'paginator': paginator
    }
    return render(request,"catalogo/pagina_1.html", data)


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
    return render(request,"cuenta-user/cuenta.html")

def administrador(request):
    return render(request,"administrador.html")

def usuario(request):
    return render(request,"administrador/usuario.html")

def listar_usuario(request):
    usuario = UserProfile.objects.all()
    data={
        'usuarios': usuario
    }
    return render(request, 'cuenta-user/cuenta/listar-usuario.html', data)

def agregar_usuario(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            # Guardar el usuario administrador actual
            admin_user = request.user

            # Crear el nuevo usuario
            user = formulario.save()

            # Restaurar la sesión del administrador
            login(request, admin_user)

            messages.success(request, 'Te has registrado correctamente')
            return redirect('listar_usuario')
        
        data['form'] = formulario
    return render(request, 'cuenta-user/cuenta/agregar-usuario.html', data)

def eliminar_usuario(request, id):
    usuario = get_object_or_404(UserProfile, id=id)
    usuario.delete()
    messages.success(request, "el usuario a sido eliminado")
    return redirect(to="listar_usuario")

def modificar_cuenta_2(request, id):
    perfil = get_object_or_404(UserProfile, id=id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('listar_usuario')
    else:
        form = UsuarioForm(instance=perfil)

    context = {
        'form': form,
        'perfil': perfil
    }

    return render(request, 'cuenta-user/cuenta/modificar-cuenta-2.html', context)


def detalles_cuenta_2(request):
    user = request.user

    # Verificar si el perfil de usuario existe
    if hasattr(user, 'userprofile'):
        perfil = user.userprofile
    else:
        # Manejar el caso si no existe perfil de usuario según tus necesidades
        # por ejemplo, redirigir a la página de creación de perfil
        return redirect(reverse('crear_perfil_2'))

    return render(request, 'cuenta-user/detalles-cuenta-2.html', {'perfil': perfil})


def modificar_cuenta(request, pk):
    perfil = get_object_or_404(UserProfile, id=pk)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect(reverse('detalles_cuenta'))
    else:
        form = UsuarioForm(instance=perfil)

    context = {
        'form': form,
        'perfil': perfil
    }

    return render(request, 'cuenta-user/cuenta/modificar-cuenta.html', context)


def detalles_cuenta(request):
    user = request.user

    # Verificar si el perfil de usuario existe
    if hasattr(user, 'userprofile'):
        perfil = user.userprofile
    else:
        # Manejar el caso si no existe perfil de usuario según tus necesidades
        # por ejemplo, redirigir a la página de creación de perfil
        return redirect(reverse('crear_perfil'))

    return render(request, 'cuenta-user/detalles-cuenta.html', {'perfil': perfil})


def pedidos(request):
    return render(request,"cuenta-user/pedidos.html")

def compras(request):
    return render(request,"administrador/compras.html")

def productos(request):
    return render(request,"administrador/productos.html")

def ventas(request):
    return render(request,"administrador/ventas.html")

def agregar_proveedor(request):
    data = {
        'form': ProveedorForm()
    }
    formulario = None 
    if request.method == 'POST':
        formulario =ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, "crud-provee/agregar_provee.html", data)

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    data={
        'proveedores': proveedores
    }
    return render(request, 'crud-provee/listar_provee.html', data)

def modificar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    data ={
        'form': ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_proveedor")
        data["form"] = formulario
    return render(request, "crud-provee/modificar_provee.html", data)

def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    messages.success(request, "el proveedor a sido eliminado")
    return redirect(to="listar_proveedor")
 

def carrito(request):
    return render(request, "carrito-compras/carrito.html")

def agregar_carrito(request, producto_id):
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 0))
        producto = get_object_or_404(Producto, id=producto_id)
        carrito = Carrito(request)
        carrito.agregar(producto, cantidad)
        return redirect(reverse("pagina_1"))
    return redirect(reverse("carrito"))


def eliminar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect(reverse("carrito"))

def restar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect(reverse("carrito"))

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(reverse("carrito"))

def sumar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.sumar(producto)
    return redirect(reverse("carrito"))

def checkout(request):
    carrito = Carrito(request)
    productos_carrito = carrito.carrito.values()

    if len(productos_carrito) > 0:
        # Calcular el subtotal y el total de la compra
        subtotal = 0
        for producto in productos_carrito:
            subtotal += producto['acumulado']
        total = subtotal  # Puedes agregar impuestos o descuentos aquí si es necesario

        context = {
            'productos_carrito': productos_carrito,
            'subtotal': subtotal,
            'total': total,
        }

        return render(request, 'carrito-compras/checkout.html', context)
    else:
        messages.warning(request, "El carrito está vacío.")
        return redirect('carrito')


def finalizar_compra(request):
    carrito = Carrito(request)
    productos_carrito = carrito.carrito.values()

    # Calcular el subtotal y el total de la compra
    subtotal = 0
    for producto in productos_carrito:
        subtotal += producto['acumulado']
    total = subtotal  # Puedes agregar impuestos o descuentos aquí si es necesario

    # Obtener los datos de la compra
    datos_compra = {
        'productos': productos_carrito,
        'subtotal': subtotal,
        'total': total,
    }

    return render(request, 'carrito-compras/finalizar_compra.html', {'datos_compra': datos_compra})
