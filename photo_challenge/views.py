from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from .serializers import PhotoChallengeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import PhotoChallenge


# Create your views here.


class PhotoChallengeList(ListCreateAPIView):
    queryset = PhotoChallenge.objects.all()
    serializer_class = PhotoChallengeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if PhotoChallenge.objects.filter(user=self.request.user, event=serializer.validated_data['event']).exists():
            return Response({"message": "You have already participated in this photo challenge"},
                            status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "You have successfully participated in this photo challenge"},
                        status=status.HTTP_201_CREATED, headers=headers)


class PhotoChallengeDetail(RetrieveUpdateDestroyAPIView):
    queryset = PhotoChallenge.objects.all()
    serializer_class = PhotoChallengeSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
