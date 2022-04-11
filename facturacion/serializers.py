from facturacion.models import Gasto
from rest_framework import serializers
from cliente.serializers import UserModelSerializer


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
    usuario=serializers.HiddenField(default=None, required=False)
    concepto=serializers.CharField(min_length=1,max_length=250)
    importe=serializers.DecimalField(max_digits=6,decimal_places=2)
    
    def validate(self,data):
        return data


    def create(self,data):
        gasto= Gasto.objects.create(**data)
        return gasto
    
    
    
class GastoUpdateSerializer(serializers.Serializer):
    
    fecha=serializers.DateField(required=False)
    usuario=serializers.HiddenField(default=None, required=False)
    concepto=serializers.CharField(min_length=1,max_length=250,required=False)
    importe=serializers.DecimalField(max_digits=6,decimal_places=2, required=False)
    
    def validate(self,data):
        return data


    def create(self,data):
        gasto= Gasto.objects.create(**data)
        return gasto
        
        
    
    