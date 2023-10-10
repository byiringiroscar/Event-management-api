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
from winner.models import WinnerLyric, WinnerPhotoChallenge
from .serializers import WinnerLyricSerializer, WinnerPhotoChallengeSerializer
from photo_challenge.models import PhotoChallenge

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
        comp_set = gamers.competition_set
        event = comp_set.event
        sample_data.append({'user': user_games, 'lyric': lyric, 'competition_set': comp_set, 'event': event})
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


@api_view(['POST', ])
def post_winner_lyrics(request):
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
            comp_set.status = True
            comp_set.save()
        users_won_models = []
        for user_name in users_won:
            email = user_name['user'].email
            user_new = User.objects.get(email=email)
            winner = WinnerLyric.objects.create(
                user=user_new,
                competition_set=user_name['competition_set'],
                event=user_name['event']
            )
            winner.save()
            users_won_models.append(user_new)

        serializer = UserSerializer(users_won_models, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def get_winners_list(request):
    winners = WinnerLyric.objects.all()
    serializer = WinnerLyricSerializer(winners, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', ])
def post_winner_photo_challenge(request):
    photo_challenges = PhotoChallenge.objects.filter(status=False)
    if not photo_challenges:
        return Response({'message': 'No photo challenge is available'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # take one from in random photo_challenge data
        random_photo_winner = photo_challenges.order_by('?').first()
        for photo in photo_challenges:
            #  change status to True
            photo.status = True
            photo.save()
    user = random_photo_winner.user
    event = random_photo_winner.event
    caption = random_photo_winner.caption
    image = random_photo_winner.image
    winner = WinnerPhotoChallenge.objects.create(user=user, event=event, caption=caption, image=image)
    winner.save()
    serializer = WinnerPhotoChallengeSerializer(winner)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', ])
def get_photo_challenge_winners_list(request):
    winners = WinnerPhotoChallenge.objects.all()
    serializer = WinnerPhotoChallengeSerializer(winners, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
