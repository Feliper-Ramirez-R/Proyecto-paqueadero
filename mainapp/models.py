from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(models.Model):
    username = models.CharField(
        unique=True, max_length=100, verbose_name='Usuario')
    first_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')          
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    email = models.EmailField(max_length=254, verbose_name='Email')
    password = models.CharField(max_length=100, verbose_name='Contraseña')
    image = models.ImageField(default='null', verbose_name='Imagen')
    

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username

class Transporte(models.Model):
    tipo_transporte = models.CharField(max_length=50)  
    user = models.ForeignKey(User, verbose_name= 'Usuario', on_delete=models.CASCADE)         
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Transporte'
        verbose_name_plural = 'Transportes'

    def __str__(self):
        return self.tipo_transporte   

class Imagen(models.Model):
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="imagenes") 
    user = models.OneToOneField(User, verbose_name= 'Usuario', on_delete=models.CASCADE)
           

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

   
class Area(models.Model):
    area = models.CharField(max_length=50)
    user = models.OneToOneField(User, verbose_name= 'Usuario', on_delete=models.CASCADE) 
           

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'        

    def __str__(self):
        return self.area


   
           
   