from django.urls import path
from .views import *

urlpatterns = [
    path('winner_lyrics/', winner_lyrics, name='winner_lyrics')
]