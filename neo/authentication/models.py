from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    EXCHANGES = (('coinbase', 'Coinbase'), ("robinhood", 'Robinhood'))

    exchange = models.CharField(max_length=50, blank=True, choices=EXCHANGES)
    api_key = models.CharField(max_length=255, blank=True)
    api_secret = models.CharField(max_length=255, blank=True)
