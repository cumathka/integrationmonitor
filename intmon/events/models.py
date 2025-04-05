from django.db import models

from locations.models import Location

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%Y-%m-%d')}"

