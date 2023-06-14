from django.urls import path
from .views import index, home, registro, quienes_somos, catalogo, pagina_1, pagina_2, pagina_3, desinfectantes, guantes, material_quirurgico, tratamiento_heridas, via_aerea, via_venosa, agregar_producto, listar_productos, modificar_producto, eliminar_producto, cuenta


urlpatterns = [
    path('', index, name="index"),
    path('home/', home, name="home"),
    path('registro/', registro, name="registro"),
    path('quienes_somos/', quienes_somos, name="quienes_somos"),
    path('catalogo/', catalogo, name="catalogo"),
    path('catalogo/pagina_1/', pagina_1, name="pagina_1"),
    path('catalogo/pagina_2/', pagina_2, name="pagina_2"),
    path('catalogo/pagina_3/', pagina_3, name="pagina_3"),
    path('categorias/desinfectantes/', desinfectantes, name="desinfectantes"),
    path('categorias/guantes/', guantes, name="guantes"),
    path('categorias/material_quirurgico/', material_quirurgico, name="material_quirurgico"),
    path('categorias/tratamiento_heridas/', tratamiento_heridas, name="tratamiento_heridas"),
    path('categorias/via_aerea/', via_aerea, name="via_aerea"),
    path('categorias/via_venosa/', via_venosa, name="via_venosa"),
    path('categorias/via_venosa/', via_venosa, name="via_venosa"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('cuenta/', cuenta, name="cuenta"),
]