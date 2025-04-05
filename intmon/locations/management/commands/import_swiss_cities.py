import csv
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from locations.models import Location

class Command(BaseCommand):
    help = "Imports Swiss city locations from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csvfile", type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        csv_path = kwargs["csvfile"]

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["name"]
                latitude = float(row["lat"])
                longitude = float(row["lon"])

                location, created = Location.objects.get_or_create(
                    name=name,
                    defaults={"point": Point(longitude, latitude)},
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added location: {name}"))
                else:
                    self.stdout.write(self.style.WARNING(f"{name} already exists"))
