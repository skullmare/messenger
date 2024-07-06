from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import CustomUser
#-----------------------------------------------------------------#
class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'login', 'first_name', 'last_name', 'password')

class CustomUserUpdateSerializer(UserSerializer):
    login = serializers.CharField(required=False)
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'login', 'first_name', 'last_name')
        read_only_fields = ('email',)
#-----------------------------------------------------------------#
class CustomPasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    re_new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['re_new_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
