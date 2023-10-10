from django.db import models
from event.models import Events
from lyric.models import CompetitionSet
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.

class WinnerLyric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    competition_set = models.ForeignKey(CompetitionSet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.full_name} ---- {self.event.event_name}'


class WinnerPhotoChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.full_name} --- {self.event.event_name}'
