from django.urls import path
from .views import event_list

app_name = "events"

urlpatterns = [
    path("", event_list, name="event-list"),
]
