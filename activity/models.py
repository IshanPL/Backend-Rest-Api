from django.db import models
from django.utils import timezone


class User(models.Model):
    tz_CHOICES = (('Asia', 'Asia'), ('America/Los_Angeles', 'America/Los_Angeles'),)
    id = models.SlugField(primary_key=True, max_length=100)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=20, choices=tz_CHOICES, default='Asia')

    def __str__(self):
        return self.real_name


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.user)

