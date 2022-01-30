from django.db import models


class Visitor(models.Model):
    rg = models.CharField(max_length=10, unique=True)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=14)
    name = models.CharField(max_length=50)
    block = models.CharField(max_length=30)
    apartament = models.CharField(max_length=10)
    expiration = models.DateField()
    create = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    last_access = models.DateField()
