# # accounts/models.py
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# import uuid

# class User(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
