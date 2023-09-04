from django.db import models

# Create your models here.

opcion =[
    [0, "Activo"],
    [1, "Inactivo"],
]  

class registros (models.Model):
    Codigo = models.CharField(max_length=7,unique=True)
    Nombre = models.CharField(max_length=50)
    Apellido_paterno = models.CharField(max_length=200)
    Apellido_materno = models.CharField(max_length=200)
    Fecha_nacimento = models.DateField()
    Edad = models.IntegerField()
    Email = models.CharField(max_length=50)
    Telefono=models.CharField(max_length=9, unique=True)
    Estado = models.IntegerField(choices=opcion)

    def __str__(self) :
        return str(self.Codigo)