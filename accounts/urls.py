from django.urls import path
from .views import RegisterUser, UserByEmailAndPassword

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('users/authenticate/', UserByEmailAndPassword.as_view(), name='authenticate'),
]
