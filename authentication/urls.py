from django.urls import path, re_path
from .views import RegistrationView, MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('event/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('event/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]