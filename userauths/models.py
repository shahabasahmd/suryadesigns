from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=50, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']  

    def __str__(self):
        return self.username

