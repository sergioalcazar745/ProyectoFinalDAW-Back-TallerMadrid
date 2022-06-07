from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from vehiculo.models import Vehiculo
from vehiculo.serializers import ArregloActualizarSerializer, ArregloModelSerializer, ArregloSerializer, VehiculoActualizarSerializer, VehiculoModelSerializer, VehiculoSerializer

from vehiculo.models import Arreglo



class VehiculoViewSet(viewsets.GenericViewSet):
    model = Vehiculo
    serializer_class = VehiculoModelSerializer

    @action(detail=False, methods=['get'])
    def vehiculos(self, request):
        vehiculo_list = self.model.objects.all()
        vehiculo_list_serializer = self.serializer_class(vehiculo_list, many=True)
        return Response(vehiculo_list_serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def getvehiculo(self, request):
        try:
            vehiculo = self.model.objects.filter(matricula=request.GET["matricula"]).first()
            if(vehiculo is None):
                return Response({'mensaje': "No existe ese vehiculo con esa matricula"}, status=status.HTTP_404_NOT_FOUND)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        vehiculo_serializer = VehiculoModelSerializer(vehiculo)
        return Response(vehiculo_serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def getvehiculobydni(self, request):
        try:
            vehiculo_list = self.model.objects.filter(cliente__dni=request.GET["dni"])
            if(vehiculo_list is None):
                return Response({'mensaje': "No existe ese vehiculo con ese cliente"}, status=status.HTTP_404_NOT_FOUND)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        vehiculo_list_serializer = self.serializer_class(vehiculo_list, many=True)
        return Response(vehiculo_list_serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def savevehiculo(self, request):
        vehiculo_serializer = VehiculoSerializer(data=request.data)
        if vehiculo_serializer.is_valid():
            vehiculo_response = vehiculo_serializer.save()
            vehiculo_response_seralizer = VehiculoModelSerializer(vehiculo_response).data
            return Response(vehiculo_response_seralizer, status=status.HTTP_201_CREATED)
        else:
            return Response(vehiculo_serializer.errors)

    @action(detail=False, methods=['put'])
    def updatevehiculo(self, request):
        queryset=self.model.objects.filter(matricula=request.data["matricula"]).first()
        serializer=VehiculoActualizarSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        objeto=serializer.save()
        data=VehiculoActualizarSerializer(objeto).data
        return Response(data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def deletevehiculo(self, request):
        vehiculo = self.model.objects.filter(matricula=request.GET["matricula"]).first()
        if(vehiculo is None):
            return Response({'mensaje': "No existe ese vehiculo con esa matricula"}, status=status.HTTP_404_NOT_FOUND)
        vehiculo_delete = vehiculo.delete()
        vehiculo_serializer = VehiculoModelSerializer(vehiculo_delete)
        return Response(vehiculo_serializer.data, status=status.HTTP_200_OK)

class ArregloViewSet(viewsets.GenericViewSet):
    model = Arreglo
    serializer_class = ArregloModelSerializer

    @action(detail=False, methods=['get'])
    def arreglos(self, request):
        arreglo_list = self.model.objects.all()
        arreglo_list_serializer = self.serializer_class(arreglo_list, many=True)
        return Response(arreglo_list_serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def getarreglo(self, request):
        try:
            arreglo = self.model.objects.filter(vehiculo__matricula=request.GET["matricula"], fecha=request.GET["fecha"]).first()
            if(arreglo is None):
                return Response({'mensaje': "No existe ese vehiculo con esa matricula y fecha"}, status=status.HTTP_404_NOT_FOUND)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        arreglo_serializer = self.serializer_class(arreglo)
        return Response(arreglo_serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def getarreglobymatricula(self, request):
        try:
            arreglo_list = self.model.objects.filter(vehiculo__matricula=request.GET["matricula"])
            if(arreglo_list is None):
                return Response({'mensaje': "No existe ese vehiculo con esa matricula"}, status=status.HTTP_404_NOT_FOUND)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        arreglo_list_serializer = self.serializer_class(arreglo_list, many=True)
        return Response(arreglo_list_serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def savearreglo(self, request):
        arreglo_serializer = ArregloSerializer(data=request.data)
        if arreglo_serializer.is_valid():
            arreglo_response = arreglo_serializer.save()
            arreglo_response_seralizer = ArregloModelSerializer(arreglo_response).data
            return Response(arreglo_response_seralizer, status=status.HTTP_201_CREATED)
        else:
            return Response(arreglo_serializer.errors)

    @action(detail=False, methods=['put'])
    def updatearreglo(self, request):
        arreglo=self.model.objects.filter(id=request.data["id"]).first()
        arreglo_serializer=ArregloActualizarSerializer(arreglo, data=request.data)
        arreglo_serializer.is_valid(raise_exception=True)
        arreglo_response=arreglo_serializer.save()
        arreglo_serializer_response=ArregloActualizarSerializer(arreglo_response)
        return Response(arreglo_serializer_response.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def deletearreglo(self, request):
        arreglo = self.model.objects.filter(id=request.GET["id"]).first()
        print(arreglo)
        if(arreglo is None):
            return Response({'mensaje': "No existe ese arreglo con ese id"}, status=status.HTTP_404_NOT_FOUND)
        try:
            arreglo_deleted=arreglo.delete()
        except Arreglo.DoesNotExist:
            return Response({'mensaje': "No existe ese arreglo con ese id"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'mensaje': "Se ha eliminado correctamente"}, status=status.HTTP_200_OK)
    