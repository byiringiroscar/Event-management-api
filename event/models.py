from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.


class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_picture = models.ImageField()
    event_venue = models.CharField(max_length=100)
    event_details = models.TextField()
    event_price = models.PositiveIntegerField()
    event_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Event'

    def __str__(self):
        return self.event_name


