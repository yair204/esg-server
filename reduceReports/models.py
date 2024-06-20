from django.db import models

class ReduceReport(models.Model):
    company_name = models.CharField(max_length=100, unique=False)
    date = models.DateField()
    electricity = models.FloatField()
    gas = models.FloatField()
    water = models.FloatField()
    electricity_cost = models.FloatField(default=0.0)
    gas_cost = models.FloatField(default=0.0)
    water_cost = models.FloatField(default=0.0)

    def __str__(self):
        return self.company_name
