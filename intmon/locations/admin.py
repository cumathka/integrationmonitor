from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from locations.models import Location

@admin.register(Location)
class LocationAdmin(GISModelAdmin):
    list_display = ("name", "point")


