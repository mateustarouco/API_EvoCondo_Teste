from django.db import models

class Garage(models.Model):
    rg = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=100)
    vieicle = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    license = models.CharField(max_length=10)

    def __str__(self):
        return self.name

