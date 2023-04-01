from django.db import models
from django.urls import reverse


class Schedules(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
