from django.db import models
from multiprocessing.sharedctypes import Value
from optparse import Values
from sys import maxsize
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique = True, max_length=100)
    email = models.EmailField('Correo electrónico', max_length=254, unique = True)
    nombres = models.CharField('Nombres', max_length=100, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length=100, blank=True, null=True)
    celular = models.PositiveIntegerField('Celular',)
    usuario_activo = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres','apellidos']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'
    
    def has_perm(self, perm, obj = None):
        return True
    def has_module_perms(self, app_label):
        return True
    

    @property
    def is_staff(self):
        return self.usuario_administrador
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    celular = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, 'userprofile'):
            UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(null=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50 )
    rut = models.IntegerField()
    correo = models.EmailField()
    celular = models.IntegerField()

    def __str__(self):
        return str(self.rut)

class Carrito(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    



