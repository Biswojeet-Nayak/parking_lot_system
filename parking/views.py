from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def perform_create(self, serializer):
        # Assign a parking slot (basic logic)
        serializer.validated_data['parking_slot'] = f"Slot-{Vehicle.objects.count() + 1}"
        serializer.save()

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def add_vehicle(request):
    return render(request, 'add_vehicle.html')

def update_vehicle(request, vehicle_id):
    return render(request, 'update_vehicle.html', {'vehicle_id': vehicle_id})
