from django.db import models

class ReduceReport(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    electricity = models.FloatField()
    gas = models.FloatField()
    water = models.FloatField()

    def __str__(self):
        return self.company_name
