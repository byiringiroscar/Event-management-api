from rest_framework import serializers
from .models import User
import re
# from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

# User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16, min_length=6, write_only=True)
    # password_2
    password_2 = serializers.CharField(max_length=16, min_length=6, write_only=True)  
    email = serializers.EmailField(max_length=255, min_length=4)
    username = serializers.CharField(max_length=255, min_length=4)
    full_name = serializers.CharField(max_length=255, min_length=4)

    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'phone_number', 'password', 'password_2', ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        full_name = attrs.get('full_name', '')
        phone_number = attrs.get('phone_number', '')
        password = attrs.get('password', '')
        phone_regex = re.compile(r'^(\+\d{1,3}\s?)?\d{7,14}$')
        try:
            existing_user = User.objects.get(username=username)
            raise serializers.ValidationError('User with this username already exists.')
        except ObjectDoesNotExist:
            pass
        try:
            existing_user = User.objects.get(email=email)
            raise serializers.ValidationError('User with this email already exists.')
        except ObjectDoesNotExist:
            pass
        try:
            existing_user = User.objects.get(phone_number=phone_number)
            raise serializers.ValidationError('User with this phone number already exists.')
        except ObjectDoesNotExist:
            pass
        if not phone_regex.match(phone_number):
            raise serializers.ValidationError('The phone number is not valid')
        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        if password != attrs.get('password_2'):
            raise serializers.ValidationError('The passwords did not match')
        return attrs

        # validate the phone number

    def create(self, validated_data):
        validated_data.pop('password_2', None)
        return User.objects.create_user(**validated_data)
