from django.db import models
from django import forms

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateField(null=False, blank=False)
    time_start = models.TimeField()
    time_end = models.TimeField()
    location = models.CharField(max_length=2000)
    details = models.TextField(null=True, blank=True)
    cost = models.CharField(max_length=200)
    event_site = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name
    