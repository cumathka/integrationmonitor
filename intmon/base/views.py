from django.shortcuts import render

from locations.models import Location   

def home(request):
    context = {
        "city": Location.objects.get(name="Altdorf"),
    }
    return render(request, "base/home.html", context)
