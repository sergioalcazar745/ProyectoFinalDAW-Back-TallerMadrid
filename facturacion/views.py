from ast import For
from posixpath import split
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date

from facturacion.models import Gasto

from facturacion.serializers import *
from vehiculo.serializers import *
from vehiculo.models import Arreglo

# Create your views here.
class GastoViewSet(viewsets.GenericViewSet):
    #permission_classes=(IsAuthenticated,)
      
    @action(detail=False, methods=['post'])
    def addGasto(self, request):
        serializer = GastoAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        gasto = serializer.save()
        data = GastoModelSerializer(gasto).data
        return Response(data, status=status.HTTP_201_CREATED)
     
    @action(detail=False, methods=['get'])
    def gastos(self, request):
        queryset=Gasto.objects.all().order_by('-fecha')
        arrGastos = []
        for result in queryset:  
            arrGastos.append(GastoModelSerializer(result).data)
        return Response(arrGastos, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def gastosPorFecha(self,request):
        inicio=request.GET['inicio'].split("-")
        fin=request.GET['fin'].split("-")
        fechaInicio=date(int(inicio[0]),int(inicio[1]),int(inicio[2]))
        fechaFin=date(int(fin[0]),int(fin[1]),int(fin[2]))
        queryset=Gasto.objects.filter(fecha__gte=fechaInicio,fecha__lte=fechaFin)
        querysetArreglos=Arreglo.objects.filter(fecha__gte=fechaInicio,fecha__lte=fechaFin)
        
        arrArreglos=[]
        arrGastos = []

        for result in queryset:
            # messtr=result.fecha.strftime("%Y-%m-%d")
            # mes=messtr.split("-")[1]
            # if mes in arrGastos.keys():
            #     arrGastos[mes].append(GastoModelSerializer(result).data)
            # else:
            #     arrGastos[mes]=[]
            #     arrGastos[mes].append(GastoModelSerializer(result).data)
            arrGastos.append(GastoModelSerializer(result).data)
        
        for result in querysetArreglos:
            # messtr=result.fecha.strftime("%Y-%m-%d")
            # mes=messtr.split("-")[1]
            # if mes in arrArreglos.keys():
            #     arrArreglos[mes].append(ArregloModelSerializer(result).data)
            # else:
            #     arrArreglos[mes]=[]
            #     arrArreglos[mes].append(ArregloModelSerializer(result).data)
            arrArreglos.append(ArregloModelSerializer(result).data)
         
        return Response({'gastos': arrGastos, 'arreglos':arrArreglos}, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['put'])
    def UpdateGasto(self, request):
        queryset=Gasto.objects.filter(id=int(request.GET['id'])).first()
        serializer=GastoUpdateSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        objeto=serializer.save()
        data=GastoModelSerializer(objeto).data
        return Response(data, status=status.HTTP_200_OK)
        
        
    @action(detail=False, methods=['delete'])
    def DeleteGasto(self, request):
        queryset=Gasto.objects.filter(id=int(request.GET['id'])).first()
        if queryset is None:
            data="No hay ningun gasto con ese ID"
        else:
            objeto=queryset.delete()
            data="Objeto borrado con exito"
        return Response(data, status=status.HTTP_200_OK)
        
        
    