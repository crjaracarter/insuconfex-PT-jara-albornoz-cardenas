from django.contrib import admin
from .models import Producto, UserProfile, Proveedor


# Register your models here.

admin.site.register(Producto)
admin.site.register(UserProfile)
admin.site.register(Proveedor)
