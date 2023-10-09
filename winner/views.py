from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import difflib
from event.models import Events
from lyric.models import CompetitionSet
import json
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name']


def calculate_winner(official_lyrics, sample_gamers):
    sample_data = []
    for gamers in sample_gamers:
        user_games = gamers.user
        lyric = gamers.user_lyrics
        sample_data.append({'user': user_games, 'lyric': lyric})
    winner_participant = []
    for data in sample_data:
        matcher = difflib.SequenceMatcher(None, data['lyric'], official_lyrics)
        similarity = matcher.ratio()
        # get who have first above similarity ratio
        initial_ratio = 0
        if similarity > initial_ratio:
            initial_ratio = similarity
            winner_participant.append(data)
    winner = winner_participant[0]
    return winner


@api_view(['GET', ])
def winner_lyrics(request):
    competition_set = CompetitionSet.objects.filter(status=False)
    if not competition_set:
        return Response({'message': 'No competition set is available'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        users_won = []
        for comp_set in competition_set:
            competition = comp_set.get_competition
            official_lyrics = comp_set.artist_lyric
            winner = calculate_winner(official_lyrics, competition)
            users_won.append(winner)
            # comp_set.status = True
            # comp_set.save()
            # Serialize the users_won list to JSON
        users_won_models = []
        for user_name in users_won:
            email = user_name['user'].email
            try:
                user_new = User.objects.get(email=email)
            except:
                return Response({'message': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)
            users_won_models.append(user_new)

        serializer = UserSerializer(users_won_models, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
