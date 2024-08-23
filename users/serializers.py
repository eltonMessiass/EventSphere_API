from rest_framework import serializers
from .models import User, Profile

from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            "password": {"write_only":True},
            'username': {"required": True},
            'email': {
                'error_messages': {
                    'required': 'O email é obrigatório.',
                    'null': 'O email não pode ser nulo.'
                }
            }
        }

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            print("Existe")
            raise serializers.ValidationError("This username is already in use!")
        return username
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    


class ProfileSerilizer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ["id", "user", "role","profile_picture",  "bio", "birth_date", "phone_number"]
        extra_kwargs = {"user":{"read_only": True}}

        
