from wagtail.models import Page
from django.shortcuts import render
from jobs.models import Job  # import your existing model

class JobsPage(Page):
    template = "jobs/jobs_page.html"

    # Optional: Add fields like intro text or filters
    # intro = models.TextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        context["jobs"] = Job.objects.all()  # add your job queryset
        return context
