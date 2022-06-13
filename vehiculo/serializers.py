from asyncore import read
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from cliente.serializers import ClienteModelSerializer

from vehiculo.models import *

"""VEHICULO"""


class VehiculoModelSerializer(serializers.ModelSerializer):
    cliente = ClienteModelSerializer()
    #cliente = serializers.StringRelatedField()
    #cliente = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Cliente.objects.all(), source='cliente')

    class Meta:
        model = Vehiculo
        fields = (
            'marca',
            'modelo',
            'color',
            'matricula',
            'cliente',
        )

class VehiculoSerializer(serializers.Serializer):

    marca = serializers.CharField(min_length=1, max_length=50)
    modelo = serializers.CharField(min_length=1, max_length=250)
    color = serializers.CharField(min_length=1, max_length=250)

    matricula = serializers.CharField(
        validators=[UniqueValidator(queryset=Vehiculo.objects.all())],
        min_length=6,
        max_length=7
    )
    cliente = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Cliente.objects.all())

    def validate(self, data):
        return data

    def create(self, validated_data):
        vehiculo = Vehiculo.objects.create(**validated_data)
        return vehiculo


class VehiculoActualizarSerializer(serializers.Serializer):
    
    marca = serializers.CharField(min_length=1, max_length=50, required=False)    
    modelo = serializers.CharField(min_length=1, max_length=250, required=False)
    color = serializers.CharField(min_length=1, max_length=250, required=False)
    
    matricula = serializers.CharField(min_length=1, max_length=7)
    
    cliente = serializers.HiddenField(default=None, required=False)
    
    def validate(self,data):
        vehiculo_matricula = Vehiculo.objects.get(matricula=data["matricula"])
        if(vehiculo_matricula): 
            return data
        raise serializers.ValidationError("La matricula no existe")

    def update(self, vehiculo, data):        
        for d in data:
            if d == "marca" and vehiculo.marca != data[d]:
                vehiculo.marca = data.get('marca', vehiculo.marca)
            elif d == "modelo" and vehiculo.modelo != data[d]:
                vehiculo.modelo = data.get('modelo', vehiculo.modelo)
            elif d == "color" and vehiculo.color != data[d]:
                vehiculo.color = data.get('color', vehiculo.color)
        vehiculo.save()
        return vehiculo

"""ARREGLO"""
class ArregloModelSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoModelSerializer()

    class Meta:
        model = Arreglo
        fields = (
            'id',
            'fecha',
            'descripcion',
            'precio',
            'vehiculo',
        )

class ArregloSerializer(serializers.Serializer):

    id = serializers.IntegerField(required=False)
    fecha = serializers.DateField()
    descripcion = serializers.CharField(min_length=1, max_length=150)
    precio = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=0)
    vehiculo = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vehiculo.objects.all())
    
    def validate(self, data):
        return data    
    
    def create(self, validated_data):
        arreglo = Arreglo.objects.create(**validated_data)
        return arreglo
    
class ArregloActualizarSerializer(serializers.Serializer):
 
    id = serializers.IntegerField(required=False)
    fecha = serializers.DateField(required=False)
    descripcion = serializers.CharField(min_length=1, max_length=150, required=False)
    precio = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=0, required=False)    
    vehiculo = serializers.HiddenField(default=None, required=False)
    
    def validate(self,data):
        return data
    
    def update(self, arreglo, data):        
        for d in data:
            if d == "fecha" and arreglo.fecha != data[d]:
                arreglo.fecha = data.get('fecha', arreglo.fecha)
            elif d == "descripcion" and arreglo.descripcion != data[d]:
                arreglo.descripcion = data.get('descripcion', arreglo.descripcion)
            elif d == "precio" and arreglo.precio != data[d]:
                arreglo.precio = data.get('precio', arreglo.precio)
        arreglo.save()
        return arreglo
