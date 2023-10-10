from django.db import models
from event.models import Events
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.

class PhotoChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    caption = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.full_name} ---- {self.caption}'
