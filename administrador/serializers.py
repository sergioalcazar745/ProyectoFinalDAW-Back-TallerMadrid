from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import password_validation, authenticate
from rest_framework.authtoken.models import Token


class UserModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )
        
        
# class userLoginSerializer(serializers.Serializer):
    
#     usu=serializers.CharField( min_length=1,max_length=50)
#     password=serializers.CharField(min_length=1,max_length=50 )
    
#     def validate(self, data):
#         return data
        
#     def create(self, data):
#         pass
    
    
class UserLoginSerializer(serializers.Serializer):
    
    # Campos que vamos a requerir
    username = serializers.CharField(min_length=1, max_length=64)
    password = serializers.CharField(min_length=1, max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key