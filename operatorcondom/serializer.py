from dataclasses import Field
from rest_framework import serializers
from operatorcondom.models import OperatorCondom


class OperatorCSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatorCondom
        fields = ['id','rg','cpf','telefone','name','birthday','create','updated','permissions','administratorSystem']

