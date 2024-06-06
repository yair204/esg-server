from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db.models import PointField  
from django.db import models

class RestaurantType(models.TextChoices):
    ITALIAN = 'italian', 'Italian'
    MEXICAN = 'mexican', 'Mexican'
    PIZZA  = 'pizza', 'Pizza'
    FLESHY = 'fleshy', 'Fleshy'
    DAIRY = 'dairy', 'Dairy'

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    coordinates = PointField(blank=True, null=True)   
    phone = models.CharField(max_length=20, blank=True)
    type = models.CharField(max_length=50, choices=RestaurantType.choices)  
    open_hour = models.TimeField(blank=True, null=True)
    close_hour = models.TimeField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

