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


#Para contraseñas,correo
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

class ClienteViewSet(viewsets.GenericViewSet):

    #permission_classes=(IsAuthenticated,)    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = ClienteSignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = ClienteModelSerializer(user).data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response({'mensaje': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    #Capar para que solo salga si el usuario es admin
    @action(detail=False, methods=['get'])
    def users(self, request):
        users_list=Cliente.objects.all()
        users_list_serializer = ClienteModelSerializer(users_list, many=True)
        return Response(users_list_serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def user(self, request):
        print(request.GET["dni"])
        try:
            cliente = Cliente.objects.filter(dni=request.GET["dni"]).first()
            print(cliente)
            # if(cliente is None):
            #     return Response({'mensaje': "No existe ese cliente con ese dni"}, status=status.HTTP_404_NOT_FOUND)
        except Cliente.DoesNotExist:
            return Response({'mensaje': "No existe ese cliente con ese dni"}, status=status.HTTP_404_NOT_FOUND)
        cliente_serializer = ClienteModelSerializer(cliente)
        return Response(cliente_serializer.data, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['put'])
    def modificar(self, request):
        queryset=Cliente.objects.filter(dni=request.data["dni"]).first()
        serializer=ClienteModifySerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        objeto=serializer.save()
        data=ClienteModelSerializer(objeto).data
        print(data)
        return Response(data, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['get'])
    def borrar(self, request):
        queryset=Cliente.objects.filter(dni=request.GET['dni']).first()
        try:
            queryset.delete()
            return Response("Se ha eliminado correctamente", status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            return Response({'mensaje': "No existe el cliente"}, status=status.HTTP_200_OK)        
        
    @action(detail=False, methods=['post'])
    def formularioContacto(self,request):
        # print (request.data['nombre'])
        site_url = 'https://localhost:3000/otro'
        site_shortcut_name = 'Click2Consent'
        dirCorreo='daw202237@estudiantes.salesianasnsp.es'
        # send an e-mail to the user
        context = {
            'current_user': request.data['nombre'],
            'email': dirCorreo,
            # 'reset_password_url': "{}?token={}".format(site_url, reset_password_token.key),
            'site_name': site_shortcut_name,
            'site_domain': site_url,
            'apellidos': request.data['apellidos'],
            'email': request.data['mail'],
            'telefono':request.data['tfn'],
            'coche':request.data['vehiculo'],
            'motivo':request.data['motivo'],
        }
        # render email text
        title = request.data['nombre']
        email_html_message = render_to_string('CorreoContacto.html', context)
        email_plaintext_message = render_to_string('CorreoContacto.txt', context)
        msg = EmailMultiAlternatives(
            # title:
            title,
            # message:
            email_plaintext_message,
            # from:
            "Solicitud Cita",
            # to:
            [dirCorreo],
            # BCC   
            ['daw202213@estudiantes.salesianasnsp.es']
        )
        msg.attach_alternative(email_html_message, "text/html")
        if(msg.send()):
            data="Correo enviado Correctamente"
            return Response(data, status=status.HTTP_200_OK)
        else:
            data="Ha ocurrido un problema, no se ha podido enviar el correo"
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        