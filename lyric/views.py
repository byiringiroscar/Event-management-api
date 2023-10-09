from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import CompetitionSetSerializer, CompetitionSerializer
from .models import CompetitionSet, Competition
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions


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
        if Competition.objects.filter(user=self.request.user,
                                      competition_set=serializer.validated_data['competition_set']).exists():
            return Response({'message': 'You have already done this competition'}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CompetitionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if the user is a superuser or superadmin
        if not request.user.is_superuser:
            return Response({"detail": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if the user is a superuser or superadmin
        if not request.user.is_superuser:
            return Response({"detail": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
