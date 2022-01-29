from rest_framework import viewsets
from garage.models import Garage
from garage.serializer import GarageSerializer

class GarageViwesets(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer