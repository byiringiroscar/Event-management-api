from django.urls import path
from .views import *

urlpatterns = [
    path('event/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('event/<int:id>/', EventRetrieveUpdateDeleteAPIView.as_view(), name='event-detail'),
]


