from django.db import models
from datetime import date
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from cliente.models import Cliente

class Vehiculo(models.Model):
    _safedelete_policy = SOFT_DELETE
    marca=models.CharField(null=True,max_length=50)
    modelo=models.CharField(null=True,max_length=50)
    color=models.CharField(null=True,max_length=50)
    matricula=models.CharField(max_length=50, primary_key=True)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.marca, self.modelo, self.color, self.matricula, self.cliente}'
    
class Arreglo(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateField(default=date.today)
    descripcion=models.CharField(null=True,max_length=50)
    precio=models.DecimalField(null=True, max_digits=6, decimal_places=2)
    vehiculo=models.ForeignKey(Vehiculo,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f'{self.fecha, self.descripcion, self.precio, self.vehiculo}'
    
