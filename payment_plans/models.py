from django.db import models

# Create your models here.

class PaymentPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in months
    interest_rate = models.FloatField()

class UserPaymentPlan(models.Model):
    user = models.ForeignKey('energy_distribution.EnergyUser', on_delete=models.CASCADE)
    plan = models.ForeignKey(PaymentPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2)