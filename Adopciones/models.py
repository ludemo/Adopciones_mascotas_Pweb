from django.db import models
from django.urls import reverse

# Create your models here.
class Mascotas(models.Model):
    nombres = models.CharField(max_length = 100)
    edad    = models.IntegerField()
    genero  = models.CharField(max_length = 100)
    animal  = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 300,null = True)
    imagen  = models.ImageField(null = True,blank = True)

    def get_absolute_url(self):
        return reverse('Adopciones:detalles',kwargs={'myID' : self.id})

class Usuario(models.Model):
    nombre     = models.CharField(max_length = 100)
    apellido   = models.CharField(max_length = 100)
    direccion  = models.CharField(max_length = 100)
    correo     = models.EmailField(max_length=70,blank=True)
    edad       = models.IntegerField()
    telefono   = models.IntegerField()
    
    def get_absolute_url(self):
        return reverse('Adopciones:detallesUsuario', kwargs={'myID':self.id})

class Direcciones():
    def adoptar(self):
        return "enviar"
    def get_adoptar_url(self):
        return "mascotas"
    def get_usuario_url(self):
        return "user"
    def usuarioLista(self):
        return "../usuarios/"
    def mascotaCrear(self):
        return "crearMascota"
    def ListaMascota(self):
        return "ListaMascotas"
    def index(self):
        return "../"
    def pdf(self):
        return "pdf"
    def  user(self):
        return "../user/"
    
    