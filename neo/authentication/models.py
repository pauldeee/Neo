from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    robinhood_email = models.CharField(max_length=255, blank=True)
    robinhood_password = models.CharField(max_length=255, blank=True)
