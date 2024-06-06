from rest_framework import serializers
from .models import Restaurant, RestaurantType

class RestaurantTypeSerializer(serializers.ChoiceField):
     def to_representation(self, value):
        if isinstance(value, str):
            return value
        return value.label

class RestaurantSerializer(serializers.ModelSerializer):
    type = RestaurantTypeSerializer(choices=RestaurantType.choices)

    class Meta:
        model = Restaurant
        fields = '__all__'  

