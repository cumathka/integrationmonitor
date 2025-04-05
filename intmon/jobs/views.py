from django.shortcuts import render
from jobs.models import Job

def jobs_list(request):
    jobs = Job.objects.all().order_by("-posted_at")  # Show latest jobs first
    return render(request, "jobs/jobs_list.html", {"jobs": jobs})
