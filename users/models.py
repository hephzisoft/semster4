from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True,)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name