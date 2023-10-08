from django.urls import path
from .views import CompetitionSetListCreateView, CompetitionSetDetailView

urlpatterns = [
    path('competition-sets/', CompetitionSetListCreateView.as_view(), name='competition-set-list'),
    path('competition-sets/<int:id>/', CompetitionSetDetailView.as_view(), name='competition-set-detail'),
    # path('competitions/', CompetitionListCreateView.as_view(), name='competition-list'),
    # path('competitions/<int:pk>/', CompetitionDetailView.as_view(), name='competition-detail'),
]
