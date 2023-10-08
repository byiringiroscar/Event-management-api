from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import CompetitionSetSerializer, CompetitionSerializer
from .models import CompetitionSet, Competition
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class CompetitionSetListCreateView(ListCreateAPIView):
    serializer_class = CompetitionSetSerializer
    queryset = CompetitionSet.objects.all()


class CompetitionSetDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CompetitionSet.objects.all()
    serializer_class = CompetitionSetSerializer
    lookup_field = 'id'


class CompetitionListCreateView(ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CompetitionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
