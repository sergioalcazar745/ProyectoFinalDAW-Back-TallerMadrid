from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


#serializers
from administrador.serializers import *

# Create your views here.
class AdminViewSet(viewsets.GenericViewSet):
    
    @action(detail=False, methods=['post'])
    def login(self, request):
    #     usu=UserLoginSerializer(data=request.data)
    #     usu.is_valid(raise_exception=True)
    #     print("usuario")
    #     print(usu.data['usu'])
    #     usu=authenticate(username=usu.data['usu'],password=usu.data['password'])
    #     if usu is not None:
    #         login(request,usu)
    #         data=UserModelSerializer(usu).data
    #         return Response(data, status=status.HTTP_200_OK)
    #     else:  
    #         data="Nombre de usuario o contraseña incorrectas"
    #         return Response({'usuarios': data}, status=status.HTTP_400_BAD_REQUEST)
        
        
        #LOGIN PARA EL TOKEN, PONER AL FINAL CUANDO TODO VAYA BIEN
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
        
        
        
    # @action(detail=False, methods=['get'])    
    # def logout(self,request):
    #     logout(request)
    #     data="Hasta pronto"
    #     return Response(data, status=status.HTTP_200_OK)
    
    
 #LOGOUT PARA EL TOKEN, PONER AL FINAL CUANDO TODO VAYA BIEN    
class AdminOutViewSet(viewsets.GenericViewSet):
    serializer_class = UserModelSerializer
    permission_classes=(IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def logout(self, request):  
        print("entroooo")
        request.user.auth_token.delete()
        data="Sesion cerrada"
        return Response({'data': data}, status=status.HTTP_200_OK)
            
        
