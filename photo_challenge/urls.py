from django.urls import path
from .views import PhotoChallengeList, PhotoChallengeDetail

urlpatterns = [
    path('photo_challenges/', PhotoChallengeList.as_view(), name='photo_challenge_list'),
    path('photo_challenges/<int:id>/', PhotoChallengeDetail.as_view(), name='photo_challenge_detail'),
]