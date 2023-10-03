from django.shortcuts import render
from rest_framework import generics, status, views
from .serializers import RegisterSerializer

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .renderers import UserRender

# Create your views here.


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    renderer_classes = (UserRender,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)