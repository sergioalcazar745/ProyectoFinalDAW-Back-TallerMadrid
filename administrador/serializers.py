from rest_framework import serializers
from django.contrib.auth.models import User


class UserModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )
        
        
class userLoginSerializer(serializers.Serializer):
    
    usu=serializers.CharField( min_length=1,max_length=50)
    password=serializers.CharField(min_length=1,max_length=50 )
    
    def validate(self, data):
        return data
        
    def create(self, data):
        pass
    