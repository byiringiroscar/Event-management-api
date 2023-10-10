from rest_framework import serializers
from .models import WinnerLyric


class WinnerLyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = WinnerLyric
        fields = ['user', 'event', 'competition_set']