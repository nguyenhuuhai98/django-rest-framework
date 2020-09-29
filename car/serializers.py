from rest_framework import serializers

from car.models import Car, User


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('name', 'color', 'brand')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
