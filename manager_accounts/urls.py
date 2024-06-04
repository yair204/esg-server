# manager_signup/urls.py
from django.urls import path
from .views import manager_signup

urlpatterns = [
    path('signup/', manager_signup, name='manager_signup'),
]
