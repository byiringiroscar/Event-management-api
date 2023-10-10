from django.urls import path
from .views import *

urlpatterns = [
    path('post-winner-lyrics/', post_winner_lyrics, name='winner_lyrics'),
    path('get-winners-list/', get_winners_list, name='get_winners_list'),
]