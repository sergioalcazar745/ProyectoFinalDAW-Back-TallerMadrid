"""Users serializers."""

# Django
from django.core.validators import RegexValidator, FileExtensionValidator

# Django REST Framework
from rest_framework import serializers
#from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from cliente.models import Cliente

# Serializers


class ClienteModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = (
            'nombre',
            'apellidos',
            'email',
            'foto',
            'telefono',
            'calle',
            'dni',
        )

# crear Cliente


class ClienteSignUpSerializer(serializers.Serializer):

    nombre = serializers.CharField(
        min_length=3,
        max_length=50,
        validators=[UniqueValidator(queryset=Cliente.objects.all())]
    )

    apellidos = serializers.CharField(
        min_length=3,
        max_length=70,
    )

    email = serializers.EmailField(
        max_length=70
    )

    #foto = serializers.ImageField(
        #validators=[FileExtensionValidator(
        #    allowed_extensions=['jpg', 'jpeg', 'png'])],
        #required=False
    #)

    phone_regex = RegexValidator(
    regex=r'\d*',
    message="Debes introducir un número con el siguiente formato: +999999999. El límite son de 15 dígitos."
    )
    telefono = serializers.CharField(   validators=[phone_regex],
        min_length=9,
        max_length=9
    )

    calle = serializers.CharField(max_length=70)

    dni = serializers.CharField(
        max_length=9,
        validators=[UniqueValidator(queryset=Cliente.objects.all())]
    )

    def validate(self, data):
        print("PADRE")
        image = None
        if 'photo' in data:
            image = data['photo']

        if image:
           if image.size > (512 * 1024):
               raise serializers.ValidationError(f"La imagen es demasiado grande, el peso máximo permitido es de 512KB y el tamaño enviado es de {round(image.size / 1024)}KB")

        return data

    def create(self, data):
        print("Datita: ", data)
        user = Cliente.objects.create(**data)
        print("Cliente creado: ", user)
        return user


class ClienteModifySerializer(serializers.Serializer):
    nombre = serializers.CharField(required=False, min_length=4, max_length=50)
    apellidos = serializers.CharField(
        required=False, min_length=3, max_length=70)
    # foto = serializers.ImageField(required=False, validators=[
    #                               FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    email = serializers.EmailField(required=False, max_length=70)
    telefono = serializers.CharField(
        required=False, min_length=9, max_length=9)
    dni = serializers.CharField(required=True, validators=[
                                UniqueValidator(queryset=Cliente.objects.all())], max_length=9)
    calle = serializers.CharField(required=False, max_length=70)

    def validate(self, data):
        print("VALIDATE")
        return data

    def update(self, cliente, data):
        print("UPDATE")
        cliente.nombre = data.get('nombre', cliente.nombre)
        cliente.apellidos = data.get('apellidos', cliente.apellidos)
        cliente.email = data.get('email', cliente.email)
        cliente.foto = data.get('foto', cliente.foto)
        cliente.telefono = data.get('telefono', cliente.telefono)
        cliente.calle = data.get('calle', cliente.calle)
        cliente.dni = data.get('dni', cliente.dni)
        print("SAVE-UPDATE: ", cliente)
        cliente.save()
        return cliente

    def create(self, data):
        user = Cliente.objects.create(**data)
        return user
