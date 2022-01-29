from rest_framework import viewsets
from resident.models import Resident
from resident.serializer import ResidentSerializer

class ResidentViwesets(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer