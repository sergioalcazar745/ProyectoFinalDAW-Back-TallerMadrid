from django.shortcuts import render

# Create your views here.

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Serializers
from cliente.serializers import *

# Models
from cliente.models import Cliente

class ClienteViewSet(viewsets.GenericViewSet):

    #permission_classes=(IsAuthenticated,)
    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = ClienteSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = ClienteSignUpSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
    
        #Capar para que solo salga si el usuario es admin
    @action(detail=False, methods=['get'])
    def users(self, request):
        queryset=Cliente.objects.all()
        arrResult = []
        for result in queryset:  
            arrResult.append(ClienteModelSerializer(result).data)
        return Response({'usuarios': arrResult}, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['put'])
    def modificar(self, request):
        queryset=Cliente.objects.filter(dni=request.POST['dni']).first()
        serializer=ClienteModifySerializer(queryset, request.data)
        serializer.is_valid(raise_exception=True)
        objeto=serializer.save()
        data=ClienteModelSerializer(objeto).data
        return Response(data, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['delete'])
    def borrar(self, request):
        queryset=Cliente.objects.filter(dni=request.GET['dni']).first()
        try:
            objeto=queryset.delete()
        except Cliente.DoesNotExist:
            return None
        else:
            data= ClienteModelSerializer(objeto).data   #Asi convierto el objeto que he guardado en serilizer para enviar el json
            return Response(data, status=status.HTTP_200_OK)