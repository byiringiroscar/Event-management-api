from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, full_name, phone_number, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('user should have email')
        if full_name is None:
            raise TypeError('user should have full_name')
        if phone_number is None:
            raise TypeError('user should have phone_number')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            full_name=full_name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, username, email, full_name, phone_number, password):
        if password is None:
            raise TypeError('Users should have a password')
        if email is None:
            raise TypeError('user should have email')
        if full_name is None:
            raise TypeError('user should have full_name')
        if phone_number is None:
            raise TypeError('user should have phone_number')
        user = self.create_user(
            username, email, full_name, phone_number, password
        )
        user.is_superuser = True
        user.is_staff = True
        user.admin = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True, db_index=True)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    full_name = models.CharField(max_length=200, unique=True, db_index=True)
    phone_number = models.CharField(max_length=200, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name', 'phone_number']
    objects = UserManager()

    def __str__(self):
        return self.email

    # get full name
    def get_full_name(self):
        return self.full_name

    # def tokens(self):
    #     refresh = RefreshToken.for_user(self)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token)
    #     }
