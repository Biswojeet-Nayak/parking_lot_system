from django.db import models

# Create your models here.
from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('truck', 'Truck'),
    ]

    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    arrival_time = models.DateTimeField(auto_now_add=True)
    parking_slot = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.vehicle_number} ({self.vehicle_type})"