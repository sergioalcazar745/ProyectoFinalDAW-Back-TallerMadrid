from facturacion.models import Gasto
from rest_framework import serializers
from administrador.serializers import UserModelSerializer
from django.contrib.auth.models import User



class GastoModelSerializer(serializers.ModelSerializer):
    usuario=UserModelSerializer(many=False)
    class Meta:
        model=Gasto
        fields= (
            'fecha',
            'usuario',
            'concepto',
            'importe'
        )
        
class GastoAddSerializer(serializers.Serializer):
    fecha=serializers.DateField(required=False)
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    concepto=serializers.CharField(min_length=1,max_length=250)
    importe=serializers.DecimalField(max_digits=6,decimal_places=2)
    
    def validate(self,data):
        return data


    def create(self,data):
        gasto= Gasto.objects.create(**data)
        return gasto
    
    
    
class GastoUpdateSerializer(serializers.Serializer):
    
    fecha=serializers.DateField(required=False)
    usuario=serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False)
    concepto=serializers.CharField(min_length=1,max_length=250,required=False)
    importe=serializers.DecimalField(max_digits=6,decimal_places=2, required=False)
    
    def validate(self,data):
        return data


    def create(self,data):
        gasto= Gasto.objects.create(**data)
        return gasto
    
    def update(self, gasto, data):        
        for d in data:
            if d == "fecha" and gasto.fecha != data[d]:
                gasto.fecha = data.get('fecha', gasto.fecha)
            elif d == "usuario" and gasto.usuario != data[d]:
                gasto.usuario = data.get('usuario', gasto.usuario)
            elif d == "concepto" and gasto.concepto != data[d]:
                gasto.concepto = data.get('concepto', gasto.concepto)
            elif d == "importe" and gasto.importe != data[d]:
                gasto.importe = data.get('importe', gasto.importe)
            
        gasto.save()
        return gasto
        
        
    
    