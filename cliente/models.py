from django.db import models
from pkg_resources import require
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from django.utils.safestring import mark_safe

def url(self,filename):
    ruta = "static/img/clientes/%s%s"%(self.nombre,str(filename))
    return ruta


# Create your models here.
class Cliente(models.Model):
    
    # def foto_cliente(self):
    #     return mark_safe('<img src="/%s" width=50px height=50px />'%(self.foto))
        
    _safedelete_policy = SOFT_DELETE
    nombre= models.CharField(null=True, max_length=50)
    apellidos= models.CharField(null=True, max_length=70)
    email = models.EmailField(null=True, max_length=70)
    # foto = models.ImageField(null=True, upload_to=url)
    telefono = models.CharField(null=True,max_length=9)
    calle = models.CharField(null=True, max_length=70)
    dni = models.CharField(max_length=9, primary_key=True)
    
    def __str__(self):
      #  return f'{self.dni}'
        return self.dni
