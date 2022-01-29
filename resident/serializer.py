from dataclasses import Field
from rest_framework import serializers
from resident.models import Resident


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ['id','rg','cpf','telefone','name','block','apartament','expiration','create','updated','last_access','familyID']

