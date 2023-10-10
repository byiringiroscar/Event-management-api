from rest_framework import serializers
from .models import PhotoChallenge


class PhotoChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoChallenge
        fields = ['event', 'caption', 'status', 'image']