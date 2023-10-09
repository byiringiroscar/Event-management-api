from django.shortcuts import render
from rest_framework.decorators import api_view
from event.models import Events

# Create your views here.

@api_view(['POST', ])
def winner_lyrics(request):
