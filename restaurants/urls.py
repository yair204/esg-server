from django.urls import path
from .views import RestaurantList ,RegisterRestaurant

urlpatterns = [
    path('list/', RestaurantList.as_view(), name='restaurant-list'),
    path('register/', RegisterRestaurant.as_view(), name='register-restaurant'),

]
