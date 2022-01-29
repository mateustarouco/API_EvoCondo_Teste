from rest_framework import serializers
from visitor.models import Visitor


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['id','rg','cpf','telefone','name','block','apartament','expiration','create','updated','last_access']

