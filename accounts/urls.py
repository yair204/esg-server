from django.urls import path
from .views import RegisterUser, UserDetail, UserByEmailAndPassword

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('users/<uuid:pk>/', UserDetail.as_view(), name='user-detail'),
    path('users/authenticate/', UserByEmailAndPassword.as_view(), name='authenticate'),
]
