from doctest import master
from pyexpat import model
from django.db import models


# Create your models here.

class Login(models.Model):
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=200)
    creacion = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s %s' % (self.usuario,self.contrasena)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)

class Mascota(models.Model):
    nombreM = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    creacion = models.DateField(auto_now_add=True)
    Cliente = models.OneToOneField(Cliente,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.nombreM,self.raza)

class Citas (models.Model):
    Fecha= models.DateField(max_length=100)
    Hora = models.TimeField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)
    Cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    Mascota = models.ForeignKey(Mascota,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.Fecha,self.Hora)

class Producto(models.Model):
    nombreP = models.CharField(max_length=100)
    fechaI = models.DateField(max_length=100)
    cantidad = models.IntegerField()
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' %(self.nombreP)



