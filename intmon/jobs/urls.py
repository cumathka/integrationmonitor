from django.urls import path
from jobs.views import jobs_list

app_name = "jobs"

urlpatterns = [
    path("", jobs_list, name="jobs-list"),
]
