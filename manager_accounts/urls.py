# manager_signup/urls.py
from django.urls import path
from .views import manager_signup ,ManagerDetail ,login,login_page

urlpatterns = [
    path('signup/', manager_signup, name='manager_signup'),
    path('details/<uuid:pk>/', ManagerDetail.as_view(), name='manager-detail'),
    path('login/', login, name='login'),
    path('login_page/', login_page, name='login_page'),


]
