from django.db import models
from locations.models import Location  # Import Location model

# page models
from jobs.cms_pages import JobsPage


class Company(models.Model): 
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)  # GIS Location
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Links to Company
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)  # GIS Location
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"


