# manager_signup/urls.py
from django.urls import path
from .views import manager_signup ,ManagerDetail

urlpatterns = [
    path('signup/', manager_signup, name='manager_signup'),
    path('details/<uuid:pk>/', ManagerDetail.as_view(), name='manager-detail'),

]
