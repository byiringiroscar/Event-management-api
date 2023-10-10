from rest_framework import serializers
from .models import WinnerLyric, WinnerPhotoChallenge


class WinnerLyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = WinnerLyric
        fields = ['user', 'event', 'competition_set']


class WinnerPhotoChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WinnerPhotoChallenge
        fields = ['user', 'event', 'caption', 'image']
