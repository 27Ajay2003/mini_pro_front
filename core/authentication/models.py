from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=255, primary_key=True)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255)

    # languages = models.CharField(max_length=5000)
    # frameworks = models.CharField(max_length=5000)
    # databases = models.CharField(max_length=5000)
    skills = models.CharField(max_length=5000)

    def __str__(self):
        return self.username
