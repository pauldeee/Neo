from django.db import models


# Create your models here.

class Exchange(models.Model):
    EXCHANGES = (("binanceus", 'BinanceUS'), ("coinbase", 'Coinbase'), ("kraken", 'Kraken'), ("robinhood", 'Robinhood'))

    exchange = models.CharField(max_length=50, blank=True, choices=EXCHANGES)
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255)
