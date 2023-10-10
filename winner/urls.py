from django.urls import path
from .views import *

urlpatterns = [
    path('post-winner-lyrics/', post_winner_lyrics, name='winner_lyrics'),
    path('get-winners-list/', get_winners_list, name='get_winners_list'),
    path('post_winner_photo_challenge/', post_winner_photo_challenge, name='post_winner_photo_challenge'),
    path('get_photo_challenge_winners_list/', get_photo_challenge_winners_list, name='get_photo_challenge_winners_list'),
]