from django.db import models


# Create your models here.

class TimeFrames(models.TextChoices):
    MIN_1 = "1m"
    HOUR_1 = "1h"
    DAY_1 = "1d"


class Exchanges(models.TextChoices):
    COINBASE = 'coinbase'
    KRAKEN = 'kraken'
    ROBINHOOD = 'robinhood'


class Account(models.Model):
    # api for accessing account
    exchange = models.CharField(max_length=255, choices=Exchanges.choices)
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)

    pass


class TradingBot(models.Model):
    pass


class Order(models.Model):
    class Status(models.TextChoices):
        OPEN = 'open'
        CLOSED = 'closed'
        CANCELED = 'canceled'
        EXPIRED = 'expired'
        REJECTED = 'rejected'
        NOT_MIN_NOTIONAL = 'not min notional'

    class Type(models.TextChoices):
        # maybe do stop loss?
        MARKET = 'market'
        LIMIT = 'limit'


class Backtesting(models.Model):
    pass
