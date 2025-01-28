from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet
from .views import home, add_vehicle, update_vehicle

# router = DefaultRouter()
# router.register(r'vehicles', VehicleViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_vehicle, name='add_vehicle'),
    path('update/<int:vehicle_id>/', update_vehicle, name='update_vehicle'),
]