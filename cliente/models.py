from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE

# Create your models here.
class Cliente(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    nombre= models.CharField(null=True, max_length=50)
    apellidos= models.CharField(null=True, max_length=70)
    email = models.EmailField(null=True, max_length=70)
    foto = models.ImageField(null=True, upload_to='uploads/fotos')
    telefono = models.CharField(null=True,max_length=9)
    calle = models.CharField(null=True, max_length=70)
    dni = models.CharField(max_length=9, primary_key=True)
