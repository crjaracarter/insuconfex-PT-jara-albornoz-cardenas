from django.urls import path
from .views import index, home, registro, quienes_somos, catalogo, pagina_1, agregar_producto, listar_productos, modificar_producto, eliminar_producto, cuenta, administrador, compras, ventas, productos, eliminar_proveedor, modificar_proveedor, listar_proveedores, agregar_proveedor, carrito,  pedidos, detalles_cuenta, modificar_cuenta, usuario, agregar_usuario, listar_usuario, eliminar_usuario, modificar_cuenta_2, detalles_cuenta_2,  agregar_carrito, eliminar_carrito, restar_carrito, limpiar_carrito, checkout, finalizar_compra
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
     # Vista para el home de la pagina
    path('', index, name="index"),
    path('home/', home, name="home"),
    path('quienes_somos/', quienes_somos, name="quienes_somos"),
    path('catalogo/', catalogo, name="catalogo"),
     # Vista para el catalogo y productos
    path('catalogo/pagina_1/', pagina_1, name="pagina_1"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
     # Vista para la cuenta usuario
    path('cuenta-user/cuenta/',cuenta, name="cuenta"),
    path('cuenta-user/detalles-cuenta/', detalles_cuenta, name="detalles_cuenta"),
    path('cuenta-user/detalles-cuenta-2/', detalles_cuenta_2, name="detalles_cuenta_2"),
    path('cuenta-user/pedidos', pedidos, name="pedidos"),
    path('cuenta-user/cuenta/modificar-cuenta/', modificar_cuenta, name="modificar_cuenta"),
    path('cuenta-user/cuenta/modificar-cuenta-2/', modificar_cuenta_2, name="modificar_cuenta_2"),
    path('cuenta-user/cuenta/agregar-usuario/', agregar_usuario, name="agregar_usuario"),
    path('cuenta-user/cuenta/listar-usuario/', listar_usuario, name="listar_usuario"),
    path('eliminar-usuario/<id>/', eliminar_usuario, name="eliminar_usuario"),
     # Vista para la cuenta administrador
    path('administrador/', administrador, name="administrador"),
    path('administrador/compras', compras, name="compras"),
    path('administrador/productos', productos, name="productos"),
    path('administrador/ventas', ventas, name="ventas"),
    path('administrador/usuario', usuario, name="usuario"),
    path('crud-provee/agregar-provee/', agregar_proveedor, name="agregar_proveedor"),
    path('crud-provee/listar-proveedor/', listar_proveedores, name="listar_proveedor"),
    path('modificar-proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    path('eliminar-proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    path('carrito-compras/carrito/', carrito, name="carrito"),
    # Vista para el registro de usuarios
    path('registration/registro/', views.registro, name='registro'),
    path('registration/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('agregar/<int:producto_id>/', agregar_carrito, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_carrito, name="Del"),
    path('restar/<int:producto_id>/', restar_carrito, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('carrito-compras/checkout/', checkout, name="checkout"),
    path('carrito-compras/finalizar_compra/', finalizar_compra, name="finalizar_compra"),
]