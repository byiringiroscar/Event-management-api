from django.urls import path, re_path
from .views import RegistrationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('event/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('event/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]