from rest_framework import serializers
from .models import User
from django.core.validators import RegexValidator
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16, min_length=6, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    username = serializers.CharField(max_length=255, min_length=4)
    full_name = serializers.CharField(max_length=255, min_length=4)

    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'phone_number', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        full_name = attrs.get('full_name', '')
        phone_number = attrs.get('phone_number', '')
        password = attrs.get('password', '')
        phone_regex = RegexValidator(regex=r'^(\+\d{1,3}\s?)?\d{7,14}$')
        if not phone_regex.match(phone_number):
            raise serializers.ValidationError('The phone number is not valid')
        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs

        # validate the phone number

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
