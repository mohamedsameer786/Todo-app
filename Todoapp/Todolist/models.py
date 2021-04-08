from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    time = timezone.now()

    def __str__(self):
        return self.title

    def __int__(self):
        return self.created
