from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import EventSerializer


# Create your views here.


class EventListCreateAPIView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = EventSerializer.Meta.model.objects.all()


class EventRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = EventSerializer.Meta.model.objects.all()
    lookup_field = 'id'
