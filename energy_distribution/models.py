from django.db import models

class EnergyProvider(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.FloatField()

class EnergyUser(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    provider = models.ForeignKey(EnergyProvider, on_delete=models.CASCADE)
    is_off_grid = models.BooleanField(default=False)

class EnergyConsumption(models.Model):
    user = models.ForeignKey(EnergyUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()