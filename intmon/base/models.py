from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Address(models.Model):
    name = models.CharField(max_length=255)
    point = models.PointField()  # GIS field for latitude & longitude

    class Meta:
        abstract = True  # This makes it reusable
