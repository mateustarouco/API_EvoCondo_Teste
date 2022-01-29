from turtle import mode
from django.db import models


class Resident(models.Model):
    rg = models.CharField(max_length=10,unique=True)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=14)
    name = models.CharField(max_length=50)
    block = models.CharField(max_length=30)
    apartament = models.CharField(max_length=10)
    expiration = models.DateField()
    create = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    last_access = models.DateField()
    familyID = models.IntegerField(unique=True)

    def __str__(self):
        return self.name