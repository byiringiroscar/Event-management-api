from rest_framework import serializers
from .models import Events


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['event_name', 'event_picture', 'event_venue', 'event_details', 'event_price', 'event_time']
    