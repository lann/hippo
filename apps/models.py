from django.conf import settings
from django.db import models
from django.urls import reverse

from pegasus.models import UuidTimestampedModel

class App(UuidTimestampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('apps:detail', kwargs={'pk': self.pk})
