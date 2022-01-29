from django.db import models

class OperatorCondom(models.Model):
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=14)
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    create = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    permissions= models.TextField()
    administratorSystem = models.BooleanField()

    def __str__(self) :
        return self.name