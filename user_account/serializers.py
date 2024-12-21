from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password

User = get_user_model()

from django.contrib.auth import authenticate
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email, password=password)
        if user and user.is_active:
            data['user'] = user
            return data
        raise serializers.ValidationError('Invalid email or password')




class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    nationality = serializers.CharField()
    national_id_number = serializers.CharField()
    passport_number = serializers.CharField()
    password = serializers.CharField(write_only=True)


    def validate(self, data):
        email = data.get('email')
        if User.objects.filter(email=email).exists(): 
            raise serializers.ValidationError("This email already is already used!")
        return data
    
    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            nationality=validated_data['nationality'],
            national_id_number=validated_data['national_id_number'],
            passport_number=validated_data['passport_number'],
        )
        user.password = make_password(validated_data['password'])
        user.save()
        return user

       