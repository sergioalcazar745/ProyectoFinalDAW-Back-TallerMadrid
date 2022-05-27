from datetime import date
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from django.contrib.auth.models import User
from vehiculo.models import Arreglo

# Create your models here.
class Gasto(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    fecha=models.DateField(default=date.today)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    concepto=models.CharField(null=True,max_length=50)
    importe=models.DecimalField(max_digits=6,decimal_places=2,null=True)
    
    
class Factura(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    fecha=models.DateField(default=date.today)
    arreglo=models.ForeignKey(Arreglo,on_delete=models.CASCADE,null=True)

    
    
    
    