from django.contrib.gis.db import models


class Location(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    point = models.PointField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
