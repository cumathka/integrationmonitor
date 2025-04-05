from django.db import models
from locations.models import Location  # Import Location model

from wagtail.models import Page
from django.shortcuts import render


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

#############################
#### Page models ############
#############################


class JobsPage(Page):
    template = "jobs/jobs_page.html"

    # Optional: Add fields like intro text or filters
    # intro = models.TextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        context["jobs"] = Job.objects.all()  # add your job queryset
        return context



