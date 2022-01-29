from rest_framework import viewsets
from visitor.models import Visitor
from visitor.serializer import VisitorSerializer

class VisitorViwesets(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer