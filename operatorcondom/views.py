from rest_framework import viewsets
from operatorcondom.models import OperatorCondom
from operatorcondom.serializer import OperatorCSerializer

class OperatorCViwesets(viewsets.ModelViewSet):
    queryset = OperatorCondom.objects.all()
    serializer_class = OperatorCSerializer