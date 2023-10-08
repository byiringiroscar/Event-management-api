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


class CompetitionSet(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=250)
    artist_lyric = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.event.event_name} ---- {self.artist_name}'


class Competition(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    competition_set = models.ForeignKey(CompetitionSet, on_delete=models.CASCADE)
    user_lyrics = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.full_name} --- {self.competition_set.artist_name}'

