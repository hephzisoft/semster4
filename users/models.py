from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name