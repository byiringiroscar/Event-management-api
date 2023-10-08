from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CompetitionSetSerializer, CompetitionSerializer
from .models import CompetitionSet, Competition


# Create your views here.

class CompetitionSetListCreateView(ListCreateAPIView):
    serializer_class = CompetitionSetSerializer
    queryset = CompetitionSet.objects.all()


class CompetitionSetDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CompetitionSet.objects.all()
    serializer_class = CompetitionSetSerializer
    lookup_field = 'id'
