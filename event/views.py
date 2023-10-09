from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import EventSerializer
from rest_framework import permissions
from .permission import IsSuperuserOrIsAdminUser, IsSuperuserOrReadOnly


# Create your views here.


class EventListCreateAPIView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = EventSerializer.Meta.model.objects.all()
    permission_classes = [IsSuperuserOrReadOnly]


class EventRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = EventSerializer.Meta.model.objects.all()
    lookup_field = 'id'
    permission_classes = [IsSuperuserOrIsAdminUser]
