from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from facturacion.models import Gasto

from facturacion.serializers import GastoModelSerializer, GastoAddSerializer

# Create your views here.
class GastoViewSet(viewsets.GenericViewSet):
    permission_classes=(IsAuthenticated,)
    
    
    @action(detail=False, methods=['post'])
    def addGasto(self, request):
        """User sign up."""
        serializer = GastoAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        gasto = serializer.save()
        data = GastoModelSerializer(gasto).data
        return Response(data, status=status.HTTP_201_CREATED)
     
    @action(detail=False, methods=['get'])
    def gastos(self, request):
        queryset=Gasto.objects.all()
        arrResult = []
        for result in queryset:  
            arrResult.append(GastoModelSerializer(result).data)
        return Response({'gastos': arrResult}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def gastosPorFecha(self,request):
        fechaInicio=request.GET['inicio']
        fechaFin=request.GET['fin']
        queryset=Gasto.objects.filter(fecha>=fechaInicio).filter(fecha<=fechaFin)
        arrResult = []
        for result in queryset:  
            arrResult.append(GastoModelSerializer(result).data)
        return Response({'gastos': arrResult}, status=status.HTTP_200_OK)
        
        
    