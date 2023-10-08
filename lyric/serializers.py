from rest_framework import serializers
from .models import CompetitionSet, Competition


class CompetitionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionSet
        fields = '__all__'


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['competition_set', 'user_lyrics', ]
