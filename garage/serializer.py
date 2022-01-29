from rest_framework import serializers
from garage.models import Garage


class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = ['id','rg','name','number','vieicle','model','license']

