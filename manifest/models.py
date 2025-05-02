from django.db import models

class BusManifest(models.Model):
    minder_name = models.CharField(max_length=100)  # Name of the minder on the bus
    bus_colour_code = models.CharField(max_length=20)  # Color code to identify the bus
    departure_time = models.TimeField()  # Time the bus left
    arrival_time = models.TimeField()  # Time the bus returned
    date = models.DateField()  # Date of the trip
    logistics_officer_number = models.CharField(max_length=20)  # Officer's phone or ID
    bus_route = models.TextField()  # Description of the route
    morning_trip = models.BooleanField(default=False)  # Was it a morning trip?
    afternoon_trip = models.BooleanField(default=False)  # Was it an afternoon trip?
    driver_name = models.CharField(max_length=100)  # Driver's full name
    driver_signature = models.CharField(max_length=100)  # Driver's signature (can be a name for now)
    number_of_children_picked = models.IntegerField()  # How many children were picked?
    children_returned = models.TextField(blank=True, null=True)  # Any notes on children returned

    def __str__(self):
        return f"{self.date} - {self.driver_name}"
